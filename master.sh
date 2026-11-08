#!/bin/bash
# Unattended master driver. Every stage is idempotent (results keyed by config hash),
# so killing and restarting this script at any point resumes where it stopped.
cd /root/rio || exit 1
export HF_ENDPOINT=https://hf-mirror.com
export TOKENIZERS_PARALLELISM=false
export OMP_NUM_THREADS=8
export PYTHONUNBUFFERED=1
CYCLE=0
while true; do
  CYCLE=$((CYCLE+1))
  echo "=== cycle $CYCLE $(date -Is) ===" >> logs/master.log
  [ -f STOP ] && { echo "STOP file present" >> logs/master.log; break; }

  FREE=$(df --output=avail -BG / | tail -1 | tr -dc '0-9')
  echo "disk_free_gb=$FREE" >> logs/master.log
  if [ "${FREE:-0}" -lt 5 ]; then echo "LOW DISK" >> logs/master.log; sleep 600; continue; fi

  # ---- 0. data / model availability (idempotent; each has its own size check)
  python3 ensure_data.py --datasets-only >> logs/ensure.log 2>&1

  # ---- 1. decode datasets
  python3 run.py --stage prepare >> logs/sup_prepare.log 2>&1

  # ---- 2. frozen features
  python3 run.py --stage extract --encoders dinov2_s,dinov2_b,clip_b,resnet50 >> logs/sup_extract.log 2>&1

  # ---- 3. science
  python3 run.py --stage e1 --shot 1,5,10,50,all --seeds 0,1,2,3,4 >> logs/sup_e1.log 2>&1
  python3 run.py --stage e2 >> logs/sup_e2.log 2>&1
  python3 run.py --stage e3 --seeds 0,1,2 >> logs/sup_e3.log 2>&1
  python3 run.py --stage control --seeds 0,1,2 >> logs/sup_control.log 2>&1

  # ---- 4. baselines (CLIP always; Qwen only when all shards are on disk)
  python3 run_baselines.py --which clip >> logs/sup_clip.log 2>&1
  if python3 -c "import sys;sys.exit(0 if __import__('ensure_data').qwen_ready() else 1)" 2>/dev/null; then
    python3 run_baselines.py --which qwen --qwen-max-n 120 >> logs/sup_qwen.log 2>&1
  fi

  # ---- 5. aggregation
  python3 report.py >> logs/sup_report.log 2>&1

  python3 - <<'PY' > outputs/status.json
import json,glob,collections,time,os
c=collections.Counter(os.path.basename(f).split('__')[0] for f in glob.glob('/root/rio/results/*.json'))
print(json.dumps({"at":time.strftime("%Y-%m-%dT%H:%M:%S"),"runs":dict(c),"n":sum(c.values())},indent=1))
PY
  sleep 900
done
