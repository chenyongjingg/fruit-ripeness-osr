#!/usr/bin/env python3
"""LoRA adaptation of DINOv2-S (the plan's third RQ1 adaptation method).

The plan lists three ways to adapt a frozen foundation model to a new crop:
linear probing, prototypical networks, and LoRA. The first two are computed from
cached frozen features (experiments.py). This script adds the third, so RQ1 is
covered in full and the paper has no gap where a reviewer would ask "why not LoRA".

Protocol is identical to E1 (frozen) and E1ft (end-to-end):
  * support set drawn from the train split only, same balanced_support + seeds;
  * evaluation on the test split only, val untouched;
  * the same deterministic centre-crop preprocessing at eval time.

Only the LoRA adapters (qkv + proj of every attention block) are trained; the
DINOv2 backbone stays frozen, which is the point of the method. Training-time
augmentation (random resized crop + horizontal flip) is used, exactly as in the
E1ft arm, so those two arms are comparable with each other; the frozen-feature
arms see one deterministic centre crop, and that asymmetry is recorded in every
result so it is never silently forgotten.
"""
import argparse, sys, time
from pathlib import Path
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_finetune as FT
from rio.common import PROC, log, atomic_write_json, read_json, sha256_ids, CODE_VERSION
from rio.methods import closed_set_metrics
from rio.experiments import balanced_support, result_path

LORA_NOTE = ("LoRA (r=%d, alpha=%d) on qkv+proj of DINOv2-S; backbone frozen; "
             "training-time crop/flip augmentation on, so this arm is if anything advantaged "
             "relative to the deterministic-crop frozen-feature arms")


def build_lora(n_cls, rank, alpha):
    import timm
    from peft import LoraConfig, get_peft_model
    # img_size=224 to match the frozen-feature arms (see README_SERVER.md §6.3)
    base = timm.create_model("vit_small_patch14_dinov2.lvd142m", pretrained=True,
                             img_size=224, num_classes=n_cls)
    cfg = LoraConfig(r=rank, lora_alpha=alpha, lora_dropout=0.0, bias="none",
                     target_modules=["qkv", "proj"], task_type=None)
    model = get_peft_model(base, cfg)
    return model


def run_one(ds, subset_fn, ordinal, shot, seed, tag, epochs=30, lr=1e-3, batch=16, size=224,
            rank=8, alpha=16):
    cfg = {"exp": "E1lora", "dataset": ds, "view": tag, "encoder": "dinov2_s_lora", "variant": "pixel",
           "head": "lora", "shot": shot, "seed": seed, "C": None, "control": "none",
           "epochs": epochs, "lr": lr, "rank": rank, "alpha": alpha}
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
    model = build_lora(len(labels), rank, alpha).to(dev)
    trainable = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.AdamW(trainable, lr=lr, weight_decay=0.0)
    lossf = nn.CrossEntropyLoss()
    dl = DataLoader(FT.ImgSet([str(PROC / p) for p in tr["path"]], list(tr["label_name"]), lab2i, True, size),
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
    dle = DataLoader(FT.ImgSet([str(PROC / p) for p in te["path"]], list(te["label_name"]), lab2i, False, size),
                     batch_size=64, shuffle=False, num_workers=4)
    preds = []
    with torch.no_grad():
        for xb, _ in dle:
            preds.append(model(xb.to(dev)).argmax(1).cpu().numpy())
    pred = np.concatenate(preds)
    pred_lab = np.array([labels[i] for i in pred])
    met = closed_set_metrics(te["label_name"].values, pred_lab, labels)
    n_trainable = sum(p.numel() for p in trainable)
    n_total = sum(p.numel() for p in model.parameters())
    met.update({"n_support": int(len(tr)), "support_per_class": per,
                "support_ids_sha256": sha256_ids(tr["id"].values),
                "test_ids_sha256": sha256_ids(te["id"].values), "n_test": int(len(te)),
                "n_trainable_params": int(n_trainable), "n_total_params": int(n_total),
                "note": LORA_NOTE % (rank, alpha)})
    del model
    torch.cuda.empty_cache()
    rec = {"config": cfg, "metrics": met, "code_version": CODE_VERSION,
           "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "extra": {}}
    atomic_write_json(result_path(cfg), rec)
    return rec


def main():
    import run as R
    ap = argparse.ArgumentParser()
    ap.add_argument("--views", default="banana3,fruit12_banana,fruit12_apple,banana4,fruit12_mango,field4_banana,field4_mango")
    ap.add_argument("--shots", default="1,5,10,50")
    ap.add_argument("--seeds", default="0,1,2")
    ap.add_argument("--epochs", type=int, default=30)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--rank", type=int, default=8)
    ap.add_argument("--alpha", type=int, default=16)
    a = ap.parse_args()
    V = R.views()
    shots = [int(s) for s in a.shots.split(",")]
    seeds = [int(s) for s in a.seeds.split(",")]
    todo = [(v, V[v], sh, s) for v in a.views.split(",") if v in V for sh in shots for s in seeds]
    log("=== lora runs=%d r=%d alpha=%d epochs=%d lr=%g ===" % (len(todo), a.rank, a.alpha, a.epochs, a.lr))
    for i, (name, v, sh, s) in enumerate(todo):
        try:
            r = run_one(v["ds"], v["subset"], v["ordinal"], sh, s, name,
                        epochs=a.epochs, lr=a.lr, rank=a.rank, alpha=a.alpha)
            if r:
                log("[E1lora] %s shot=%d seed=%d acc=%.3f f1=%.3f"
                    % (name, sh, s, r["metrics"]["acc"], r["metrics"]["macro_f1"]))
        except Exception as e:
            import traceback
            log("[E1lora] FAIL %s shot=%d seed=%d: %s\n%s" % (name, sh, s, e, traceback.format_exc()[-500:]))
        if (i + 1) % 10 == 0:
            log("[E1lora] %d/%d" % (i + 1, len(todo)))
    log("=== lora done ===")


if __name__ == "__main__":
    main()
