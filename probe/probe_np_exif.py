import sys, os, io, zipfile
sys.path.insert(0, "/root/rio")
import rio.data as D
from PIL import Image, ImageOps
from collections import Counter

idx = D.ninepeach_index()
zf = zipfile.ZipFile(idx["zip"])
orient = Counter()
fixed = Counter()
n = 0
for a in idx["anns"]:
    base = os.path.basename(a["filename"]).lower()
    ci = sorted(idx["by_base"].get(base) or [], key=lambda i: i.filename)
    if not ci:
        continue
    with zf.open(ci[0].filename) as fh:
        im = Image.open(io.BytesIO(fh.read()))
    ex = im.getexif()
    o = int(ex.get(274, -1))
    orient[o] += 1
    im2 = ImageOps.exif_transpose(im)
    fixed[(im.size, im2.size)] += 1
    n += 1
print("n:", n)
print("EXIF orientation:", orient.most_common())
print("(raw size -> exif_transpose size):", fixed.most_common())
# split folders
sp = Counter()
for i in idx["images"]:
    sp[D._split_of(i.filename)] += 1
print("split folders:", sp)
