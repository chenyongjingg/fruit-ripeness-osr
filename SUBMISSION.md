# Submission metadata

**Title:** Open-Set Recognition for Postharvest Fruit Ripeness Grading: A Ten-Dataset Technical Benchmark of Rejection Protocols and Deployment Rules

**Authors:** Yongjin Chen, Chenrui Yang, Ziying Xue, Xiyuan Wang, Songze Zhu

**Affiliation:** People's Public Security University of China, Beijing, China

**Corresponding author:** Songze Zhu, 18513826980@163.com

**Journal:** Frontiers in Plant Science

**Section:** Technical Advances in Plant Science

**Research Topic:** AI-Driven Innovations in Plant Phenotyping and Genomics

**Article type:** Original Research

**Status:** prepared for submission (2026)

**Keywords:** open-set recognition; postharvest fruit grading; plant phenotyping; distribution shift; out-of-distribution detection; foundation models; threshold calibration

---

## What the manuscript reports

The manuscript measures when an image-based postharvest ripeness phenotyping model should refuse a trait call. Six rejection arms (terminal level, unseen interior level, leave-one-fruit-class-out, unseen species, decay and a foreign dataset) are crossed with four frozen backbones, four training-free scores and five seeds over ten public datasets, giving 12,728 configurations. The central finding is that the difficulty of rejection is governed by where the unknown sits relative to the known scale, not by how visually different it is: at unseen interior levels the two scoring families land within 0.001 near 0.63 AUROC, whereas the other five arms span 0.76–0.98.

The work is a technical advance and benchmark, not a new classifier. It contributes the protocol, the ten-dataset grid, source-grouped splits, negative controls, a 57-assertion acceptance suite, an independent implementation of every metric, and four deployment rules. The protocol is directly instantiable for cultivar-holdout phenotyping, which the manuscript presents as a future extension; no genomic data are analysed.

## Scope statement

This manuscript fits Frontiers in Plant Science and the Technical Advances in Plant Science specialty because it reports a reusable measurement technology rather than a new classifier: an open-set rejection protocol for image-based postharvest ripeness phenotyping. The work treats ripeness as an image-derived plant trait and asks when a phenotyping model should refuse a trait call, a decision that current plant-science pipelines leave unmeasured. It contributes six rejection arms, ten public datasets, 12,728 configurations, source-grouped splits, 57 acceptance assertions, an independent metric implementation and four deployment rules; all protocols, split fingerprints and score arrays are released. The study also fits the Research Topic AI-Driven Innovations in Plant Phenotyping and Genomics: it uses frozen foundation models, tests domain adaptation and cross-environment generalisability, and provides an open benchmark with reproducible workflows. Its leave-one-out design is directly instantiable for cultivar-holdout phenotyping, which we present as a future extension; the manuscript does not analyse genomic data.

## Data and code

- **Code, split tables, 3,264 sealed score arrays and the 57-assertion suite:** https://github.com/chenyongjingg/fruit-ripeness-osr
- **Source datasets:** see [`DATA.md`](DATA.md) for repository names, direct links and licences.
- **Important licence note:** `FBK-TeV/RaspGrade` is CC-BY-NC-4.0 (non-commercial). The MIT licence covers the code only.

## Citation

Use [`CITATION.cff`](CITATION.cff) or [`CITATION.bib`](CITATION.bib). The manuscript citation will be updated when the article is accepted.
