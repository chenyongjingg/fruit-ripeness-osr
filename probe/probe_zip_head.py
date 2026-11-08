"""Scan the LOCAL FILE HEADERS of a ZIP that is still being appended to.

The central directory lives at the end of the archive and is not there yet, so
zipfile cannot open it. This walks the local headers from byte 0 instead and
prints the first N members; --dump pulls the content of one member.
"""
import struct, sys, zlib

def walk(path, limit=40, want=None):
    f = open(path, 'rb')
    out = []
    while len(out) < limit:
        sig = f.read(4)
        if sig != b'PK\x03\x04':
            out.append(('STOP', repr(sig), f.tell() - 4))
            break
        hdr = f.read(26)
        if len(hdr) < 26:
            break
        (_ver, flag, method, _t, _d, _crc, csize, usize, nlen, elen) = struct.unpack('<HHHHHIIIHH', hdr)
        name = f.read(nlen).decode('utf-8', 'replace')
        f.read(elen)
        data = b''
        if flag & 8:                       # sizes follow the data in a descriptor
            d = zlib.decompressobj(-15 if method == 8 else 15)
            chunks = []
            while not d.eof:
                buf = f.read(65536)
                if not buf:
                    break
                chunks.append(d.decompress(buf))
                rest = d.unconsumed_tail
                if rest:
                    # push the remainder back by seeking: the compressor stopped mid-buffer
                    f.seek(-len(rest), 1)
            data = b''.join(chunks)
            dsz = f.read(4)
            if dsz == b'PK\x07\x08':
                f.read(12)
            else:
                f.read(8)
            csize = usize = -1
        else:
            data = f.read(csize)
            if method == 8:
                data = zlib.decompress(data, -15)
        out.append((name, usize if usize >= 0 else len(data), method))
        if want and name.endswith(want):
            return out, data
    return out, None

if __name__ == '__main__':
    path, limit = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 40
    want = sys.argv[3] if len(sys.argv) > 3 else None
    rows, data = walk(path, limit, want)
    for n, s, m in rows:
        print('%10s  m=%s  %s' % (s, m, n))
    if data is not None:
        open('/tmp/sample.xml', 'wb').write(data)
        print('---- /tmp/sample.xml %d bytes ----' % len(data))
        print(data.decode('utf-8', 'replace')[:3000])
