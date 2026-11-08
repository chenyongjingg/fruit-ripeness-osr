#!/usr/bin/env python3
"""Ordinal cost-weighted macro-F1 (plan v1.3 line 98 / 5.3).

The plan asks the main closed-set table to report **off-by-one rate** AND a
**weighted macro-F1 whose cost is 1 for an adjacent-grade error and 2 for a
skipped grade**.  Two facts made this a real gap rather than a formatting one:

1. `report.py`'s T2 never printed any weighted F1, so the plan's metric was
   absent from every table.
2. `rio.methods._weighted_f1` -- the only function with a matching name -- does
   NOT implement the plan's definition. It weights class c by
   `1/(1 + min(i, n-1-i))`, i.e. a position weight that down-weights the two
   *edge* grades. That is a support/edge weighting, not an ordinal-distance
   cost, and printing it under the plan's label would be a mislabelled number.
   It is left untouched (some runs already carry it) and is not reported.

Definition implemented here, chosen so that the plan's 1:2 ratio is honoured and
the metric survives hand computation:

    credit(a, b) = 1.0 if a == b
                 = 0.5 if |grade(a) - grade(b)| == 1     (cost 1 -> credit 1/2)
                 = 0.0 otherwise                        (cost 2 -> credit 0)
    R_c = mean credit over samples whose true grade is c
    P_c = mean credit over samples predicted as c
    F1_c = 2PR/(P+R)  (0 when P+R == 0)
    cost_f1 = mean of F1_c over the ordinal classes

Penalty ratio between an adjacent and a skipped grade is (1-0.5):(1-0) = 1:2,
exactly the plan's weights. Averaging over the ordinal class list (including a
class absent from the test split, which then contributes F1=0) matches how
`macro_f1` is computed upstream, so the two numbers are directly comparable.

Hard predictions, not probabilities, are needed; E1 does not keep them. This
script re-fits exactly the same cells as `rio.experiments.e1` (same view subset,
support selection, seeds, heads, C) under a **new experiment key `E1ord`**, so no
existing run id moves and every table that filters `exp == "E1"` is unchanged.
As a by-product it recomputes acc and macro-F1 from the re-fitted head and
compares them to the stored E1 values: if `E1ord` disagreed with `E1` anywhere,
the new metric would be measuring a different pipeline, so that comparison is
treated as a gate, not a note.
"""
import sys, argparse
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run as R
from rio.common import OUT, RESULTS, log
from rio.experiments import (aligned, balanced_support, make_head, save_result, already,
                             read_json, result_path, sha256_ids)


def credit(a, b, pos):
    d = abs(pos[a] - pos[b])
    return 1.0 if d == 0 else (0.5 if d == 1 else 0.0)


def cost_f1(y, pred, order):
    """Graded macro-F1; adjacent-grade errors count half, skipped grades zero."""
    pos = {c: i for i, c in enumerate(order)}
    y = [str(t) for t in y]; pred = [str(p) for p in pred]
    cr = np.array([credit(t, p, pos) for t, p in zip(y, pred)])
    f1s = []
    for c in order:
        tmask = np.array([t == c for t in y])
        pmask = np.array([p == c for p in pred])
        R = float(cr[tmask].mean()) if tmask.sum() else 0.0
        P = float(cr[pmask].mean()) if pmask.sum() else 0.0
        f1s.append(0.0 if P + R == 0 else 2 * P * R / (P + R))
    return float(np.mean(f1s))


def self_test():
    """Three cases whose values are computable on paper; a metric that is never
    checked against a hand-computable case is a second uncalibrated ruler."""
    # (a) perfect predictions -> every class F1 = 1
    A = ["A"] * 4 + ["B"] * 4 + ["C"] * 4
    a = cost_f1(A, A, ["A", "B", "C"])
    # (b) two classes, one of two A's predicted B (adjacent):
    #     R_A=(1+0.5)/2=3/4  P_A=1          -> F1_A=6/7
    #     R_B=1              P_B=(0.5+1+1)/3 -> F1_B=2*1*(5/6)/(11/6)=10/11
    #     macro = (6/7+10/11)/2 = 68/77 = 0.883116...
    b = cost_f1(["A", "A", "B", "B"], ["A", "B", "B", "B"], ["A", "B"])
    # (c) three classes, every prediction one grade too high in a cyclic roll
    #     A->B (adjacent, credit .5), B->C (adjacent, .5), C->A (skip, 0):
    #     R=(0.5,0.5,0) P=(0,0.5,0.5) -> F1=(0,.5,0) -> macro = 1/6
    c = cost_f1(A, ["B"] * 4 + ["C"] * 4 + ["A"] * 4, ["A", "B", "C"])
    print("self-test: perfect %.4f | hand-2class %.4f (paper 68/77) | "
          "roll-3class %.4f (paper 1/6)" % (a, b, c))
    ok = (abs(a - 1.0) < 1e-12 and abs(b - 68.0 / 77.0) < 1e-9
          and abs(c - 1.0 / 6.0) < 1e-9 and a > b > c)
    print("SELF-TEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def e1_ord(ds, enc, subset_fn, ordinal, head_kind="linear", shot=5, seed=0, variant="cls",
           C=1.0, tag=""):
    cfg = {"exp": "E1ord", "dataset": ds, "view": tag, "encoder": enc, "variant": variant,
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
    head = make_head(head_kind, C=C, order=labels).fit(X[sup_idx], tr["label_name"].values)
    pred = head.predict(X[te])
    y = m["label_name"].values[te]
    # same quantities e1 computes, so the two can be compared one-to-one
    from sklearn.metrics import f1_score
    acc = float((y == pred).mean())
    macro = float(f1_score(y, pred, average="macro", labels=list(labels), zero_division=0))
    pos = {c: i for i, c in enumerate(labels)}
    mask = np.array([t in pos and p in pos for t, p in zip(y, pred)])
    d = np.array([abs(pos[t] - pos[p]) for t, p in zip(y[mask], pred[mask])]) if mask.sum() else np.array([0])
    cf = cost_f1(y, pred, labels)
    lab = list(labels)
    conf = np.zeros((len(lab), len(lab)), dtype=int)
    for t, p in zip(y, pred):
        if str(t) in pos and str(p) in pos:
            conf[pos[str(t)], pos[str(p)]] += 1
    met = {"acc": acc, "macro_f1": macro, "cost_f1": cf,
           "off_by_one_rate": float((d == 1).mean()) if mask.sum() else float("nan"),
           "ordinal_mae": float(d.mean()) if mask.sum() else float("nan"),
           "cost_definition": "adjacent credit .5, skip 0 (plan weights 1:2), macro over ordinal classes",
           "classes": lab, "confusion": conf.tolist(),
           "n_support": int(len(tr)), "n_test": int(te.sum()),
           "support_ids_sha256": sha256_ids(tr["id"].values),
           "test_ids_sha256": sha256_ids(m.loc[te, "id"].values)}
    return save_result(cfg, met)


def cross_check():
    """E1ord must reproduce E1's acc/macro_f1 exactly: same support, same seed, same head."""
    def key(c):
        return (c.get("view"), c.get("encoder"), c.get("variant"), c.get("head"),
                str(c.get("shot")), c.get("seed"))
    e1 = {}
    for p in RESULTS.glob("E1__*.json"):
        r = read_json(p); c = r["config"]
        if str(c.get("control", "none")) != "none":
            continue
        e1[key(c)] = r["metrics"]
    n = bad = 0
    worst = (0.0, "")
    for p in RESULTS.glob("E1ord__*.json"):
        r = read_json(p); c = r["config"]; k = key(c)
        if k not in e1:
            continue
        n += 1
        for f in ("acc", "macro_f1"):
            dd = abs(float(r["metrics"][f]) - float(e1[k][f]))
            if dd > worst[0]:
                worst = (dd, "%s/%s" % (p.name, f))
            if dd > 1e-12:
                bad += 1
    return n, bad, worst


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
                                r = e1_ord(ds, enc, v["subset"], ordn, head_kind=hk, shot=shot,
                                           seed=s, variant=var, tag=vname)
                                n_done += 1 if r is not None else 0
                                n_skip += 1 if r is None else 0
                            except Exception as e:
                                log("[E1ord] FAIL %s %s %s shot=%s seed=%s: %s"
                                    % (vname, enc, hk, shot, s, e))
    log("[E1ord] done ok=%d skipped=%d" % (n_done, n_skip))
    rows = []
    for p in sorted(RESULTS.glob("E1ord__*.json")):
        r = read_json(p); c, m = r["config"], r["metrics"]
        rows.append({"view": c["view"], "encoder": c["encoder"], "variant": c["variant"],
                     "head": c["head"], "shot": c["shot"], "seed": c["seed"],
                     "acc": m["acc"], "macro_f1": m["macro_f1"], "cost_f1": m["cost_f1"],
                     "off_by_one": m["off_by_one_rate"], "ordinal_mae": m["ordinal_mae"],
                     "n_test": m["n_test"]})
    if rows:
        d = pd.DataFrame(rows)
        g = d.groupby(["view", "encoder", "variant", "head", "shot"], dropna=False)
        def ms(x, k):
            v = x[k].astype(float)
            return "%.4f ± %.4f" % (v.mean(), v.std(ddof=1) if len(v) > 1 else 0.0)
        t = g.apply(lambda x: pd.Series({"cost_f1": ms(x, "cost_f1"),
                                         "macro_f1": ms(x, "macro_f1"),
                                         "off_by_one": ms(x, "off_by_one"),
                                         "ordinal_mae": ms(x, "ordinal_mae"),
                                         "n_runs": len(x)})).reset_index()
        t.to_csv(OUT / "T2c_ordinal_cost_f1.csv", index=False)
        log("[E1ord] wrote %s (%d rows)" % (OUT / "T2c_ordinal_cost_f1.csv", len(t)))
        n, bad, worst = cross_check()
        log("[E1ord] cross-check vs E1: pairs=%d mismatches=%d worst=%.2e (%s)"
            % (n, bad, worst[0], worst[1]))
        (OUT / "E1ORD_XCHECK.txt").write_text(
            "pairs=%d mismatches=%d worst_abs_diff=%.3e (%s)\n" % (n, bad, worst[0], worst[1]),
            encoding="utf-8")
        if bad:
            log("[E1ord] FATAL: E1ord does not reproduce E1 -- cost_f1 would measure a "
                "different pipeline; refusing to certify the table")
    return 0


if __name__ == "__main__":
    sys.exit(main())
