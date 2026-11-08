# Open-set fruit-ripeness pipeline — server handbook

Everything runs on the 4090 box under `/root/rio`, driven by `master.sh` (an infinite,
idempotent loop). Every experiment result is a JSON file keyed by a hash of its full
config, so killing the driver at any moment and restarting it resumes exactly where it
stopped — no result is ever recomputed and none is ever half-written (writes go through
`atomic_write_json`).

## 1. Is it alive?

```bash
tail -20 /root/rio/logs/master.log          # one line per cycle + disk space
cat /root/rio/outputs/status.json           # counts of finished runs, refreshed per cycle
tail -5  /root/rio/logs/sup_e1.log          # per-stage logs: sup_prepare/extract/e1/e2/e3/
tail -5  /root/rio/logs/sup_report.log      #   control/clip/qwen/report
cat /root/rio/outputs/REPORT.md             # aggregated tables (regenerated every cycle)
cat /root/rio/outputs/VERIFY.md             # stored score arrays re-scored with the same metric code
                                           # (consistency check, NOT an independent implementation)
nvidia-smi                                  # GPU busy == extraction or a VLM baseline
```

To stop cleanly: `touch /root/rio/STOP` (the loop exits after the current cycle).
To restart: `cd /root/rio && setsid nohup bash master.sh >> logs/master.out 2>&1 &`

**Plan v2.0 stage names.** The plan's week checklists spell stages the pipeline did not
have, so `run.py` now accepts them as aliases over the scripts that already implement the
work. None of them re-implements a check; each runs its script as a subprocess and
propagates a non-zero exit, so a caller cannot mistake a failed report for a finished one.

| plan command | what actually runs |
|---|---|
| `run.py --stage seal --write <keys>` | `seal.py` (the asserted key set is fixed in the file; `--write` is logged) |
| `run.py --stage aggregate --v2` | `analyze_v2.py [--bootstrap N]` → T11–T16 (T14b = the granularity curve) |
| `run.py --stage figures --v2` | `fig_v2.py` → `outputs/figures/fig_v2_{arms,flip}.pdf` |
| `run.py --stage report --rebuild` | `report.py` (no incremental mode; it always rebuilds from results) |
| `run.py --stage verify --seeds 3` | `verify_indep.py` then `final_check.py` (both count the seeds they read) |
| `run.py --stage validate --fix-leak-check` | `final_check.py` (the group-leak assertion runs unconditionally) |

The plan's other stage names were already covered under different spellings:
`experiments` → `--stage e1` / `--stage e2`, `baselines` → `run_baselines.py`,
`recalibrate --matched-fpr` → `--stage e2 --calib` + `report.py` T10, `extract` is the same
word, `scripts/add_dataset.py` → the decoders in `rio/data.py` driven by `--stage prepare`.

## 2. Layout

```
/root/rio
  run.py            stages: prepare | extract | e1 | e2 | e3 | control | all
  run_finetune.py   end-to-end ResNet-50 arm (E1ft)
  run_lora.py       LoRA on DINOv2-S (E1lora); driven by lora_loop.sh, after Qwen
  run_baselines.py  CLIP zero-shot + Qwen2-VL zero-shot / 5-shot over every view
  report.py         results/*.json -> master.csv, T*.csv, figures/, REPORT.md, VERIFY.md
  ensure_data.py    byte-exact dataset/model availability checks
  qwen_dl.sh        own download loop for the Qwen weights (never blocks science)
  recompute_e2.py   re-derive E2 summary stats from stored score arrays
  verify_indep.py   second, independent implementation of AUROC / FPR@95 / known accuracy
  ap_extra.py       per-class AP for the closed-set arm (plan's long-tail metric). E1 stores
                    only hard predictions, so AP is re-fitted from the same cells and kept
                    under exp = E1ap (no existing run id moves); `--self-test` checks the
                    metric against perfect / uninformative / wrong-class scorers
  fig_extra.py      Fig. 4 (score histograms) and Fig. 5 (source vs target t-SNE)
  fig_v2.py         plan-v2 week-3 figures read from the T11/T12 tables: four-arm grouped
                    bars by score family, and the family-flip interaction (per-view faint
                    lines + cross-view mean). Writes outputs/figures/fig_v2_{arms,flip}.pdf
  np_run.py         NinePeach end-to-end: build -> extract -> E1 -> E2 -> P3b foreign
  np_verify.py      post-download check of the NinePeach archive: size + md5, then the
                    image/box/class histogram read straight out of the zip (writes nothing)
  final_check.py    PASS/FAIL checklist over every artefact the paper cites
  seal.py           plan-v2 fix #10: writes the data seal (view/ordinal/known/meta_sha256)
                    into every result, backfills the pre-existing ones as `derived`, and
                    reports card-vs-live drift. Incremental after the first pass.
  analyze_v2.py     plan-v2 analysis layer T11..T16: AUROC by arm, family flip by hidden
                    level (with per-view breakdown), score-family agreement split by the
                    number of known classes, adjacent-grade rejection, collapsed cells,
                    thin cells + seed bootstrap. Reads stored scores only.
  np_fetch.py       (LOCAL, not on the server) pulls the NinePeach zip: figshare 403s the
                    pod's egress IP but the 302 target on Cloudflare R2 is reachable, and
                    figshare's signed URL expires in 10 s, so this machine mints the URL
                    through its own proxy and the pod appends `Range: bytes=<have>-`.
  rio/              common, data, encoders, methods, experiments
  data/raw          downloaded archives        data/processed  decoded images + meta.csv
  cache/features    frozen features (.npz)     results/        one JSON per run
  outputs           report artefacts           logs/           per-stage logs
```

## 3. Datasets actually used

The v1.3 plan names RaspGrade, NinePeach, the Ataulfo mango set and a blackberry set.
RaspGrade and NinePeach are now acquired (HF parquet / figshare R2, see §4); Ataulfo and
the blackberry set (SDGD) still cannot be fetched unattended (request-only / Roboflow
manual export). The rest of the benchmark is public, directly downloadable data that
covers every protocol the plan needs (3-, 4- and 5-level ordinal grading, multi-crop, and
a controlled-vs-field pairing for cross-domain). Substitutions must be stated in the paper.

| view | dataset | n | classes used | role |
|---|---|---|---|---|
| banana3 | TCleo/3-banana-maturity | 1,186 | underripe / ripe / overripe | clean 3-grade ordinal, P1 |
| banana4 | Sapek007/banana-ripeness | 13,478 | unripe / ripe / overripe + rotten | 4-level, P1 + P3 (rotten) |
| fruit12_apple | Carlosmg23/fruit-ripeness-12clases | — | Unripe / Ripe / Overripe + Rotten | multi-crop, P1 + P3 |
| fruit12_banana | idem | — | idem | RQ3 source domain |
| fruit12_mango | idem | — | idem | RQ3 source domain |
| field4_banana | darthraider/fruit-ripeness-detection-dataset | — | Raw / Ripe | RQ3 target (field) |
| field4_mango | idem | — | Raw / Ripe | RQ3 target (field) |
| mango_khir | Kaggle `srabon00/mango-ripening-stage-classification` (Khirshapat) | 975 (911/43/21) | UnRipe / Ripe / OverRipe | the plan's named extension set; RQ1 only (see below) |
| fruits360 | Kaggle `moltean/fruits`, curated subset | 7,440 (62 classes, 6 species) | 62 Fruits-360 folders | P2 leave-one-fruit-out |
| ffr | Kaggle `sriramr/fruits-fresh-and-rotten-for-classification`, curated subset | 3,600 (6 classes × 600) | Fresh/Rotten × Apple/Banana/Orange | P3 rotten (plan §4.5's independent rotten source) |
| f360rot | Kaggle `moltean/fruits` curated subset **+ its only rotten class** | 8,090 (7,440 + 650) | 61 classes with train images known, `Apple Rotten 1` unknown | P3 rotten (plan §4.5's "Fruits-360 rotten class", literally) |
| raspgrade | HF `FBK-TeV/RaspGrade` | 5,043 berry crops from 200 conveyor images | grade1..grade5 | the only 5-level source; granularity analysis |
| ninepeach | figshare 27125373 `Peach Maturity Dataset` | 3,493 peach crops from **1,245** orchard photos | immature / semi-mature / mature | field-scene 3-grade source; P3b known side |

Two of these are the plan's own named Kaggle sets, added 2026-11-08. **Kaggle cannot be
reached from this server**: `www.kaggle.com/api/v1/*` answers 404 and the web page returns
a reCAPTCHA wall for this egress IP, while the same request from an ordinary residential IP
returns 200. Both archives were therefore downloaded on a local machine and pushed over
SFTP (~190 KB/s); the server never logged into Kaggle. Credentials were never stored on
the server.

* `raspgrade` is a **segmentation** set, not a classification set: 200 conveyor images,
  every one of them containing more than one grade, so the image label would be a
  majority vote. The unit is a berry cut from a class-1..5 polygon (class 0 = whole bunch,
  dropped). `group` is the source image; 5,043 crops, split 3556/755/732; grade4 (6 test)
  and grade5 (12 test) fall under the n>=30 gate and are labelled descriptive.
* `ninepeach` is the figshare record the plan calls "NinePeach". **The plan's own numbers
  do not match the record**: plan row 1 says "3,849 images, 9 cultivars"; the record's
  description (v1 and v2, same 8,838,332,680-byte zip) and the archive state **1,245
  photographs, 3,493 boxes, 3 ripeness stages, and no cultivar field or folder**, so the
  "8 cultivars known + 1 held out" arm cannot be built from it and is recorded as
  unavailable rather than approximated (`card.json: plan_claim_vs_archive`). What the set
  does give is a genuine orchard 3-grade source for E1/E2 and the known side of a P3b pair.
  Unit = annotated peach crop (bbox + 10% margin); `group` = source photograph.
  **Every JPEG is stored landscape (4032x3024) with EXIF orientation 6 while every XML
  declares 3024x4032**, so the boxes live in the displayed frame: the build applies
  `ImageOps.exif_transpose` before cropping and hard-asserts that the transposed size equals
  the XML `<size>` (`card.json: exif_transposed=1245, xml_size_mismatch=0`). Without it the
  crop rectangle leaves the image and PIL raises `Coordinate 'lower' is less than 'upper'`.
  Archive split folders are `train` (996) and `val` (249) with **no test**, which the code
  detects and replaces with a group-aware stratified split (2446/524/523, leak 0).
* `mango_khir` has no split folders and photographs every mango twice (`GUTI_<id>_A/B`),
  so the leakage group is the **filename stem without the frame suffix** and the split is
  group-aware stratified (`official_split: false`, `group_key: filename-group`).
  Its class sizes are 911/43/21 — an extreme long tail — so `E2` applies `min_te_each = 10`
  to **both** sides. That gate removes the cells that used to be scored with 9 known test
  images (192 runs were deleted and recomputed), but it does **not** remove the view: the
  cells where both sides have >=10 test images survive as thin cells (mango_khir P2 hiding
  UnRipe: n_known = 10, n_unknown = 136), are listed in `outputs/T16_small_n.csv`, and are
  **descriptive only** under the plan's n>=30 rule. `T15_collapsed.csv` records that 12 of
  those runs collapse to a single predicted class.
* `fruits360` is a **curated subset** of the 278-class original (6 species, 62 classes,
  120 images per class), cut because the full 8.8 GB could not be pushed at this
  bandwidth. Sampling is systematic (evenly spaced over the path-sorted member list) and
  must be described as such in the paper; each class keeps ~31 test images.
  The official Training/Validation/Test split is kept (`official_split: true`).
* `ffr` (`fruits-fresh-and-rotten-for-classification`, 3.8 GB, 13,599 images) is the
  plan's named independent P3 source. Also a **curated subset**: 300 images per
  (split, class) out of the authors' train/test folders, so 3,600 images in 6 classes,
  1,800 train / 1,800 test, class-balanced. The archive ships every tree twice
  (`dataset/dataset/...` and `dataset/...`); the duplicating copy is dropped by basename
  (13,599 skipped), which is why the subset has exactly 3,600 distinct images rather than
  7,200 rows. Only the three fruit species present (apple/banana/orange) are used; the
  folder names were normalised to `<Fresh|Rotten>_<Fruit>` so the label is read straight
  off the folder. E1 and the zero-shot baselines are switched off for this view (see
  `run.py`): its three "grades" would be species, so an off-by-one rate or a CLIP grading
  prompt on it would be a number with no meaning. Only `P3_rotten` runs there.
* `f360rot` is the same curated subset with the archive's **only** rotten class,
  `Apple Rotten 1` (650 images), appended under `test/` — written by
  `kag/add_f360_rotten.py`, same 256 px / q90 rule as the curated subset, and the
  `fruits360` archive is left untouched (its content is already keyed into run ids).
  The class exists only in the `fruits-360_3-body-problem` flavour and only under
  `Training/`, so the append is not a re-split: the class is never in a known set, therefore
  no image of it can ever become support. Two details the card carries: `Pear 14` has all
  120 of its images on the val/test side, so it is **excluded from the known set** in
  `run.py` (a class with no train rows can never be predicted, and leaving it in would
  depress known accuracy for a reason unrelated to rejection); and the known set is 61
  variants over 6 species, which is why no ordinal claim is made on this view either.

Leakage control: the split unit is the **content hash of the image bytes**, except for
fruit12 where it is the **source photograph** (`fuente`), because several crops are cut
from one photo; fruits360, where it is `(class folder, specimen number)` because the
archive stores two rotations of the same fruit as `r0_<id>`/`r1_<id>`; and mango_khir,
where it is the filename stem without the `_A`/`_B` frame suffix.
fruit12's shipped split leaks 360 of 3,591 source images across
train/val/test, so the shipped split was discarded and a group-aware stratified split was
used instead (`split_was_regrouped: true` in the card). Every dataset card asserts
`group_leak_count == 0`; a non-zero value raises and the build fails. Measured for the
fruits360 subset: 4,788 specimens over 7,440 images, **0** specimens spanning the
authors' splits.

## 4. Protocols and metrics

Closed-set (RQ1): linear probe (logistic regression, C = 1.0, fixed a priori) and a
cosine prototype head with temperature 10, on L2-normalised frozen features. Support is
drawn from **train only**; evaluation is on **test only**; the val split is untouched
(no hyper-parameter search is performed, so nothing can leak).

Open-set (RQ2), four protocol families per view:

* **P1 out-of-grade** — the most extreme grade is absent from training entirely.
* **P2 leave-one-fruit-out** (`protocol = P2_leave_one_fruit`, dataset `fruits360`) — the
  plan's §4.5 wording taken literally: one whole **species** is the unknown class
  (Apple / Pear / Cucumber / Tomato / Orange, five runs-arms), and the known set is *every
  class of every other species*. Fruits-360's class numbers are dataset indices, **not a
  documented ordinal scale**, so nothing is pooled across fruits here and no grader
  ordering is claimed. "Species" is the first token of the class folder, so
  `Apple Braeburn 1` and `Apple Red Yellow 2` are apples — otherwise holding out "Apple"
  would leave other apple cultivars in the known set and the fruit would not be unseen.
  Reduced grid, same cost logic as P2c: 5 species × 2 encoders × 2 shot levels × 3 seeds ×
  4 scores = 240 runs. Unknown-side test sizes 150–580, known-side 1,351–1,781.
* **P2c unseen cultivar** — this is the plan's §4.5 "unseen cultivar" protocol: one whole
  fruit is held out (fruit12 apple / banana / mango), and the known set is the four grades
  of the *other* two fruits. The decayed grade is excluded from the known set so the
  result is not contaminated by P3. Naming a view "fruit12_x_apple" means apple is unknown.
  This protocol runs a **reduced grid** on purpose (cost): 3 held-out fruits × 2 encoders
  (dinov2_s, resnet50) × 2 shot levels (all, 5) × 3 seeds × 4 scores = 144 runs, versus the
  full grid of the other protocols. It also has no calibration arm.
* **P2_unseen_interior** — an extra protocol we added: one interior grade is hidden
  (only defined for views with ≥3 grades; a 2-grade view has no interior grade to hide).
  **This is not the plan's P2** and must not be reported as such.
* **P3 rotten/foreign matter** — the plan defines P3 as decay **and foreign matter**, so it
  is implemented as two arms. `P3_rotten`: the decayed class is the unknown (views that
  have one). `P3_foreign` (stage `e2x`): the known arm is one dataset's normal grades and
  the unknown images come from **another dataset and another species** — `banana3` ←
  fruit12 mangoes, `fruit12_apple` ← field4 mangoes, `ffr` fresh labels ← fruits360
  cucumbers/tomatoes. 3 pairs × 2 encoders × 2 shot levels × 3 seeds × 4 scores = 144
  runs. Caveat for the paper: the foreign set differs in capture condition as well as
  species, so a high AUROC means "not this fruit *and* not this camera".

Adjacent-grade rejection is quantified in two ways: per-class rejection rates at the
global 5%-FPR threshold (shows the imbalance), and a **calibration arm**
(`--stage e2 --calib`) that fits one threshold per class at the 5th percentile of that
class's scores **on the val split** (group-disjoint from train, never used for model
selection). The calibration arm reports CCR/FPR and the before/after spread of per-class
rejection rates. Note the honest reading: calibration can only move thresholds, so where
AUROC < 0.5 the ranking itself is inverted and `fpr_cal` will approach 1.0 — that is a
property of the score, not a bug in the calibration. The calibration pool is part of the
run id (`config.calib = "per_class_val_q05"`): a threshold fitted on val and one fitted on
the support set are different methods and must never share a run id. A view with **no
usable val split** (`ffr` ships train/test only) has **no calibration arm at all**: the
older fallback fitted on the support set, and that is the one pool known to be inflated
(it rejected 77% of the known test set). Absence from T10 is the signal.

The calibration is **class-conditional, not ordinal-smoothed**: each grade gets its own
threshold and nothing enforces that the thresholds vary smoothly along the grade order.
So it tests "is the imbalance a calibration artefact of one global threshold?", which is
the mechanism the plan hypothesises; it does **not** test an ordinal regulariser, and the
paper must not describe it as one.

Scoring functions: MSP, energy, Mahalanobis (shared within-class covariance, Ledoit-Wolf
shrinkage), kNN (mean cosine to the k = 5 nearest support vectors). Metrics: AUROC,
FPR@95TPR, OSCR — where **CCR counts only correctly-classified accepted knowns** — and
CCR@FPR5, plus per-class rejection rates at the global 5% threshold (the adjacent-grade
hypothesis).

FPR@95TPR is the FPR at the **largest threshold whose TPR is still ≥ 95%** (the
conventional operating point), and every record stores the TPR actually achieved
(`tpr_at_fpr95`). It used to be `np.percentile(known_scores, 5)`, which is a different
point: the interpolated percentile can land below 95% TPR (e.g. 90/95 = 0.947) and, when
the score has ties, a whole tie-block away from the crossing. An independent sweep found
deltas up to **0.163 FPR**; all E2 records were recomputed from the stored score arrays
with `recompute_e2.py` (no re-training), and `verify_indep.py` now reports 0 violations
over 1056 arrays (AUROC agrees to 2e-16, known accuracy exactly).

Cross-domain (RQ3): train on the fruit12 (controlled) train split, test on the field4
(real orchard) test split, with an explicit label correspondence; both a zero-shot
transfer and a 5-shot adaptation are reported, with prototype and linear heads.
The plan's optional third tier (§4.3c, feature-level alignment) is implemented as
`--align bn`: each feature dimension is z-scored with the **target domain's train split**
statistics (target images, **no target labels**) and the same transform is applied to the
source features, then rows are L2-normalised again. The key is written into the config
only when the tier is used, so no pre-existing E3 run id moves, and `T4_cross_domain`
groups by `align` so aligned and plain transfer rows are never averaged together. On the
banana3→banana4 mango-free pair it lifts a proto head from 0.700 to 0.857 accuracy at
0-shot — it is a real second method, not a knob.

Negative controls: (a) support labels **rotated by a non-zero class offset** — every
support sample's label changes while the class multiset is preserved, so accuracy must
fall to chance; (b) Gaussian random features — the whole pipeline must fall to chance.
Both are run at 5-shot over three seeds. The rotation replaced an earlier per-sample
i.i.d. shuffle which left ~1/C of the support labels unchanged, i.e. it leaked part of the
answer (with 15 support samples, ~5 true labels survived, enough for one seed to reach
macro-F1 0.46 against a chance level of 0.33). Judge the controls on **macro-F1 against
1/C**, not on accuracy: the test splits are imbalanced and a collapse to one class scores
0.673 accuracy on `fruit12_banana`.

## 5. Models

| key | timm id | input |
|---|---|---|
| dinov2_s | vit_small_patch14_dinov2.lvd142m | 224, dynamic |
| dinov2_b | vit_base_patch14_dinov2.lvd142m | 224, dynamic |
| clip_b | vit_base_patch16_clip_224.openai | 224 |
| resnet50 | resnet50.a1_in1k | 224 |

Both the CLS token and the patch-mean are cached per image (float16 npz). Preprocessing
is short-side resize + centre crop to 224 (DINOv2 is run at 224 rather than its native
518 — this is recorded, not hidden).

Baselines: CLIP-ViT-L/14 zero-shot with three templates per class (`a photo of an
{state} {fruit}` etc., the fruit word is stripped from the class name so templates do not
repeat it); Qwen2-VL-7B-Instruct, **INT4 (nf4, bnb)**, greedy decoding, zero-shot and
5-shot in-context (5 labelled exemplars per class in one conversation). Unparseable
answers are kept as a distinct `__unparsed__` prediction, counted as errors, and their
rate is reported — never silently dropped.

## 6. Deviations from the plan (to be stated in the paper)

1. Datasets substituted as in §3 (named sets not fetchable unattended). No dataset has
   more than four grades, so no "does it degrade as the number of grades grows" trend
   can be shown.
2. LoRA **is** implemented (`run_lora.py`): adapters r=8/alpha=16 on the qkv+proj
   projections of every DINOv2-S attention block, backbone frozen, AdamW lr 1e-3,
   30 epochs, same train-time augmentation as E1ft. Launched from `master2.sh` **after**
   the Qwen baseline (concurrent execution OOMs at 24 GB).
3. DINOv2 runs at 224 px (native 518) for throughput on a single 24 GB card.
4. P1/P2 are not defined for the two-grade field views (hiding the only interior grade
   would leave a single known class). Guarded in code by `len(ordn) >= 3`.
5. Terminology: title and text use **open-set recognition**, not "open-world"; the
   horticulture phrase "open-world orchard environment" (Li Zhang et al. 2023) is a
   different concept and is disambiguated explicitly.
6. **No ordinal-regression head** (CORN/CORAL). Ordinality is handled at the *evaluation*
   level (off-by-one rate, ordinal MAE), not by an ordinal inductive bias. Do not claim
   otherwise.
7. **No occlusion / mask-preactivation ablation.**
8. **No novel-class discovery arm** (the plan's k-means / Sinkhorn post-processing is
   marked "加分项"/optional there). Nothing in the pipeline identifies *what* an unknown
   is — it only rejects it. Do not claim otherwise.
9. `outputs/VERIFY.md` is a **consistency check, not an independent implementation**:
   it re-feeds the stored score arrays into the same `open_set_metrics` that produced
   them. It catches stale numbers, not a wrong metric definition. Until 2026-11-08 it
   also checked **nothing**: score arrays are named `<run_id>.npz` while run records are
   `<EXP>__<dataset>__<run_id>.json`, and the lookup used `<run_id>.json` for all 1764
   files, skipping every one and still printing "mismatches: 0". It now resolves each
   array to its run record by globbing `*__<run_id>.json` and counts unresolved files as
   failures; the current run reports 1820/1820 resolved, 0 unmatched, 0 mismatches.
10. The four collision-check references (E-CLIP, YOLOE, Grounding-DINO, Li Zhang 2023)
   were read only as summarised in the plan; **their full texts were never retrieved**.
10b. The plan's §3.4 execution design assumes a `configs/matrix.yaml` that adds an
   experiment by adding a row. Here the matrix lives in `run.py` (`views()` plus the grid
   arguments of each stage), which is the same thing written as code: a new dataset is a
   block in `views()` and a prepare block, not a YAML line. Two §3.4 guards are also
   weaker than stated: an out-of-memory run is **recorded as a failure and retried
   unchanged** next cycle (no automatic batch-halving retry), and the periodic summary is
   `outputs/status.json`, refreshed per cycle rather than once nightly. Disk is guarded at
   **5 GB free** (90% of the 50 GB volume), not "85% used".
11. There is no cron and no systemd in this container, so there is no true
    reboot-autostart. `/root/.bashrc` starts the driver when an interactive shell opens
    and the driver is absent; `bash /root/rio/START.sh` does the same explicitly.
