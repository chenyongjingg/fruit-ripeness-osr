#!/usr/bin/env python3
"""End-to-end ResNet-50 fine-tuning baseline (the plan's "full fine-tuning" arm).

Everything else in this project uses FROZEN features. This stage is the deliberate
exception, and it exists so the paper's central claim ("frozen foundation-model features
beat a fully fine-tuned ResNet-50 in the few-shot regime") is tested against the arm the
claim is about.

Protocol mirrors E1 exactly: support drawn from the train split only (same
balanced_support call and the same seeds), evaluation on the test split only, and the
val split untouched. Results are written in the same JSON schema with exp="E1ft", so
report.py aggregates them next to the frozen-feature runs.

Caveat recorded in every record: fine-tuning uses random crops/flips; the frozen-feature
arms see one deterministic centre crop. The comparison therefore favours the fine-tuned
arm if anything, which is the conservative direction for the claim.
"""
import argparse, json, sys, time, hashlib
from pathlib import Path
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import PROC, RESULTS, log, atomic_write_json, read_json, sha256_ids, CODE_VERSION
from rio.methods import closed_set_metrics
from rio.experiments import balanced_support, run_id, result_path

try:
    FLIP = Image.Transpose.FLIP_LEFT_RIGHT
except AttributeError:  # Pillow < 9.1
    FLIP = Image.FLIP_LEFT_RIGHT

MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)


class ImgSet(Dataset):
    def __init__(self, paths, labels, lab2i, train, size=224):
        self.paths, self.labels, self.lab2i, self.train, self.size = paths, labels, lab2i, train, size

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, i):
        im = Image.open(self.paths[i]).convert("RGB")
        if self.train:
            w, h = im.size
            s = int(self.size * 1.15)
            im = im.resize((s, s), Image.BILINEAR)
            x = np.random.randint(0, s - self.size + 1)
            y = np.random.randint(0, s - self.size + 1)
            im = im.crop((x, y, x + self.size, y + self.size))
            if np.random.rand() < 0.5:
                im = im.transpose(FLIP)
        else:
            w, h = im.size
            s = min(w, h)
            im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
            im = im.resize((self.size, self.size), Image.BILINEAR)
        a = (np.asarray(im, dtype=np.float32) / 255.0 - MEAN) / STD
        return torch.from_numpy(a.transpose(2, 0, 1)), self.lab2i[self.labels[i]]


def build_model(n_cls):
    import timm
    return timm.create_model("resnet50.a1_in1k", pretrained=True, num_classes=n_cls)


def run_one(ds, subset_fn, ordinal, shot, seed, tag, epochs=30, lr=3e-4, batch=16, size=224):
    cfg = {"exp": "E1ft", "dataset": ds, "view": tag, "encoder": "resnet50_ft", "variant": "pixel",
           "head": "finetune", "shot": shot, "seed": seed, "C": None, "control": "none",
           "epochs": epochs, "lr": lr}
    if result_path(cfg).exists():
        return read_json(result_path(cfg))
    m = pd.read_csv(PROC / ds / "meta.csv")
    if subset_fn is not None:
        m = m[m.apply(subset_fn, axis=1)].reset_index(drop=True)
    labels = [c for c in ordinal if c in set(m["label_name"])]
    m = m[m["label_name"].isin(labels)].reset_index(drop=True)
    if len(m) == 0:
        return None
    sup_idx, per = balanced_support(m, labels, shot, seed)
    if len(sup_idx) == 0:
        return None
    lab2i = {c: i for i, c in enumerate(labels)}
    tr = m.loc[sup_idx]
    te = m[m["split"] == "test"].reset_index(drop=True)
    if len(te) == 0:
        return None
    torch.manual_seed(seed)
    np.random.seed(seed)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    model = build_model(len(labels)).to(dev)
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    lossf = nn.CrossEntropyLoss()
    dl = DataLoader(ImgSet([str(PROC / p) for p in tr["path"]], list(tr["label_name"]), lab2i, True, size),
                    batch_size=min(batch, len(tr)), shuffle=True, num_workers=4, drop_last=False)
    model.train()
    for ep in range(epochs):
        for xb, yb in dl:
            xb, yb = xb.to(dev, non_blocking=True), yb.to(dev)
            opt.zero_grad()
            loss = lossf(model(xb), yb)
            loss.backward()
            opt.step()
    model.eval()
    dle = DataLoader(ImgSet([str(PROC / p) for p in te["path"]], list(te["label_name"]), lab2i, False, size),
                     batch_size=64, shuffle=False, num_workers=4)
    preds = []
    with torch.no_grad():
        for xb, _ in dle:
            preds.append(model(xb.to(dev)).argmax(1).cpu().numpy())
    pred = np.concatenate(preds)
    pred_lab = np.array([labels[i] for i in pred])
    met = closed_set_metrics(te["label_name"].values, pred_lab, labels)
    met.update({"n_support": int(len(tr)), "support_per_class": per,
                "support_ids_sha256": sha256_ids(tr["id"].values),
                "test_ids_sha256": sha256_ids(te["id"].values), "n_test": int(len(te)),
                "note": "end-to-end fine-tuning; augmentation on, so this arm is if anything advantaged"})
    del model
    torch.cuda.empty_cache()
    rec = {"config": cfg, "metrics": met, "code_version": CODE_VERSION,
           "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "extra": {}}
    atomic_write_json(result_path(cfg), rec)
    return rec


def main():
    import run as R
    ap = argparse.ArgumentParser()
    ap.add_argument("--views", default="banana3,fruit12_banana,fruit12_apple,banana4")
    ap.add_argument("--shots", default="1,5,10,50")
    ap.add_argument("--seeds", default="0,1,2")
    ap.add_argument("--epochs", type=int, default=30)
    a = ap.parse_args()
    V = R.views()
    shots = [int(s) for s in a.shots.split(",")]
    seeds = [int(s) for s in a.seeds.split(",")]
    todo = [(v, vv, sh, s) for v in a.views.split(",") if v in V for vv in [V[v]]
            for sh in shots for s in seeds]
    log("=== finetune runs=%d epochs=%d ===" % (len(todo), a.epochs))
    for i, (name, v, sh, s) in enumerate(todo):
        try:
            r = run_one(v["ds"], v["subset"], v["ordinal"], sh, s, name, epochs=a.epochs)
            if r:
                log("[E1ft] %s shot=%d seed=%d acc=%.3f f1=%.3f (%.0fs)"
                    % (name, sh, s, r["metrics"]["acc"], r["metrics"]["macro_f1"], 0))
        except Exception as e:
            import traceback
            log("[E1ft] FAIL %s shot=%d seed=%d: %s\n%s" % (name, sh, s, e, traceback.format_exc()[-500:]))
        if (i + 1) % 10 == 0:
            log("[E1ft] %d/%d" % (i + 1, len(todo)))
    log("=== finetune done ===")


if __name__ == "__main__":
    main()
