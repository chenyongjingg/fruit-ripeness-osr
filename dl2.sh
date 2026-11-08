#!/bin/bash
cd /root/rio/data/raw || exit 1
dl(){ url="$1"; out="$2"; want="$3";
  for i in $(seq 1 40); do
    sz=$(stat -c%s "$out" 2>/dev/null || echo 0)
    if [ "$sz" -ge "$want" ]; then echo "OK $out $sz"; return 0; fi
    curl -sSL --retry 2 --retry-delay 3 -C - --speed-limit 20000 --speed-time 30 -o "$out" "$url" && echo "curl done $out"
    sleep 2
  done
  echo "GAVEUP $out"; return 1; }
dl "https://hf-mirror.com/datasets/Sapek007/banana-ripeness/resolve/main/banana_ripeness_dataset.zip" banana4/data.zip 234641843 &
dl "https://hf-mirror.com/datasets/Carlosmg23/fruit-ripeness-12clases/resolve/main/fruit-ripeness-12clases.zip" fruit12/data.zip 377524652 &
dl "https://hf-mirror.com/datasets/darthraider/fruit-ripeness-detection-dataset/resolve/main/data/train-00000-of-00001.parquet" field4/train.parquet 347126000 &
wait
echo ALLDONE
python3 - <<'PY'
import zipfile
for p in ['banana4/data.zip','fruit12/data.zip']:
    try:
        z=zipfile.ZipFile(p); print(p,'ZIP_OK',len(z.namelist()))
    except Exception as e: print(p,'ZIP_BAD',e)
PY
