#!/bin/bash
# Own loop for the Qwen weights: never blocks the science stages.
cd "$(cd "$(dirname "$0")" && pwd)" || exit 1
for i in $(seq 1 12); do
  python3 - <<'PY'
import ensure_data as E
print("ready:", E.qwen_ready(), flush=True)
if not E.qwen_ready():
    E.ensure_qwen()
PY
  python3 -c "import ensure_data as E,sys; sys.exit(0 if E.qwen_ready() else 1)" && { echo QWEN_READY; break; }
  sleep 30
done
