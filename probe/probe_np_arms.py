import glob, json, collections
import numpy as np
agg = collections.defaultdict(list)
for f in glob.glob('/root/rio/results/E2__*.json'):
    d = json.load(open(f))
    cfg = d.get('config') or {}
    if cfg.get('exp') != 'E2' or cfg.get('calib'):
        continue
    if cfg.get('view') not in ('ninepeach', 'raspgrade'):
        continue
    m = d.get('metrics') or {}
    a = m.get('auroc')
    if a is None or not np.isfinite(a):
        continue
    agg[(cfg['view'], cfg.get('protocol'), str(cfg.get('unknown')),
         'dist' if cfg.get('score') in ('mahalanobis', 'knn') else 'prob')].append(float(a))
for k in sorted(agg):
    v = np.array(agg[k])
    print('%-10s %-20s %-14s %-5s n=%3d mean=%.4f sd=%.4f min=%.4f max=%.4f'
          % (k[0], k[1], k[2], k[3], len(v), v.mean(), v.std(ddof=1) if len(v) > 1 else 0,
             v.min(), v.max()))
