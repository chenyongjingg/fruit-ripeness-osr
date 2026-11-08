#!/usr/bin/env python3
"""Backfill the data seal (plan v2.0 fix #10) into results written before it existed.

Why this is a separate pass and not a recompute: 10,277 result files were written with
no record of the data they came from. `rio.experiments.save_result` now stores a `seal`
block with every new result, and `already()` refuses to reuse a result whose seal no
longer matches the live data. This script derives the same block for the pre-existing
files from (config + card.json + the live meta.csv) and marks them `seal_source: derived`.

The honest limitation, stated in the report it writes: for a legacy file we cannot know
WHICH version of meta.csv it actually ran on. The derived `meta_sha256_live` is the file
as it stands today. So a derived seal says "this result is consistent with today's data",
not "it was produced from today's data". The card-vs-live drift column is what separates
the two: a non-zero drift means the dataset changed after the card was written, and every
legacy result on that dataset is suspect.

Usage:  python3 seal.py [--dry-run] [--limit N]
"""
import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rio.common import (ROOT, PROC, RESULTS, OUT, read_json, sha256_file,
                        atomic_write_json, CODE_VERSION)

MARKER = ROOT / "cache" / ".seal_marker"

# The three ordinal grades every P2c (unseen species) run is scored against -- the
# default of experiments.e2_cultivar.
P2C_GRADES = ["unripe", "ripe", "overripe"]


def _views():
    """The view table, imported lazily: run.py reads processed meta files at import."""
    import run
    return run.views()


def _e3_label_sets(V):
    """Mirror of stage_e3's `pairs` -> {tag: sorted(source labels)}.

    Duplicated here on purpose: the seal must be derivable from what a run file
    *contains* and what the view table *defines*, not from a call stack that no longer
    exists. If stage_e3's pairs change, this map changes with them and `already()`
    reports drift -- which is the point.
    """
    m = {}
    if "fruit12_mango" in V and "field4_mango" in V:
        o = V["fruit12_mango"]["ordinal"]
        m["mango"] = sorted({o[0], o[1]})
    if "fruit12_banana" in V and "field4_banana" in V:
        o = V["fruit12_banana"]["ordinal"]
        m["banana"] = sorted({o[0], o[1]})
    if "banana3" in V and "banana4" in V:
        m["b3->b4"] = ["overripe", "ripe", "unripe"]
        m["b4->b3"] = ["overripe", "ripe", "unripe"]
    return m


def _first_token_counts(ds):
    """label -> (species first token) for the Fruits-360 style multi-species sets."""
    import pandas as pd
    p = PROC / ds / "meta.csv"
    if not p.exists():
        return None, None
    lab = pd.read_csv(p)["label_name"].astype(str)
    return lab, lab.str.split().str[0]


def _known_of_leave_one_fruit(ds, held):
    lab, fruit = _first_token_counts(ds)
    if lab is None:
        return None
    return sorted(set(lab[fruit != held]))


def derive_seal(cfg, V, e3map):
    """Return (seal, ds_used, why_not) for one result config."""
    exp = cfg.get("exp")
    view = cfg.get("view")
    proto = cfg.get("protocol")
    ds = cfg.get("dataset")
    ordinal, known, ds_used, why = None, None, None, ""

    if exp == "E1":
        ds_used = ds
        v = V.get(view)
        if v:
            ordinal = list(v["ordinal"])
        else:
            why = "view not in view table"
    elif exp == "E2":
        if proto in ("P1_out_of_grade", "P2_unseen_interior", "P3_rotten"):
            ds_used = ds
            v = V.get(view)
            if v:
                ordinal = list(v["ordinal"])
            else:
                why = "view not in view table"
        elif proto == "P2c_unseen_cultivar":
            ds_used = ds
            ordinal = list(P2C_GRADES)
        elif proto == "P2_leave_one_fruit":
            ds_used = ds
            held = (cfg.get("unknown") or [None])[0]
            known = _known_of_leave_one_fruit(ds, held)
            why = "classes are dataset indices, not grades: ordinal not asserted"
        elif proto == "P3_foreign":
            ds_used = str(ds).split("<-foreign:")[0]
            known = list(cfg.get("known") or [])
            why = "known side are class names, not grades: ordinal not asserted"
        else:
            ds_used = str(ds).split("->")[0] if ds else None
            why = "unknown protocol"
    elif exp == "E3":
        ds_used = str(ds).split("->")[0]
        ordinal = e3map.get(view)
        if ordinal is None:
            why = "E3 tag not in reproduction map"
    else:
        # E1ap / E1ord / E1ft / E1lora / B1 / B2 all share one shape: a single dataset, a
        # view key from the same table. Their ordinal set is whatever that view defines,
        # so the seal is derivable for them too -- no reason to record "unknown".
        v = V.get(view)
        if v and isinstance(ds, str) and "->" not in ds and "<-foreign:" not in ds:
            ds_used = ds
            ordinal = list(v["ordinal"])
        else:
            why = "unknown exp"

    card_p = PROC / ds_used / "card.json" if ds_used else None
    card = read_json(card_p) if (card_p and card_p.exists()) else {}
    meta_p = PROC / ds_used / "meta.csv" if ds_used else None
    seal = {"view": None if view is None else str(view),
            "ordinal": None if ordinal is None else [str(x) for x in ordinal],
            "known": None if known is None else sorted(str(x) for x in known),
            "meta_sha256": card.get("meta_sha256"),
            "meta_sha256_live": sha256_file(meta_p) if (meta_p and meta_p.exists()) else None,
            "code_version": CODE_VERSION,
            "seal_source": "derived",
            "derived_from": "config+card+live meta.csv"}
    return seal, ds_used, why


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    # A background stage may be writing results while this runs. Reading and rewriting a
    # file another process is about to replace is a lost-update race, so anything touched
    # in the last N minutes is left for a later pass; new results carry their own seal.
    ap.add_argument("--min-age-min", type=float, default=30.0)
    # Incremental by default: after the first full pass, only files touched since the
    # marker are examined, so putting this in the 15-minute driver loop costs nothing
    # until a new result appears. `--full` re-derives everything (use it after a change
    # to the view table, which is exactly when old seals must be invalidated).
    ap.add_argument("--full", action="store_true")
    a = ap.parse_args()

    V = _views()
    e3map = _e3_label_sets(V)
    import time
    cutoff = time.time() - a.min_age_min * 60.0
    all_files = sorted(RESULTS.glob("*.json"))
    marker = MARKER
    floor = 0.0
    if marker.exists() and not a.full:
        floor = marker.stat().st_mtime - 2.0
    files = [p for p in all_files if floor < p.stat().st_mtime < cutoff]
    if a.limit:
        files = files[: a.limit]

    stats = Counter()
    stats["skipped_recent"] = sum(1 for p in all_files if p.stat().st_mtime >= cutoff)
    stats["skipped_sealed_earlier"] = sum(1 for p in all_files if p.stat().st_mtime <= floor)
    if not files and not a.dry_run:
        print("nothing new since the last pass (%d files skipped); marker kept" %
              (len(all_files) - len(files)))
        atomic_write_json(marker, {"at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                   "n_files_seen": len(all_files), "incremental": True})
        return
    per_proto = defaultdict(Counter)
    drift = defaultdict(list)          # ds -> [(file, card, live)]
    noreason = Counter()
    out_rows = []

    for p in files:
        try:
            rec = read_json(p)
        except Exception as e:
            stats["unreadable"] += 1
            noreason["unreadable json"] += 1
            continue
        cfg = rec.get("config") or {}
        proto = cfg.get("protocol") or cfg.get("exp") or "?"
        if rec.get("seal") and rec["seal"].get("seal_source") != "derived":
            stats["already_sealed"] += 1
            per_proto[proto]["already_sealed"] += 1
            continue
        seal, ds_used, why = derive_seal(cfg, V, e3map)
        if seal["meta_sha256"] and seal["meta_sha256_live"] and \
                seal["meta_sha256"] != seal["meta_sha256_live"]:
            drift[ds_used].append((p.name, seal["meta_sha256"], seal["meta_sha256_live"]))
        if why:
            noreason[why] += 1
        if seal["ordinal"] is None:
            stats["ordinal_null"] += 1
            per_proto[proto]["ordinal_null"] += 1
        else:
            per_proto[proto]["ordinal_set"] += 1
        if not a.dry_run:
            rec["seal"] = seal
            atomic_write_json(p, rec)
        stats["backfilled"] += 1
        out_rows.append((p.name, proto, ds_used, seal["ordinal"] is not None))

    lines = ["# Seal backfill report", "",
             "Generated by `seal.py` (`--dry-run` = %s) over %d result files." % (a.dry_run, len(files)),
             "", "## Counts", ""]
    for k in ("backfilled", "already_sealed", "ordinal_null", "unreadable", "skipped_recent",
              "skipped_sealed_earlier"):
        lines.append("- %s: %d" % (k, stats[k]))

    lines += ["", "## By protocol", "", "| protocol | ordinal set | ordinal null | already sealed |",
              "|---|---|---|---|"]
    for proto in sorted(per_proto):
        c = per_proto[proto]
        lines.append("| %s | %d | %d | %d |" % (proto, c["ordinal_set"], c["ordinal_null"],
                                                 c["already_sealed"]))

    lines += ["", "## Card vs live meta.csv drift", ""]
    if not drift:
        lines.append("None: every dataset's card.json meta_sha256 equals the live meta.csv hash.")
    else:
        lines.append("A non-zero entry means the dataset changed after its card was written; "
                     "every legacy result on it is suspect (its derived seal only says it is "
                     "consistent with the CURRENT file, not that it ran on it).")
        lines.append("")
        lines.append("| dataset | result files | card meta_sha256 | live meta.csv sha256 |")
        lines.append("|---|---|---|---|")
        for d, rows in sorted(drift.items()):
            lines.append("| %s | %d | `%s` | `%s` |" % (d, len(rows), rows[0][1][:16], rows[0][2][:16]))
        lines.append("")
        lines.append("Affected files: " + ", ".join(sorted(r[0] for rows in drift.values() for r in rows)[:40])
                     + (" ..." if sum(len(v) for v in drift.values()) > 40 else ""))

    if noreason:
        lines += ["", "## Keys not asserted (why)", ""]
        for why, n in noreason.most_common():
            lines.append("- %s: %d" % (why, n))

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "SEAL_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if not a.dry_run:
        atomic_write_json(marker, {"at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                   "n_files_seen": len(all_files), "backfilled": stats["backfilled"],
                                   "incremental": floor > 0})
    print("\n".join(lines))
    print("\nwrote", OUT / "SEAL_REPORT.md")


if __name__ == "__main__":
    main()
