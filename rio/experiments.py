"""Experiment drivers: closed-set few-shot (E1), open-set (E2), cross-domain (E3)."""
import json, time, traceback, hashlib
import numpy as np
import pandas as pd
from pathlib import Path
from .common import (PROC, FEAT, RESULTS, log, atomic_write_json, read_json, sha256_ids,
                     sha256_file, CODE_VERSION)
from .methods import (make_head, l2norm, score_msp, score_energy, score_mahalanobis, score_knn,
                      MahalanobisScorer, KNNScorer,
                      closed_set_metrics, open_set_metrics, per_class_rejection)

RESULTS.mkdir(parents=True, exist_ok=True)
(RESULTS / "scores").mkdir(exist_ok=True)

_cache = {}


def load_features(ds, enc):
    key = (ds, enc)
    if key in _cache:
        return _cache[key]
    z = np.load(FEAT / ("%s__%s.npz" % (ds, enc)), allow_pickle=True)
    ids = [str(i) for i in z["ids"]]
    d = {"cls": z["cls"].astype(np.float32), "mean": z["mean"].astype(np.float32), "ids": ids,
         "pos": {i: k for k, i in enumerate(ids)}}
    _cache[key] = d
    return d


_align_cache = {}


def aligned(ds, enc, variant, subset_fn=None, key=None):
    """Return X (N,d, L2-normalised) and meta (N rows, index 0..N-1), positionally aligned.

    `key` enables caching of the assembled matrix. A view's subset function is applied to
    every one of its runs, and re-assembling a 13k-image matrix per run dominated the E2
    stage; the key must uniquely identify the (dataset, encoder, variant, subset) tuple.
    """
    ck = None if key is None else (ds, enc, variant, key)
    if ck is not None and ck in _align_cache:
        return _align_cache[ck]
    f = load_features(ds, enc)
    meta = pd.read_csv(PROC / ds / "meta.csv")
    rows, feats = [], []
    for _, r in meta.iterrows():
        p = f["pos"].get(r["id"])
        if p is None:
            continue
        if subset_fn is not None and not subset_fn(r):
            continue
        rows.append(r)
        feats.append(f[variant][p])
    m = pd.DataFrame(rows).reset_index(drop=True)
    X = np.stack(feats, 0).astype(np.float32) if feats else np.zeros((0, 1), np.float32)
    out = (l2norm(X), m)
    if ck is not None:
        _align_cache[ck] = out
        if len(_align_cache) > 12:
            _align_cache.pop(next(iter(_align_cache)))
    return out


def run_id(cfg):
    return hashlib.sha1(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16]


def result_path(cfg):
    return RESULTS / (cfg["exp"] + "__" + cfg["dataset"].replace("/", "_") + "__" + run_id(cfg) + ".json")


def seal_of(ds, ordinal, view, known=None):
    """Everything needed to re-identify the data a result was computed from.

    Plan v2.0 fix #10: 0/6,952 result files recorded which version of the data they
    came from, and nothing recorded the ordinal class list -- so a change to a view
    definition would silently reinterpret old results under a new definition. This
    block is stored next to each result. It is NOT part of the config hash on purpose:
    adding it to `cfg` would mint a new run_id for every existing result and force a
    full re-run of 10k configurations. The hash keeps identifying the *experiment*;
    the seal identifies the *data it was run on*, and `already()` refuses to reuse a
    result whose seal no longer matches.
    """
    card_path = PROC / ds / "card.json"
    card = read_json(card_path) if card_path.exists() else {}
    meta = PROC / ds / "meta.csv"
    return {"view": str(view),
            # ordinal=None means "this arm has no grade scale" (P3_foreign, P3_rotten).
            # `already()` treats a None in the incoming seal as "cannot assert this key",
            # so passing it through is the same convention, not a silent omission.
            "ordinal": None if ordinal is None else [str(x) for x in ordinal],
            "known": sorted(str(x) for x in known) if known is not None else None,
            "meta_sha256": card.get("meta_sha256"),
            "meta_sha256_live": sha256_file(meta) if meta.exists() else None,
            "code_version": CODE_VERSION}


def already(cfg, seal=None):
    p = result_path(cfg)
    if not p.exists():
        return False
    if seal is None:
        return True
    try:
        rec = read_json(p)
    except Exception:
        return False
    old = rec.get("seal")
    if not old:
        # Legacy file written before sealing. seal.py backfills those; recomputing them
        # here would redraw 10k runs to fix a bookkeeping omission.
        return True
    # A None in the *incoming* seal means "this call cannot assert that key" (E3 has no
    # ordinal scale; P2_leave_one_fruit's classes are dataset indices, not grades). Skipping
    # it keeps those protocols from recomputing forever against an asserted-but-unknown value.
    drift = [k for k in ("view", "ordinal", "meta_sha256_live")
             if seal.get(k) is not None and old.get(k) != seal.get(k)]
    if drift:
        log("[drift] %s: %s changed since this result was written -> recomputing"
            % (p.name, ",".join(drift)))
        return False
    return True


def save_result(cfg, metrics, extra=None, seal=None):
    rec = {"config": cfg, "metrics": metrics, "code_version": CODE_VERSION,
           "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "extra": extra or {}}
    if seal is not None:
        rec["seal"] = seal
    atomic_write_json(result_path(cfg), rec)
    return rec


def balanced_support(meta, classes, shot, seed):
    rng = np.random.RandomState(seed)
    pool = meta[meta["split"] == "train"]
    idx, per = [], {}
    for c in classes:
        cand = pool.index[pool["label_name"] == c].values
        if len(cand) == 0:
            continue
        take = cand if (shot is None or shot >= len(cand)) else rng.choice(cand, size=shot, replace=False)
        idx.extend(list(take))
        per[c] = int(len(take))
    return np.array(idx, dtype=int), per


# ---------------------------------------------------------------- E1
def e1(ds, enc, subset_fn, ordinal, head_kind="linear", shot=5, seed=0,
       variant="cls", C=1.0, tag="", control="none"):
    cfg = {"exp": "E1", "dataset": ds, "view": tag, "encoder": enc, "variant": variant,
           "head": head_kind, "shot": shot, "seed": seed, "C": C, "control": control}
    if already(cfg, seal_of(ds, ordinal, tag)):
        return read_json(result_path(cfg))
    X, m = aligned(ds, enc, variant, subset_fn, key=tag)
    labels = [c for c in ordinal if c in set(m["label_name"])]
    keep = m["label_name"].isin(labels).values
    X, m = X[keep], m[keep].reset_index(drop=True)
    if len(m) == 0:
        return None
    sup_idx, per = balanced_support(m, labels, shot, seed)
    te_mask = (m["split"] == "test").values
    if control == "random_features":
        rng = np.random.RandomState(seed + 999)
        X = rng.randn(*X.shape).astype(np.float32)
        X = l2norm(X)
    if control == "shuffle_labels":
        # Destroy the support-label association only (test labels untouched) -> expect chance.
        #
        # This rotates the class NAMES by a non-zero offset k instead of drawing labels
        # i.i.d. per sample. The old version left about 1/C of the support labels equal to
        # their true label by chance -- with 15 support samples that is ~5 true labels,
        # enough for one seed to reach macro-F1 0.46 against a chance level of 0.33. A
        # control that leaks part of the answer is not a control. Rotation changes EVERY
        # sample's label and keeps the class multiset exactly, so the only thing the head
        # can exploit is the geometry of the features, not the labels.
        rng = np.random.RandomState(seed + 12345)
        m = m.copy()
        if len(labels) > 1:
            k = int(rng.randint(1, len(labels)))
            rot = {c: labels[(i + k) % len(labels)] for i, c in enumerate(labels)}
            m.loc[sup_idx, "label_name"] = [rot[c] for c in m.loc[sup_idx, "label_name"]]
        else:
            m.loc[sup_idx, "label_name"] = labels[0]
    if len(sup_idx) == 0 or te_mask.sum() == 0:
        return None
    tr, te = m.loc[sup_idx], m[te_mask].reset_index(drop=True)
    # order=labels is what the CORN head needs (the grade sequence); the other heads
    # ignore it, so the call site is unconditional.
    head = make_head(head_kind, C=C, order=labels).fit(X[sup_idx], tr["label_name"].values)
    pred = head.predict(X[te_mask])
    met = closed_set_metrics(te["label_name"].values, pred, labels)
    met.update({"n_support": int(len(tr)), "support_per_class": per,
                "support_ids_sha256": sha256_ids(tr["id"].values),
                "test_ids_sha256": sha256_ids(te["id"].values),
                "n_test": int(len(te))})
    return save_result(cfg, met, seal=seal_of(ds, ordinal, tag))


# ---------------------------------------------------------------- E2
def e2(ds, enc, subset_fn, ordinal, unknown_classes, protocol, score="energy", shot=None,
       seed=0, variant="cls", C=1.0, tag="", k=5, calib=False, min_te_each=1):
    cfg = {"exp": "E2", "dataset": ds, "view": tag, "encoder": enc, "variant": variant,
           "protocol": protocol, "unknown": sorted(unknown_classes), "score": score,
           "shot": shot, "seed": seed, "C": C}
    if calib:
        # Kept out of the hash unless requested, so the uncalibrated results keep their
        # run_id. The string names the *calibration pool*, and it must: the pool is part
        # of the method, so changing it has to change the hash. It previously said
        # "per_class_support_q05" while the code fitted on val -- two different methods
        # with one run_id, i.e. the stale-result trap. All results written under the old
        # string were deleted and recomputed under this one.
        cfg["calib"] = "per_class_val_q05"
    if already(cfg, seal_of(ds, ordinal, tag)):
        return read_json(result_path(cfg))
    X, m = aligned(ds, enc, variant, subset_fn, key=tag)
    unk = set(unknown_classes)
    known_lab = [c for c in ordinal if c in set(m["label_name"]) and c not in unk]
    keep = m["label_name"].isin(known_lab + sorted(unk)).values
    X, m = X[keep], m[keep].reset_index(drop=True)
    known_tr = m[(m["split"] == "train") & m["label_name"].isin(known_lab)].index.values
    if shot is None:
        sup_idx = known_tr
    else:
        sup_idx, _ = balanced_support(m, known_lab, shot, seed)
    te = m["split"].values == "test"
    te_k = te & m["label_name"].isin(known_lab).values
    te_u = te & m["label_name"].isin(sorted(unk)).values
    if len(sup_idx) == 0 or te_k.sum() < max(1, min_te_each) or te_u.sum() < max(1, min_te_each):
        # min_te_each is 1 by default and changes nothing for the main sets. Views may
        # raise it (Khirshapat: 21 OverRipe images in total, so hiding any grade leaves
        # one side of the AUROC with a handful of test images). Both sides are checked:
        # guarding only the unknown side still let P2_unseen_interior on UnRipe through
        # with 137 unknown and NINE known test images. An AUROC on that is a number, not
        # an estimate, and once written into a results table nothing downstream can tell
        # it apart from a real one.
        return None
    tr = m.loc[sup_idx]
    head = make_head("linear", C=C).fit(X[sup_idx], tr["label_name"].values)
    Xk, Xu = X[te_k], X[te_u]
    if score == "msp":
        sk, su = score_msp(head, Xk), score_msp(head, Xu)
    elif score == "energy":
        sk, su = score_energy(head, Xk), score_energy(head, Xu)
    elif score == "mahalanobis":
        sc = _mahal_cached(X, sup_idx, tr["label_name"].values,
                           tag="e2|%s|%s|%s|%s" % (ds, enc, variant, tag))
        sk, su = sc.score(Xk), sc.score(Xu)
    elif score == "knn":
        sc = KNNScorer(X[sup_idx], tr["label_name"].values, k)
        sk, su = sc.score(Xk), sc.score(Xu)
    else:
        raise ValueError(score)
    yk = m["label_name"].values[te_k]
    pred_k = head.predict(Xk)
    met = open_set_metrics(sk, su, known_correct=(pred_k == yk))
    met["known_acc"] = float((pred_k == yk).mean())
    thr = float(np.percentile(sk, 5))
    met["threshold_fpr5"] = thr
    met["rejection_rate_per_class"] = per_class_rejection(yk, sk, thr)
    if cfg.get("calib"):
        # Class-conditional calibration, fitted on the VAL split (see below).
        #
        # Motivation (the plan's RQ2): at one global threshold the rejection rate is very
        # uneven across grades, because a grade adjacent to the hidden one sits closer to
        # the decision boundary and gets rejected far more often than the distant ones.
        # Here each known class c gets its own threshold tau_c = 5th percentile of the
        # scores that class's own calibration samples receive, and a test sample is
        # accepted iff its score clears the threshold of the class the classifier
        # predicts for it. Nothing is fitted on test data.
        #
        # What this changes and what it does not: it equalises *acceptance* per class on
        # the calibration distribution, not on test, so an improvement is evidence the
        # imbalance is calibration artefact rather than an intrinsic property of the
        # feature space. The global FPR is whatever falls out; it is reported, not tuned.
        # Thresholds are fitted on the VAL split, not on the support set. Fitting on
        # support was tried first and failed loudly: the head is trained on exactly those
        # samples, so their scores are inflated; the 5th percentile there sat above almost
        # every test score and the calibrated arm rejected 77% of the known test set.
        # Val has never been used for fitting anything, and it is group-disjoint from
        # train and test, so it is the one honest calibration pool. Test stays untouched.
        calk = (m["split"].values == "val") & m["label_name"].isin(known_lab).values
        if calk.sum() < 20:
            # No usable val split (e.g. `ffr`, whose archive ships train/test only). The
            # only honest answer is that this view has no calibration arm. An earlier
            # version fell back to fitting on the SUPPORT set -- the very samples the head
            # was trained on, whose scores are inflated -- and that arm rejected 77% of the
            # known test set while looking like an ordinary result. Absence from T10 is the
            # correct signal; a support-fitted number is not.
            log("[E2] no calibration arm for %s (%s): val rows=%d"
                % (cfg.get("view"), cfg.get("dataset"), int(calk.sum())))
            return None
        calib_src = "val"
        Xc = X[calk]
        yc = m["label_name"].values[calk]
        if score == "msp":
            ss = score_msp(head, Xc)
        elif score == "energy":
            ss = score_energy(head, Xc)
        elif score == "mahalanobis":
            ss = _mahal_cached(X, sup_idx, tr["label_name"].values,
                               tag="e2|%s|%s|%s|%s" % (ds, enc, variant, tag)).score(Xc)
        else:
            ss = KNNScorer(X[sup_idx], tr["label_name"].values, k).score(Xc)
        taumap = {c: float(np.percentile(ss[yc == c], 5)) for c in known_lab if (yc == c).sum() > 0}
        pk = head.predict(Xk)
        pu = head.predict(Xu)
        acc_k = sk >= np.array([taumap.get(p, -np.inf) for p in pk])
        acc_u = su >= np.array([taumap.get(p, -np.inf) for p in pu])
        rej_after = {c: float((~acc_k[yk == c]).mean()) for c in known_lab if (yk == c).sum() > 0}
        before = met["rejection_rate_per_class"]
        met["calibrated"] = {
            "tau": {k: round(v, 6) for k, v in taumap.items()},
            "ccr": float(((pk == yk) & acc_k).mean()),
            "fpr": float(acc_u.mean()),
            "known_accept_rate": float(acc_k.mean()),
            "rejection_rate_per_class": rej_after,
            "rejection_spread_before": float(np.std(list(before.values()))) if before else None,
            "rejection_spread_after": float(np.std(list(rej_after.values()))),
            "calib_source": calib_src,
            "n_calib": int(calk.sum()),
            # A known class with no calibration samples gets tau = -inf, i.e. everything
            # predicted as it is accepted. That can only push FPR up, so it is recorded
            # rather than left implicit; an empty list is the normal case.
            "classes_without_threshold": sorted(c for c in known_lab if c not in taumap),
            "note": "thresholds fitted on val (group-disjoint from train/test); global FPR is an outcome, not a target",
        }
    met["unknown_mix"] = {c: int((m["label_name"].values[te_u] == c).sum()) for c in sorted(unk)}
    met.update({"n_support": int(len(tr)), "support_ids_sha256": sha256_ids(tr["id"].values),
                "n_known_test": int(te_k.sum()), "n_unknown_test": int(te_u.sum())})
    np.savez_compressed(RESULTS / "scores" / (run_id(cfg) + ".npz"),
                        known_scores=sk, unknown_scores=su, known_labels=yk,
                        unknown_labels=m["label_name"].values[te_u],
                        known_pred=pred_k)
    return save_result(cfg, met, seal=seal_of(ds, ordinal, tag))


# ---------------------------------------------------------------- E2c unseen cultivar
def e2_cultivar(ds, enc, held_fruit, grades=("unripe", "ripe", "overripe"), score="energy",
                shot=None, seed=0, variant="cls", C=1.0, k=5):
    """The plan's P2: a *new cultivar* is the unknown class.

    The plan defines the three open-set scenarios as out-of-grade, unseen cultivar, and
    decay/foreign matter. The P2 that E2 originally shipped with hides an interior
    grade, which is a different (and harder) question, so it is kept but this protocol
    is added: the whole held-out fruit is unknown, and the known space is the same
    ordinal grades pooled over the other fruits. Labels are collapsed to the grade
    ("Apple_Ripe" -> "ripe") so the known class set is shared across fruits.

    The held-out fruit contributes only its three ordinal grades, not its Rotten class:
    rotting is already P3, and mixing the two would make this test a blend of cultivar
    novelty and decay novelty.
    """
    cfg = {"exp": "E2", "dataset": ds, "view": "fruit12_x_" + held_fruit.lower(), "encoder": enc,
           "variant": variant, "protocol": "P2c_unseen_cultivar", "unknown": [held_fruit],
           "score": score, "shot": shot, "seed": seed, "C": C}
    if already(cfg, seal_of(ds, grades, cfg["view"])):
        return read_json(result_path(cfg))
    X, m = aligned(ds, enc, variant, None, key="fruit12|all")
    lab = m["label_name"].astype(str)
    parts = lab.str.split("_", n=1)
    fruit = parts.str[0].values
    grade = parts.str[1].str.lower().values
    known_lab = sorted(set(grades) & set(grade[fruit != held_fruit]))
    if len(known_lab) < 2:
        return None
    is_known = (fruit != held_fruit) & np.isin(grade, known_lab)
    is_unk = (fruit == held_fruit) & np.isin(grade, list(grades))
    tr = is_known & (m["split"].values == "train")
    te = m["split"].values == "test"
    te_k = te & is_known
    te_u = te & is_unk
    if te_k.sum() == 0 or te_u.sum() == 0 or tr.sum() == 0:
        return None
    if shot is None:
        sup_idx = np.where(tr)[0]
    else:
        rng = np.random.RandomState(seed)
        picked = []
        for c in known_lab:
            cand = np.where(tr & (grade == c))[0]
            if len(cand) == 0:
                continue
            picked.extend(rng.choice(cand, size=min(shot, len(cand)), replace=False).tolist())
        sup_idx = np.array(sorted(picked), dtype=int)
    y_sup = grade[sup_idx]
    head = make_head("linear", C=C).fit(X[sup_idx], y_sup)
    tk = np.where(te_k)[0]
    tu = np.where(te_u)[0]
    Xk, Xu = X[tk], X[tu]
    if score == "msp":
        sk, su = score_msp(head, Xk), score_msp(head, Xu)
    elif score == "energy":
        sk, su = score_energy(head, Xk), score_energy(head, Xu)
    elif score == "mahalanobis":
        sc = _mahal_cached(X, sup_idx, y_sup,
                           tag="e2c|%s|%s|%s|%s" % (ds, enc, variant, held_fruit))
        sk, su = sc.score(Xk), sc.score(Xu)
    elif score == "knn":
        sc = KNNScorer(X[sup_idx], y_sup, k)
        sk, su = sc.score(Xk), sc.score(Xu)
    else:
        raise ValueError(score)
    yk = grade[tk]
    pred_k = head.predict(Xk)
    met = open_set_metrics(sk, su, known_correct=(pred_k == yk))
    met["known_acc"] = float((pred_k == yk).mean())
    thr = float(np.percentile(sk, 5))
    met["threshold_fpr5"] = thr
    met["rejection_rate_per_class"] = per_class_rejection(yk, sk, thr)
    met["unknown_mix"] = {c: int((grade[tu] == c).sum()) for c in sorted(set(grade[tu]))}
    met.update({"n_support": int(len(sup_idx)),
                "support_ids_sha256": sha256_ids(m["id"].values[sup_idx]),
                "n_known_test": int(te_k.sum()), "n_unknown_test": int(te_u.sum()),
                "note": "known = pooled ordinal grades of the other fruits; unknown = the whole held-out fruit"})
    np.savez_compressed(RESULTS / "scores" / (run_id(cfg) + ".npz"),
                        known_scores=sk, unknown_scores=su, known_labels=yk,
                        unknown_labels=grade[tu], known_pred=pred_k)
    return save_result(cfg, met, seal=seal_of(ds, grades, cfg["view"]))


# ---------------------------------------------------------------- E2 leave-one-fruit-out
_FIT_CACHE = {}


_MAHAL_CACHE = {}


def _mahal_cached(X, sup_idx, y_sup, tag=""):
    """Fit the shared-covariance Gaussian once per (support set, feature space).

    The same support is scored by mahalanobis for every seed (shot=None) and, when the
    calibration arm runs, twice within one call. At d=2048 -- resnet50 -- one LedoitWolf
    fit plus its inverse is tens of seconds, and e2_fruit_out repeats it three times for
    three seeds over an identical support. Keyed on (tag, dims, support indices): the tag
    is what separates two datasets whose support index arrays happen to coincide.
    """
    h = hashlib.md5(np.ascontiguousarray(sup_idx).tobytes()).hexdigest()
    key = (tag, int(X.shape[1]), h)
    hit = _MAHAL_CACHE.get(key)
    if hit is None:
        hit = MahalanobisScorer(X[sup_idx], y_sup)
        if len(_MAHAL_CACHE) > 8:          # each holds a d x d precision matrix
            _MAHAL_CACHE.pop(next(iter(_MAHAL_CACHE)))
        _MAHAL_CACHE[key] = hit
    return hit


def _fit_linear_cached(X, sup_idx, y_sup, C, tag=""):
    """Fit the linear head once per (feature matrix, support set).

    The same support set is re-used by the four scoring rules and, when shot is None, by
    every seed; a 56-class multinomial fit on 2048-d ResNet features is the expensive part
    of a leave-one-fruit-out cell, so refitting it per score quadrupled a stage that is
    already hours long. Keyed on the md5 of the support indices (exact, no collision
    guesswork) plus the feature width; ids are dataset-prefixed so two datasets cannot
    share a key by accident.
    """
    h = hashlib.md5(np.ascontiguousarray(sup_idx).tobytes()).hexdigest()
    key = (tag, float(C), int(X.shape[1]), h)
    hit = _FIT_CACHE.get(key)
    if hit is None:
        hit = make_head("linear", C=C).fit(X[sup_idx], y_sup)
        if len(_FIT_CACHE) > 32:
            _FIT_CACHE.pop(next(iter(_FIT_CACHE)))
        _FIT_CACHE[key] = hit
    return hit


def e2_fruit_out(ds, enc, held_fruit, score="energy", shot=None, seed=0, variant="cls",
                 C=1.0, k=5, min_known_classes=2):
    """The plan's P2 on a multi-species set: a whole FRUIT is the unknown class.

    Labels are Fruits-360 folder names, "<Fruit> <number>" (e.g. "Apple 5", "Pear 13").
    The number is a variety/stage index assigned by the dataset authors — it is NOT a
    documented ordinal ripeness scale, and "Apple 5" has nothing to do with "Pear 5".
    The known classes therefore stay as they are: every class of every OTHER fruit is a
    known class, and the held-out fruit contributes only unknown rows. Nothing is pooled
    across fruits.

    This is the plan's literal "leave-one-fruit-out" (§4.5), distinct from P2c
    (leave-one-cultivar-out on fruit12, where the grades ARE ordinal and are pooled) and
    from P2_unseen_interior (hide one grade of one fruit).
    """
    cfg = {"exp": "E2", "dataset": ds,
           "view": "%s_x_%s" % (ds, held_fruit.lower().replace(" ", "_")),
           "encoder": enc, "variant": variant, "protocol": "P2_leave_one_fruit",
           "unknown": [held_fruit], "score": score, "shot": shot, "seed": seed, "C": C}
    if already(cfg, seal_of(ds, None, cfg["view"])):
        return read_json(result_path(cfg))
    X, m = aligned(ds, enc, variant, None, key=ds + "|all")
    lab = m["label_name"].astype(str)
    # Species = FIRST token, not "everything but the last". Fruits-360 also spells classes
    # "Apple Braeburn 1" / "Apple Red Yellow 2" / "Tomato Cherry Maroon 1": stripping only
    # the trailing number would withhold "Apple 5".."Apple 23" while leaving the other
    # apple cultivars in the known space, i.e. the "unseen fruit" would have been seen.
    fruit = lab.str.split().str[0].values
    known_classes = sorted(set(lab[fruit != held_fruit]))
    if len(known_classes) < min_known_classes:
        return None
    is_known = (fruit != held_fruit)
    is_unk = (fruit == held_fruit)
    tr = is_known & (m["split"].values == "train")
    te = m["split"].values == "test"
    te_k = te & is_known
    te_u = te & is_unk
    if te_k.sum() == 0 or te_u.sum() == 0 or tr.sum() == 0:
        return None
    if shot is None:
        sup_idx = np.where(tr)[0]
    else:
        rng = np.random.RandomState(seed)
        picked = []
        for c in known_classes:
            cand = np.where(tr & (lab.values == c))[0]
            if len(cand) == 0:
                continue
            picked.extend(rng.choice(cand, size=min(shot, len(cand)), replace=False).tolist())
        sup_idx = np.array(sorted(picked), dtype=int)
    if len(sup_idx) == 0:
        return None
    y_sup = lab.values[sup_idx]
    head = _fit_linear_cached(X, sup_idx, y_sup, C, tag="%s|%s|%s" % (ds, enc, variant))
    tk = np.where(te_k)[0]
    tu = np.where(te_u)[0]
    Xk, Xu = X[tk], X[tu]
    if score == "msp":
        sk, su = score_msp(head, Xk), score_msp(head, Xu)
    elif score == "energy":
        sk, su = score_energy(head, Xk), score_energy(head, Xu)
    elif score == "mahalanobis":
        sc = _mahal_cached(X, sup_idx, y_sup,
                           tag="e2f|%s|%s|%s|%s" % (ds, enc, variant, held_fruit))
        sk, su = sc.score(Xk), sc.score(Xu)
    elif score == "knn":
        sc = KNNScorer(X[sup_idx], y_sup, k)
        sk, su = sc.score(Xk), sc.score(Xu)
    else:
        raise ValueError(score)
    yk = lab.values[tk]
    pred_k = head.predict(Xk)
    met = open_set_metrics(sk, su, known_correct=(pred_k == yk))
    met["known_acc"] = float((pred_k == yk).mean())
    thr = float(np.percentile(sk, 5))
    met["threshold_fpr5"] = thr
    met["rejection_rate_per_class"] = per_class_rejection(yk, sk, thr)
    met["unknown_mix"] = {c: int((lab.values[tu] == c).sum()) for c in sorted(set(lab.values[tu]))}
    met.update({"n_support": int(len(sup_idx)),
                "support_ids_sha256": sha256_ids(m["id"].values[sup_idx]),
                "n_known_test": int(te_k.sum()), "n_unknown_test": int(te_u.sum()),
                "n_known_classes": len(known_classes),
                "note": "known = every class of the other fruits; unknown = the whole held-out fruit. "
                        "Class numbers are dataset indices, not pooled ordinal grades."})
    np.savez_compressed(RESULTS / "scores" / (run_id(cfg) + ".npz"),
                        known_scores=sk, unknown_scores=su, known_labels=yk,
                        unknown_labels=lab.values[tu], known_pred=pred_k)
    return save_result(cfg, met, seal=seal_of(ds, None, cfg["view"], known=known_classes))


# ---------------------------------------------------------------- E3 cross domain
def e3(src_ds, tgt_ds, enc, label_map, shot=0, seed=0, variant="cls", head_kind="proto", C=1.0, tag="",
       align="none"):
    """label_map: {target_label: source_label}. Train on source train, evaluate on target test.

    align="bn" is the plan's optional feature-level alignment tier (§4.3c, "BN calibration"):
    every feature dimension is z-scored with the mean/sd of the TARGET domain's train split
    -- target images, no target labels -- and the identical transform is applied to the
    source features, after which rows are L2-normalised again so the heads keep working in
    the same geometry. The key is only put into the config when it is used, so every E3
    run that existed before this tier keeps its run id.
    """
    cfg = {"exp": "E3", "dataset": "%s->%s" % (src_ds, tgt_ds), "view": tag, "encoder": enc,
           "variant": variant, "head": head_kind, "shot": shot, "seed": seed, "C": C}
    if align != "none":
        cfg["align"] = align
    if already(cfg, seal_of(src_ds, sorted(set(label_map.values())), tag)):
        return read_json(result_path(cfg))
    src_labels = set(label_map.values())
    Xs, ms = aligned(src_ds, enc, variant,
                     lambda r: r["split"] == "train" and r["label_name"] in src_labels, key=tag + "|src")
    Xt, mt = aligned(tgt_ds, enc, variant, lambda r: r["label_name"] in set(label_map), key=tag + "|tgt")
    if len(Xs) == 0 or len(Xt) == 0:
        return None
    mt = mt.copy()
    mt["mapped"] = mt["label_name"].map(label_map)
    if align == "bn":
        tgt_tr = (mt["split"].values == "train")
        if tgt_tr.sum() < 10:
            return None
        mu = Xt[tgt_tr].mean(0)
        sd = Xt[tgt_tr].std(0) + 1e-6
        Xs = l2norm((Xs - mu) / sd)
        Xt = l2norm((Xt - mu) / sd)
    te_mask = (mt["split"] == "test").values
    if te_mask.sum() == 0:
        return None
    if shot and shot > 0:
        pool = mt[mt["split"] == "train"]
        rng = np.random.RandomState(seed)
        add = []
        for c in sorted(set(pool["mapped"])):
            cand = pool.index[pool["mapped"] == c].values
            if len(cand):
                add.extend(rng.choice(cand, size=min(shot, len(cand)), replace=False))
        add = np.array(add, dtype=int)
        Xtr = np.vstack([Xs, Xt[add]])
        ytr = np.r_[ms["label_name"].values, mt["mapped"].values[add]]
    else:
        Xtr, ytr = Xs, ms["label_name"].values
    head = make_head(head_kind, C=C).fit(Xtr, ytr)
    pred = head.predict(Xt[te_mask])
    labels = sorted(src_labels)
    met = closed_set_metrics(mt["mapped"].values[te_mask], pred, labels)
    met.update({"n_support": int(len(Xtr)), "n_test": int(te_mask.sum()),
                "source": src_ds, "target": tgt_ds})
    return save_result(cfg, met, seal=seal_of(src_ds, sorted(set(label_map.values())), tag))


# ---------------------------------------------------------------- E2x foreign matter
def e2_foreign(known_ds, foreign_ds, enc, known_classes, foreign_classes, score="energy",
               shot=None, seed=0, variant="cls", C=1.0, k=5, tag="", min_foreign_test=20):
    """Plan 4.5's P3 "foreign matter": something that is not the graded fruit at all.

    The known arm is an ordinary closed-set problem on `known_ds` (support from train,
    evaluation on test). The unknown arm is the foreign images, which come from a
    *different dataset* and a *different species*. Both sides pass through the same frozen
    encoder, the same preprocessing and the same L2 normalisation, so the scores live in
    one space -- that is the only thing a cross-dataset open-set claim rests on, and it is
    why the two feature files are loaded through `aligned()` rather than recomputed here.

    Honest caveat to carry into the paper: the foreign set differs in capture condition as
    well as species, so a high AUROC here is "not-this-fruit AND not-this-camera". On a
    real grading line the foreign object appears in the same optics as the fruit.
    """
    kc, fc = sorted(known_classes), sorted(foreign_classes)
    cfg = {"exp": "E2", "dataset": "%s<-foreign:%s" % (known_ds, foreign_ds), "view": tag,
           "encoder": enc, "variant": variant, "protocol": "P3_foreign",
           "known": kc, "foreign": fc, "score": score, "shot": shot, "seed": seed, "C": C}
    if already(cfg, seal_of(known_ds, None, tag, known=kc)):
        return read_json(result_path(cfg))
    Xk, mk = aligned(known_ds, enc, variant,
                     lambda r: r["label_name"] in set(kc), key=tag + "|fx-known")
    Xu, mu = aligned(foreign_ds, enc, variant,
                     lambda r: r["label_name"] in set(fc), key=tag + "|fx-foreign")
    if len(Xk) == 0 or len(Xu) == 0:
        return None
    sup_idx, _ = balanced_support(mk, kc, shot, seed)
    te_k = (mk["split"] == "test").values
    te_u = (mu["split"] == "test").values
    if not te_u.any():                      # a set with no test split: use all of it
        te_u = np.ones(len(mu), dtype=bool)
    if len(sup_idx) == 0 or te_k.sum() == 0 or te_u.sum() < min_foreign_test:
        return None
    tr = mk.loc[sup_idx]
    head = make_head("linear", C=C).fit(Xk[sup_idx], tr["label_name"].values)
    Xkt, Xut = Xk[te_k], Xu[te_u]
    if score == "msp":
        sk, su = score_msp(head, Xkt), score_msp(head, Xut)
    elif score == "energy":
        sk, su = score_energy(head, Xkt), score_energy(head, Xut)
    elif score == "mahalanobis":
        sc = _mahal_cached(Xk, sup_idx, tr["label_name"].values,
                           tag="e2x|%s|%s|%s|%s|%s" % (known_ds, foreign_ds, enc, variant, tag))
        sk, su = sc.score(Xkt), sc.score(Xut)
    elif score == "knn":
        sc = KNNScorer(Xk[sup_idx], tr["label_name"].values, k)
        sk, su = sc.score(Xkt), sc.score(Xut)
    else:
        raise ValueError(score)
    yk = mk["label_name"].values[te_k]
    pred_k = head.predict(Xkt)
    met = open_set_metrics(sk, su, known_correct=(pred_k == yk))
    met["known_acc"] = float((pred_k == yk).mean())
    thr = float(np.percentile(sk, 5))
    met["threshold_fpr5"] = thr
    met["rejection_rate_per_class"] = per_class_rejection(yk, sk, thr)
    met["foreign_mix"] = {c: int((mu["label_name"].values[te_u] == c).sum()) for c in fc}
    met.update({"n_support": int(len(tr)), "support_ids_sha256": sha256_ids(tr["id"].values),
                "n_known_test": int(te_k.sum()), "n_unknown_test": int(te_u.sum()),
                "known_ds": known_ds, "foreign_ds": foreign_ds})
    np.savez_compressed(RESULTS / "scores" / (run_id(cfg) + ".npz"),
                        known_scores=sk, unknown_scores=su, known_labels=yk,
                        unknown_labels=mu["label_name"].values[te_u], known_pred=pred_k)
    return save_result(cfg, met, seal=seal_of(known_ds, None, tag, known=kc))
