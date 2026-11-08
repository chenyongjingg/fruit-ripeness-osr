#!/bin/bash
# Fresh (non-resumed) download + byte-exact size check. Absolute paths only.
set -u
URL="https://hf-mirror.com/datasets/Sapek007/banana-ripeness/resolve/main/banana_ripeness_dataset.zip"
EXP=234641843
R="$(cd "$(dirname "$0")" && pwd)"
OUT="$R/data/raw/banana4/data.zip"
mkdir -p "$R/data/raw/banana4"
cd "$R/data/raw/banana4" || exit 1
rm -f data.zip data.zip.part
for i in $(seq 1 40); do
  curl -sSL --speed-limit 30000 --speed-time 60 -o data.zip.part "$URL"
  SZ=$(stat -c%s data.zip.part 2>/dev/null || echo 0)
  echo "$(date -Is) try=$i size=$SZ"
  if [ "$SZ" = "$EXP" ]; then mv data.zip.part data.zip; echo "SIZE_OK $SZ"; break; fi
  rm -f data.zip.part; sleep 5
done
python3 - <<'PY'
import zipfile
z=zipfile.ZipFile('data.zip')
imgs=[n for n in z.namelist() if n.lower().endswith(('.jpg','.png'))]
bad=0
for n in imgs: 
    try: z.read(n)
    except Exception: bad+=1
print('members',len(z.namelist()),'imgs',len(imgs),'bad',bad)
PY
echo BANANA4_DONE
