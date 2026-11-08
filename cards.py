import json
for ds in ('raspgrade',):
    c = json.load(open('/root/rio/data/processed/%s/card.json' % ds))
    print(ds, {k: c.get(k) for k in ('n_images','n_groups','class_counts','split_counts',
                                     'n_source_images','dropped_small_polygons','unit','group_leak_count')})
