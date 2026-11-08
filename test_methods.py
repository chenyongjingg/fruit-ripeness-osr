#!/usr/bin/env python3
"""Checks for the two instruments that are not covered by the pipeline's own tables:

  * the CORN ordinal head (E4 ablation) -- probabilities must be a proper distribution
    and must reproduce the conditional algebra by hand;
  * the Mahalanobis open-set scorer -- the fast BLAS form used in production must agree
    with the direct quadratic form to well below the reported precision.

An instrument that is never checked against a hand-computable case is a second
uncalibrated ruler: it produces numbers, tables and a paragraph of interpretation without
anyone knowing whether they mean what the plan says they mean.
"""
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.methods import CORNHead, make_head, MahalanobisScorer

FAILS = []
STATUS = []


def ck(name, ok, detail=""):
    print(("PASS %-52s %s" if ok else "FAIL %-52s %s") % (name, detail))
    STATUS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name)


def check_corn(rng):
    order = ["Unripe", "SemiRipe", "Ripe", "Overripe"]
    K = len(order)
    n = 400
    # 1-D ordinal structure: the class index moves the mean along axis 0.
    y = np.array([order[i] for i in rng.randint(0, K, n)])
    yy = np.array([order.index(v) for v in y])
    X = rng.randn(n, 6).astype(np.float32)
    X[:, 0] += 2.0 * yy
    tr, te = slice(0, 250), slice(250, n)
    h = CORNHead(C=1.0, order=order).fit(X[tr], y[tr])

    P = h.proba(X[te])
    ck("corn: proba rows sum to 1", np.allclose(P.sum(1), 1.0, atol=1e-10),
       "max|sum-1|=%.2e" % float(np.abs(P.sum(1) - 1).max()))
    ck("corn: proba non-negative", bool((P >= -1e-12).all()))

    # the composition must equal the conditional algebra, recomputed from the stored S_j
    S = h._S(X[te])
    ck("corn: P(K-1) == prod(S)", np.allclose(P[:, K - 1], S.prod(1), atol=1e-10),
       "max|d|=%.2e" % float(np.abs(P[:, K - 1] - S.prod(1)).max()))
    ck("corn: P(0) == 1 - S_0", np.allclose(P[:, 0], 1 - S[:, 0], atol=1e-10))

    # each S_j must track the empirical conditional rate P(y>j | y>=j) on held-out data
    yy_te = np.array([order.index(v) for v in y[te]])
    emp, pred_rate = [], []
    for j in range(K - 1):
        m = yy_te >= j
        emp.append(float((yy_te[m] > j).mean()) if m.sum() else float("nan"))
        pred_rate.append(float(S[m, j].mean()))
    ck("corn: conditional tasks calibrated to their subsets",
       all(abs(pred_rate[j] - emp[j]) < 0.15 for j in range(K - 1)),
       "pred=%s data=%s" % (np.round(pred_rate, 3), np.round(emp, 3)))

    # separable data must be classified exactly; shuffled labels must not.
    Xs = np.vstack([np.full((50, 2), float(i)) + rng.randn(50, 2) * 0.05
                    for i in range(K)])
    ys = np.array([order[i] for i in range(K) for _ in range(50)])
    hs = CORNHead(C=1.0, order=order).fit(Xs, ys)
    acc = float((hs.predict(Xs) == ys).mean())
    ck("corn: separated grades -> accuracy 1.0", acc == 1.0, "acc=%.4f" % acc)

    ysh = ys.copy(); rng.shuffle(ysh)
    hsh = CORNHead(C=1.0, order=order).fit(Xs, ysh)
    acc_sh = float((hsh.predict(Xs) == ys).mean())
    ck("corn: shuffled labels do not reproduce grades", acc_sh < 0.5, "acc=%.4f" % acc_sh)

    pred_idx = np.array([order.index(v) for v in hs.predict(Xs)])
    ck("corn: prediction index non-decreasing in grade",
       bool(np.all(np.diff(pred_idx) >= 0)), "idx=%s" % list(pred_idx[::50]))

    try:
        make_head("conr")
        ck("corn: make_head rejects unknown head names", False, "no exception")
    except ValueError:
        ck("corn: make_head rejects unknown head names", True)


def check_mahal(rng):
    """The production scorer (_fast form_) must equal the textbook quadratic form."""
    n, d = 600, 64            # small d: the direct form is affordable here
    classes = np.array(["A", "B", "C"])
    ys = np.array([classes[i % 3] for i in range(n)])
    Xs = rng.randn(n, d).astype(np.float32) + np.repeat(
        [[0.0] * d, [1.0] * d, [2.0] * d], n // 3, axis=0).astype(np.float32)
    X = rng.randn(200, d).astype(np.float32)
    sc = MahalanobisScorer(Xs, ys)
    fast = sc.score(X)

    # direct reference: build the same Ledoit-Wolf precision independently
    from sklearn.covariance import LedoitWolf
    ci = np.searchsorted(sc.classes, ys)
    R = Xs - sc.mu[ci]
    prec = LedoitWolf().fit(R).precision_
    ck("mahal: precision reused, not refitted",
       np.allclose(prec, sc.prec, atol=1e-12),
       "max|d|=%.2e" % float(np.abs(prec - sc.prec).max()))
    direct = np.empty((X.shape[0], len(sc.classes)))
    for i, m in enumerate(sc.mu):
        dif = X - m
        direct[:, i] = np.array([float(v @ prec @ v) for v in dif])
    d_max = float(np.abs(fast - (-direct.min(1))).max())
    scale = float(np.abs(direct.min(1)).max())
    ck("mahal: fast form agrees with the quadratic form (rel < 1e-5)", d_max <= 1e-5 * scale,
       "max|d|=%.2e (scale %.2e)" % (d_max, scale))

    # a positive control: an in-distribution point must score better than a far one
    near = sc.score(Xs[:5]); far = sc.score((Xs[:5] + 50.0).astype(np.float32))
    ck("mahal: far points score lower than support points",
       bool((far < near).all()), "near=%s far=%s" % (np.round(near[:3], 2), np.round(far[:3], 2)))


def main():
    rng = np.random.RandomState(0)
    check_corn(rng)
    check_mahal(rng)
    print("\nFAILURES: %d" % len(FAILS))
    # Persist the verdict: final_check.py asserts the file exists, reports 0 failures and
    # carries PASS lines for the named checks, so "the instruments were checked" is a
    # checkable claim rather than a sentence in a handover document.
    try:
        from rio.common import OUT
        body = ["FAILURES: %d" % len(FAILS), "checks: %d" % len(STATUS)]
        body += ["%s: %s" % (n, "PASS" if ok else "FAIL") for n, ok in STATUS]
        (OUT / "METHODS_SELFTEST.txt").write_text("\n".join(body) + "\n", encoding="utf-8")
    except Exception as e:
        print("could not persist verdict: %s" % e)
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
