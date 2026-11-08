"""Adaptation heads, open-set scorers, and metrics. All training uses support data only."""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, f1_score, confusion_matrix
from sklearn.covariance import LedoitWolf


def l2norm(x):
    n = np.linalg.norm(x, axis=1, keepdims=True)
    n[n == 0] = 1.0
    return x / n


class LinearHead:
    def __init__(self, C=1.0):
        self.C = C
        self.clf = None

    def fit(self, X, y):
        self.clf = LogisticRegression(C=self.C, max_iter=5000, solver="lbfgs",
                                      n_jobs=1)
        self.clf.fit(X, y)
        self.classes_ = self.clf.classes_
        return self

    def logits(self, X):
        d = self.clf.decision_function(X)
        if d.ndim == 1:
            d = np.stack([-d, d], 1)
        return d

    def predict(self, X):
        return self.classes_[np.argmax(self.logits(X), 1)]

    def proba(self, X):
        z = self.logits(X)
        z = z - z.max(1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(1, keepdims=True)


class ProtoHead:
    """Cosine prototype head with learnable-free temperature (fixed 10)."""
    def __init__(self, tau=10.0):
        self.tau = tau

    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.P = np.stack([l2norm(X[y == c]).mean(0) for c in self.classes_], 0)
        self.P = l2norm(self.P)
        return self

    def logits(self, X):
        return (l2norm(X) @ self.P.T) * self.tau

    def predict(self, X):
        return self.classes_[np.argmax(self.logits(X), 1)]

    def proba(self, X):
        z = self.logits(X)
        z = z - z.max(1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(1, keepdims=True)


class CORNHead:
    """CORN (conditional ordinal regression, Shi et al. 2023): the plan's ordinal head.

    K-1 binary tasks over the ordered grades. Task j is fitted **only on support
    samples with y >= j** and predicts S_j = P(y > j | y >= j). Inference composes the
    conditional probabilities into a proper distribution:

        P(y = 0)     = 1 - S_0
        P(y = k)     = S_0 ... S_{k-1} * (1 - S_k)     1 <= k <= K-2
        P(y = K - 1) = S_0 ... S_{K-2}

    The probabilities telescope to 1 exactly, so `proba()` is a distribution and the
    same MSP/energy scores can be computed from it. The point of the head is that it
    never treats the grades as unordered: a boundary between far-apart grades is a
    different quantity from one between neighbours.

    Degenerate task (all support labels on one side): the constant conditional rate is
    used instead of a fit, rather than dropping the task -- dropping it would silently
    change the composition and its normalisation.
    """

    def __init__(self, C=1.0, order=None):
        self.C = C
        self.order = list(order) if order is not None else None

    def fit(self, X, y):
        y = np.asarray(y).astype(str)
        if self.order is None:          # only reachable if a caller forgot to pass order
            self.order = sorted(set(y))
        self.order = [c for c in self.order if c in set(y)] or list(sorted(set(y)))
        self.classes_ = np.array(self.order)
        pos = {c: i for i, c in enumerate(self.order)}
        yy = np.array([pos[v] for v in y])
        self.models, self.consts = [], []
        for j in range(len(self.order) - 1):
            m = yy >= j
            if m.sum() == 0:
                self.models.append(None); self.consts.append(0.0); continue
            tgt = (yy[m] > j).astype(int)
            if tgt.min() == tgt.max():          # no contrast -> constant
                self.models.append(None); self.consts.append(float(tgt[0])); continue
            clf = LogisticRegression(C=self.C, max_iter=5000, solver="lbfgs", n_jobs=1)
            clf.fit(X[m], tgt)
            self.models.append(clf); self.consts.append(None)
        return self

    def _S(self, X):
        K = len(self.order)
        S = np.ones((X.shape[0], max(K - 1, 1)))
        for j in range(K - 1):
            m = self.models[j]
            S[:, j] = m.predict_proba(X)[:, 1] if m is not None else self.consts[j]
        return S

    def proba(self, X):
        S = self._S(X)
        K = len(self.order)
        P = np.zeros((X.shape[0], K))
        P[:, 0] = 1.0 - S[:, 0]
        for k in range(1, K - 1):
            P[:, k] = np.prod(S[:, :k], axis=1) * (1.0 - S[:, k])
        if K > 1:
            P[:, K - 1] = np.prod(S, axis=1)
        return P

    def logits(self, X):
        P = np.clip(self.proba(X), 1e-12, 1.0)
        return np.log(P)

    def predict(self, X):
        return np.asarray(self.order)[np.argmax(self.proba(X), 1)]


def make_head(kind, C=1.0, order=None):
    """order: the ordinal grade list. Only CORN uses it; passing it to the other heads is
    harmless, so every call site can pass it unconditionally."""
    if kind == "linear":
        return LinearHead(C=C)
    if kind == "proto":
        return ProtoHead()
    if kind == "corn":
        return CORNHead(C=C, order=order)
    raise ValueError("unknown head %r (expected linear|proto|corn)" % (kind,))


# ---------------- open-set scores ----------------
def score_msp(head, X):
    p = head.proba(X)
    return p.max(1)


def score_energy(head, X, T=1.0):
    z = head.logits(X) * T
    m = z.max(1, keepdims=True)
    return m[:, 0] + np.log(np.exp(z - m).sum(1))


class MahalanobisScorer:
    """Class-conditional Gaussians with a shared, shrunk within-class covariance.

    Fit once per support set (X, y); score() returns -min_c squared Mahalanobis distance
    (larger = closer to the known-class manifold = more in-distribution).
    """

    def __init__(self, Xs, ys, shrink=True):
        self.classes = np.unique(ys)
        self.mu = np.stack([Xs[ys == c].mean(0) for c in self.classes])
        ci = np.searchsorted(self.classes, ys)
        R = Xs - self.mu[ci]
        d = Xs.shape[1]
        if shrink:
            self.prec = LedoitWolf().fit(R).precision_
        else:
            C = R.T @ R / max(len(R), 1) + 1e-3 * np.eye(d)
            self.prec = np.linalg.pinv(C)

    def score(self, X):
        # d(x,c) = (x-mu_c)^T P (x-mu_c). Written as one BLAS matmul + a row dot instead
        # of a three-operand einsum: the einsum does not lower to BLAS and ran at ~0.7
        # core, which made ONE fruits-360 Mahalanobis cell take ~8 minutes and was the
        # only thing bounding the P2/P3 arms. Measured 60.7 s -> 0.27 s (227x) on
        # 7440x2048 float32 here; the two formulas agree to 1.1e-6 relative, which is
        # below the 4-decimal resolution of every reported metric (test_methods.py
        # asserts the equivalence).
        D = np.empty((X.shape[0], len(self.classes)), dtype=np.float64)
        for i, m in enumerate(self.mu):
            dif = X - m
            D[:, i] = np.einsum("ij,ij->i", dif @ self.prec, dif)
        return -D.min(1)


def score_mahalanobis(head, Xs, ys, X, shrink=True):
    return MahalanobisScorer(Xs, ys, shrink).score(X)


class KNNScorer:
    def __init__(self, Xs, ys, k=5):
        self.Xs = l2norm(Xs)
        self.k = min(k, len(self.Xs))

    def score(self, X):
        S = l2norm(X) @ self.Xs.T
        part = np.partition(-S, self.k - 1, axis=1)[:, :self.k]
        return (-part).mean(1)


def score_knn(Xs, ys, X, k=5):
    Xs_ = l2norm(Xs); X_ = l2norm(X)
    S = X_ @ Xs_.T
    k = min(k, S.shape[1])
    part = np.partition(-S, k - 1, axis=1)[:, :k]
    return (-part).mean(1)  # mean top-k cosine similarity to support (higher = more in-distribution)


# ---------------- metrics ----------------
def closed_set_metrics(y_true, y_pred, ordinal_order):
    """ordinal_order: list of class labels in ordinal sequence (off-scale excluded)."""
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    acc = float((y_true == y_pred).mean())
    macro = float(f1_score(y_true, y_pred, average="macro", labels=list(ordinal_order), zero_division=0))
    pos = {c: i for i, c in enumerate(ordinal_order)}
    mask = np.array([t in pos and p in pos for t, p in zip(y_true, y_pred)])
    if mask.sum() > 0:
        d = np.array([abs(pos[t] - pos[p]) for t, p in zip(y_true[mask], y_pred[mask])])
        off1 = float((d == 1).mean()); mae = float(d.mean())
        weighted_f1 = _weighted_f1(y_true[mask], y_pred[mask], pos)
    else:
        off1, mae, weighted_f1 = float("nan"), float("nan"), float("nan")
    # per-class recall
    per = {}
    for c in np.unique(y_true):
        m = y_true == c
        per[str(c)] = float((y_pred[m] == c).mean())
    return {"acc": acc, "macro_f1": macro, "off_by_one_rate": off1,
            "ordinal_mae": mae, "weighted_f1": weighted_f1, "per_class_recall": per,
            "n": int(len(y_true))}


def _weighted_f1(y_true, y_pred, pos):
    labels = sorted(pos, key=lambda c: pos[c])
    f1s, ws = [], []
    for i, c in enumerate(labels):
        tp = np.sum((y_pred == c) & (y_true == c))
        fp = np.sum((y_pred == c) & (y_true != c))
        fn = np.sum((y_pred != c) & (y_true == c))
        f1 = 0.0 if (2 * tp + fp + fn) == 0 else 2 * tp / (2 * tp + fp + fn)
        f1s.append(f1)
        ws.append(1.0 / (1.0 + min(i, len(labels) - 1 - i)))
    f1s = np.array(f1s); ws = np.array(ws)
    return float((f1s * ws).sum() / ws.sum())


def open_set_metrics(known_scores, unknown_scores, known_correct=None):
    """known_correct: optional bool array; if given, OSCR/CCR count only correctly classified accepted knowns
    (standard OSCR definition)."""
    ks = np.asarray(known_scores, dtype=float)
    us = np.asarray(unknown_scores, dtype=float)
    y = np.r_[np.ones(len(ks)), np.zeros(len(us))]
    s = np.r_[ks, us]
    auroc = float(roc_auc_score(y, s))
    # FPR at 95% TPR.
    # The operating point is the LARGEST threshold at which at least 95% of the knowns
    # are still accepted (any higher threshold drops below 95% TPR). This used to be
    # np.percentile(ks, 5), which is not that point: with an interpolated percentile it
    # can yield TPR < 95% (e.g. 90/95 = 0.947) and, when scores have ties, can sit a whole
    # tie-block away from the crossing; measured deltas against an independent sweep went
    # up to 0.163 FPR. Definition and code now agree.
    ks_s = np.sort(ks)
    nk0 = max(len(ks_s), 1)
    cand = np.unique(s)
    lo, hi, ti = 0, len(cand) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        t = cand[mid]
        tpr = (nk0 - np.searchsorted(ks_s, t, side="left")) / nk0
        if tpr >= 0.95:
            ti = mid
            lo = mid + 1
        else:
            hi = mid - 1
    thr95 = float(cand[ti]) if ti >= 0 else float(np.max(s))
    fpr95 = float((us >= thr95).mean())
    tpr95 = float((ks >= thr95).mean())
    # OSCR curve over sorted thresholds
    # Build the effective label vector BEFORE sorting: knowns occupy indices [0, nk),
    # so a mask on the unsorted vector is the only correct way to mark them.
    y_eff = y.copy()
    if known_correct is not None:
        kc = np.asarray(known_correct, dtype=bool)
        y_eff[:len(kc)][~kc] = -1  # an accepted-but-misclassified known is not a true accept
    order = np.argsort(-s)
    s_sorted = s[order]; y_sorted = y[order]; ye_sorted = y_eff[order]
    cum_known = np.cumsum(ye_sorted == 1)
    cum_unk = np.cumsum(y_sorted == 0)
    nk, nu = len(ks), len(us)
    ccr = cum_known / max(nk, 1)
    fpr = cum_unk / max(nu, 1)
    # prepend origin
    ccr = np.r_[0.0, ccr]; fpr = np.r_[0.0, fpr]
    _trapz = getattr(np, 'trapezoid', None) or np.trapz
    oscr = float(_trapz(ccr, fpr))
    # CCR at FPR<=5%
    idx = np.searchsorted(fpr, 0.05, side="right") - 1
    ccr5 = float(ccr[max(idx, 0)])
    return {"auroc": auroc, "fpr95": fpr95, "tpr_at_fpr95": tpr95, "oscr": oscr,
            "ccr_at_fpr5": ccr5, "n_known": int(nk), "n_unknown": int(nu)}


def per_class_rejection(y_known, scores_known, threshold):
    """Fraction of each known class rejected at a global threshold (for the adjacent-grade hypothesis)."""
    out = {}
    for c in np.unique(y_known):
        m = y_known == c
        out[str(c)] = float((scores_known[m] < threshold).mean())
    return out
