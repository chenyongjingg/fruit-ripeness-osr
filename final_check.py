#!/usr/bin/env python3
"""Acceptance checks for the unattended run. Prints PASS/FAIL lines and a final count.

Every check is written so that it can FAIL. A check that can never fail is not evidence:
each one names the object it reads and the property it asserts, and prints the observed
value next to the verdict.
"""
import json, glob, os, re, sys, time
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import OUT, RESULTS, PROC, RAW, sha256_file

RES = []


def ck(name, ok, detail=""):
    RES.append((name, bool(ok), detail))
    print(("PASS %-46s %s" % (name, detail)) if ok else ("FAIL %-46s %s" % (name, detail)))


def read(p):
    with open(p) as f:
        return json.load(f)


def main():
    # 1. dataset cards: zero group leakage, and the card is the one the features were built from
    cards = sorted(PROC.glob("*/card.json"))
    ck("cards exist", len(cards) >= 4, "n=%d" % len(cards))
    bad = [(read(c)["dataset"], read(c)["group_leak_count"]) for c in cards if read(c)["group_leak_count"] != 0]
    ck("group_leak_count == 0 everywhere", not bad, str(bad))

    # 1b. Every raw archive on disk has a prepared card. stage_prepare catches its own
    # exceptions and only logs them, so a prepare that dies (truncated upload, unknown
    # layout) leaves the rest of the pipeline green while that dataset contributes
    # exactly nothing - the failure mode this check exists to surface.
    raw_sets = sorted({p.parent.name for p in RAW.glob("*/*")
                       if p.name in ("data.zip", "data.parquet", "train.parquet")})
    unprepared = [d for d in raw_sets if not (PROC / d / "card.json").exists()]
    ck("every raw dataset prepared", bool(raw_sets) and not unprepared,
       "raw=%s unprepared=%s" % (raw_sets, unprepared))

    mc = OUT / "master.csv"
    if not mc.exists():
        ck("master.csv exists", False, str(mc))
        return finish()
    df = pd.read_csv(mc)
    ck("master.csv non-trivial", len(df) > 3000, "rows=%d" % len(df))

    # 2. every planned arm is present
    for exp, n in [("E1", 1000), ("E2", 900), ("E3", 100), ("E1ft", 20), ("E1lora", 20)]:
        c = int((df["exp"] == exp).sum())
        ck("arm %s present" % exp, c >= n, "runs=%d (>=%d)" % (c, n))
    b1 = int(df["exp"].astype(str).str.startswith("B1").sum())
    b2 = int(df["exp"].astype(str).str.startswith("B2").sum())
    ck("CLIP baselines", b1 >= 7, "runs=%d" % b1)
    ck("Qwen zero-shot baselines", b2 >= 7, "runs=%d" % b2)
    # Baselines must be scored on THIS view's classes only. `_cap` samples per label, so
    # an unfiltered test split let other fruits' classes through (field4_banana was
    # evaluated on 240 rows, half mango). The signature is n_test above the cap.
    for pat, lim in (("B1_*", 410), ("B2_*", 130)):
        over = []
        for f in glob.glob(str(RESULTS / (pat + ".json"))):
            r = read(f)
            nt = r.get("metrics", {}).get("n_test")
            if nt is not None and nt > lim:
                over.append((os.path.basename(f), nt))
        ck("%s test size within cap" % pat, not over, "over-cap=%s" % (over[:3],))

    # 2b. the datasets added for the plan's extension layer and the multi-species P2 must
    # have produced runs, not merely a card. A prepared dataset with zero runs is the same
    # silent no-op one level further down.
    mh = df[(df["dataset"].astype(str) == "mango_khir") & (df["exp"].astype(str).str.startswith("E1"))]
    ck("mango_khir has E1 runs", len(mh) >= 10, "runs=%d (>=10)" % len(mh))
    e2f = df[df["protocol"].astype(str) == "P2_leave_one_fruit"]
    held = sorted(set(e2f["view"].astype(str).str.replace("fruits360_x_", "", regex=False)))
    ck("leave-one-fruit-out present", len(held) >= 4,
       "held=%s runs=%d" % (held, len(e2f)))
    # The plan's P3 has two halves. Decay comes from Fruits Fresh and Rotten (added
    # 2026-11-08) as well as from the sets that carry a rotten grade; foreign matter is
    # the cross-dataset arm. A prepared dataset with no runs is a silent no-op, so both
    # halves are asserted separately.
    ffr_r = df[(df["dataset"].astype(str) == "ffr") & (df["protocol"].astype(str) == "P3_rotten")]
    ck("ffr has P3_rotten runs", len(ffr_r) >= 8,
       "runs=%d encoders=%s" % (len(ffr_r), sorted(set(ffr_r["encoder"].astype(str)))))
    f360r = df[(df["dataset"].astype(str) == "f360rot") & (df["protocol"].astype(str) == "P3_rotten")]
    ck("Fruits-360 rotten class arm present", len(f360r) >= 8,
       "runs=%d encoders=%s" % (len(f360r), sorted(set(f360r["encoder"].astype(str)))))
    fx = df[df["protocol"].astype(str) == "P3_foreign"]
    ck("P3 foreign-matter arm present", len(fx) >= 100,
       "runs=%d known_views=%s" % (len(fx), sorted(set(fx["view"].dropna().astype(str)))))

    # 2c. per-class AP (the plan's long-tail closed-set metric). E1 stores hard predictions
    # only, so AP needs its own arm (exp = E1ap); a missing T2b means that arm produced
    # nothing and the plan's metric list is silently short one entry.
    t2b = OUT / "T2b_per_class_ap.csv"
    if t2b.exists():
        d2b = pd.read_csv(t2b)
        ck("per-class AP arm present", len(d2b) >= 100,
           "rows=%d views=%d" % (len(d2b), d2b["view"].nunique()))
    else:
        ck("per-class AP arm present", False, "T2b_per_class_ap.csv missing -> run ap_extra.py")

    # 2c2. the plan's weighted macro-F1 (adjacent error 1, skipped grade 2). Its own arm
    # because E1 keeps hard predictions only; and its own check because a metric whose
    # arm exists but whose numbers were produced by a different pipeline is worse than a
    # missing one -- hence the E1ORD cross-check file, which must exist and report 0
    # mismatches over a non-zero number of paired cells.
    eord = df[df["exp"].astype(str) == "E1ord"] if len(df) else df
    ck("ordinal cost-F1 arm present", len(eord) >= 300,
       "runs=%d views=%d" % (len(eord), eord["view"].nunique() if len(eord) else 0))
    xc = OUT / "E1ORD_XCHECK.txt"
    if xc.exists():
        import re as _re3
        t = xc.read_text(encoding="utf-8", errors="replace")
        m3 = _re3.search(r"pairs=(\d+) mismatches=(\d+)", t)
        ck("E1ord reproduces E1 (acc, macro-F1)", bool(m3) and int(m3.group(1)) > 0 and int(m3.group(2)) == 0,
           t.strip() if m3 else "no parseable summary")
    else:
        ck("E1ord reproduces E1 (acc, macro-F1)", False, "E1ORD_XCHECK.txt missing -> run ord_extra.py")

    # 2d. the plan's optional RQ3 tier (c): feature-level alignment. Same silent-no-op
    # argument as above -- a column that is never populated looks exactly like a tier that
    # was never run.
    if "align" in df.columns:
        e3bn = df[(df["exp"] == "E3") & (df["align"].astype(str) == "bn")]
        ck("E3 feature-alignment tier present", len(e3bn) >= 100,
           "runs=%d views=%s" % (len(e3bn), sorted(set(e3bn["view"].astype(str)))))
    else:
        ck("E3 feature-alignment tier present", False, "master.csv has no align column")

    # 2e. the plan's ordinal head (E4 ablation): the arm must exist AND the head must have
    # passed its own hand-computable checks -- an unvalidated ordinal head would produce a
    # plausible-looking column and a paragraph of interpretation behind it.
    corn = df[(df["exp"].astype(str) == "E1") & (df["head"].astype(str) == "corn")] if len(df) else df
    ck("ordinal (CORN) head arm present", len(corn) >= 100,
       "runs=%d views=%d" % (len(corn), corn["view"].nunique() if len(corn) else 0))
    cs = OUT / "METHODS_SELFTEST.txt"
    if cs.exists():
        t = cs.read_text(encoding="utf-8", errors="replace")
        import re as _re4
        m4 = _re4.search(r"checks: (\d+)", t)
        # "FAILURES: 0" alone is satisfied by an empty file with that one line; both named
        # checks must appear with PASS, so the verdict is tied to the objects it claims.
        both = ("corn: proba rows sum to 1: PASS" in t
                and "mahal: fast form agrees with the quadratic form (rel < 1e-5): PASS" in t)
        ck("instrument self-tests clean", bool(m4) and int(m4.group(1)) >= 8
           and _re4.search(r"FAILURES: 0\b", t) is not None and both,
           "checks=%s both_named=%s" % (m4.group(1) if m4 else "?", both))
    else:
        ck("instrument self-tests clean", False,
           "METHODS_SELFTEST.txt missing -> run test_methods.py")

    # 3. P2c (the plan's unseen-species protocol) is really in the results. The filter
    # uses the same honest name master.csv now carries; matching the old key here made
    # this check report runs=0 the moment the rename landed (a check pinned to the
    # defect rather than to the arm).
    p2c = df[(df["exp"] == "E2") & (df["protocol"] == "P2c_unseen_species")]
    views = sorted(set(p2c["view"].dropna().astype(str)))
    ck("P2c present", len(p2c) > 0 and len(views) == 3, "runs=%d views=%s" % (len(p2c), views))

    # 4. calibration arm: present, fitted on val, and NOT pooled into T3
    cal = df[(df["exp"] == "E2") & (df["calib"].notna())] if "calib" in df else pd.DataFrame()
    ck("calibration arm present", len(cal) > 0, "runs=%d" % len(cal))
    t3 = OUT / "T3_open_set.csv"
    if t3.exists():
        d3 = pd.read_csv(t3)
        ncal = int((df["exp"] == "E2").sum())
        nuncal = int(((df["exp"] == "E2") & (df["calib"].isna())).sum()) if "calib" in df else ncal
        ck("T3 excludes calibrated runs", int(d3["n_runs"].sum()) == nuncal,
           "sum(n_runs)=%d uncalibrated=%d" % (int(d3["n_runs"].sum()), nuncal))
    else:
        ck("T3 written", False, str(t3))
    t10 = OUT / "T10_calibration.csv"
    if t10.exists():
        d10 = pd.read_csv(t10)
        ck("T10 rows", len(d10) > 10, "rows=%d" % len(d10))
        has_src = "calib_src" in d10.columns
        ck("T10 records calibration source", has_src,
           ",".join(sorted(set(d10["calib_src"].dropna().astype(str)))) if has_src
           else "column missing -> T10 was written by an older report.py")
        if has_src:
            n_sup = int(d10["calib_src"].astype(str).str.contains("support").sum())
            ck("calibration not on support (except tiny views)", n_sup <= 5,
               "support-fitted rows=%d" % n_sup)
    else:
        ck("T10 written", False, str(t10))

    # 5. efficiency table has real measurements, not NaN
    t9 = OUT / "T9_efficiency.csv"
    if t9.exists():
        d9 = pd.read_csv(t9)
        enc = d9[d9["kind"] == "encoder"]
        ck("T9 encoders measured", len(enc) >= 4 and enc["latency_ms_b1"].notna().all() and (enc["latency_ms_b1"] > 0).all(),
           "; ".join("%s %.1fms" % (r["name"], r["latency_ms_b1"]) for _, r in enc.iterrows()))
        ck("T9 peakers", d9[d9["kind"] != "train_mem"]["params"].notna().all(), "rows=%d" % len(d9))
        # the plan's E5 also asks for TRAINING peak memory, which only the two end-to-end
        # arms can have. A missing probe leaves the plan's third quantity blank in Tab. 6
        # while the table still renders -- so it is asserted separately.
        tm = d9[d9["kind"] == "train_mem"]
        ck("T9 training-memory probe", len(tm) >= 1 and tm["peak_mem_mb_b32"].notna().all()
           and (tm["peak_mem_mb_b32"] > 0).all(),
           "; ".join("%s %.0fMB" % (r["name"], r["peak_mem_mb_b32"]) for _, r in tm.iterrows())
           if len(tm) else "no train_mem rows")
    else:
        ck("T9 written", False, str(t9))

    # 6. adapted arms: both fine-tuning and LoRA, both non-empty
    t7 = OUT / "T7_adapted.csv"
    if t7.exists():
        d7 = pd.read_csv(t7)
        exps = sorted(set(d7["exp"].astype(str)))
        ck("T7 has both adapted arms", set(exps) >= {"E1ft", "E1lora"}, str(exps))
    else:
        ck("T7 written", False, str(t7))

    # 7. the Qwen 5-shot records must post-date the prompt fix (2026-11-08T06:00Z)
    q5 = sorted(glob.glob(str(RESULTS / "B2_qwen_5shot__*.json")))
    old = []
    unr = []
    for f in q5:
        r = read(f)
        if str(r.get("finished_at", "")) < "2026-11-08T06:00:00":
            old.append(os.path.basename(f))
        u = r.get("metrics", {}).get("unparsed_rate")
        if u is not None and u > 0.5:
            unr.append((os.path.basename(f), round(float(u), 3)))
    ck("Qwen 5-shot recomputed after prompt fix", q5 and not old, "n=%d stale=%d %s" % (len(q5), len(old), old[:3]))
    ck("Qwen 5-shot parseable", not unr, "high-unparsed=%s" % (unr[:4],))

    # 8. negative controls actually collapse.
    #    Criterion is macro-F1 against 1/n_classes, NOT accuracy: the test splits are not
    #    class-balanced (fruit12_banana test is 67% Ripe), so a predictor that collapses
    #    to a single class gets acc = 0.673 there while its macro-F1 is 0.28. Judging the
    #    control by accuracy would fail a control that is in fact dead.
    ctl = df[(df["exp"] == "E1") & (df["control"].astype(str) != "none")]
    if len(ctl):
        # Closed-set views hold the DECAYED class out (it is the P3 unknown), so banana4
        # and fruit12_* are 3-class views even though the datasets have 4 grades. Using
        # the raw grade count here made chance 0.25 instead of 0.333 and manufactured a
        # +0.088 "excess" on a control that is in fact at chance.
        ncls = {"banana3": 3, "banana4": 3, "fruit12_apple": 3, "fruit12_banana": 3,
                "fruit12_mango": 3, "field4_banana": 2, "field4_mango": 2}
        ctl = ctl.copy()
        ctl["base"] = ctl["view"].map(ncls).fillna(3).rdiv(1.0)
        ctl["excess"] = ctl["macro_f1"] - ctl["base"]
        # Decision on the CELL MEAN, not on the max over ~84 runs: the max of 84 null
        # draws reaches 2-4 sigma by construction (observed +0.115 on one seed of a
        # random-feature control whose cell mean is below chance). The max is printed so
        # the reader can see it rather than have it hidden.
        means = ctl.groupby(["view", "control"])["excess"].mean()
        worst_cell = means.idxmax()
        ck("controls at chance (mean macro-F1)", means.max() < 0.05,
           "worst cell %s %s = %+.3f; single-run max = %+.3f"
           % (worst_cell[0], worst_cell[1], means.max(), ctl["excess"].max()))
    else:
        ck("controls present", False, "")

    # 9. report sections present and failures reported as a section
    rp = OUT / "REPORT.md"
    if rp.exists():
        txt = rp.read_text(encoding="utf-8", errors="replace")
        need = ["## Datasets", "## Closed-set few-shot", "## Open-set rejection", "## Cross-domain",
                "## Calibration arm", "## Adapted backbones", "## Zero-shot", "## Negative controls",
                "## Efficiency", "## Notes that must travel", "## Failures", "## Run inventory"]
        miss = [s for s in need if s not in txt]
        ck("REPORT sections", not miss, "missing=%s size=%dB" % (miss, len(txt)))
        # Was: assert the OLD (false) name is present -- a check that the defect passed.
        # The honest name is asserted in check 13, which also requires the old one gone.
        ck("REPORT reports the P2c arm", "P2c_unseen_species" in txt, "")
        import re as _re0
        m0 = _re0.search(r"unreadable result files: (\d+)", txt)
        ck("no unreadable result files", bool(m0) and int(m0.group(1)) == 0,
           m0.group(0) if m0 else "section missing")
    else:
        ck("REPORT.md exists", False, "")

    # 10. verify pass
    v = OUT / "VERIFY.md"
    if v.exists():
        t = v.read_text(encoding="utf-8", errors="replace")
        # The old criterion was just the substring "mismatches: 0", which a run that
        # verified nothing also printed. Require a non-zero number of arrays actually
        # resolved to their run JSON, and no unmatched files.
        import re as _re
        m = _re.search(r"(\d+) on disk, (\d+) resolved to their run JSON, (\d+) unmatched; "
                       r"metric mismatches: (\d+)", t)
        if m:
            n_disk, n_res, n_unm, n_mis = map(int, m.groups())
            ck("VERIFY resolved every score file", n_disk > 0 and n_res == n_disk and n_unm == 0,
               "disk=%d resolved=%d unmatched=%d" % (n_disk, n_res, n_unm))
            ck("VERIFY metric mismatches == 0", n_mis == 0 and n_res > 0, "mismatches=%d" % n_mis)
        else:
            ck("VERIFY format", False, "no parseable summary line")

    # 11. independent re-derivation (verify_indep.py) -- catches a wrong metric definition,
    # which report.verify() cannot, because it calls the same production code.
    iv = OUT / "VERIFY_INDEP.md"
    if iv.exists():
        t = iv.read_text(encoding="utf-8", errors="replace")
        import re as _re2
        m = _re2.search(r"checked: (\d+) arrays, unresolved: (\d+), violations: (\d+)", t)
        if m:
            n_chk, n_unr, n_vio = map(int, m.groups())
            ck("independent metrics: arrays checked > 0", n_chk > 0, "checked=%d" % n_chk)
            ck("independent metrics: no violations", n_vio == 0 and n_unr == 0,
               "unresolved=%d violations=%d" % (n_unr, n_vio))
        else:
            ck("VERIFY_INDEP format", False, "no parseable summary line")
    else:
        ck("VERIFY_INDEP.md exists", False, "")

    # 12. data provenance (plan fix #10). Two separate assertions, because "the seal
    # exists" and "the seal still matches the data" fail for different reasons.
    now = time.time()
    unsealed, sealed, drift = [], 0, []
    for f in glob.glob(str(RESULTS / "*.json")):
        try:
            r = read(f)
        except Exception:
            continue
        if r.get("seal"):
            sealed += 1
        elif now - os.path.getmtime(f) > 1800:
            # seal.py's own contract: anything younger than 30 min may still be being
            # written by a live stage, so only older files are evidence of a gap.
            unsealed.append(os.path.basename(f))
    ck("every result carries a data seal", not unsealed and sealed > 3000,
       "sealed=%d unsealed(>30min)=%d %s" % (sealed, len(unsealed), unsealed[:3]))
    for c in sorted(PROC.glob("*/card.json")):
        card = read(c)
        meta = c.parent / "meta.csv"
        if not meta.exists():
            continue
        live = sha256_file(meta)
        if card.get("meta_sha256") and card["meta_sha256"] != live:
            drift.append((c.parent.name, card["meta_sha256"][:12], live[:12]))
    ck("no card-vs-live data drift", not drift,
       "drift=%s" % (drift[:4],) if drift else "all %d datasets match" % len(list(PROC.glob("*/card.json"))))

    # 13. the honesty rename must have reached the OUTPUTS, not just the loader. The old
    # check asserted the false name was present; that was satisfied by a report that said
    # "P2c_unseen_cultivar" everywhere, i.e. by the defect.
    # A line may name the old key only to declare that it is the old key -- that is the
    # sentence the reader needs to connect our tables to the run ids. Every other use is
    # the defect, so the allowance is line-scoped and keyword-tied, not file-scoped.
    OK_CTX = ("renaming", "renamed", "internal", "still reads")
    bad_name = []
    for nm in ("REPORT.md", "T3_open_set.csv", "ANALYSIS_V2.md"):
        p = OUT / nm
        if not p.exists():
            continue
        hits = [ln for ln in p.read_text(encoding="utf-8", errors="replace").splitlines()
                if "P2c_unseen_cultivar" in ln and not any(k in ln for k in OK_CTX)]
        if hits:
            bad_name.append("%s:%d" % (nm, len(hits)))
    ck("no 'unseen_cultivar' in outputs", not bad_name, "found in %s" % bad_name if bad_name else "")
    rp2 = OUT / "REPORT.md"
    if rp2.exists():
        t = rp2.read_text(encoding="utf-8", errors="replace")
        ck("REPORT uses P2c_unseen_species", "P2c_unseen_species" in t, "")

    # 14. collapsed / thin cells (plan fixes #6 and §6). Both are claims the paper makes,
    # so both must be backed by a file that lists them; a missing file means the analysis
    # layer did not run and the "12 collapsed cells" sentence would be typing, not data.
    t15 = OUT / "T15_collapsed.csv"
    if t15.exists():
        d15 = pd.read_csv(t15)
        ck("T15 collapsed-cell list written", len(d15.columns) >= 4, "rows=%d" % len(d15))
        # Cross-check against master.csv: each listed run must carry the accuracy the
        # listing attributes to it. Guards against a stale T15 sitting next to a fresh
        # master. T15 keys on the run coordinates (it has no file column), so the merge
        # is on those and a missing match is itself a failure -- an inner join that
        # silently drops everything would make this check vacuous.
        keys = ["view", "encoder", "variant", "protocol", "unknown", "score", "shot", "seed"]
        if len(d15) and set(keys).issubset(d15.columns) and set(keys).issubset(df.columns):
            a = d15[keys + ["known_acc"]].copy()
            b = df[keys + ["known_acc"]].copy()
            for t in (a, b):
                t["shot"] = pd.to_numeric(t["shot"], errors="coerce").fillna(-1)
                t["seed"] = pd.to_numeric(t["seed"], errors="coerce").fillna(-1)
            j = a.merge(b, on=keys, how="left", suffixes=("", "_master"))
            n_missing = int(j["known_acc_master"].isna().sum())
            gap = float((j["known_acc_master"] - j["known_acc"]).abs().max()) if n_missing < len(j) else np.inf
            ck("T15 agrees with master.csv", n_missing == 0 and gap < 1e-9,
               "matched=%d/%d max|gap|=%.2e" % (len(j) - n_missing, len(j), gap))
        else:
            ck("T15 agrees with master.csv", False, "key columns missing in T15 or master.csv")
    else:
        ck("T15 collapsed-cell list written", False, "T15_collapsed.csv missing -> run analyze_v2.py")
    t16 = OUT / "T16_small_n.csv"
    ck("T16 thin-cell list written", t16.exists(),
       "rows=%d" % len(pd.read_csv(t16)) if t16.exists() else "missing -> run analyze_v2.py")

    # 15. the analysis layer itself (T11..T16) must be on disk and non-empty. Without it
    # three of the plan's five replacement claims have no artifact behind them.
    av = OUT / "ANALYSIS_V2.md"
    if av.exists():
        t = av.read_text(encoding="utf-8", errors="replace")
        need = ["T11_auroc_by_arm", "T11b_auroc_by_arm_score", "T12_family_flip",
                "T13_score_corr", "T14_adjacent",
                "T14b_granularity", "T15_collapsed", "T16_small_n"]
        miss = [s for s in need if s not in t]
        ck("ANALYSIS_V2 tables present", not miss, "missing=%s size=%dB" % (miss, len(t)))
        t13p = OUT / "T13_score_corr.csv"
        if t13p.exists():
            d13 = pd.read_csv(t13p)
            sel = d13[(d13["score_a"] == "msp") & (d13["score_b"] == "energy")
                      & (d13["subset"] == "known=2")]
            ok = len(sel) == 1 and float(sel["spearman"].iloc[0]) == 1.0 \
                and float(sel["frac_identical"].iloc[0]) == 1.0
            ck("MSP==Energy exactly on 2-class cells", ok,
               "row=%s" % (sel[["n_cells", "spearman", "frac_identical"]].to_dict("records")
                           if len(sel) else "missing"))
        else:
            ck("MSP==Energy exactly on 2-class cells", False, "T13_score_corr.csv missing")
    else:
        ck("ANALYSIS_V2 tables present", False, "ANALYSIS_V2.md missing -> run analyze_v2.py")

    # 16. plan v2.0 week-3 figures, and the NinePeach card's honesty fields. The plan row
    # claims "3,849 images, 9 cultivars"; the archive has 1,245 images and no cultivar
    # field. The card has to SAY that, and the check has to read it back, otherwise the
    # correction lives only in a chat message.
    for f in ("fig_v2_arms.pdf", "fig_v2_flip.pdf"):
        p = OUT / "figures" / f
        ck("plan-v2 figure %s" % f, p.exists() and p.stat().st_size > 1000,
           "%dB" % (p.stat().st_size if p.exists() else 0))
    np_card = PROC / "ninepeach" / "card.json"
    np_zip = RAW / "ninepeach" / "Peach_maturity_dataset.zip"
    if np_card.exists():
        c = read(np_card)
        ok = (bool(c.get("plan_claim_vs_archive"))
              and "1,245" in str(c.get("plan_claim_vs_archive"))
              and c.get("group_leak_count") == 0
              and c.get("unit", "").startswith("annotated peach instance"))
        ck("NinePeach card records plan-vs-archive discrepancy", ok,
           "n_images=%s leak=%s" % (c.get("n_images"), c.get("group_leak_count")))
        # The archive itself has to have been CHECKED, not merely present: a truncated or
        # corrupted 8.8 GB download still builds a card. np_verify.py measures size + md5
        # and reads the counts straight out of the zip; this reads its report back and
        # cross-checks the box count against the card, so the two artefacts cannot drift
        # apart silently.
        np_md = OUT / "NINEPEACH_VERIFY.md"
        txt = np_md.read_text(encoding="utf-8") if np_md.exists() else ""
        m = re.search(r"\|\s*annotated boxes\s*\|\s*(\d+)\s*\|", txt)
        boxes_md = int(m.group(1)) if m else None
        boxes_card = c.get("n_boxes_in_annotations")
        ck("NinePeach archive verified (size + md5) and the counts agree with the card",
           bool(txt) and "MISMATCH" not in txt and boxes_md is not None
           and boxes_card is not None and boxes_md == int(boxes_card),
           "file=%s boxes_in_report=%s boxes_in_card=%s" % (np_md.exists(), boxes_md, boxes_card))
    elif np_zip.exists():
        ck("NinePeach card present", False,
           "archive downloaded but no card -> run build_ninepeach")
    else:
        # The plan's own §4.4 fallback: a failed acquisition downgrades the claim set, it
        # does not fail the run. What must NOT happen is a card that pretends otherwise,
        # which the branch above would catch.
        ck("NinePeach not acquired (plan §4.4 fallback)", True,
           "zip absent -> cultivar arm stays unavailable and must be listed as a limitation")
    finish()


def finish():
    n = sum(1 for _, ok, _ in RES if ok)
    print("\nPASSED %d / %d" % (n, len(RES)))
    print("FAILURES: %d" % (len(RES) - n))
    for name, ok, d in RES:
        if not ok:
            print("  - %s  %s" % (name, d))
    return 0 if n == len(RES) else 1


if __name__ == "__main__":
    sys.exit(main())
