#!/bin/bash
# Unattended master driver. Every stage is idempotent (results keyed by config hash),
# so killing and restarting this script at any point resumes where it stopped.
#
# v2 adds a per-stage wall-clock guard. Nothing else in this container will notice a
# hung process: there is no cron, no systemd, no supervisor entry for /root/rio, and the
# author is away. A single stuck Qwen generation would otherwise stall the driver
# forever and the next REPORT.md would never be written. `timeout` turns a hang into a
# logged non-zero return code, and the loop moves on; the next cycle retries the stage.
cd /root/rio || exit 1
export HF_ENDPOINT=https://hf-mirror.com
export TOKENIZERS_PARALLELISM=false
export OMP_NUM_THREADS=8
export PYTHONUNBUFFERED=1
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

guard() {                      # guard <name> <seconds> <command...>
  local name=$1 tmo=$2; shift 2
  timeout --signal=TERM "$tmo" "$@"
  local rc=$?
  if [ $rc -ne 0 ]; then
    echo "[$name] rc=$rc (124 = timed out after ${tmo}s) $(date -Is)" >> logs/master.log
  fi
}

CYCLE=0
while true; do
  CYCLE=$((CYCLE+1))
  echo "=== cycle $CYCLE $(date -Is) ===" >> logs/master.log
  [ -f STOP ] && { echo "STOP file present" >> logs/master.log; break; }

  FREE=$(df --output=avail -BG / | tail -1 | tr -dc '0-9')
  echo "disk_free_gb=$FREE" >> logs/master.log
  if [ "${FREE:-0}" -lt 5 ]; then echo "LOW DISK" >> logs/master.log; sleep 600; continue; fi

  # ---- 0. data / model availability (idempotent; each has its own size check)
  guard ensure 3600 python3 ensure_data.py --datasets-only >> logs/ensure.log 2>&1

  # ---- 1. decode datasets
  guard prepare 3600 python3 run.py --stage prepare >> logs/sup_prepare.log 2>&1

  # ---- 2. frozen features
  guard extract 7200 python3 run.py --stage extract --encoders dinov2_s,dinov2_b,clip_b,resnet50 >> logs/sup_extract.log 2>&1

  # ---- 3. science
  guard e1 10800 python3 run.py --stage e1 --shot 1,5,10,50,all --seeds 0,1,2,3,4 >> logs/sup_e1.log 2>&1
  # dual-path ablation: the plan stores both the CLS token and the patch mean; only the
  # CLS route was evaluated until now. 3 seeds is enough for an ablation arm.
  guard e1mean 10800 python3 run.py --stage e1 --variants mean --encoders dinov2_s,dinov2_b,clip_b \
      --shot 1,5,10,50,all --seeds 0,1,2 >> logs/sup_e1mean.log 2>&1
  # per-class AP (the plan closed-set metric that needs probabilities, so it lives in
  # its own experiment key E1ap; idempotent like everything else)
  # E4 ordinal ablation: CORN head fitted on the same support as the linear head.
  guard corn 10800 python3 run.py --stage e1 --heads corn --shot 1,5,10,50,all --seeds 0,1,2,3,4 >> logs/sup_corn.log 2>&1
  guard ap 10800 python3 ap_extra.py >> logs/sup_ap.log 2>&1
  # plan 5.3 weighted macro-F1 (adjacent 1 / skipped 2) + E4 CORN vs linear pairs
  guard ord 10800 python3 ord_extra.py --heads linear,proto,corn >> logs/sup_ord.log 2>&1
  guard e2 18000 python3 run.py --stage e2 >> logs/sup_e2.log 2>&1
  # calibration arm: same grid, per-class thresholds fitted on val (see experiments.e2)
  guard e2calib 18000 python3 run.py --stage e2 --calib >> logs/sup_e2cal.log 2>&1
  guard e3 10800 python3 run.py --stage e3 --seeds 0,1,2 >> logs/sup_e3.log 2>&1
  # RQ3 tier (c): feature-level alignment (target-domain train statistics, no labels)
  guard e3bn 10800 python3 run.py --stage e3 --align bn --seeds 0,1,2 >> logs/sup_e3bn.log 2>&1
  guard control 7200 python3 run.py --stage control --seeds 0,1,2 >> logs/sup_control.log 2>&1

  # ---- 3b. end-to-end fine-tuned ResNet-50 arm (the plan's "full fine-tuning" baseline)
  guard finetune 10800 python3 run_finetune.py --views banana3,banana4,fruit12_banana,fruit12_apple --shots 1,5,10,50 --seeds 0,1,2 >> logs/sup_ft.log 2>&1

  # ---- 4. baselines (CLIP always; Qwen only when all shards are on disk)
  guard clip 3600 python3 run_baselines.py --which clip >> logs/sup_clip.log 2>&1
  # one process per view: a single long-lived process accumulated ~19 GB and OOM'd on
  # the 4th view, even though the model itself is only ~5 GB at INT4
  if python3 -c "import sys;sys.exit(0 if __import__('ensure_data').qwen_ready() else 1)" 2>/dev/null; then
    for QV in banana3 banana4 fruit12_apple fruit12_banana fruit12_mango field4_banana field4_mango; do
      guard "qwen_$QV" 3600 python3 run_baselines.py --which qwen --views "$QV" --qwen-max-n 120 --quant 4bit >> logs/sup_qwen.log 2>&1
    done
  fi

  # ---- 4b. LoRA arm (the plan's third RQ1 adaptation method). Runs AFTER Qwen on
  #         purpose: Qwen holds ~20 GB of the 24 GB card and a concurrent LoRA run
  #         produced CUDA OOM warnings in the smoke test.
  guard lora 10800 python3 run_lora.py --shots 1,5,10,50 --seeds 0,1,2 >> logs/sup_lora.log 2>&1

  # ---- 4c. efficiency measurements (plan's E5 / Tab. 6). Cheap, runs last so it never
  #         competes with the VLM baselines for the card.
  guard efficiency 3600 python3 efficiency.py >> logs/sup_eff.log 2>&1

  # ---- 4d. extra figures (plan Fig. 4 / Fig. 5). Cheap, never fatal.
  guard figures 3600 python3 fig_extra.py >> logs/sup_fig.log 2>&1

  # ---- 5. aggregation
  guard selftest 600 python3 test_methods.py >> logs/sup_selftest.log 2>&1
  # data seal (plan fix #10): every result must record the data it ran on. Incremental
  # after the first pass -- it only examines results written since the marker, so in a
  # steady-state cycle it costs one `stat` of the results directory.
  guard seal 1800 python3 seal.py >> logs/sup_seal.log 2>&1
  guard report 3600 python3 report.py >> logs/sup_report.log 2>&1
  # the plan-v2 analysis layer (T11..T16): family flip by hidden level, adjacent-grade
  # direction, collapsed/thin cells, bootstrap CIs. Reads stored score arrays only.
  # plan v2.0 week 1 asks for "--bootstrap 1000"; the driver used to call analyze with no
  # resampling and every cycle overwrote the bootstrapped table with the plain one.
  guard analyze 1800 python3 analyze_v2.py --bootstrap 1000 >> logs/sup_analyze.log 2>&1
  # the plan's week-3 figures (four-arm bars + family-flip interaction). They read the
  # T11/T12 CSVs, so they must run after analyze; fig_extra (above) draws the older set.
  guard figv2 900 python3 fig_v2.py >> logs/sup_figv2.log 2>&1
  # independent re-derivation of AUROC / FPR@95 / known accuracy from the score arrays
  # (report.verify re-uses the production metric code, so it cannot catch a wrong
  # definition; this one implements the metrics a second time and exits non-zero on a
  # disagreement)
  guard verify_indep 3600 python3 verify_indep.py >> logs/sup_verify_indep.log 2>&1
  # the checklist: prints PASS/FAIL per item, exits non-zero if any item fails
  guard final_check 3600 python3 final_check.py >> logs/sup_final.log 2>&1

  python3 - <<'PY' > outputs/status.json
import json,glob,collections,time,os
c=collections.Counter(os.path.basename(f).split('__')[0] for f in glob.glob('/root/rio/results/*.json'))
print(json.dumps({"at":time.strftime("%Y-%m-%dT%H:%M:%S"),"runs":dict(c),"n":sum(c.values())},indent=1))
PY
  sleep 900
done
