import glob, json, collections
import numpy as np
agg = collections.defaultdict(list)
for f in glob.glob('/root/rio/results/*.json'):
    d = json.load(open(f))
    c = d.get('config') or {}
    if c.get('exp') != 'E2':
        continue
    p = c.get('protocol')
    if p not in ('P2_unseen_interior', 'P1_out_of_grade', 'P3_rotten', 'P3_foreign', 'P2c_unseen_cultivar'):
        continue
    a = (d.get('metrics') or {}).get('auroc')
    if a is None or not np.isfinite(a):
        continue
    agg[(p, c.get('score'))].append(float(a))
for k in sorted(agg):
    v = np.array(agg[k])
    print('%-22s %-12s n=%4d mean=%.4f sd=%.4f' % (k[0], k[1], len(v), v.mean(), v.std()))
