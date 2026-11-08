# Independent metric re-derivation

AUROC (rank form, no sklearn), FPR@95 (threshold sweep), known accuracy and
array sizes, recomputed from `results/scores/*.npz` and compared with the stored
values. OSCR is definition-sensitive (discrete ROC); only its deviation under a
right-continuous step rule is reported.

checked: 3264 arrays, unresolved: 0, violations: 0
worst |diff|: auroc 2.22e-16 (003ee4248e1f608d.npz), fpr95 0.00e+00 (), known_acc 0.00e+00 (), oscr-step 6.63e-06 (2379c46b27afc9b5.npz)
