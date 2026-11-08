"""Frozen foundation encoders via timm; feature extraction to disk (float16)."""
import json, time
import numpy as np
import torch
from PIL import Image
import pandas as pd
from pathlib import Path
from .common import PROC, FEAT, log, atomic_write_json, sha256_ids

ENCODERS = {
    "dinov2_s": {"timm": "vit_small_patch14_dinov2.lvd142m", "kind": "vit"},
    "dinov2_b": {"timm": "vit_base_patch14_dinov2.lvd142m", "kind": "vit"},
    "clip_b":   {"timm": "vit_base_patch16_clip_224.openai", "kind": "vit"},
    "resnet50": {"timm": "resnet50.a1_in1k", "kind": "cnn"},
}

_IMAGENET_MEAN = (0.485, 0.456, 0.406)
_IMAGENET_STD = (0.229, 0.224, 0.225)


def build_model(key, img_size=224):
    import timm
    spec = ENCODERS[key]
    kw = dict(pretrained=True, num_classes=0)
    if spec["kind"] == "vit":
        kw.update(img_size=img_size, dynamic_img_size=True)
    m = timm.create_model(spec["timm"], **kw)
    m.eval()
    cfg = timm.data.resolve_data_config({}, model=m)
    return m, cfg


def load_image(path, size=224):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    # resize short side then center crop (standard protocol)
    s = size / min(w, h)
    if s != 1.0:
        im = im.resize((max(1, int(round(w * s))), max(1, int(round(h * s)))), Image.BICUBIC)
    w, h = im.size
    l = (w - size) // 2
    t = (h - size) // 2
    im = im.crop((l, t, l + size, t + size))
    a = np.asarray(im, dtype=np.float32) / 255.0
    return a


def to_tensor(batch_np, mean, std):
    x = torch.from_numpy(np.stack(batch_np, 0)).permute(0, 3, 1, 2)
    m = torch.tensor(mean).view(1, 3, 1, 1)
    s = torch.tensor(std).view(1, 3, 1, 1)
    return (x - m) / s


@torch.no_grad()
def extract(ds, enc_key, img_size=224, batch=64, device="cuda", limit=None):
    meta = pd.read_csv(PROC / ds / "meta.csv")
    if limit:
        meta = meta.iloc[:limit]
    m, cfg = build_model(enc_key, img_size)
    m = m.to(device).eval()
    mean = cfg.get("mean", _IMAGENET_MEAN)
    std = cfg.get("std", _IMAGENET_STD)
    ids, cls_feats, mean_feats = [], [], []
    t0 = time.time()
    buf, buf_ids = [], []
    def flush():
        if not buf:
            return
        x = to_tensor(buf, mean, std).to(device)
        with torch.autocast("cuda", dtype=torch.float16):
            f = m.forward_features(x)
        f = f.float()
        if f.ndim == 4:  # CNN: B,C,H,W
            v = f.mean(dim=(2, 3))
            cls_feats.append(v.cpu().numpy().astype(np.float16))
            mean_feats.append(v.cpu().numpy().astype(np.float16))
        else:
            c = f[:, 0]
            p = f[:, 1:].mean(dim=1) if f.shape[1] > 1 else c
            cls_feats.append(c.cpu().numpy().astype(np.float16))
            mean_feats.append(p.cpu().numpy().astype(np.float16))
        ids.extend(buf_ids)
        buf.clear(); buf_ids.clear()
    for _, r in meta.iterrows():
        try:
            buf.append(load_image(str(PROC / r["path"]), img_size))
            buf_ids.append(r["id"])
        except Exception as e:
            log("[feat] skip %s: %s" % (r["id"], e))
        if len(buf) >= batch:
            flush()
            if len(ids) % (batch * 10) == 0:
                el = time.time() - t0
                log("[feat] %s %s: %d/%d (%.1f img/s)" % (ds, enc_key, len(ids), len(meta), len(ids) / max(el, 1e-6)))
    flush()
    cls_arr = np.concatenate(cls_feats, 0)
    mean_arr = np.concatenate(mean_feats, 0)
    out = FEAT / ("%s__%s.npz" % (ds, enc_key))
    np.savez_compressed(out, cls=cls_arr, mean=mean_arr, ids=np.array(ids))
    info = {"dataset": ds, "encoder": enc_key, "timm": ENCODERS[enc_key]["timm"],
            "img_size": img_size, "dim": int(cls_arr.shape[1]), "n": int(cls_arr.shape[0]),
            "ids_sha256": sha256_ids(ids), "seconds": round(time.time() - t0, 1),
            "dtype": "float16", "tta": "none", "resize": "short-side+center-crop"}
    atomic_write_json(FEAT / ("%s__%s.json" % (ds, enc_key)), info)
    log("[feat] done %s %s n=%d dim=%d %.1fs -> %s" % (ds, enc_key, len(ids), cls_arr.shape[1],
                                                       time.time() - t0, out))
    del m
    torch.cuda.empty_cache()
    return info
