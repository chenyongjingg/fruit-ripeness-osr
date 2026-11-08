# Datasets: sources, counts and licences

**No image data is redistributed in this repository.** What is included is (a) a measured
fingerprint of every dataset — `data/processed/<name>/card.json` — and (b) the exact split
membership — `data/processed/<name>/meta.csv` — so any reported number can be traced to the
items that produced it, and the splits can be rebuilt identically once the public archives are
downloaded.

Each card records: number of items, per-class counts, per-class test counts, the split sizes,
the group-leak count (0 for every dataset), the archive size and md5 where a single archive
exists, and the unit of analysis.

## Views

| view | source | items | classes used | role |
|---|---|---|---|---|
| `banana3` | HF `TCleo/3-banana-maturity` | 1,186 | underripe / ripe / overripe | clean 3-grade ordinal |
| `banana4` | HF `Sapek007/banana-ripeness` | 13,478 | unripe / ripe / overripe / rotten | 4-level |
| `fruit12_apple`, `fruit12_banana`, `fruit12_mango` | HF `Carlosmg23/fruit-ripeness-12clases` | 8,256 total | Unripe / Ripe / Overripe (+ Rotten unknowable) | multi-crop |
| `field4_banana`, `field4_mango` | `darthraider/fruit-ripeness-detection-dataset` | 4,999 total | Raw / Ripe | orchard/field target domain |
| `mango_khir` | Kaggle `srabon00/mango-ripening-stage-classification` | 975 (911/43/21) | UnRipe / Ripe / OverRipe | extreme class imbalance |
| `fruits360` | Kaggle `moltean/fruits`, curated subset | 7,440 (62 classes, 6 species) | 62 fruit folders | leave-one-fruit-out |
| `ffr` | Kaggle `sriramr/fruits-fresh-and-rotten-for-classification`, curated | 3,600 (6 × 600) | Fresh/Rotten × Apple/Banana/Orange | independent rotten source |
| `f360rot` | Kaggle `moltean/fruits` + its only rotten class | 8,090 | 61 classes known, `Apple Rotten 1` unknown | rotten class *in situ* |
| `raspgrade` | HF `FBK-TeV/RaspGrade` (also Zenodo 17698589) | 5,043 berry crops from 200 conveyor images | grade1 … grade5 | the only 5-level source |
| `ninepeach` | figshare record 27125373 `Peach Maturity Dataset` | 3,493 crops from 1,245 orchard photos | immature / semi-mature / mature | orchard 3-grade |

## Licences

| dataset | licence |
|---|---|
| `FBK-TeV/RaspGrade` | **CC-BY-NC-4.0** — non-commercial; attribution required |
| NinePeach (figshare 27125373) | CC BY 4.0 |
| Kaggle sets (`mango_khir`, `fruits360`, `ffr`, `f360rot`) | as stated on each Kaggle dataset page — check before redistribution |
| HuggingFace sets (`banana3`, `banana4`, `fruit12`, `field4`) | as stated on each dataset card |

The MIT licence of this repository covers **the code only**. It does not relicense any dataset,
and it does not override the non-commercial clause of RaspGrade.

## Two things to know before you compare numbers

1. **`raspgrade` is a segmentation set, not a classification set.** Each of the 200 conveyor
   images contains several berries of different grades, so an image label would be a majority
   vote. The unit here is a berry cropped from a grade-1…5 polygon (class 0 = whole bunch, is
   dropped). `group` = source image, and the split is group-aware (3,556 / 755 / 732 crops;
   `group_leak_count = 0`). Test counts per class are 148 / 523 / 43 / **6** / **12**, which is
   why grade-4 cells do not exist (the `n ≥ 10` per-side gate skips them) and why grade-5 cells
   are labelled descriptive.
2. **`ninepeach` has no cultivar field.** The archive holds 1,245 photographs, 1,245 Pascal-VOC
   annotations and 3,493 boxes, but no cultivar attribute or folder — so a “8 cultivars known,
   1 held out” protocol cannot be built from it, and none is reported
   (`card.json: plan_claim_vs_archive`). Every JPEG is stored landscape with EXIF orientation 6
   while every XML declares the portrait size, so the build applies `ImageOps.exif_transpose`
   and hard-asserts the transposed size against the XML (`exif_transposed=1245`,
   `xml_size_mismatch=0`); without that the crop rectangle leaves the image.

## Acquisition notes (reproducibility boundary)

HuggingFace downloads are scripted (`ensure_data.py`, `dl*.sh`). Kaggle and figshare are **not
scripted**: Kaggle serves a reCAPTCHA to datacentre IPs and the figshare API answers 403 to the
pod's egress while its signed R2 URL works — both archives were fetched manually and pushed to
the compute host. No credentials are stored in this repository, and none were stored on the
compute host.
