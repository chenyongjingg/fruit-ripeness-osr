"""Headline numbers for the status report, correct config keys."""
import glob, json, collections
import numpy as np

by = collections.defaultdict(list)
for f in glob.glob('/root/rio/results/*.json'):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    by[d.get('config', {}).get('exp')].append((d.get('config') or {}, d.get('metrics') or {}))


def mean(exp, pred, fld='acc'):
    r = collections.defaultdict(list)
    for cfg, m in by.get(exp, []):
        if pred(cfg) and m.get(fld) is not None:
            r[(cfg.get('view'), cfg.get('encoder'), cfg.get('head'), cfg.get('shot'))].append(float(m[fld]))
    return r


print('=== E1 linear (variant=cls, control=none) ===')
r = mean('E1', lambda c: c.get('head') == 'linear' and c.get('variant') == 'cls'
         and c.get('control') == 'none')
for view in sorted({k[0] for k in r}):
    parts = []
    for enc in ('dinov2_s', 'dinov2_b', 'clip_b', 'resnet50'):
        for shot in (1, 5, None):
            v = r.get((view, enc, 'linear', shot))
            if v:
                parts.append('%s/%s=%.3f' % (enc.replace('dinov2_', 'd'), 'full' if shot is None else shot,
                                            np.mean(v)))
    print('%-15s %s' % (view, ' '.join(parts)))

print('\n=== E1 proto (variant=cls, control=none) ===')
r = mean('E1', lambda c: c.get('head') == 'proto' and c.get('variant') == 'cls'
         and c.get('control') == 'none')
for view in sorted({k[0] for k in r}):
    v = r.get((view, 'dinov2_b', 'proto', None))
    v5 = r.get((view, 'dinov2_b', 'proto', 5))
    if v or v5:
        print('%-15s dinov2_b 5=%s full=%s' % (view,
              '%.3f' % np.mean(v5) if v5 else '-', '%.3f' % np.mean(v) if v else '-'))

print('\n=== E1ft (resnet50_ft end-to-end) ===')
r = mean('E1ft', lambda c: True)
for view in sorted({k[0] for k in r}):
    parts = []
    for shot in (1, 5, None):
        v = [x for k, x in r.items() if k[0] == view and k[3] == shot]
        if v:
            parts.append('%s=%.3f(n=%d)' % ('full' if shot is None else shot, np.mean(v),
                                            sum(len(x) for k, x in r.items() if k[0] == view and k[3] == shot)))
    print('%-15s %s' % (view, ' '.join(parts)))

print('\n=== E1lora (dinov2_s + LoRA) ===')
r = mean('E1lora', lambda c: True)
for view in sorted({k[0] for k in r}):
    parts = []
    for shot in (1, 5, None):
        v = [x for k, x in r.items() if k[0] == view and k[3] == shot]
        if v:
            parts.append('%s=%.3f' % ('full' if shot is None else shot, np.mean(v)))
    print('%-15s %s' % (view, ' '.join(parts)))

print('\n=== E3 cross-domain acc ===')
r = mean('E3', lambda c: True)
for k in sorted({(a, b, c) for a, b, c, d in r}):
    parts = []
    for shot in (1, 5, None):
        v = r.get((k[0], k[1], k[2], shot))
        if v:
            parts.append('%s=%.3f' % ('full' if shot is None else shot, np.mean(v)))
    print('%-14s %-9s align=%-4s %s' % (k[0], k[1], k[2], ' '.join(parts)))

print('\n=== E1ap long-tail (per-class AP) ===')
ks = collections.Counter()
for cfg, m in by.get('E1ap', []):
    ks.update(m.keys())
print('metric keys:', dict(ks))

print('\n=== VLM baselines ===')
for exp in ('B1_clip_zeroshot', 'B2_qwen_zeroshot', 'B2_qwen_5shot'):
    r = mean(exp, lambda c: True)
    for k in sorted(r, key=lambda x: str(x[0])):
        print('%-18s %-15s %.3f (n=%d runs)' % (exp, k[0], np.mean(r[k]), len(r[k])))
