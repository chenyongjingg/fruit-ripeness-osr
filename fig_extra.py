#!/usr/bin/env python3
"""Extra figures the plan asks for and the main report does not draw.

  Fig. 4  score distributions, known vs unknown, for a few (view, protocol, score) cells
  Fig. 5  2-D embedding of the source-domain (fruit12) and target-domain (field4) test
          features, per encoder, to show how far the frozen space drifts

Every panel is wrapped so a missing cache cell skips the panel instead of killing the
script; whatever could be drawn is recorded in outputs/FIGURES_EXTRA.md. Nothing here
feeds a number into any table -- these are visual aids only.
"""
import json, glob, os, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import OUT, RESULTS, PROC, FEAT

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIG = OUT / "figures"
FIG.mkdir(parents=True, exist_ok=True)
DONE = []


def load_npz_for(pattern, pred=None):
    out = []
    for f in sorted(glob.glob(str(RESULTS / "scores" / pattern))):
        # Score arrays are named by the config hash alone; the run JSON is
        # "<EXP>__<dataset>__<same hash>.json", one directory up. Building
        # RESULTS/<hash>.json instead matched nothing, which is why fig. 4 stayed empty.
        js = list(RESULTS.glob("*__%s.json" % Path(f).stem))
        if not js:
            continue
        try:
            with open(js[0]) as fh:
                c = json.load(fh)["config"]
        except Exception:
            continue
        # filter on the (cheap) config BEFORE touching the array: opening 1800 npz
        # files without closing them exhausted the fd limit ("Too many open files").
        if pred is not None and not pred(c):
            continue
        try:
            with np.load(f, allow_pickle=True) as z:      # NpzFile must be closed
                arr = {k: np.array(z[k]) for k in ("known_scores", "unknown_scores")}
        except Exception:
            continue
        out.append((c, arr))
    return out


def fig4():
    """Known vs unknown score histograms; one panel per (view, protocol), one line per score."""
    cells = {}

    # score files are named by the config hash alone (no "E2__" prefix); the experiment
    # is inside the JSON. Globbing "E2__*.npz" matched zero files.
    # E2 is only run at shot in {1,5,10,50} (there is no all-support arm), so pick the
    # largest shot rather than expecting a null.
    # E2 has no 50-shot arm: its grid is shot in {None (all support), 5}. Taking the
    # per-cell maximum (not a hard-coded 50) keeps this figure working if the grid changes.
    def _sel(c):
        return (c.get("exp") == "E2" and not c.get("calib")
                and c.get("variant") == "cls" and c.get("shot") in (None, 5))

    for c, z in load_npz_for("*.npz", _sel):
        key = (c["view"], c["protocol"])
        cells.setdefault(key, []).append((c["score"], c["encoder"], z, c.get("shot")))
    # keep, per cell, only the entries from the richest shot arm available there
    w = lambda s: float("inf") if s is None else float(s)   # None == all support == richest
    for key, got in cells.items():
        best = max(w(g[3]) for g in got)
        cells[key] = [g for g in got if w(g[3]) == best]
    print("[fig4] cells available: %d" % len(cells))
    want = [("banana3", "P1_out_of_grade"), ("fruit12_banana", "P3_rotten"),
            ("banana3", "P2_unseen_interior"), ("fruit12_x_apple", "P2c_unseen_cultivar")]
    picked = [k for k in want if k in cells]
    if not picked:                      # fall back to whatever exists, deterministically
        picked = sorted([k for k in cells if any(g[1] == "dinov2_s" for g in cells[k])])[:4]
    print("[fig4] picked: %s" % (picked,))
    if not picked:
        return
    fig, axes = plt.subplots(1, len(picked), figsize=(4.2 * len(picked), 3.4), squeeze=False)
    for ax, key in zip(axes[0], picked):
        got = [g for g in cells[key] if g[1] == "dinov2_s"]
        if not got:
            got = [g for g in cells[key] if g[1] == "resnet50"] or cells[key]
        # ONE score per panel. Two scores share an axis only if they share a scale, and
        # these do not: mahalanobis scores run to -2500 while energy is O(1), so the first
        # version drew a single spike at 0 and hid both distributions.
        names = {g[0] for g in got}
        score = "energy" if "energy" in names else sorted(names)[0]
        g = [x for x in got if x[0] == score][0]
        ks = g[2]["known_scores"].astype(float)
        us = g[2]["unknown_scores"].astype(float)
        lo, hi = np.percentile(np.r_[ks, us], [1, 99])
        bins = np.linspace(lo, hi, 40)
        ax.hist(ks, bins=bins, density=True, alpha=.55, label="known")
        ax.hist(us, bins=bins, density=True, alpha=.35, histtype="step", lw=1.8, label="unknown")
        ax.set_title("%s | %s | %s | %s" % (key[0], key[1], g[1], score), fontsize=7)
        ax.set_xlabel("score (higher = more in-distribution)")
        ax.set_ylabel("density")
        ax.legend(fontsize=6)
        ax.grid(alpha=.3)
    fig.tight_layout()
    p = FIG / "fig4_score_distributions.png"
    fig.savefig(p, dpi=200)
    plt.close(fig)
    DONE.append(("fig4_score_distributions.png", "known vs unknown score distributions"))


def fig5():
    """fruit12 (source domain) vs field4 (target domain) test features, per encoder."""
    try:
        from sklearn.manifold import TSNE
    except Exception:
        return
    rows = []
    for enc in ("dinov2_s", "resnet50"):
        fs = FEAT / ("fruit12__%s.npz" % enc)
        ft = FEAT / ("field4__%s.npz" % enc)
        if not (fs.exists() and ft.exists()):
            continue
        try:
            zs, zt = np.load(fs, allow_pickle=True), np.load(ft, allow_pickle=True)
            Xs, Xt = zs["cls"].astype(np.float32), zt["cls"].astype(np.float32)
            ids_s, ids_t = zs["ids"].astype(str), zt["ids"].astype(str)
        except Exception:
            continue
        # map ids -> split via meta.csv
        try:
            import pandas as pd
            ms = pd.read_csv(PROC / "fruit12" / "meta.csv")
            mt = pd.read_csv(PROC / "field4" / "meta.csv")
            ss = ms.set_index("id")["split"].reindex(ids_s).values
            st = mt.set_index("id")["split"].reindex(ids_t).values
        except Exception:
            continue
        sel_s = np.where(ss == "test")[0]
        sel_t = np.where(st == "test")[0]
        if len(sel_s) == 0 or len(sel_t) == 0:
            continue
        rng = np.random.RandomState(0)
        sel_s = rng.choice(sel_s, size=min(900, len(sel_s)), replace=False)
        sel_t = rng.choice(sel_t, size=min(900, len(sel_t)), replace=False)
        X = np.vstack([Xs[sel_s], Xt[sel_t]])
        dom = np.r_[np.zeros(len(sel_s), int), np.ones(len(sel_t), int)]
        X = X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-8)
        try:
            from sklearn.decomposition import PCA
            Xr = PCA(n_components=50, random_state=0).fit_transform(X)
        except Exception:
            Xr = X[:, :50]
        Y = TSNE(n_components=2, perplexity=30, init="pca", random_state=0).fit_transform(Xr)
        fig, ax = plt.subplots(figsize=(4.6, 4.0))
        ax.scatter(Y[dom == 0, 0], Y[dom == 0, 1], s=6, alpha=.55, label="fruit12 test (source)")
        ax.scatter(Y[dom == 1, 0], Y[dom == 1, 1], s=6, alpha=.55, label="field4 test (target)")
        ax.set_title("frozen %s features, 2-D t-SNE" % enc, fontsize=9)
        ax.legend(fontsize=7); ax.set_xticks([]); ax.set_yticks([])
        fig.tight_layout()
        p = FIG / ("fig5_domain_tsne_%s.png" % enc)
        fig.savefig(p, dpi=200)
        plt.close(fig)
        rows.append("fig5_domain_tsne_%s.png" % enc)
    if rows:
        DONE.append((", ".join(rows), "source vs target domain embeddings"))


def main():
    for fn in (fig4, fig5):
        try:
            fn()
        except Exception as e:
            print("[fig] %s failed: %s" % (fn.__name__, e))
    lines = ["# Extra figures", "",
             "Visual aids only; no table number depends on them.", ""]
    for name, desc in DONE:
        lines.append("- `%s` -- %s" % (name, desc))
    if not DONE:
        lines.append("_Nothing could be drawn (missing caches or score files)._")
    (OUT / "FIGURES_EXTRA.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("drew:", DONE)


if __name__ == "__main__":
    main()
