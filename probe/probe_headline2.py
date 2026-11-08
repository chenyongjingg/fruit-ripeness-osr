"""Headline numbers for the status report: closed-set, cross-domain, efficiency.

Reads only /root/rio/results/*.json. Prints compact tables.
"""
import glob, json, collections
import numpy as np

by = collections.defaultdict(list)
for f in glob.glob('/root/rio/results/*.json'):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    cfg = d.get('config') or {}
    m = d.get('metrics') or {}
    by[cfg.get('exp')].append((cfg, m))

print('--- run counts by exp ---')
for k in sorted(by, key=lambda x: str(x)):
    print('%-10s %d' % (k, len(by[k])))


def agg(exp, filt, field):
    rows = collections.defaultdict(list)
    for cfg, m in by.get(exp, []):
        if not filt(cfg):
            continue
        v = m.get(field)
        if v is None:
            continue
        rows[(cfg.get('view'), cfg.get('encoder'), cfg.get('head'), cfg.get('shot'))].append(float(v))
    return rows


print('\n--- E1 closed-set acc (linear head, variant=cls, no control) ---')
rows = agg('E1', lambda c: c.get('variant') in (None, 'cls') and not c.get('control')
           and c.get('head') == 'linear', 'acc')
views = sorted({k[0] for k in rows})
for view in views:
    parts = []
    for enc in ('dinov2_s', 'dinov2_b', 'clip_b', 'resnet50'):
        for shot in (5, None):
            v = rows.get((view, enc, 'linear', shot))
            if v:
                parts.append('%s@%s=%.3f' % (enc, 'full' if shot is None else shot, np.mean(v)))
    if parts:
        print('%-16s %s' % (view, '  '.join(parts)))

print('\n--- E1ft / E1lora acc (resnet50) ---')
for exp in ('E1ft', 'E1lora'):
    rows = agg(exp, lambda c: not c.get('control'), 'acc')
    views = sorted({k[0] for k in rows})
    for view in views:
        parts = []
        for shot in (1, 5, None):
            v = [np.mean(x) for k, x in rows.items() if k[0] == view and k[3] == shot]
            if v:
                parts.append('%s=%.3f' % ('full' if shot is None else shot, float(np.mean(v))))
        if parts:
            print('%-6s %-16s %s' % (exp, view, '  '.join(parts)))

print('\n--- E3 cross-domain (all metric keys, mean) ---')
if by.get('E3'):
    keys = collections.Counter()
    for cfg, m in by['E3']:
        keys.update(m.keys())
    print('metric keys:', dict(keys))
    rows = collections.defaultdict(list)
    for cfg, m in by['E3']:
        for fld in ('auroc', 'acc', 'acc_src', 'acc_tgt'):
            if fld in m:
                rows[(cfg.get('view'), cfg.get('encoder'), cfg.get('align'), fld,
                      cfg.get('shot'))].append(float(m[fld]))
    for k in sorted(rows, key=lambda x: tuple(str(i) for i in x)):
        if k[3] == 'auroc':
            print('%-16s %-9s align=%-5s shot=%-5s AUROC %.3f (n=%d)'
                  % (k[0], k[1], k[2], k[4], np.mean(rows[k]), len(rows[k])))
