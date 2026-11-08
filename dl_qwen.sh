#!/bin/bash
# Download Qwen2-VL-7B-Instruct from ModelScope (resumable per shard).
set -u
BASE="https://modelscope.cn/models/Qwen/Qwen2-VL-7B-Instruct/resolve/master"
OUT="/root/rio/models/Qwen2-VL-7B-Instruct"
mkdir -p "$OUT"
FILES="config.json generation_config.json preprocessor_config.json chat_template.json merges.txt vocab.json tokenizer.json tokenizer_config.json special_tokens_map.json model.safetensors.index.json model-00001-of-00005.safetensors model-00002-of-00005.safetensors model-00003-of-00005.safetensors model-00004-of-00005.safetensors model-00005-of-00005.safetensors"
for f in $FILES; do
  for i in $(seq 1 30); do
    curl -sSL --retry 3 -C - --speed-limit 50000 --speed-time 30 -o "$OUT/$f" "$BASE/$f" && break
    sleep 3
  done
  echo "got $f $(stat -c%s "$OUT/$f" 2>/dev/null)"
done
echo QWEN_DONE
