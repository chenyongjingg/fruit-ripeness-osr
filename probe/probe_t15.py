import pandas as pd
d = pd.read_csv('/root/rio/outputs/T15_collapsed.csv')
print('rows', len(d))
print(d.groupby(['view', 'protocol', 'unknown', 'shot']).size())
print('by view/protocol')
print(d.groupby(['view', 'protocol']).size())
