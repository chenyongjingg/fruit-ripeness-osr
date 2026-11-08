#!/usr/bin/env python3
"""Independent re-derivation of the open-set metrics.

`report.py:verify()` re-feeds the stored score arrays into the SAME `open_set_metrics`
that produced the numbers, so it can only catch a stale file. This script implements the
metrics a second time, from the definitions, and compares:

  AUROC   -- rank (Mann-Whitney U) formulation, no sklearn
  FPR@95  -- explicit threshold sweep: the smallest FPR over thresholds whose TPR >= 95%
             (the original uses the 5th percentile of the known scores; with ties the two
             can differ by up to one sample, so the tolerance is tied to 1/n_unknown)
  known accuracy -- recomputed from the stored predictions, compared to the stored value
  sizes   -- array lengths vs the stored n_known / n_unknown

OSCR is defined over a discrete ROC curve, so "independent" is not well-defined; the
script recomputes it with a right-continuous step rule and only reports the deviation.
Exit code is non-zero if anything exceeds tolerance.
"""
import json, sys
from pathlib import Path
import numpy as np
from scipy.stats import rankdata

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import OUT, RESULTS, log


def auroc_rank(ks, us):
    """P(known > unknown) + 0.5 P(tie), via average ranks (Mann-Whitney U)."""
    n1, n0 = len(ks), len(us)
    r = rankdata(np.r_[ks, us])
    R1 = r[:n1].sum()
    return (R1 - n1 * (n1 + 1) / 2.0) / (n1 * n0)


def fpr_at_95(ks, us):
    """Smallest FPR among thresholds that accept >= 95% of the knowns."""
    ks_s = np.sort(ks)
    n = len(ks_s)
    # candidate thresholds: every distinct score; TPR(t) = #{ks >= t}/n
    cand = np.unique(np.r_[ks, us])
    # TPR is non-increasing in t -> binary search for the largest t with TPR >= .95
    lo, hi, best = 0, len(cand) - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        t = cand[mid]
        tpr = (n - np.searchsorted(ks_s, t, side="left")) / n
        if tpr >= 0.95:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    t = cand[best]
    return float((us >= t).mean())


def oscr_step(ks, us, kc):
    """OSCR with a right-continuous step rule (different from the trapezoid used upstream)."""
    y = np.r_[np.ones(len(ks)), np.zeros(len(us))]
    s = np.r_[ks, us]
    ye = y.copy()
    if kc is not None:
        ye[:len(kc)][~np.asarray(kc, bool)] = -1
    o = np.argsort(-s, kind="mergesort")
    s, y, ye = s[o], y[o], ye[o]
    nk, nu = len(ks), len(us)
    ccr = np.cumsum(ye == 1) / max(nk, 1)
    fpr = np.cumsum(y == 0) / max(nu, 1)
    ccr = np.r_[0.0, ccr]; fpr = np.r_[0.0, fpr]
    # right-continuous step area: sum over each horizontal segment
    area = 0.0
    for i in range(len(fpr) - 1):
        area += (fpr[i + 1] - fpr[i]) * ccr[i + 1]
    return float(area)


def main():
    files = sorted((RESULTS / "scores").glob("*.npz"))
    bad, checked, unresolved = [], 0, 0
    worst = {"auroc": (0.0, ""), "fpr95": (0.0, ""), "oscr": (0.0, ""), "acc": (0.0, "")}
    for f in files:
        cands = sorted(RESULTS.glob("*__%s.json" % f.stem))
        if len(cands) != 1:
            unresolved += 1
            bad.append("UNRESOLVED %s" % f.name)
            continue
        rec = json.loads(Path(cands[0]).read_text())
        met = rec.get("metrics", {})
        with np.load(f, allow_pickle=True) as z:
            ks = np.array(z["known_scores"], float)
            us = np.array(z["unknown_scores"], float)
            kp = np.array(z["known_pred"]) if "known_pred" in z else None
            kl = np.array(z["known_labels"]) if "known_labels" in z else None
        kc = (kp == kl) if (kp is not None and kl is not None) else None
        checked += 1

        a = auroc_rank(ks, us)
        d = abs(a - met["auroc"])
        if d > worst["auroc"][0]:
            worst["auroc"] = (d, f.name)
        if d > 1e-9:
            bad.append("AUROC %s stored=%.6f indep=%.6f" % (f.name, met["auroc"], a))

        fp = fpr_at_95(ks, us)
        d = abs(fp - met["fpr95"])
        if d > worst["fpr95"][0]:
            worst["fpr95"] = (d, f.name)
        if d > max(2.0 / max(len(us), 1), 1e-9):
            bad.append("FPR95 %s stored=%.6f indep=%.6f (n_uk=%d)" % (f.name, met["fpr95"], fp, len(us)))

        if kc is not None and "known_acc" in met:
            acc = float(kc.mean())
            d = abs(acc - met["known_acc"])
            if d > worst["acc"][0]:
                worst["acc"] = (d, f.name)
            if d > 1e-9:
                bad.append("ACC %s stored=%.6f indep=%.6f" % (f.name, met["known_acc"], acc))

        if "oscr" in met:
            o = oscr_step(ks, us, kc)
            d = abs(o - met["oscr"])
            if d > worst["oscr"][0]:
                worst["oscr"] = (d, f.name)

        for k, n in (("n_known", len(ks)), ("n_unknown", len(us))):
            if k in met and int(met[k]) != n:
                bad.append("SIZE %s %s stored=%s array=%d" % (f.name, k, met[k], n))

    lines = ["# Independent metric re-derivation", "",
             "AUROC (rank form, no sklearn), FPR@95 (threshold sweep), known accuracy and",
             "array sizes, recomputed from `results/scores/*.npz` and compared with the stored",
             "values. OSCR is definition-sensitive (discrete ROC); only its deviation under a",
             "right-continuous step rule is reported.", "",
             "checked: %d arrays, unresolved: %d, violations: %d" % (checked, unresolved, len(bad)),
             "worst |diff|: auroc %.2e (%s), fpr95 %.2e (%s), known_acc %.2e (%s), oscr-step %.2e (%s)"
             % (worst["auroc"][0], worst["auroc"][1], worst["fpr95"][0], worst["fpr95"][1],
                worst["acc"][0], worst["acc"][1], worst["oscr"][0], worst["oscr"][1]), ""]
    lines += bad[:50]
    if len(bad) > 50:
        lines.append("... and %d more" % (len(bad) - 50))
    txt = "\n".join(lines)
    (OUT / "VERIFY_INDEP.md").write_text(txt, encoding="utf-8")
    print(txt)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
