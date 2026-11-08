"""Run the RaspGrade arms (E1 closed-set + E2 open-set) ahead of the master loop.

Idempotent: every cell is keyed on its config hash, so a later master cycle that
reaches the same cell is a no-op. Kept as a separate script so the master driver
can run it too without any change.
"""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rio.common import log
import run

V = run.views()
VR = {k: v for k, v in V.items() if k == 'raspgrade'}
if not VR:
    log('[rasp] raspgrade not prepared')
    sys.exit(0)

t = time.time()
run.stage_e1(VR, ['dinov2_s', 'dinov2_b', 'clip_b', 'resnet50'],
             [1, 5, 10, 50, None], [0, 1, 2, 3, 4], ['linear', 'proto'], ['cls'])
log('[rasp] e1 done in %.0fs' % (time.time() - t))

t = time.time()
run.stage_e2(VR, ['dinov2_s', 'resnet50'], [None, 5], [0, 1, 2],
             ['msp', 'energy', 'mahalanobis', 'knn'], ['cls'])
log('[rasp] e2 done in %.0fs' % (time.time() - t))
log('[rasp] finished')
