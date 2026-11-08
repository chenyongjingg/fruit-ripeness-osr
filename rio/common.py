"""Shared paths, IO, hashing, logging."""
import os, json, hashlib, time, sys, tempfile
from pathlib import Path

# The repository root is this file's grandparent, so a clone runs where it sits.
# `RIO_ROOT` overrides it (e.g. when results live on a bigger disk than the code).
ROOT = Path(os.environ.get("RIO_ROOT", Path(__file__).resolve().parent.parent))
DATA = ROOT / "data"
RAW = DATA / "raw"
PROC = DATA / "processed"
CACHE = ROOT / "cache"
FEAT = CACHE / "features"
RESULTS = ROOT / "results"
OUT = ROOT / "outputs"
LOGS = ROOT / "logs"
CONF = ROOT / "configs"
for p in (DATA, RAW, PROC, CACHE, FEAT, RESULTS, OUT, LOGS, CONF):
    p.mkdir(parents=True, exist_ok=True)

CODE_VERSION = "rio-1.0.0"

# Plan v2.0 fix #3: the `P2c_*` arm holds out a whole SPECIES of fruit12, not a
# cultivar -- "Apple" vs "Banana" differ in colour, shape and texture, so an AUROC
# there measures species separability and cannot support a cultivar-level claim.
# The internal view key is kept (renaming it would change every config hash and
# silently create a second arm), but every table, figure and report line must use
# the honest name. Applied at load time so no grouping key changes.
VIEW_ALIASES = {"P2c_unseen_cultivar": "P2c_unseen_species"}
# The same run is named by both its `view` key ("fruit12_x_apple") and its `protocol`
# key ("P2c_unseen_cultivar"). Fix #3 has to reach both, or the honest name appears in
# one column and the false one beside it in the next.
PROTOCOL_ALIASES = {"P2c_unseen_cultivar": "P2c_unseen_species"}


def display_view(v):
    return VIEW_ALIASES.get(str(v), v)


def display_protocol(p):
    return PROTOCOL_ALIASES.get(str(p), p)


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def log(msg, fname="pipeline.log"):
    line = f"[{now()}] {msg}"
    print(line, flush=True)
    with open(LOGS / fname, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def atomic_write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, path)


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def sha256_file(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_ids(ids):
    return sha256_text("\n".join(sorted(str(i) for i in ids)))


def marker(stage):
    return ROOT / "cache" / f".done_{stage}"


def set_done(stage, payload=None):
    atomic_write_json(marker(stage), {"stage": stage, "at": now(), "payload": payload or {}})


def is_done(stage):
    return marker(stage).exists()


def heartbeat(stage, extra=None):
    atomic_write_json(ROOT / "cache" / ".heartbeat.json",
                      {"stage": stage, "at": now(), "extra": extra or {}})


def disk_free_gb(path="/"):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize / 1e9
