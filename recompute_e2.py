#!/usr/bin/env python3
"""Recompute E2 metrics from the stored score arrays after a metric-definition fix.

The stored scores are untouched: this re-derives only the summary statistics, so the
numbers stay tied to the same experiment run (no re-training, no re-sampling).
"""
import sys, numpy as np
from pathlib import Path
sys.path.insert(0, "/root/rio")
from rio.common import RESULTS, atomic_write_json, read_json
from rio.methods import open_set_metrics

n = 0
for j in sorted(RESULTS.glob("E2__*.json")):
    f = RESULTS / "scores" / (j.stem.split("__")[-1] + ".npz")
    if not f.exists():
        continue
    rec = read_json(j)
    with np.load(f, allow_pickle=True) as z:     # close: 1900 open fds exhaust the limit
        ks, us = np.array(z["known_scores"]), np.array(z["unknown_scores"])
        kc = (z["known_pred"] == z["known_labels"]) if "known_pred" in z else None
        if kc is not None:
            kc = np.array(kc)
    met = open_set_metrics(ks, us, known_correct=kc)
    for k in ("auroc", "fpr95", "tpr_at_fpr95", "oscr", "ccr_at_fpr5"):
        old = rec["metrics"].get(k)
        if old is None or abs(float(old) - met[k]) > 1e-12:
            rec["metrics"][k] = met[k]
            n += 1
    rec["metrics"]["oscr_definition"] = "CCR counts only correctly classified accepted knowns"
    atomic_write_json(j, rec)
print("updated fields:", n)
