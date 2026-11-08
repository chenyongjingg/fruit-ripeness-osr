#!/bin/bash
R="$(cd "$(dirname "$0")" && pwd)"; cd "$R/data/raw" || exit 1
get(){ url="$1"; out="$2"; want="$3"
  for i in $(seq 1 20); do
    rm -f "$out"
    curl -sSL --retry 2 --speed-limit 50000 --speed-time 40 -o "$out" "$url"
    sz=$(stat -c%s "$out" 2>/dev/null || echo 0)
    if [ "$sz" = "$want" ]; then echo "OK $out $sz"; return 0; fi
    echo "retry $i size=$sz want=$want"
  done
  echo "FAIL $out"; return 1; }
get "https://hf-mirror.com/datasets/Carlosmg23/fruit-ripeness-12clases/resolve/main/fruit-ripeness-12clases.zip" fruit12/data.zip 377524652
get "https://hf-mirror.com/datasets/Sapek007/banana-ripeness/resolve/main/banana_ripeness_dataset.zip" banana4/data.zip 234641843
echo DL3_DONE
