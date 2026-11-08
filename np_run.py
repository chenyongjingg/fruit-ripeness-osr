"""Run the NinePeach arms end to end, in the same order the master driver uses.

Called once the archive is complete and its md5 matches the figshare record (`np_verify.py`
checks both and writes outputs/NINEPEACH_VERIFY.md). Every stage is idempotent (results are
keyed on the config hash), so re-running this after the master loop already covered a cell
is a no-op.

Usage: python3 np_run.py [all|build|extract|e1|e2|e2x]
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import log
from rio import data as D
import run

STEP = sys.argv[1] if len(sys.argv) > 1 else 'all'

if STEP in ('all', 'build'):
    t = time.time()
    card = D.build_ninepeach()
    log('[np] build done in %.0fs: items=%s photos=%s splits=%s classes=%s leak=%s'
        % (time.time() - t, card.get("n_images"), card.get("n_source_images_annotated"),
           card.get("split_counts"), card.get("class_counts"), card.get("group_leak_count")))

if STEP in ('all', 'extract'):
    t = time.time()
    run.stage_extract(['dinov2_s', 'dinov2_b', 'clip_b', 'resnet50'], ['ninepeach'], 224)
    log('[np] extract done in %.0fs' % (time.time() - t))

V = run.views()
VNP = {k: v for k, v in V.items() if k == 'ninepeach'}
if not VNP and STEP != 'build':
    log('[np] ninepeach is not a view yet (no card.json) -> nothing to score')
    sys.exit(0)

if STEP in ('all', 'e1'):
    t = time.time()
    run.stage_e1(VNP, ['dinov2_s', 'dinov2_b', 'clip_b', 'resnet50'],
                 [1, 5, 10, 50, None], [0, 1, 2, 3, 4], ['linear', 'proto'], ['cls'])
    log('[np] e1 done in %.0fs' % (time.time() - t))

if STEP in ('all', 'e2'):
    t = time.time()
    run.stage_e2(VNP, ['dinov2_s', 'resnet50'], [None, 5], [0, 1, 2],
                 ['msp', 'energy', 'mahalanobis', 'knn'], ['cls'])
    log('[np] e2 done in %.0fs' % (time.time() - t))

if STEP in ('all', 'e2x'):
    t = time.time()
    run.stage_e2x(VNP, ['dinov2_s', 'resnet50'], [0, 1, 2])
    log('[np] e2x done in %.0fs' % (time.time() - t))

log('[np] step %s finished' % STEP)
