"""Print the measured fingerprint of one dataset, straight from its card.json.

Usage: python3 cards.py <dataset>            e.g. python3 cards.py raspgrade
"""
import json, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
ds = sys.argv[1] if len(sys.argv) > 1 else "raspgrade"
c = json.load(open(REPO / "data" / "processed" / ds / "card.json"))
print(ds, {k: c.get(k) for k in ('n_images', 'n_groups', 'class_counts', 'split_counts',
                                 'n_source_images', 'dropped_small_polygons', 'unit',
                                 'group_leak_count')})
