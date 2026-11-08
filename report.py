#!/usr/bin/env python3
"""Aggregate results -> master.csv, tables, figures, REPORT.md, and independent verification."""
import sys, json, glob, math
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import (RESULTS, OUT, PROC, FEAT, log, read_json, atomic_write_json, now,
                        display_view, display_protocol)
from rio.methods import open_set_metrics, closed_set_metrics

OUT.mkdir(parents=True, exist_ok=True)

SKIPPED = []      # result files that could not be read; reported, never swallowed


def load_runs():
    rows = []
    for p in sorted(RESULTS.glob("*.json")):
        try:
            r = read_json(p)
        except Exception as e:
            # Never skip silently. A result file that cannot be read is a hole in a
            # table, and the old `continue` made it indistinguishable from "the
            # experiment was never run". Counted, named and asserted to zero by
            # final_check.py.
            SKIPPED.append((p.name, ("%s: %s" % (type(e).__name__, e))[:160]))
            continue
        if not isinstance(r, dict) or not isinstance(r.get("config"), dict) \
                or not isinstance(r.get("metrics"), dict):
            SKIPPED.append((p.name, "missing config/metrics"))
            continue
        c = r.get("config", {})
        m = r.get("metrics", {})
        rec = {"file": p.name, "exp": c.get("exp"), "dataset": c.get("dataset"),
               "view": display_view(c.get("view")), "encoder": c.get("encoder"), "variant": c.get("variant"),
               "head": c.get("head"), "shot": c.get("shot"), "seed": c.get("seed"),
               "protocol": display_protocol(c.get("protocol")), "score": c.get("score"),
               "unknown": "|".join(c.get("unknown", [])) if isinstance(c.get("unknown"), list) else c.get("unknown"),
               # P3_foreign records name the unknown side under "foreign" (the label list)
               # rather than "unknown", because its unknown side is a whole other dataset.
               "foreign": "|".join(c.get("foreign", [])) if isinstance(c.get("foreign"), list) else c.get("foreign"),
               "C": c.get("C"), "control": c.get("control", "none"),
               # the calibration arm re-runs the same E2 grid with per-class thresholds;
               # its auroc/fpr95 are identical to the uncalibrated run, so if both are
               # pooled the mean stays right but the seed-wise sd shrinks and n_runs
               # doubles. T3 therefore filters calibrated runs out; T10 owns them.
               "calib": c.get("calib"),
               # E3 only: "bn" = the plan's optional feature-level alignment tier. Kept as
               # its own column so aligned and unaligned runs are never pooled into one mean.
               "align": c.get("align"),
               "finished_at": r.get("finished_at")}
        for k, v in m.items():
            if isinstance(v, (int, float, str, bool)) or v is None:
                rec[k] = v
        rows.append(rec)
    return pd.DataFrame(rows)


def ms_values(g, col):
    if col not in g.columns:
        return "NA"
    v = g[col].dropna().values
    if len(v) == 0:
        return "NA"
    return "%.4f ± %.4f" % (v.mean(), v.std(ddof=1) if len(v) > 1 else 0.0)


def correct_multiple(df, alpha=0.05):
    """Attach Bonferroni and Holm corrections to a table of p-values.

    Plan v2.0 fix #7: the paired-test table has ~32 tests over the same 5 seeds, so an
    uncorrected p<0.05 is not evidence -- it is the expected number of false positives
    at that count. Both corrections are printed, and the verdict column is the strict
    one (Bonferroni), because the paper's claim is "how many survive correction".
    """
    if df is None or not len(df) or "p" not in df.columns:
        return df
    p = df["p"].astype(float).values
    m = len(p)
    df = df.copy()
    df["p_bonferroni"] = np.minimum(1.0, p * m)
    order = np.argsort(p)
    holm = np.empty(m)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (m - rank) * p[i])
        holm[i] = min(1.0, running)
    df["p_holm"] = holm
    df["survives_bonferroni_0.05"] = p < alpha / m
    df["n_tests_in_family"] = m
    return df


def calibration_table():
    """E2 calibration arm: per-class thresholds fitted on val, evaluated on test."""
    rows = []
    for p in sorted(RESULTS.glob("E2__*.json")):
        try:
            r = read_json(p)
        except Exception:
            continue
        c = r.get("config", {})
        if not c.get("calib"):
            continue
        m, cal = r.get("metrics", {}), (r.get("metrics", {}).get("calibrated") or {})
        if not cal:
            continue
        # A known class missing from `tau` was calibrated to -inf (accept everything).
        # Derived from the stored maps so it also works for runs written before the
        # explicit field existed.
        tau = cal.get("tau") or {}
        n_no_tau = len(set(cal.get("rejection_rate_per_class") or {}) - set(tau))
        rows.append({"view": display_view(c.get("view")), "encoder": c.get("encoder"),
                     "protocol": display_protocol(c.get("protocol")), "score": c.get("score"),
                     "shot": c.get("shot"), "seed": c.get("seed"),
                     "auroc": m.get("auroc"), "ccr5_base": m.get("ccr_at_fpr5"),
                     # The two numbers the plan says a calibration claim may rest on:
                     # OSCR and the CCR at the fixed 5%-FPR operating point. Both are
                     # computed from the SAME scores as the uncalibrated arm -- per-class
                     # thresholds do not change the scores, only where the cut is placed.
                     "oscr_base": m.get("oscr"),
                     # CCR if every sample were accepted: the closed-set accuracy of knowns.
                     # Per-class 5%-quantile thresholds accept ~95% of EVERYTHING, so this
                     # is the number ccr_cal must be compared against, not a ceiling to beat.
                     "ccr_all": m.get("known_acc"),
                     "b": cal.get("rejection_spread_before"),
                     "a": cal.get("rejection_spread_after"), "ccr": cal.get("ccr"),
                     "fpr": cal.get("fpr"), "ka": cal.get("known_accept_rate"),
                     "src": cal.get("calib_source"), "n_calib": cal.get("n_calib"),
                     "n_no_tau": n_no_tau})
    if not rows:
        return None
    d = pd.DataFrame(rows)
    g = d.groupby(["view", "encoder", "protocol", "score", "shot"], dropna=False)
    return g.apply(lambda x: pd.Series({
        "auroc": ms_values(x, "auroc"),
        "oscr_at_fpr5_rule": ms_values(x, "oscr_base"),
        "ccr_fpr5_before": ms_values(x, "ccr5_base"),
        "ccr_accept_all": ms_values(x, "ccr_all"),
        "rej_sd_before": ms_values(x, "b"), "rej_sd_after": ms_values(x, "a"),
        "ccr_cal": ms_values(x, "ccr"), "fpr_cal": ms_values(x, "fpr"),
        "known_accept_cal": ms_values(x, "ka"), "n_runs": len(x),
        # number of known classes that fell back to an accept-everything threshold
        "classes_no_tau_max": int(x["n_no_tau"].max()) if "n_no_tau" in x else 0,
        "calib_src": ",".join(sorted(set(x["src"].dropna().astype(str))))})).reset_index()


def tables(df):
    out = {}
    # datasets
    rows = []
    for cp in sorted(PROC.glob("*/card.json")):
        c = read_json(cp)
        rows.append({"dataset": c["dataset"], "n_images": c["n_images"], "n_groups": c["n_groups"],
                     "splits": json.dumps(c["split_counts"]), "classes": ", ".join(c["classes"]),
                     "group_leaks": c["group_leak_count"], "meta_sha256": c["meta_sha256"][:16]})
    out["T1_datasets"] = pd.DataFrame(rows)
    d1 = df[(df["exp"] == "E1") & (df["control"] == "none")]
    if len(d1):
        g = d1.groupby(["view", "encoder", "variant", "head", "shot"], dropna=False)
        t = g.apply(lambda x: pd.Series({"acc": ms_values(x, "acc"), "macro_f1": ms_values(x, "macro_f1"),
                                         "off_by_one": ms_values(x, "off_by_one_rate"),
                                         "n_runs": len(x)})).reset_index()
        out["T2_closed_set"] = t
    # per-class AP lives under its own experiment key (E1ap, written by ap_extra.py):
    # same cells as E1 but with probabilities, so AP can be computed at all. Kept apart
    # from T2 so no existing row or paired test changes.
    dap = df[df["exp"] == "E1ap"]
    if len(dap):
        g = dap.groupby(["view", "encoder", "variant", "head", "shot"], dropna=False)
        t = g.apply(lambda x: pd.Series({"macro_ap": ms_values(x, "macro_ap"),
                                         "chance": ms_values(x, "prevalence_macro"),
                                         "n_runs": len(x)})).reset_index()
        out["T2b_per_class_ap"] = t
    # The plan's weighted macro-F1 (adjacent-grade error cost 1, skipped grade cost 2).
    # E1 keeps hard predictions only and the existing `_weighted_f1` in rio/methods.py is
    # an edge-position weight, NOT this cost -- so the metric has its own arm (E1ord,
    # written by ord_extra.py) and its own column name. Pooling the two would print two
    # different quantities under one label.
    dord = df[df["exp"] == "E1ord"]
    if len(dord):
        g = dord.groupby(["view", "encoder", "variant", "head", "shot"], dropna=False)
        t = g.apply(lambda x: pd.Series({"cost_f1": ms_values(x, "cost_f1"),
                                         "macro_f1": ms_values(x, "macro_f1"),
                                         "off_by_one": ms_values(x, "off_by_one"),
                                         "ordinal_mae": ms_values(x, "ordinal_mae"),
                                         "n_runs": len(x)})).reset_index()
        out["T2c_ordinal_cost_f1"] = t
    # adapted backbones: E1ft = fully fine-tuned ResNet-50, E1lora = LoRA on DINOv2-S
    dft = df[df["exp"].isin(["E1ft", "E1lora"])]
    if len(dft):
        g = dft.groupby(["exp", "encoder", "view", "shot"], dropna=False)
        t = g.apply(lambda x: pd.Series({"acc": ms_values(x, "acc"), "macro_f1": ms_values(x, "macro_f1"),
                                         "off_by_one": ms_values(x, "off_by_one_rate"),
                                         "n_runs": len(x)})).reset_index()
        out["T7_adapted"] = t
    d2 = df[(df["exp"] == "E2") & (df["calib"].isna())]
    if len(d2):
        g = d2.groupby(["view", "encoder", "variant", "protocol", "score", "shot"], dropna=False)
        t = g.apply(lambda x: pd.Series({"auroc": ms_values(x, "auroc"), "fpr95": ms_values(x, "fpr95"),
                                         "oscr": ms_values(x, "oscr"),
                                         "known_acc": ms_values(x, "known_acc"),
                                         # Plan v2.0 fix #6: the smallest side of the
                                         # AUROC in this cell. Below 30 the number is
                                         # still printed but it is not an estimate, and
                                         # `thin` says so next to it rather than letting a
                                         # reader infer precision from four decimals.
                                         "n_known_test": int(x["n_known"].min()) if "n_known" in x else -1,
                                         "n_unknown_test": int(x["n_unknown"].min()) if "n_unknown" in x else -1,
                                         "thin": bool(((x["n_known"] < 30) | (x["n_unknown"] < 30)).any())
                                         if "n_known" in x else False,
                                         "n_runs": len(x)})).reset_index()
        out["T3_open_set"] = t
    t10 = calibration_table()
    if t10 is not None and len(t10):
        out["T10_calibration"] = t10
    dctl = df[(df["exp"] == "E1") & (df["control"] != "none")]
    if len(dctl):
        g = dctl.groupby(["view", "encoder", "control", "shot"], dropna=False)
        t = g.apply(lambda x: pd.Series({"acc": ms_values(x, "acc"), "macro_f1": ms_values(x, "macro_f1"),
                                         "n_runs": len(x)})).reset_index()
        out["T8_controls"] = t
    db = df[df["exp"].astype(str).str.startswith("B")]
    if len(db):
        g = db.groupby(["exp", "view", "encoder"], dropna=False)
        t = g.apply(lambda x: pd.Series({"acc": ms_values(x, "acc"), "macro_f1": ms_values(x, "macro_f1"),
                                         "off_by_one": ms_values(x, "off_by_one_rate"),
                                         "unparsed_rate": ms_values(x, "unparsed_rate"),
                                         # Plan v2.0 fix #8: a baseline number is only
                                         # comparable to E1 if it was measured on the same
                                         # rows. n_test and the hash of the exact test ids
                                         # are the two fields that make that checkable; a
                                         # baseline that used a capped subset shows a
                                         # smaller n and a different hash, by construction.
                                         "n_test": ms_values(x, "n_test"),
                                         "test_ids_sha256": (x["test_ids_sha256"].dropna().iloc[0][:16]
                                                             if "test_ids_sha256" in x and
                                                             x["test_ids_sha256"].notna().any() else "NA"),
                                         "n_runs": len(x)})).reset_index()
        out["T6_baselines"] = t
    d3 = df[df["exp"] == "E3"]
    if len(d3):
        # align is part of the method: BN-aligned and plain transfer runs must not share a
        # row, or the reported mean is of two different methods.
        g = d3.groupby(["view", "encoder", "variant", "head", "shot", "align"], dropna=False)
        t = g.apply(lambda x: pd.Series({"acc": ms_values(x, "acc"), "macro_f1": ms_values(x, "macro_f1"),
                                         "n_runs": len(x)})).reset_index()
        out["T4_cross_domain"] = t
    return out


def paired_tests(df):
    """Paired comparison of dinov2_s vs resnet50 over seeds within (view, shot, head)."""
    from scipy import stats
    # variant == "cls" is required: the mean-patch arm also has dinov2_s/resnet50 at
    # linear/cls-head, so without the filter each (view, shot, seed) has two rows and
    # set_index produces a duplicate index -- a.loc[common] then returns 2x2 arrays and
    # scipy raises "shapes are incompatible for broadcasting" at report time.
    d = df[(df["exp"] == "E1") & (df["control"] == "none") &
           (df["encoder"].isin(["dinov2_s", "resnet50"])) & (df["head"] == "linear") &
           (df["variant"] == "cls")]
    rows = []
    for (v, shot), g in d.groupby(["view", "shot"], dropna=False):
        a = g[g["encoder"] == "dinov2_s"].set_index("seed")["macro_f1"]
        b = g[g["encoder"] == "resnet50"].set_index("seed")["macro_f1"]
        common = sorted(set(a.index) & set(b.index))
        if len(common) < 2:
            continue
        dif = (a.loc[common] - b.loc[common]).values
        t, p = stats.ttest_rel(a.loc[common].values, b.loc[common].values)
        rows.append({"view": display_view(v), "shot": shot, "n_pairs": len(common),
                     "mean_diff_dinov2_minus_resnet": dif.mean(),
                     "sd_diff": dif.std(ddof=1), "t": t, "p": p})
    return correct_multiple(pd.DataFrame(rows))


def ordinal_head_tests(df):
    """E4 ordinal ablation: CORN head vs the plain linear head, paired by seed.

    Both heads are fitted on the same support of the same cell, so the only thing that
    differs is whether the grade order enters the model. The comparison is on the plan's
    ordinal metrics (cost-weighted macro-F1 and off-by-one rate), not on accuracy: a head
    that respects the ordering is supposed to trade a few exact hits for nearer misses.
    Sign counts are reported next to the means so a reader can see whether the mean is
    carried by one seed or by every pair.
    """
    from scipy import stats
    d = df[(df["exp"] == "E1ord") & (df["head"].isin(["corn", "linear"]))]
    rows = []
    for (v, enc, var, shot), g in d.groupby(["view", "encoder", "variant", "shot"], dropna=False):
        a = g[g["head"] == "corn"].set_index("seed")
        b = g[g["head"] == "linear"].set_index("seed")
        common = sorted(set(a.index) & set(b.index))
        if len(common) < 2:
            continue
        for met in ("cost_f1", "off_by_one", "macro_f1"):
            if met not in a.columns:
                continue
            dif = (a.loc[common, met].astype(float) - b.loc[common, met].astype(float)).values
            t, p = stats.ttest_rel(a.loc[common, met].astype(float).values,
                                   b.loc[common, met].astype(float).values)
            rows.append({"view": v, "encoder": enc, "variant": var, "shot": shot,
                         "metric": met, "n_pairs": len(common),
                         "corn": float(a.loc[common, met].astype(float).mean()),
                         "linear": float(b.loc[common, met].astype(float).mean()),
                         "delta_corn_minus_linear": float(dif.mean()),
                         "sd_diff": float(dif.std(ddof=1)), "t": t, "p": p,
                         "corn_better_pairs": int((dif > 0).sum()) if met != "off_by_one"
                         else int((dif < 0).sum())})
    return correct_multiple(pd.DataFrame(rows))


def figures(df, T):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figdir = OUT / "figures"
    figdir.mkdir(exist_ok=True)
    d = df[(df["exp"] == "E1") & (df["control"] == "none") & (df["head"] == "linear") & (df["variant"] == "cls")].copy()
    if len(d):
        d["shot_num"] = d["shot"].apply(lambda x: 10 ** 4 if pd.isna(x) else x)
        for view, g in d.groupby("view"):
            fig, ax = plt.subplots(figsize=(6, 4))
            for enc, gg in g.groupby("encoder"):
                s = gg.groupby("shot_num")["macro_f1"].agg(["mean", "std"]).sort_index()
                ax.errorbar(range(len(s)), s["mean"], yerr=s["std"].fillna(0), marker="o", label=enc)
            ax.set_xticks(range(len(s.index)))
            ax.set_xticklabels(["all" if i == 10 ** 4 else str(i) for i in s.index])
            ax.set_xlabel("shots per class"); ax.set_ylabel("macro-F1")
            ax.set_title("Few-shot closed-set: %s" % view); ax.legend(fontsize=8); ax.grid(alpha=.3)
            fig.tight_layout(); fig.savefig(figdir / ("fig_shot_%s.png" % view), dpi=200); plt.close(fig)
    d2 = df[(df["exp"] == "E2") & (df["calib"].isna())].copy()
    if len(d2):
        fig, ax = plt.subplots(figsize=(8, 4))
        sub = d2[d2["score"] == "energy"]
        piv = sub.groupby(["view", "encoder"])["auroc"].mean().unstack()
        piv.plot(kind="bar", ax=ax)
        ax.set_ylabel("AUROC (energy, all-shot)"); ax.set_ylim(0.4, 1.0); ax.grid(alpha=.3, axis="y")
        fig.tight_layout(); fig.savefig(figdir / "fig_open_set_auroc.png", dpi=200); plt.close(fig)
    if "T3_open_set" in T:
        pass
    return figdir


def write_report(df, T, tests):
    L = []
    L.append("# Ripeness OPEN-SET recognition pipeline — automatic results report\n")
    L.append("Generated: %s\n" % now())
    L.append("## Datasets\n")
    if "T1_datasets" in T:
        L.append(T["T1_datasets"].to_markdown(index=False))
    L.append("\n## Closed-set few-shot (mean ± sd over seeds)\n")
    if "T2_closed_set" in T:
        L.append(T["T2_closed_set"].to_markdown(index=False))
    L.append("\n## Per-class average precision (the plan's long-tail metric; mean ± sd over seeds)\n")
    if "T2b_per_class_ap" in T:
        L.append(T["T2b_per_class_ap"].to_markdown(index=False))
        L.append("\n`chance` is the macro prevalence of the test split: on a balanced view "
                 "it is 1/C, and an uninformative scorer's macro AP lands there. These runs "
                 "live under `exp = E1ap` so they never enter T2 or the paired tests.")
    else:
        L.append("not yet computed (`python3 ap_extra.py`)")
    L.append("\n## Ordinal cost-weighted macro-F1 (plan 5.3: adjacent error costs 1, "
             "skipped grade costs 2; mean ± sd over seeds)\n")
    if "T2c_ordinal_cost_f1" in T:
        L.append(T["T2c_ordinal_cost_f1"].to_markdown(index=False))
        L.append("\nDefinition: an adjacent-grade error earns credit 1/2 and a skipped grade "
                 "credit 0, so the penalty ratio is 1:2 exactly as the plan states; per-class "
                 "precision/recall are the mean credit over samples predicted-as / labelled-as "
                 "that class, F1 is their harmonic mean, and the macro average runs over the "
                 "ordinal class list (same convention as `macro_f1`). `macro_f1` here is "
                 "recomputed from the re-fitted head and must equal T2's value for the same "
                 "cell -- `outputs/E1ORD_XCHECK.txt` records that comparison, and a non-zero "
                 "mismatch means this table measures a different pipeline. Runs live under "
                 "`exp = E1ord` so they never enter T2 or the paired tests.")
    else:
        L.append("not yet computed (`python3 ord_extra.py`)")
    ot = ordinal_head_tests(df)
    L.append("\n## E4 ordinal ablation: CORN ordinal head vs linear head (paired by seed)\n")
    if len(ot):
        ot.to_csv(OUT / "T5b_ordinal_head.csv", index=False)
        L.append(ot.to_markdown(index=False, floatfmt=".4f"))
        L.append("\n`delta_corn_minus_linear` is the seed-paired mean difference (positive "
                 "= CORN higher). `corn_better_pairs` counts seeds on which CORN is better "
                 "under each metric's own direction (off-by-one is better when smaller). "
                 "Both heads are fitted on the identical support of the identical cell, "
                 "so the comparison isolates the ordinal constraint.")
    else:
        L.append("not yet computed (`python3 run.py --stage e1 --heads corn` plus "
                 "`python3 ord_extra.py --heads linear,corn`)")
    L.append("\n## Open-set rejection (mean ± sd over seeds)\n")
    if "T3_open_set" in T:
        L.append(T["T3_open_set"].to_markdown(index=False))
    L.append("\n## Cross-domain\n")
    if "T4_cross_domain" in T:
        L.append(T["T4_cross_domain"].to_markdown(index=False))
    L.append("\n## Paired tests: DINOv2-S vs ResNet-50 (linear head, macro-F1, paired by seed)\n")
    if len(tests):
        L.append(tests.to_markdown(index=False))
        n_sig = int(tests["survives_bonferroni_0.05"].sum()) if "survives_bonferroni_0.05" in tests else 0
        L.append("\n`n_tests_in_family` is the size of this family (%d). Raw p is corrected "
                 "twice (Bonferroni and Holm); the verdict column is the strict one. "
                 "**%d of %d survive Bonferroni at alpha=0.05** -- that count, not the raw "
                 "p-values, is what a significance statement may cite."
                 % (len(tests), n_sig, len(tests)))
    L.append("\n## Calibration arm: per-class thresholds fitted on val\n")
    if "T10_calibration" in T:
        L.append(T["T10_calibration"].to_markdown(index=False))
        L.append("""
Read this table before making any claim about calibration.

**The comparison at a matched false-positive rate is the only one the plan allows.**
Per-class thresholds do not touch the scores; they move the cut. So at a matched global
FPR the calibrated arm cannot differ from the uncalibrated one -- the matched-FPR
numbers are therefore `oscr_at_fpr5_rule` and `ccr_fpr5_before`, and `ccr_cal` must never
be compared against `ccr_fpr5_before` as if the two had the same FPR. The honest summary
of this table is *threshold redistribution*: `ccr_cal` is bought with `fpr_cal`, which
sits near 0.95 precisely because the per-class 5%-quantile accepts ~95% of everything.
Per-class matched-FPR calibration (shifting all thresholds by one common offset until the
global FPR returns to 5%) is *not* computable from the stored arrays, because the
predicted class of each unknown sample was not kept; that is a limitation of the
measurement, not a result.

**`ccr_accept_all` is the column that decides whether calibration bought anything.**
A per-class threshold at the 5th percentile accepts ~95% of *known* samples by
construction — and also ~95% of unknown ones, because the threshold sits near the bottom
of the score distribution rather than at a fixed global FPR. So `fpr_cal` hovering near
0.95 is not a failure of the calibration, and `ccr_cal` rising above `ccr_fpr5_before` is
not by itself evidence of better rejection: compare `ccr_cal` with `ccr_accept_all`. If the
two are close, the calibrated arm accepted essentially everything and the only thing it
repairs is the *imbalance* of rejection across grades — which is what
`rej_sd_before/after` measures and what the plan asked about.

`ccr_fpr5_before` is the uncalibrated operating point (CCR at the global 5%-FPR threshold).
`rej_sd_before/after` are the
standard deviations of the per-class rejection rates at, respectively, the global
5%-FPR operating point and the calibrated one; a drop means the imbalance across grades
was a threshold artefact. `fpr_cal` is the false-positive rate that results from the
calibrated thresholds -- it is an outcome, not something that was tuned. Where `fpr_cal`
approaches 1.0 while `auroc` is below 0.5, the score ranking is inverted for that view
(unknowns look more in-distribution than knowns) and no per-class calibration can repair
it; the honest reading is that the ranking, not the threshold, is the problem.
`calib_src` says which pool the thresholds were fitted on (`val` is the normal case;
`support (no usable val split)` means the view had fewer than 20 calibration samples and
fell back to a pool the head was trained on, so its thresholds are optimistic).
`classes_no_tau_max` counts known classes with no calibration samples: those get
threshold -inf (everything predicted as them is accepted), which can only inflate FPR.
""")
    L.append("\n## Adapted backbones: full fine-tuning vs LoRA (mean ± sd over seeds)\n")
    if "T7_adapted" in T:
        L.append(T["T7_adapted"].to_markdown(index=False))
    L.append("\n## Zero-shot / few-shot VLM baselines\n")
    if "T6_baselines" in T:
        L.append(T["T6_baselines"].to_markdown(index=False))
    L.append("\n## Negative controls (must not exceed chance)\n")
    if "T8_controls" in T:
        L.append(T["T8_controls"].to_markdown(index=False))
        L.append("""
`shuffle_labels` rotates the class names of the support set by a non-zero offset: every
support label changes and the class multiset is preserved, so the head can exploit only
feature geometry. Expect macro-F1 at or *below* 1/C -- below is normal, because the
rotation maps each class to a specific wrong one and the test split is imbalanced. What
matters is that it never exceeds chance. `random_features` keeps the labels and replaces
the features with Gaussian noise. Judge both on macro-F1 (chance = 1/C); accuracy has a
high floor on these splits.
""")
    L.append("\n## Efficiency (E5)\n")
    eff = OUT / "T9_efficiency.md"
    if eff.exists():
        L.append(eff.read_text(encoding="utf-8"))
        L.append("\nLatency is encoder-only, batch 1, median of 20 passes after warm-up, "
                 "with a CUDA synchronisation around each pass. It excludes image decoding "
                 "and is a relative comparison, not a deployment figure. At batch 1 the "
                 "time is dominated by launch overhead, so a 4x smaller ViT is *not* 4x "
                 "faster -- dinov2_s and dinov2_b come out within ~2 ms of each other. "
                 "Read `params` and `peak_mem_mb_b32` for the cost story, not `latency_ms_b1`. "
                 "If this table was produced while another job was using the CPU, the "
                 "launch-bound numbers are inflated; the driver re-measures it with an idle "
                 "card at the end of every cycle.\n")
    analysis = OUT / "ANALYSIS_V2.md"
    L.append("\n## Plan v2.0 analyses (arm difficulty, family flip, score families, "
             "adjacent-grade rejection, collapse and thin cells)\n")
    if analysis.exists():
        L.append("Computed by `analyze_v2.py` from the stored score arrays; the file is "
                 "reproduced here verbatim so REPORT.md is self-contained.\n")
        L.append(analysis.read_text(encoding="utf-8"))
    else:
        L.append("not yet computed (`python3 analyze_v2.py`)")
    L.append("""
## Notes that must travel with these numbers

1. **MSP and Energy are rank-equivalent on two-class known sets -- and only there.**
   The earlier text here said `E = -log p_max`, which is wrong: the energy score is
   `logsumexp(z)`, a free energy, not a transform of the maximum probability. The real
   mechanism is narrower. With exactly two known classes the logits enter softmax as
   `(z1, z2)`, so `MSP = sigmoid(|z1-z2|)` and `Energy = log(2 cosh((z1-z2)/2))`; both are
   strictly increasing in `|z1-z2|`, so every rank-based statistic -- AUROC, FPR@95TPR,
   OSCR -- is *identical* for the two scores. With three or more known classes that
   identity is gone (measured: P3_foreign 0.645 vs 0.664 on the same runs). The
   consequence for the paper: on P1/P2 cells MSP and Energy are one signal, not two; the
   measured cell-level Spearman over the whole E2 grid is 0.91, not the 0.99 the plan
   quoted, and it is 1.000 exactly on the two-class cells.
2. **OSCR counts only correctly-classified accepted knowns** in the CCR term. An open-set
   method that rejects everything would otherwise score perfectly on the known side.
3. **There are four unknown arms, and P1/P2 are two instances of one operation.**
   P1 hides the terminal grade; P2 hides any non-terminal grade, *including the first*
   (the code loops `ordn[:-1]`, so "first" is a P2 case, not an extra protocol); P3a
   hides the decayed class; P3b is a cross-dataset foreign fruit. P1 and P2 are the same
   "hide one level" operation with different positions on the ordinal scale -- do not
   write them as two different phenomena. P2 needs at least three grades: hiding the
   single non-terminal grade of a two-grade view would leave one known class, which is
   not a classification problem. P3b's unknown differs in species AND camera AND
   lighting by construction (`FOREIGN_PAIRS` is deliberately cross-dataset), so a high
   P3b AUROC is "not-this-fruit AND not-this-camera" and is not attributable to foreign
   matter alone.
4. **Support is drawn from train, evaluation is on test**, and no hyper-parameter is
   selected on val, so the val split contributes nothing to any number here.
5. **The adapted arms (E1ft, E1lora) train with random crop/flip**, while the frozen
   arms see one deterministic centre crop. The asymmetry favours the adapted arms; the
   claims about frozen features are therefore conservative.
6. **Group leakage is asserted to zero on every dataset**; a non-zero count aborts the
   build. For fruit12 the group is the source photograph, not the crop.
7. **Test splits are not class-balanced, so accuracy has a high floor.** The
   `fruit12_banana` test split is 67% Ripe; a predictor that collapses to a single class
   scores acc 0.673 there with macro-F1 0.28 (this is exactly what the shuffled-label
   control does for one seed). Read macro-F1 as primary, and read the negative controls
   in macro-F1, not accuracy.
8. **FPR@95TPR is the FPR at the largest threshold whose TPR is still >= 95%**, and each
   record also stores the TPR actually reached (`tpr_at_fpr95`). The earlier definition
   (`np.percentile(known_scores, 5)`) is a different operating point and was wrong by up
   to 0.163 FPR; all E2 numbers were recomputed from the stored score arrays by
   `recompute_e2.py` (no re-training, same arrays).
9. **`VERIFY.md` is a self-consistency check only** -- it re-feeds the stored arrays into
   the same metric code. `VERIFY_INDEP.md` is the independent one: AUROC by the
   Mann-Whitney rank formula (no sklearn), FPR@95 by an explicit threshold sweep, and
   known accuracy recomputed from the stored predictions. It must report 0 violations;
   `final_check.py` fails the build otherwise.
10. **Cross-domain (E3) is binary, same-crop, controlled->field, four pairs.** The label
   map keeps Raw/Ripe only; fruit12's Overripe is dropped, and the pairs are
   banana3<->banana4 plus fruit12->field4 for banana and mango. Do not describe this as
   multi-grade or cross-crop; the numbers do not support either.
11. **Paired tests carry Bonferroni and Holm columns and a verdict.** The family size is
   the number of tests in the table itself (`n_tests_in_family`); the verdict column is
   the strict Bonferroni one. An uncorrected p<0.05 among ~32 tests is what chance
   produces, so "significant" must mean "survives correction", and the count that
   survives is the finding.
12. **Cells with fewer than 30 test images on either side are marked `thin` in T3.**
   Their AUROC is still printed (dropping it would hide data) but it is *descriptive*:
   the seed-bootstrap interval in `outputs/T16b_seed_bootstrap.csv` is the number to
   quote next to it. Known-side cells whose predictions collapse to a single class are
   listed in `outputs/T15_collapsed.csv`; their `known_acc` equals the majority share by
   construction and every open-set number computed on them is an artefact of that
   collapse.
13. **The `P2c` arm is *unseen species*, not unseen cultivar.** `fruit12`'s Apple /
   Banana / Mango differ in colour, shape and texture, so its AUROC measures species
   separability. The internal view key still reads `P2c_unseen_cultivar` (renaming it
   would change every config hash and create a second arm beside the first); every table
   here prints it as `P2c_unseen_species`, and the paper must not use the word
   "cultivar" unless NinePeach is added.
""")
    L.append("\n## Failures\n")
    fp = OUT.parent / "logs" / "failures.jsonl"
    if fp.exists() and fp.stat().st_size:
        rows = []
        for line in fp.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
        if rows:
            fd = pd.DataFrame(rows)
            g = fd.groupby(["stage", "key"], dropna=False).agg(
                n_failed=("at", "size"), last_at=("at", "max"), last_err=("err", "last")).reset_index()
            g = g.sort_values("n_failed", ascending=False)
            L.append("A run that fails repeatedly is a hole in a table, not a transient. "
                     "Anything listed here is *not* in any result table above.\n")
            L.append(g.head(40).to_markdown(index=False))
            L.append("\nTotal failure records: %d, distinct keys: %d" % (len(fd), len(g)))
    else:
        L.append("No recorded failures.")
    L.append("\n## Unreadable result files\n")
    L.append("unreadable result files: %d" % len(SKIPPED))
    if SKIPPED:
        L.append("These files exist in `results/` but are in NO table below. A non-zero "
                 "count fails `final_check.py`.")
        for n, why in SKIPPED[:40]:
            L.append("- `%s` — %s" % (n, why))
    L.append("\n## Run inventory\n")
    L.append(df.groupby(["exp"]).size().to_string())
    (OUT / "REPORT.md").write_text("\n".join(L), encoding="utf-8")
    for k, t in T.items():
        t.to_csv(OUT / (k + ".csv"), index=False)
        try:
            (OUT / (k + ".md")).write_text(t.to_markdown(index=False), encoding="utf-8")
        except Exception:
            pass


def verify():
    """Consistency check: recompute E2 metrics from the stored score arrays.

    This is NOT an independent implementation of the metrics -- it calls the same
    `open_set_metrics` that produced the stored values, so it can only catch a stored
    number that no longer matches the scores it came from (e.g. after a metric fix).
    It says nothing about whether the metric definition itself is right. The docstring
    used to claim "independent re-derivation"; it overstated what this does.
    """
    msgs, bad = [], 0
    files = sorted((RESULTS / "scores").glob("*.npz"))
    # Score arrays are named by the config hash alone ("<run_id>.npz"); the run JSON that
    # owns them is "<EXP>__<dataset>__<run_id>.json". Looking up RESULTS/<stem>.json matched
    # zero files for every array, so this check skipped all of them and still printed
    # "mismatches: 0". A check that cannot fail is worse than no check.
    checked = unmatched = 0
    for f in files:
        cands = sorted(RESULTS.glob("*__%s.json" % f.stem))
        if len(cands) != 1:
            unmatched += 1
            msgs.append("NO/AMBIGUOUS JSON for score file %s (matches: %d)" % (f.name, len(cands)))
            bad += 1
            continue
        rec = read_json(cands[0])
        with np.load(f, allow_pickle=True) as z:   # close: 1800+ open fds exhaust the limit
            ks, us = np.array(z["known_scores"]), np.array(z["unknown_scores"])
            kc = (z["known_pred"] == z["known_labels"]) if ("known_pred" in z) else None
            if kc is not None:
                kc = np.array(kc)
        met = open_set_metrics(ks, us, known_correct=kc)
        for k in ("auroc", "fpr95", "oscr"):
            if abs(met[k] - rec["metrics"][k]) > 1e-9:
                bad += 1
                msgs.append("MISMATCH %s %s stored=%.10f recomputed=%.10f" % (f.name, k, rec["metrics"][k], met[k]))
        checked += 1
    msgs.append("E2 score files: %d on disk, %d resolved to their run JSON, %d unmatched; metric mismatches: %d"
                % (len(files), checked, unmatched, bad))
    if len(files) and checked == 0:
        msgs.append("VACUOUS CHECK: no score file could be resolved, so nothing was verified")
    # sanity: label counts
    for cp in sorted(PROC.glob("*/card.json")):
        c = read_json(cp)
        if c["group_leak_count"] != 0:
            msgs.append("LEAK %s" % c["dataset"]); bad += 1
    txt = "\n".join(msgs)
    (OUT / "VERIFY.md").write_text(txt, encoding="utf-8")
    print(txt)
    return bad


def main():
    df = load_runs()
    if len(df) == 0:
        print("no results yet"); return
    df.to_csv(OUT / "master.csv", index=False, encoding="utf-8")
    T = tables(df)
    tests = paired_tests(df)
    if len(tests):
        tests.to_csv(OUT / "T5_paired_tests.csv", index=False)
    figures(df, T)
    write_report(df, T, tests)
    verify()
    print("runs:", len(df), "outputs ->", OUT)


if __name__ == "__main__":
    main()
