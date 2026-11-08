import glob, json, collections
import numpy as np

frozen = collections.defaultdict(list)
ft = collections.defaultdict(list)
for f in glob.glob('/root/rio/results/E1__*.json') + glob.glob('/root/rio/results/E1ft__*.json'):
    d = json.load(open(f))
    c = d['config']
    if c.get('control') not in (None, 'none'):
        continue
    acc = d['metrics'].get('acc')
    if acc is None:
        continue
    if c['exp'] == 'E1' and c.get('encoder') == 'dinov2_s' and c.get('head') == 'linear' \
            and c.get('variant') == 'cls':
        frozen[(c['view'], c['shot'])].append(acc)
    elif c['exp'] == 'E1ft':
        ft[(c['view'], c['shot'])].append(acc)

print('view        shot  frozen_ds   FT_resnet50  gap_pp')
for k in sorted(set(frozen) & set(ft), key=lambda x: (x[0], -1 if x[1] is None else x[1])):
    a, b = np.mean(frozen[k]), np.mean(ft[k])
    print('%-12s %-5s %.3f       %.3f       %+.1f' % (k[0], k[1], a, b, (a - b) * 100))
