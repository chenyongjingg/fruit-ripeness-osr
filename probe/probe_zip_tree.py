"""Print the directory tree implied by the local headers of the partial archive."""
import sys, struct, zlib, collections
path = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
f = open(path, 'rb'); i = 0
pref = collections.Counter(); ex = collections.defaultdict(list)
while i < n:
    sig = f.read(4)
    if sig != b'PK\x03\x04':
        print('STOP at member %d: %r' % (i, sig)); break
    hdr = f.read(26)
    (_v, flag, method, _t, _d, _crc, csize, usize, nlen, elen) = struct.unpack('<HHHHHIIIHH', hdr)
    name = f.read(nlen).decode('utf-8', 'replace'); f.read(elen)
    parts = name.split('/')
    key = '/'.join(parts[:3]) if len(parts) > 3 else name
    pref[key] += 1
    if len(ex[key]) < 3: ex[key].append(name)
    # skip the payload
    if flag & 8:
        d = zlib.decompressobj(-15 if method == 8 else 15)
        while not d.eof:
            buf = f.read(65536)
            if not buf: break
            d.decompress(buf)
            if d.unconsumed_tail: f.seek(-len(d.unconsumed_tail), 1)
        if f.read(4) != b'PK\x07\x08': f.read(8)
    else:
        f.seek(csize, 1)
    i += 1
for k, v in sorted(pref.items(), key=lambda kv: -kv[1])[:40]:
    print('%6d  %s' % (v, k))
    for e in ex[k][:2]: print('          e.g. %s' % e)
