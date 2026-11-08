#!/usr/bin/env python3
"""Drive the two zero-shot baselines (CLIP, Qwen2-VL) over every fruit view.

Idempotent: every (view, shot) config is cached as a results JSON keyed by its
config hash, so re-running after an interruption resumes where it stopped.
"""
import argparse, sys, time, traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import log, read_json
import run as R
import baselines as B

QWEN_DIR = str(Path(__file__).resolve().parent / "models" / "Qwen2-VL-7B-Instruct")


def fruit_of(view, v):
    """Human-readable fruit name for the prompt."""
    n = (view.replace("mango_khir", "mango").replace("fruits360_", "")
             .replace("fruit12_", "").replace("field4_", "")
             .replace("banana3", "banana").replace("banana4", "banana"))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--which", default="clip,qwen")
    ap.add_argument("--views", default="")
    ap.add_argument("--qwen-max-n", type=int, default=120)
    ap.add_argument("--clip-max-n", type=int, default=400)
    ap.add_argument("--qwen-shots", default="0,5")
    ap.add_argument("--quant", default="4bit")
    a = ap.parse_args()
    V = R.views()
    want = [w for w in a.views.split(",") if w] or list(V.keys())
    shots = [int(x) for x in a.qwen_shots.split(",") if x]
    log("=== baselines which=%s views=%d ===" % (a.which, len(want)))
    nfail = 0
    for view in want:
        v = V.get(view)
        if v is None:
            continue
        if not v.get("baseline", True):
            log("[baselines] skip %s (view marks itself baseline=False)" % view)
            continue
        ds, ordn = v["ds"], v["ordinal"]
        fruit = fruit_of(view, v)
        if "clip" in a.which:
            try:
                r = B.clip_zeroshot(ds, view, fruit, ordn, max_n=a.clip_max_n)
                log("[clip] %-16s acc=%.3f f1=%.3f" % (view, r["metrics"]["acc"], r["metrics"]["macro_f1"]))
            except Exception as e:
                log("[clip] FAIL %s: %s\n%s" % (view, e, traceback.format_exc()[-500:]))
        if "qwen" in a.which:
            for sh in shots:
                try:
                    t = time.time()
                    r = B.qwen_eval(ds, view, fruit, ordn, shot=sh, model_dir=QWEN_DIR,
                                    quant=a.quant, max_n=a.qwen_max_n)
                    log("[qwen] %-16s shot=%d acc=%.3f f1=%.3f unparsed=%.3f (%.0fs)"
                        % (view, sh, r["metrics"]["acc"], r["metrics"]["macro_f1"],
                           r["metrics"].get("unparsed_rate", -1), time.time() - t))
                    nfail = 0
                except Exception as e:
                    import torch, gc
                    nfail += 1
                    log("[qwen] FAIL %s shot=%d: %s\n%s" % (view, sh, e, traceback.format_exc()[-600:]))
                    gc.collect()
                    try:
                        torch.cuda.empty_cache()
                    except Exception:
                        pass
                    if nfail >= 2:   # repeated hard failure (OOM): stop, retry next cycle
                        return
    log("=== baselines done ===")


if __name__ == "__main__":
    main()
