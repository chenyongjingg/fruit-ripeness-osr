import csv, re
import numpy as np

rows = list(csv.DictReader(open('/root/rio/outputs/T10_calibration.csv')))


def num(s):
    m = re.match(r'^\s*(-?[0-9.]+)', s or '')
    return float(m.group(1)) if m else None


A = [(num(r['auroc']), num(r['ccr_fpr5_before']), num(r['ccr_cal']), num(r['fpr_cal']),
      num(r['ccr_accept_all'])) for r in rows]
A = [a for a in A if None not in a]
print('rows', len(rows), 'parseable', len(A))
auroc = np.array([a[0] for a in A])
fprc = np.array([a[3] for a in A])
ccr0 = np.array([a[1] for a in A])
ccrc = np.array([a[2] for a in A])
print('corr(auroc, fpr_cal) = %.3f' % np.corrcoef(auroc, fprc)[0, 1])
print('corr(auroc, ccr_fpr5_before) = %.3f' % np.corrcoef(auroc, ccr0)[0, 1])
print('mean ccr@fpr5 before = %.3f' % ccr0.mean())
print('mean ccr_cal = %.3f, mean fpr_cal = %.3f' % (ccrc.mean(), fprc.mean()))
print('median fpr_cal = %.3f' % np.median(fprc))
print('rows with fpr_cal > 0.20: %d/%d' % ((fprc > 0.20).sum(), len(A)))
print('rows with auroc < 0.5: %d; their mean ccr_cal %.3f, mean fpr_cal %.3f'
      % ((auroc < 0.5).sum(), ccrc[auroc < 0.5].mean(), fprc[auroc < 0.5].mean()))
print('rows with auroc >= 0.8: %d; their mean ccr_cal %.3f, mean fpr_cal %.3f'
      % ((auroc >= 0.8).sum(), ccrc[auroc >= 0.8].mean(), fprc[auroc >= 0.8].mean()))
