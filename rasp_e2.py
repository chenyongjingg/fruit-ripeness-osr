"""Count the RaspGrade open-set cells that exist and show a few of them."""
import json, glob, os, collections
REPO = os.path.dirname(os.path.abspath(__file__))
c = collections.Counter(); first = []
for f in glob.glob(os.path.join(REPO, 'results', 'E2__raspgrade__*.json')):
    d = json.load(open(f)); cf = d['config']; m = d.get('metrics', {})
    unk = tuple(cf.get('unknown') or [])
    c[(cf.get('protocol'), unk, cf.get('score'), cf.get('shot'))] += 1
    if len(first) < 4:
        first.append((cf.get('protocol'), unk, cf.get('score'), m.get('auroc'),
                      m.get('n_known'), m.get('n_unknown')))
print('cells', len(c))
for x in first: print(x)
