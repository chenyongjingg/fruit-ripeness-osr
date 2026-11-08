#!/usr/bin/env python3
"""Plan v2.0 analyses that can be computed from already-stored score arrays.

Everything here is read-only with respect to `results/`: it reads the E2 JSONs and the
`results/scores/*.npz` arrays and writes only into `outputs/`.

What it produces (and why each one exists):

  T11_auroc_by_arm      Plan 5.4 #1: AUROC per protocol arm x score family. Answers
                        "how hard is each kind of unknown", which is the paper's first
                        empirical finding.
  T11b_auroc_by_arm_score
                        The same cells keyed on the individual score, because the plan
                        quotes per-score numbers ("all four scores ~0.65") that a family
                        mean cannot check.
  T12_family_flip       Plan 5.4 #2: AUROC of each family split by WHERE the hidden
                        grade sits in the ordinal scale. The plan's claim is that the
                        better family flips with the hidden level; this table is the
                        evidence, so it must be produced by code, not by hand.
  T13_score_corr        Plan 5.4 #3: cell-level rank correlation between scores. If
                        msp~energy and mahalanobis~kNN are ~0.99 while cross-family is
                        ~0.5, then "four scores" is really "two families".
  T14_adjacent          Plan 5.2 #5: adjacent-vs-distant rejection rates, per family and
                        per protocol, with the sign count. The point is to show the
                        direction is family-dependent (i.e. NOT a universal finding).
  T14b_granularity      Plan 5.3: the adjacent-vs-distant gap as a function of HOW MANY
                        grades the view has (3 / 4 / 5). One row per level count, so the
                        "does granularity make rejection harder" question is answered by a
                        table instead of a hand-drawn curve.
  T15_collapsed         Plan 5.2 #6 / 6: known-side cells where the argmax collapses to
                        one class. Their known_acc equals the majority share, and any
                        open-set number from them is an artefact.
  T16_small_n           Plan 5.2 #6: cells with fewer than n_min test images on either
                        side, plus a seed bootstrap CI on AUROC so a reader can see how
                        wide the interval is where the point estimate is thin.

Definitions that travel with the numbers:

  * family: prob = {msp, energy}; dist = {mahalanobis, knn}. The split is the plan's,
    not ours -- see T13 for the empirical justification.
  * a "cell" is one (view, encoder, variant, protocol, unknown-grade, shot) group; the
    per-cell statistic is the mean over seeds, and every table reports n_cells and
    n_runs so a mean cannot be read as if it rested on many independent cells.
  * the adjacent/distant split uses the ORIGINAL ordinal index of each label, so hiding
    a middle grade leaves a gap that is measured, not closed up.
  * rejection at a fixed operating point uses the stored `threshold_fpr5` (the same
    threshold the reported CCR@5% uses), never a re-tuned one.

Usage:  python3 analyze_v2.py [--n-min 30] [--bootstrap 2000]
"""
import argparse
import glob
import itertools
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import RESULTS, OUT, PROC, read_json, display_view  # noqa: E402

PROB = {"msp", "energy"}
DIST = {"mahalanobis", "knn"}
ARMS = {
    "P1_out_of_grade": "P1 terminal level out-of-grade",
    "P2_unseen_interior": "P2 unseen grade (incl. first)",
    "P3_rotten": "P3a decayed class",
    "P3_foreign": "P3b cross-dataset foreign fruit",
    "P2f_leave_one_fruit": "P2 leave-one-fruit-out (Fruits-360)",
    "P2c_unseen_species": "P2 leave-one-species-out (fruit12; species, NOT cultivar)",
}


def family(score):
    if score in PROB:
        return "prob"
    if score in DIST:
        return "dist"
    return "other"


def load_e2():
    """One record per uncalibrated E2 run, with the arm it belongs to."""
    rows = []
    for p in sorted(RESULTS.glob("E2__*.json")):
        try:
            r = read_json(p)
        except Exception:
            continue
        c, m = r.get("config", {}), r.get("metrics", {})
        if c.get("calib"):
            continue                      # the calibration arm duplicates the scores
        proto = c.get("protocol")
        if proto == "P3_foreign":
            arm = "P3_foreign"
        elif proto in ARMS:
            arm = proto
        elif proto and proto.startswith("P2f"):
            arm = "P2f_leave_one_fruit"
        else:
            arm = proto or "unknown"
        arm = display_view(arm)
        rows.append({
            "file": p.name, "run_id": p.stem.split("__")[-1],
            "arm": arm, "protocol": proto,
            "view": display_view(c.get("view")), "dataset": c.get("dataset"),
            "encoder": c.get("encoder"), "variant": c.get("variant"),
            "score": c.get("score"), "family": family(c.get("score")),
            "shot": c.get("shot"), "seed": c.get("seed"),
            "unknown": "|".join(c.get("unknown") or []),
            "auroc": m.get("auroc"), "oscr": m.get("oscr"),
            "fpr95": m.get("fpr95"), "known_acc": m.get("known_acc"),
            "n_known": m.get("n_known_test", m.get("n_known")),
            "n_unknown": m.get("n_unknown_test", m.get("n_unknown")),
            "threshold_fpr5": m.get("threshold_fpr5"),
            "ccr_at_fpr5": m.get("ccr_at_fpr5"),
        })
    d = pd.DataFrame(rows)
    for col in ("auroc", "oscr", "fpr95", "known_acc", "n_known", "n_unknown",
                "threshold_fpr5", "ccr_at_fpr5", "shot", "seed"):
        if col in d.columns:
            d[col] = pd.to_numeric(d[col], errors="coerce")
    return d


def t11_by_arm(df):
    d = df[df["auroc"].notna()]
    if not len(d):
        return None
    g = d.groupby(["arm", "family"], dropna=False)
    out = g.apply(lambda x: pd.Series({
        "n_cells": x.groupby(["view", "encoder", "variant", "protocol", "unknown", "shot"]).ngroups,
        "n_runs": len(x),
        "auroc_mean": x["auroc"].mean(),
        "auroc_sd": x["auroc"].std(ddof=1),
        "oscr_mean": x["oscr"].mean(),
        "fpr95_mean": x["fpr95"].mean(),
    })).reset_index()
    out["arm_desc"] = out["arm"].map(ARMS).fillna(out["arm"])
    return out.sort_values(["arm", "family"])


def t11b_by_arm_score(df):
    """The same cells as T11, keyed on the individual score instead of the family.

    Why it has to exist: the plan's C4(a) quotes "all four scores ≈0.65" for the P2 arm,
    and a family MEAN cannot check a per-score claim -- prob = {msp, energy} averaging to
    0.65 is also what 0.58 and 0.72 average to. A reader who wants to reproduce the
    plan's number needs the per-score row, so it gets its own table.
    """
    d = df[df["auroc"].notna()]
    if not len(d):
        return None
    out = d.groupby(["arm", "score"], dropna=False).apply(lambda x: pd.Series({
        "n_cells": x.groupby(["view", "encoder", "variant", "protocol", "unknown", "shot"]).ngroups,
        "n_runs": len(x),
        "auroc_mean": x["auroc"].mean(),
        "auroc_sd": x["auroc"].std(ddof=1),
        "auroc_min": x["auroc"].min(),
        "auroc_max": x["auroc"].max(),
    })).reset_index()
    out["arm_desc"] = out["arm"].map(ARMS).fillna(out["arm"])
    return out.sort_values(["arm", "score"])


def _ordinal_index_map():
    """view -> {label: index in the view's full ordinal list} from the live definitions.

    Read from run.views() rather than from the results, because that is the only place
    the ordinal order exists at all; when it disagrees with a stored `unknown` grade the
    cell is skipped rather than guessed.
    """
    import run
    return {k: {str(l): i for i, l in enumerate(v["ordinal"])}
            for k, v in run.views().items()}


def t12_family_flip(df, ordmap):
    d = df[(df["arm"].isin(["P1_out_of_grade", "P2_unseen_interior"])) & df["auroc"].notna()].copy()

    def where(row):
        om = ordmap.get(row["view"])
        if not om or not row["unknown"]:
            return None
        unk = row["unknown"].split("|")[0]
        if unk not in om:
            return None
        i, L = om[unk], len(om)
        if i == 0:
            return "first"
        if i == L - 1:
            return "last"
        return "middle"

    d["hidden_at"] = d.apply(where, axis=1)
    d = d[d["hidden_at"].notna()]
    if not len(d):
        return None, None
    g = d.groupby(["hidden_at", "family"], dropna=False)
    out = g.apply(lambda x: pd.Series({
        "n_cells": x.groupby(["view", "encoder", "variant", "unknown", "shot"]).ngroups,
        "n_runs": len(x), "auroc_mean": x["auroc"].mean(), "auroc_sd": x["auroc"].std(ddof=1),
    })).reset_index()
    # Per-view breakdown. The aggregate flip is not uniform across datasets -- printing
    # only the mean would let one view carry it, which is exactly the failure mode the
    # plan's own numbers fell into (0.530/0.845/0.856 is banana4 alone).
    bv = d.groupby(["view", "hidden_at", "family"], dropna=False).apply(
        lambda x: pd.Series({"n_runs": len(x), "auroc_mean": x["auroc"].mean()})
    ).reset_index()
    piv = bv.pivot_table(index=["view", "hidden_at"], columns="family",
                         values="auroc_mean").reset_index()
    if {"prob", "dist"}.issubset(piv.columns):
        piv["dist_minus_prob"] = piv["dist"] - piv["prob"]
        piv["better_family"] = np.where(piv["dist_minus_prob"] > 0, "dist", "prob")
    return out.sort_values(["hidden_at", "family"]), piv.sort_values(["hidden_at", "view"])


def t13_score_corr(df, ordmap=None):
    """Cell-level agreement between scores, split by how many classes the head knows.

    On a two-known-class head the plan's RQ2 claim is not a correlation but a theorem:
    MSP = sigmoid(|z1-z2|) and Energy = log(2cosh((z1-z2)/2)) are both strictly monotone
    in |z1-z2|, so their AUROC is *identical* on every such cell. Reporting one pooled
    correlation would hide that: pooling two-class cells (where the two scores must agree)
    with three-class cells (where they need not) produces a number that is neither.
    """
    d = df[df["auroc"].notna()].copy()
    if ordmap:
        # known classes = ordinal length minus the hidden grade; only P1/P2 have one.
        nk = []
        for _, r in d.iterrows():
            om = ordmap.get(r["view"])
            unk = (r["unknown"] or "").split("|")[0]
            if om and unk in om and r["protocol"] in ("P1_out_of_grade", "P2_unseen_interior"):
                nk.append(len(om) - 1)
            else:
                nk.append(np.nan)
        d["n_known_classes"] = nk
    else:
        d["n_known_classes"] = np.nan
    # -1, not NaN: pivot_table silently drops NaN group keys, which would quietly
    # restrict every pair to the P1/P2 cells and make "all" a lie.
    d["n_known_classes"] = pd.to_numeric(d["n_known_classes"], errors="coerce").fillna(-1)
    key = ["view", "dataset", "encoder", "variant", "protocol", "unknown", "shot", "seed",
           "n_known_classes"]
    piv = d.pivot_table(index=key, columns="score", values="auroc", aggfunc="mean")
    scores = [s for s in ("msp", "energy", "mahalanobis", "knn") if s in piv.columns]
    rows = []
    lvl = np.asarray(piv.index.get_level_values("n_known_classes"), dtype=float)
    for a, b in itertools.combinations(scores, 2):
        for subset, sel in (("all", np.ones(len(piv), dtype=bool)),
                            ("known=2", lvl == 2),
                            ("known>=3", lvl >= 3)):
            sub = piv.loc[sel, [a, b]].dropna()
            if len(sub) < 3:
                continue
            rows.append({"score_a": a, "score_b": b,
                         "family_a": family(a), "family_b": family(b),
                         "same_family": family(a) == family(b), "subset": subset,
                         "n_cells": len(sub),
                         "spearman": float(sub[a].corr(sub[b], method="spearman")),
                         "pearson": float(sub[a].corr(sub[b], method="pearson")),
                         "median_abs_diff": float((sub[a] - sub[b]).abs().median()),
                         "frac_identical": float(((sub[a] - sub[b]).abs() < 1e-12).mean())})
    order = {"all": 0, "known=2": 1, "known>=3": 2}
    return pd.DataFrame(rows).sort_values(["score_a", "score_b", "subset"],
                                          key=lambda s: s.map(order) if s.name == "subset" else s)


def t14_adjacent(df, ordmap, npz_dir=None):
    """Adjacent-vs-distant known-grade rejection at the stored 5%-FPR threshold."""
    npz_dir = npz_dir or (RESULTS / "scores")
    rows = []
    d = df[df["arm"].isin(["P1_out_of_grade", "P2_unseen_interior"]) & df["auroc"].notna()]
    for _, r in d.iterrows():
        om = ordmap.get(r["view"])
        if not om or not r["unknown"]:
            continue
        unk = r["unknown"].split("|")[0]
        if unk not in om:
            continue
        hidx = om[unk]
        f = npz_dir / (r["run_id"] + ".npz")
        if not f.exists():
            continue
        with np.load(f, allow_pickle=True) as z:
            ks = np.asarray(z["known_scores"], dtype=float)
            kl = np.asarray(z["known_labels"])
        thr = r["threshold_fpr5"]
        if thr is None or np.isnan(thr):
            continue
        idx = np.array([om.get(str(l), -99) for l in kl])
        ok = idx >= 0
        if not ok.any():
            continue
        ks, idx = ks[ok], idx[ok]
        dist = np.abs(idx - hidx)
        adj, far = dist == 1, dist >= 2
        if adj.sum() < 5 or far.sum() < 5:
            continue                     # one side empty/too thin to compare
        rows.append({"view": r["view"], "encoder": r["encoder"], "variant": r["variant"],
                     "protocol": r["protocol"], "unknown": r["unknown"],
                     "score": r["score"], "family": r["family"], "shot": r["shot"],
                     "seed": r["seed"],
                     # how many grades this view actually has: the plan's granularity
                     # curve is the adjacent-distant gap as a function of this number.
                     "n_levels": len(om),
                     "rej_adjacent": float((ks[adj] < thr).mean()),
                     "rej_distant": float((ks[far] < thr).mean()),
                     "n_adjacent": int(adj.sum()), "n_distant": int(far.sum())})
    if not rows:
        return None, None
    raw = pd.DataFrame(rows)
    raw["delta_pp"] = (raw["rej_adjacent"] - raw["rej_distant"]) * 100.0
    g = raw.groupby(["protocol", "family"], dropna=False)
    summ = g.apply(lambda x: pd.Series({
        "n_cells": x.groupby(["view", "encoder", "variant", "unknown", "shot", "seed"]).ngroups,
        "delta_pp_mean": x["delta_pp"].mean(),
        "pct_cells_positive": 100.0 * float((x["delta_pp"] > 0).mean()),
    })).reset_index()
    # The plan's §5.3 ask on RaspGrade ("does adjacent-grade confusion grow with the number
    # of levels?") answered as a table, not a curve drawn by hand: one row per level count.
    gran = raw.groupby(["n_levels", "family"], dropna=False).apply(lambda x: pd.Series({
        "n_cells": x.groupby(["view", "encoder", "variant", "unknown", "shot", "seed"]).ngroups,
        "n_views": int(x["view"].nunique()),
        "delta_pp_mean": x["delta_pp"].mean(),
        "pct_cells_positive": 100.0 * float((x["delta_pp"] > 0).mean()),
    })).reset_index()
    return raw, summ, gran


def t15_collapsed(df, npz_dir=None):
    """Known-side cells whose argmax is a constant, or matches the majority share."""
    npz_dir = npz_dir or (RESULTS / "scores")
    rows = []
    for _, r in df.iterrows():
        f = npz_dir / (r["run_id"] + ".npz")
        if not f.exists():
            continue
        with np.load(f, allow_pickle=True) as z:
            if "known_pred" not in z:
                continue
            pred = np.asarray(z["known_pred"])
            lab = np.asarray(z["known_labels"])
        if len(pred) == 0:
            continue
        acc = float((pred == lab).mean())
        _, counts = np.unique(lab, return_counts=True)
        maj = float(counts.max() / counts.sum())
        const = len(np.unique(pred)) == 1
        if const or abs(acc - maj) < 1e-9:
            rows.append({"view": r["view"], "encoder": r["encoder"], "variant": r["variant"],
                         "protocol": r["protocol"], "unknown": r["unknown"],
                         "score": r["score"], "shot": r["shot"], "seed": r["seed"],
                         "known_acc": acc, "majority_share": maj,
                         "collapsed_to_single_class": bool(const),
                         "n_known": int(len(pred))})
    return pd.DataFrame(rows)


def t16_small_n(df, n_min):
    d = df[(df["n_known"] < n_min) | (df["n_unknown"] < n_min)]
    if not len(d):
        return None
    g = d.groupby(["arm", "view", "protocol", "unknown", "shot"], dropna=False)
    out = g.apply(lambda x: pd.Series({
        "n_known": int(x["n_known"].max()), "n_unknown": int(x["n_unknown"].max()),
        "n_runs": len(x), "auroc_mean": x["auroc"].mean(),
        "auroc_min": x["auroc"].min(), "auroc_max": x["auroc"].max(),
    })).reset_index()
    return out


def seed_bootstrap(df, n_boot=2000, seed=0):
    """Percentile CI of the cell mean, resampling SEEDS (the only replicate we have).

    Resampling seeds answers "how much of this mean is seed noise", not "how much is
    dataset noise" -- the latter needs more datasets, not more resampling. Stated here
    because a CI without its resampling unit invites exactly that misreading.
    """
    rng = np.random.RandomState(seed)
    d = df[df["auroc"].notna()]
    rows = []
    for (v, enc, proto, unk, sc, shot), g in d.groupby(
            ["view", "encoder", "protocol", "unknown", "score", "shot"], dropna=False):
        vals = g["auroc"].dropna().values
        if len(vals) < 3:
            continue
        means = [vals[rng.randint(0, len(vals), len(vals))].mean() for _ in range(n_boot)]
        rows.append({"view": v, "encoder": enc, "protocol": proto, "unknown": unk,
                     "score": sc, "shot": shot, "n_seeds": len(vals),
                     "mean": float(vals.mean()),
                     "lo": float(np.percentile(means, 2.5)),
                     "hi": float(np.percentile(means, 97.5))})
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-min", type=int, default=30)
    ap.add_argument("--bootstrap", type=int, default=2000)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    df = load_e2()
    if not len(df):
        print("no E2 results"); return
    print("E2 uncalibrated runs:", len(df))
    ordmap = _ordinal_index_map()

    T = {}
    T["T11_auroc_by_arm"] = t11_by_arm(df)
    T["T11b_auroc_by_arm_score"] = t11b_by_arm_score(df)
    T["T12_family_flip"], T["T12b_family_flip_by_view"] = t12_family_flip(df, ordmap)
    T["T13_score_corr"] = t13_score_corr(df, ordmap)
    raw_adj, summ_adj, gran_adj = t14_adjacent(df, ordmap)
    T["T14_adjacent"] = summ_adj
    T["T14b_granularity"] = gran_adj
    T["T15_collapsed"] = t15_collapsed(df)
    T["T16_small_n"] = t16_small_n(df, a.n_min)

    L = ["# Plan v2.0 analyses computed from stored score arrays\n",
         "Generated by `analyze_v2.py`. Every number here is recomputed from "
         "`results/*.json` + `results/scores/*.npz`; nothing is typed by hand.\n",
         "Definitions that travel with the numbers:\n",
         "- a **cell** = (view, encoder, variant, protocol, unknown, shot, seed); "
         "`n_cells` counts them, `n_runs` counts result files (they differ only where a "
         "variant or head is part of the run but not of the cell key).\n",
         "- **family** prob = {msp, energy}; dist = {mahalanobis, knn}.\n",
         "- **`delta_pp` = (reject rate on the ADJACENT grade − reject rate on the DISTANT "
         "grade) × 100**. A NEGATIVE value is the desirable direction: the score rejects "
         "far grades more often than near ones. Read the sign before reading the size.\n",
         "- a view with fewer than %d test images on either side is thin: E2 skips those "
         "cells and T16 lists them; their numbers are descriptive only.\n" % a.n_min]

    for k in ("T11_auroc_by_arm", "T11b_auroc_by_arm_score", "T12_family_flip",
              "T12b_family_flip_by_view",
              "T13_score_corr", "T14_adjacent", "T14b_granularity"):
        t = T.get(k)
        if t is None or not len(t):
            L.append("## %s\n\nnot computed (no matching runs)\n" % k)
            continue
        L.append("## %s\n" % k)
        L.append(t.to_markdown(index=False, floatfmt=".4f"))
        L.append("")

    t15 = T.get("T15_collapsed")
    L.append("## T15_collapsed\n")
    if t15 is None or not len(t15):
        L.append("No collapsed known-side cells: every cell's prediction spread is wider "
                 "than one class and its accuracy differs from the majority share.\n")
    else:
        cells = t15.groupby(["view", "protocol", "unknown"]).size()
        L.append("Collapsed cells: **%d runs** over %d (view, protocol, hidden-grade) "
                 "combinations.\n" % (len(t15), len(cells)))
        L.append(t15.groupby(["view", "encoder", "protocol", "unknown", "shot"], dropna=False)
                 .agg(n_runs=("known_acc", "size"), known_acc=("known_acc", "mean"),
                      majority_share=("majority_share", "mean"),
                      single_class=("collapsed_to_single_class", "max"))
                 .reset_index().to_markdown(index=False, floatfmt=".4f"))
        L.append("")

    t16 = T.get("T16_small_n")
    L.append("## T16_small_n (threshold n >= %d on both sides)\n" % a.n_min)
    if t16 is None or not len(t16):
        L.append("Every open-set cell has at least %d test images on both sides.\n" % a.n_min)
    else:
        L.append("%d (view, protocol, hidden-grade, shot) groups fall below %d on one side. "
                 "They keep their numbers but must be labelled *descriptive* in the paper; "
                 "the seed bootstrap interval is in `T16b_seed_bootstrap.csv`.\n"
                 % (len(t16), a.n_min))
        L.append(t16.to_markdown(index=False, floatfmt=".4f"))
        L.append("")

    if t16 is not None and len(t16):
        small_keys = set(map(tuple, t16[["view", "protocol", "unknown", "shot"]].values))
        bs = seed_bootstrap(df, a.bootstrap)
        bs = bs[[tuple(x) in small_keys for x in
                 bs[["view", "protocol", "unknown", "shot"]].values]]
        if len(bs):
            bs.to_csv(OUT / "T16b_seed_bootstrap.csv", index=False)
            L.append("### Seed bootstrap CI for the thin cells (unit = seed)\n")
            L.append(bs.head(60).to_markdown(index=False, floatfmt=".4f"))
            L.append("")

    for k, t in T.items():
        if t is not None and len(t):
            t.to_csv(OUT / (k + ".csv"), index=False)
    if raw_adj is not None and len(raw_adj):
        raw_adj.to_csv(OUT / "T14_adjacent_raw.csv", index=False)
    (OUT / "ANALYSIS_V2.md").write_text("\n".join(L), encoding="utf-8")
    print("wrote", OUT / "ANALYSIS_V2.md")


if __name__ == "__main__":
    main()
