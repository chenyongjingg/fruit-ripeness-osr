#!/usr/bin/env python3
"""Plan v2.0 week-3 figures, drawn from the T11/T12 tables rather than from raw runs.

  fig_v2_arms        four-arm grouped bars: mean AUROC per score family, sd across cells
  fig_v2_flip        family-flip interaction: dist vs prob as the hidden grade moves from
                     the first to the middle to the last position (per-view lines faint,
                     the cross-view mean thick)

Both are visual aids; every number in them is read from outputs/*.csv, none is typed here.
Palette: two categorical slots validated with the dataviz validator (blue/orange,
worst CVD dE 24.7, normal-vision 33.6, contrast >=3:1).
"""
import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path("/root/rio")))
from rio.common import OUT

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIG = OUT / "figures"
FIG.mkdir(parents=True, exist_ok=True)

DIST, PROB = "#2a78d6", "#eb6834"
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#d9d8d4"
plt.rcParams.update({
    "font.size": 9, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": MUTED, "axes.linewidth": 0.8,
    "font.family": "DejaVu Sans", "pdf.fonttype": 42,
})

ARMS = [("P1_out_of_grade", "P1\ntransitional\ngrade"),
        ("P2_unseen_interior", "P2\nunseen\ngrade"),
        ("P3_rotten", "P3a\ndecay"),
        ("P3_foreign", "P3b\ncross-dataset")]


def fig_arms():
    df = pd.read_csv(OUT / "T11_auroc_by_arm.csv")
    fig, ax = plt.subplots(figsize=(6.4, 3.1), dpi=200)
    w = 0.34
    for i, (arm, lab) in enumerate(ARMS):
        for j, (fam, col) in enumerate((("dist", DIST), ("prob", PROB))):
            r = df[(df["arm"] == arm) & (df["family"] == fam)]
            if r.empty:
                continue
            m, sd = float(r["auroc_mean"].iloc[0]), float(r["auroc_sd"].iloc[0])
            x = i + (j - 0.5) * (w + 0.03)
            ax.bar(x, m, w, color=col, edgecolor="white", linewidth=1.2,
                   yerr=sd, capsize=2.5,
                   error_kw=dict(elinewidth=0.8, ecolor=MUTED), zorder=3)
            ax.text(x, m + sd + 0.025, "%.2f" % m, ha="center", va="bottom",
                    fontsize=7.5, color=INK)
    ax.set_xticks(range(len(ARMS)))
    ax.set_xticklabels([l for _, l in ARMS], fontsize=8.5)
    ax.set_ylabel("AUROC (mean over cells)")
    ax.set_ylim(0.45, 1.05)
    ax.grid(axis="y", color=GRID, linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    h = [plt.Rectangle((0, 0), 1, 1, color=c) for c in (DIST, PROB)]
    ax.legend(h, ["distance family (mahalanobis, kNN)", "probability family (MSP, energy)"],
              frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=2,
              fontsize=8, handlelength=1.2, columnspacing=1.2)
    ax.set_title("Mean AUROC by unknown arm and score family", fontsize=10, loc="left")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(FIG / ("fig_v2_arms.%s" % ext), bbox_inches="tight")
    plt.close(fig)
    return "fig_v2_arms"


def fig_flip():
    agg = pd.read_csv(OUT / "T12_family_flip.csv")
    per = pd.read_csv(OUT / "T12b_family_flip_by_view.csv")
    order = ["first", "middle", "last"]
    fig, ax = plt.subplots(figsize=(5.6, 3.4), dpi=200)
    for fam, col, lab in (("dist", DIST, "distance family"), ("prob", PROB, "probability family")):
        # per-view faint lines: one per view, same x order. A view that has no cell at a
        # position (mango_khir only has the "first" arm: its 10-image test sides fail the
        # n>=10 gate elsewhere) yields NaN, and matplotlib breaks the line there.
        for v, g in per.groupby("view"):
            ys = []
            for o in order:
                hit = g.loc[g["hidden_at"] == o, fam]
                ys.append(float(hit.iloc[0]) if len(hit) else float("nan"))
            if sum(1 for y in ys if y == y) < 2:
                continue
            ax.plot(range(3), ys, color=col, linewidth=0.8, alpha=0.25, zorder=2)
        ys = [float(agg[(agg["hidden_at"] == o) & (agg["family"] == fam)]["auroc_mean"].iloc[0])
              for o in order]
        ax.plot(range(3), ys, color=col, linewidth=2.0, marker="o", markersize=6,
                markeredgecolor="white", markeredgewidth=1.2, label=lab, zorder=4)
        # Selective labels only: the two first-position points (which differ by 0.05 and
        # would collide if both sat above), the middle peak, and the two end points.
        for x, y in zip(range(3), ys):
            if x == 0:
                off, ha = ((6, 6), "left") if fam == "dist" else ((6, -14), "left")
            elif x == 2:
                off, ha = ((6, 4), "left") if fam == "dist" else ((6, -12), "left")
            else:
                off, ha = ((0, 10) if fam == "prob" else (0, -16), "center")
            ax.annotate("%.3f" % y, (x, y), textcoords="offset points", xytext=off,
                        ha=ha, fontsize=7.5, color=INK)
    ax.set_xticks(range(3))
    ax.set_xticklabels(["first grade hidden", "middle grade hidden", "last grade hidden"])
    ax.set_xlim(-0.30, 2.45)
    ax.set_ylabel("AUROC (mean over views and cells)")
    ax.grid(axis="y", color=GRID, linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, loc="lower right", fontsize=8)
    ax.set_title("The winning family depends on where the gap is", fontsize=10, loc="left")
    fig.text(0.01, -0.02, "faint lines: individual views (T12b); thick lines: cross-view mean (T12)",
             fontsize=7, color=MUTED)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(FIG / ("fig_v2_flip.%s" % ext), bbox_inches="tight")
    plt.close(fig)
    return "fig_v2_flip"


if __name__ == "__main__":
    done = []
    for f in (fig_arms, fig_flip):
        try:
            done.append(f())
        except Exception as e:
            print("FAIL %s: %s" % (f.__name__, e))
    print("figures:", done)
    with open(OUT / "FIGURES_V2.md", "w") as fh:
        fh.write("# Plan v2.0 figures\n\n")
        for d in done:
            fh.write("- `%s.pdf` / `%s.png`\n" % (d, d))
        fh.write("\nNumbers are read from T11_auroc_by_arm.csv and T12*/T12b tables; "
                 "nothing is typed by hand.\n")
