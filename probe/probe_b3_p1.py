import glob, json, collections
import numpy as np
agg = collections.defaultdict(list)
for f in glob.glob('/root/rio/results/E2__*.json'):
    d = json.load(open(f))
    cfg = d.get('config') or {}
    if cfg.get('exp') != 'E2' or cfg.get('calib'):
        continue
    if cfg.get('view') != 'banana3' or cfg.get('protocol') != 'P1_out_of_grade':
        continue
    a = (d.get('metrics') or {}).get('auroc')
    if a is None or not np.isfinite(a):
        continue
    agg[cfg.get('score')].append(float(a))
for k in sorted(agg):
    v = np.array(agg[k])
    print('%-12s n=%2d mean=%.4f  vals=%s' % (k, len(v), v.mean(),
                                               ' '.join('%.3f' % x for x in sorted(v))))
