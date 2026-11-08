#!/usr/bin/env python3
"""Ensure every raw dataset archive and every Qwen2-VL shard is on disk, byte-exact.

Why a size check and not just "the file exists": an interrupted `curl -C -` against a
mirror that ignores Range appends a whole 200 response onto the partial file, which
makes the file *bigger* than Content-Length and the zip unreadable while still looking
like a finished download. Every artefact here is therefore accepted only when its size
equals the size the server reports.
"""
import json, os, subprocess, sys, time
from pathlib import Path

_REPO = Path(__file__).resolve().parent
RAW = Path(os.environ.get("RIO_ROOT", _REPO)) / "data" / "raw"
QWEN = Path(os.environ.get("RIO_ROOT", _REPO)) / "models" / "Qwen2-VL-7B-Instruct"
QFILES = ["config.json", "generation_config.json", "preprocessor_config.json",
          "chat_template.json", "merges.txt", "vocab.json", "tokenizer.json",
          "tokenizer_config.json", "special_tokens_map.json",
          "model.safetensors.index.json"] + ["model-%05d-of-00005.safetensors" % i for i in range(1, 6)]

DATASETS = {
    "banana4/data.zip": "https://hf-mirror.com/datasets/Sapek007/banana-ripeness/resolve/main/banana_ripeness_dataset.zip",
    "fruit12/data.zip": "https://hf-mirror.com/datasets/Carlosmg23/fruit-ripeness-12clases/resolve/main/fruit-ripeness-12clases.zip",
}
# Last-resort fallbacks if the server does not answer HEAD: known-good sizes measured once.
KNOWN = {"banana4/data.zip": 234641843, "fruit12/data.zip": 377524652}
QWEN_BASE = "https://modelscope.cn/models/Qwen/Qwen2-VL-7B-Instruct/resolve/master/"


def log(m):
    print("[ensure %s] %s" % (time.strftime("%H:%M:%S"), m), flush=True)


def head_size(url):
    try:
        out = subprocess.run(["curl", "-sIL", "--max-time", "60", url],
                             capture_output=True, text=True).stdout
        sizes = [int(l.split(":")[1].strip()) for l in out.splitlines()
                 if l.lower().startswith("content-length:")]
        return sizes[-1] if sizes else None
    except Exception:
        return None


def fetch(url, dst, expect):
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_suffix(dst.suffix + ".part")
    for k in range(1, 11):
        if tmp.exists():
            tmp.unlink()
        log("GET %s (try %d)" % (dst.name, k))
        subprocess.run(["curl", "-sSL", "--speed-limit", "30000", "--speed-time", "60",
                        "-o", str(tmp), url])
        size = tmp.stat().st_size if tmp.exists() else 0
        if expect is None or size == expect:
            os.replace(tmp, dst)
            log("OK %s %d" % (dst.name, size))
            return True
        log("size %d != %s, retrying" % (size, expect))
        time.sleep(5)
    return False


def ensure_dataset(rel):
    dst = RAW / rel
    url = DATASETS[rel]
    if dst.exists():
        sz = dst.stat().st_size
        exp = head_size(url) or KNOWN.get(rel)
        if exp is None or sz == exp:
            return True
        log("%s size %d != expected %s" % (rel, sz, exp))
        dst.unlink()
    exp = head_size(url) or KNOWN.get(rel)
    return fetch(url, dst, exp)


def safetensors_ok(path):
    """A safetensors file is complete iff file_size == 8 + header_len + max(end offset).

    This is a local, definitive check: a truncated download has a valid header but a
    short data section, and no size-from-the-server query is needed to catch it.
    """
    import struct
    try:
        n = os.path.getsize(path)
        with open(path, "rb") as f:
            h = struct.unpack("<Q", f.read(8))[0]
            if h <= 0 or h > 200 * 1024 * 1024 or 8 + h > n:
                return False
            meta = json.loads(f.read(h))
        end = 0
        for k, v in meta.items():
            if k == "__metadata__":
                continue
            a, b = v["data_offsets"]
            end = max(end, b)
        return n == 8 + h + end
    except Exception:
        return False


def qwen_sizes():
    out = {}
    for f in QFILES:
        u = QWEN_BASE + f
        out[f] = head_size(u)
    return out


def qwen_ready():
    """True only when every shard exists with exactly the size the server reports."""
    for f in QFILES:
        p = QWEN / f
        if not p.exists() or p.stat().st_size == 0:
            return False
        if f.endswith(".safetensors") and not safetensors_ok(p):
            return False
    return True


def ensure_qwen():
    if qwen_ready():
        return True
    sizes = qwen_sizes()
    log("qwen remote sizes known for %d/%d files" % (sum(v is not None for v in sizes.values()), len(sizes)))
    for f in QFILES:
        p = QWEN / f
        if p.exists() and p.stat().st_size > 0:
            if not f.endswith(".safetensors") or safetensors_ok(p):
                continue
            log("%s exists but is incomplete (%d B) -> re-fetching" % (f, p.stat().st_size))
            p.unlink()
        exp = sizes.get(f)
        if not fetch(QWEN_BASE + f, p, exp):
            log("FAILED %s" % f)
            return False
        if f.endswith(".safetensors") and not safetensors_ok(p):
            log("%s still incomplete after fetch" % f)
            return False
    return qwen_ready()


def main():
    only = "--datasets-only" in sys.argv
    ok = True
    for rel in DATASETS:
        ok &= ensure_dataset(rel)
    if not only:
        ok &= ensure_qwen()
    log("all data/models ready" if ok else "SOMETHING IS NOT READY")


if __name__ == "__main__":
    main()
