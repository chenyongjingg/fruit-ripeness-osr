import glob, json, collections, sys
fs = sorted(glob.glob('/root/rio/results/E2__raspgrade__*.json'))
groups = collections.defaultdict(list)
for f in fs:
    d = json.load(open(f))
    c = d['config']
    k = (str(c.get('protocol')), str(c.get('encoder')), str(c.get('shot')),
         str(c.get('unknown')), str(c.get('score')))
    groups[k].append((f, c, d.get('finished_at')))
print('files', len(fs), 'groups', len(groups))
k = sorted(groups)[0]
print('group', k)
for f, c, fa in groups[k]:
    print(f, fa)
    print('   ', json.dumps(c, sort_keys=True))
# which config keys vary inside any group
varying = collections.Counter()
mult = 0
for k, lst in groups.items():
    if len(lst) < 2:
        continue
    mult += 1
    keys = set()
    for _, c, _ in lst:
        keys |= set(c)
    for kk in keys:
        vals = {json.dumps(c.get(kk), sort_keys=True) for _, c, _ in lst}
        if len(vals) > 1:
            varying[kk] += 1
print('multi-file groups', mult)
print('varying keys', varying)
