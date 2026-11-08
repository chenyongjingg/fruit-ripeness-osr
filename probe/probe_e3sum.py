import glob, json, collections
import numpy as np

rows = collections.defaultdict(list)
pairs = collections.Counter()
for f in glob.glob('/root/rio/results/E3__*.json'):
    d = json.load(open(f))
    c, m = d['config'], d['metrics']
    pairs[(c['view'], m.get('source'), m.get('target'))] += 1
    rows[(c['view'], c.get('align', 'none'), c['encoder'], c['shot'])].append(m['acc'])

print('--- view -> source/target ---')
for k, v in sorted(pairs.items()):
    print(k, v)
print('--- acc by view/align (all encoders x seeds) ---')
for k in sorted({(a, b) for a, b, c, d in rows}):
    vs = [x for kk, vv in rows.items() if kk[0] == k[0] and kk[1] == k[1] for x in vv]
    print('%-14s %-6s n=%3d mean=%.3f min=%.3f max=%.3f'
          % (k[0], k[1], len(vs), np.mean(vs), min(vs), max(vs)))
print('--- same view, dinov2_b, shot=5, per encoder ---')
for k in sorted(rows):
    if k[1] == 'linear' and k[3] == 5:
        print('%-14s %-9s %.3f' % (k[0], k[2], np.mean(rows[k])))
