"""Survey the local-header stream of the (still growing) NinePeach archive:
prefix histogram + annotation schema."""
import sys, re, collections
sys.path.insert(0, '/root/rio')
from probe_zip_head import walk
import xml.etree.ElementTree as ET

path = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 400

f = open(path, 'rb')
import struct, zlib
prefix = collections.Counter()
names = collections.Counter()
folders = collections.Counter()
keys = collections.Counter()
samples = []
i = 0
while i < n:
    sig = f.read(4)
    if sig != b'PK\x03\x04':
        print('STOP at member %d: %r' % (i, sig)); break
    hdr = f.read(26)
    (_v, flag, method, _t, _d, _crc, csize, usize, nlen, elen) = struct.unpack('<HHHHHIIIHH', hdr)
    name = f.read(nlen).decode('utf-8', 'replace'); f.read(elen)
    data = b''
    if flag & 8:
        d = zlib.decompressobj(-15 if method == 8 else 15); out = []
        while not d.eof:
            buf = f.read(65536)
            if not buf: break
            out.append(d.decompress(buf))
            if d.unconsumed_tail: f.seek(-len(d.unconsumed_tail), 1)
        data = b''.join(out)
        if f.read(4) != b'PK\x07\x08': f.read(8)
    else:
        data = f.read(csize)
        if method == 8: data = zlib.decompress(data, -15)
    parts = name.split('/')
    prefix['/'.join(parts[:2]) if len(parts) > 1 else '(root)'] += 1
    if name.endswith('.xml'):
        try:
            r = ET.fromstring(data)
        except Exception as e:
            print('BAD XML', name, e); i += 1; continue
        fold = r.findtext('folder'); folder = r.findtext('path')
        folders[(fold, (folder or '').rsplit(chr(92), 1)[0])] += 1
        for o in r.iter('object'):
            names[o.findtext('name')] += 1
        for ch in r:
            keys[ch.tag] += 1
        if len(samples) < 3:
            samples.append((name, fold, folder, [o.findtext('name') for o in r.iter('object')]))
    i += 1
print('members scanned:', i)
print('prefix:', dict(prefix))
print('annotation <folder>/<path dir>:')
for k, v in folders.most_common(10): print('   ', k, v)
print('object names:', dict(names))
print('annotation tags:', dict(keys))
for s in samples: print('sample:', s)
