"""Dataset decoding: raw downloads -> processed/{ds}/images + meta.csv (leakage-safe)."""
import io, json, os, re, hashlib, zipfile, shutil
from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image, ImageOps
from .common import RAW, PROC, log, atomic_write_json, read_json, sha256_file, now

RNG_SEED = 0


def _img_bytes_hash(b):
    return hashlib.md5(b).hexdigest()


def _write_image(b, dst):
    im = Image.open(io.BytesIO(b))
    im = im.convert("RGB")
    im.save(dst, "JPEG", quality=92)


def _finalize(ds, rows, classes, offscale, source, official_split, extra_card=None):
    """rows: list of dict(id,label_name,split,group); images already written."""
    df = pd.DataFrame(rows).sort_values("id").reset_index(drop=True)
    out = PROC / ds
    df.to_csv(out / "meta.csv", index=False, encoding="utf-8")
    g = df.groupby("group")["split"].nunique()
    leaks = int((g > 1).sum())
    card = {
        "dataset": ds, "classes": classes, "offscale": offscale,
        "n_images": int(len(df)), "n_groups": int(df["group"].nunique()),
        "split_counts": {k: int(v) for k, v in df["split"].value_counts().items()},
        "class_counts": {k: int(v) for k, v in df["label_name"].value_counts().items()},
        "group_leak_count": leaks, "official_split": bool(official_split),
        "source": source, "built_at": now(), "meta_sha256": sha256_file(out / "meta.csv"),
    }
    if extra_card:
        card.update(extra_card)
    atomic_write_json(out / "card.json", card)
    if leaks:
        raise AssertionError("GROUP LEAKAGE in %s: %d groups span splits" % (ds, leaks))
    log("[data] %s: n=%d classes=%d splits=%s groups=%d" % (
        ds, len(df), len(classes), card["split_counts"], card["n_groups"]))
    return card


def _stratified_split(rows, frac=(0.7, 0.15, 0.15), seed=RNG_SEED):
    """Group-aware split. A group (source image) is assigned to exactly ONE split.

    Stratification is done over GROUPS (using each group's majority label), not over
    rows: assigning per label would place the same group in two splits whenever the
    group contains boxes of two classes (fruit12 has multi-class source images).
    """
    from collections import defaultdict, Counter
    rng = np.random.RandomState(seed)
    g2rows, g2lab = defaultdict(list), {}
    for r in rows:
        g2rows[r["group"]].append(r)
    for g, rs in g2rows.items():
        g2lab[g] = Counter(r["label_name"] for r in rs).most_common(1)[0][0]
    by_lab = defaultdict(list)
    for g, lab in g2lab.items():
        by_lab[lab].append(g)
    gmap = {}
    for lab, gs in by_lab.items():
        gs = sorted(gs)
        rng.shuffle(gs)
        n = len(gs)
        n_tr = max(1, int(round(frac[0] * n)))
        n_va = max(1, int(round(frac[1] * n))) if n >= 5 else 0
        n_tr = min(n_tr, max(1, n - n_va))
        for i, g in enumerate(gs):
            gmap[g] = "train" if i < n_tr else ("val" if i < n_tr + n_va else "test")
    for r in rows:
        r["split"] = gmap[r["group"]]
    return rows


def build_parquet_classification(ds, parquet_files, label_names, classes, offscale,
                                 source, split_from_file=False):
    """HF parquet with columns image (struct with bytes) + label (class index)."""
    import pyarrow.parquet as pq
    out = PROC / ds
    imgdir = out / "images"
    imgdir.mkdir(parents=True, exist_ok=True)
    rows, k = [], 0
    for pf, split in parquet_files:
        t = pq.read_table(pf)
        imgcol = t.column("image")
        lab = t.column("label")
        for i in range(t.num_rows):
            cell = imgcol[i].as_py()
            b = None
            if isinstance(cell, dict):
                b = cell.get("bytes")
                if b is None and cell.get("path"):
                    b = open(cell["path"], "rb").read()
            if b is None:
                continue
            lab_i = int(lab[i].as_py())
            name = label_names[lab_i]
            iid = "%s_%06d" % (ds, k)
            k += 1
            dst = imgdir / (iid + ".jpg")
            try:
                _write_image(b, dst)
            except Exception as e:
                log("[data] skip undecodable image %s: %s" % (iid, e))
                continue
            rows.append({"id": iid, "path": str(dst.relative_to(PROC)), "label_name": name,
                         "split": split, "group": _img_bytes_hash(b)})
    if not split_from_file:
        rows = _stratified_split(rows)
    return _finalize(ds, rows, classes, offscale, source, official_split=split_from_file)


def build_zip_folders(ds, zip_path, classes, offscale, source,
                      split_dirs=("train", "valid", "test"), group_fn=None,
                      require_split_dir=True):
    """ZIP with <split>/<class>/<img> layout.

    group_fn(member_path) -> leakage group, where member_path is the full name inside the
    archive (class folders are needed: Fruits-360 numbers its specimens per class). The
    default (content hash) is right only when
    every file is its own specimen; datasets that photograph each fruit twice would put
    the two frames in different splits and leak. `require_split_dir=False` accepts an
    archive with no split folders (<class>/<img>), in which case a group-aware
    stratified split is made here and the card records official_split=False.
    """
    out = PROC / ds
    imgdir = out / "images"
    imgdir.mkdir(parents=True, exist_ok=True)
    zf = zipfile.ZipFile(zip_path)
    rows, bad = [], 0
    sd = {s.lower() for s in split_dirs}
    for n in zf.namelist():
        if not n.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        parts = n.split("/")
        sp = next((p for p in parts if p.lower() in sd), None)
        if sp is None and require_split_dir:
            continue
        lab = parts[-2]
        if classes is not None and lab not in classes:
            continue
        try:
            b = zf.read(n)
        except Exception as e:
            log("[data] corrupt zip member %s: %s" % (n, e))
            bad += 1
            continue
        iid = "%s_%06d" % (ds, len(rows))
        dst = imgdir / (iid + ".jpg")
        try:
            _write_image(b, dst)
        except Exception as e:
            log("[data] skip undecodable %s: %s" % (n, e))
            continue
        # Fruits-360 spells the folders "Training"/"Test"; map the observed spellings
        # explicitly rather than trusting .lower() to land on the canonical three.
        split = None
        if sp is not None:
            split = {"train": "train", "training": "train", "valid": "val", "val": "val",
                     "validation": "val", "test": "test"}[sp.lower()]
        grp = group_fn(n) if group_fn else _img_bytes_hash(b)
        rows.append({"id": iid, "path": str(dst.relative_to(PROC)), "label_name": lab,
                     "split": split, "group": grp})
    n_seen = len(rows) + bad
    if n_seen and bad / float(n_seen) > 0.02:
        raise AssertionError("%s: %d/%d zip members unreadable (%.1f%%) - archive is corrupt"
                             % (ds, bad, n_seen, 100.0 * bad / n_seen))
    official = True
    if not require_split_dir:
        official = False
        if any(r["split"] is None for r in rows):
            rows = _stratified_split(rows)
    if classes is None:      # "take whatever is in the archive"
        classes = sorted({r["label_name"] for r in rows})
    card = _finalize(ds, rows, classes, offscale, source, official_split=official)
    card["n_corrupt_members"] = bad
    card["group_key"] = "filename-group" if group_fn else "content-hash"
    atomic_write_json(PROC / ds / "card.json", card)
    return card


def build_fruit12(zip_path):
    """Carlosmg23/fruit-ripeness-12clases: crops/<Class>/*.jpg + labels.csv + split.csv.

    labels.csv columns (Spanish): recorte=relative path, clase="Banana Ripe",
    fruta=fruit, estado=state, nivel=ordinal level, split=train/valid/test,
    group_id=per-box id, fuente=SOURCE IMAGE id, indice_caja=box index.

    Leakage group = `fuente` (source image): several crops share one photograph and
    must never span splits. `group_id` is per box and is NOT usable for this.
    """
    ds = "fruit12"
    out = PROC / ds
    imgdir = out / "images"
    imgdir.mkdir(parents=True, exist_ok=True)
    zf = zipfile.ZipFile(zip_path)
    names = set(zf.namelist())
    cand = [n for n in names if n.endswith("labels.csv")]
    root = cand[0][: -len("labels.csv")] if cand else ""
    labels = pd.read_csv(io.BytesIO(zf.read(root + "labels.csv")))
    col_path = next((c for c in ("recorte", "path", "filepath", "filename", "ruta") if c in labels.columns), None)
    col_lab = next((c for c in ("clase", "class", "label", "clase_nombre") if c in labels.columns), None)
    col_spl = next((c for c in ("split", "set", "conjunto") if c in labels.columns), None)
    col_grp = next((c for c in ("fuente", "group", "group_id", "session") if c in labels.columns), None)
    if not (col_path and col_lab):
        raise KeyError("labels.csv columns unknown: %s" % list(labels.columns))
    rows, missing = [], 0
    for _, r in labels.iterrows():
        rel = str(r[col_path])
        member = root + rel
        if member not in names:
            alt = [n for n in names if n.endswith("/" + rel)]
            if not alt:
                missing += 1
                continue
            member = alt[0]
        b = zf.read(member)
        lab = str(r[col_lab]).strip().replace(" ", "_")
        spl = str(r[col_spl]).strip().lower() if col_spl else None
        spl = {"train": "train", "valid": "val", "val": "val", "test": "test"}.get(spl)
        grp = str(r[col_grp]) if col_grp else _img_bytes_hash(b)
        iid = "%s_%06d" % (ds, len(rows))
        dst = imgdir / (iid + ".jpg")
        try:
            _write_image(b, dst)
        except Exception as e:
            log("[data] skip undecodable %s: %s" % (member, e))
            continue
        rows.append({"id": iid, "path": str(dst.relative_to(PROC)), "label_name": lab,
                     "split": spl, "group": grp})
    if missing:
        log("[data] fruit12: %d rows whose file is missing from the archive" % missing)
    if any(r["split"] is None for r in rows):
        log("[data] fruit12: %d rows without split -> assigned by group" % sum(r["split"] is None for r in rows))
        miss = [r for r in rows if r["split"] is None]
        for r2 in _stratified_split([dict(r) for r in miss]):
            for r in miss:
                if r["id"] == r2["id"]:
                    r["split"] = r2["split"]
    # leakage check on the official split; re-split group-aware if it leaks
    from collections import defaultdict
    g2s = defaultdict(set)
    for r in rows:
        g2s[r["group"]].add(r["split"])
    leak = sum(1 for g, ss in g2s.items() if len(ss) > 1)
    if leak:
        log("[data] fruit12: official split leaks %d/%d source images -> group-aware re-split"
            % (leak, len(g2s)))
        rows = _stratified_split(rows)
        official = False
    else:
        official = col_spl is not None
    classes = sorted({r["label_name"] for r in rows})
    off = [c for c in classes if "rotten" in c.lower()]
    card = _finalize(ds, rows, classes, off, "HF Carlosmg23/fruit-ripeness-12clases (CC BY 4.0)",
                     official_split=official)
    card["split_was_regrouped"] = bool(leak)
    atomic_write_json(PROC / ds / "card.json", card)
    return card


def build_raspgrade(ds="raspgrade"):
    """HF FBK-TeV/RaspGrade: 200 conveyor-belt images, FIVE grades as instance polygons.

    This is a segmentation set, not an image-level classification set: one image shows
    many berries at once and all 200 images contain more than one grade, so any image
    label would be a majority vote over berries and would measure something else. Each
    berry polygon of class 1..5 is therefore cut out (bbox + 10% margin, square-padded)
    and becomes ONE sample. Class 0 is the whole bunch region -- once per image, bbox
    up to the full frame -- and is not a ripeness grade, so it is dropped rather than
    silently becoming a sixth class.

    Consequences that must travel with any number computed on this set:
      * samples are berries, `group` is their source image: the split is group-aware, so
        no berry in test shares an image with one in train;
      * berries from one image are not independent observations, so the effective n is
        nearer the image count (200) than the crop count;
      * Grade 4 and Grade 5 are rare (62 and 94 polygons) and the n>=30 gate in
        report/analyze_v2 decides whether their cells may be read as estimates.
    """
    import pyarrow.parquet as pq
    out = PROC / ds
    imgdir = out / "images"
    imgdir.mkdir(parents=True, exist_ok=True)
    rows = []
    drop_small = 0
    for pf in (RAW / ds / "train-00000-of-00001.parquet",
               RAW / ds / "valid-00000-of-00001.parquet"):
        if not pf.exists():
            raise FileNotFoundError(pf)
        t = pq.read_table(str(pf))
        for i in range(t.num_rows):
            cell = t.column("image")[i].as_py()
            b = cell.get("bytes") if isinstance(cell, dict) else None
            iid = str(t.column("image_id")[i].as_py())
            if not b:
                continue
            try:
                im = Image.open(io.BytesIO(b)).convert("RGB")
            except Exception as e:
                log("[data] raspgrade: skip undecodable %s: %s" % (iid, e))
                continue
            W, H = im.size
            polys = t.column("labels")[i].as_py()
            # pyarrow hands back a ragged python list; np.asarray on that raises on
            # numpy>=2 ("inhomogeneous shape"), so the container is normalised first and
            # each polygon is converted on its own.
            if isinstance(polys, np.ndarray) and polys.dtype == object:
                items = list(polys.ravel())
            elif isinstance(polys, (list, tuple)):
                items = list(polys)
            else:
                items = [polys]
            k = 0
            for poly in items:
                a = np.asarray(poly, dtype=float).ravel()
                if a.size < 7:                    # class id + at least 3 points
                    continue
                cls = int(a[0])
                if cls < 1 or cls > 5:            # 0 = bunch region, not a grade
                    continue
                xy = a[1:1 + 2 * ((a.size - 1) // 2)].reshape(-1, 2)
                x0, y0 = xy.min(0) * [W, H]
                x1, y1 = xy.max(0) * [W, H]
                w, h = x1 - x0, y1 - y0
                if w < 24 or h < 24:              # a sliver cannot carry texture
                    drop_small += 1
                    continue
                m = 0.10 * max(w, h)              # context margin
                cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
                half = max(w, h) / 2 + m
                box = (int(max(0, cx - half)), int(max(0, cy - half)),
                       int(min(W, cx + half)), int(min(H, cy + half)))
                crop = im.crop(box)
                if crop.size[0] < 24 or crop.size[1] < 24:
                    drop_small += 1
                    continue
                sid = "%s_%02d" % (iid, k)
                k += 1
                dst = imgdir / (sid + ".jpg")
                crop.save(dst, "JPEG", quality=92)
                rows.append({"id": sid, "path": str(dst.relative_to(PROC)),
                             "label_name": "grade%d" % cls, "split": None, "group": iid})
    rows = _stratified_split(rows)
    classes = ["grade%d" % i for i in range(1, 6)]
    card = _finalize(ds, rows, classes, [], "HF FBK-TeV/RaspGrade (CC BY-NC-4.0)",
                     official_split=False,
                     extra_card={"unit": "berry instance (polygon crop), NOT image",
                                 "n_source_images": int(len({r["group"] for r in rows})),
                                 "dropped_small_polygons": drop_small,
                                 "note": "class 0 (bunch region) excluded; splits are "
                                         "group-aware over source images"})
    return card


# --------------------------------------------------------------------------- ninepeach
# figshare record 27125373 ("Peach Maturity Dataset", CC BY 4.0, doi 10.6084/m9.figshare.27125373).
#
# WHAT THE ARCHIVE ACTUALLY IS (checked against the record's own description, the central
# directory, and the decoded pixels, not against the plan): 1,245 smartphone photographs
# (3024x4032) taken in a real orchard, 3,493 instance boxes, THREE ripeness stages whose
# XML names are `immature` / `semi-mature` / `mature` (measured: 1,618 / 707 / 1,168 boxes;
# the figshare prose calls the same three stages "hard ripe / semi-ripe / fully ripe" —
# the XML is what the code reads). The record has no cultivar field and no cultivar
# directories, so the plan's "3,849 张、9 品种" and its "8 cultivars known + 1 held out"
# arm cannot be built from it. The card records this; the code does not invent labels.
#
# ORIENTATION: every one of the 1,245 JPEGs is stored landscape (4032x3024) with EXIF
# orientation 6, i.e. "rotate 90 deg clockwise on display", while every XML declares
# 3024x4032 — the boxes live in the DISPLAYED frame. Cropping the raw array with those
# boxes produced a box whose lower edge was past the image edge (the first build died on
# `Coordinate 'lower' is less than 'upper'`). Exif-transposing first makes im.size equal
# the XML size for all 1,245, which is asserted below rather than assumed.
NINEPEACH_CLASSES = ["immature", "semi-mature", "mature"]   # ripeness order
NINEPEACH_ALIAS = {"immature": "immature", "semi-mature": "semi-mature", "mature": "mature",
                   "semi mature": "semi-mature", "semimature": "semi-mature"}


def ninepeach_index(zip_path=None):
    """Read the archive WITHOUT writing anything: annotation table + image member table."""
    import xml.etree.ElementTree as ET
    from collections import defaultdict
    ds = "ninepeach"
    zp = Path(zip_path) if zip_path else RAW / ds / "Peach_maturity_dataset.zip"
    zf = zipfile.ZipFile(zp)
    infos = zf.infolist()
    xmls = [i for i in infos if i.filename.lower().endswith(".xml")]
    imgs = [i for i in infos if i.filename.lower().endswith((".jpg", ".jpeg", ".png"))]
    by_base = defaultdict(list)
    for i in imgs:
        by_base[os.path.basename(i.filename).lower()].append(i)
    # A basename that appears in more than one split folder must be the SAME photograph
    # (same CRC32 and size), otherwise calling it one leakage group would silently merge
    # two different pictures and the split would be wrong in the other direction.
    dup_conflicts = []
    for base, lst in by_base.items():
        if len(lst) > 1:
            sig = {(i.CRC, i.file_size) for i in lst}
            if len(sig) > 1:
                dup_conflicts.append({"basename": base,
                                      "members": [i.filename for i in lst],
                                      "distinct_contents": len(sig)})
    anns = []
    for i in xmls:
        try:
            r = ET.fromstring(zf.read(i.filename))
        except Exception as e:
            log("[data] ninepeach: unreadable annotation %s: %s" % (i.filename, e))
            continue
        fn = (r.findtext("filename") or "").strip()
        sz = r.find("size")
        W = int(sz.findtext("width")) if sz is not None else None
        H = int(sz.findtext("height")) if sz is not None else None
        objs = []
        for o in r.iter("object"):
            nm = (o.findtext("name") or "").strip().lower()
            nm = NINEPEACH_ALIAS.get(nm, nm)
            b = o.find("bndbox")
            if b is None:
                continue
            try:
                box = [int(float(b.findtext(k))) for k in ("xmin", "ymin", "xmax", "ymax")]
            except Exception:
                continue
            objs.append((nm, box))
        anns.append({"xml": i.filename, "filename": fn, "W": W, "H": H, "objects": objs})
    return {"zip": str(zp), "xmls": xmls, "images": imgs, "by_base": by_base, "anns": anns,
            "dup_conflicts": dup_conflicts}


def _split_of(member):
    for p in member.split("/"):
        q = p.lower()
        if q in ("train", "training"):
            return "train"
        if q in ("val", "valid", "validation"):
            return "val"
        if q in ("test", "testing"):
            return "test"
    return None


def build_ninepeach(ds="ninepeach", zip_path=None, min_px=24):
    """Instance crops (bbox + 10% margin) from the figshare peach archive.

    Unit = one annotated peach, not one photograph: the photographs are 12 MP orchard
    frames holding several fruits each, and 3,493 boxes sit on 1,245 images. `group` is
    the source photograph, so no crop in test shares a photograph with one in train.
    """
    from collections import defaultdict
    idx = ninepeach_index(zip_path)
    zf = zipfile.ZipFile(idx["zip"])
    out = PROC / ds
    imgdir = out / "images"
    imgdir.mkdir(parents=True, exist_ok=True)
    rows, drop_small, drop_nobox, missing_img = [], 0, 0, 0
    n_transposed, size_mismatch = 0, 0
    for a in idx["anns"]:
        base = os.path.basename(a["filename"]).lower()
        cand = idx["by_base"].get(base) or []
        if not cand:
            missing_img += 1
            continue
        ci = sorted(cand, key=lambda i: i.filename)
        try:
            b = zf.read(ci[0].filename)
            im = Image.open(io.BytesIO(b))
            raw_size = im.size
            # Boxes are in the EXIF-displayed frame; see the note above the class list.
            im = ImageOps.exif_transpose(im).convert("RGB")
        except Exception as e:
            log("[data] ninepeach: undecodable %s: %s" % (ci[0].filename, e))
            missing_img += 1
            continue
        W, H = im.size
        if im.size != raw_size:
            n_transposed += 1
        if a["W"] and a["H"] and im.size != (a["W"], a["H"]):
            size_mismatch += 1
            log("[data] ninepeach: %s decodes to %s but the XML says %s; boxes are in the "
                "XML frame" % (ci[0].filename, im.size, (a["W"], a["H"])))
        # Group = the source photograph. Two split copies of the same photograph have the
        # same basename, so one group spans every copy and the leak check can see it.
        grp = base
        split = _split_of(ci[0].filename)
        if split is None:
            seen = sorted({_split_of(c.filename) for c in cand if _split_of(c.filename)})
            if seen:
                split = seen[0]
        k = 0
        for nm, (x0, y0, x1, y1) in a["objects"]:
            if nm not in NINEPEACH_CLASSES:
                drop_nobox += 1
                continue
            if x1 <= x0 or y1 <= y0:
                drop_nobox += 1
                continue
            w, h = x1 - x0, y1 - y0
            if w < min_px or h < min_px:
                drop_small += 1
                continue
            m = 0.10 * max(w, h)
            cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
            half = max(w, h) / 2.0 + m
            box = (int(max(0, cx - half)), int(max(0, cy - half)),
                   int(min(W, cx + half)), int(min(H, cy + half)))
            crop = im.crop(box)
            if crop.size[0] < min_px or crop.size[1] < min_px:
                drop_small += 1
                continue
            iid = "%s_%05d" % (os.path.splitext(base)[0], k)
            k += 1
            dst = imgdir / (iid + ".jpg")
            crop.save(dst, "JPEG", quality=92)
            rows.append({"id": iid, "path": str(dst.relative_to(PROC)),
                         "label_name": nm, "split": split, "group": grp})
    if size_mismatch:
        # The boxes were read in the XML frame; if the decoded (EXIF-transposed) image has a
        # different size, the crop offsets are wrong but every downstream check still passes
        # — so this is refused here instead of being reported as a good build.
        raise AssertionError(
            "ninepeach: %d images decode to a size other than their XML <size> after "
            "EXIF transposition; bounding boxes would be applied to the wrong frame"
            % size_mismatch)
    if not rows:
        # An empty build must stop here: _finalize would write a card with n_images=0 and
        # the run would look "prepared" to every later stage.
        raise AssertionError(
            "ninepeach: no crops built (annotations=%d, image members=%d, "
            "annotations without a matching image=%d)"
            % (len(idx["anns"]), len(idx["images"]), missing_img))
    official = bool(rows) and all(r["split"] for r in rows)
    # An "official" split with only one folder (everything under train/) would leave the
    # open-set protocols with zero test rows. Two folders are not enough either unless one
    # of them is a test side, so the accepted shape is checked, not assumed.
    if official:
        seen = {r["split"] for r in rows}
        if len(seen) < 2 or "test" not in seen:
            log("[data] ninepeach: archive split folders are %s -> not a usable official "
                "split, making a group-aware one" % sorted(seen))
            official = False
    leak = 0
    if official:
        g2s = defaultdict(set)
        for r in rows:
            g2s[r["group"]].add(r["split"])
        leak = sum(1 for g, ss in g2s.items() if len(ss) > 1)
    if (not official) or leak:
        if leak:
            log("[data] ninepeach: official split puts %d/%d photographs in >1 split "
                "-> group-aware re-split" % (leak, len(g2s)))
        rows = _stratified_split(rows)
        official = False
    card = _finalize(ds, rows, list(NINEPEACH_CLASSES), [],
                     "figshare 27125373 Peach Maturity Dataset (CC BY 4.0, "
                     "doi 10.6084/m9.figshare.27125373)",
                     official_split=official,
                     extra_card={
                         "unit": "annotated peach instance (bbox crop), NOT image",
                         "n_source_images_annotated": len({a["filename"] for a in idx["anns"]}),
                         "n_source_images_used": int(len({r["group"] for r in rows})),
                         "exif_transposed": n_transposed,
                         "xml_size_mismatch": size_mismatch,
                         "n_boxes_in_annotations": int(sum(len(a["objects"]) for a in idx["anns"])),
                         "dropped_small_boxes": drop_small,
                         "dropped_unknown_or_bad_boxes": drop_nobox,
                         "annotations_without_image": missing_img,
                         "class_order": NINEPEACH_CLASSES,
                         "class_name_source": "XML <object><name>; ripeness order as shipped",
                         "plan_claim_vs_archive": (
                             "plan v2.0 row 1 claims '3,849 images, 9 cultivars, 3 grades' and an "
                             "'8 cultivars known + 1 held out' arm. The figshare record (v1 and v2, "
                             "same 8,838,332,680-byte zip) and the archive itself state 1,245 "
                             "images, 3,493 boxes, 3 stages, and contain NO cultivar field or "
                             "folder. Cultivar-level P2 is therefore not buildable from this "
                             "source; it is recorded as unavailable rather than approximated."),
                         "annotation_format": "Pascal VOC XML (the record also ships YOLO txt)",
                         "duplicate_basenames": int(sum(1 for v in idx["by_base"].values()
                                                        if len(v) > 1)),
                         "duplicate_basename_conflicts": idx["dup_conflicts"][:20],
                     })
    return card
