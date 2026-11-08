#!/usr/bin/env python3
"""E5: efficiency measurements that the plan's Tab. 6 needs.

What is measured, and what is deliberately NOT claimed:
  * parameter count of each frozen encoder (the whole network, not just the head);
  * single-image inference latency at batch 1 (median of N timed passes after warm-up);
  * peak GPU memory of one batch-32 forward pass;
  * trainable parameters of each adaptation head, counted from the cached features
    (linear probe) or from the recorded E1lora runs (LoRA), not estimated by hand.

Latency here is the *encoder* cost on this card, timed with cuda synchronisation. It is
a relative comparison, not a deployment number: it excludes image decoding and I/O.
"""
import json, time, sys
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import OUT, RESULTS, log, atomic_write_json

ENCODERS = [("dinov2_s", "vit_small_patch14_dinov2.lvd142m"),
            ("dinov2_b", "vit_base_patch14_dinov2.lvd142m"),
            ("clip_b", "vit_base_patch16_clip_224.openai"),
            ("resnet50", "resnet50.a1_in1k")]


def build(timm_id, size=224):
    """ResNet has no img_size kwarg; ViTs do. Ask for it only where it exists."""
    import timm
    try:
        return timm.create_model(timm_id, pretrained=True, num_classes=0, img_size=size)
    except TypeError:
        return timm.create_model(timm_id, pretrained=True, num_classes=0)


def warm_gpu(seconds=2.0):
    """Raise the GPU clock before the first measurement.

    The first encoder measured was consistently reported SLOWER than the larger second
    one (dinov2_s 6.17 ms vs dinov2_b 4.87 ms), which is the opposite of the FLOP
    ordering: the card was still at idle clocks when the first model ran. A short
    sustained load before timing, plus discarding a first timing pass, removes that.
    """
    import torch, time
    if not torch.cuda.is_available():
        return
    a = torch.randn(1024, 1024, device="cuda")
    t0 = time.time()
    while time.time() - t0 < seconds:
        for _ in range(20):
            a = a @ a * 1e-4
    torch.cuda.synchronize()


def measure(timm_id, size=224, iters=20, batch=32):
    import torch
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    m = build(timm_id, size).to(dev).eval()
    p = sum(q.numel() for q in m.parameters())
    with torch.no_grad():
        for _ in range(10):                                   # warm-up (cuDNN autotune)
            m(torch.zeros(1, 3, size, size, device=dev))
        if dev == "cuda":
            torch.cuda.synchronize()
        ts = []
        for _ in range(iters):
            x = torch.zeros(1, 3, size, size, device=dev)
            if dev == "cuda":
                torch.cuda.synchronize()
            t0 = time.perf_counter()
            m(x)
            if dev == "cuda":
                torch.cuda.synchronize()
            ts.append((time.perf_counter() - t0) * 1000.0)
        lat = float(np.median(ts))
        if dev == "cuda":
            torch.cuda.reset_peak_memory_stats()
        xb = torch.zeros(batch, 3, size, size, device=dev)
        m(xb)
        peak = float(torch.cuda.max_memory_allocated() / 2 ** 20) if dev == "cuda" else float("nan")
    del m
    if dev == "cuda":
        torch.cuda.empty_cache()
    return p, lat, peak


def train_mem_probe(gpu):
    """Peak GPU memory of one TRAINING step for the two GPU-trained arms.

    The plan's E5 asks for `training peak GPU memory`, while `measure()` above reports
    the peak of a batch-32 *forward* pass. For the frozen-feature pipeline the training
    memory is the cached feature matrix (no GPU training at all), so the only arms where
    a training figure exists are the two end-to-end ones. Both are trained at batch 16 in
    this repo (run_finetune / run_lora), so the probe uses batch 16 -- reporting a
    batch-32 number under a "training" label would be a different measurement wearing the
    same name.

    Two steps are run and the peak is reset before the first: the first step pays for
    lazy CUDA allocations and would otherwise be reported as the model's cost.
    """
    import torch
    rows = []
    if not torch.cuda.is_available():
        return rows
    size, batch, n_cls = 224, 16, 3

    def one(name, model):
        try:
            model = model.to("cuda").train()
            opt = torch.optim.AdamW([q for q in model.parameters() if q.requires_grad], lr=1e-3)
            x = torch.randn(batch, 3, size, size, device="cuda")
            y = torch.randint(0, n_cls, (batch,), device="cuda")
            torch.cuda.synchronize()
            torch.cuda.reset_peak_memory_stats()
            for _ in range(2):
                opt.zero_grad()
                loss = torch.nn.functional.cross_entropy(model(x), y)
                loss.backward()
                opt.step()
            torch.cuda.synchronize()
            peak = float(torch.cuda.max_memory_allocated() / 2 ** 20)
            rows.append({"kind": "train_mem", "name": name, "timm_id": "", "params": np.nan,
                         "latency_ms_b1": np.nan, "peak_mem_mb_b32": round(peak, 1),
                         "gpu": gpu, "note": "one training step, batch %d (repo default)" % batch})
            log("[E5] train_mem %-18s %.0f MB" % (name, peak))
        except Exception as e:
            log("[E5] train_mem FAIL %s: %s" % (name, e))
        finally:
            try:
                del model
            except Exception:
                pass
            torch.cuda.empty_cache()

    try:
        import timm
        one("finetune_resnet50", timm.create_model("resnet50.a1_in1k", pretrained=True,
                                                   num_classes=n_cls))
    except Exception as e:
        log("[E5] train_mem build failed for resnet50: %s" % e)
    try:
        import run_lora
        one("lora_dinov2_s", run_lora.build_lora(n_cls, 8, 16))
    except Exception as e:
        log("[E5] train_mem build failed for lora: %s" % e)
    return rows


def head_params():
    """Trainable parameters for the two frozen-feature heads, and for LoRA."""
    rows = []
    # linear probe: d x C weights + C biases, taken from the actual feature cache
    for f in sorted(Path(OUT.parent / "cache" / "features").glob("*__dinov2_s.npz")):
        z = np.load(f, allow_pickle=True)
        d = int(z["cls"].shape[1])
        rows.append(("linear_probe", "dinov2_s", d * 3 + 3))
        break
    rows.append(("prototype", "dinov2_s", 0))       # non-parametric: class means are the model
    # LoRA: read from a finished run rather than assuming 8 * 384 * 2 per block
    for f in sorted(RESULTS.glob("E1lora__*.json")):
        r = json.load(open(f))
        met = r["metrics"]
        if "n_trainable_params" in met:
            rows.append(("lora_r8", r["config"]["encoder"], met["n_trainable_params"]))
            break
    for f in sorted(RESULTS.glob("E1ft__*.json")):
        r = json.load(open(f))
        if "n_trainable_params" in r["metrics"]:
            rows.append(("finetune", r["config"]["encoder"], r["metrics"]["n_trainable_params"]))
            break
    return rows


def main():
    try:
        import torch
        gpu = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"
    except Exception:
        gpu = "unknown"
    rows = []
    warm_gpu(2.0)
    # Two passes; the second is what gets reported. The first pass is the one that pays
    # for lazy kernel autotuning and clock ramp, and it was biasing the FIRST encoder
    # measured in every run.
    res = {}
    for rnd in (1, 2):
        for key, tid in ENCODERS:
            try:
                res[key] = (tid,) + measure(tid)
            except Exception as e:
                if rnd == 2:
                    log("[E5] FAIL %s: %s" % (key, e))
    for key, tid in ENCODERS:
        if key not in res:
            continue
        _, p, lat, peak = res[key]
        rows.append({"kind": "encoder", "name": key, "timm_id": tid, "params": p,
                     "latency_ms_b1": round(lat, 2), "peak_mem_mb_b32": round(peak, 1),
                     "gpu": gpu})
        log("[E5] %-10s params=%.2fM latency=%.2fms peak32=%.0fMB" % (key, p / 1e6, lat, peak))
    for kind, name, p in head_params():
        rows.append({"kind": "head", "name": kind, "timm_id": "", "params": int(p),
                     "latency_ms_b1": np.nan, "peak_mem_mb_b32": np.nan, "gpu": gpu})
    # the plan's E5 list has THREE quantities: latency, trainable params, and training
    # peak memory. The last one only exists for the two end-to-end arms.
    for r in train_mem_probe(gpu):
        rows.append(r)
    # full fine-tuning of ResNet-50 trains every parameter; E1ft results predate the
    # n_trainable_params field, so take it from the measured model rather than guessing
    if "resnet50" in res:
        rows.append({"kind": "head", "name": "finetune_resnet50", "timm_id": "", "params": int(res["resnet50"][1]),
                     "latency_ms_b1": np.nan, "peak_mem_mb_b32": np.nan, "gpu": gpu})
    df = pd.DataFrame(rows)
    out = OUT / "T9_efficiency.csv"
    df.to_csv(out, index=False)
    try:
        (OUT / "T9_efficiency.md").write_text(df.to_markdown(index=False), encoding="utf-8")
    except Exception:
        pass
    log("[E5] wrote %s (%d rows)" % (out, len(df)))


if __name__ == "__main__":
    main()
