#!/usr/bin/env python3
"""Single entry point. Stages are idempotent; rerun the same command to resume."""
import argparse, os, sys, time, traceback, json, re
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
HERE = Path(__file__).resolve().parent
from rio.common import RAW, PROC, FEAT, RESULTS, OUT, CONF, LOGS, log, atomic_write_json, read_json, set_done, is_done, heartbeat, disk_free_gb, read_json
from rio import data as D
from rio import experiments as E


def run_aux(script, args=()):
    """Run a sibling script as its own process, and fail loudly if it fails.

    The plan's week-3 checklist names stages (`seal`, `aggregate --v2`, `figures --v2`,
    `report --rebuild`, `verify --seeds 3`) that were implemented as standalone scripts.
    Aliasing them here means the plan's literal command runs the same code the script
    runs -- it does not re-implement a single check. A non-zero exit propagates, so a
    caller waiting on this stage cannot mistake a failed report for a completed one.
    """
    import subprocess
    cmd = [sys.executable, str(HERE / script)] + [str(x) for x in args]
    log("[aux] %s" % " ".join(cmd[1:]))
    r = subprocess.run(cmd, cwd=str(HERE))
    if r.returncode != 0:
        raise SystemExit("[aux] %s exited %d" % (script, r.returncode))
    return r.returncode


def note_failure(stage, key, err):
    """Append a machine-readable failure record.

    Failures used to exist only as free text in a stage log, so a run that failed every
    cycle looked identical to a healthy one from the outside. report.py now turns this
    file into a Failures table, which is the only thing that makes a silent, repeating
    failure visible.
    """
    try:
        with open(LOGS / "failures.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"at": time.strftime("%Y-%m-%dT%H:%M:%S"), "stage": stage,
                                "key": str(key), "err": str(err)[:300]}) + "\n")
    except Exception:
        pass


# ------------------------------------------------------------------ dataset registry
def _sfx(state_names):
    def f(label):
        lab = label.lower()
        return next((s for s in state_names if lab.endswith(s.lower()) or lab.lower().startswith(s.lower())), None)
    return f


def views():
    """name -> dict(ds, subset(r) -> bool, ordinal[], offscale[], group_key)"""
    V = {}
    V["banana3"] = dict(ds="banana3", subset=lambda r: True,
                        ordinal=["underripe", "ripe", "overripe"], offscale=[], p1="overripe")
    V["banana4"] = dict(ds="banana4", subset=lambda r: True,
                        ordinal=["unripe", "ripe", "overripe"], offscale=["rotten"], p1="overripe")
    meta = pd.read_csv(PROC / "fruit12" / "meta.csv") if (PROC / "fruit12" / "meta.csv").exists() else None
    if meta is not None:
        labs = sorted(meta["label_name"].astype(str).unique())
        fruits = sorted({l.split("_")[0] if "_" in l else l.split("-")[0] for l in labs})
        st = {"unripe": "Unripe", "ripe": "Ripe", "overripe": "Overripe", "rotten": "Rotten"}
        for fr in fruits:
            sub = [l for l in labs if l.split("_")[0] == fr or l.split("-")[0] == fr]
            states = {}
            for l in sub:
                base = str(l)[len(fr):].strip("_- ").lower()
                if base in st:          # exact match: "ripe" in "unripe" is true, equality is not
                    states[base] = l
            ordn = [states[k] for k in ("unripe", "ripe", "overripe") if k in states]
            assert len(set(ordn)) == len(ordn), "duplicate ordinal classes in view %s: %s" % (fr, ordn)
            off = [states["rotten"]] if "rotten" in states else []
            if len(ordn) >= 2:
                V["fruit12_" + fr.lower()] = dict(ds="fruit12", subset=(lambda f: (lambda r: str(r["label_name"]).startswith(f)))(fr),
                                                  ordinal=ordn, offscale=off, p1=ordn[-1])
    if (PROC / "mango_khir" / "meta.csv").exists():
        # The plan's extension-layer set: 975 images, 911/43/21 - an EXTREME long tail.
        # Its whole point is to probe where few-shot stops working, so the tiny classes
        # are kept as they are rather than balanced away. Test sets are correspondingly
        # tiny (a handful of Ripe/OverRipe images); per-class numbers there are
        # descriptive, not estimates.
        V["mango_khir"] = dict(ds="mango_khir", subset=lambda r: True,
                               ordinal=["UnRipe", "Ripe", "OverRipe"], offscale=[],
                               p1="OverRipe",
                               # 911/43/21: hiding any grade leaves one side of the AUROC
                               # with a handful of test images (UnRipe: 137 unknown vs 9
                               # known), so the open-set protocols are not estimable here.
                               # E1 (few-shot adaptation) is what this set is here to probe.
                               min_te_each=10)
    if (PROC / "raspgrade" / "meta.csv").exists():
        # Plan 4.2 priority 2: the only five-grade source, and the set the plan's
        # "granularity" analysis (how adjacent-grade confusion moves with the number of
        # levels) rests on. The unit is a berry crop cut from a segmentation polygon,
        # so its test sides are small and uneven; the n>=30 gate decides readability.
        V["raspgrade"] = dict(ds="raspgrade", subset=lambda r: True,
                              ordinal=["grade%d" % i for i in range(1, 6)],
                              offscale=[], p1="grade5", min_te_each=10)
    if (PROC / "ninepeach" / "meta.csv").exists():
        # Plan 4.2 priority 1: the field-scene source. RIPENESS ONLY -- the archive has
        # 1,245 photographs and 3,493 boxes but no cultivar field, so this view carries
        # E1/E2/P3_foreign arms and NOT the plan's cultivar-holdout arm (see build_ninepeach).
        # p1 = the fully ripe terminal grade; the other two grades are the closed set.
        V["ninepeach"] = dict(ds="ninepeach", subset=lambda r: True,
                              ordinal=["immature", "semi-mature", "mature"],
                              offscale=[], p1="mature", min_te_each=10)
    if (PROC / "ffr" / "meta.csv").exists():
        # Plan §4.5 P3 names "Fruits Fresh and Rotten" as a rotten source that is
        # independent of the sets already carrying P1/P2. Known space = the fresh class of
        # each species (a classifier needs the normal side); unknown = every rotten label.
        # No P1/P2 here: the three "grades" would be species, and no ordinal claim is made.
        # E1 is off for the same reason - an off-by-one rate between apple and banana is a
        # number with no meaning - and so are the zero-shot baselines, which would be asked
        # to grade a fruit species it was never given.
        V["ffr"] = dict(ds="ffr", subset=lambda r: True,
                        ordinal=["Fresh_Apple", "Fresh_Banana", "Fresh_Orange"],
                        offscale=["Rotten_Apple", "Rotten_Banana", "Rotten_Orange"],
                        protocols=["P3_rotten"], e1=False, baseline=False)
    if (PROC / "f360rot" / "meta.csv").exists():
        # Plan 4.5's "Fruits-360 rotten" source. Known = the 62 curated classes; unknown =
        # Apple Rotten 1, the archive's only decayed class (650 images, all on the test
        # side because the class is never in the known set). E1 and the zero-shot
        # baselines are off: 62 classes across 6 species are a dataset index, not a
        # ripeness scale, so "number of grades off by one" would be meaningless here.
        # Known classes are restricted to those with train rows: Pear 14 has all 120 of its
        # images on the val/test side, so it can never appear in a support set (support is
        # drawn from train only). Leaving it in the known list would put a class in front of
        # the scorer that no head can ever predict, deflating known accuracy for a reason
        # that has nothing to do with open-set rejection.
        _m = pd.read_csv(PROC / "f360rot" / "meta.csv")
        _tr = _m[_m["split"].astype(str) == "train"].groupby(_m["label_name"].astype(str)).size()
        _labs = sorted(str(l) for l in _tr[_tr >= 10].index)
        V["f360rot"] = dict(ds="f360rot", subset=lambda r: True,
                            ordinal=[l for l in _labs if l != "Apple Rotten 1"],
                            offscale=["Apple Rotten 1"], protocols=["P3_rotten"],
                            e1=False, baseline=False)
    if (PROC / "field4" / "meta.csv").exists():
        for fruit, cap in (("banana", "Banana"), ("mango", "Mango")):
            V["field4_" + fruit] = dict(ds="field4", subset=(lambda c: (lambda r: c in str(r["label_name"])))(cap),
                                        ordinal=["Raw_" + cap, "Ripe_" + cap], offscale=[], p1="Ripe_" + cap)
    return V


# ------------------------------------------------------------------ stages
def _f360_group(member):
    """Leakage group for Fruits-360: one physical fruit, not one JPEG.

    The archive stores two rotations of the same specimen as r0_<id> and r1_<id> inside
    the class folder; the ids are numbered per class, so the class folder is part of the
    key. Grouping by content hash would put r0_<id> in train and r1_<id> in test and let
    the model memorise the specimen. (Measured on the 62-class subset: 18,267 groups over
    49,960 images, 0 of them spanning the authors' official splits.)
    """
    parts = member.split("/")
    return parts[-2] + "/" + re.sub(r"^r\d+_", "", parts[-1])


def stage_prepare(force=False):
    rs = RAW
    if (rs / "banana3" / "data.parquet").exists() and not (PROC / "banana3" / "card.json").exists():
        D.build_parquet_classification(
            "banana3", [(rs / "banana3" / "data.parquet", "train")],
            label_names={0: "overripe", 1: "ripe", 2: "underripe"},
            classes=["underripe", "ripe", "overripe"], offscale=[],
            source="HF TCleo/3-banana-maturity (GPL-3.0)", split_from_file=False)
    if (rs / "banana4" / "data.zip").exists() and not (PROC / "banana4" / "card.json").exists():
        try:
            D.build_zip_folders("banana4", rs / "banana4" / "data.zip",
                                classes=["unripe", "ripe", "overripe", "rotten"], offscale=["rotten"],
                                source="HF Sapek007/banana-ripeness (CC BY 4.0, Roboflow v6)")
        except Exception as e:
            log("[prepare] banana4 failed: %s" % e)
    if (rs / "fruits360" / "data.zip").exists() and not (PROC / "fruits360" / "card.json").exists():
        try:
            # Curated subset of the Kaggle moltean/fruits archive (see HANDOVER): a handful
            # of fruit species, Training/Test kept as the authors split them. The classes
            # are taken from the archive itself - the subset was cut locally because the
            # server's egress IP is served a reCAPTCHA wall by Kaggle, so the full 8.8 GB
            # archive cannot be downloaded there.
            D.build_zip_folders(
                "fruits360", rs / "fruits360" / "data.zip",
                classes=None, offscale=[],
                source="Kaggle moltean/fruits (Fruits-360, 278 classes; curated subset)",
                split_dirs=("Training", "Test", "Validation"),
                group_fn=_f360_group)
        except Exception as e:
            log("[prepare] fruits360 failed: %s" % e)
    if (rs / "f360rot" / "data.zip").exists() and not (PROC / "f360rot" / "card.json").exists():
        try:
            # Plan 4.5's first P3 source, literally: "Fruits-360 rotten class". Fruits-360
            # ships exactly ONE rotten class (Apple Rotten 1, 650 images) and only in the
            # 3-body-problem flavour, under Training. A separate dataset is built instead
            # of adding the class to `fruits360`, because changing a dataset's *content*
            # silently invalidates every result already keyed on it (the run id hashes the
            # config, not the images). The rotten images are written to `test/`; see
            # kag/add_f360_rotten.py for why that is not a re-split.
            D.build_zip_folders(
                "f360rot", rs / "f360rot" / "data.zip",
                classes=None, offscale=[],
                source="Kaggle moltean/fruits (curated subset) + the archive's only rotten class, Apple Rotten 1",
                split_dirs=("Training", "Test", "Validation", "test"),
                group_fn=_f360_group)
        except Exception as e:
            log("[prepare] f360rot failed: %s" % e)
    if (rs / "mango_khir" / "data.zip").exists() and not (PROC / "mango_khir" / "card.json").exists():
        try:
            import re as _re
            # The archive has no split folders and photographs every mango twice
            # (GUTI_138_A / GUTI_138_B are the same fruit). The plan (§4.4) asks for a
            # filename-grouped split here; grouping by content hash would separate the
            # two frames and leak the same fruit across splits.
            D.build_zip_folders(
                "mango_khir", rs / "mango_khir" / "data.zip",
                classes=["UnRipe", "Ripe", "OverRipe"], offscale=[],
                source="Kaggle srabon00/mango-ripening-stage-classification (Khirshapat, 975 imgs, 911/43/21)",
                split_dirs=(), require_split_dir=False,
                group_fn=lambda fn: _re.sub(r"_[AB]\.\w+$", "", fn, flags=_re.I))
        except Exception as e:
            log("[prepare] mango_khir failed: %s" % e)
    if (rs / "ffr" / "data.zip").exists() and not (PROC / "ffr" / "card.json").exists():
        try:
            # Fruits Fresh and Rotten: train/<class>/ and test/<class>/ with the six
            # class folders already renamed to <Fresh|Rotten>_<Fruit> locally, so this
            # builder reads the label straight off the folder name.
            D.build_zip_folders(
                "ffr", rs / "ffr" / "data.zip",
                classes=None, offscale=[],
                source="Kaggle sriramr/fruits-fresh-and-rotten-for-classification (curated subset)",
                split_dirs=("train", "test"))
        except Exception as e:
            log("[prepare] ffr failed: %s" % e)
    if (rs / "fruit12" / "data.zip").exists() and not (PROC / "fruit12" / "card.json").exists():
        try:
            D.build_fruit12(rs / "fruit12" / "data.zip")
        except Exception as e:
            log("[prepare] fruit12 failed: %s" % e)
    if (rs / "field4" / "train.parquet").exists() and not (PROC / "field4" / "card.json").exists():
        try:
            D.build_parquet_classification(
                "field4", [(rs / "field4" / "train.parquet", "train"),
                           (rs / "field4" / "test.parquet", "test")],
                label_names={0: "Raw_Banana", 1: "Raw_Mango", 2: "Ripe_Banana", 3: "Ripe_Mango"},
                classes=["Raw_Banana", "Ripe_Banana", "Raw_Mango", "Ripe_Mango"], offscale=[],
                source="HF darthraider/fruit-ripeness-detection-dataset (Apache-2.0; Mendeley y3649cmgg6)",
                split_from_file=True)
        except Exception as e:
            log("[prepare] field4 failed: %s" % e)
    if (rs / "raspgrade" / "train-00000-of-00001.parquet").exists() \
            and not (PROC / "raspgrade" / "card.json").exists():
        try:
            # Plan 4.2 priority 2: the only FIVE-grade source in the pool. Instance
            # polygons, so the unit is a berry crop, not an image (see build_raspgrade).
            D.build_raspgrade()
        except Exception as e:
            log("[prepare] raspgrade failed: %s" % e)
    if (rs / "ninepeach" / "Peach_maturity_dataset.zip").exists() \
            and not (PROC / "ninepeach" / "card.json").exists():
        try:
            # Plan 4.2 priority 1. The archive is a real orchard set with INSTANCE boxes,
            # so the unit is a peach crop, not a photograph (see build_ninepeach). The
            # plan's "9 cultivars" arm does not exist in this release; the card records
            # the record-vs-plan discrepancy rather than the code inventing labels.
            D.build_ninepeach()
        except Exception as e:
            log("[prepare] ninepeach failed: %s" % e)
    set_done("prepare", {"n": len(list(PROC.glob("*/card.json")))})


def stage_extract(encs, dss, img_size=224, limit=None):
    from rio import encoders as EN
    for ds in dss:
        if not (PROC / ds / "card.json").exists():
            log("[extract] skip %s (not prepared)" % ds); continue
        n_expect = len(pd.read_csv(PROC / ds / "meta.csv"))
        for enc in encs:
            out = FEAT / ("%s__%s.npz" % (ds, enc))
            jp = FEAT / ("%s__%s.json" % (ds, enc))
            ok = out.exists() and jp.exists() and read_json(jp).get("n") == n_expect
            if ok:
                log("[extract] skip %s %s (exists)" % (ds, enc)); continue
            if disk_free_gb() < 5:
                log("[extract] LOW DISK %.1fGB - stopping" % disk_free_gb()); return
            heartbeat("extract", {"ds": ds, "enc": enc})
            try:
                EN.extract(ds, enc, img_size=img_size, limit=limit)
            except Exception as e:
                log("[extract] FAIL %s %s: %s\n%s" % (ds, enc, e, traceback.format_exc()[-800:]))


def stage_e1(V, encs, shots, seeds, heads, variants, C=1.0, control="none"):
    todo = []
    for vname, v in V.items():
        if not v.get("e1", True):
            continue
        for enc in encs:
            for h in heads:
                for var in variants:
                    for shot in shots:
                        for s in ([0] if shot is None else seeds):
                            todo.append(dict(vname=vname, v=v, enc=enc, h=h, var=var, shot=shot, s=s))
    done = 0
    for t in todo:
        ds = t["v"]["ds"]
        if not (FEAT / ("%s__%s.npz" % (ds, t["enc"]))).exists():
            continue
        try:
            E.e1(ds, t["enc"], t["v"]["subset"], t["v"]["ordinal"], head_kind=t["h"], shot=t["shot"],
                 seed=t["s"], variant=t["var"], C=C, tag=t["vname"], control=control)
            done += 1
        except Exception as e:
            log("[E1] FAIL %s: %s" % (t, e))
            note_failure("E1", t, e)
        if done % 40 == 0:
            heartbeat("E1", {"done": done, "total": len(todo)})
    log("[E1] finished chunk done=%d" % done)


def stage_e2(V, encs, shots, seeds, scores, variants, calib=False):
    for vname, v in V.items():
        ds = v["ds"]
        ordn = v["ordinal"]
        if v.get("min_te_each"):
            log("[E2] %s: open-set cells with fewer than %d TEST images on either side are "
                "skipped (long-tail view; E1 still runs)" % (vname, v["min_te_each"]))
        protos = []
        # P1 and P2 both hide a grade, so both need >=2 known classes left over.
        # A two-grade view (Raw/Ripe) would be left with a single known class and the
        # classifier cannot be fitted at all -- that produced 288 FAILs per cycle before
        # this guard was added. Hiding a grade is simply undefined there.
        if len(ordn) >= 3:
            protos.append(("P1_out_of_grade", [ordn[-1]]))
            for c in ordn[:-1]:
                protos.append(("P2_unseen_interior", [c]))
        if v["offscale"]:
            protos.append(("P3_rotten", v["offscale"]))
        if v.get("protocols"):
            # A view may restrict itself to the protocols that are actually defined on it
            # (ffr is a P3-only set: its "grades" are species, so hiding the last one as
            # P1 or an interior one as P2 would be a protocol run on a non-ordinal axis).
            keep = set(v["protocols"])
            protos = [p for p in protos if p[0] in keep]
        for enc in encs:
            if not (FEAT / ("%s__%s.npz" % (ds, enc))).exists():
                continue
            for var in variants:
                for proto, unk in protos:
                    for sc in scores:
                        for shot in shots:
                            for s in seeds:
                                try:
                                    E.e2(ds, enc, v["subset"], ordn, unk, proto, score=sc, shot=shot,
                                         seed=s, variant=var, tag=vname, calib=calib,
                                         min_te_each=v.get("min_te_each", 1))
                                except Exception as e:
                                    log("[E2] FAIL %s %s %s: %s" % (vname, proto, sc, e))
                                    note_failure("E2", "%s|%s|%s|%s|shot=%s" % (vname, proto, sc, enc, shot), e)
            heartbeat("E2", {"view": vname, "enc": enc})


# Plan §4.5 names "leave-one-fruit-out" on Fruits-360 as the P2 protocol. These are the
# fruit SPECIES (first token of the class folder) withheld in turn. The known space is
# every class of every other fruit - Fruits-360's numbers are dataset variety indices,
# not a documented ordinal scale, so nothing is pooled across fruits here.
FRUIT360_HELDOUT = ["Apple", "Pear", "Cucumber", "Tomato", "Orange"]


def stage_e2f(encs, seeds, scores=("msp", "energy", "mahalanobis", "knn"), shots=(None, 5)):
    """Leave-one-fruit-out open-set runs on the multi-species set.

    Kept to a scoped grid (2 shot levels, cls variant) unlike the view grid: the point is
    a protocol-level statement -- does a whole unseen fruit get rejected -- not another
    sweep of hyper-parameters that already vary elsewhere.
    """
    ds = "fruits360"
    if not FRUIT360_HELDOUT or not (PROC / ds / "meta.csv").exists():
        return
    for held in FRUIT360_HELDOUT:
        for enc in encs:
            if not (FEAT / ("%s__%s.npz" % (ds, enc))).exists():
                continue
            for sc in scores:
                for shot in shots:
                    for s in seeds:
                        try:
                            E.e2_fruit_out(ds, enc, held, score=sc, shot=shot, seed=s)
                        except Exception as e:
                            log("[E2f] FAIL %s %s shot=%s seed=%s: %s" % (held, sc, shot, s, e))
                            note_failure("E2f", "%s|%s|shot=%s" % (held, sc, shot), e)
        heartbeat("E2f", {"held": held})


# Plan 4.5's P3 has two halves: decayed fruit AND foreign matter ("异物"). The rotten half
# is covered by the P3_rotten arms of banana4 / fruit12 / ffr. This is the foreign half:
# the unknown images belong to a species that is not the graded fruit at all and, on
# purpose, come from a different dataset than the known arm, which is literally what the
# plan's wording says ("跨数据集水果图像作异物").
FOREIGN_PAIRS = [
    # known view, foreign dataset, foreign label prefixes, why this pair
    ("banana3", "fruit12", ["Mango_"],
     "controlled/controlled: a mango on a banana grading line"),
    ("fruit12_apple", "field4", ["Raw_Mango", "Ripe_Mango"],
     "controlled known + field foreign: orchard mango as line debris"),
    ("ffr", "fruits360", ["Cucumber", "Tomato"],
     "fresh/rotten produce as known + non-fruit-line vegetables as debris"),
    ("ninepeach", "fruit12", ["Mango_"],
     "ORCHARD peaches as known + a controlled lab mango as debris (field -> lab, the "
     "reverse direction of the existing pair; the mango is a different species, camera "
     "and lighting, so this is the confounded P3b arm the plan describes)"),
]


def stage_e2x(V, encs, seeds, scores=("msp", "energy", "mahalanobis", "knn"),
              shots=(None, 5)):
    """P3_foreign runs: known classes from one dataset, unknown images from another."""
    for kview, fds, prefixes, why in FOREIGN_PAIRS:
        v = V.get(kview)
        if v is None or not (PROC / fds / "meta.csv").exists():
            continue
        mu = pd.read_csv(PROC / fds / "meta.csv")
        fc = sorted({str(l) for l in mu["label_name"].unique()
                     if any(str(l).startswith(p) for p in prefixes)})
        if not fc:
            log("[E2x] no foreign labels match %s in %s" % (prefixes, fds))
            continue
        known = list(v["ordinal"])
        log("[E2x] %s <- %s %s (%s)" % (kview, fds, fc, why))
        for enc in encs:
            if not (FEAT / ("%s__%s.npz" % (v["ds"], enc))).exists():
                continue
            if not (FEAT / ("%s__%s.npz" % (fds, enc))).exists():
                log("[E2x] skip %s (no features for %s/%s)" % (kview, fds, enc))
                continue
            for sc in scores:
                for shot in shots:
                    for s in seeds:
                        try:
                            E.e2_foreign(v["ds"], fds, enc, known, fc, score=sc, shot=shot,
                                         seed=s, tag=kview)
                        except Exception as e:
                            # The old format string had four slots and three arguments, so
                            # the first real failure of this stage died inside its own error
                            # handler and the pair looked like "nothing to run".
                            log("[E2x] FAIL %s %s %s shot=%s: %r" % (kview, enc, sc, shot, e))
                            note_failure("E2x", "%s|%s|shot=%s" % (kview, sc, shot), e)
            heartbeat("E2x", {"view": kview, "enc": enc})


def stage_e2c(encs, shots, seeds, scores, fruits=("Apple", "Banana", "Mango")):
    """The plan's P2: leave-one-cultivar-out. Only fruit12 has several fruits."""
    if not (PROC / "fruit12" / "meta.csv").exists():
        return
    for held in fruits:
        for enc in encs:
            if not (FEAT / ("fruit12__%s.npz" % enc)).exists():
                continue
            for sc in scores:
                for shot in shots:
                    for s in seeds:
                        try:
                            E.e2_cultivar("fruit12", enc, held, score=sc, shot=shot, seed=s)
                        except Exception as e:
                            log("[E2c] FAIL %s %s shot=%s: %s" % (held, sc, shot, e))
                            note_failure("E2c", "%s|%s|shot=%s" % (held, sc, shot), e)
        heartbeat("E2c", {"held": held})


def stage_e3(V, encs, seeds, variants, align="none"):
    """Cross-dataset pairs with an explicit label correspondence."""
    pairs = []
    if "fruit12_mango" in V and "field4_mango" in V:
        m12, f4 = V["fruit12_mango"], V["field4_mango"]
        pairs.append(("fruit12", "field4",
                      {"Raw_Mango": m12["ordinal"][0], "Ripe_Mango": m12["ordinal"][1]}, "mango"))
    if "fruit12_banana" in V and "field4_banana" in V:
        b12, f4 = V["fruit12_banana"], V["field4_banana"]
        pairs.append(("fruit12", "field4",
                      {"Raw_Banana": b12["ordinal"][0], "Ripe_Banana": b12["ordinal"][1]}, "banana"))
    if "banana3" in V and "banana4" in V:
        pairs.append(("banana3", "banana4",
                      {"unripe": "underripe", "ripe": "ripe", "overripe": "overripe"}, "b3->b4"))
        pairs.append(("banana4", "banana3",
                      {"underripe": "unripe", "ripe": "ripe", "overripe": "overripe"}, "b4->b3"))
    for src, tgt, lmap, tag in pairs:
        for enc in encs:
            ok = (FEAT / ("%s__%s.npz" % (src, enc))).exists() and (FEAT / ("%s__%s.npz" % (tgt, enc))).exists()
            if not ok:
                continue
            for var in variants:
                for s in seeds:
                    for shot in [0, 1, 5, 10]:
                        for head in ("proto", "linear"):
                            try:
                                E.e3(src, tgt, enc, lmap, shot=shot, seed=s, variant=var,
                                     head_kind=head, tag=tag, align=align)
                            except Exception as e:
                                log("[E3] FAIL %s %s shot=%s: %s" % (tag, enc, shot, e))
                                note_failure("E3", "%s|%s|shot=%s" % (tag, enc, shot), e)
    log("[E3] pairs defined: %d" % len(pairs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all")
    ap.add_argument("--encoders", default="dinov2_s,dinov2_b,clip_b,resnet50")
    ap.add_argument("--datasets", default="")
    ap.add_argument("--shot", default="1,5,10,50")
    ap.add_argument("--seeds", default="0,1,2,3,4")
    ap.add_argument("--img-size", type=int, default=224)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--calib", action="store_true",
                    help="E2 only: also fit per-class support-set thresholds (calibration arm)")
    ap.add_argument("--align", default="none", choices=["none", "bn"],
                    help="E3 only: 'bn' adds the plan's optional feature-level alignment tier "
                         "(z-score with target-domain train statistics, no target labels)")
    ap.add_argument("--variants", default="cls",
                    help="feature variant(s): cls (CLS token) and/or mean (patch mean). "
                         "Both are cached; default stays cls so existing runs are unchanged.")
    ap.add_argument("--heads", default="linear,proto",
                    help="E1 only: adaptation head(s). 'corn' is the plan's ordinal head "
                         "(conditional ordinal regression) and is the E4 ordinal ablation.")
    # ---- plan v2.0 checklist spellings (see PLAN_STAGES below). Each flag is accepted
    # and acted on or explicitly logged; none is silently ignored.
    ap.add_argument("--v2", action="store_true",
                    help="plan §week-3: use the v2 tables/figures (aggregate, figures)")
    ap.add_argument("--rebuild", action="store_true",
                    help="plan §week-3: report is always rebuilt from the result files; "
                         "accepted for spelling compatibility and logged")
    ap.add_argument("--write", default="",
                    help="plan §week-1: seal keys to assert, e.g. 'meta_sha256 known ordinal view'. "
                         "seal.py always derives the full block; the list is logged.")
    ap.add_argument("--bootstrap", type=int, default=0,
                    help="aggregate only: bootstrap resamples for CI (default 2000)")
    ap.add_argument("--fix-leak-check", action="store_true",
                    help="plan §week-1 spelling; validate always runs the group-leak assertion")
    a = ap.parse_args()
    encs = [x for x in a.encoders.split(",") if x]
    heads = [x for x in a.heads.split(",") if x]
    shots = [None if x == "all" else int(x) for x in a.shot.split(",") if x]
    variants = [x for x in a.variants.split(",") if x]
    seeds = [int(x) for x in a.seeds.split(",") if x]
    log("=== run.py stage=%s enc=%s shots=%s seeds=%s ===" % (a.stage, encs, shots, seeds))
    # ---- plan v2.0 stage names -> the scripts that implement them
    if a.stage == "seal":
        # Legacy results have no seal, so the whole corpus is backfilled. A result that
        # already carries a non-derived seal is left alone by seal.py.
        if a.write:
            log("[seal] --write %s: seal.py always derives the full block "
                "(view/ordinal/known/meta_sha256/live/code_version); the asserted key set "
                "is fixed in the file, not selectable" % a.write)
        run_aux("seal.py")
    if a.stage == "aggregate":
        # --v2 is the only aggregate this pipeline has: analyze_v2.py writes T11..T16.
        run_aux("analyze_v2.py", ["--bootstrap", a.bootstrap] if a.bootstrap else [])
    if a.stage == "figures":
        if not a.v2:
            log("[figures] without --v2: drawing the v2 plan figures anyway (they are the "
                "only ones built from the T11/T12 tables)")
        run_aux("fig_v2.py")
    if a.stage == "report":
        # report.py always regenerates from results/*.json + outputs/*.csv; there is no
        # incremental mode, so --rebuild needs no separate code path.
        if a.rebuild:
            log("[report] --rebuild accepted: report.py has no incremental mode, it always "
                "rebuilds from the result files and the aggregate CSVs")
        run_aux("report.py")
    if a.stage == "verify":
        # verify_indep.py re-derives the headline numbers from the stored score arrays with
        # an independent implementation; final_check.py then asserts the package.
        log("[verify] --seeds %s accepted: both verifiers recompute from every stored seed "
            "file and count what they actually read, so the count is measured, not asserted"
            % a.seeds)
        run_aux("verify_indep.py")
        run_aux("final_check.py")
    if a.stage == "validate":
        if a.fix_leak_check:
            log("[validate] --fix-leak-check accepted: the group-leak assertion is part of "
                "final_check.py (card.group_leak_count == 0) and runs unconditionally")
        run_aux("final_check.py")
    if a.stage in ("prepare", "all"):
        stage_prepare()
    if a.stage in ("extract", "all"):
        # Extract for every PREPARED dataset, not only for those a closed-set view was
        # built from: fruits360 is used by the leave-one-fruit-out protocol (stage_e2f)
        # and has no view, and a dataset with no features would silently contribute
        # nothing to it.
        dss = sorted({p.parent.name for p in PROC.glob("*/card.json")})
        if a.datasets:
            dss = [d for d in a.datasets.split(",") if d in dss]
        stage_extract(encs, dss, a.img_size, a.limit)
    if a.stage in ("control",):
        V = views()
        for ctl in ("shuffle_labels", "random_features"):
            stage_e1(V, encs, [5], [0, 1, 2], ["linear"], ["cls"], control=ctl)
    if a.stage in ("e1", "all"):
        V = views()
        stage_e1(V, encs, shots, seeds, heads, variants)
    if a.stage in ("e2", "all"):
        V = views()
        stage_e2(V, [e for e in encs if e in ("dinov2_s", "resnet50")], [None, 5], [0, 1, 2],
                 ["msp", "energy", "mahalanobis", "knn"], variants, calib=a.calib)
        stage_e2c([e for e in encs if e in ("dinov2_s", "resnet50")], [None, 5], [0, 1, 2],
                  ["msp", "energy", "mahalanobis", "knn"])
        # the plan's leave-one-fruit-out P2 (multi-species set only)
        stage_e2f([e for e in encs if e in ("dinov2_s", "resnet50")], [0, 1, 2])
        # the plan's P3 foreign-matter half (cross-dataset unknown species)
        stage_e2x(V, [e for e in encs if e in ("dinov2_s", "resnet50")], [0, 1, 2])
    if a.stage in ("e3", "all"):
        V = views()
        stage_e3(V, encs, seeds[:3], variants, align=a.align)
    log("=== done stage=%s ===" % a.stage)


if __name__ == "__main__":
    main()
