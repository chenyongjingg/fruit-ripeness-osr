#!/bin/bash
# LoRA driver, kept in its own process on purpose.
#
# master2.sh is currently RUNNING and a bash process reads its script lazily, so
# rewriting master2.sh in place is not safe. Instead the LoRA stage lives here and
# waits until the Qwen baseline has released the GPU (Qwen keeps ~20 GB of the
# 24 GB card; running LoRA at the same time produced CUDA OOM warnings).
#
# Every run is keyed by its config hash, so this loop is idempotent: it finishes
# the arm once and then just idles, picking up nothing on later passes.
cd /root/rio || exit 1
export HF_ENDPOINT=https://hf-mirror.com
export OMP_NUM_THREADS=8
export PYTHONUNBUFFERED=1
while true; do
  if pgrep -f "run_baselines.py --which qwe[n]" >/dev/null; then
    sleep 120; continue
  fi
  echo "=== lora pass $(date -Is) ===" >> logs/sup_lora.log
  python3 run_lora.py --shots 1,5,10,50 --seeds 0,1,2 >> logs/sup_lora.log 2>&1
  python3 report.py >> logs/sup_report.log 2>&1
  sleep 3600
done
