import sys, glob, os, random
from PIL import Image
import numpy as np

for ds in sys.argv[1:]:
    files = sorted(glob.glob('/root/rio/data/processed/%s/images/*.jpg' % ds))
    if not files:
        print(ds, 'no images'); continue
    random.Random(0).shuffle(files)
    ws, hs = [], []
    for f in files[:400]:
        with Image.open(f) as im:
            ws.append(im.size[0]); hs.append(im.size[1])
    ws = np.array(ws); hs = np.array(hs)
    side = np.minimum(ws, hs)
    print('%-10s n_files=%d sampled=%d  min-side px: p5=%d p50=%d p95=%d  max=%d'
          % (ds, len(files), len(ws), np.percentile(side, 5), np.percentile(side, 50),
             np.percentile(side, 95), side.max()))
