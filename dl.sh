#!/bin/bash
set -u
R="$(cd "$(dirname "$0")" && pwd)"
cd "$R/data/raw" 2>/dev/null || { mkdir -p "$R/data/raw"; cd "$R/data/raw"; }
mkdir -p banana3 banana4 fruit12 field4
dl(){ url="$1"; out="$2"; for i in 1 2 3 4 5 6; do curl -sSL --retry 3 -C - -o "$out" "$url" && return 0; sleep 5; done; return 1; }
dl "https://hf-mirror.com/datasets/TCleo/3-banana-maturity/resolve/main/data/train-00000-of-00001-a4ba92e8901684d5.parquet" banana3/data.parquet &
dl "https://hf-mirror.com/datasets/Sapek007/banana-ripeness/resolve/main/banana_ripeness_dataset.zip" banana4/data.zip &
dl "https://hf-mirror.com/datasets/Carlosmg23/fruit-ripeness-12clases/resolve/main/fruit-ripeness-12clases.zip" fruit12/data.zip &
dl "https://hf-mirror.com/datasets/darthraider/fruit-ripeness-detection-dataset/resolve/main/data/train-00000-of-00001.parquet" field4/train.parquet &
dl "https://hf-mirror.com/datasets/darthraider/fruit-ripeness-detection-dataset/resolve/main/data/test-00000-of-00001.parquet" field4/test.parquet &
wait
echo DONE
ls -lR "$R/data/raw" | head -40
