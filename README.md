# fruit-ripeness-osr

Code, result records and aggregated tables for **“Open-Set Recognition of Fruit Ripeness: A
Multi-Dataset Benchmark and Empirical Analysis of Rejection Protocols, Scoring Families, and
Few-Shot Boundaries”** (manuscript in preparation, MDPI *Horticulturae*).

The question the repository answers with code and stored evidence: **when a ripeness grader
meets a grade it was never trained on, do training-free rejection scores actually fire?** Four
unknown-class protocols are evaluated across 8 open-set views (10 closed-set views), four
frozen backbones, four training-free scores, and five seeds.

Everything here is the state that produced the tables: **12,728 experiment records**, each with
its config, its metrics and the SHA-256 of the data it ran on.

---

## Headline numbers

Open-set AUROC, per arm, averaged over the cells of that arm (both score families; see
`outputs/T11_auroc_by_arm.csv`, per-score breakdown in `T11b`):

| arm | what is unknown | dist family | prob family |
|---|---|---|---|
| `P2_unseen_interior` | an interior grade (incl. the first) | **0.631** | **0.630** |
| `P1_out_of_grade` | the terminal grade | 0.760 | 0.553 |
| `P3_rotten` | a decay class | 0.832 | 0.632 |
| `P2c_unseen_species` | a whole species (fruit12) | 0.891 | 0.658 |
| `P2_leave_one_fruit` | a whole fruit class (Fruits-360) | 0.958 | 0.878 |
| `P3_foreign` | another dataset's fruit | **0.982** | 0.798 |

The one robust statement about score families is directional and narrow: **at the terminal
grade the distance family wins in 7 of 7 views**; at the first grade it is 4 : 4 and at an
interior grade 4 : 3, i.e. dataset-dependent (`outputs/T12b_family_flip_by_view.csv`).
On two-known-class heads MSP and Energy are **identical, bit for bit** (114/114 cells), so
“four scores” is really “two families” (`outputs/T13_score_corr.csv`).

Three results constrain the story and are not hidden in the paper:

* on the 5-grade conveyor-belt set (`raspgrade`) the most levels do **not** produce the most
  rejection: every cell mean sits between 0.49 and 0.58, i.e. near chance, and the arm means
  range only 0.493–0.555 (`outputs/T12b_family_flip_by_view.csv`);
* on the orchard set (`ninepeach`) the **prob family falls below chance** at both the first
  (0.302) and the terminal (0.334) grade, while the distance family holds 0.814 and 0.677 —
  the family ordering reverses with the hidden position in a way no "one family is weaker"
  summary captures;
* 16 runs collapse to a single predicted class, and 4 cells carry fewer than 30 test images;
  both are listed explicitly (`outputs/T15_collapsed.csv`, `outputs/T16_small_n.csv`) instead
  of being silently averaged.

**Gate:** `python3 final_check.py` → `PASSED 57 / 57`, `FAILURES: 0` on the machine that
produced the results. It checks, among other things, that every result carries a data seal,
that `verify_indep.py` re-derives AUROC / FPR@95 / known accuracy from the raw score arrays
with a **second implementation** (0 violations over 3,264 arrays), and that no dataset card
has drifted from the live `meta.csv`. In a clone the one item that needs the image archives
(`every raw dataset prepared`) prints `SKIP` instead of a verdict, so a bare clone reads
`PASSED 56 / 56`, `SKIPPED: 1` — a skip is never counted as a pass.

---

## Two ways to use this repository

### A. Re-derive every table from the stored evidence (no GPU, no datasets)

`results/scores/*.npz` holds the raw rejection scores for all 3,264 open-set runs, so the
analysis layer can be re-run on its own. The scripts read and write under the repository
root (`RIO_ROOT` overrides that if the results live on another disk):

```bash
pip install -r requirements.txt
python3 analyze_v2.py --bootstrap 1000     # T11 … T16
python3 report.py                          # outputs/REPORT.md, master.csv, figures
python3 verify_indep.py                    # independent re-derivation of the metrics
python3 final_check.py                     # 56 / 56 + 1 skip in a bare clone
```

Regenerating `outputs/` on a different machine reproduces the tables digit for digit; the
only differences seen are float last digits (1e-16, from the numpy/scipy build) and PNG
bytes (matplotlib version). The bootstrap column of `T16b` depends on `--bootstrap`.

### B. Re-run the experiments from scratch

```bash
python3 ensure_data.py --datasets-only     # scripted public downloads (HuggingFace)
# Kaggle / figshare sources are manual: see DATA.md
python3 run.py --stage prepare             # decode + group-aware splits
python3 run.py --stage extract --encoders dinov2_s,dinov2_b,clip_b,resnet50
bash master2.sh                            # the full idempotent driver
```

Runs are keyed on a SHA-1 of their config and are skipped when already present, so the driver
can be stopped and restarted at any point.

---

## Layout

```
run.py                 one entry point, all stages (prepare / extract / e1 / e2 / e3 / …)
master2.sh             unattended driver: every stage, per-stage wall-clock guard
analyze_v2.py          T11–T16: arms, score families, adjacent grades, collapsed/thin cells
report.py              the long-form report and T1–T10 tables
final_check.py         57 assertions; prints PASS/FAIL and exits non-zero on any failure
verify_indep.py        second, independent implementation of AUROC / FPR@95 / known accuracy
seal.py                pins every result to the data it ran on (meta_sha256 + view + grades)
rio/                   the package: datasets, features, heads, scores, metrics, protocols
results/               12,728 experiment records + scores/*.npz (the raw rejection scores)
outputs/               every table and figure the manuscript cites
data/processed/*/      card.json (measured dataset fingerprint) + meta.csv (the exact split)
logs/                  the run logs, including the passing final_check
probe/                 the small audit scripts behind the checks quoted in the paper
docs: PLAN_VS_DATA.md  (zh) measured-vs-planned ledger; README_SERVER.md (en) operations;
      HANDOVER_ZH.md   (zh) full operating notes and known traps
```

Two things about the tree that will look odd and are not damage. `probe/` and
`make_snapshot.sh` still carry the pod's `/root/rio` paths: they are the scripts that were
actually executed there and are kept as run evidence, unlike the pipeline itself, which
resolves its root from `__file__`. And 960 file names under `results/` contain a private-use
`<` / `:` — Windows cannot store those characters, so the extractor remapped them — which
is why those names look like `E2__banana3?-foreign?fruit12__…`. Every reader globs
`results/*.json`, so no name is ever typed by hand.

## Protocols in one sentence each

* **P1** hides the terminal grade (over-ripe usually); **P2** hides an interior grade — this is
  the same “leave-one-level-out” operation, instantiated twice, and the paper does not claim
  they are different phenomena.
* **P3a** hides a decay class; **P3b** holds out an entire other dataset. P3b therefore
  changes species, camera and lighting at once: it is reported descriptively, not as evidence
  about “foreign objects”.
* Scores: `msp`, `energy` (prob family), `mahalanobis`, `knn` (distance family). Thresholds are
  either fixed or fitted on the validation split per class (`--calib`); calibration is reported
  as **threshold redistribution**, with CCR and FPR always quoted together.

## Data and licences

Datasets are **not** redistributed here — only their measured fingerprints (`card.json`) and
the exact split membership (`meta.csv`). Sources, counts and licences are in
[`DATA.md`](DATA.md). Note that `FBK-TeV/RaspGrade` is **CC-BY-NC-4.0** (non-commercial); the
code in this repository is MIT, but that licence does not extend to the data.

## Citation

See `CITATION.cff`. If you use the benchmark or the stored score arrays, please cite the
manuscript (details to be filled in on acceptance) and this repository.

## Contact

Yongjin Chen — `3337851329@qq.com`
