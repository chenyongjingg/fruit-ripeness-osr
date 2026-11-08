import glob, os, time, collections

for exp in ('E1ap', 'E1ord', 'E2', 'E1'):
    h = collections.Counter()
    n = 0
    for f in glob.glob('/root/rio/results/%s__*.json' % exp):
        n += 1
        h[time.strftime('%H:%M', time.localtime(os.path.getmtime(f)))[:4] + '0'] += 1
    print(exp, n, dict(sorted(h.items())))
