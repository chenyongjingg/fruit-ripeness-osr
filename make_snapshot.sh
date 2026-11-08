#!/bin/bash
# Build the "code + results + docs" snapshot. Deliberately excludes
# data/raw, data/processed/*/images, cache/features and models/ (public
# downloads and recomputable features). Run only after the driver has exited.
set -e
cd /root/rio
OUT=/root/rio_snapshot_20261108.tgz
rm -f "$OUT"
find data/processed -maxdepth 2 -type f \( -name card.json -o -name meta.csv \) > /tmp/snap_extra.txt
echo "extra data files: $(wc -l < /tmp/snap_extra.txt)"
tar czf "$OUT" \
    --exclude='__pycache__' --exclude='*.pyc' \
    --transform 's,^,rio/,' \
    *.py *.sh *.md rio results outputs logs -T /tmp/snap_extra.txt
sha256sum "$OUT" > /root/rio_snapshot_20261108.sha256
cat /root/rio_snapshot_20261108.sha256
ls -l --block-size=K "$OUT"
echo "members: $(tar tzf "$OUT" | wc -l)"
echo "results json: $(tar tzf "$OUT" | grep -c '^rio/results/.*\.json$')"
echo "score files: $(tar tzf "$OUT" | grep -c '^rio/results/scores/')"
echo "no images/datasets: $(tar tzf "$OUT" | grep -cE 'images/|\.npy$|\.npz$|data/raw|models/' || true)"
