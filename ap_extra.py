#!/usr/bin/env python3
"""Per-class average precision for the closed-set arm (plan §4 metric list).

The plan asks for Accuracy / macro-F1 / **per-class AP** (its own gloss: "应对长尾") /
off-by-one / weighted macro-F1. E1 stores only hard predictions, and AP needs scores, so
it cannot be recovered from the existing records without re-fitting. This script re-fits
exactly the same cells (same view subset, same support selection, same seeds, same heads)
and writes them under a **different experiment key, `E1ap`**, so not one existing run id
moves and `report.py`'s tables -- which filter `exp == "E1"` -- are untouched.

AP is computed one-vs-rest per class with sklearn's `average_precision_score` and
averaged over the classes present in the test split. Both the per-class map and the
macro average are stored; the macro average is what T2b reports.

The instrument is checked against cases whose answer is known without the pipeline
(`--self-test`): a perfect scorer gives AP = 1.0 for every class, and uninformative
scores give AP ≈ class prevalence, i.e. macro AP ≈ 1/C on a balanced problem. A metric
that is never checked against a hand-computable case is a second uncalibrated ruler.
"""
import sys, json, argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run as R
from rio.common import OUT, RESULTS, log
from rio.experiments import (aligned, balanced_support, make_head, save_result, already,
                             read_json, result_path, sha256_ids)


def _macro_ap(y, P, classes):
    ap = {}
    for i, c in enumerate(classes):
        ap[str(c)] = float(average_precision_score((y == c).astype(int), P[:, i]))
    present = [c for c in classes if (y == c).sum() > 0]
    return float(np.mean([ap[str(c)] for c in present])), ap, present


def self_test():
    rng = np.random.RandomState(0)
    n, C = 900, 3
    y = np.array([str(i % C) for i in range(n)])
    # 1. uninformative scores: macro AP must land near 1/C on balanced data
    P_rand = rng.rand(n, C); P_rand /= P_rand.sum(1, keepdims=True)
    m_rand, ap_rand, _ = _macro_ap(y, P_rand, sorted(set(y)))
    # 2. perfect scores: AP = 1.0 for every class
    P_perf = np.zeros((n, C)); P_perf[np.arange(n), [int(t) for t in y]] = 1.0
    m_perf, ap_perf, _ = _macro_ap(y, P_perf, sorted(set(y)))
    # 3. a systematically WRONG scorer must fall BELOW prevalence.
    #    It has to be built by permuting the classes, not by `1 - P_perf`: the latter
    #    gives every negative the same score and every positive the same score, i.e. one
    #    giant tie block, and a tie block scores exactly prevalence -- which says nothing
    #    about the metric (it is the degenerate case). A soft permutation has no ties.
    perm = np.argsort(np.roll(np.arange(C), 1))
    P_bad = 0.9 * P_perf[:, perm] + 0.1 * P_rand
    m_inv, _, _ = _macro_ap(y, P_bad, sorted(set(y)))
    print("self-test: random macro AP %.4f (chance %.4f) | perfect %.4f | wrong-class %.4f"
          % (m_rand, 1.0 / C, m_perf, m_inv))
    ok = abs(m_rand - 1.0 / C) < 0.05 and m_perf == 1.0 and m_inv < 1.0 / C - 0.02
    print("SELF-TEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def e1_ap(ds, enc, subset_fn, ordinal, head_kind="linear", shot=5, seed=0, variant="cls",
          C=1.0, tag=""):
    cfg = {"exp": "E1ap", "dataset": ds, "view": tag, "encoder": enc, "variant": variant,
           "head": head_kind, "shot": shot, "seed": seed, "C": C}
    if already(cfg):
        return read_json(result_path(cfg))
    X, m = aligned(ds, enc, variant, subset_fn, key=tag)
    labels = [c for c in ordinal if c in set(m["label_name"])]
    keep = m["label_name"].isin(labels).values
    X, m = X[keep], m[keep].reset_index(drop=True)
    if len(m) == 0:
        return None
    sup_idx, per = balanced_support(m, labels, shot, seed)
    te = (m["split"] == "test").values
    if len(sup_idx) == 0 or te.sum() == 0:
        return None
    tr = m.loc[sup_idx]
    head = make_head(head_kind, C=C).fit(X[sup_idx], tr["label_name"].values)
    P = head.proba(X[te])
    y = m["label_name"].values[te]
    macro, ap, present = _macro_ap(y, P, list(head.classes_))
    met = {"macro_ap": macro, "per_class_ap": ap,
           "prevalence_macro": float(np.mean([(y == c).mean() for c in present])),
           "n_support": int(len(tr)), "n_test": int(te.sum()),
           "support_ids_sha256": sha256_ids(tr["id"].values),
           "test_ids_sha256": sha256_ids(m.loc[te, "id"].values)}
    return save_result(cfg, met)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--encoders", default="dinov2_s,dinov2_b,clip_b,resnet50")
    ap.add_argument("--variants", default="cls")
    ap.add_argument("--heads", default="linear,proto")
    ap.add_argument("--shot", default="1,5,10,50,all")
    ap.add_argument("--seeds", default="0,1,2,3,4")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    encs = [x for x in a.encoders.split(",") if x]
    variants = [x for x in a.variants.split(",") if x]
    heads = [x for x in a.heads.split(",") if x]
    shots = [None if x == "all" else int(x) for x in a.shot.split(",") if x]
    seeds = [int(x) for x in a.seeds.split(",") if x]
    V = R.views()
    n_done = n_skip = 0
    for vname, v in V.items():
        if not v.get("e1", True):          # P3-only views (ffr, f360rot) are not closed-set
            continue
        ds, ordn = v["ds"], v["ordinal"]
        for enc in encs:
            if not (R.FEAT / ("%s__%s.npz" % (ds, enc))).exists():
                continue
            for var in variants:
                for hk in heads:
                    for shot in shots:
                        for s in seeds:
                            try:
                                r = e1_ap(ds, enc, v["subset"], ordn, head_kind=hk, shot=shot,
                                          seed=s, variant=var, tag=vname)
                                n_done += 1 if r is not None else 0
                                n_skip += 1 if r is None else 0
                            except Exception as e:
                                log("[E1ap] FAIL %s %s %s shot=%s seed=%s: %s"
                                    % (vname, enc, hk, shot, s, e))
    log("[E1ap] done ok=%d skipped=%d" % (n_done, n_skip))
    # a flat table, so the numbers are readable without re-deriving them from master.csv
    rows = []
    for p in sorted(RESULTS.glob("E1ap__*.json")):
        r = read_json(p)
        c, m = r["config"], r["metrics"]
        rows.append({"view": c["view"], "encoder": c["encoder"], "variant": c["variant"],
                     "head": c["head"], "shot": c["shot"], "seed": c["seed"],
                     "macro_ap": m["macro_ap"], "prevalence_macro": m["prevalence_macro"],
                     "n_test": m["n_test"]})
    if rows:
        d = pd.DataFrame(rows)
        g = d.groupby(["view", "encoder", "variant", "head", "shot"], dropna=False)
        t = g.apply(lambda x: pd.Series({
            "macro_ap": "%.4f ± %.4f" % (x["macro_ap"].mean(),
                                         x["macro_ap"].std(ddof=1) if len(x) > 1 else 0.0),
            "chance": "%.4f" % x["prevalence_macro"].mean(),
            "n_runs": len(x)})).reset_index()
        t.to_csv(OUT / "T2b_per_class_ap.csv", index=False)   # exists_ok default; plain write
        log("[E1ap] wrote %s (%d rows)" % (OUT / "T2b_per_class_ap.csv", len(t)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
