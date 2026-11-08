import glob, json, collections
c = collections.Counter()
nu = collections.Counter()
for f in glob.glob('/root/rio/results/E2__*.json'):
    d = json.load(open(f))
    cfg = d.get('config') or {}
    if cfg.get('exp') != 'E2' or cfg.get('calib'):
        continue
    if cfg.get('view') != 'raspgrade':
        continue
    m = d.get('metrics') or {}
    key = (cfg.get('protocol'), str(cfg.get('unknown')), cfg.get('shot'))
    c[key] += 1
    nu[key] = m.get('n_unknown')
for k in sorted(c, key=str):
    print(k, 'runs=%d' % c[k], 'n_unknown=%s' % nu[k])
