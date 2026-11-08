import sys, os, io, zipfile
sys.path.insert(0, "/root/rio")
import rio.data as D
from PIL import Image
from collections import Counter

idx = D.ninepeach_index()
zf = zipfile.ZipFile(idx["zip"])
sizes = Counter()
odd = []
for a in idx["anns"]:
    base = os.path.basename(a["filename"]).lower()
    cand = idx["by_base"].get(base) or []
    if not cand:
        odd.append((a["xml"], a["filename"], None, "no image"))
        continue
    ci = sorted(cand, key=lambda i: i.filename)[0]
    with zf.open(ci.filename) as fh:
        data = fh.read()
    im = Image.open(io.BytesIO(data))
    sizes[im.size] += 1
    if im.size != (a["W"], a["H"]):
        odd.append((a["xml"], ci.filename, im.size, (a["W"], a["H"])))
print("decoded:", sum(sizes.values()))
print("image sizes:", sizes.most_common(10))
print("xml-vs-image mismatches:", len(odd))
for o in odd[:15]:
    print(o)
