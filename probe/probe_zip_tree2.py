import sys, struct, zlib, collections
path = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 2500
f = open(path, 'rb'); i = 0
top = collections.Counter(); sub = collections.defaultdict(collections.Counter)
firsts = collections.defaultdict(list)
while i < n:
    sig = f.read(4)
    if sig != b'PK\x03\x04':
        print('STOP at member %d (bytes read %d)' % (i, f.tell())); break
    hdr = f.read(26)
    (_v, flag, method, _t, _d, _crc, csize, usize, nlen, elen) = struct.unpack('<HHHHHIIIHH', hdr)
    name = f.read(nlen).decode('utf-8', 'replace'); f.read(elen)
    p = name.split('/')
    if len(p) >= 2:
        top[p[1]] += 1
        if len(p) >= 3:
            sub[p[1]][p[2] if len(p) > 3 else '(file)'] += 1
        if len(firsts[p[1]]) < 3: firsts[p[1]].append(name)
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
print('members:', i)
for k, v in top.most_common():
    print('%-40s %d' % (k, v))
    print('    first:', firsts[k][:2])
    for kk, vv in sub[k].most_common(12):
        print('      %-36s %d' % (kk, vv))
