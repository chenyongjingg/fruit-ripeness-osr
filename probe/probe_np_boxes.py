import sys, os
sys.path.insert(0, "/root/rio")
import rio.data as D

idx = D.ninepeach_index()
bad = []
for a in idx["anns"]:
    W, H = a["W"], a["H"]
    for nm, (x0, y0, x1, y1) in a["objects"]:
        if x1 <= x0 or y1 <= y0:
            bad.append((a["xml"], a["filename"], W, H, nm, (x0, y0, x1, y1), "degenerate"))
            continue
        w, h = x1 - x0, y1 - y0
        m = 0.10 * max(w, h)
        cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
        half = max(w, h) / 2.0 + m
        lo_y, hi_y = max(0, cy - half), min(H, cy + half)
        lo_x, hi_x = max(0, cx - half), min(W, cx + half)
        if int(lo_y) >= int(hi_y) or int(lo_x) >= int(hi_x):
            bad.append((a["xml"], a["filename"], W, H, nm, (x0, y0, x1, y1),
                        "clamped %s" % (int(lo_x), int(lo_y), int(hi_x), int(hi_y))))
print("annotations:", len(idx["anns"]), "boxes:", sum(len(a["objects"]) for a in idx["anns"]))
print("bad:", len(bad))
for b in bad[:20]:
    print(b)
# also: do the XML <size> values agree with anything? print the range of W/H
from collections import Counter
print("xml sizes:", Counter((a["W"], a["H"]) for a in idx["anns"]).most_common(5))
mx = max((max(o[1][2] for o in a["objects"]), a["W"]) for a in idx["anns"] if a["objects"])
print("max x1 vs W (worst):", mx)
my = max((max(o[1][3] for o in a["objects"]), a["H"]) for a in idx["anns"] if a["objects"])
print("max y1 vs H (worst):", my)
