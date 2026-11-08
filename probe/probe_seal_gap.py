import glob, json, os, time, collections

now = time.time()
no_seal = collections.Counter()
by_age = collections.Counter()
tot = 0
youngest = None
for f in glob.glob('/root/rio/results/*.json'):
    tot += 1
    try:
        r = json.load(open(f))
    except Exception:
        no_seal['UNREADABLE'] += 1
        continue
    if not r.get('seal'):
        exp = os.path.basename(f).split('__')[0]
        age_min = (now - os.path.getmtime(f)) / 60.0
        no_seal[exp] += 1
        bucket = '<10min' if age_min < 10 else ('10-30min' if age_min < 30 else '>30min')
        by_age[bucket] += 1
        if youngest is None or age_min < youngest[0]:
            youngest = (age_min, os.path.basename(f))
print('total files', tot)
print('files without seal by exp:', dict(no_seal))
print('by age:', dict(by_age))
print('youngest unsealed:', youngest)
