# Ripeness OPEN-SET recognition pipeline — automatic results report

Generated: 2026-11-08T12:54:47+0000

## Datasets

| dataset    |   n_images |   n_groups | splits                                     | classes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |   group_leaks | meta_sha256      |
|:-----------|-----------:|-----------:|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------:|:-----------------|
| banana3    |       1186 |       1181 | {"test": 178, "train": 830, "val": 178}    | underripe, ripe, overripe                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             0 | a4aca1049a622c3e |
| banana4    |      13478 |      13478 | {"test": 562, "train": 11793, "val": 1123} | unripe, ripe, overripe, rotten                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             0 | 5ed9e8f12548187d |
| f360rot    |       8090 |       5113 | {"test": 2581, "train": 3715, "val": 1794} | Apple 10, Apple 11, Apple 12, Apple 13, Apple 14, Apple 17, Apple 18, Apple 19, Apple 20, Apple 21, Apple 22, Apple 23, Apple 5, Apple 6, Apple 7, Apple 8, Apple 9, Apple Braeburn 1, Apple Red Yellow 2, Apple Rotten 1, Cucumber 1, Cucumber 10, Cucumber 11, Cucumber 3, Cucumber 4, Cucumber 5, Cucumber 6, Cucumber 7, Cucumber 8, Cucumber 9, Orange 2, Orange 3, Orange 4, Orange 5, Orange peeled 1, Peach 3, Peach 4, Peach 5, Peach 6, Pear 1, Pear 10, Pear 11, Pear 12, Pear 13, Pear 14, Pear 3, Pear 5, Pear 6, Pear 7, Pear 8, Pear 9, Pear common 1, Tomato 1, Tomato 10, Tomato 5, Tomato 7, Tomato 8, Tomato 9, Tomato Cherry Maroon 1, Tomato Cherry Orange 1, Tomato Cherry Red 2, Tomato Cherry Yellow 1, Tomato Maroon 2 |             0 | a64b2d1ccb1d6ff6 |
| ffr        |       3600 |       3600 | {"test": 1800, "train": 1800}              | Fresh_Apple, Fresh_Banana, Fresh_Orange, Rotten_Apple, Rotten_Banana, Rotten_Orange                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |             0 | 3c866afcd6c8102e |
| field4     |       4999 |       4999 | {"test": 1000, "train": 3999}              | Raw_Banana, Ripe_Banana, Raw_Mango, Ripe_Mango                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             0 | c8322676df3dec30 |
| fruit12    |       8256 |       3591 | {"test": 1315, "train": 5754, "val": 1187} | Apple_Overripe, Apple_Ripe, Apple_Rotten, Apple_Unripe, Banana_Overripe, Banana_Ripe, Banana_Rotten, Banana_Unripe, Mango_Overripe, Mango_Ripe, Mango_Rotten, Mango_Unripe                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             0 | 4a89f53048ee8b41 |
| fruits360  |       7440 |       4788 | {"test": 1931, "train": 3715, "val": 1794} | Apple 10, Apple 11, Apple 12, Apple 13, Apple 14, Apple 17, Apple 18, Apple 19, Apple 20, Apple 21, Apple 22, Apple 23, Apple 5, Apple 6, Apple 7, Apple 8, Apple 9, Apple Braeburn 1, Apple Red Yellow 2, Cucumber 1, Cucumber 10, Cucumber 11, Cucumber 3, Cucumber 4, Cucumber 5, Cucumber 6, Cucumber 7, Cucumber 8, Cucumber 9, Orange 2, Orange 3, Orange 4, Orange 5, Orange peeled 1, Peach 3, Peach 4, Peach 5, Peach 6, Pear 1, Pear 10, Pear 11, Pear 12, Pear 13, Pear 14, Pear 3, Pear 5, Pear 6, Pear 7, Pear 8, Pear 9, Pear common 1, Tomato 1, Tomato 10, Tomato 5, Tomato 7, Tomato 8, Tomato 9, Tomato Cherry Maroon 1, Tomato Cherry Orange 1, Tomato Cherry Red 2, Tomato Cherry Yellow 1, Tomato Maroon 2                 |             0 | 0390ec4b43a578c5 |
| mango_khir |        975 |        487 | {"test": 146, "train": 683, "val": 146}    | UnRipe, Ripe, OverRipe                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             0 | 689a5df23071e723 |
| ninepeach  |       3493 |       1245 | {"test": 523, "train": 2446, "val": 524}   | immature, semi-mature, mature                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             0 | 2bfe2f32c3414acf |
| raspgrade  |       5043 |        200 | {"test": 732, "train": 3556, "val": 755}   | grade1, grade2, grade3, grade4, grade5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             0 | df27a49dad04d17c |

## Closed-set few-shot (mean ± sd over seeds)

| view           | encoder   | variant   | head   |   shot | acc             | macro_f1        | off_by_one      |   n_runs |
|:---------------|:----------|:----------|:-------|-------:|:----------------|:----------------|:----------------|---------:|
| banana3        | clip_b    | cls       | corn   |      1 | 0.4831 ± 0.0533 | 0.4552 ± 0.0789 | 0.4618 ± 0.0957 |        5 |
| banana3        | clip_b    | cls       | corn   |      5 | 0.7124 ± 0.0532 | 0.6977 ± 0.0712 | 0.2393 ± 0.0416 |        5 |
| banana3        | clip_b    | cls       | corn   |     10 | 0.7427 ± 0.0304 | 0.7347 ± 0.0290 | 0.2281 ± 0.0205 |        5 |
| banana3        | clip_b    | cls       | corn   |     50 | 0.8011 ± 0.0135 | 0.7997 ± 0.0133 | 0.1809 ± 0.0145 |        5 |
| banana3        | clip_b    | cls       | corn   |    nan | 0.8876 ± 0.0000 | 0.8803 ± 0.0000 | 0.1011 ± 0.0000 |        1 |
| banana3        | clip_b    | cls       | linear |      1 | 0.5213 ± 0.0479 | 0.5112 ± 0.0604 | 0.4079 ± 0.0603 |        5 |
| banana3        | clip_b    | cls       | linear |      5 | 0.7124 ± 0.0517 | 0.6933 ± 0.0729 | 0.2236 ± 0.0421 |        5 |
| banana3        | clip_b    | cls       | linear |     10 | 0.7371 ± 0.0394 | 0.7249 ± 0.0386 | 0.2292 ± 0.0331 |        5 |
| banana3        | clip_b    | cls       | linear |     50 | 0.8124 ± 0.0193 | 0.8075 ± 0.0195 | 0.1685 ± 0.0159 |        5 |
| banana3        | clip_b    | cls       | linear |    nan | 0.8820 ± 0.0000 | 0.8745 ± 0.0000 | 0.1067 ± 0.0000 |        1 |
| banana3        | clip_b    | cls       | proto  |      1 | 0.4742 ± 0.0352 | 0.4620 ± 0.0418 | 0.4427 ± 0.0813 |        5 |
| banana3        | clip_b    | cls       | proto  |      5 | 0.7022 ± 0.0524 | 0.6911 ± 0.0655 | 0.2416 ± 0.0433 |        5 |
| banana3        | clip_b    | cls       | proto  |     10 | 0.7191 ± 0.0320 | 0.7148 ± 0.0312 | 0.2461 ± 0.0175 |        5 |
| banana3        | clip_b    | cls       | proto  |     50 | 0.7461 ± 0.0047 | 0.7455 ± 0.0049 | 0.2225 ± 0.0050 |        5 |
| banana3        | clip_b    | cls       | proto  |    nan | 0.7472 ± 0.0000 | 0.7452 ± 0.0000 | 0.2247 ± 0.0000 |        1 |
| banana3        | clip_b    | mean      | linear |      1 | 0.5618 ± 0.0515 | 0.5461 ± 0.0508 | 0.3127 ± 0.0892 |        3 |
| banana3        | clip_b    | mean      | linear |      5 | 0.6798 ± 0.0839 | 0.6594 ± 0.0959 | 0.2397 ± 0.0429 |        3 |
| banana3        | clip_b    | mean      | linear |     10 | 0.7022 ± 0.0292 | 0.6895 ± 0.0269 | 0.2172 ± 0.0117 |        3 |
| banana3        | clip_b    | mean      | linear |     50 | 0.7996 ± 0.0032 | 0.7912 ± 0.0065 | 0.1873 ± 0.0065 |        3 |
| banana3        | clip_b    | mean      | linear |    nan | 0.8596 ± 0.0000 | 0.8523 ± 0.0000 | 0.1348 ± 0.0000 |        1 |
| banana3        | clip_b    | mean      | proto  |      1 | 0.5412 ± 0.0754 | 0.5203 ± 0.0777 | 0.2865 ± 0.0595 |        3 |
| banana3        | clip_b    | mean      | proto  |      5 | 0.6723 ± 0.0924 | 0.6634 ± 0.0900 | 0.2734 ± 0.0819 |        3 |
| banana3        | clip_b    | mean      | proto  |     10 | 0.7041 ± 0.0162 | 0.6950 ± 0.0118 | 0.2341 ± 0.0172 |        3 |
| banana3        | clip_b    | mean      | proto  |     50 | 0.7416 ± 0.0149 | 0.7367 ± 0.0140 | 0.2228 ± 0.0162 |        3 |
| banana3        | clip_b    | mean      | proto  |    nan | 0.7528 ± 0.0000 | 0.7484 ± 0.0000 | 0.2191 ± 0.0000 |        1 |
| banana3        | dinov2_b  | cls       | corn   |      1 | 0.4764 ± 0.1227 | 0.4475 ± 0.1383 | 0.4910 ± 0.1396 |        5 |
| banana3        | dinov2_b  | cls       | corn   |      5 | 0.7404 ± 0.0333 | 0.7311 ± 0.0353 | 0.2292 ± 0.0392 |        5 |
| banana3        | dinov2_b  | cls       | corn   |     10 | 0.7697 ± 0.0462 | 0.7611 ± 0.0420 | 0.1989 ± 0.0464 |        5 |
| banana3        | dinov2_b  | cls       | corn   |     50 | 0.8640 ± 0.0122 | 0.8572 ± 0.0128 | 0.1169 ± 0.0122 |        5 |
| banana3        | dinov2_b  | cls       | corn   |    nan | 0.9270 ± 0.0000 | 0.9231 ± 0.0000 | 0.0618 ± 0.0000 |        1 |
| banana3        | dinov2_b  | cls       | linear |      1 | 0.5067 ± 0.1187 | 0.4678 ± 0.1041 | 0.3933 ± 0.0689 |        5 |
| banana3        | dinov2_b  | cls       | linear |      5 | 0.7438 ± 0.0402 | 0.7224 ± 0.0491 | 0.2157 ± 0.0427 |        5 |
| banana3        | dinov2_b  | cls       | linear |     10 | 0.7888 ± 0.0361 | 0.7730 ± 0.0345 | 0.1764 ± 0.0398 |        5 |
| banana3        | dinov2_b  | cls       | linear |     50 | 0.8787 ± 0.0176 | 0.8719 ± 0.0175 | 0.1034 ± 0.0152 |        5 |
| banana3        | dinov2_b  | cls       | linear |    nan | 0.9213 ± 0.0000 | 0.9175 ± 0.0000 | 0.0674 ± 0.0000 |        1 |
| banana3        | dinov2_b  | cls       | proto  |      1 | 0.4798 ± 0.1208 | 0.4400 ± 0.1393 | 0.4124 ± 0.0744 |        5 |
| banana3        | dinov2_b  | cls       | proto  |      5 | 0.7371 ± 0.0492 | 0.7315 ± 0.0468 | 0.2427 ± 0.0452 |        5 |
| banana3        | dinov2_b  | cls       | proto  |     10 | 0.7596 ± 0.0575 | 0.7541 ± 0.0507 | 0.2213 ± 0.0591 |        5 |
| banana3        | dinov2_b  | cls       | proto  |     50 | 0.8371 ± 0.0210 | 0.8318 ± 0.0200 | 0.1483 ± 0.0262 |        5 |
| banana3        | dinov2_b  | cls       | proto  |    nan | 0.8708 ± 0.0000 | 0.8649 ± 0.0000 | 0.1180 ± 0.0000 |        1 |
| banana3        | dinov2_b  | mean      | linear |      1 | 0.4007 ± 0.0606 | 0.3584 ± 0.0728 | 0.4551 ± 0.1685 |        3 |
| banana3        | dinov2_b  | mean      | linear |      5 | 0.5787 ± 0.0717 | 0.5540 ± 0.0773 | 0.3277 ± 0.0716 |        3 |
| banana3        | dinov2_b  | mean      | linear |     10 | 0.6573 ± 0.0446 | 0.6400 ± 0.0417 | 0.2734 ± 0.0339 |        3 |
| banana3        | dinov2_b  | mean      | linear |     50 | 0.8146 ± 0.0149 | 0.8061 ± 0.0158 | 0.1517 ± 0.0149 |        3 |
| banana3        | dinov2_b  | mean      | linear |    nan | 0.9270 ± 0.0000 | 0.9215 ± 0.0000 | 0.0730 ± 0.0000 |        1 |
| banana3        | dinov2_b  | mean      | proto  |      1 | 0.3951 ± 0.0601 | 0.3401 ± 0.0724 | 0.4588 ± 0.1714 |        3 |
| banana3        | dinov2_b  | mean      | proto  |      5 | 0.5468 ± 0.0982 | 0.5362 ± 0.0931 | 0.3502 ± 0.0924 |        3 |
| banana3        | dinov2_b  | mean      | proto  |     10 | 0.6610 ± 0.0458 | 0.6530 ± 0.0416 | 0.2921 ± 0.0439 |        3 |
| banana3        | dinov2_b  | mean      | proto  |     50 | 0.7285 ± 0.0086 | 0.7245 ± 0.0086 | 0.2266 ± 0.0309 |        3 |
| banana3        | dinov2_b  | mean      | proto  |    nan | 0.7584 ± 0.0000 | 0.7550 ± 0.0000 | 0.2135 ± 0.0000 |        1 |
| banana3        | dinov2_s  | cls       | corn   |      1 | 0.4989 ± 0.1100 | 0.4742 ± 0.1190 | 0.4607 ± 0.1397 |        5 |
| banana3        | dinov2_s  | cls       | corn   |      5 | 0.7494 ± 0.0283 | 0.7334 ± 0.0293 | 0.2112 ± 0.0334 |        5 |
| banana3        | dinov2_s  | cls       | corn   |     10 | 0.7899 ± 0.0418 | 0.7784 ± 0.0404 | 0.1764 ± 0.0398 |        5 |
| banana3        | dinov2_s  | cls       | corn   |     50 | 0.9045 ± 0.0105 | 0.8988 ± 0.0116 | 0.0798 ± 0.0108 |        5 |
| banana3        | dinov2_s  | cls       | corn   |    nan | 0.9438 ± 0.0000 | 0.9417 ± 0.0000 | 0.0449 ± 0.0000 |        1 |
| banana3        | dinov2_s  | cls       | linear |      1 | 0.5315 ± 0.0854 | 0.5093 ± 0.0630 | 0.4135 ± 0.1013 |        5 |
| banana3        | dinov2_s  | cls       | linear |      5 | 0.7494 ± 0.0240 | 0.7232 ± 0.0295 | 0.2034 ± 0.0309 |        5 |
| banana3        | dinov2_s  | cls       | linear |     10 | 0.8000 ± 0.0299 | 0.7821 ± 0.0317 | 0.1652 ± 0.0329 |        5 |
| banana3        | dinov2_s  | cls       | linear |     50 | 0.9067 ± 0.0129 | 0.9009 ± 0.0150 | 0.0764 ± 0.0129 |        5 |
| banana3        | dinov2_s  | cls       | linear |    nan | 0.9551 ± 0.0000 | 0.9537 ± 0.0000 | 0.0337 ± 0.0000 |        1 |
| banana3        | dinov2_s  | cls       | proto  |      1 | 0.5112 ± 0.1186 | 0.4990 ± 0.1191 | 0.4303 ± 0.1352 |        5 |
| banana3        | dinov2_s  | cls       | proto  |      5 | 0.7551 ± 0.0452 | 0.7421 ± 0.0408 | 0.2180 ± 0.0445 |        5 |
| banana3        | dinov2_s  | cls       | proto  |     10 | 0.7843 ± 0.0492 | 0.7737 ± 0.0472 | 0.1955 ± 0.0472 |        5 |
| banana3        | dinov2_s  | cls       | proto  |     50 | 0.8652 ± 0.0210 | 0.8564 ± 0.0215 | 0.1202 ± 0.0189 |        5 |
| banana3        | dinov2_s  | cls       | proto  |    nan | 0.8933 ± 0.0000 | 0.8874 ± 0.0000 | 0.0899 ± 0.0000 |        1 |
| banana3        | dinov2_s  | mean      | linear |      1 | 0.4551 ± 0.1105 | 0.4164 ± 0.1350 | 0.4157 ± 0.1515 |        3 |
| banana3        | dinov2_s  | mean      | linear |      5 | 0.6386 ± 0.0621 | 0.5926 ± 0.0692 | 0.2846 ± 0.0504 |        3 |
| banana3        | dinov2_s  | mean      | linear |     10 | 0.7154 ± 0.0213 | 0.6934 ± 0.0216 | 0.2322 ± 0.0319 |        3 |
| banana3        | dinov2_s  | mean      | linear |     50 | 0.8502 ± 0.0162 | 0.8414 ± 0.0160 | 0.1199 ± 0.0086 |        3 |
| banana3        | dinov2_s  | mean      | linear |    nan | 0.9270 ± 0.0000 | 0.9231 ± 0.0000 | 0.0618 ± 0.0000 |        1 |
| banana3        | dinov2_s  | mean      | proto  |      1 | 0.4382 ± 0.0955 | 0.4021 ± 0.1150 | 0.4363 ± 0.1466 |        3 |
| banana3        | dinov2_s  | mean      | proto  |      5 | 0.6142 ± 0.0927 | 0.5909 ± 0.0790 | 0.3165 ± 0.0871 |        3 |
| banana3        | dinov2_s  | mean      | proto  |     10 | 0.7041 ± 0.0288 | 0.6901 ± 0.0295 | 0.2528 ± 0.0281 |        3 |
| banana3        | dinov2_s  | mean      | proto  |     50 | 0.7640 ± 0.0149 | 0.7557 ± 0.0156 | 0.1948 ± 0.0086 |        3 |
| banana3        | dinov2_s  | mean      | proto  |    nan | 0.7753 ± 0.0000 | 0.7677 ± 0.0000 | 0.2022 ± 0.0000 |        1 |
| banana3        | resnet50  | cls       | corn   |      1 | 0.4831 ± 0.0802 | 0.4498 ± 0.0936 | 0.4202 ± 0.1282 |        5 |
| banana3        | resnet50  | cls       | corn   |      5 | 0.5933 ± 0.0831 | 0.5743 ± 0.0805 | 0.3225 ± 0.0978 |        5 |
| banana3        | resnet50  | cls       | corn   |     10 | 0.6921 ± 0.0223 | 0.6771 ± 0.0228 | 0.2371 ± 0.0279 |        5 |
| banana3        | resnet50  | cls       | corn   |     50 | 0.7899 ± 0.0220 | 0.7809 ± 0.0232 | 0.1944 ± 0.0152 |        5 |
| banana3        | resnet50  | cls       | corn   |    nan | 0.8708 ± 0.0000 | 0.8630 ± 0.0000 | 0.1236 ± 0.0000 |        1 |
| banana3        | resnet50  | cls       | linear |      1 | 0.5090 ± 0.0739 | 0.4637 ± 0.0828 | 0.3551 ± 0.1191 |        5 |
| banana3        | resnet50  | cls       | linear |      5 | 0.6180 ± 0.0710 | 0.5950 ± 0.0720 | 0.2854 ± 0.0839 |        5 |
| banana3        | resnet50  | cls       | linear |     10 | 0.7022 ± 0.0173 | 0.6855 ± 0.0202 | 0.2326 ± 0.0268 |        5 |
| banana3        | resnet50  | cls       | linear |     50 | 0.8022 ± 0.0145 | 0.7915 ± 0.0155 | 0.1843 ± 0.0083 |        5 |
| banana3        | resnet50  | cls       | linear |    nan | 0.8933 ± 0.0000 | 0.8859 ± 0.0000 | 0.1011 ± 0.0000 |        1 |
| banana3        | resnet50  | cls       | proto  |      1 | 0.4933 ± 0.0973 | 0.4672 ± 0.1087 | 0.3809 ± 0.1200 |        5 |
| banana3        | resnet50  | cls       | proto  |      5 | 0.5865 ± 0.0864 | 0.5723 ± 0.0790 | 0.3258 ± 0.1103 |        5 |
| banana3        | resnet50  | cls       | proto  |     10 | 0.6798 ± 0.0235 | 0.6685 ± 0.0217 | 0.2371 ± 0.0230 |        5 |
| banana3        | resnet50  | cls       | proto  |     50 | 0.7236 ± 0.0208 | 0.7133 ± 0.0176 | 0.2393 ± 0.0162 |        5 |
| banana3        | resnet50  | cls       | proto  |    nan | 0.7416 ± 0.0000 | 0.7295 ± 0.0000 | 0.2135 ± 0.0000 |        1 |
| banana4        | clip_b    | cls       | corn   |      1 | 0.6525 ± 0.1147 | 0.6263 ± 0.1473 | 0.3321 ± 0.1066 |        5 |
| banana4        | clip_b    | cls       | corn   |      5 | 0.8844 ± 0.0369 | 0.8840 ± 0.0403 | 0.1146 ± 0.0379 |        5 |
| banana4        | clip_b    | cls       | corn   |     10 | 0.9040 ± 0.0402 | 0.9075 ± 0.0369 | 0.0960 ± 0.0402 |        5 |
| banana4        | clip_b    | cls       | corn   |     50 | 0.9517 ± 0.0058 | 0.9528 ± 0.0058 | 0.0483 ± 0.0058 |        5 |
| banana4        | clip_b    | cls       | corn   |    nan | 0.9708 ± 0.0000 | 0.9716 ± 0.0000 | 0.0292 ± 0.0000 |        1 |
| banana4        | clip_b    | cls       | linear |      1 | 0.6477 ± 0.0978 | 0.6200 ± 0.1306 | 0.3401 ± 0.0931 |        5 |
| banana4        | clip_b    | cls       | linear |      5 | 0.8950 ± 0.0351 | 0.8969 ± 0.0361 | 0.1034 ± 0.0364 |        5 |
| banana4        | clip_b    | cls       | linear |     10 | 0.8950 ± 0.0548 | 0.8994 ± 0.0509 | 0.1045 ± 0.0543 |        5 |
| banana4        | clip_b    | cls       | linear |     50 | 0.9538 ± 0.0030 | 0.9551 ± 0.0028 | 0.0462 ± 0.0030 |        5 |
| banana4        | clip_b    | cls       | linear |    nan | 0.9761 ± 0.0000 | 0.9768 ± 0.0000 | 0.0239 ± 0.0000 |        1 |
| banana4        | clip_b    | cls       | proto  |      1 | 0.6387 ± 0.1012 | 0.6124 ± 0.1354 | 0.3438 ± 0.0959 |        5 |
| banana4        | clip_b    | cls       | proto  |      5 | 0.8706 ± 0.0191 | 0.8707 ± 0.0202 | 0.1263 ± 0.0220 |        5 |
| banana4        | clip_b    | cls       | proto  |     10 | 0.8870 ± 0.0416 | 0.8911 ± 0.0381 | 0.1130 ± 0.0416 |        5 |
| banana4        | clip_b    | cls       | proto  |     50 | 0.9422 ± 0.0044 | 0.9437 ± 0.0040 | 0.0578 ± 0.0044 |        5 |
| banana4        | clip_b    | cls       | proto  |    nan | 0.9576 ± 0.0000 | 0.9585 ± 0.0000 | 0.0424 ± 0.0000 |        1 |
| banana4        | clip_b    | mean      | linear |      1 | 0.6755 ± 0.0570 | 0.6635 ± 0.0487 | 0.2997 ± 0.0417 |        3 |
| banana4        | clip_b    | mean      | linear |      5 | 0.8736 ± 0.0489 | 0.8769 ± 0.0444 | 0.1256 ± 0.0493 |        3 |
| banana4        | clip_b    | mean      | linear |     10 | 0.8833 ± 0.0666 | 0.8872 ± 0.0627 | 0.1158 ± 0.0651 |        3 |
| banana4        | clip_b    | mean      | linear |     50 | 0.9416 ± 0.0122 | 0.9434 ± 0.0114 | 0.0584 ± 0.0122 |        3 |
| banana4        | clip_b    | mean      | linear |    nan | 0.9761 ± 0.0000 | 0.9767 ± 0.0000 | 0.0239 ± 0.0000 |        1 |
| banana4        | clip_b    | mean      | proto  |      1 | 0.6331 ± 0.0619 | 0.6035 ± 0.0332 | 0.3431 ± 0.0476 |        3 |
| banana4        | clip_b    | mean      | proto  |      5 | 0.8771 ± 0.0368 | 0.8804 ± 0.0332 | 0.1211 ± 0.0362 |        3 |
| banana4        | clip_b    | mean      | proto  |     10 | 0.8789 ± 0.0539 | 0.8836 ± 0.0493 | 0.1202 ± 0.0523 |        3 |
| banana4        | clip_b    | mean      | proto  |     50 | 0.9337 ± 0.0140 | 0.9355 ± 0.0137 | 0.0663 ± 0.0140 |        3 |
| banana4        | clip_b    | mean      | proto  |    nan | 0.9496 ± 0.0000 | 0.9509 ± 0.0000 | 0.0504 ± 0.0000 |        1 |
| banana4        | dinov2_b  | cls       | corn   |      1 | 0.7236 ± 0.1279 | 0.7086 ± 0.1403 | 0.2446 ± 0.1208 |        5 |
| banana4        | dinov2_b  | cls       | corn   |      5 | 0.9003 ± 0.0569 | 0.8993 ± 0.0608 | 0.0997 ± 0.0569 |        5 |
| banana4        | dinov2_b  | cls       | corn   |     10 | 0.9162 ± 0.0399 | 0.9176 ± 0.0400 | 0.0838 ± 0.0399 |        5 |
| banana4        | dinov2_b  | cls       | corn   |     50 | 0.9459 ± 0.0030 | 0.9468 ± 0.0030 | 0.0541 ± 0.0030 |        5 |
| banana4        | dinov2_b  | cls       | corn   |    nan | 0.9735 ± 0.0000 | 0.9742 ± 0.0000 | 0.0265 ± 0.0000 |        1 |
| banana4        | dinov2_b  | cls       | linear |      1 | 0.7443 ± 0.1299 | 0.7310 ± 0.1459 | 0.2154 ± 0.1182 |        5 |
| banana4        | dinov2_b  | cls       | linear |      5 | 0.9061 ± 0.0577 | 0.9052 ± 0.0618 | 0.0939 ± 0.0577 |        5 |
| banana4        | dinov2_b  | cls       | linear |     10 | 0.9289 ± 0.0435 | 0.9303 ± 0.0434 | 0.0711 ± 0.0435 |        5 |
| banana4        | dinov2_b  | cls       | linear |     50 | 0.9480 ± 0.0044 | 0.9491 ± 0.0045 | 0.0520 ± 0.0044 |        5 |
| banana4        | dinov2_b  | cls       | linear |    nan | 0.9814 ± 0.0000 | 0.9820 ± 0.0000 | 0.0186 ± 0.0000 |        1 |
| banana4        | dinov2_b  | cls       | proto  |      1 | 0.7294 ± 0.1407 | 0.7100 ± 0.1556 | 0.2180 ± 0.1265 |        5 |
| banana4        | dinov2_b  | cls       | proto  |      5 | 0.8584 ± 0.0893 | 0.8476 ± 0.1060 | 0.1416 ± 0.0893 |        5 |
| banana4        | dinov2_b  | cls       | proto  |     10 | 0.8801 ± 0.0735 | 0.8770 ± 0.0824 | 0.1199 ± 0.0735 |        5 |
| banana4        | dinov2_b  | cls       | proto  |     50 | 0.9061 ± 0.0124 | 0.9082 ± 0.0122 | 0.0939 ± 0.0124 |        5 |
| banana4        | dinov2_b  | cls       | proto  |    nan | 0.8992 ± 0.0000 | 0.9014 ± 0.0000 | 0.1008 ± 0.0000 |        1 |
| banana4        | dinov2_b  | mean      | linear |      1 | 0.5464 ± 0.0505 | 0.5366 ± 0.0579 | 0.4067 ± 0.0177 |        3 |
| banana4        | dinov2_b  | mean      | linear |      5 | 0.7728 ± 0.0494 | 0.7709 ± 0.0550 | 0.2113 ± 0.0539 |        3 |
| banana4        | dinov2_b  | mean      | linear |     10 | 0.8859 ± 0.0276 | 0.8889 ± 0.0266 | 0.1114 ± 0.0256 |        3 |
| banana4        | dinov2_b  | mean      | linear |     50 | 0.9399 ± 0.0041 | 0.9407 ± 0.0041 | 0.0601 ± 0.0041 |        3 |
| banana4        | dinov2_b  | mean      | linear |    nan | 0.9788 ± 0.0000 | 0.9794 ± 0.0000 | 0.0212 ± 0.0000 |        1 |
| banana4        | dinov2_b  | mean      | proto  |      1 | 0.5261 ± 0.0839 | 0.5074 ± 0.0995 | 0.4032 ± 0.0401 |        3 |
| banana4        | dinov2_b  | mean      | proto  |      5 | 0.7569 ± 0.0350 | 0.7589 ± 0.0353 | 0.2219 ± 0.0394 |        3 |
| banana4        | dinov2_b  | mean      | proto  |     10 | 0.8470 ± 0.0296 | 0.8504 ± 0.0289 | 0.1485 ± 0.0279 |        3 |
| banana4        | dinov2_b  | mean      | proto  |     50 | 0.8939 ± 0.0565 | 0.8954 ± 0.0557 | 0.1052 ± 0.0567 |        3 |
| banana4        | dinov2_b  | mean      | proto  |    nan | 0.9072 ± 0.0000 | 0.9091 ± 0.0000 | 0.0928 ± 0.0000 |        1 |
| banana4        | dinov2_s  | cls       | corn   |      1 | 0.6902 ± 0.0739 | 0.6867 ± 0.0730 | 0.2939 ± 0.0646 |        5 |
| banana4        | dinov2_s  | cls       | corn   |      5 | 0.9040 ± 0.0449 | 0.9044 ± 0.0464 | 0.0960 ± 0.0449 |        5 |
| banana4        | dinov2_s  | cls       | corn   |     10 | 0.9236 ± 0.0335 | 0.9255 ± 0.0330 | 0.0764 ± 0.0335 |        5 |
| banana4        | dinov2_s  | cls       | corn   |     50 | 0.9533 ± 0.0048 | 0.9544 ± 0.0048 | 0.0467 ± 0.0048 |        5 |
| banana4        | dinov2_s  | cls       | corn   |    nan | 0.9814 ± 0.0000 | 0.9819 ± 0.0000 | 0.0186 ± 0.0000 |        1 |
| banana4        | dinov2_s  | cls       | linear |      1 | 0.6944 ± 0.0750 | 0.6904 ± 0.0776 | 0.2881 ± 0.0649 |        5 |
| banana4        | dinov2_s  | cls       | linear |      5 | 0.9072 ± 0.0466 | 0.9080 ± 0.0485 | 0.0928 ± 0.0466 |        5 |
| banana4        | dinov2_s  | cls       | linear |     10 | 0.9337 ± 0.0290 | 0.9355 ± 0.0287 | 0.0663 ± 0.0290 |        5 |
| banana4        | dinov2_s  | cls       | linear |     50 | 0.9576 ± 0.0062 | 0.9587 ± 0.0063 | 0.0424 ± 0.0062 |        5 |
| banana4        | dinov2_s  | cls       | linear |    nan | 0.9841 ± 0.0000 | 0.9846 ± 0.0000 | 0.0159 ± 0.0000 |        1 |
| banana4        | dinov2_s  | cls       | proto  |      1 | 0.6801 ± 0.0726 | 0.6711 ± 0.0761 | 0.3019 ± 0.0624 |        5 |
| banana4        | dinov2_s  | cls       | proto  |      5 | 0.8769 ± 0.0694 | 0.8738 ± 0.0753 | 0.1231 ± 0.0694 |        5 |
| banana4        | dinov2_s  | cls       | proto  |     10 | 0.8976 ± 0.0506 | 0.8983 ± 0.0531 | 0.1024 ± 0.0506 |        5 |
| banana4        | dinov2_s  | cls       | proto  |     50 | 0.9225 ± 0.0110 | 0.9246 ± 0.0108 | 0.0775 ± 0.0110 |        5 |
| banana4        | dinov2_s  | cls       | proto  |    nan | 0.9257 ± 0.0000 | 0.9277 ± 0.0000 | 0.0743 ± 0.0000 |        1 |
| banana4        | dinov2_s  | mean      | linear |      1 | 0.5393 ± 0.0504 | 0.5322 ± 0.0590 | 0.4244 ± 0.0421 |        3 |
| banana4        | dinov2_s  | mean      | linear |      5 | 0.7091 ± 0.0493 | 0.7080 ± 0.0539 | 0.2538 ± 0.0100 |        3 |
| banana4        | dinov2_s  | mean      | linear |     10 | 0.8170 ± 0.0544 | 0.8198 ± 0.0542 | 0.1795 ± 0.0519 |        3 |
| banana4        | dinov2_s  | mean      | linear |     50 | 0.9328 ± 0.0171 | 0.9350 ± 0.0165 | 0.0672 ± 0.0171 |        3 |
| banana4        | dinov2_s  | mean      | linear |    nan | 0.9788 ± 0.0000 | 0.9793 ± 0.0000 | 0.0212 ± 0.0000 |        1 |
| banana4        | dinov2_s  | mean      | proto  |      1 | 0.5031 ± 0.0606 | 0.4918 ± 0.0759 | 0.4341 ± 0.0442 |        3 |
| banana4        | dinov2_s  | mean      | proto  |      5 | 0.7003 ± 0.0486 | 0.6990 ± 0.0530 | 0.2573 ± 0.0217 |        3 |
| banana4        | dinov2_s  | mean      | proto  |     10 | 0.7958 ± 0.0322 | 0.7985 ± 0.0324 | 0.1998 ± 0.0292 |        3 |
| banana4        | dinov2_s  | mean      | proto  |     50 | 0.8630 ± 0.0662 | 0.8655 ± 0.0665 | 0.1344 ± 0.0692 |        3 |
| banana4        | dinov2_s  | mean      | proto  |    nan | 0.9310 ± 0.0000 | 0.9330 ± 0.0000 | 0.0690 ± 0.0000 |        1 |
| banana4        | resnet50  | cls       | corn   |      1 | 0.6074 ± 0.0593 | 0.5915 ± 0.0527 | 0.3666 ± 0.0250 |        5 |
| banana4        | resnet50  | cls       | corn   |      5 | 0.7538 ± 0.0601 | 0.7469 ± 0.0684 | 0.2446 ± 0.0597 |        5 |
| banana4        | resnet50  | cls       | corn   |     10 | 0.7862 ± 0.0661 | 0.7814 ± 0.0747 | 0.2138 ± 0.0661 |        5 |
| banana4        | resnet50  | cls       | corn   |     50 | 0.8520 ± 0.0280 | 0.8527 ± 0.0298 | 0.1480 ± 0.0280 |        5 |
| banana4        | resnet50  | cls       | corn   |    nan | 0.9576 ± 0.0000 | 0.9588 ± 0.0000 | 0.0424 ± 0.0000 |        1 |
| banana4        | resnet50  | cls       | linear |      1 | 0.5915 ± 0.0824 | 0.5700 ± 0.0804 | 0.3724 ± 0.0350 |        5 |
| banana4        | resnet50  | cls       | linear |      5 | 0.7528 ± 0.0646 | 0.7479 ± 0.0724 | 0.2451 ± 0.0655 |        5 |
| banana4        | resnet50  | cls       | linear |     10 | 0.7973 ± 0.0668 | 0.7933 ± 0.0748 | 0.2027 ± 0.0668 |        5 |
| banana4        | resnet50  | cls       | linear |     50 | 0.8748 ± 0.0330 | 0.8761 ± 0.0342 | 0.1252 ± 0.0330 |        5 |
| banana4        | resnet50  | cls       | linear |    nan | 0.9655 ± 0.0000 | 0.9665 ± 0.0000 | 0.0345 ± 0.0000 |        1 |
| banana4        | resnet50  | cls       | proto  |      1 | 0.5947 ± 0.0850 | 0.5834 ± 0.0873 | 0.3751 ± 0.0529 |        5 |
| banana4        | resnet50  | cls       | proto  |      5 | 0.7210 ± 0.0353 | 0.7084 ± 0.0416 | 0.2775 ± 0.0354 |        5 |
| banana4        | resnet50  | cls       | proto  |     10 | 0.7480 ± 0.0536 | 0.7369 ± 0.0654 | 0.2520 ± 0.0536 |        5 |
| banana4        | resnet50  | cls       | proto  |     50 | 0.7448 ± 0.0274 | 0.7352 ± 0.0347 | 0.2552 ± 0.0274 |        5 |
| banana4        | resnet50  | cls       | proto  |    nan | 0.7480 ± 0.0000 | 0.7412 ± 0.0000 | 0.2520 ± 0.0000 |        1 |
| field4_banana  | clip_b    | cls       | corn   |      1 | 0.7124 ± 0.1129 | 0.6826 ± 0.1578 | 0.2876 ± 0.1129 |        5 |
| field4_banana  | clip_b    | cls       | corn   |      5 | 0.7684 ± 0.1391 | 0.7576 ± 0.1495 | 0.2316 ± 0.1391 |        5 |
| field4_banana  | clip_b    | cls       | corn   |     10 | 0.8348 ± 0.0605 | 0.8308 ± 0.0634 | 0.1652 ± 0.0605 |        5 |
| field4_banana  | clip_b    | cls       | corn   |     50 | 0.9256 ± 0.0446 | 0.9249 ± 0.0460 | 0.0744 ± 0.0446 |        5 |
| field4_banana  | clip_b    | cls       | corn   |    nan | 0.9980 ± 0.0000 | 0.9980 ± 0.0000 | 0.0020 ± 0.0000 |        1 |
| field4_banana  | clip_b    | cls       | linear |      1 | 0.7124 ± 0.1129 | 0.6826 ± 0.1578 | 0.2876 ± 0.1129 |        5 |
| field4_banana  | clip_b    | cls       | linear |      5 | 0.7684 ± 0.1391 | 0.7576 ± 0.1495 | 0.2316 ± 0.1391 |        5 |
| field4_banana  | clip_b    | cls       | linear |     10 | 0.8348 ± 0.0605 | 0.8308 ± 0.0634 | 0.1652 ± 0.0605 |        5 |
| field4_banana  | clip_b    | cls       | linear |     50 | 0.9256 ± 0.0446 | 0.9249 ± 0.0460 | 0.0744 ± 0.0446 |        5 |
| field4_banana  | clip_b    | cls       | linear |    nan | 0.9980 ± 0.0000 | 0.9980 ± 0.0000 | 0.0020 ± 0.0000 |        1 |
| field4_banana  | clip_b    | cls       | proto  |      1 | 0.7124 ± 0.1129 | 0.6826 ± 0.1578 | 0.2876 ± 0.1129 |        5 |
| field4_banana  | clip_b    | cls       | proto  |      5 | 0.7620 ± 0.1387 | 0.7484 ± 0.1544 | 0.2380 ± 0.1387 |        5 |
| field4_banana  | clip_b    | cls       | proto  |     10 | 0.8204 ± 0.0632 | 0.8149 ± 0.0685 | 0.1796 ± 0.0632 |        5 |
| field4_banana  | clip_b    | cls       | proto  |     50 | 0.8480 ± 0.0660 | 0.8435 ± 0.0732 | 0.1520 ± 0.0660 |        5 |
| field4_banana  | clip_b    | cls       | proto  |    nan | 0.8700 ± 0.0000 | 0.8689 ± 0.0000 | 0.1300 ± 0.0000 |        1 |
| field4_banana  | clip_b    | mean      | linear |      1 | 0.7247 ± 0.0443 | 0.7049 ± 0.0545 | 0.2753 ± 0.0443 |        3 |
| field4_banana  | clip_b    | mean      | linear |      5 | 0.6420 ± 0.1331 | 0.6047 ± 0.1811 | 0.3580 ± 0.1331 |        3 |
| field4_banana  | clip_b    | mean      | linear |     10 | 0.6087 ± 0.0353 | 0.5649 ± 0.0842 | 0.3913 ± 0.0353 |        3 |
| field4_banana  | clip_b    | mean      | linear |     50 | 0.6373 ± 0.0680 | 0.5802 ± 0.1063 | 0.3627 ± 0.0680 |        3 |
| field4_banana  | clip_b    | mean      | linear |    nan | 0.9420 ± 0.0000 | 0.9419 ± 0.0000 | 0.0580 ± 0.0000 |        1 |
| field4_banana  | clip_b    | mean      | proto  |      1 | 0.7247 ± 0.0443 | 0.7049 ± 0.0545 | 0.2753 ± 0.0443 |        3 |
| field4_banana  | clip_b    | mean      | proto  |      5 | 0.6347 ± 0.1285 | 0.5963 ± 0.1771 | 0.3653 ± 0.1285 |        3 |
| field4_banana  | clip_b    | mean      | proto  |     10 | 0.5960 ± 0.0322 | 0.5513 ± 0.0746 | 0.4040 ± 0.0322 |        3 |
| field4_banana  | clip_b    | mean      | proto  |     50 | 0.5753 ± 0.0393 | 0.4872 ± 0.0784 | 0.4247 ± 0.0393 |        3 |
| field4_banana  | clip_b    | mean      | proto  |    nan | 0.5960 ± 0.0000 | 0.5278 ± 0.0000 | 0.4040 ± 0.0000 |        1 |
| field4_banana  | dinov2_b  | cls       | corn   |      1 | 0.7560 ± 0.0576 | 0.7467 ± 0.0657 | 0.2440 ± 0.0576 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |      5 | 0.7896 ± 0.1146 | 0.7766 ± 0.1295 | 0.2104 ± 0.1146 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |     10 | 0.8956 ± 0.0340 | 0.8945 ± 0.0356 | 0.1044 ± 0.0340 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |     50 | 0.9744 ± 0.0297 | 0.9743 ± 0.0299 | 0.0256 ± 0.0297 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_banana  | dinov2_b  | cls       | linear |      1 | 0.7560 ± 0.0576 | 0.7467 ± 0.0657 | 0.2440 ± 0.0576 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |      5 | 0.7896 ± 0.1146 | 0.7766 ± 0.1295 | 0.2104 ± 0.1146 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |     10 | 0.8956 ± 0.0340 | 0.8945 ± 0.0356 | 0.1044 ± 0.0340 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |     50 | 0.9744 ± 0.0297 | 0.9743 ± 0.0299 | 0.0256 ± 0.0297 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_banana  | dinov2_b  | cls       | proto  |      1 | 0.7560 ± 0.0576 | 0.7467 ± 0.0657 | 0.2440 ± 0.0576 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |      5 | 0.7720 ± 0.1318 | 0.7511 ± 0.1544 | 0.2280 ± 0.1318 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |     10 | 0.8888 ± 0.0413 | 0.8873 ± 0.0439 | 0.1112 ± 0.0413 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |     50 | 0.8736 ± 0.1113 | 0.8658 ± 0.1271 | 0.1264 ± 0.1113 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |    nan | 0.9480 ± 0.0000 | 0.9479 ± 0.0000 | 0.0520 ± 0.0000 |        1 |
| field4_banana  | dinov2_b  | mean      | linear |      1 | 0.6400 ± 0.0382 | 0.6009 ± 0.0450 | 0.3600 ± 0.0382 |        3 |
| field4_banana  | dinov2_b  | mean      | linear |      5 | 0.6093 ± 0.0935 | 0.5807 ± 0.0921 | 0.3907 ± 0.0935 |        3 |
| field4_banana  | dinov2_b  | mean      | linear |     10 | 0.5947 ± 0.0682 | 0.5689 ± 0.0788 | 0.4053 ± 0.0682 |        3 |
| field4_banana  | dinov2_b  | mean      | linear |     50 | 0.6873 ± 0.0150 | 0.6664 ± 0.0310 | 0.3127 ± 0.0150 |        3 |
| field4_banana  | dinov2_b  | mean      | linear |    nan | 0.8760 ± 0.0000 | 0.8756 ± 0.0000 | 0.1240 ± 0.0000 |        1 |
| field4_banana  | dinov2_b  | mean      | proto  |      1 | 0.6400 ± 0.0382 | 0.6009 ± 0.0450 | 0.3600 ± 0.0382 |        3 |
| field4_banana  | dinov2_b  | mean      | proto  |      5 | 0.6040 ± 0.0975 | 0.5658 ± 0.1045 | 0.3960 ± 0.0975 |        3 |
| field4_banana  | dinov2_b  | mean      | proto  |     10 | 0.5960 ± 0.0794 | 0.5499 ± 0.1143 | 0.4040 ± 0.0794 |        3 |
| field4_banana  | dinov2_b  | mean      | proto  |     50 | 0.5660 ± 0.0296 | 0.4663 ± 0.0575 | 0.4340 ± 0.0296 |        3 |
| field4_banana  | dinov2_b  | mean      | proto  |    nan | 0.5480 ± 0.0000 | 0.4319 ± 0.0000 | 0.4520 ± 0.0000 |        1 |
| field4_banana  | dinov2_s  | cls       | corn   |      1 | 0.6600 ± 0.1018 | 0.6217 ± 0.1445 | 0.3400 ± 0.1018 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |      5 | 0.7820 ± 0.0889 | 0.7704 ± 0.0972 | 0.2180 ± 0.0889 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |     10 | 0.8920 ± 0.0833 | 0.8918 ± 0.0834 | 0.1080 ± 0.0833 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |     50 | 0.9640 ± 0.0338 | 0.9638 ± 0.0341 | 0.0360 ± 0.0338 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |    nan | 0.9980 ± 0.0000 | 0.9980 ± 0.0000 | 0.0020 ± 0.0000 |        1 |
| field4_banana  | dinov2_s  | cls       | linear |      1 | 0.6600 ± 0.1018 | 0.6217 ± 0.1445 | 0.3400 ± 0.1018 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |      5 | 0.7820 ± 0.0889 | 0.7704 ± 0.0972 | 0.2180 ± 0.0889 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |     10 | 0.8920 ± 0.0833 | 0.8918 ± 0.0834 | 0.1080 ± 0.0833 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |     50 | 0.9640 ± 0.0338 | 0.9638 ± 0.0341 | 0.0360 ± 0.0338 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |    nan | 0.9980 ± 0.0000 | 0.9980 ± 0.0000 | 0.0020 ± 0.0000 |        1 |
| field4_banana  | dinov2_s  | cls       | proto  |      1 | 0.6600 ± 0.1018 | 0.6217 ± 0.1445 | 0.3400 ± 0.1018 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |      5 | 0.7600 ± 0.1134 | 0.7380 ± 0.1363 | 0.2400 ± 0.1134 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |     10 | 0.8692 ± 0.0970 | 0.8681 ± 0.0980 | 0.1308 ± 0.0970 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |     50 | 0.9088 ± 0.0690 | 0.9067 ± 0.0726 | 0.0912 ± 0.0690 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |    nan | 0.9440 ± 0.0000 | 0.9438 ± 0.0000 | 0.0560 ± 0.0000 |        1 |
| field4_banana  | dinov2_s  | mean      | linear |      1 | 0.6487 ± 0.0364 | 0.6279 ± 0.0404 | 0.3513 ± 0.0364 |        3 |
| field4_banana  | dinov2_s  | mean      | linear |      5 | 0.5873 ± 0.1033 | 0.5600 ± 0.1260 | 0.4127 ± 0.1033 |        3 |
| field4_banana  | dinov2_s  | mean      | linear |     10 | 0.5993 ± 0.0896 | 0.5765 ± 0.0905 | 0.4007 ± 0.0896 |        3 |
| field4_banana  | dinov2_s  | mean      | linear |     50 | 0.6967 ± 0.0340 | 0.6689 ± 0.0425 | 0.3033 ± 0.0340 |        3 |
| field4_banana  | dinov2_s  | mean      | linear |    nan | 0.9760 ± 0.0000 | 0.9760 ± 0.0000 | 0.0240 ± 0.0000 |        1 |
| field4_banana  | dinov2_s  | mean      | proto  |      1 | 0.6487 ± 0.0364 | 0.6279 ± 0.0404 | 0.3513 ± 0.0364 |        3 |
| field4_banana  | dinov2_s  | mean      | proto  |      5 | 0.5947 ± 0.0947 | 0.5577 ± 0.1225 | 0.4053 ± 0.0947 |        3 |
| field4_banana  | dinov2_s  | mean      | proto  |     10 | 0.5933 ± 0.0725 | 0.5665 ± 0.0790 | 0.4067 ± 0.0725 |        3 |
| field4_banana  | dinov2_s  | mean      | proto  |     50 | 0.5707 ± 0.0424 | 0.4767 ± 0.0724 | 0.4293 ± 0.0424 |        3 |
| field4_banana  | dinov2_s  | mean      | proto  |    nan | 0.5540 ± 0.0000 | 0.4505 ± 0.0000 | 0.4460 ± 0.0000 |        1 |
| field4_banana  | resnet50  | cls       | corn   |      1 | 0.8212 ± 0.0448 | 0.8181 ± 0.0462 | 0.1788 ± 0.0448 |        5 |
| field4_banana  | resnet50  | cls       | corn   |      5 | 0.8452 ± 0.0382 | 0.8427 ± 0.0411 | 0.1548 ± 0.0382 |        5 |
| field4_banana  | resnet50  | cls       | corn   |     10 | 0.8308 ± 0.1035 | 0.8263 ± 0.1096 | 0.1692 ± 0.1035 |        5 |
| field4_banana  | resnet50  | cls       | corn   |     50 | 0.9180 ± 0.0246 | 0.9176 ± 0.0250 | 0.0820 ± 0.0246 |        5 |
| field4_banana  | resnet50  | cls       | corn   |    nan | 0.9880 ± 0.0000 | 0.9880 ± 0.0000 | 0.0120 ± 0.0000 |        1 |
| field4_banana  | resnet50  | cls       | linear |      1 | 0.8212 ± 0.0448 | 0.8181 ± 0.0462 | 0.1788 ± 0.0448 |        5 |
| field4_banana  | resnet50  | cls       | linear |      5 | 0.8452 ± 0.0382 | 0.8427 ± 0.0411 | 0.1548 ± 0.0382 |        5 |
| field4_banana  | resnet50  | cls       | linear |     10 | 0.8308 ± 0.1035 | 0.8263 ± 0.1096 | 0.1692 ± 0.1035 |        5 |
| field4_banana  | resnet50  | cls       | linear |     50 | 0.9180 ± 0.0246 | 0.9176 ± 0.0250 | 0.0820 ± 0.0246 |        5 |
| field4_banana  | resnet50  | cls       | linear |    nan | 0.9880 ± 0.0000 | 0.9880 ± 0.0000 | 0.0120 ± 0.0000 |        1 |
| field4_banana  | resnet50  | cls       | proto  |      1 | 0.8212 ± 0.0448 | 0.8181 ± 0.0462 | 0.1788 ± 0.0448 |        5 |
| field4_banana  | resnet50  | cls       | proto  |      5 | 0.8212 ± 0.0397 | 0.8167 ± 0.0440 | 0.1788 ± 0.0397 |        5 |
| field4_banana  | resnet50  | cls       | proto  |     10 | 0.7980 ± 0.1099 | 0.7908 ± 0.1194 | 0.2020 ± 0.1099 |        5 |
| field4_banana  | resnet50  | cls       | proto  |     50 | 0.8328 ± 0.0346 | 0.8295 ± 0.0379 | 0.1672 ± 0.0346 |        5 |
| field4_banana  | resnet50  | cls       | proto  |    nan | 0.8560 ± 0.0000 | 0.8547 ± 0.0000 | 0.1440 ± 0.0000 |        1 |
| field4_mango   | clip_b    | cls       | corn   |      1 | 0.7556 ± 0.0518 | 0.7469 ± 0.0577 | 0.2444 ± 0.0518 |        5 |
| field4_mango   | clip_b    | cls       | corn   |      5 | 0.9456 ± 0.0221 | 0.9455 ± 0.0221 | 0.0544 ± 0.0221 |        5 |
| field4_mango   | clip_b    | cls       | corn   |     10 | 0.9696 ± 0.0231 | 0.9695 ± 0.0232 | 0.0304 ± 0.0231 |        5 |
| field4_mango   | clip_b    | cls       | corn   |     50 | 0.9960 ± 0.0055 | 0.9960 ± 0.0055 | 0.0040 ± 0.0055 |        5 |
| field4_mango   | clip_b    | cls       | corn   |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_mango   | clip_b    | cls       | linear |      1 | 0.7556 ± 0.0518 | 0.7469 ± 0.0577 | 0.2444 ± 0.0518 |        5 |
| field4_mango   | clip_b    | cls       | linear |      5 | 0.9456 ± 0.0221 | 0.9455 ± 0.0221 | 0.0544 ± 0.0221 |        5 |
| field4_mango   | clip_b    | cls       | linear |     10 | 0.9696 ± 0.0231 | 0.9695 ± 0.0232 | 0.0304 ± 0.0231 |        5 |
| field4_mango   | clip_b    | cls       | linear |     50 | 0.9960 ± 0.0055 | 0.9960 ± 0.0055 | 0.0040 ± 0.0055 |        5 |
| field4_mango   | clip_b    | cls       | linear |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_mango   | clip_b    | cls       | proto  |      1 | 0.7556 ± 0.0518 | 0.7469 ± 0.0577 | 0.2444 ± 0.0518 |        5 |
| field4_mango   | clip_b    | cls       | proto  |      5 | 0.9392 ± 0.0230 | 0.9391 ± 0.0230 | 0.0608 ± 0.0230 |        5 |
| field4_mango   | clip_b    | cls       | proto  |     10 | 0.9620 ± 0.0329 | 0.9618 ± 0.0331 | 0.0380 ± 0.0329 |        5 |
| field4_mango   | clip_b    | cls       | proto  |     50 | 0.9940 ± 0.0068 | 0.9940 ± 0.0068 | 0.0060 ± 0.0068 |        5 |
| field4_mango   | clip_b    | cls       | proto  |    nan | 0.9980 ± 0.0000 | 0.9980 ± 0.0000 | 0.0020 ± 0.0000 |        1 |
| field4_mango   | clip_b    | mean      | linear |      1 | 0.6907 ± 0.0934 | 0.6689 ± 0.1163 | 0.3093 ± 0.0934 |        3 |
| field4_mango   | clip_b    | mean      | linear |      5 | 0.7400 ± 0.1626 | 0.7075 ± 0.2080 | 0.2600 ± 0.1626 |        3 |
| field4_mango   | clip_b    | mean      | linear |     10 | 0.9033 ± 0.0590 | 0.9019 ± 0.0614 | 0.0967 ± 0.0590 |        3 |
| field4_mango   | clip_b    | mean      | linear |     50 | 0.9333 ± 0.0237 | 0.9330 ± 0.0241 | 0.0667 ± 0.0237 |        3 |
| field4_mango   | clip_b    | mean      | linear |    nan | 0.9860 ± 0.0000 | 0.9860 ± 0.0000 | 0.0140 ± 0.0000 |        1 |
| field4_mango   | clip_b    | mean      | proto  |      1 | 0.6907 ± 0.0934 | 0.6689 ± 0.1163 | 0.3093 ± 0.0934 |        3 |
| field4_mango   | clip_b    | mean      | proto  |      5 | 0.7313 ± 0.1623 | 0.6966 ± 0.2095 | 0.2687 ± 0.1623 |        3 |
| field4_mango   | clip_b    | mean      | proto  |     10 | 0.8887 ± 0.0733 | 0.8861 ± 0.0776 | 0.1113 ± 0.0733 |        3 |
| field4_mango   | clip_b    | mean      | proto  |     50 | 0.8920 ± 0.0750 | 0.8893 ± 0.0793 | 0.1080 ± 0.0750 |        3 |
| field4_mango   | clip_b    | mean      | proto  |    nan | 0.9080 ± 0.0000 | 0.9072 ± 0.0000 | 0.0920 ± 0.0000 |        1 |
| field4_mango   | dinov2_b  | cls       | corn   |      1 | 0.8604 ± 0.1664 | 0.8513 ± 0.1829 | 0.1396 ± 0.1664 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |      5 | 0.9872 ± 0.0166 | 0.9872 ± 0.0166 | 0.0128 ± 0.0166 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |     10 | 0.9964 ± 0.0038 | 0.9964 ± 0.0038 | 0.0036 ± 0.0038 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |     50 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_mango   | dinov2_b  | cls       | linear |      1 | 0.8604 ± 0.1664 | 0.8513 ± 0.1829 | 0.1396 ± 0.1664 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |      5 | 0.9872 ± 0.0166 | 0.9872 ± 0.0166 | 0.0128 ± 0.0166 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |     10 | 0.9964 ± 0.0038 | 0.9964 ± 0.0038 | 0.0036 ± 0.0038 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |     50 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_mango   | dinov2_b  | cls       | proto  |      1 | 0.8604 ± 0.1664 | 0.8513 ± 0.1829 | 0.1396 ± 0.1664 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |      5 | 0.9844 ± 0.0144 | 0.9844 ± 0.0145 | 0.0156 ± 0.0144 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |     10 | 0.9964 ± 0.0026 | 0.9964 ± 0.0026 | 0.0036 ± 0.0026 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |     50 | 0.9996 ± 0.0009 | 0.9996 ± 0.0009 | 0.0004 ± 0.0009 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_mango   | dinov2_b  | mean      | linear |      1 | 0.6433 ± 0.1570 | 0.6012 ± 0.1916 | 0.3567 ± 0.1570 |        3 |
| field4_mango   | dinov2_b  | mean      | linear |      5 | 0.7013 ± 0.0611 | 0.6972 ± 0.0657 | 0.2987 ± 0.0611 |        3 |
| field4_mango   | dinov2_b  | mean      | linear |     10 | 0.7947 ± 0.0384 | 0.7926 ± 0.0375 | 0.2053 ± 0.0384 |        3 |
| field4_mango   | dinov2_b  | mean      | linear |     50 | 0.8873 ± 0.0358 | 0.8858 ± 0.0377 | 0.1127 ± 0.0358 |        3 |
| field4_mango   | dinov2_b  | mean      | linear |    nan | 0.9840 ± 0.0000 | 0.9840 ± 0.0000 | 0.0160 ± 0.0000 |        1 |
| field4_mango   | dinov2_b  | mean      | proto  |      1 | 0.6433 ± 0.1570 | 0.6012 ± 0.1916 | 0.3567 ± 0.1570 |        3 |
| field4_mango   | dinov2_b  | mean      | proto  |      5 | 0.6893 ± 0.0237 | 0.6821 ± 0.0228 | 0.3107 ± 0.0237 |        3 |
| field4_mango   | dinov2_b  | mean      | proto  |     10 | 0.8113 ± 0.0375 | 0.8092 ± 0.0385 | 0.1887 ± 0.0375 |        3 |
| field4_mango   | dinov2_b  | mean      | proto  |     50 | 0.8407 ± 0.0813 | 0.8341 ± 0.0904 | 0.1593 ± 0.0813 |        3 |
| field4_mango   | dinov2_b  | mean      | proto  |    nan | 0.8460 ± 0.0000 | 0.8423 ± 0.0000 | 0.1540 ± 0.0000 |        1 |
| field4_mango   | dinov2_s  | cls       | corn   |      1 | 0.8200 ± 0.1038 | 0.8190 ± 0.1036 | 0.1800 ± 0.1038 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |      5 | 0.9664 ± 0.0267 | 0.9664 ± 0.0267 | 0.0336 ± 0.0267 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |     10 | 0.9912 ± 0.0064 | 0.9912 ± 0.0064 | 0.0088 ± 0.0064 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |     50 | 0.9992 ± 0.0011 | 0.9992 ± 0.0011 | 0.0008 ± 0.0011 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_mango   | dinov2_s  | cls       | linear |      1 | 0.8200 ± 0.1038 | 0.8190 ± 0.1036 | 0.1800 ± 0.1038 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |      5 | 0.9664 ± 0.0267 | 0.9664 ± 0.0267 | 0.0336 ± 0.0267 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |     10 | 0.9912 ± 0.0064 | 0.9912 ± 0.0064 | 0.0088 ± 0.0064 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |     50 | 0.9992 ± 0.0011 | 0.9992 ± 0.0011 | 0.0008 ± 0.0011 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 |        1 |
| field4_mango   | dinov2_s  | cls       | proto  |      1 | 0.8200 ± 0.1038 | 0.8190 ± 0.1036 | 0.1800 ± 0.1038 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |      5 | 0.9720 ± 0.0187 | 0.9720 ± 0.0187 | 0.0280 ± 0.0187 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |     10 | 0.9912 ± 0.0064 | 0.9912 ± 0.0064 | 0.0088 ± 0.0064 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |     50 | 0.9988 ± 0.0011 | 0.9988 ± 0.0011 | 0.0012 ± 0.0011 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |    nan | 0.9960 ± 0.0000 | 0.9960 ± 0.0000 | 0.0040 ± 0.0000 |        1 |
| field4_mango   | dinov2_s  | mean      | linear |      1 | 0.5927 ± 0.0241 | 0.5562 ± 0.0577 | 0.4073 ± 0.0241 |        3 |
| field4_mango   | dinov2_s  | mean      | linear |      5 | 0.7467 ± 0.1331 | 0.7352 ± 0.1478 | 0.2533 ± 0.1331 |        3 |
| field4_mango   | dinov2_s  | mean      | linear |     10 | 0.8353 ± 0.0234 | 0.8343 ± 0.0224 | 0.1647 ± 0.0234 |        3 |
| field4_mango   | dinov2_s  | mean      | linear |     50 | 0.9193 ± 0.0130 | 0.9189 ± 0.0134 | 0.0807 ± 0.0130 |        3 |
| field4_mango   | dinov2_s  | mean      | linear |    nan | 0.9980 ± 0.0000 | 0.9980 ± 0.0000 | 0.0020 ± 0.0000 |        1 |
| field4_mango   | dinov2_s  | mean      | proto  |      1 | 0.5927 ± 0.0241 | 0.5562 ± 0.0577 | 0.4073 ± 0.0241 |        3 |
| field4_mango   | dinov2_s  | mean      | proto  |      5 | 0.7107 ± 0.0755 | 0.6985 ± 0.0845 | 0.2893 ± 0.0755 |        3 |
| field4_mango   | dinov2_s  | mean      | proto  |     10 | 0.8353 ± 0.0276 | 0.8338 ± 0.0275 | 0.1647 ± 0.0276 |        3 |
| field4_mango   | dinov2_s  | mean      | proto  |     50 | 0.8527 ± 0.0533 | 0.8486 ± 0.0577 | 0.1473 ± 0.0533 |        3 |
| field4_mango   | dinov2_s  | mean      | proto  |    nan | 0.8620 ± 0.0000 | 0.8593 ± 0.0000 | 0.1380 ± 0.0000 |        1 |
| field4_mango   | resnet50  | cls       | corn   |      1 | 0.7308 ± 0.1264 | 0.7115 ± 0.1514 | 0.2692 ± 0.1264 |        5 |
| field4_mango   | resnet50  | cls       | corn   |      5 | 0.9260 ± 0.0442 | 0.9258 ± 0.0444 | 0.0740 ± 0.0442 |        5 |
| field4_mango   | resnet50  | cls       | corn   |     10 | 0.9632 ± 0.0323 | 0.9631 ± 0.0325 | 0.0368 ± 0.0323 |        5 |
| field4_mango   | resnet50  | cls       | corn   |     50 | 0.9884 ± 0.0074 | 0.9884 ± 0.0074 | 0.0116 ± 0.0074 |        5 |
| field4_mango   | resnet50  | cls       | corn   |    nan | 0.9980 ± 0.0000 | 0.9980 ± 0.0000 | 0.0020 ± 0.0000 |        1 |
| field4_mango   | resnet50  | cls       | linear |      1 | 0.7308 ± 0.1264 | 0.7115 ± 0.1514 | 0.2692 ± 0.1264 |        5 |
| field4_mango   | resnet50  | cls       | linear |      5 | 0.9260 ± 0.0442 | 0.9258 ± 0.0444 | 0.0740 ± 0.0442 |        5 |
| field4_mango   | resnet50  | cls       | linear |     10 | 0.9632 ± 0.0323 | 0.9631 ± 0.0325 | 0.0368 ± 0.0323 |        5 |
| field4_mango   | resnet50  | cls       | linear |     50 | 0.9884 ± 0.0074 | 0.9884 ± 0.0074 | 0.0116 ± 0.0074 |        5 |
| field4_mango   | resnet50  | cls       | linear |    nan | 0.9980 ± 0.0000 | 0.9980 ± 0.0000 | 0.0020 ± 0.0000 |        1 |
| field4_mango   | resnet50  | cls       | proto  |      1 | 0.7308 ± 0.1264 | 0.7115 ± 0.1514 | 0.2692 ± 0.1264 |        5 |
| field4_mango   | resnet50  | cls       | proto  |      5 | 0.8980 ± 0.0638 | 0.8969 ± 0.0650 | 0.1020 ± 0.0638 |        5 |
| field4_mango   | resnet50  | cls       | proto  |     10 | 0.9544 ± 0.0442 | 0.9540 ± 0.0449 | 0.0456 ± 0.0442 |        5 |
| field4_mango   | resnet50  | cls       | proto  |     50 | 0.9700 ± 0.0130 | 0.9700 ± 0.0131 | 0.0300 ± 0.0130 |        5 |
| field4_mango   | resnet50  | cls       | proto  |    nan | 0.9900 ± 0.0000 | 0.9900 ± 0.0000 | 0.0100 ± 0.0000 |        1 |
| fruit12_apple  | clip_b    | cls       | corn   |      1 | 0.3906 ± 0.0646 | 0.3601 ± 0.0773 | 0.4604 ± 0.0588 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |      5 | 0.4632 ± 0.0572 | 0.4443 ± 0.0774 | 0.4594 ± 0.0561 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |     10 | 0.5170 ± 0.0463 | 0.5102 ± 0.0492 | 0.4038 ± 0.0486 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |     50 | 0.6406 ± 0.0342 | 0.6392 ± 0.0372 | 0.2925 ± 0.0256 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |    nan | 0.7972 ± 0.0000 | 0.7764 ± 0.0000 | 0.1698 ± 0.0000 |        1 |
| fruit12_apple  | clip_b    | cls       | linear |      1 | 0.3811 ± 0.0694 | 0.3533 ± 0.0812 | 0.4651 ± 0.0577 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |      5 | 0.4736 ± 0.0611 | 0.4540 ± 0.0805 | 0.4491 ± 0.0619 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |     10 | 0.5302 ± 0.0495 | 0.5219 ± 0.0526 | 0.3877 ± 0.0505 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |     50 | 0.6547 ± 0.0293 | 0.6536 ± 0.0315 | 0.2877 ± 0.0105 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |    nan | 0.8302 ± 0.0000 | 0.8163 ± 0.0000 | 0.1462 ± 0.0000 |        1 |
| fruit12_apple  | clip_b    | cls       | proto  |      1 | 0.3943 ± 0.0625 | 0.3625 ± 0.0761 | 0.4566 ± 0.0656 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |      5 | 0.4538 ± 0.0619 | 0.4338 ± 0.0830 | 0.4679 ± 0.0623 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |     10 | 0.4925 ± 0.0330 | 0.4796 ± 0.0288 | 0.4283 ± 0.0220 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |     50 | 0.5953 ± 0.0333 | 0.5960 ± 0.0328 | 0.3425 ± 0.0451 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |    nan | 0.6321 ± 0.0000 | 0.6281 ± 0.0000 | 0.2972 ± 0.0000 |        1 |
| fruit12_apple  | clip_b    | mean      | linear |      1 | 0.4182 ± 0.0477 | 0.3671 ± 0.0800 | 0.4638 ± 0.0563 |        3 |
| fruit12_apple  | clip_b    | mean      | linear |      5 | 0.4654 ± 0.0567 | 0.4314 ± 0.0979 | 0.4198 ± 0.0826 |        3 |
| fruit12_apple  | clip_b    | mean      | linear |     10 | 0.5833 ± 0.0628 | 0.5752 ± 0.0652 | 0.3616 ± 0.0547 |        3 |
| fruit12_apple  | clip_b    | mean      | linear |     50 | 0.7044 ± 0.0179 | 0.7027 ± 0.0245 | 0.2563 ± 0.0191 |        3 |
| fruit12_apple  | clip_b    | mean      | linear |    nan | 0.8255 ± 0.0000 | 0.8067 ± 0.0000 | 0.1462 ± 0.0000 |        1 |
| fruit12_apple  | clip_b    | mean      | proto  |      1 | 0.4088 ± 0.0396 | 0.3602 ± 0.0793 | 0.4481 ± 0.0510 |        3 |
| fruit12_apple  | clip_b    | mean      | proto  |      5 | 0.4355 ± 0.0484 | 0.4130 ± 0.0679 | 0.4214 ± 0.0504 |        3 |
| fruit12_apple  | clip_b    | mean      | proto  |     10 | 0.5377 ± 0.0617 | 0.5258 ± 0.0710 | 0.4057 ± 0.0425 |        3 |
| fruit12_apple  | clip_b    | mean      | proto  |     50 | 0.6274 ± 0.0250 | 0.6271 ± 0.0253 | 0.3365 ± 0.0237 |        3 |
| fruit12_apple  | clip_b    | mean      | proto  |    nan | 0.6557 ± 0.0000 | 0.6451 ± 0.0000 | 0.3019 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_b  | cls       | corn   |      1 | 0.4604 ± 0.1063 | 0.3895 ± 0.1155 | 0.4179 ± 0.0617 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |      5 | 0.5849 ± 0.0715 | 0.5647 ± 0.0897 | 0.3481 ± 0.0440 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |     10 | 0.6462 ± 0.0304 | 0.6391 ± 0.0251 | 0.2934 ± 0.0181 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |     50 | 0.7434 ± 0.0190 | 0.7365 ± 0.0204 | 0.2189 ± 0.0098 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |    nan | 0.8255 ± 0.0000 | 0.8103 ± 0.0000 | 0.1509 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_b  | cls       | linear |      1 | 0.4415 ± 0.1057 | 0.3736 ± 0.1250 | 0.4170 ± 0.0549 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |      5 | 0.5764 ± 0.0657 | 0.5591 ± 0.0764 | 0.3509 ± 0.0404 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |     10 | 0.6528 ± 0.0288 | 0.6463 ± 0.0272 | 0.2802 ± 0.0109 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |     50 | 0.7519 ± 0.0244 | 0.7492 ± 0.0253 | 0.2132 ± 0.0178 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |    nan | 0.8349 ± 0.0000 | 0.8216 ± 0.0000 | 0.1321 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_b  | cls       | proto  |      1 | 0.4377 ± 0.1110 | 0.3602 ± 0.1208 | 0.4132 ± 0.0579 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |      5 | 0.5585 ± 0.0813 | 0.5427 ± 0.0887 | 0.3604 ± 0.0381 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |     10 | 0.5981 ± 0.0391 | 0.5932 ± 0.0401 | 0.3274 ± 0.0371 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |     50 | 0.7028 ± 0.0322 | 0.6965 ± 0.0343 | 0.2528 ± 0.0240 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |    nan | 0.7547 ± 0.0000 | 0.7430 ± 0.0000 | 0.2123 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_b  | mean      | linear |      1 | 0.4544 ± 0.0144 | 0.3913 ± 0.0648 | 0.4167 ± 0.0722 |        3 |
| fruit12_apple  | dinov2_b  | mean      | linear |      5 | 0.5252 ± 0.0633 | 0.5082 ± 0.0907 | 0.4167 ± 0.0706 |        3 |
| fruit12_apple  | dinov2_b  | mean      | linear |     10 | 0.6557 ± 0.0544 | 0.6498 ± 0.0630 | 0.3145 ± 0.0465 |        3 |
| fruit12_apple  | dinov2_b  | mean      | linear |     50 | 0.7563 ± 0.0196 | 0.7527 ± 0.0220 | 0.2091 ± 0.0136 |        3 |
| fruit12_apple  | dinov2_b  | mean      | linear |    nan | 0.8113 ± 0.0000 | 0.7945 ± 0.0000 | 0.1604 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_b  | mean      | proto  |      1 | 0.4371 ± 0.0191 | 0.3673 ± 0.0887 | 0.4135 ± 0.0757 |        3 |
| fruit12_apple  | dinov2_b  | mean      | proto  |      5 | 0.4701 ± 0.0893 | 0.4572 ± 0.1142 | 0.4261 ± 0.0640 |        3 |
| fruit12_apple  | dinov2_b  | mean      | proto  |     10 | 0.6148 ± 0.0654 | 0.6080 ± 0.0722 | 0.3553 ± 0.0559 |        3 |
| fruit12_apple  | dinov2_b  | mean      | proto  |     50 | 0.6965 ± 0.0179 | 0.6997 ± 0.0201 | 0.2767 ± 0.0144 |        3 |
| fruit12_apple  | dinov2_b  | mean      | proto  |    nan | 0.6981 ± 0.0000 | 0.6942 ± 0.0000 | 0.2689 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_s  | cls       | corn   |      1 | 0.4830 ± 0.0618 | 0.4226 ± 0.0805 | 0.3991 ± 0.0752 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |      5 | 0.5943 ± 0.0920 | 0.5645 ± 0.1164 | 0.3377 ± 0.0757 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |     10 | 0.6604 ± 0.0345 | 0.6559 ± 0.0316 | 0.2783 ± 0.0328 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |     50 | 0.7500 ± 0.0229 | 0.7461 ± 0.0231 | 0.2170 ± 0.0180 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |    nan | 0.8160 ± 0.0000 | 0.8052 ± 0.0000 | 0.1698 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_s  | cls       | linear |      1 | 0.4764 ± 0.0711 | 0.4178 ± 0.0937 | 0.4009 ± 0.0809 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |      5 | 0.5792 ± 0.0881 | 0.5537 ± 0.1055 | 0.3377 ± 0.0583 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |     10 | 0.6651 ± 0.0325 | 0.6603 ± 0.0301 | 0.2660 ± 0.0144 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |     50 | 0.7528 ± 0.0159 | 0.7477 ± 0.0156 | 0.2057 ± 0.0148 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |    nan | 0.8160 ± 0.0000 | 0.8069 ± 0.0000 | 0.1698 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_s  | cls       | proto  |      1 | 0.4708 ± 0.1051 | 0.4072 ± 0.1040 | 0.3962 ± 0.0798 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |      5 | 0.5830 ± 0.0982 | 0.5572 ± 0.1136 | 0.3434 ± 0.0720 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |     10 | 0.6283 ± 0.0297 | 0.6239 ± 0.0302 | 0.3113 ± 0.0406 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |     50 | 0.7009 ± 0.0317 | 0.6960 ± 0.0306 | 0.2557 ± 0.0278 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |    nan | 0.7406 ± 0.0000 | 0.7325 ± 0.0000 | 0.2217 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_s  | mean      | linear |      1 | 0.4245 ± 0.0216 | 0.3775 ± 0.0442 | 0.4418 ± 0.0651 |        3 |
| fruit12_apple  | dinov2_s  | mean      | linear |      5 | 0.5519 ± 0.1024 | 0.5188 ± 0.1323 | 0.3884 ± 0.0865 |        3 |
| fruit12_apple  | dinov2_s  | mean      | linear |     10 | 0.6761 ± 0.0407 | 0.6676 ± 0.0373 | 0.2830 ± 0.0638 |        3 |
| fruit12_apple  | dinov2_s  | mean      | linear |     50 | 0.7531 ± 0.0054 | 0.7463 ± 0.0077 | 0.2044 ± 0.0223 |        3 |
| fruit12_apple  | dinov2_s  | mean      | linear |    nan | 0.8160 ± 0.0000 | 0.8023 ± 0.0000 | 0.1557 ± 0.0000 |        1 |
| fruit12_apple  | dinov2_s  | mean      | proto  |      1 | 0.4245 ± 0.0047 | 0.3783 ± 0.0514 | 0.4434 ± 0.0772 |        3 |
| fruit12_apple  | dinov2_s  | mean      | proto  |      5 | 0.5110 ± 0.1450 | 0.4823 ± 0.1744 | 0.3978 ± 0.0798 |        3 |
| fruit12_apple  | dinov2_s  | mean      | proto  |     10 | 0.6211 ± 0.0710 | 0.6123 ± 0.0732 | 0.3302 ± 0.0835 |        3 |
| fruit12_apple  | dinov2_s  | mean      | proto  |     50 | 0.6950 ± 0.0213 | 0.6867 ± 0.0241 | 0.2484 ± 0.0119 |        3 |
| fruit12_apple  | dinov2_s  | mean      | proto  |    nan | 0.6934 ± 0.0000 | 0.6821 ± 0.0000 | 0.2358 ± 0.0000 |        1 |
| fruit12_apple  | resnet50  | cls       | corn   |      1 | 0.3811 ± 0.1027 | 0.3463 ± 0.1284 | 0.4670 ± 0.0552 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |      5 | 0.5245 ± 0.0806 | 0.5089 ± 0.1076 | 0.4009 ± 0.0681 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |     10 | 0.6208 ± 0.0230 | 0.6231 ± 0.0217 | 0.3075 ± 0.0143 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |     50 | 0.6962 ± 0.0159 | 0.6923 ± 0.0131 | 0.2538 ± 0.0339 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |    nan | 0.8113 ± 0.0000 | 0.7956 ± 0.0000 | 0.1557 ± 0.0000 |        1 |
| fruit12_apple  | resnet50  | cls       | linear |      1 | 0.3519 ± 0.0888 | 0.3210 ± 0.1118 | 0.4726 ± 0.0570 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |      5 | 0.5396 ± 0.0770 | 0.5246 ± 0.1034 | 0.3840 ± 0.0626 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |     10 | 0.6255 ± 0.0310 | 0.6271 ± 0.0287 | 0.3047 ± 0.0169 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |     50 | 0.7094 ± 0.0228 | 0.7061 ± 0.0243 | 0.2406 ± 0.0238 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |    nan | 0.8491 ± 0.0000 | 0.8348 ± 0.0000 | 0.1132 ± 0.0000 |        1 |
| fruit12_apple  | resnet50  | cls       | proto  |      1 | 0.3708 ± 0.1042 | 0.3398 ± 0.1178 | 0.4670 ± 0.0598 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |      5 | 0.4925 ± 0.0937 | 0.4813 ± 0.1108 | 0.4311 ± 0.0746 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |     10 | 0.5962 ± 0.0599 | 0.5978 ± 0.0567 | 0.3179 ± 0.0266 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |     50 | 0.6755 ± 0.0656 | 0.6768 ± 0.0542 | 0.2755 ± 0.0686 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |    nan | 0.7453 ± 0.0000 | 0.7362 ± 0.0000 | 0.2075 ± 0.0000 |        1 |
| fruit12_banana | clip_b    | cls       | corn   |      1 | 0.3904 ± 0.0633 | 0.3286 ± 0.0412 | 0.5181 ± 0.0589 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |      5 | 0.4915 ± 0.0470 | 0.4079 ± 0.0412 | 0.4441 ± 0.0431 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |     10 | 0.5744 ± 0.0856 | 0.4767 ± 0.0673 | 0.3643 ± 0.0774 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |     50 | 0.7461 ± 0.0349 | 0.6366 ± 0.0261 | 0.2237 ± 0.0304 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |    nan | 0.8994 ± 0.0000 | 0.7196 ± 0.0000 | 0.0898 ± 0.0000 |        1 |
| fruit12_banana | clip_b    | cls       | linear |      1 | 0.3794 ± 0.0934 | 0.3195 ± 0.0607 | 0.5257 ± 0.0780 |        5 |
| fruit12_banana | clip_b    | cls       | linear |      5 | 0.5071 ± 0.0519 | 0.4188 ± 0.0396 | 0.4295 ± 0.0526 |        5 |
| fruit12_banana | clip_b    | cls       | linear |     10 | 0.6074 ± 0.0682 | 0.4972 ± 0.0511 | 0.3291 ± 0.0599 |        5 |
| fruit12_banana | clip_b    | cls       | linear |     50 | 0.7646 ± 0.0344 | 0.6570 ± 0.0253 | 0.2067 ± 0.0300 |        5 |
| fruit12_banana | clip_b    | cls       | linear |    nan | 0.9162 ± 0.0000 | 0.7832 ± 0.0000 | 0.0707 ± 0.0000 |        1 |
| fruit12_banana | clip_b    | cls       | proto  |      1 | 0.4034 ± 0.0726 | 0.3346 ± 0.0467 | 0.5023 ± 0.0640 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |      5 | 0.4826 ± 0.0339 | 0.4029 ± 0.0364 | 0.4493 ± 0.0392 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |     10 | 0.5437 ± 0.0915 | 0.4521 ± 0.0677 | 0.3904 ± 0.0779 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |     50 | 0.7236 ± 0.0322 | 0.6146 ± 0.0143 | 0.2434 ± 0.0378 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |    nan | 0.7042 ± 0.0000 | 0.6028 ± 0.0000 | 0.2323 ± 0.0000 |        1 |
| fruit12_banana | clip_b    | mean      | linear |      1 | 0.3820 ± 0.0809 | 0.3354 ± 0.0682 | 0.5477 ± 0.0525 |        3 |
| fruit12_banana | clip_b    | mean      | linear |      5 | 0.4862 ± 0.0249 | 0.4179 ± 0.0133 | 0.4563 ± 0.0578 |        3 |
| fruit12_banana | clip_b    | mean      | linear |     10 | 0.5729 ± 0.0702 | 0.4824 ± 0.0504 | 0.3828 ± 0.0695 |        3 |
| fruit12_banana | clip_b    | mean      | linear |     50 | 0.7098 ± 0.0220 | 0.6221 ± 0.0127 | 0.2579 ± 0.0236 |        3 |
| fruit12_banana | clip_b    | mean      | linear |    nan | 0.9114 ± 0.0000 | 0.7639 ± 0.0000 | 0.0790 ± 0.0000 |        1 |
| fruit12_banana | clip_b    | mean      | proto  |      1 | 0.3749 ± 0.0744 | 0.3302 ± 0.0603 | 0.5533 ± 0.0429 |        3 |
| fruit12_banana | clip_b    | mean      | proto  |      5 | 0.4731 ± 0.0332 | 0.4085 ± 0.0222 | 0.4707 ± 0.0572 |        3 |
| fruit12_banana | clip_b    | mean      | proto  |     10 | 0.5641 ± 0.0853 | 0.4741 ± 0.0609 | 0.3924 ± 0.0842 |        3 |
| fruit12_banana | clip_b    | mean      | proto  |     50 | 0.5868 ± 0.0322 | 0.5171 ± 0.0337 | 0.3725 ± 0.0240 |        3 |
| fruit12_banana | clip_b    | mean      | proto  |    nan | 0.5820 ± 0.0000 | 0.5081 ± 0.0000 | 0.3497 ± 0.0000 |        1 |
| fruit12_banana | dinov2_b  | cls       | corn   |      1 | 0.4726 ± 0.1549 | 0.3900 ± 0.1170 | 0.4577 ± 0.1434 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |      5 | 0.6326 ± 0.1080 | 0.5357 ± 0.0804 | 0.3222 ± 0.0942 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |     10 | 0.7234 ± 0.0463 | 0.6024 ± 0.0451 | 0.2256 ± 0.0526 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |     50 | 0.8402 ± 0.0166 | 0.7280 ± 0.0200 | 0.1303 ± 0.0124 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |    nan | 0.9293 ± 0.0000 | 0.7927 ± 0.0000 | 0.0563 ± 0.0000 |        1 |
| fruit12_banana | dinov2_b  | cls       | linear |      1 | 0.4704 ± 0.1531 | 0.3874 ± 0.1237 | 0.4632 ± 0.1504 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |      5 | 0.6572 ± 0.1149 | 0.5541 ± 0.0847 | 0.2949 ± 0.0940 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |     10 | 0.7435 ± 0.0420 | 0.6217 ± 0.0348 | 0.2057 ± 0.0498 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |     50 | 0.8594 ± 0.0113 | 0.7497 ± 0.0152 | 0.1128 ± 0.0060 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |    nan | 0.9341 ± 0.0000 | 0.8187 ± 0.0000 | 0.0479 ± 0.0000 |        1 |
| fruit12_banana | dinov2_b  | cls       | proto  |      1 | 0.4687 ± 0.1393 | 0.3854 ± 0.1019 | 0.4589 ± 0.1363 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |      5 | 0.6218 ± 0.0999 | 0.5262 ± 0.0750 | 0.3293 ± 0.0897 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |     10 | 0.7224 ± 0.0597 | 0.5980 ± 0.0632 | 0.2287 ± 0.0673 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |     50 | 0.8098 ± 0.0226 | 0.6859 ± 0.0215 | 0.1497 ± 0.0252 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |    nan | 0.8132 ± 0.0000 | 0.6829 ± 0.0000 | 0.1413 ± 0.0000 |        1 |
| fruit12_banana | dinov2_b  | mean      | linear |      1 | 0.4411 ± 0.0785 | 0.3787 ± 0.0753 | 0.4978 ± 0.0675 |        3 |
| fruit12_banana | dinov2_b  | mean      | linear |      5 | 0.5737 ± 0.0498 | 0.5061 ± 0.0273 | 0.3697 ± 0.0276 |        3 |
| fruit12_banana | dinov2_b  | mean      | linear |     10 | 0.7393 ± 0.0339 | 0.6295 ± 0.0314 | 0.2176 ± 0.0301 |        3 |
| fruit12_banana | dinov2_b  | mean      | linear |     50 | 0.8367 ± 0.0073 | 0.7317 ± 0.0075 | 0.1353 ± 0.0043 |        3 |
| fruit12_banana | dinov2_b  | mean      | linear |    nan | 0.9425 ± 0.0000 | 0.8628 ± 0.0000 | 0.0479 ± 0.0000 |        1 |
| fruit12_banana | dinov2_b  | mean      | proto  |      1 | 0.4036 ± 0.1367 | 0.3558 ± 0.0873 | 0.5253 ± 0.0951 |        3 |
| fruit12_banana | dinov2_b  | mean      | proto  |      5 | 0.5836 ± 0.0218 | 0.5110 ± 0.0104 | 0.3733 ± 0.0301 |        3 |
| fruit12_banana | dinov2_b  | mean      | proto  |     10 | 0.7441 ± 0.0452 | 0.6199 ± 0.0516 | 0.2192 ± 0.0374 |        3 |
| fruit12_banana | dinov2_b  | mean      | proto  |     50 | 0.7645 ± 0.0038 | 0.6556 ± 0.0056 | 0.1872 ± 0.0111 |        3 |
| fruit12_banana | dinov2_b  | mean      | proto  |    nan | 0.7689 ± 0.0000 | 0.6557 ± 0.0000 | 0.1725 ± 0.0000 |        1 |
| fruit12_banana | dinov2_s  | cls       | corn   |      1 | 0.4532 ± 0.1192 | 0.3803 ± 0.0881 | 0.4869 ± 0.1086 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |      5 | 0.6572 ± 0.1065 | 0.5643 ± 0.0846 | 0.3107 ± 0.0883 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |     10 | 0.7269 ± 0.0492 | 0.6113 ± 0.0468 | 0.2376 ± 0.0516 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |     50 | 0.8156 ± 0.0263 | 0.7191 ± 0.0288 | 0.1617 ± 0.0215 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |    nan | 0.9269 ± 0.0000 | 0.8308 ± 0.0000 | 0.0671 ± 0.0000 |        1 |
| fruit12_banana | dinov2_s  | cls       | linear |      1 | 0.4398 ± 0.1207 | 0.3711 ± 0.0984 | 0.5001 ± 0.1116 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |      5 | 0.6783 ± 0.1168 | 0.5841 ± 0.0918 | 0.2886 ± 0.0953 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |     10 | 0.7411 ± 0.0693 | 0.6277 ± 0.0545 | 0.2244 ± 0.0683 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |     50 | 0.8419 ± 0.0222 | 0.7459 ± 0.0244 | 0.1363 ± 0.0202 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |    nan | 0.9425 ± 0.0000 | 0.8814 ± 0.0000 | 0.0515 ± 0.0000 |        1 |
| fruit12_banana | dinov2_s  | cls       | proto  |      1 | 0.4469 ± 0.1172 | 0.3785 ± 0.0946 | 0.4949 ± 0.1159 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |      5 | 0.6484 ± 0.0982 | 0.5519 ± 0.0735 | 0.3169 ± 0.0823 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |     10 | 0.7298 ± 0.0586 | 0.6126 ± 0.0621 | 0.2381 ± 0.0598 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |     50 | 0.7983 ± 0.0282 | 0.6971 ± 0.0349 | 0.1775 ± 0.0171 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |    nan | 0.7952 ± 0.0000 | 0.6894 ± 0.0000 | 0.1760 ± 0.0000 |        1 |
| fruit12_banana | dinov2_s  | mean      | linear |      1 | 0.4467 ± 0.0396 | 0.3735 ± 0.0378 | 0.4942 ± 0.0218 |        3 |
| fruit12_banana | dinov2_s  | mean      | linear |      5 | 0.5760 ± 0.0965 | 0.5119 ± 0.0675 | 0.3796 ± 0.0690 |        3 |
| fruit12_banana | dinov2_s  | mean      | linear |     10 | 0.6647 ± 0.0258 | 0.5743 ± 0.0225 | 0.3018 ± 0.0247 |        3 |
| fruit12_banana | dinov2_s  | mean      | linear |     50 | 0.7956 ± 0.0080 | 0.6996 ± 0.0088 | 0.1768 ± 0.0037 |        3 |
| fruit12_banana | dinov2_s  | mean      | linear |    nan | 0.9473 ± 0.0000 | 0.8914 ± 0.0000 | 0.0455 ± 0.0000 |        1 |
| fruit12_banana | dinov2_s  | mean      | proto  |      1 | 0.4323 ± 0.0527 | 0.3704 ± 0.0549 | 0.5078 ± 0.0475 |        3 |
| fruit12_banana | dinov2_s  | mean      | proto  |      5 | 0.5856 ± 0.0607 | 0.5174 ± 0.0508 | 0.3709 ± 0.0323 |        3 |
| fruit12_banana | dinov2_s  | mean      | proto  |     10 | 0.6607 ± 0.0366 | 0.5642 ± 0.0332 | 0.3106 ± 0.0323 |        3 |
| fruit12_banana | dinov2_s  | mean      | proto  |     50 | 0.7393 ± 0.0100 | 0.6478 ± 0.0098 | 0.2208 ± 0.0080 |        3 |
| fruit12_banana | dinov2_s  | mean      | proto  |    nan | 0.7437 ± 0.0000 | 0.6436 ± 0.0000 | 0.2072 ± 0.0000 |        1 |
| fruit12_banana | resnet50  | cls       | corn   |      1 | 0.4029 ± 0.0593 | 0.3409 ± 0.0396 | 0.5164 ± 0.0382 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |      5 | 0.5466 ± 0.1084 | 0.4651 ± 0.0816 | 0.3986 ± 0.0979 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |     10 | 0.5952 ± 0.1320 | 0.5044 ± 0.1109 | 0.3514 ± 0.1093 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |     50 | 0.7770 ± 0.0230 | 0.6715 ± 0.0206 | 0.2000 ± 0.0184 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |    nan | 0.9150 ± 0.0000 | 0.8069 ± 0.0000 | 0.0802 ± 0.0000 |        1 |
| fruit12_banana | resnet50  | cls       | linear |      1 | 0.3921 ± 0.0542 | 0.3376 ± 0.0350 | 0.5248 ± 0.0203 |        5 |
| fruit12_banana | resnet50  | cls       | linear |      5 | 0.5574 ± 0.1037 | 0.4782 ± 0.0808 | 0.3873 ± 0.0889 |        5 |
| fruit12_banana | resnet50  | cls       | linear |     10 | 0.6278 ± 0.1170 | 0.5306 ± 0.1008 | 0.3195 ± 0.0894 |        5 |
| fruit12_banana | resnet50  | cls       | linear |     50 | 0.7993 ± 0.0193 | 0.6945 ± 0.0162 | 0.1780 ± 0.0161 |        5 |
| fruit12_banana | resnet50  | cls       | linear |    nan | 0.9269 ± 0.0000 | 0.8442 ± 0.0000 | 0.0659 ± 0.0000 |        1 |
| fruit12_banana | resnet50  | cls       | proto  |      1 | 0.4041 ± 0.0626 | 0.3420 ± 0.0359 | 0.5138 ± 0.0368 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |      5 | 0.5212 ± 0.1181 | 0.4473 ± 0.0881 | 0.4242 ± 0.1035 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |     10 | 0.5238 ± 0.1489 | 0.4499 ± 0.1196 | 0.4105 ± 0.1260 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |     50 | 0.6417 ± 0.0836 | 0.5550 ± 0.0641 | 0.3004 ± 0.0769 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |    nan | 0.6659 ± 0.0000 | 0.5715 ± 0.0000 | 0.2359 ± 0.0000 |        1 |
| fruit12_mango  | clip_b    | cls       | corn   |      1 | 0.4116 ± 0.0649 | 0.4146 ± 0.0796 | 0.4362 ± 0.0887 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |      5 | 0.6232 ± 0.0547 | 0.6210 ± 0.0444 | 0.2696 ± 0.0985 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |     10 | 0.6696 ± 0.0675 | 0.6709 ± 0.0609 | 0.2435 ± 0.1046 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |     50 | 0.7942 ± 0.0310 | 0.7944 ± 0.0308 | 0.1362 ± 0.0360 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |    nan | 0.8116 ± 0.0000 | 0.8130 ± 0.0000 | 0.1304 ± 0.0000 |        1 |
| fruit12_mango  | clip_b    | cls       | linear |      1 | 0.4116 ± 0.0713 | 0.4169 ± 0.0845 | 0.4275 ± 0.0873 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |      5 | 0.6406 ± 0.0546 | 0.6413 ± 0.0471 | 0.2435 ± 0.0992 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |     10 | 0.6971 ± 0.0598 | 0.6978 ± 0.0556 | 0.2203 ± 0.0840 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |     50 | 0.8058 ± 0.0418 | 0.8062 ± 0.0418 | 0.1348 ± 0.0437 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |    nan | 0.8333 ± 0.0000 | 0.8347 ± 0.0000 | 0.1087 ± 0.0000 |        1 |
| fruit12_mango  | clip_b    | cls       | proto  |      1 | 0.4058 ± 0.0672 | 0.4091 ± 0.0806 | 0.4362 ± 0.0894 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |      5 | 0.6014 ± 0.0703 | 0.6042 ± 0.0596 | 0.2841 ± 0.1039 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |     10 | 0.6261 ± 0.0846 | 0.6298 ± 0.0759 | 0.2870 ± 0.1196 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |     50 | 0.7623 ± 0.0226 | 0.7615 ± 0.0231 | 0.1652 ± 0.0220 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |    nan | 0.7536 ± 0.0000 | 0.7525 ± 0.0000 | 0.1594 ± 0.0000 |        1 |
| fruit12_mango  | clip_b    | mean      | linear |      1 | 0.3986 ± 0.0475 | 0.3885 ± 0.0527 | 0.4541 ± 0.1215 |        3 |
| fruit12_mango  | clip_b    | mean      | linear |      5 | 0.6667 ± 0.0836 | 0.6759 ± 0.0768 | 0.2729 ± 0.1200 |        3 |
| fruit12_mango  | clip_b    | mean      | linear |     10 | 0.6860 ± 0.0669 | 0.6878 ± 0.0661 | 0.2488 ± 0.0482 |        3 |
| fruit12_mango  | clip_b    | mean      | linear |     50 | 0.8043 ± 0.0261 | 0.8051 ± 0.0250 | 0.1401 ± 0.0302 |        3 |
| fruit12_mango  | clip_b    | mean      | linear |    nan | 0.8551 ± 0.0000 | 0.8561 ± 0.0000 | 0.1304 ± 0.0000 |        1 |
| fruit12_mango  | clip_b    | mean      | proto  |      1 | 0.4130 ± 0.0261 | 0.4046 ± 0.0418 | 0.4541 ± 0.1109 |        3 |
| fruit12_mango  | clip_b    | mean      | proto  |      5 | 0.6377 ± 0.0784 | 0.6488 ± 0.0707 | 0.3068 ± 0.1085 |        3 |
| fruit12_mango  | clip_b    | mean      | proto  |     10 | 0.6329 ± 0.0654 | 0.6389 ± 0.0608 | 0.3213 ± 0.0685 |        3 |
| fruit12_mango  | clip_b    | mean      | proto  |     50 | 0.7415 ± 0.0209 | 0.7402 ± 0.0214 | 0.1884 ± 0.0192 |        3 |
| fruit12_mango  | clip_b    | mean      | proto  |    nan | 0.7536 ± 0.0000 | 0.7522 ± 0.0000 | 0.1812 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_b  | cls       | corn   |      1 | 0.5232 ± 0.0873 | 0.5079 ± 0.1124 | 0.3913 ± 0.1081 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |      5 | 0.7304 ± 0.0442 | 0.7320 ± 0.0397 | 0.2101 ± 0.0719 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |     10 | 0.7638 ± 0.0330 | 0.7645 ± 0.0288 | 0.1841 ± 0.0570 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |     50 | 0.8725 ± 0.0259 | 0.8727 ± 0.0262 | 0.0971 ± 0.0167 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |    nan | 0.8841 ± 0.0000 | 0.8849 ± 0.0000 | 0.0870 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_b  | cls       | linear |      1 | 0.5130 ± 0.0796 | 0.4995 ± 0.1025 | 0.3971 ± 0.0969 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |      5 | 0.7261 ± 0.0305 | 0.7275 ± 0.0288 | 0.2043 ± 0.0479 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |     10 | 0.7768 ± 0.0268 | 0.7766 ± 0.0248 | 0.1696 ± 0.0415 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |     50 | 0.8797 ± 0.0254 | 0.8802 ± 0.0259 | 0.0942 ± 0.0162 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |    nan | 0.8913 ± 0.0000 | 0.8924 ± 0.0000 | 0.0870 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_b  | cls       | proto  |      1 | 0.5145 ± 0.0706 | 0.5004 ± 0.0970 | 0.3986 ± 0.0902 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |      5 | 0.7304 ± 0.0313 | 0.7316 ± 0.0278 | 0.2072 ± 0.0541 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |     10 | 0.7464 ± 0.0271 | 0.7464 ± 0.0239 | 0.2000 ± 0.0553 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |     50 | 0.8348 ± 0.0392 | 0.8338 ± 0.0404 | 0.1145 ± 0.0349 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |    nan | 0.8261 ± 0.0000 | 0.8263 ± 0.0000 | 0.1087 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_b  | mean      | linear |      1 | 0.4034 ± 0.0726 | 0.3675 ± 0.1113 | 0.4565 ± 0.0691 |        3 |
| fruit12_mango  | dinov2_b  | mean      | linear |      5 | 0.6449 ± 0.0261 | 0.6490 ± 0.0293 | 0.3068 ± 0.0466 |        3 |
| fruit12_mango  | dinov2_b  | mean      | linear |     10 | 0.7319 ± 0.0632 | 0.7361 ± 0.0604 | 0.2440 ± 0.0775 |        3 |
| fruit12_mango  | dinov2_b  | mean      | linear |     50 | 0.8792 ± 0.0293 | 0.8802 ± 0.0296 | 0.0870 ± 0.0316 |        3 |
| fruit12_mango  | dinov2_b  | mean      | linear |    nan | 0.8986 ± 0.0000 | 0.8997 ± 0.0000 | 0.0725 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_b  | mean      | proto  |      1 | 0.3986 ± 0.0854 | 0.3645 ± 0.1078 | 0.4758 ± 0.1243 |        3 |
| fruit12_mango  | dinov2_b  | mean      | proto  |      5 | 0.6256 ± 0.0399 | 0.6357 ± 0.0406 | 0.3261 ± 0.0628 |        3 |
| fruit12_mango  | dinov2_b  | mean      | proto  |     10 | 0.6715 ± 0.0673 | 0.6813 ± 0.0631 | 0.3019 ± 0.0775 |        3 |
| fruit12_mango  | dinov2_b  | mean      | proto  |     50 | 0.8382 ± 0.0342 | 0.8394 ± 0.0341 | 0.1280 ± 0.0357 |        3 |
| fruit12_mango  | dinov2_b  | mean      | proto  |    nan | 0.8261 ± 0.0000 | 0.8272 ± 0.0000 | 0.1377 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_s  | cls       | corn   |      1 | 0.5348 ± 0.1174 | 0.5254 ± 0.1419 | 0.3942 ± 0.1470 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |      5 | 0.7348 ± 0.0471 | 0.7388 ± 0.0388 | 0.2159 ± 0.0671 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |     10 | 0.7826 ± 0.0185 | 0.7855 ± 0.0148 | 0.1754 ± 0.0474 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |     50 | 0.8754 ± 0.0374 | 0.8773 ± 0.0371 | 0.0986 ± 0.0342 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |    nan | 0.8551 ± 0.0000 | 0.8561 ± 0.0000 | 0.1159 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_s  | cls       | linear |      1 | 0.5261 ± 0.1203 | 0.5211 ± 0.1358 | 0.3971 ± 0.1362 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |      5 | 0.7261 ± 0.0305 | 0.7295 ± 0.0254 | 0.2159 ± 0.0609 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |     10 | 0.7739 ± 0.0165 | 0.7763 ± 0.0148 | 0.1783 ± 0.0421 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |     50 | 0.8884 ± 0.0279 | 0.8899 ± 0.0275 | 0.0913 ± 0.0259 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |    nan | 0.9058 ± 0.0000 | 0.9066 ± 0.0000 | 0.0797 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_s  | cls       | proto  |      1 | 0.5261 ± 0.1135 | 0.5179 ± 0.1382 | 0.4014 ± 0.1411 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |      5 | 0.7377 ± 0.0506 | 0.7416 ± 0.0429 | 0.2130 ± 0.0673 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |     10 | 0.7536 ± 0.0419 | 0.7574 ± 0.0379 | 0.2058 ± 0.0687 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |     50 | 0.8493 ± 0.0565 | 0.8506 ± 0.0568 | 0.1188 ± 0.0529 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |    nan | 0.8333 ± 0.0000 | 0.8355 ± 0.0000 | 0.1304 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_s  | mean      | linear |      1 | 0.3527 ± 0.1178 | 0.3384 ± 0.1356 | 0.5121 ± 0.1360 |        3 |
| fruit12_mango  | dinov2_s  | mean      | linear |      5 | 0.6353 ± 0.0274 | 0.6402 ± 0.0125 | 0.3261 ± 0.0332 |        3 |
| fruit12_mango  | dinov2_s  | mean      | linear |     10 | 0.7053 ± 0.0233 | 0.7104 ± 0.0234 | 0.2705 ± 0.0254 |        3 |
| fruit12_mango  | dinov2_s  | mean      | linear |     50 | 0.8889 ± 0.0182 | 0.8899 ± 0.0180 | 0.0894 ± 0.0254 |        3 |
| fruit12_mango  | dinov2_s  | mean      | linear |    nan | 0.8841 ± 0.0000 | 0.8851 ± 0.0000 | 0.0870 ± 0.0000 |        1 |
| fruit12_mango  | dinov2_s  | mean      | proto  |      1 | 0.3792 ± 0.1370 | 0.3614 ± 0.1556 | 0.5145 ± 0.1779 |        3 |
| fruit12_mango  | dinov2_s  | mean      | proto  |      5 | 0.6304 ± 0.0362 | 0.6357 ± 0.0253 | 0.3333 ± 0.0403 |        3 |
| fruit12_mango  | dinov2_s  | mean      | proto  |     10 | 0.6377 ± 0.0403 | 0.6470 ± 0.0364 | 0.3430 ± 0.0471 |        3 |
| fruit12_mango  | dinov2_s  | mean      | proto  |     50 | 0.8309 ± 0.0182 | 0.8325 ± 0.0168 | 0.1522 ± 0.0217 |        3 |
| fruit12_mango  | dinov2_s  | mean      | proto  |    nan | 0.8333 ± 0.0000 | 0.8342 ± 0.0000 | 0.1304 ± 0.0000 |        1 |
| fruit12_mango  | resnet50  | cls       | corn   |      1 | 0.4710 ± 0.1055 | 0.4693 ± 0.1118 | 0.3928 ± 0.1419 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |      5 | 0.6899 ± 0.0622 | 0.6895 ± 0.0636 | 0.2232 ± 0.0835 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |     10 | 0.7304 ± 0.0553 | 0.7282 ± 0.0567 | 0.2029 ± 0.0699 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |     50 | 0.8478 ± 0.0154 | 0.8473 ± 0.0157 | 0.1000 ± 0.0139 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |    nan | 0.8768 ± 0.0000 | 0.8767 ± 0.0000 | 0.0942 ± 0.0000 |        1 |
| fruit12_mango  | resnet50  | cls       | linear |      1 | 0.4768 ± 0.0975 | 0.4736 ± 0.1022 | 0.3696 ± 0.1443 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |      5 | 0.7000 ± 0.0742 | 0.6997 ± 0.0751 | 0.2000 ± 0.0913 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |     10 | 0.7377 ± 0.0541 | 0.7357 ± 0.0555 | 0.1884 ± 0.0703 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |     50 | 0.8594 ± 0.0083 | 0.8590 ± 0.0082 | 0.0942 ± 0.0115 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |    nan | 0.8841 ± 0.0000 | 0.8836 ± 0.0000 | 0.0870 ± 0.0000 |        1 |
| fruit12_mango  | resnet50  | cls       | proto  |      1 | 0.4710 ± 0.1036 | 0.4712 ± 0.1113 | 0.3957 ± 0.1376 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |      5 | 0.6565 ± 0.0558 | 0.6578 ± 0.0535 | 0.2594 ± 0.0669 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |     10 | 0.6841 ± 0.0392 | 0.6804 ± 0.0410 | 0.2464 ± 0.0589 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |     50 | 0.8043 ± 0.0177 | 0.8037 ± 0.0178 | 0.1319 ± 0.0119 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |    nan | 0.8188 ± 0.0000 | 0.8181 ± 0.0000 | 0.1087 ± 0.0000 |        1 |
| mango_khir     | clip_b    | cls       | corn   |      1 | 0.6356 ± 0.2161 | 0.3752 ± 0.1044 | 0.2000 ± 0.2141 |        5 |
| mango_khir     | clip_b    | cls       | corn   |      5 | 0.8205 ± 0.1012 | 0.5287 ± 0.1699 | 0.1329 ± 0.0706 |        5 |
| mango_khir     | clip_b    | cls       | corn   |     10 | 0.8027 ± 0.1065 | 0.4978 ± 0.1324 | 0.1534 ± 0.0701 |        5 |
| mango_khir     | clip_b    | cls       | corn   |     50 | 0.9685 ± 0.0038 | 0.5959 ± 0.0167 | 0.0178 ± 0.0038 |        5 |
| mango_khir     | clip_b    | cls       | corn   |    nan | 0.9315 ± 0.0000 | 0.3215 ± 0.0000 | 0.0548 ± 0.0000 |        1 |
| mango_khir     | clip_b    | cls       | linear |      1 | 0.6164 ± 0.2133 | 0.3565 ± 0.0970 | 0.2274 ± 0.2008 |        5 |
| mango_khir     | clip_b    | cls       | linear |      5 | 0.7986 ± 0.1075 | 0.4886 ± 0.1527 | 0.1466 ± 0.0845 |        5 |
| mango_khir     | clip_b    | cls       | linear |     10 | 0.7904 ± 0.1137 | 0.5742 ± 0.1832 | 0.1699 ± 0.0795 |        5 |
| mango_khir     | clip_b    | cls       | linear |     50 | 0.9726 ± 0.0000 | 0.6142 ± 0.0000 | 0.0137 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | linear |    nan | 0.9315 ± 0.0000 | 0.3215 ± 0.0000 | 0.0548 ± 0.0000 |        1 |
| mango_khir     | clip_b    | cls       | proto  |      1 | 0.5548 ± 0.2768 | 0.3496 ± 0.1082 | 0.2616 ± 0.2869 |        5 |
| mango_khir     | clip_b    | cls       | proto  |      5 | 0.7904 ± 0.1298 | 0.5237 ± 0.1861 | 0.1493 ± 0.0927 |        5 |
| mango_khir     | clip_b    | cls       | proto  |     10 | 0.7849 ± 0.0993 | 0.5036 ± 0.1005 | 0.1685 ± 0.0660 |        5 |
| mango_khir     | clip_b    | cls       | proto  |     50 | 0.8411 ± 0.0177 | 0.4987 ± 0.1026 | 0.1425 ± 0.0190 |        5 |
| mango_khir     | clip_b    | cls       | proto  |    nan | 0.8493 ± 0.0000 | 0.4339 ± 0.0000 | 0.1301 ± 0.0000 |        1 |
| mango_khir     | clip_b    | mean      | linear |      1 | 0.6370 ± 0.2489 | 0.3639 ± 0.0588 | 0.1575 ± 0.1140 |        3 |
| mango_khir     | clip_b    | mean      | linear |      5 | 0.7557 ± 0.0881 | 0.4561 ± 0.0553 | 0.1324 ± 0.0788 |        3 |
| mango_khir     | clip_b    | mean      | linear |     10 | 0.7626 ± 0.0979 | 0.5020 ± 0.0944 | 0.1484 ± 0.0395 |        3 |
| mango_khir     | clip_b    | mean      | linear |     50 | 0.9566 ± 0.0040 | 0.5345 ± 0.0240 | 0.0297 ± 0.0040 |        3 |
| mango_khir     | clip_b    | mean      | linear |    nan | 0.9315 ± 0.0000 | 0.3215 ± 0.0000 | 0.0548 ± 0.0000 |        1 |
| mango_khir     | clip_b    | mean      | proto  |      1 | 0.5023 ± 0.3513 | 0.2696 ± 0.0859 | 0.2169 ± 0.1167 |        3 |
| mango_khir     | clip_b    | mean      | proto  |      5 | 0.7260 ± 0.0896 | 0.4399 ± 0.0343 | 0.1507 ± 0.0675 |        3 |
| mango_khir     | clip_b    | mean      | proto  |     10 | 0.7443 ± 0.0856 | 0.4915 ± 0.0623 | 0.1370 ± 0.0205 |        3 |
| mango_khir     | clip_b    | mean      | proto  |     50 | 0.8630 ± 0.0356 | 0.7051 ± 0.0104 | 0.1279 ± 0.0395 |        3 |
| mango_khir     | clip_b    | mean      | proto  |    nan | 0.8630 ± 0.0000 | 0.6162 ± 0.0000 | 0.1027 ± 0.0000 |        1 |
| mango_khir     | dinov2_b  | cls       | corn   |      1 | 0.8164 ± 0.1125 | 0.4462 ± 0.0614 | 0.0945 ± 0.0652 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |      5 | 0.9041 ± 0.0227 | 0.6343 ± 0.0526 | 0.0630 ± 0.0239 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |     10 | 0.8918 ± 0.0502 | 0.6362 ± 0.0590 | 0.0452 ± 0.0104 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |     50 | 0.9699 ± 0.0061 | 0.6132 ± 0.0174 | 0.0164 ± 0.0061 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |    nan | 0.9589 ± 0.0000 | 0.5484 ± 0.0000 | 0.0274 ± 0.0000 |        1 |
| mango_khir     | dinov2_b  | cls       | linear |      1 | 0.8397 ± 0.0955 | 0.4491 ± 0.0744 | 0.0904 ± 0.0450 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |      5 | 0.8959 ± 0.0244 | 0.6090 ± 0.0305 | 0.0589 ± 0.0115 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |     10 | 0.8795 ± 0.0418 | 0.6154 ± 0.0465 | 0.0479 ± 0.0108 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |     50 | 0.9671 ± 0.0031 | 0.6054 ± 0.0082 | 0.0192 ± 0.0031 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |    nan | 0.9658 ± 0.0000 | 0.5837 ± 0.0000 | 0.0205 ± 0.0000 |        1 |
| mango_khir     | dinov2_b  | cls       | proto  |      1 | 0.7329 ± 0.1579 | 0.4179 ± 0.0344 | 0.1370 ± 0.1357 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |      5 | 0.8836 ± 0.0188 | 0.6103 ± 0.0274 | 0.0795 ± 0.0272 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |     10 | 0.8918 ± 0.0460 | 0.6299 ± 0.0442 | 0.0479 ± 0.0128 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |     50 | 0.9178 ± 0.0153 | 0.6779 ± 0.0368 | 0.0603 ± 0.0075 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |    nan | 0.9452 ± 0.0000 | 0.7373 ± 0.0000 | 0.0411 ± 0.0000 |        1 |
| mango_khir     | dinov2_b  | mean      | linear |      1 | 0.7146 ± 0.2821 | 0.3630 ± 0.0901 | 0.1553 ± 0.0904 |        3 |
| mango_khir     | dinov2_b  | mean      | linear |      5 | 0.6621 ± 0.0519 | 0.3812 ± 0.1029 | 0.1895 ± 0.1583 |        3 |
| mango_khir     | dinov2_b  | mean      | linear |     10 | 0.7785 ± 0.1048 | 0.4852 ± 0.0554 | 0.0845 ± 0.0285 |        3 |
| mango_khir     | dinov2_b  | mean      | linear |     50 | 0.9749 ± 0.0040 | 0.6270 ± 0.0119 | 0.0114 ± 0.0040 |        3 |
| mango_khir     | dinov2_b  | mean      | linear |    nan | 0.9315 ± 0.0000 | 0.3215 ± 0.0000 | 0.0548 ± 0.0000 |        1 |
| mango_khir     | dinov2_b  | mean      | proto  |      1 | 0.6644 ± 0.3930 | 0.3226 ± 0.1517 | 0.2466 ± 0.2759 |        3 |
| mango_khir     | dinov2_b  | mean      | proto  |      5 | 0.6370 ± 0.0952 | 0.3628 ± 0.0654 | 0.2032 ± 0.1779 |        3 |
| mango_khir     | dinov2_b  | mean      | proto  |     10 | 0.7352 ± 0.1565 | 0.4966 ± 0.0418 | 0.0822 ± 0.0381 |        3 |
| mango_khir     | dinov2_b  | mean      | proto  |     50 | 0.8242 ± 0.0435 | 0.4998 ± 0.0612 | 0.1301 ± 0.0237 |        3 |
| mango_khir     | dinov2_b  | mean      | proto  |    nan | 0.8493 ± 0.0000 | 0.5191 ± 0.0000 | 0.1164 ± 0.0000 |        1 |
| mango_khir     | dinov2_s  | cls       | corn   |      1 | 0.7781 ± 0.1314 | 0.4196 ± 0.0827 | 0.0904 ± 0.0824 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |      5 | 0.8808 ± 0.0507 | 0.5448 ± 0.1064 | 0.0726 ± 0.0250 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |     10 | 0.8808 ± 0.0667 | 0.5841 ± 0.0614 | 0.0521 ± 0.0230 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |     50 | 0.9644 ± 0.0031 | 0.5984 ± 0.0074 | 0.0219 ± 0.0031 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |    nan | 0.9521 ± 0.0000 | 0.5068 ± 0.0000 | 0.0342 ± 0.0000 |        1 |
| mango_khir     | dinov2_s  | cls       | linear |      1 | 0.7822 ± 0.1247 | 0.4055 ± 0.0678 | 0.1014 ± 0.0779 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |      5 | 0.8795 ± 0.0500 | 0.5814 ± 0.0879 | 0.0740 ± 0.0213 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |     10 | 0.8753 ± 0.0551 | 0.5907 ± 0.0867 | 0.0603 ± 0.0271 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |     50 | 0.9603 ± 0.0089 | 0.5894 ± 0.0196 | 0.0260 ± 0.0089 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |    nan | 0.9658 ± 0.0000 | 0.5837 ± 0.0000 | 0.0205 ± 0.0000 |        1 |
| mango_khir     | dinov2_s  | cls       | proto  |      1 | 0.7192 ± 0.1640 | 0.3975 ± 0.0836 | 0.1233 ± 0.1230 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |      5 | 0.8548 ± 0.0641 | 0.5284 ± 0.1170 | 0.0836 ± 0.0333 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |     10 | 0.8726 ± 0.0621 | 0.5759 ± 0.0554 | 0.0603 ± 0.0213 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |     50 | 0.9055 ± 0.0171 | 0.5833 ± 0.1121 | 0.0671 ± 0.0075 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |    nan | 0.9110 ± 0.0000 | 0.6446 ± 0.0000 | 0.0685 ± 0.0000 |        1 |
| mango_khir     | dinov2_s  | mean      | linear |      1 | 0.7694 ± 0.2071 | 0.3580 ± 0.0763 | 0.1963 ± 0.2106 |        3 |
| mango_khir     | dinov2_s  | mean      | linear |      5 | 0.6895 ± 0.0532 | 0.4019 ± 0.0703 | 0.1872 ± 0.1114 |        3 |
| mango_khir     | dinov2_s  | mean      | linear |     10 | 0.7922 ± 0.0621 | 0.5292 ± 0.0552 | 0.1005 ± 0.0523 |        3 |
| mango_khir     | dinov2_s  | mean      | linear |     50 | 0.9680 ± 0.0040 | 0.6033 ± 0.0102 | 0.0183 ± 0.0040 |        3 |
| mango_khir     | dinov2_s  | mean      | linear |    nan | 0.9315 ± 0.0000 | 0.3215 ± 0.0000 | 0.0548 ± 0.0000 |        1 |
| mango_khir     | dinov2_s  | mean      | proto  |      1 | 0.7329 ± 0.3097 | 0.3137 ± 0.0884 | 0.2374 ± 0.3164 |        3 |
| mango_khir     | dinov2_s  | mean      | proto  |      5 | 0.6872 ± 0.0791 | 0.3990 ± 0.0963 | 0.2237 ± 0.1644 |        3 |
| mango_khir     | dinov2_s  | mean      | proto  |     10 | 0.7785 ± 0.0554 | 0.5252 ± 0.0396 | 0.1050 ± 0.0636 |        3 |
| mango_khir     | dinov2_s  | mean      | proto  |     50 | 0.8379 ± 0.0413 | 0.4864 ± 0.0180 | 0.1187 ± 0.0309 |        3 |
| mango_khir     | dinov2_s  | mean      | proto  |    nan | 0.8219 ± 0.0000 | 0.4555 ± 0.0000 | 0.1233 ± 0.0000 |        1 |
| mango_khir     | resnet50  | cls       | corn   |      1 | 0.5945 ± 0.2271 | 0.3211 ± 0.0587 | 0.2575 ± 0.1863 |        5 |
| mango_khir     | resnet50  | cls       | corn   |      5 | 0.7301 ± 0.1343 | 0.4938 ± 0.1350 | 0.1014 ± 0.0652 |        5 |
| mango_khir     | resnet50  | cls       | corn   |     10 | 0.7753 ± 0.0822 | 0.5364 ± 0.0662 | 0.0479 ± 0.0261 |        5 |
| mango_khir     | resnet50  | cls       | corn   |     50 | 0.9699 ± 0.0061 | 0.6132 ± 0.0156 | 0.0164 ± 0.0061 |        5 |
| mango_khir     | resnet50  | cls       | corn   |    nan | 0.9384 ± 0.0000 | 0.3967 ± 0.0000 | 0.0479 ± 0.0000 |        1 |
| mango_khir     | resnet50  | cls       | linear |      1 | 0.5932 ± 0.2262 | 0.3142 ± 0.0571 | 0.2644 ± 0.1661 |        5 |
| mango_khir     | resnet50  | cls       | linear |      5 | 0.7096 ± 0.1318 | 0.4720 ± 0.1083 | 0.1137 ± 0.0803 |        5 |
| mango_khir     | resnet50  | cls       | linear |     10 | 0.7671 ± 0.0708 | 0.5264 ± 0.0469 | 0.0534 ± 0.0190 |        5 |
| mango_khir     | resnet50  | cls       | linear |     50 | 0.9658 ± 0.0119 | 0.6038 ± 0.0275 | 0.0205 ± 0.0119 |        5 |
| mango_khir     | resnet50  | cls       | linear |    nan | 0.9589 ± 0.0000 | 0.5484 ± 0.0000 | 0.0274 ± 0.0000 |        1 |
| mango_khir     | resnet50  | cls       | proto  |      1 | 0.5671 ± 0.2412 | 0.3174 ± 0.0639 | 0.2726 ± 0.2063 |        5 |
| mango_khir     | resnet50  | cls       | proto  |      5 | 0.6918 ± 0.1400 | 0.4698 ± 0.1404 | 0.1274 ± 0.0867 |        5 |
| mango_khir     | resnet50  | cls       | proto  |     10 | 0.7233 ± 0.0693 | 0.5024 ± 0.0485 | 0.0575 ± 0.0230 |        5 |
| mango_khir     | resnet50  | cls       | proto  |     50 | 0.7795 ± 0.0553 | 0.5202 ± 0.0454 | 0.0658 ± 0.0263 |        5 |
| mango_khir     | resnet50  | cls       | proto  |    nan | 0.8014 ± 0.0000 | 0.5467 ± 0.0000 | 0.0548 ± 0.0000 |        1 |
| ninepeach      | clip_b    | cls       | corn   |      1 | 0.6532 ± 0.0674 | 0.5758 ± 0.0520 | 0.2990 ± 0.0597 |        5 |
| ninepeach      | clip_b    | cls       | corn   |      5 | 0.7159 ± 0.0220 | 0.6695 ± 0.0313 | 0.2371 ± 0.0263 |        5 |
| ninepeach      | clip_b    | cls       | corn   |     10 | 0.7759 ± 0.0337 | 0.7405 ± 0.0375 | 0.1855 ± 0.0319 |        5 |
| ninepeach      | clip_b    | cls       | corn   |     50 | 0.8459 ± 0.0105 | 0.8222 ± 0.0118 | 0.1247 ± 0.0108 |        5 |
| ninepeach      | clip_b    | cls       | corn   |    nan | 0.8834 ± 0.0000 | 0.8520 ± 0.0000 | 0.1013 ± 0.0000 |        1 |
| ninepeach      | clip_b    | cls       | linear |      1 | 0.6421 ± 0.0675 | 0.5735 ± 0.0618 | 0.3140 ± 0.0568 |        5 |
| ninepeach      | clip_b    | cls       | linear |      5 | 0.7140 ± 0.0349 | 0.6510 ± 0.0552 | 0.2382 ± 0.0360 |        5 |
| ninepeach      | clip_b    | cls       | linear |     10 | 0.7774 ± 0.0360 | 0.7251 ± 0.0621 | 0.1843 ± 0.0325 |        5 |
| ninepeach      | clip_b    | cls       | linear |     50 | 0.8528 ± 0.0135 | 0.8239 ± 0.0211 | 0.1231 ± 0.0165 |        5 |
| ninepeach      | clip_b    | cls       | linear |    nan | 0.8910 ± 0.0000 | 0.8625 ± 0.0000 | 0.0956 ± 0.0000 |        1 |
| ninepeach      | clip_b    | cls       | proto  |      1 | 0.6176 ± 0.0691 | 0.5603 ± 0.0495 | 0.3185 ± 0.0814 |        5 |
| ninepeach      | clip_b    | cls       | proto  |      5 | 0.6902 ± 0.0455 | 0.6551 ± 0.0409 | 0.2727 ± 0.0571 |        5 |
| ninepeach      | clip_b    | cls       | proto  |     10 | 0.7507 ± 0.0465 | 0.7211 ± 0.0508 | 0.2134 ± 0.0450 |        5 |
| ninepeach      | clip_b    | cls       | proto  |     50 | 0.8027 ± 0.0087 | 0.7809 ± 0.0083 | 0.1625 ± 0.0092 |        5 |
| ninepeach      | clip_b    | cls       | proto  |    nan | 0.8145 ± 0.0000 | 0.7941 ± 0.0000 | 0.1472 ± 0.0000 |        1 |
| ninepeach      | clip_b    | mean      | linear |      1 | 0.5985 ± 0.0804 | 0.5377 ± 0.0190 | 0.3187 ± 0.0778 |        3 |
| ninepeach      | clip_b    | mean      | linear |      5 | 0.7126 ± 0.0421 | 0.6534 ± 0.0320 | 0.2263 ± 0.0519 |        3 |
| ninepeach      | clip_b    | mean      | linear |     10 | 0.7584 ± 0.0300 | 0.6912 ± 0.0522 | 0.1957 ± 0.0300 |        3 |
| ninepeach      | clip_b    | mean      | linear |     50 | 0.8343 ± 0.0178 | 0.8023 ± 0.0186 | 0.1358 ± 0.0149 |        3 |
| ninepeach      | clip_b    | mean      | linear |    nan | 0.8776 ± 0.0000 | 0.8355 ± 0.0000 | 0.1090 ± 0.0000 |        1 |
| ninepeach      | clip_b    | mean      | proto  |      1 | 0.5883 ± 0.1059 | 0.5276 ± 0.0259 | 0.3327 ± 0.0931 |        3 |
| ninepeach      | clip_b    | mean      | proto  |      5 | 0.6941 ± 0.0498 | 0.6588 ± 0.0292 | 0.2626 ± 0.0668 |        3 |
| ninepeach      | clip_b    | mean      | proto  |     10 | 0.7259 ± 0.0329 | 0.6935 ± 0.0208 | 0.2326 ± 0.0367 |        3 |
| ninepeach      | clip_b    | mean      | proto  |     50 | 0.7871 ± 0.0155 | 0.7678 ± 0.0132 | 0.1708 ± 0.0136 |        3 |
| ninepeach      | clip_b    | mean      | proto  |    nan | 0.8164 ± 0.0000 | 0.7959 ± 0.0000 | 0.1453 ± 0.0000 |        1 |
| ninepeach      | dinov2_b  | cls       | corn   |      1 | 0.6398 ± 0.0974 | 0.5856 ± 0.0685 | 0.3380 ± 0.0929 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |      5 | 0.7977 ± 0.0260 | 0.7631 ± 0.0292 | 0.1904 ± 0.0278 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |     10 | 0.8363 ± 0.0125 | 0.8033 ± 0.0184 | 0.1545 ± 0.0150 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |     50 | 0.8696 ± 0.0044 | 0.8447 ± 0.0056 | 0.1228 ± 0.0037 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |    nan | 0.9101 ± 0.0000 | 0.8881 ± 0.0000 | 0.0822 ± 0.0000 |        1 |
| ninepeach      | dinov2_b  | cls       | linear |      1 | 0.6428 ± 0.0834 | 0.5927 ± 0.0493 | 0.3327 ± 0.0791 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |      5 | 0.7927 ± 0.0157 | 0.7446 ± 0.0263 | 0.1946 ± 0.0185 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |     10 | 0.8375 ± 0.0198 | 0.7958 ± 0.0299 | 0.1522 ± 0.0210 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |     50 | 0.8719 ± 0.0098 | 0.8454 ± 0.0130 | 0.1189 ± 0.0091 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |    nan | 0.9140 ± 0.0000 | 0.8939 ± 0.0000 | 0.0784 ± 0.0000 |        1 |
| ninepeach      | dinov2_b  | cls       | proto  |      1 | 0.5924 ± 0.1023 | 0.5492 ± 0.0644 | 0.3763 ± 0.1111 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |      5 | 0.7568 ± 0.0288 | 0.7305 ± 0.0254 | 0.2329 ± 0.0280 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |     10 | 0.8203 ± 0.0188 | 0.7934 ± 0.0223 | 0.1725 ± 0.0199 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |     50 | 0.8554 ± 0.0074 | 0.8312 ± 0.0080 | 0.1373 ± 0.0071 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |    nan | 0.8719 ± 0.0000 | 0.8490 ± 0.0000 | 0.1205 ± 0.0000 |        1 |
| ninepeach      | dinov2_b  | mean      | linear |      1 | 0.5768 ± 0.0994 | 0.5155 ± 0.0944 | 0.3314 ± 0.1088 |        3 |
| ninepeach      | dinov2_b  | mean      | linear |      5 | 0.7247 ± 0.0289 | 0.6908 ± 0.0213 | 0.2447 ± 0.0306 |        3 |
| ninepeach      | dinov2_b  | mean      | linear |     10 | 0.7674 ± 0.0189 | 0.7241 ± 0.0192 | 0.2046 ± 0.0215 |        3 |
| ninepeach      | dinov2_b  | mean      | linear |     50 | 0.8228 ± 0.0048 | 0.7874 ± 0.0081 | 0.1568 ± 0.0088 |        3 |
| ninepeach      | dinov2_b  | mean      | linear |    nan | 0.8815 ± 0.0000 | 0.8485 ± 0.0000 | 0.1052 ± 0.0000 |        1 |
| ninepeach      | dinov2_b  | mean      | proto  |      1 | 0.5258 ± 0.1321 | 0.4624 ± 0.1391 | 0.3671 ± 0.1653 |        3 |
| ninepeach      | dinov2_b  | mean      | proto  |      5 | 0.6718 ± 0.0576 | 0.6542 ± 0.0407 | 0.2976 ± 0.0637 |        3 |
| ninepeach      | dinov2_b  | mean      | proto  |     10 | 0.7387 ± 0.0335 | 0.7090 ± 0.0270 | 0.2352 ± 0.0326 |        3 |
| ninepeach      | dinov2_b  | mean      | proto  |     50 | 0.7980 ± 0.0029 | 0.7666 ± 0.0048 | 0.1842 ± 0.0055 |        3 |
| ninepeach      | dinov2_b  | mean      | proto  |    nan | 0.8222 ± 0.0000 | 0.7956 ± 0.0000 | 0.1606 ± 0.0000 |        1 |
| ninepeach      | dinov2_s  | cls       | corn   |      1 | 0.6088 ± 0.0731 | 0.5590 ± 0.0308 | 0.3442 ± 0.0796 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |      5 | 0.7847 ± 0.0236 | 0.7499 ± 0.0215 | 0.1954 ± 0.0245 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |     10 | 0.8306 ± 0.0262 | 0.8008 ± 0.0267 | 0.1564 ± 0.0261 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |     50 | 0.8772 ± 0.0104 | 0.8548 ± 0.0120 | 0.1120 ± 0.0106 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |    nan | 0.8987 ± 0.0000 | 0.8767 ± 0.0000 | 0.0937 ± 0.0000 |        1 |
| ninepeach      | dinov2_s  | cls       | linear |      1 | 0.6057 ± 0.0839 | 0.5637 ± 0.0490 | 0.3472 ± 0.0982 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |      5 | 0.7962 ± 0.0208 | 0.7553 ± 0.0202 | 0.1862 ± 0.0222 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |     10 | 0.8428 ± 0.0291 | 0.8105 ± 0.0304 | 0.1442 ± 0.0283 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |     50 | 0.8837 ± 0.0093 | 0.8606 ± 0.0115 | 0.1059 ± 0.0089 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |    nan | 0.8987 ± 0.0000 | 0.8767 ± 0.0000 | 0.0937 ± 0.0000 |        1 |
| ninepeach      | dinov2_s  | cls       | proto  |      1 | 0.5533 ± 0.0870 | 0.5085 ± 0.0559 | 0.3866 ± 0.1269 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |      5 | 0.7683 ± 0.0333 | 0.7416 ± 0.0230 | 0.2168 ± 0.0360 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |     10 | 0.8210 ± 0.0330 | 0.7951 ± 0.0312 | 0.1679 ± 0.0321 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |     50 | 0.8665 ± 0.0164 | 0.8432 ± 0.0190 | 0.1228 ± 0.0171 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |    nan | 0.8853 ± 0.0000 | 0.8637 ± 0.0000 | 0.1052 ± 0.0000 |        1 |
| ninepeach      | dinov2_s  | mean      | linear |      1 | 0.4933 ± 0.0927 | 0.4515 ± 0.0424 | 0.3932 ± 0.1312 |        3 |
| ninepeach      | dinov2_s  | mean      | linear |      5 | 0.7126 ± 0.0508 | 0.6792 ± 0.0313 | 0.2416 ± 0.0549 |        3 |
| ninepeach      | dinov2_s  | mean      | linear |     10 | 0.7686 ± 0.0496 | 0.7321 ± 0.0440 | 0.1880 ± 0.0436 |        3 |
| ninepeach      | dinov2_s  | mean      | linear |     50 | 0.8528 ± 0.0200 | 0.8247 ± 0.0258 | 0.1205 ± 0.0225 |        3 |
| ninepeach      | dinov2_s  | mean      | linear |    nan | 0.8967 ± 0.0000 | 0.8729 ± 0.0000 | 0.0860 ± 0.0000 |        1 |
| ninepeach      | dinov2_s  | mean      | proto  |      1 | 0.4691 ± 0.0430 | 0.4108 ± 0.0750 | 0.3856 ± 0.1419 |        3 |
| ninepeach      | dinov2_s  | mean      | proto  |      5 | 0.6590 ± 0.0882 | 0.6405 ± 0.0654 | 0.3040 ± 0.0977 |        3 |
| ninepeach      | dinov2_s  | mean      | proto  |     10 | 0.7285 ± 0.0535 | 0.7035 ± 0.0423 | 0.2365 ± 0.0507 |        3 |
| ninepeach      | dinov2_s  | mean      | proto  |     50 | 0.7941 ± 0.0048 | 0.7703 ± 0.0075 | 0.1689 ± 0.0149 |        3 |
| ninepeach      | dinov2_s  | mean      | proto  |    nan | 0.8394 ± 0.0000 | 0.8200 ± 0.0000 | 0.1300 ± 0.0000 |        1 |
| ninepeach      | resnet50  | cls       | corn   |      1 | 0.5614 ± 0.0479 | 0.5249 ± 0.0867 | 0.3702 ± 0.0607 |        5 |
| ninepeach      | resnet50  | cls       | corn   |      5 | 0.7809 ± 0.0700 | 0.7552 ± 0.0574 | 0.1935 ± 0.0548 |        5 |
| ninepeach      | resnet50  | cls       | corn   |     10 | 0.8229 ± 0.0378 | 0.7935 ± 0.0373 | 0.1583 ± 0.0365 |        5 |
| ninepeach      | resnet50  | cls       | corn   |     50 | 0.8673 ± 0.0134 | 0.8386 ± 0.0142 | 0.1182 ± 0.0117 |        5 |
| ninepeach      | resnet50  | cls       | corn   |    nan | 0.8757 ± 0.0000 | 0.8414 ± 0.0000 | 0.1090 ± 0.0000 |        1 |
| ninepeach      | resnet50  | cls       | linear |      1 | 0.6115 ± 0.0588 | 0.5774 ± 0.0914 | 0.3163 ± 0.0623 |        5 |
| ninepeach      | resnet50  | cls       | linear |      5 | 0.7706 ± 0.0729 | 0.7354 ± 0.0577 | 0.2065 ± 0.0587 |        5 |
| ninepeach      | resnet50  | cls       | linear |     10 | 0.8161 ± 0.0418 | 0.7810 ± 0.0425 | 0.1683 ± 0.0381 |        5 |
| ninepeach      | resnet50  | cls       | linear |     50 | 0.8654 ± 0.0124 | 0.8358 ± 0.0136 | 0.1201 ± 0.0138 |        5 |
| ninepeach      | resnet50  | cls       | linear |    nan | 0.8948 ± 0.0000 | 0.8693 ± 0.0000 | 0.0918 ± 0.0000 |        1 |
| ninepeach      | resnet50  | cls       | proto  |      1 | 0.5059 ± 0.0402 | 0.4808 ± 0.0725 | 0.4226 ± 0.0988 |        5 |
| ninepeach      | resnet50  | cls       | proto  |      5 | 0.7388 ± 0.0911 | 0.7229 ± 0.0779 | 0.2398 ± 0.0793 |        5 |
| ninepeach      | resnet50  | cls       | proto  |     10 | 0.7889 ± 0.0414 | 0.7676 ± 0.0387 | 0.1931 ± 0.0408 |        5 |
| ninepeach      | resnet50  | cls       | proto  |     50 | 0.8390 ± 0.0249 | 0.8119 ± 0.0256 | 0.1465 ± 0.0226 |        5 |
| ninepeach      | resnet50  | cls       | proto  |    nan | 0.8795 ± 0.0000 | 0.8549 ± 0.0000 | 0.1052 ± 0.0000 |        1 |
| raspgrade      | clip_b    | cls       | corn   |      1 | 0.3060 ± 0.2027 | 0.1539 ± 0.0577 | 0.4975 ± 0.1522 |        5 |
| raspgrade      | clip_b    | cls       | corn   |      5 | 0.2888 ± 0.0692 | 0.1762 ± 0.0203 | 0.4287 ± 0.0437 |        5 |
| raspgrade      | clip_b    | cls       | corn   |     10 | 0.3669 ± 0.0809 | 0.2045 ± 0.0253 | 0.3596 ± 0.0402 |        5 |
| raspgrade      | clip_b    | cls       | corn   |     50 | 0.4839 ± 0.0365 | 0.2486 ± 0.0165 | 0.3156 ± 0.0296 |        5 |
| raspgrade      | clip_b    | cls       | corn   |    nan | 0.7254 ± 0.0000 | 0.1950 ± 0.0000 | 0.2445 ± 0.0000 |        1 |
| raspgrade      | clip_b    | cls       | linear |      1 | 0.2792 ± 0.1738 | 0.1501 ± 0.0520 | 0.4954 ± 0.1440 |        5 |
| raspgrade      | clip_b    | cls       | linear |      5 | 0.2418 ± 0.0583 | 0.1582 ± 0.0177 | 0.4104 ± 0.0453 |        5 |
| raspgrade      | clip_b    | cls       | linear |     10 | 0.3178 ± 0.0938 | 0.1839 ± 0.0247 | 0.3503 ± 0.0567 |        5 |
| raspgrade      | clip_b    | cls       | linear |     50 | 0.4699 ± 0.0412 | 0.2611 ± 0.0162 | 0.3027 ± 0.0308 |        5 |
| raspgrade      | clip_b    | cls       | linear |    nan | 0.7377 ± 0.0000 | 0.2160 ± 0.0000 | 0.2254 ± 0.0000 |        1 |
| raspgrade      | clip_b    | cls       | proto  |      1 | 0.2705 ± 0.2232 | 0.1266 ± 0.0443 | 0.5096 ± 0.1418 |        5 |
| raspgrade      | clip_b    | cls       | proto  |      5 | 0.3046 ± 0.0898 | 0.1808 ± 0.0293 | 0.4003 ± 0.0522 |        5 |
| raspgrade      | clip_b    | cls       | proto  |     10 | 0.3443 ± 0.0715 | 0.1969 ± 0.0205 | 0.3454 ± 0.0317 |        5 |
| raspgrade      | clip_b    | cls       | proto  |     50 | 0.4336 ± 0.0321 | 0.2404 ± 0.0124 | 0.2902 ± 0.0454 |        5 |
| raspgrade      | clip_b    | cls       | proto  |    nan | 0.4699 ± 0.0000 | 0.2518 ± 0.0000 | 0.2609 ± 0.0000 |        1 |
| raspgrade      | clip_b    | mean      | linear |      1 | 0.1817 ± 0.0632 | 0.1205 ± 0.0355 | 0.3903 ± 0.1027 |        3 |
| raspgrade      | clip_b    | mean      | linear |      5 | 0.2017 ± 0.0573 | 0.1505 ± 0.0306 | 0.3201 ± 0.0751 |        3 |
| raspgrade      | clip_b    | mean      | linear |     10 | 0.2914 ± 0.0599 | 0.1876 ± 0.0262 | 0.2964 ± 0.0930 |        3 |
| raspgrade      | clip_b    | mean      | linear |     50 | 0.4463 ± 0.0417 | 0.2452 ± 0.0256 | 0.2928 ± 0.0525 |        3 |
| raspgrade      | clip_b    | mean      | linear |    nan | 0.7363 ± 0.0000 | 0.2137 ± 0.0000 | 0.2227 ± 0.0000 |        1 |
| raspgrade      | clip_b    | mean      | proto  |      1 | 0.1407 ± 0.0663 | 0.0957 ± 0.0372 | 0.3543 ± 0.1312 |        3 |
| raspgrade      | clip_b    | mean      | proto  |      5 | 0.2787 ± 0.0486 | 0.1775 ± 0.0321 | 0.3429 ± 0.0394 |        3 |
| raspgrade      | clip_b    | mean      | proto  |     10 | 0.3233 ± 0.0588 | 0.1976 ± 0.0237 | 0.3046 ± 0.0817 |        3 |
| raspgrade      | clip_b    | mean      | proto  |     50 | 0.3711 ± 0.0477 | 0.2306 ± 0.0212 | 0.2983 ± 0.0566 |        3 |
| raspgrade      | clip_b    | mean      | proto  |    nan | 0.4440 ± 0.0000 | 0.2598 ± 0.0000 | 0.2801 ± 0.0000 |        1 |
| raspgrade      | dinov2_b  | cls       | corn   |      1 | 0.3030 ± 0.1186 | 0.1488 ± 0.0314 | 0.4669 ± 0.1805 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |      5 | 0.2869 ± 0.0831 | 0.1763 ± 0.0431 | 0.4790 ± 0.0544 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |     10 | 0.3686 ± 0.1109 | 0.2031 ± 0.0261 | 0.4240 ± 0.1057 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |     50 | 0.4336 ± 0.0354 | 0.2815 ± 0.0183 | 0.3224 ± 0.0284 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |    nan | 0.7199 ± 0.0000 | 0.1874 ± 0.0000 | 0.2418 ± 0.0000 |        1 |
| raspgrade      | dinov2_b  | cls       | linear |      1 | 0.3041 ± 0.1044 | 0.1528 ± 0.0327 | 0.4719 ± 0.1670 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |      5 | 0.2653 ± 0.0758 | 0.1783 ± 0.0512 | 0.4519 ± 0.0507 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |     10 | 0.3407 ± 0.1221 | 0.1994 ± 0.0377 | 0.4079 ± 0.1008 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |     50 | 0.4342 ± 0.0234 | 0.2876 ± 0.0156 | 0.3126 ± 0.0261 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |    nan | 0.7336 ± 0.0000 | 0.2284 ± 0.0000 | 0.2227 ± 0.0000 |        1 |
| raspgrade      | dinov2_b  | cls       | proto  |      1 | 0.2661 ± 0.0592 | 0.1425 ± 0.0262 | 0.4101 ± 0.1856 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |      5 | 0.3044 ± 0.0731 | 0.1862 ± 0.0365 | 0.4555 ± 0.0443 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |     10 | 0.3555 ± 0.0938 | 0.2051 ± 0.0233 | 0.4164 ± 0.0945 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |     50 | 0.3918 ± 0.0370 | 0.2452 ± 0.0097 | 0.3407 ± 0.0355 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |    nan | 0.4358 ± 0.0000 | 0.2610 ± 0.0000 | 0.2910 ± 0.0000 |        1 |
| raspgrade      | dinov2_b  | mean      | linear |      1 | 0.3224 ± 0.1547 | 0.1479 ± 0.0619 | 0.4203 ± 0.2018 |        3 |
| raspgrade      | dinov2_b  | mean      | linear |      5 | 0.3001 ± 0.0692 | 0.1869 ± 0.0395 | 0.3989 ± 0.0190 |        3 |
| raspgrade      | dinov2_b  | mean      | linear |     10 | 0.3821 ± 0.1130 | 0.2020 ± 0.0329 | 0.3529 ± 0.0542 |        3 |
| raspgrade      | dinov2_b  | mean      | linear |     50 | 0.4057 ± 0.0393 | 0.2696 ± 0.0142 | 0.3256 ± 0.0444 |        3 |
| raspgrade      | dinov2_b  | mean      | linear |    nan | 0.7322 ± 0.0000 | 0.2266 ± 0.0000 | 0.2268 ± 0.0000 |        1 |
| raspgrade      | dinov2_b  | mean      | proto  |      1 | 0.2714 ± 0.0919 | 0.1448 ± 0.0613 | 0.3898 ± 0.2205 |        3 |
| raspgrade      | dinov2_b  | mean      | proto  |      5 | 0.2923 ± 0.0756 | 0.1884 ± 0.0409 | 0.4290 ± 0.0362 |        3 |
| raspgrade      | dinov2_b  | mean      | proto  |     10 | 0.3784 ± 0.0815 | 0.2111 ± 0.0215 | 0.3702 ± 0.0353 |        3 |
| raspgrade      | dinov2_b  | mean      | proto  |     50 | 0.3830 ± 0.0261 | 0.2342 ± 0.0089 | 0.3370 ± 0.0223 |        3 |
| raspgrade      | dinov2_b  | mean      | proto  |    nan | 0.4098 ± 0.0000 | 0.2594 ± 0.0000 | 0.3251 ± 0.0000 |        1 |
| raspgrade      | dinov2_s  | cls       | corn   |      1 | 0.3268 ± 0.0804 | 0.1773 ± 0.0384 | 0.4180 ± 0.1734 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |      5 | 0.3314 ± 0.0589 | 0.2017 ± 0.0198 | 0.4301 ± 0.0336 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |     10 | 0.3850 ± 0.0868 | 0.2336 ± 0.0140 | 0.3658 ± 0.0587 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |     50 | 0.4631 ± 0.0326 | 0.2949 ± 0.0140 | 0.3128 ± 0.0246 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |    nan | 0.7363 ± 0.0000 | 0.2271 ± 0.0000 | 0.2145 ± 0.0000 |        1 |
| raspgrade      | dinov2_s  | cls       | linear |      1 | 0.3079 ± 0.0627 | 0.1727 ± 0.0374 | 0.4008 ± 0.1737 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |      5 | 0.3079 ± 0.0532 | 0.1952 ± 0.0226 | 0.4077 ± 0.0218 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |     10 | 0.3544 ± 0.0774 | 0.2282 ± 0.0145 | 0.3519 ± 0.0531 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |     50 | 0.4478 ± 0.0207 | 0.2937 ± 0.0048 | 0.3025 ± 0.0227 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |    nan | 0.7637 ± 0.0000 | 0.3040 ± 0.0000 | 0.1926 ± 0.0000 |        1 |
| raspgrade      | dinov2_s  | cls       | proto  |      1 | 0.3260 ± 0.0944 | 0.1728 ± 0.0380 | 0.3577 ± 0.1473 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |      5 | 0.3443 ± 0.0770 | 0.1998 ± 0.0250 | 0.4033 ± 0.0470 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |     10 | 0.3615 ± 0.0749 | 0.2257 ± 0.0166 | 0.3552 ± 0.0546 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |     50 | 0.4208 ± 0.0413 | 0.2569 ± 0.0201 | 0.3290 ± 0.0290 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |    nan | 0.5027 ± 0.0000 | 0.2837 ± 0.0000 | 0.2869 ± 0.0000 |        1 |
| raspgrade      | dinov2_s  | mean      | linear |      1 | 0.2359 ± 0.0724 | 0.1361 ± 0.0302 | 0.3575 ± 0.2387 |        3 |
| raspgrade      | dinov2_s  | mean      | linear |      5 | 0.2650 ± 0.0595 | 0.1772 ± 0.0332 | 0.4321 ± 0.0096 |        3 |
| raspgrade      | dinov2_s  | mean      | linear |     10 | 0.3734 ± 0.0708 | 0.2303 ± 0.0301 | 0.3470 ± 0.0188 |        3 |
| raspgrade      | dinov2_s  | mean      | linear |     50 | 0.4212 ± 0.0383 | 0.2790 ± 0.0210 | 0.3315 ± 0.0209 |        3 |
| raspgrade      | dinov2_s  | mean      | linear |    nan | 0.7596 ± 0.0000 | 0.2925 ± 0.0000 | 0.1899 ± 0.0000 |        1 |
| raspgrade      | dinov2_s  | mean      | proto  |      1 | 0.1995 ± 0.0542 | 0.1262 ± 0.0112 | 0.3434 ± 0.2164 |        3 |
| raspgrade      | dinov2_s  | mean      | proto  |      5 | 0.2864 ± 0.0772 | 0.1816 ± 0.0300 | 0.4244 ± 0.0607 |        3 |
| raspgrade      | dinov2_s  | mean      | proto  |     10 | 0.3593 ± 0.0443 | 0.2168 ± 0.0153 | 0.3752 ± 0.0096 |        3 |
| raspgrade      | dinov2_s  | mean      | proto  |     50 | 0.3670 ± 0.0369 | 0.2287 ± 0.0139 | 0.3725 ± 0.0110 |        3 |
| raspgrade      | dinov2_s  | mean      | proto  |    nan | 0.4631 ± 0.0000 | 0.2805 ± 0.0000 | 0.3128 ± 0.0000 |        1 |
| raspgrade      | resnet50  | cls       | corn   |      1 | 0.2907 ± 0.1268 | 0.1477 ± 0.0361 | 0.3710 ± 0.1948 |        5 |
| raspgrade      | resnet50  | cls       | corn   |      5 | 0.3249 ± 0.0957 | 0.1963 ± 0.0410 | 0.3765 ± 0.0919 |        5 |
| raspgrade      | resnet50  | cls       | corn   |     10 | 0.3885 ± 0.0931 | 0.2253 ± 0.0355 | 0.3284 ± 0.0709 |        5 |
| raspgrade      | resnet50  | cls       | corn   |     50 | 0.5142 ± 0.0373 | 0.2977 ± 0.0226 | 0.2787 ± 0.0195 |        5 |
| raspgrade      | resnet50  | cls       | corn   |    nan | 0.7391 ± 0.0000 | 0.2336 ± 0.0000 | 0.2131 ± 0.0000 |        1 |
| raspgrade      | resnet50  | cls       | linear |      1 | 0.3025 ± 0.1337 | 0.1480 ± 0.0348 | 0.3489 ± 0.1795 |        5 |
| raspgrade      | resnet50  | cls       | linear |      5 | 0.3071 ± 0.1026 | 0.1864 ± 0.0416 | 0.3628 ± 0.0937 |        5 |
| raspgrade      | resnet50  | cls       | linear |     10 | 0.3626 ± 0.0948 | 0.2190 ± 0.0293 | 0.3216 ± 0.0683 |        5 |
| raspgrade      | resnet50  | cls       | linear |     50 | 0.5063 ± 0.0433 | 0.2956 ± 0.0243 | 0.2675 ± 0.0157 |        5 |
| raspgrade      | resnet50  | cls       | linear |    nan | 0.7459 ± 0.0000 | 0.2572 ± 0.0000 | 0.1967 ± 0.0000 |        1 |
| raspgrade      | resnet50  | cls       | proto  |      1 | 0.2481 ± 0.1326 | 0.1394 ± 0.0364 | 0.3199 ± 0.1817 |        5 |
| raspgrade      | resnet50  | cls       | proto  |      5 | 0.2932 ± 0.0821 | 0.1797 ± 0.0330 | 0.3519 ± 0.0727 |        5 |
| raspgrade      | resnet50  | cls       | proto  |     10 | 0.3276 ± 0.0827 | 0.2044 ± 0.0277 | 0.3339 ± 0.0597 |        5 |
| raspgrade      | resnet50  | cls       | proto  |     50 | 0.4314 ± 0.0435 | 0.2494 ± 0.0246 | 0.2934 ± 0.0422 |        5 |
| raspgrade      | resnet50  | cls       | proto  |    nan | 0.5055 ± 0.0000 | 0.2806 ± 0.0000 | 0.2678 ± 0.0000 |        1 |

## Per-class average precision (the plan's long-tail metric; mean ± sd over seeds)

| view           | encoder   | variant   | head   |   shot | macro_ap        | chance          |   n_runs |
|:---------------|:----------|:----------|:-------|-------:|:----------------|:----------------|---------:|
| banana3        | clip_b    | cls       | linear |      1 | 0.6364 ± 0.0671 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | linear |      5 | 0.7764 ± 0.0472 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | linear |     10 | 0.7874 ± 0.0346 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | linear |     50 | 0.8889 ± 0.0084 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | linear |    nan | 0.9557 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | proto  |      1 | 0.6186 ± 0.0828 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | proto  |      5 | 0.7801 ± 0.0559 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | proto  |     10 | 0.7720 ± 0.0350 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | proto  |     50 | 0.8105 ± 0.0075 | 0.3333 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | proto  |    nan | 0.8193 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | linear |      1 | 0.6090 ± 0.0742 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | linear |      5 | 0.7938 ± 0.0521 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | linear |     10 | 0.8336 ± 0.0270 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | linear |     50 | 0.9400 ± 0.0048 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | linear |    nan | 0.9807 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | proto  |      1 | 0.5941 ± 0.0940 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | proto  |      5 | 0.8149 ± 0.0497 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | proto  |     10 | 0.8537 ± 0.0283 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | proto  |     50 | 0.9073 ± 0.0077 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | proto  |    nan | 0.9201 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | linear |      1 | 0.6336 ± 0.0759 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | linear |      5 | 0.8177 ± 0.0456 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | linear |     10 | 0.8526 ± 0.0213 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | linear |     50 | 0.9572 ± 0.0066 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | linear |    nan | 0.9883 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | proto  |      1 | 0.6222 ± 0.0894 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | proto  |      5 | 0.8404 ± 0.0400 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | proto  |     10 | 0.8702 ± 0.0226 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | proto  |     50 | 0.9236 ± 0.0054 | 0.3333 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | proto  |    nan | 0.9325 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | linear |      1 | 0.6113 ± 0.0442 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | linear |      5 | 0.6862 ± 0.0819 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | linear |     10 | 0.7821 ± 0.0284 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | linear |     50 | 0.8818 ± 0.0157 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | linear |    nan | 0.9480 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | proto  |      1 | 0.5844 ± 0.0449 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | proto  |      5 | 0.6803 ± 0.0837 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | proto  |     10 | 0.7679 ± 0.0154 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | proto  |     50 | 0.8135 ± 0.0141 | 0.3333 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | proto  |    nan | 0.8211 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | linear |      1 | 0.8365 ± 0.0385 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | linear |      5 | 0.9414 ± 0.0384 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | linear |     10 | 0.9669 ± 0.0123 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | linear |     50 | 0.9872 ± 0.0048 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | linear |    nan | 0.9970 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | proto  |      1 | 0.8348 ± 0.0402 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | proto  |      5 | 0.9445 ± 0.0411 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | proto  |     10 | 0.9675 ± 0.0124 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | proto  |     50 | 0.9821 ± 0.0040 | 0.3333 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | proto  |    nan | 0.9834 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | linear |      1 | 0.9032 ± 0.0371 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | linear |      5 | 0.9855 ± 0.0055 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | linear |     10 | 0.9887 ± 0.0061 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | linear |     50 | 0.9940 ± 0.0014 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | linear |    nan | 0.9991 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | proto  |      1 | 0.8989 ± 0.0431 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | proto  |      5 | 0.9833 ± 0.0065 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | proto  |     10 | 0.9877 ± 0.0068 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | proto  |     50 | 0.9904 ± 0.0020 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | proto  |    nan | 0.9911 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | linear |      1 | 0.8291 ± 0.0308 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | linear |      5 | 0.9810 ± 0.0065 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | linear |     10 | 0.9839 ± 0.0051 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | linear |     50 | 0.9934 ± 0.0008 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | linear |    nan | 0.9991 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | proto  |      1 | 0.8161 ± 0.0430 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | proto  |      5 | 0.9809 ± 0.0057 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | proto  |     10 | 0.9839 ± 0.0053 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | proto  |     50 | 0.9901 ± 0.0008 | 0.3333 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | proto  |    nan | 0.9912 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | linear |      1 | 0.7263 ± 0.0588 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | linear |      5 | 0.8621 ± 0.0611 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | linear |     10 | 0.9015 ± 0.0526 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | linear |     50 | 0.9634 ± 0.0092 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | linear |    nan | 0.9967 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | proto  |      1 | 0.7142 ± 0.0474 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | proto  |      5 | 0.8442 ± 0.0710 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | proto  |     10 | 0.8688 ± 0.0638 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | proto  |     50 | 0.8778 ± 0.0201 | 0.3333 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | proto  |    nan | 0.8881 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | linear |      1 | 0.8204 ± 0.0946 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | linear |      5 | 0.8907 ± 0.1076 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | linear |     10 | 0.9466 ± 0.0314 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | linear |     50 | 0.9933 ± 0.0071 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | linear |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | proto  |      1 | 0.8204 ± 0.0946 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | proto  |      5 | 0.8871 ± 0.1078 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | proto  |     10 | 0.9381 ± 0.0345 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | proto  |     50 | 0.9717 ± 0.0141 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | proto  |    nan | 0.9730 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |      1 | 0.8865 ± 0.0838 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |      5 | 0.9493 ± 0.0432 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |     10 | 0.9792 ± 0.0097 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |     50 | 1.0000 ± 0.0001 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |      1 | 0.8865 ± 0.0838 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |      5 | 0.9576 ± 0.0389 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |     10 | 0.9819 ± 0.0116 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |     50 | 0.9986 ± 0.0017 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |      1 | 0.8118 ± 0.1055 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |      5 | 0.9283 ± 0.0490 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |     10 | 0.9489 ± 0.0692 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |     50 | 0.9967 ± 0.0069 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |    nan | 0.9999 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |      1 | 0.8118 ± 0.1055 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |      5 | 0.9358 ± 0.0539 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |     10 | 0.9533 ± 0.0706 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |     50 | 0.9914 ± 0.0171 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |    nan | 0.9977 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | linear |      1 | 0.9246 ± 0.0446 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | linear |      5 | 0.9446 ± 0.0176 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | linear |     10 | 0.9174 ± 0.0741 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | linear |     50 | 0.9832 ± 0.0068 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | linear |    nan | 0.9996 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | proto  |      1 | 0.9246 ± 0.0446 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | proto  |      5 | 0.9411 ± 0.0223 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | proto  |     10 | 0.8972 ± 0.0872 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | proto  |     50 | 0.9438 ± 0.0088 | 0.5000 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | proto  |    nan | 0.9501 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | linear |      1 | 0.9066 ± 0.0632 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | linear |      5 | 0.9935 ± 0.0072 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | linear |     10 | 0.9989 ± 0.0017 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | linear |     50 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | linear |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | proto  |      1 | 0.9066 ± 0.0632 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | proto  |      5 | 0.9926 ± 0.0081 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | proto  |     10 | 0.9986 ± 0.0020 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | proto  |     50 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | proto  |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |      1 | 0.9097 ± 0.1226 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |      5 | 0.9981 ± 0.0038 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |     10 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |     50 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |      1 | 0.9097 ± 0.1226 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |      5 | 0.9974 ± 0.0054 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |     10 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |     50 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |      1 | 0.8842 ± 0.1232 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |      5 | 0.9963 ± 0.0061 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |     10 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |     50 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |      1 | 0.8842 ± 0.1232 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |      5 | 0.9960 ± 0.0065 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |     10 | 1.0000 ± 0.0001 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |     50 | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | linear |      1 | 0.8828 ± 0.0530 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | linear |      5 | 0.9789 ± 0.0224 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | linear |     10 | 0.9990 ± 0.0006 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | linear |     50 | 0.9996 ± 0.0003 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | linear |    nan | 1.0000 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | proto  |      1 | 0.8828 ± 0.0531 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | proto  |      5 | 0.9726 ± 0.0283 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | proto  |     10 | 0.9984 ± 0.0007 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | proto  |     50 | 0.9986 ± 0.0008 | 0.5000 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | proto  |    nan | 0.9993 ± 0.0000 | 0.5000 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |      1 | 0.4515 ± 0.0775 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |      5 | 0.5161 ± 0.0840 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |     10 | 0.6106 ± 0.0411 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |     50 | 0.7633 ± 0.0204 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |    nan | 0.8465 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |      1 | 0.4527 ± 0.0769 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |      5 | 0.5041 ± 0.0872 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |     10 | 0.5678 ± 0.0405 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |     50 | 0.6964 ± 0.0441 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |    nan | 0.7584 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |      1 | 0.4965 ± 0.0542 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |      5 | 0.6504 ± 0.0991 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |     10 | 0.7444 ± 0.0233 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |     50 | 0.8437 ± 0.0129 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |    nan | 0.8961 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |      1 | 0.4892 ± 0.0538 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |      5 | 0.6336 ± 0.1031 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |     10 | 0.7019 ± 0.0210 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |     50 | 0.8057 ± 0.0175 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |    nan | 0.8266 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |      1 | 0.4917 ± 0.0667 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |      5 | 0.6438 ± 0.1244 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |     10 | 0.7495 ± 0.0433 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |     50 | 0.8362 ± 0.0303 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |    nan | 0.9052 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |      1 | 0.4916 ± 0.0731 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |      5 | 0.6256 ± 0.1284 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |     10 | 0.7048 ± 0.0467 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |     50 | 0.8068 ± 0.0245 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |    nan | 0.8179 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |      1 | 0.4542 ± 0.0869 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |      5 | 0.5973 ± 0.1409 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |     10 | 0.7365 ± 0.0184 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |     50 | 0.8289 ± 0.0156 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |    nan | 0.8989 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |      1 | 0.4535 ± 0.0751 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |      5 | 0.5588 ± 0.1235 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |     10 | 0.6746 ± 0.0667 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |     50 | 0.7565 ± 0.0693 | 0.3333 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |    nan | 0.8099 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | linear |      1 | 0.4439 ± 0.0261 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | linear |      5 | 0.4870 ± 0.0362 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | linear |     10 | 0.5544 ± 0.0398 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | linear |     50 | 0.7403 ± 0.0129 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | linear |    nan | 0.9003 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |      1 | 0.4414 ± 0.0288 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |      5 | 0.4764 ± 0.0366 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |     10 | 0.5262 ± 0.0453 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |     50 | 0.6756 ± 0.0186 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |    nan | 0.6960 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |      1 | 0.5323 ± 0.0705 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |      5 | 0.6272 ± 0.0326 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |     10 | 0.6675 ± 0.0400 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |     50 | 0.8211 ± 0.0182 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |    nan | 0.9245 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |      1 | 0.5184 ± 0.0751 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |      5 | 0.6284 ± 0.0339 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |     10 | 0.6568 ± 0.0570 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |     50 | 0.7711 ± 0.0262 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |    nan | 0.7720 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |      1 | 0.5408 ± 0.0649 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |      5 | 0.6516 ± 0.0425 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |     10 | 0.6920 ± 0.0582 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |     50 | 0.8529 ± 0.0090 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |    nan | 0.9561 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |      1 | 0.5345 ± 0.0665 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |      5 | 0.6496 ± 0.0503 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |     10 | 0.6758 ± 0.0766 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |     50 | 0.7901 ± 0.0206 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |    nan | 0.7865 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | linear |      1 | 0.4499 ± 0.0485 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | linear |      5 | 0.5641 ± 0.0632 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | linear |     10 | 0.6245 ± 0.0735 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | linear |     50 | 0.7804 ± 0.0060 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | linear |    nan | 0.9243 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |      1 | 0.4461 ± 0.0458 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |      5 | 0.5348 ± 0.0667 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |     10 | 0.5750 ± 0.0843 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |     50 | 0.6679 ± 0.0301 | 0.3333 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |    nan | 0.6840 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |      1 | 0.5376 ± 0.0966 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |      5 | 0.7644 ± 0.0549 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |     10 | 0.8108 ± 0.0620 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |     50 | 0.9200 ± 0.0219 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |    nan | 0.9458 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |      1 | 0.5366 ± 0.0988 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |      5 | 0.7443 ± 0.0677 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |     10 | 0.7617 ± 0.0756 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |     50 | 0.8738 ± 0.0143 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |    nan | 0.8821 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |      1 | 0.5904 ± 0.1116 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |      5 | 0.8413 ± 0.0640 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |     10 | 0.8822 ± 0.0299 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |     50 | 0.9504 ± 0.0152 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |    nan | 0.9535 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |      1 | 0.5886 ± 0.1173 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |      5 | 0.8447 ± 0.0539 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |     10 | 0.8725 ± 0.0386 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |     50 | 0.9375 ± 0.0164 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |    nan | 0.9380 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |      1 | 0.6094 ± 0.1491 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |      5 | 0.8290 ± 0.0655 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |     10 | 0.8775 ± 0.0335 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |     50 | 0.9482 ± 0.0193 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |    nan | 0.9496 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |      1 | 0.6133 ± 0.1445 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |      5 | 0.8283 ± 0.0663 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |     10 | 0.8621 ± 0.0454 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |     50 | 0.9365 ± 0.0212 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |    nan | 0.9393 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |      1 | 0.5340 ± 0.1140 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |      5 | 0.7867 ± 0.0777 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |     10 | 0.8806 ± 0.0181 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |     50 | 0.9434 ± 0.0052 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |    nan | 0.9635 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |      1 | 0.5324 ± 0.1151 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |      5 | 0.7582 ± 0.0881 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |     10 | 0.8271 ± 0.0615 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |     50 | 0.9105 ± 0.0090 | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |    nan | 0.9117 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | linear |      1 | 0.5353 ± 0.0867 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | linear |      5 | 0.6074 ± 0.0522 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | linear |     10 | 0.6964 ± 0.0734 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | linear |     50 | 0.6931 ± 0.0207 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | linear |    nan | 0.6643 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | proto  |      1 | 0.5287 ± 0.0891 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | proto  |      5 | 0.6100 ± 0.0606 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | proto  |     10 | 0.6899 ± 0.0696 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | proto  |     50 | 0.6605 ± 0.0111 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | proto  |    nan | 0.6512 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |      1 | 0.5438 ± 0.0869 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |      5 | 0.6977 ± 0.0898 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |     10 | 0.8302 ± 0.0884 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |     50 | 0.9157 ± 0.0843 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |    nan | 0.7158 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |      1 | 0.5311 ± 0.0512 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |      5 | 0.7381 ± 0.1337 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |     10 | 0.8462 ± 0.0833 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |     50 | 0.8446 ± 0.0555 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |    nan | 0.8201 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |      1 | 0.4992 ± 0.0878 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |      5 | 0.6241 ± 0.0789 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |     10 | 0.6999 ± 0.0370 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |     50 | 0.7045 ± 0.0300 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |    nan | 0.6612 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |      1 | 0.5038 ± 0.0836 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |      5 | 0.6429 ± 0.0889 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |     10 | 0.6998 ± 0.0296 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |     50 | 0.7080 ± 0.0303 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |    nan | 0.7472 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | linear |      1 | 0.4624 ± 0.0600 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | linear |      5 | 0.6490 ± 0.0293 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | linear |     10 | 0.7842 ± 0.0609 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | linear |     50 | 0.8014 ± 0.0382 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | linear |    nan | 0.6741 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | proto  |      1 | 0.4547 ± 0.0483 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | proto  |      5 | 0.6391 ± 0.0507 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | proto  |     10 | 0.7773 ± 0.0645 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | proto  |     50 | 0.8014 ± 0.0061 | 0.3333 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | proto  |    nan | 0.8033 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | linear |      1 | 0.6372 ± 0.0683 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | linear |      5 | 0.7007 ± 0.0168 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | linear |     10 | 0.7647 ± 0.0387 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | linear |     50 | 0.8614 ± 0.0045 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | linear |    nan | 0.9275 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | proto  |      1 | 0.6491 ± 0.0658 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | proto  |      5 | 0.7068 ± 0.0205 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | proto  |     10 | 0.7625 ± 0.0399 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | proto  |     50 | 0.7913 ± 0.0057 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | proto  |    nan | 0.8046 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |      1 | 0.6873 ± 0.0212 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |      5 | 0.7605 ± 0.0183 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |     10 | 0.8142 ± 0.0303 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |     50 | 0.9018 ± 0.0119 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |    nan | 0.9536 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |      1 | 0.6891 ± 0.0250 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |      5 | 0.7814 ± 0.0204 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |     10 | 0.8264 ± 0.0265 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |     50 | 0.8737 ± 0.0125 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |    nan | 0.8906 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |      1 | 0.6389 ± 0.0430 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |      5 | 0.7670 ± 0.0242 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |     10 | 0.8262 ± 0.0472 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |     50 | 0.9034 ± 0.0078 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |    nan | 0.9470 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |      1 | 0.6408 ± 0.0475 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |      5 | 0.7851 ± 0.0169 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |     10 | 0.8348 ± 0.0410 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |     50 | 0.8745 ± 0.0103 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |    nan | 0.8864 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | linear |      1 | 0.6754 ± 0.0503 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | linear |      5 | 0.7646 ± 0.0392 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | linear |     10 | 0.7943 ± 0.0348 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | linear |     50 | 0.8840 ± 0.0130 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | linear |    nan | 0.9463 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | proto  |      1 | 0.6734 ± 0.0547 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | proto  |      5 | 0.7771 ± 0.0483 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | proto  |     10 | 0.8012 ± 0.0312 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | proto  |     50 | 0.8393 ± 0.0193 | 0.3333 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | proto  |    nan | 0.8746 ± 0.0000 | 0.3333 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | linear |      1 | 0.2269 ± 0.0190 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | linear |      5 | 0.2279 ± 0.0108 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | linear |     10 | 0.2376 ± 0.0112 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | linear |     50 | 0.2637 ± 0.0068 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | linear |    nan | 0.3832 ± 0.0000 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | proto  |      1 | 0.2285 ± 0.0268 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | proto  |      5 | 0.2276 ± 0.0110 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | proto  |     10 | 0.2360 ± 0.0115 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | proto  |     50 | 0.2483 ± 0.0053 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | proto  |    nan | 0.2576 ± 0.0000 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |      1 | 0.2297 ± 0.0134 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |      5 | 0.2484 ± 0.0320 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |     10 | 0.2506 ± 0.0098 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |     50 | 0.3069 ± 0.0150 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |    nan | 0.4259 ± 0.0000 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |      1 | 0.2251 ± 0.0127 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |      5 | 0.2456 ± 0.0304 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |     10 | 0.2449 ± 0.0089 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |     50 | 0.2557 ± 0.0082 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |    nan | 0.2722 ± 0.0000 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |      1 | 0.2381 ± 0.0156 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |      5 | 0.2711 ± 0.0349 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |     10 | 0.2823 ± 0.0140 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |     50 | 0.3356 ± 0.0182 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |    nan | 0.4666 ± 0.0000 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |      1 | 0.2413 ± 0.0204 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |      5 | 0.2695 ± 0.0356 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |     10 | 0.2738 ± 0.0135 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |     50 | 0.2850 ± 0.0218 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |    nan | 0.3104 ± 0.0000 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | linear |      1 | 0.2263 ± 0.0252 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | linear |      5 | 0.2520 ± 0.0282 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | linear |     10 | 0.2688 ± 0.0154 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | linear |     50 | 0.3397 ± 0.0161 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | linear |    nan | 0.4244 ± 0.0000 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | proto  |      1 | 0.2266 ± 0.0257 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | proto  |      5 | 0.2519 ± 0.0287 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | proto  |     10 | 0.2645 ± 0.0144 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | proto  |     50 | 0.3084 ± 0.0165 | 0.2000 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | proto  |    nan | 0.3342 ± 0.0000 | 0.2000 ± 0.0000 |        5 |

`chance` is the macro prevalence of the test split: on a balanced view it is 1/C, and an uninformative scorer's macro AP lands there. These runs live under `exp = E1ap` so they never enter T2 or the paired tests.

## Ordinal cost-weighted macro-F1 (plan 5.3: adjacent error costs 1, skipped grade costs 2; mean ± sd over seeds)

| view           | encoder   | variant   | head   |   shot | cost_f1         | macro_f1        | off_by_one   | ordinal_mae     |   n_runs |
|:---------------|:----------|:----------|:-------|-------:|:----------------|:----------------|:-------------|:----------------|---------:|
| banana3        | clip_b    | cls       | corn   |      1 | 0.6883 ± 0.1098 | 0.4552 ± 0.0789 | NA           | 0.5719 ± 0.0665 |        5 |
| banana3        | clip_b    | cls       | corn   |      5 | 0.8291 ± 0.0391 | 0.6977 ± 0.0712 | NA           | 0.3360 ± 0.0695 |        5 |
| banana3        | clip_b    | cls       | corn   |     10 | 0.8536 ± 0.0195 | 0.7347 ± 0.0290 | NA           | 0.2865 ± 0.0415 |        5 |
| banana3        | clip_b    | cls       | corn   |     50 | 0.8920 ± 0.0067 | 0.7997 ± 0.0133 | NA           | 0.2169 ± 0.0141 |        5 |
| banana3        | clip_b    | cls       | corn   |    nan | 0.9358 ± 0.0000 | 0.8803 ± 0.0000 | NA           | 0.1236 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | linear |      1 | 0.7284 ± 0.0591 | 0.5112 ± 0.0604 | NA           | 0.5494 ± 0.0971 |        5 |
| banana3        | clip_b    | cls       | linear |      5 | 0.8217 ± 0.0361 | 0.6933 ± 0.0729 | NA           | 0.3517 ± 0.0650 |        5 |
| banana3        | clip_b    | cls       | linear |     10 | 0.8468 ± 0.0242 | 0.7249 ± 0.0386 | NA           | 0.2966 ± 0.0502 |        5 |
| banana3        | clip_b    | cls       | linear |     50 | 0.8949 ± 0.0118 | 0.8075 ± 0.0195 | NA           | 0.2067 ± 0.0240 |        5 |
| banana3        | clip_b    | cls       | linear |    nan | 0.9327 ± 0.0000 | 0.8745 ± 0.0000 | NA           | 0.1292 ± 0.0000 |        5 |
| banana3        | clip_b    | cls       | proto  |      1 | 0.7037 ± 0.0441 | 0.4620 ± 0.0418 | NA           | 0.6090 ± 0.0625 |        5 |
| banana3        | clip_b    | cls       | proto  |      5 | 0.8223 ± 0.0361 | 0.6911 ± 0.0655 | NA           | 0.3539 ± 0.0666 |        5 |
| banana3        | clip_b    | cls       | proto  |     10 | 0.8411 ± 0.0242 | 0.7148 ± 0.0312 | NA           | 0.3157 ± 0.0502 |        5 |
| banana3        | clip_b    | cls       | proto  |     50 | 0.8587 ± 0.0032 | 0.7455 ± 0.0049 | NA           | 0.2854 ± 0.0062 |        5 |
| banana3        | clip_b    | cls       | proto  |    nan | 0.8598 ± 0.0000 | 0.7452 ± 0.0000 | NA           | 0.2809 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | corn   |      1 | 0.7304 ± 0.0469 | 0.4475 ± 0.1383 | NA           | 0.5562 ± 0.1110 |        5 |
| banana3        | dinov2_b  | cls       | corn   |      5 | 0.8519 ± 0.0159 | 0.7311 ± 0.0353 | NA           | 0.2899 ± 0.0314 |        5 |
| banana3        | dinov2_b  | cls       | corn   |     10 | 0.8664 ± 0.0218 | 0.7611 ± 0.0420 | NA           | 0.2618 ± 0.0461 |        5 |
| banana3        | dinov2_b  | cls       | corn   |     50 | 0.9200 ± 0.0068 | 0.8572 ± 0.0128 | NA           | 0.1551 ± 0.0129 |        5 |
| banana3        | dinov2_b  | cls       | corn   |    nan | 0.9570 ± 0.0000 | 0.9231 ± 0.0000 | NA           | 0.0843 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | linear |      1 | 0.6955 ± 0.0860 | 0.4678 ± 0.1041 | NA           | 0.5933 ± 0.1817 |        5 |
| banana3        | dinov2_b  | cls       | linear |      5 | 0.8448 ± 0.0228 | 0.7224 ± 0.0491 | NA           | 0.2966 ± 0.0394 |        5 |
| banana3        | dinov2_b  | cls       | linear |     10 | 0.8734 ± 0.0164 | 0.7730 ± 0.0345 | NA           | 0.2461 ± 0.0326 |        5 |
| banana3        | dinov2_b  | cls       | linear |     50 | 0.9281 ± 0.0106 | 0.8719 ± 0.0175 | NA           | 0.1393 ± 0.0208 |        5 |
| banana3        | dinov2_b  | cls       | linear |    nan | 0.9540 ± 0.0000 | 0.9175 ± 0.0000 | NA           | 0.0899 ± 0.0000 |        5 |
| banana3        | dinov2_b  | cls       | proto  |      1 | 0.6826 ± 0.1035 | 0.4400 ± 0.1393 | NA           | 0.6281 ± 0.1940 |        5 |
| banana3        | dinov2_b  | cls       | proto  |      5 | 0.8573 ± 0.0256 | 0.7315 ± 0.0468 | NA           | 0.2831 ± 0.0554 |        5 |
| banana3        | dinov2_b  | cls       | proto  |     10 | 0.8695 ± 0.0244 | 0.7541 ± 0.0507 | NA           | 0.2596 ± 0.0560 |        5 |
| banana3        | dinov2_b  | cls       | proto  |     50 | 0.9093 ± 0.0079 | 0.8318 ± 0.0200 | NA           | 0.1775 ± 0.0167 |        5 |
| banana3        | dinov2_b  | cls       | proto  |    nan | 0.9272 ± 0.0000 | 0.8649 ± 0.0000 | NA           | 0.1404 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | corn   |      1 | 0.7416 ± 0.0279 | 0.4742 ± 0.1190 | NA           | 0.5416 ± 0.0828 |        5 |
| banana3        | dinov2_s  | cls       | corn   |      5 | 0.8504 ± 0.0131 | 0.7334 ± 0.0293 | NA           | 0.2899 ± 0.0253 |        5 |
| banana3        | dinov2_s  | cls       | corn   |     10 | 0.8748 ± 0.0227 | 0.7784 ± 0.0404 | NA           | 0.2438 ± 0.0447 |        5 |
| banana3        | dinov2_s  | cls       | corn   |     50 | 0.9434 ± 0.0052 | 0.8988 ± 0.0116 | NA           | 0.1112 ± 0.0108 |        5 |
| banana3        | dinov2_s  | cls       | corn   |    nan | 0.9662 ± 0.0000 | 0.9417 ± 0.0000 | NA           | 0.0674 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | linear |      1 | 0.7417 ± 0.0358 | 0.5093 ± 0.0630 | NA           | 0.5236 ± 0.0792 |        5 |
| banana3        | dinov2_s  | cls       | linear |      5 | 0.8455 ± 0.0116 | 0.7232 ± 0.0295 | NA           | 0.2978 ± 0.0186 |        5 |
| banana3        | dinov2_s  | cls       | linear |     10 | 0.8785 ± 0.0164 | 0.7821 ± 0.0317 | NA           | 0.2348 ± 0.0316 |        5 |
| banana3        | dinov2_s  | cls       | linear |     50 | 0.9441 ± 0.0066 | 0.9009 ± 0.0150 | NA           | 0.1101 ± 0.0129 |        5 |
| banana3        | dinov2_s  | cls       | linear |    nan | 0.9718 ± 0.0000 | 0.9537 ± 0.0000 | NA           | 0.0562 ± 0.0000 |        5 |
| banana3        | dinov2_s  | cls       | proto  |      1 | 0.7367 ± 0.0618 | 0.4990 ± 0.1191 | NA           | 0.5472 ± 0.1253 |        5 |
| banana3        | dinov2_s  | cls       | proto  |      5 | 0.8596 ± 0.0216 | 0.7421 ± 0.0408 | NA           | 0.2719 ± 0.0471 |        5 |
| banana3        | dinov2_s  | cls       | proto  |     10 | 0.8779 ± 0.0251 | 0.7737 ± 0.0472 | NA           | 0.2360 ± 0.0513 |        5 |
| banana3        | dinov2_s  | cls       | proto  |     50 | 0.9224 ± 0.0128 | 0.8564 ± 0.0215 | NA           | 0.1494 ± 0.0253 |        5 |
| banana3        | dinov2_s  | cls       | proto  |    nan | 0.9375 ± 0.0000 | 0.8874 ± 0.0000 | NA           | 0.1236 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | corn   |      1 | 0.6890 ± 0.0275 | 0.4498 ± 0.0936 | NA           | 0.6135 ± 0.0671 |        5 |
| banana3        | resnet50  | cls       | corn   |      5 | 0.7483 ± 0.0396 | 0.5743 ± 0.0805 | NA           | 0.4910 ± 0.0768 |        5 |
| banana3        | resnet50  | cls       | corn   |     10 | 0.8073 ± 0.0182 | 0.6771 ± 0.0228 | NA           | 0.3787 ± 0.0410 |        5 |
| banana3        | resnet50  | cls       | corn   |     50 | 0.8841 ± 0.0151 | 0.7809 ± 0.0232 | NA           | 0.2258 ± 0.0290 |        5 |
| banana3        | resnet50  | cls       | corn   |    nan | 0.9295 ± 0.0000 | 0.8630 ± 0.0000 | NA           | 0.1348 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | linear |      1 | 0.6772 ± 0.0323 | 0.4637 ± 0.0828 | NA           | 0.6270 ± 0.0644 |        5 |
| banana3        | resnet50  | cls       | linear |      5 | 0.7525 ± 0.0406 | 0.5950 ± 0.0720 | NA           | 0.4787 ± 0.0773 |        5 |
| banana3        | resnet50  | cls       | linear |     10 | 0.8135 ± 0.0125 | 0.6855 ± 0.0202 | NA           | 0.3629 ± 0.0280 |        5 |
| banana3        | resnet50  | cls       | linear |     50 | 0.8900 ± 0.0108 | 0.7915 ± 0.0155 | NA           | 0.2112 ± 0.0216 |        5 |
| banana3        | resnet50  | cls       | linear |    nan | 0.9409 ± 0.0000 | 0.8859 ± 0.0000 | NA           | 0.1124 ± 0.0000 |        5 |
| banana3        | resnet50  | cls       | proto  |      1 | 0.6776 ± 0.0561 | 0.4672 ± 0.1087 | NA           | 0.6326 ± 0.1106 |        5 |
| banana3        | resnet50  | cls       | proto  |      5 | 0.7467 ± 0.0355 | 0.5723 ± 0.0790 | NA           | 0.5011 ± 0.0738 |        5 |
| banana3        | resnet50  | cls       | proto  |     10 | 0.7953 ± 0.0177 | 0.6685 ± 0.0217 | NA           | 0.4034 ± 0.0367 |        5 |
| banana3        | resnet50  | cls       | proto  |     50 | 0.8401 ± 0.0148 | 0.7133 ± 0.0176 | NA           | 0.3135 ± 0.0321 |        5 |
| banana3        | resnet50  | cls       | proto  |    nan | 0.8452 ± 0.0000 | 0.7295 ± 0.0000 | NA           | 0.3034 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | corn   |      1 | 0.8285 ± 0.0591 | 0.6263 ± 0.1473 | NA           | 0.3629 ± 0.1272 |        5 |
| banana4        | clip_b    | cls       | corn   |      5 | 0.9436 ± 0.0178 | 0.8840 ± 0.0403 | NA           | 0.1167 ± 0.0359 |        5 |
| banana4        | clip_b    | cls       | corn   |     10 | 0.9548 ± 0.0177 | 0.9075 ± 0.0369 | NA           | 0.0960 ± 0.0402 |        5 |
| banana4        | clip_b    | cls       | corn   |     50 | 0.9767 ± 0.0027 | 0.9528 ± 0.0058 | NA           | 0.0483 ± 0.0058 |        5 |
| banana4        | clip_b    | cls       | corn   |    nan | 0.9860 ± 0.0000 | 0.9716 ± 0.0000 | NA           | 0.0292 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | linear |      1 | 0.8285 ± 0.0505 | 0.6200 ± 0.1306 | NA           | 0.3645 ± 0.1062 |        5 |
| banana4        | clip_b    | cls       | linear |      5 | 0.9483 ± 0.0170 | 0.8969 ± 0.0361 | NA           | 0.1066 ± 0.0339 |        5 |
| banana4        | clip_b    | cls       | linear |     10 | 0.9511 ± 0.0237 | 0.8994 ± 0.0509 | NA           | 0.1056 ± 0.0554 |        5 |
| banana4        | clip_b    | cls       | linear |     50 | 0.9778 ± 0.0015 | 0.9551 ± 0.0028 | NA           | 0.0462 ± 0.0030 |        5 |
| banana4        | clip_b    | cls       | linear |    nan | 0.9885 ± 0.0000 | 0.9768 ± 0.0000 | NA           | 0.0239 ± 0.0000 |        5 |
| banana4        | clip_b    | cls       | proto  |      1 | 0.8220 ± 0.0515 | 0.6124 ± 0.1354 | NA           | 0.3788 ± 0.1110 |        5 |
| banana4        | clip_b    | cls       | proto  |      5 | 0.9362 ± 0.0080 | 0.8707 ± 0.0202 | NA           | 0.1326 ± 0.0168 |        5 |
| banana4        | clip_b    | cls       | proto  |     10 | 0.9468 ± 0.0185 | 0.8911 ± 0.0381 | NA           | 0.1130 ± 0.0416 |        5 |
| banana4        | clip_b    | cls       | proto  |     50 | 0.9723 ± 0.0022 | 0.9437 ± 0.0040 | NA           | 0.0578 ± 0.0044 |        5 |
| banana4        | clip_b    | cls       | proto  |    nan | 0.9798 ± 0.0000 | 0.9585 ± 0.0000 | NA           | 0.0424 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | corn   |      1 | 0.8466 ± 0.0903 | 0.7086 ± 0.1403 | NA           | 0.3082 ± 0.1622 |        5 |
| banana4        | dinov2_b  | cls       | corn   |      5 | 0.9527 ± 0.0264 | 0.8993 ± 0.0608 | NA           | 0.0997 ± 0.0569 |        5 |
| banana4        | dinov2_b  | cls       | corn   |     10 | 0.9604 ± 0.0183 | 0.9176 ± 0.0400 | NA           | 0.0838 ± 0.0399 |        5 |
| banana4        | dinov2_b  | cls       | corn   |     50 | 0.9741 ± 0.0015 | 0.9468 ± 0.0030 | NA           | 0.0541 ± 0.0030 |        5 |
| banana4        | dinov2_b  | cls       | corn   |    nan | 0.9872 ± 0.0000 | 0.9742 ± 0.0000 | NA           | 0.0265 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | linear |      1 | 0.8501 ± 0.0931 | 0.7310 ± 0.1459 | NA           | 0.2960 ± 0.1669 |        5 |
| banana4        | dinov2_b  | cls       | linear |      5 | 0.9554 ± 0.0267 | 0.9052 ± 0.0618 | NA           | 0.0939 ± 0.0577 |        5 |
| banana4        | dinov2_b  | cls       | linear |     10 | 0.9664 ± 0.0202 | 0.9303 ± 0.0434 | NA           | 0.0711 ± 0.0435 |        5 |
| banana4        | dinov2_b  | cls       | linear |     50 | 0.9750 ± 0.0021 | 0.9491 ± 0.0045 | NA           | 0.0520 ± 0.0044 |        5 |
| banana4        | dinov2_b  | cls       | linear |    nan | 0.9911 ± 0.0000 | 0.9820 ± 0.0000 | NA           | 0.0186 ± 0.0000 |        5 |
| banana4        | dinov2_b  | cls       | proto  |      1 | 0.8340 ± 0.0987 | 0.7100 ± 0.1556 | NA           | 0.3231 ± 0.1801 |        5 |
| banana4        | dinov2_b  | cls       | proto  |      5 | 0.9325 ± 0.0428 | 0.8476 ± 0.1060 | NA           | 0.1416 ± 0.0893 |        5 |
| banana4        | dinov2_b  | cls       | proto  |     10 | 0.9434 ± 0.0346 | 0.8770 ± 0.0824 | NA           | 0.1199 ± 0.0735 |        5 |
| banana4        | dinov2_b  | cls       | proto  |     50 | 0.9559 ± 0.0057 | 0.9082 ± 0.0122 | NA           | 0.0939 ± 0.0124 |        5 |
| banana4        | dinov2_b  | cls       | proto  |    nan | 0.9528 ± 0.0000 | 0.9014 ± 0.0000 | NA           | 0.1008 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | corn   |      1 | 0.8447 ± 0.0410 | 0.6867 ± 0.0730 | NA           | 0.3257 ± 0.0854 |        5 |
| banana4        | dinov2_s  | cls       | corn   |      5 | 0.9545 ± 0.0207 | 0.9044 ± 0.0464 | NA           | 0.0960 ± 0.0449 |        5 |
| banana4        | dinov2_s  | cls       | corn   |     10 | 0.9636 ± 0.0155 | 0.9255 ± 0.0330 | NA           | 0.0764 ± 0.0335 |        5 |
| banana4        | dinov2_s  | cls       | corn   |     50 | 0.9775 ± 0.0023 | 0.9544 ± 0.0048 | NA           | 0.0467 ± 0.0048 |        5 |
| banana4        | dinov2_s  | cls       | corn   |    nan | 0.9911 ± 0.0000 | 0.9819 ± 0.0000 | NA           | 0.0186 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | linear |      1 | 0.8470 ± 0.0413 | 0.6904 ± 0.0776 | NA           | 0.3231 ± 0.0878 |        5 |
| banana4        | dinov2_s  | cls       | linear |      5 | 0.9560 ± 0.0215 | 0.9080 ± 0.0485 | NA           | 0.0928 ± 0.0466 |        5 |
| banana4        | dinov2_s  | cls       | linear |     10 | 0.9683 ± 0.0137 | 0.9355 ± 0.0287 | NA           | 0.0663 ± 0.0290 |        5 |
| banana4        | dinov2_s  | cls       | linear |     50 | 0.9795 ± 0.0030 | 0.9587 ± 0.0063 | NA           | 0.0424 ± 0.0062 |        5 |
| banana4        | dinov2_s  | cls       | linear |    nan | 0.9923 ± 0.0000 | 0.9846 ± 0.0000 | NA           | 0.0159 ± 0.0000 |        5 |
| banana4        | dinov2_s  | cls       | proto  |      1 | 0.8397 ± 0.0423 | 0.6711 ± 0.0761 | NA           | 0.3379 ± 0.0868 |        5 |
| banana4        | dinov2_s  | cls       | proto  |      5 | 0.9418 ± 0.0324 | 0.8738 ± 0.0753 | NA           | 0.1231 ± 0.0694 |        5 |
| banana4        | dinov2_s  | cls       | proto  |     10 | 0.9514 ± 0.0235 | 0.8983 ± 0.0531 | NA           | 0.1024 ± 0.0506 |        5 |
| banana4        | dinov2_s  | cls       | proto  |     50 | 0.9631 ± 0.0050 | 0.9246 ± 0.0108 | NA           | 0.0775 ± 0.0110 |        5 |
| banana4        | dinov2_s  | cls       | proto  |    nan | 0.9648 ± 0.0000 | 0.9277 ± 0.0000 | NA           | 0.0743 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | corn   |      1 | 0.7940 ± 0.0524 | 0.5915 ± 0.0527 | NA           | 0.4186 ± 0.0961 |        5 |
| banana4        | resnet50  | cls       | corn   |      5 | 0.8820 ± 0.0315 | 0.7469 ± 0.0684 | NA           | 0.2477 ± 0.0604 |        5 |
| banana4        | resnet50  | cls       | corn   |     10 | 0.8993 ± 0.0327 | 0.7814 ± 0.0747 | NA           | 0.2138 ± 0.0661 |        5 |
| banana4        | resnet50  | cls       | corn   |     50 | 0.9313 ± 0.0128 | 0.8527 ± 0.0298 | NA           | 0.1480 ± 0.0280 |        5 |
| banana4        | resnet50  | cls       | corn   |    nan | 0.9796 ± 0.0000 | 0.9588 ± 0.0000 | NA           | 0.0424 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | linear |      1 | 0.7810 ± 0.0650 | 0.5700 ± 0.0804 | NA           | 0.4446 ± 0.1316 |        5 |
| banana4        | resnet50  | cls       | linear |      5 | 0.8806 ± 0.0323 | 0.7479 ± 0.0724 | NA           | 0.2493 ± 0.0638 |        5 |
| banana4        | resnet50  | cls       | linear |     10 | 0.9042 ± 0.0328 | 0.7933 ± 0.0748 | NA           | 0.2027 ± 0.0668 |        5 |
| banana4        | resnet50  | cls       | linear |     50 | 0.9416 ± 0.0152 | 0.8761 ± 0.0342 | NA           | 0.1252 ± 0.0330 |        5 |
| banana4        | resnet50  | cls       | linear |    nan | 0.9834 ± 0.0000 | 0.9665 ± 0.0000 | NA           | 0.0345 ± 0.0000 |        5 |
| banana4        | resnet50  | cls       | proto  |      1 | 0.7888 ± 0.0590 | 0.5834 ± 0.0873 | NA           | 0.4355 ± 0.1203 |        5 |
| banana4        | resnet50  | cls       | proto  |      5 | 0.8669 ± 0.0200 | 0.7084 ± 0.0416 | NA           | 0.2806 ± 0.0353 |        5 |
| banana4        | resnet50  | cls       | proto  |     10 | 0.8815 ± 0.0275 | 0.7369 ± 0.0654 | NA           | 0.2520 ± 0.0536 |        5 |
| banana4        | resnet50  | cls       | proto  |     50 | 0.8811 ± 0.0138 | 0.7352 ± 0.0347 | NA           | 0.2552 ± 0.0274 |        5 |
| banana4        | resnet50  | cls       | proto  |    nan | 0.8828 ± 0.0000 | 0.7412 ± 0.0000 | NA           | 0.2520 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | corn   |      1 | 0.8592 ± 0.0562 | 0.6826 ± 0.1578 | NA           | 0.2876 ± 0.1129 |        5 |
| field4_banana  | clip_b    | cls       | corn   |      5 | 0.8866 ± 0.0701 | 0.7576 ± 0.1495 | NA           | 0.2316 ± 0.1391 |        5 |
| field4_banana  | clip_b    | cls       | corn   |     10 | 0.9202 ± 0.0285 | 0.8308 ± 0.0634 | NA           | 0.1652 ± 0.0605 |        5 |
| field4_banana  | clip_b    | cls       | corn   |     50 | 0.9637 ± 0.0209 | 0.9249 ± 0.0460 | NA           | 0.0744 ± 0.0446 |        5 |
| field4_banana  | clip_b    | cls       | corn   |    nan | 0.9990 ± 0.0000 | 0.9980 ± 0.0000 | NA           | 0.0020 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | linear |      1 | 0.8592 ± 0.0562 | 0.6826 ± 0.1578 | NA           | 0.2876 ± 0.1129 |        5 |
| field4_banana  | clip_b    | cls       | linear |      5 | 0.8866 ± 0.0701 | 0.7576 ± 0.1495 | NA           | 0.2316 ± 0.1391 |        5 |
| field4_banana  | clip_b    | cls       | linear |     10 | 0.9202 ± 0.0285 | 0.8308 ± 0.0634 | NA           | 0.1652 ± 0.0605 |        5 |
| field4_banana  | clip_b    | cls       | linear |     50 | 0.9637 ± 0.0209 | 0.9249 ± 0.0460 | NA           | 0.0744 ± 0.0446 |        5 |
| field4_banana  | clip_b    | cls       | linear |    nan | 0.9990 ± 0.0000 | 0.9980 ± 0.0000 | NA           | 0.0020 ± 0.0000 |        5 |
| field4_banana  | clip_b    | cls       | proto  |      1 | 0.8592 ± 0.0562 | 0.6826 ± 0.1578 | NA           | 0.2876 ± 0.1129 |        5 |
| field4_banana  | clip_b    | cls       | proto  |      5 | 0.8833 ± 0.0707 | 0.7484 ± 0.1544 | NA           | 0.2380 ± 0.1387 |        5 |
| field4_banana  | clip_b    | cls       | proto  |     10 | 0.9135 ± 0.0292 | 0.8149 ± 0.0685 | NA           | 0.1796 ± 0.0632 |        5 |
| field4_banana  | clip_b    | cls       | proto  |     50 | 0.9267 ± 0.0300 | 0.8435 ± 0.0732 | NA           | 0.1520 ± 0.0660 |        5 |
| field4_banana  | clip_b    | cls       | proto  |    nan | 0.9364 ± 0.0000 | 0.8689 ± 0.0000 | NA           | 0.1300 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |      1 | 0.8817 ± 0.0273 | 0.7467 ± 0.0657 | NA           | 0.2440 ± 0.0576 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |      5 | 0.8986 ± 0.0534 | 0.7766 ± 0.1295 | NA           | 0.2104 ± 0.1146 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |     10 | 0.9491 ± 0.0155 | 0.8945 ± 0.0356 | NA           | 0.1044 ± 0.0340 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |     50 | 0.9875 ± 0.0143 | 0.9743 ± 0.0299 | NA           | 0.0256 ± 0.0297 |        5 |
| field4_banana  | dinov2_b  | cls       | corn   |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |      1 | 0.8817 ± 0.0273 | 0.7467 ± 0.0657 | NA           | 0.2440 ± 0.0576 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |      5 | 0.8986 ± 0.0534 | 0.7766 ± 0.1295 | NA           | 0.2104 ± 0.1146 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |     10 | 0.9491 ± 0.0155 | 0.8945 ± 0.0356 | NA           | 0.1044 ± 0.0340 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |     50 | 0.9875 ± 0.0143 | 0.9743 ± 0.0299 | NA           | 0.0256 ± 0.0297 |        5 |
| field4_banana  | dinov2_b  | cls       | linear |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |      1 | 0.8817 ± 0.0273 | 0.7467 ± 0.0657 | NA           | 0.2440 ± 0.0576 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |      5 | 0.8914 ± 0.0613 | 0.7511 ± 0.1544 | NA           | 0.2280 ± 0.1318 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |     10 | 0.9460 ± 0.0186 | 0.8873 ± 0.0439 | NA           | 0.1112 ± 0.0413 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |     50 | 0.9399 ± 0.0513 | 0.8658 ± 0.1271 | NA           | 0.1264 ± 0.1113 |        5 |
| field4_banana  | dinov2_b  | cls       | proto  |    nan | 0.9746 ± 0.0000 | 0.9479 ± 0.0000 | NA           | 0.0520 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |      1 | 0.8330 ± 0.0533 | 0.6217 ± 0.1445 | NA           | 0.3400 ± 0.1018 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |      5 | 0.8958 ± 0.0422 | 0.7704 ± 0.0972 | NA           | 0.2180 ± 0.0889 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |     10 | 0.9463 ± 0.0417 | 0.8918 ± 0.0834 | NA           | 0.1080 ± 0.0833 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |     50 | 0.9824 ± 0.0162 | 0.9638 ± 0.0341 | NA           | 0.0360 ± 0.0338 |        5 |
| field4_banana  | dinov2_s  | cls       | corn   |    nan | 0.9990 ± 0.0000 | 0.9980 ± 0.0000 | NA           | 0.0020 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |      1 | 0.8330 ± 0.0533 | 0.6217 ± 0.1445 | NA           | 0.3400 ± 0.1018 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |      5 | 0.8958 ± 0.0422 | 0.7704 ± 0.0972 | NA           | 0.2180 ± 0.0889 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |     10 | 0.9463 ± 0.0417 | 0.8918 ± 0.0834 | NA           | 0.1080 ± 0.0833 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |     50 | 0.9824 ± 0.0162 | 0.9638 ± 0.0341 | NA           | 0.0360 ± 0.0338 |        5 |
| field4_banana  | dinov2_s  | cls       | linear |    nan | 0.9990 ± 0.0000 | 0.9980 ± 0.0000 | NA           | 0.0020 ± 0.0000 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |      1 | 0.8330 ± 0.0533 | 0.6217 ± 0.1445 | NA           | 0.3400 ± 0.1018 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |      5 | 0.8863 ± 0.0529 | 0.7380 ± 0.1363 | NA           | 0.2400 ± 0.1134 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |     10 | 0.9356 ± 0.0484 | 0.8681 ± 0.0980 | NA           | 0.1308 ± 0.0970 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |     50 | 0.9563 ± 0.0320 | 0.9067 ± 0.0726 | NA           | 0.0912 ± 0.0690 |        5 |
| field4_banana  | dinov2_s  | cls       | proto  |    nan | 0.9727 ± 0.0000 | 0.9438 ± 0.0000 | NA           | 0.0560 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | corn   |      1 | 0.9129 ± 0.0221 | 0.8181 ± 0.0462 | NA           | 0.1788 ± 0.0448 |        5 |
| field4_banana  | resnet50  | cls       | corn   |      5 | 0.9246 ± 0.0178 | 0.8427 ± 0.0411 | NA           | 0.1548 ± 0.0382 |        5 |
| field4_banana  | resnet50  | cls       | corn   |     10 | 0.9170 ± 0.0505 | 0.8263 ± 0.1096 | NA           | 0.1692 ± 0.1035 |        5 |
| field4_banana  | resnet50  | cls       | corn   |     50 | 0.9597 ± 0.0116 | 0.9176 ± 0.0250 | NA           | 0.0820 ± 0.0246 |        5 |
| field4_banana  | resnet50  | cls       | corn   |    nan | 0.9940 ± 0.0000 | 0.9880 ± 0.0000 | NA           | 0.0120 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | linear |      1 | 0.9129 ± 0.0221 | 0.8181 ± 0.0462 | NA           | 0.1788 ± 0.0448 |        5 |
| field4_banana  | resnet50  | cls       | linear |      5 | 0.9246 ± 0.0178 | 0.8427 ± 0.0411 | NA           | 0.1548 ± 0.0382 |        5 |
| field4_banana  | resnet50  | cls       | linear |     10 | 0.9170 ± 0.0505 | 0.8263 ± 0.1096 | NA           | 0.1692 ± 0.1035 |        5 |
| field4_banana  | resnet50  | cls       | linear |     50 | 0.9597 ± 0.0116 | 0.9176 ± 0.0250 | NA           | 0.0820 ± 0.0246 |        5 |
| field4_banana  | resnet50  | cls       | linear |    nan | 0.9940 ± 0.0000 | 0.9880 ± 0.0000 | NA           | 0.0120 ± 0.0000 |        5 |
| field4_banana  | resnet50  | cls       | proto  |      1 | 0.9129 ± 0.0221 | 0.8181 ± 0.0462 | NA           | 0.1788 ± 0.0448 |        5 |
| field4_banana  | resnet50  | cls       | proto  |      5 | 0.9137 ± 0.0184 | 0.8167 ± 0.0440 | NA           | 0.1788 ± 0.0397 |        5 |
| field4_banana  | resnet50  | cls       | proto  |     10 | 0.9010 ± 0.0544 | 0.7908 ± 0.1194 | NA           | 0.2020 ± 0.1099 |        5 |
| field4_banana  | resnet50  | cls       | proto  |     50 | 0.9189 ± 0.0155 | 0.8295 ± 0.0379 | NA           | 0.1672 ± 0.0346 |        5 |
| field4_banana  | resnet50  | cls       | proto  |    nan | 0.9295 ± 0.0000 | 0.8547 ± 0.0000 | NA           | 0.1440 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | corn   |      1 | 0.8813 ± 0.0258 | 0.7469 ± 0.0577 | NA           | 0.2444 ± 0.0518 |        5 |
| field4_mango   | clip_b    | cls       | corn   |      5 | 0.9731 ± 0.0111 | 0.9455 ± 0.0221 | NA           | 0.0544 ± 0.0221 |        5 |
| field4_mango   | clip_b    | cls       | corn   |     10 | 0.9851 ± 0.0113 | 0.9695 ± 0.0232 | NA           | 0.0304 ± 0.0231 |        5 |
| field4_mango   | clip_b    | cls       | corn   |     50 | 0.9980 ± 0.0027 | 0.9960 ± 0.0055 | NA           | 0.0040 ± 0.0055 |        5 |
| field4_mango   | clip_b    | cls       | corn   |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | linear |      1 | 0.8813 ± 0.0258 | 0.7469 ± 0.0577 | NA           | 0.2444 ± 0.0518 |        5 |
| field4_mango   | clip_b    | cls       | linear |      5 | 0.9731 ± 0.0111 | 0.9455 ± 0.0221 | NA           | 0.0544 ± 0.0221 |        5 |
| field4_mango   | clip_b    | cls       | linear |     10 | 0.9851 ± 0.0113 | 0.9695 ± 0.0232 | NA           | 0.0304 ± 0.0231 |        5 |
| field4_mango   | clip_b    | cls       | linear |     50 | 0.9980 ± 0.0027 | 0.9960 ± 0.0055 | NA           | 0.0040 ± 0.0055 |        5 |
| field4_mango   | clip_b    | cls       | linear |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | clip_b    | cls       | proto  |      1 | 0.8813 ± 0.0258 | 0.7469 ± 0.0577 | NA           | 0.2444 ± 0.0518 |        5 |
| field4_mango   | clip_b    | cls       | proto  |      5 | 0.9700 ± 0.0116 | 0.9391 ± 0.0230 | NA           | 0.0608 ± 0.0230 |        5 |
| field4_mango   | clip_b    | cls       | proto  |     10 | 0.9815 ± 0.0159 | 0.9618 ± 0.0331 | NA           | 0.0380 ± 0.0329 |        5 |
| field4_mango   | clip_b    | cls       | proto  |     50 | 0.9970 ± 0.0034 | 0.9940 ± 0.0068 | NA           | 0.0060 ± 0.0068 |        5 |
| field4_mango   | clip_b    | cls       | proto  |    nan | 0.9990 ± 0.0000 | 0.9980 ± 0.0000 | NA           | 0.0020 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |      1 | 0.9312 ± 0.0821 | 0.8513 ± 0.1829 | NA           | 0.1396 ± 0.1664 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |      5 | 0.9936 ± 0.0083 | 0.9872 ± 0.0166 | NA           | 0.0128 ± 0.0166 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |     10 | 0.9982 ± 0.0019 | 0.9964 ± 0.0038 | NA           | 0.0036 ± 0.0038 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |     50 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | corn   |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |      1 | 0.9312 ± 0.0821 | 0.8513 ± 0.1829 | NA           | 0.1396 ± 0.1664 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |      5 | 0.9936 ± 0.0083 | 0.9872 ± 0.0166 | NA           | 0.0128 ± 0.0166 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |     10 | 0.9982 ± 0.0019 | 0.9964 ± 0.0038 | NA           | 0.0036 ± 0.0038 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |     50 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | linear |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |      1 | 0.9312 ± 0.0821 | 0.8513 ± 0.1829 | NA           | 0.1396 ± 0.1664 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |      5 | 0.9923 ± 0.0071 | 0.9844 ± 0.0145 | NA           | 0.0156 ± 0.0144 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |     10 | 0.9982 ± 0.0013 | 0.9964 ± 0.0026 | NA           | 0.0036 ± 0.0026 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |     50 | 0.9998 ± 0.0004 | 0.9996 ± 0.0009 | NA           | 0.0004 ± 0.0009 |        5 |
| field4_mango   | dinov2_b  | cls       | proto  |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |      1 | 0.9111 ± 0.0524 | 0.8190 ± 0.1036 | NA           | 0.1800 ± 0.1038 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |      5 | 0.9833 ± 0.0134 | 0.9664 ± 0.0267 | NA           | 0.0336 ± 0.0267 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |     10 | 0.9956 ± 0.0032 | 0.9912 ± 0.0064 | NA           | 0.0088 ± 0.0064 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |     50 | 0.9996 ± 0.0005 | 0.9992 ± 0.0011 | NA           | 0.0008 ± 0.0011 |        5 |
| field4_mango   | dinov2_s  | cls       | corn   |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |      1 | 0.9111 ± 0.0524 | 0.8190 ± 0.1036 | NA           | 0.1800 ± 0.1038 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |      5 | 0.9833 ± 0.0134 | 0.9664 ± 0.0267 | NA           | 0.0336 ± 0.0267 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |     10 | 0.9956 ± 0.0032 | 0.9912 ± 0.0064 | NA           | 0.0088 ± 0.0064 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |     50 | 0.9996 ± 0.0005 | 0.9992 ± 0.0011 | NA           | 0.0008 ± 0.0011 |        5 |
| field4_mango   | dinov2_s  | cls       | linear |    nan | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | NA           | 0.0000 ± 0.0000 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |      1 | 0.9111 ± 0.0524 | 0.8190 ± 0.1036 | NA           | 0.1800 ± 0.1038 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |      5 | 0.9861 ± 0.0093 | 0.9720 ± 0.0187 | NA           | 0.0280 ± 0.0187 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |     10 | 0.9956 ± 0.0032 | 0.9912 ± 0.0064 | NA           | 0.0088 ± 0.0064 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |     50 | 0.9994 ± 0.0005 | 0.9988 ± 0.0011 | NA           | 0.0012 ± 0.0011 |        5 |
| field4_mango   | dinov2_s  | cls       | proto  |    nan | 0.9980 ± 0.0000 | 0.9960 ± 0.0000 | NA           | 0.0040 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | corn   |      1 | 0.8667 ± 0.0623 | 0.7115 ± 0.1514 | NA           | 0.2692 ± 0.1264 |        5 |
| field4_mango   | resnet50  | cls       | corn   |      5 | 0.9634 ± 0.0219 | 0.9258 ± 0.0444 | NA           | 0.0740 ± 0.0442 |        5 |
| field4_mango   | resnet50  | cls       | corn   |     10 | 0.9820 ± 0.0156 | 0.9631 ± 0.0325 | NA           | 0.0368 ± 0.0323 |        5 |
| field4_mango   | resnet50  | cls       | corn   |     50 | 0.9942 ± 0.0037 | 0.9884 ± 0.0074 | NA           | 0.0116 ± 0.0074 |        5 |
| field4_mango   | resnet50  | cls       | corn   |    nan | 0.9990 ± 0.0000 | 0.9980 ± 0.0000 | NA           | 0.0020 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | linear |      1 | 0.8667 ± 0.0623 | 0.7115 ± 0.1514 | NA           | 0.2692 ± 0.1264 |        5 |
| field4_mango   | resnet50  | cls       | linear |      5 | 0.9634 ± 0.0219 | 0.9258 ± 0.0444 | NA           | 0.0740 ± 0.0442 |        5 |
| field4_mango   | resnet50  | cls       | linear |     10 | 0.9820 ± 0.0156 | 0.9631 ± 0.0325 | NA           | 0.0368 ± 0.0323 |        5 |
| field4_mango   | resnet50  | cls       | linear |     50 | 0.9942 ± 0.0037 | 0.9884 ± 0.0074 | NA           | 0.0116 ± 0.0074 |        5 |
| field4_mango   | resnet50  | cls       | linear |    nan | 0.9990 ± 0.0000 | 0.9980 ± 0.0000 | NA           | 0.0020 ± 0.0000 |        5 |
| field4_mango   | resnet50  | cls       | proto  |      1 | 0.8667 ± 0.0623 | 0.7115 ± 0.1514 | NA           | 0.2692 ± 0.1264 |        5 |
| field4_mango   | resnet50  | cls       | proto  |      5 | 0.9501 ± 0.0307 | 0.8969 ± 0.0650 | NA           | 0.1020 ± 0.0638 |        5 |
| field4_mango   | resnet50  | cls       | proto  |     10 | 0.9778 ± 0.0211 | 0.9540 ± 0.0449 | NA           | 0.0456 ± 0.0442 |        5 |
| field4_mango   | resnet50  | cls       | proto  |     50 | 0.9852 ± 0.0064 | 0.9700 ± 0.0131 | NA           | 0.0300 ± 0.0130 |        5 |
| field4_mango   | resnet50  | cls       | proto  |    nan | 0.9950 ± 0.0000 | 0.9900 ± 0.0000 | NA           | 0.0100 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |      1 | 0.5964 ± 0.0561 | 0.3601 ± 0.0773 | NA           | 0.7585 ± 0.1232 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |      5 | 0.6746 ± 0.0485 | 0.4443 ± 0.0774 | NA           | 0.6142 ± 0.0699 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |     10 | 0.7098 ± 0.0328 | 0.5102 ± 0.0492 | NA           | 0.5623 ± 0.0627 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |     50 | 0.7866 ± 0.0288 | 0.6392 ± 0.0372 | NA           | 0.4264 ± 0.0528 |        5 |
| fruit12_apple  | clip_b    | cls       | corn   |    nan | 0.8650 ± 0.0000 | 0.7764 ± 0.0000 | NA           | 0.2358 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |      1 | 0.5931 ± 0.0583 | 0.3533 ± 0.0812 | NA           | 0.7726 ± 0.1286 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |      5 | 0.6794 ± 0.0477 | 0.4540 ± 0.0805 | NA           | 0.6038 ± 0.0690 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |     10 | 0.7144 ± 0.0327 | 0.5219 ± 0.0526 | NA           | 0.5519 ± 0.0610 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |     50 | 0.7992 ± 0.0266 | 0.6536 ± 0.0315 | NA           | 0.4028 ± 0.0494 |        5 |
| fruit12_apple  | clip_b    | cls       | linear |    nan | 0.8914 ± 0.0000 | 0.8163 ± 0.0000 | NA           | 0.1934 ± 0.0000 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |      1 | 0.5965 ± 0.0548 | 0.3625 ± 0.0761 | NA           | 0.7547 ± 0.1209 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |      5 | 0.6681 ± 0.0488 | 0.4338 ± 0.0830 | NA           | 0.6245 ± 0.0691 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |     10 | 0.6922 ± 0.0271 | 0.4796 ± 0.0288 | NA           | 0.5868 ± 0.0633 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |     50 | 0.7681 ± 0.0228 | 0.5960 ± 0.0328 | NA           | 0.4670 ± 0.0487 |        5 |
| fruit12_apple  | clip_b    | cls       | proto  |    nan | 0.7783 ± 0.0000 | 0.6281 ± 0.0000 | NA           | 0.4387 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |      1 | 0.6182 ± 0.0860 | 0.3895 ± 0.1155 | NA           | 0.6613 ± 0.1717 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |      5 | 0.7407 ± 0.0673 | 0.5647 ± 0.0897 | NA           | 0.4821 ± 0.1007 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |     10 | 0.7865 ± 0.0267 | 0.6391 ± 0.0251 | NA           | 0.4142 ± 0.0653 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |     50 | 0.8468 ± 0.0167 | 0.7365 ± 0.0204 | NA           | 0.2943 ± 0.0303 |        5 |
| fruit12_apple  | dinov2_b  | cls       | corn   |    nan | 0.8889 ± 0.0000 | 0.8103 ± 0.0000 | NA           | 0.1981 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |      1 | 0.5982 ± 0.0909 | 0.3736 ± 0.1250 | NA           | 0.7000 ± 0.1775 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |      5 | 0.7350 ± 0.0583 | 0.5591 ± 0.0764 | NA           | 0.4962 ± 0.0948 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |     10 | 0.7862 ± 0.0262 | 0.6463 ± 0.0272 | NA           | 0.4142 ± 0.0567 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |     50 | 0.8565 ± 0.0187 | 0.7492 ± 0.0253 | NA           | 0.2830 ± 0.0340 |        5 |
| fruit12_apple  | dinov2_b  | cls       | linear |    nan | 0.8891 ± 0.0000 | 0.8216 ± 0.0000 | NA           | 0.1981 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |      1 | 0.5851 ± 0.0854 | 0.3602 ± 0.1208 | NA           | 0.7113 ± 0.1804 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |      5 | 0.7201 ± 0.0777 | 0.5427 ± 0.0887 | NA           | 0.5226 ± 0.1292 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |     10 | 0.7554 ± 0.0317 | 0.5932 ± 0.0401 | NA           | 0.4764 ± 0.0652 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |     50 | 0.8232 ± 0.0226 | 0.6965 ± 0.0343 | NA           | 0.3415 ± 0.0411 |        5 |
| fruit12_apple  | dinov2_b  | cls       | proto  |    nan | 0.8502 ± 0.0000 | 0.7430 ± 0.0000 | NA           | 0.2783 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |      1 | 0.6379 ± 0.0609 | 0.4226 ± 0.0805 | NA           | 0.6349 ± 0.1082 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |      5 | 0.7388 ± 0.0770 | 0.5645 ± 0.1164 | NA           | 0.4736 ± 0.1127 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |     10 | 0.7952 ± 0.0327 | 0.6559 ± 0.0316 | NA           | 0.4009 ± 0.0705 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |     50 | 0.8550 ± 0.0163 | 0.7461 ± 0.0231 | NA           | 0.2830 ± 0.0315 |        5 |
| fruit12_apple  | dinov2_s  | cls       | corn   |    nan | 0.8927 ± 0.0000 | 0.8052 ± 0.0000 | NA           | 0.1981 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |      1 | 0.6331 ± 0.0676 | 0.4178 ± 0.0937 | NA           | 0.6462 ± 0.1159 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |      5 | 0.7254 ± 0.0797 | 0.5537 ± 0.1055 | NA           | 0.5038 ± 0.1229 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |     10 | 0.7935 ± 0.0308 | 0.6603 ± 0.0301 | NA           | 0.4038 ± 0.0659 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |     50 | 0.8512 ± 0.0139 | 0.7477 ± 0.0156 | NA           | 0.2887 ± 0.0255 |        5 |
| fruit12_apple  | dinov2_s  | cls       | linear |    nan | 0.8937 ± 0.0000 | 0.8069 ± 0.0000 | NA           | 0.1981 ± 0.0000 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |      1 | 0.6244 ± 0.0889 | 0.4072 ± 0.1040 | NA           | 0.6623 ± 0.1891 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |      5 | 0.7308 ± 0.0816 | 0.5572 ± 0.1136 | NA           | 0.4906 ± 0.1303 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |     10 | 0.7785 ± 0.0328 | 0.6239 ± 0.0302 | NA           | 0.4321 ± 0.0627 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |     50 | 0.8232 ± 0.0198 | 0.6960 ± 0.0306 | NA           | 0.3425 ± 0.0395 |        5 |
| fruit12_apple  | dinov2_s  | cls       | proto  |    nan | 0.8432 ± 0.0000 | 0.7325 ± 0.0000 | NA           | 0.2972 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |      1 | 0.5647 ± 0.1165 | 0.3463 ± 0.1284 | NA           | 0.7708 ± 0.1685 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |      5 | 0.7099 ± 0.0705 | 0.5089 ± 0.1076 | NA           | 0.5500 ± 0.0966 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |     10 | 0.7811 ± 0.0208 | 0.6231 ± 0.0217 | NA           | 0.4509 ± 0.0512 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |     50 | 0.8200 ± 0.0127 | 0.6923 ± 0.0131 | NA           | 0.3538 ± 0.0160 |        5 |
| fruit12_apple  | resnet50  | cls       | corn   |    nan | 0.8741 ± 0.0000 | 0.7956 ± 0.0000 | NA           | 0.2217 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |      1 | 0.5448 ± 0.0959 | 0.3210 ± 0.1118 | NA           | 0.8236 ± 0.1392 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |      5 | 0.7165 ± 0.0684 | 0.5246 ± 0.1034 | NA           | 0.5368 ± 0.0928 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |     10 | 0.7828 ± 0.0239 | 0.6271 ± 0.0287 | NA           | 0.4443 ± 0.0570 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |     50 | 0.8278 ± 0.0224 | 0.7061 ± 0.0243 | NA           | 0.3406 ± 0.0394 |        5 |
| fruit12_apple  | resnet50  | cls       | linear |    nan | 0.8918 ± 0.0000 | 0.8348 ± 0.0000 | NA           | 0.1887 ± 0.0000 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |      1 | 0.5584 ± 0.1045 | 0.3398 ± 0.1178 | NA           | 0.7915 ± 0.1647 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |      5 | 0.6919 ± 0.0773 | 0.4813 ± 0.1108 | NA           | 0.5840 ± 0.1179 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |     10 | 0.7579 ± 0.0469 | 0.5978 ± 0.0567 | NA           | 0.4896 ± 0.0991 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |     50 | 0.8137 ± 0.0230 | 0.6768 ± 0.0542 | NA           | 0.3736 ± 0.0652 |        5 |
| fruit12_apple  | resnet50  | cls       | proto  |    nan | 0.8360 ± 0.0000 | 0.7362 ± 0.0000 | NA           | 0.3019 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |      1 | 0.5966 ± 0.0146 | 0.3286 ± 0.0412 | NA           | 0.7011 ± 0.0762 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |      5 | 0.6515 ± 0.0351 | 0.4079 ± 0.0412 | NA           | 0.5729 ± 0.0580 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |     10 | 0.6974 ± 0.0410 | 0.4767 ± 0.0673 | NA           | 0.4869 ± 0.0970 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |     50 | 0.7939 ± 0.0195 | 0.6366 ± 0.0261 | NA           | 0.2841 ± 0.0421 |        5 |
| fruit12_banana | clip_b    | cls       | corn   |    nan | 0.8550 ± 0.0000 | 0.7196 ± 0.0000 | NA           | 0.1114 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | linear |      1 | 0.5909 ± 0.0155 | 0.3195 ± 0.0607 | NA           | 0.7154 ± 0.1138 |        5 |
| fruit12_banana | clip_b    | cls       | linear |      5 | 0.6570 ± 0.0307 | 0.4188 ± 0.0396 | NA           | 0.5564 ± 0.0579 |        5 |
| fruit12_banana | clip_b    | cls       | linear |     10 | 0.7033 ± 0.0343 | 0.4972 ± 0.0511 | NA           | 0.4560 ± 0.0815 |        5 |
| fruit12_banana | clip_b    | cls       | linear |     50 | 0.8053 ± 0.0217 | 0.6570 ± 0.0253 | NA           | 0.2642 ± 0.0427 |        5 |
| fruit12_banana | clip_b    | cls       | linear |    nan | 0.8715 ± 0.0000 | 0.7832 ± 0.0000 | NA           | 0.0970 ± 0.0000 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |      1 | 0.5976 ± 0.0137 | 0.3346 ± 0.0467 | NA           | 0.6910 ± 0.0864 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |      5 | 0.6473 ± 0.0330 | 0.4029 ± 0.0364 | NA           | 0.5854 ± 0.0435 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |     10 | 0.6804 ± 0.0384 | 0.4521 ± 0.0677 | NA           | 0.5222 ± 0.1104 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |     50 | 0.7795 ± 0.0138 | 0.6146 ± 0.0143 | NA           | 0.3095 ± 0.0348 |        5 |
| fruit12_banana | clip_b    | cls       | proto  |    nan | 0.7698 ± 0.0000 | 0.6028 ± 0.0000 | NA           | 0.3593 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |      1 | 0.6410 ± 0.0593 | 0.3900 ± 0.1170 | NA           | 0.5971 ± 0.1733 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |      5 | 0.7391 ± 0.0481 | 0.5357 ± 0.0804 | NA           | 0.4127 ± 0.1258 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |     10 | 0.7635 ± 0.0321 | 0.6024 ± 0.0451 | NA           | 0.3277 ± 0.0474 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |     50 | 0.8429 ± 0.0195 | 0.7280 ± 0.0200 | NA           | 0.1892 ± 0.0232 |        5 |
| fruit12_banana | dinov2_b  | cls       | corn   |    nan | 0.8685 ± 0.0000 | 0.7927 ± 0.0000 | NA           | 0.0850 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |      1 | 0.6397 ± 0.0586 | 0.3874 ± 0.1237 | NA           | 0.5959 ± 0.1623 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |      5 | 0.7459 ± 0.0500 | 0.5541 ± 0.0847 | NA           | 0.3907 ± 0.1380 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |     10 | 0.7737 ± 0.0263 | 0.6217 ± 0.0348 | NA           | 0.3073 ± 0.0419 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |     50 | 0.8521 ± 0.0145 | 0.7497 ± 0.0152 | NA           | 0.1684 ± 0.0172 |        5 |
| fruit12_banana | dinov2_b  | cls       | linear |    nan | 0.8726 ± 0.0000 | 0.8187 ± 0.0000 | NA           | 0.0838 ± 0.0000 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |      1 | 0.6335 ± 0.0381 | 0.3854 ± 0.1019 | NA           | 0.6036 ± 0.1486 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |      5 | 0.7291 ± 0.0485 | 0.5262 ± 0.0750 | NA           | 0.4271 ± 0.1152 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |     10 | 0.7598 ± 0.0409 | 0.5980 ± 0.0632 | NA           | 0.3265 ± 0.0576 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |     50 | 0.8102 ± 0.0144 | 0.6859 ± 0.0215 | NA           | 0.2307 ± 0.0242 |        5 |
| fruit12_banana | dinov2_b  | cls       | proto  |    nan | 0.8071 ± 0.0000 | 0.6829 ± 0.0000 | NA           | 0.2323 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |      1 | 0.6521 ± 0.0476 | 0.3803 ± 0.0881 | NA           | 0.6067 ± 0.1371 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |      5 | 0.7649 ± 0.0479 | 0.5643 ± 0.0846 | NA           | 0.3749 ± 0.1256 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |     10 | 0.7806 ± 0.0291 | 0.6113 ± 0.0468 | NA           | 0.3085 ± 0.0482 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |     50 | 0.8470 ± 0.0179 | 0.7191 ± 0.0288 | NA           | 0.2072 ± 0.0318 |        5 |
| fruit12_banana | dinov2_s  | cls       | corn   |    nan | 0.9079 ± 0.0000 | 0.8308 ± 0.0000 | NA           | 0.0790 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |      1 | 0.6475 ± 0.0538 | 0.3711 ± 0.0984 | NA           | 0.6204 ± 0.1373 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |      5 | 0.7748 ± 0.0498 | 0.5841 ± 0.0918 | NA           | 0.3547 ± 0.1387 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |     10 | 0.7917 ± 0.0247 | 0.6277 ± 0.0545 | NA           | 0.2934 ± 0.0710 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |     50 | 0.8587 ± 0.0141 | 0.7459 ± 0.0244 | NA           | 0.1799 ± 0.0256 |        5 |
| fruit12_banana | dinov2_s  | cls       | linear |    nan | 0.9303 ± 0.0000 | 0.8814 ± 0.0000 | NA           | 0.0635 ± 0.0000 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |      1 | 0.6501 ± 0.0439 | 0.3785 ± 0.0946 | NA           | 0.6113 ± 0.1264 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |      5 | 0.7551 ± 0.0420 | 0.5519 ± 0.0735 | NA           | 0.3863 ± 0.1151 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |     10 | 0.7825 ± 0.0394 | 0.6126 ± 0.0621 | NA           | 0.3023 ± 0.0595 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |     50 | 0.8355 ± 0.0242 | 0.6971 ± 0.0349 | NA           | 0.2259 ± 0.0396 |        5 |
| fruit12_banana | dinov2_s  | cls       | proto  |    nan | 0.8331 ± 0.0000 | 0.6894 ± 0.0000 | NA           | 0.2335 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |      1 | 0.6171 ± 0.0261 | 0.3409 ± 0.0396 | NA           | 0.6778 ± 0.0901 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |      5 | 0.6892 ± 0.0315 | 0.4651 ± 0.0816 | NA           | 0.5083 ± 0.1242 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |     10 | 0.7213 ± 0.0715 | 0.5044 ± 0.1109 | NA           | 0.4582 ± 0.1575 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |     50 | 0.8216 ± 0.0153 | 0.6715 ± 0.0206 | NA           | 0.2460 ± 0.0285 |        5 |
| fruit12_banana | resnet50  | cls       | corn   |    nan | 0.9007 ± 0.0000 | 0.8069 ± 0.0000 | NA           | 0.0898 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | linear |      1 | 0.6166 ± 0.0237 | 0.3376 ± 0.0350 | NA           | 0.6910 ± 0.0951 |        5 |
| fruit12_banana | resnet50  | cls       | linear |      5 | 0.6983 ± 0.0352 | 0.4782 ± 0.0808 | NA           | 0.4980 ± 0.1231 |        5 |
| fruit12_banana | resnet50  | cls       | linear |     10 | 0.7340 ± 0.0703 | 0.5306 ± 0.1008 | NA           | 0.4249 ± 0.1471 |        5 |
| fruit12_banana | resnet50  | cls       | linear |     50 | 0.8321 ± 0.0136 | 0.6945 ± 0.0162 | NA           | 0.2235 ± 0.0237 |        5 |
| fruit12_banana | resnet50  | cls       | linear |    nan | 0.9100 ± 0.0000 | 0.8442 ± 0.0000 | NA           | 0.0802 ± 0.0000 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |      1 | 0.6177 ± 0.0186 | 0.3420 ± 0.0359 | NA           | 0.6781 ± 0.0969 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |      5 | 0.6824 ± 0.0388 | 0.4473 ± 0.0881 | NA           | 0.5334 ± 0.1385 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |     10 | 0.6901 ± 0.0733 | 0.4499 ± 0.1196 | NA           | 0.5418 ± 0.1758 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |     50 | 0.7445 ± 0.0407 | 0.5550 ± 0.0641 | NA           | 0.4163 ± 0.1042 |        5 |
| fruit12_banana | resnet50  | cls       | proto  |    nan | 0.7346 ± 0.0000 | 0.5715 ± 0.0000 | NA           | 0.4323 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |      1 | 0.6350 ± 0.0788 | 0.4146 ± 0.0796 | NA           | 0.7406 ± 0.1445 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |      5 | 0.7589 ± 0.0249 | 0.6210 ± 0.0444 | NA           | 0.4841 ± 0.0484 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |     10 | 0.7935 ± 0.0248 | 0.6709 ± 0.0609 | NA           | 0.4174 ± 0.0524 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |     50 | 0.8629 ± 0.0152 | 0.7944 ± 0.0308 | NA           | 0.2754 ± 0.0312 |        5 |
| fruit12_mango  | clip_b    | cls       | corn   |    nan | 0.8773 ± 0.0000 | 0.8130 ± 0.0000 | NA           | 0.2464 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |      1 | 0.6334 ± 0.0889 | 0.4169 ± 0.0845 | NA           | 0.7493 ± 0.1739 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |      5 | 0.7632 ± 0.0186 | 0.6413 ± 0.0471 | NA           | 0.4754 ± 0.0364 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |     10 | 0.8087 ± 0.0320 | 0.6978 ± 0.0556 | NA           | 0.3855 ± 0.0639 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |     50 | 0.8739 ± 0.0221 | 0.8062 ± 0.0418 | NA           | 0.2536 ± 0.0455 |        5 |
| fruit12_mango  | clip_b    | cls       | linear |    nan | 0.8885 ± 0.0000 | 0.8347 ± 0.0000 | NA           | 0.2246 ± 0.0000 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |      1 | 0.6318 ± 0.0776 | 0.4091 ± 0.0806 | NA           | 0.7522 ± 0.1501 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |      5 | 0.7466 ± 0.0287 | 0.6042 ± 0.0596 | NA           | 0.5130 ± 0.0614 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |     10 | 0.7720 ± 0.0298 | 0.6298 ± 0.0759 | NA           | 0.4609 ± 0.0645 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |     50 | 0.8451 ± 0.0129 | 0.7615 ± 0.0231 | NA           | 0.3101 ± 0.0253 |        5 |
| fruit12_mango  | clip_b    | cls       | proto  |    nan | 0.8334 ± 0.0000 | 0.7525 ± 0.0000 | NA           | 0.3333 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |      1 | 0.7184 ± 0.0583 | 0.5079 ± 0.1124 | NA           | 0.5623 ± 0.1080 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |      5 | 0.8390 ± 0.0197 | 0.7320 ± 0.0397 | NA           | 0.3290 ± 0.0364 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |     10 | 0.8587 ± 0.0149 | 0.7645 ± 0.0288 | NA           | 0.2884 ± 0.0318 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |     50 | 0.9218 ± 0.0181 | 0.8727 ± 0.0262 | NA           | 0.1580 ± 0.0367 |        5 |
| fruit12_mango  | dinov2_b  | cls       | corn   |    nan | 0.9293 ± 0.0000 | 0.8849 ± 0.0000 | NA           | 0.1449 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |      1 | 0.7066 ± 0.0564 | 0.4995 ± 0.1025 | NA           | 0.5768 ± 0.0959 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |      5 | 0.8328 ± 0.0248 | 0.7275 ± 0.0288 | NA           | 0.3435 ± 0.0529 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |     10 | 0.8646 ± 0.0209 | 0.7766 ± 0.0248 | NA           | 0.2768 ± 0.0448 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |     50 | 0.9280 ± 0.0172 | 0.8802 ± 0.0259 | NA           | 0.1464 ± 0.0356 |        5 |
| fruit12_mango  | dinov2_b  | cls       | linear |    nan | 0.9360 ± 0.0000 | 0.8924 ± 0.0000 | NA           | 0.1304 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |      1 | 0.7100 ± 0.0539 | 0.5004 ± 0.0970 | NA           | 0.5725 ± 0.0914 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |      5 | 0.8366 ± 0.0198 | 0.7316 ± 0.0278 | NA           | 0.3319 ± 0.0371 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |     10 | 0.8479 ± 0.0133 | 0.7464 ± 0.0239 | NA           | 0.3072 ± 0.0254 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |     50 | 0.8932 ± 0.0224 | 0.8338 ± 0.0404 | NA           | 0.2159 ± 0.0454 |        5 |
| fruit12_mango  | dinov2_b  | cls       | proto  |    nan | 0.8825 ± 0.0000 | 0.8263 ± 0.0000 | NA           | 0.2391 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |      1 | 0.7310 ± 0.0569 | 0.5254 ± 0.1419 | NA           | 0.5362 ± 0.0963 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |      5 | 0.8458 ± 0.0176 | 0.7388 ± 0.0388 | NA           | 0.3145 ± 0.0385 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |     10 | 0.8725 ± 0.0148 | 0.7855 ± 0.0148 | NA           | 0.2594 ± 0.0287 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |     50 | 0.9260 ± 0.0226 | 0.8773 ± 0.0371 | NA           | 0.1507 ± 0.0457 |        5 |
| fruit12_mango  | dinov2_s  | cls       | corn   |    nan | 0.9142 ± 0.0000 | 0.8561 ± 0.0000 | NA           | 0.1739 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |      1 | 0.7226 ± 0.0675 | 0.5211 ± 0.1358 | NA           | 0.5507 ± 0.1123 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |      5 | 0.8373 ± 0.0077 | 0.7295 ± 0.0254 | NA           | 0.3319 ± 0.0173 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |     10 | 0.8658 ± 0.0182 | 0.7763 ± 0.0148 | NA           | 0.2739 ± 0.0392 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |     50 | 0.9352 ± 0.0174 | 0.8899 ± 0.0275 | NA           | 0.1319 ± 0.0356 |        5 |
| fruit12_mango  | dinov2_s  | cls       | linear |    nan | 0.9470 ± 0.0000 | 0.9066 ± 0.0000 | NA           | 0.1087 ± 0.0000 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |      1 | 0.7261 ± 0.0557 | 0.5179 ± 0.1382 | NA           | 0.5464 ± 0.0948 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |      5 | 0.8470 ± 0.0193 | 0.7416 ± 0.0429 | NA           | 0.3116 ± 0.0419 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |     10 | 0.8587 ± 0.0075 | 0.7574 ± 0.0379 | NA           | 0.2870 ± 0.0175 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |     50 | 0.9098 ± 0.0299 | 0.8506 ± 0.0568 | NA           | 0.1826 ± 0.0609 |        5 |
| fruit12_mango  | dinov2_s  | cls       | proto  |    nan | 0.9001 ± 0.0000 | 0.8355 ± 0.0000 | NA           | 0.2029 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |      1 | 0.6695 ± 0.0819 | 0.4693 ± 0.1118 | NA           | 0.6652 ± 0.1515 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |      5 | 0.8036 ± 0.0428 | 0.6895 ± 0.0636 | NA           | 0.3971 ± 0.0844 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |     10 | 0.8353 ± 0.0316 | 0.7282 ± 0.0567 | NA           | 0.3362 ± 0.0627 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |     50 | 0.8977 ± 0.0165 | 0.8473 ± 0.0157 | NA           | 0.2043 ± 0.0313 |        5 |
| fruit12_mango  | resnet50  | cls       | corn   |    nan | 0.9238 ± 0.0000 | 0.8767 ± 0.0000 | NA           | 0.1522 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |      1 | 0.6690 ± 0.0796 | 0.4736 ± 0.1022 | NA           | 0.6768 ± 0.1724 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |      5 | 0.8008 ± 0.0453 | 0.6997 ± 0.0751 | NA           | 0.4000 ± 0.0923 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |     10 | 0.8340 ± 0.0320 | 0.7357 ± 0.0555 | NA           | 0.3362 ± 0.0623 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |     50 | 0.9061 ± 0.0096 | 0.8590 ± 0.0082 | NA           | 0.1870 ± 0.0188 |        5 |
| fruit12_mango  | resnet50  | cls       | linear |    nan | 0.9271 ± 0.0000 | 0.8836 ± 0.0000 | NA           | 0.1449 ± 0.0000 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |      1 | 0.6720 ± 0.0823 | 0.4712 ± 0.1113 | NA           | 0.6623 ± 0.1525 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |      5 | 0.7886 ± 0.0409 | 0.6578 ± 0.0535 | NA           | 0.4275 ± 0.0800 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |     10 | 0.8105 ± 0.0316 | 0.6804 ± 0.0410 | NA           | 0.3855 ± 0.0590 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |     50 | 0.8704 ± 0.0125 | 0.8037 ± 0.0178 | NA           | 0.2594 ± 0.0258 |        5 |
| fruit12_mango  | resnet50  | cls       | proto  |    nan | 0.8723 ± 0.0000 | 0.8181 ± 0.0000 | NA           | 0.2536 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | corn   |      1 | 0.5469 ± 0.0745 | 0.3752 ± 0.1044 | NA           | 0.5288 ± 0.3378 |        5 |
| mango_khir     | clip_b    | cls       | corn   |      5 | 0.6766 ± 0.1425 | 0.5287 ± 0.1699 | NA           | 0.2260 ± 0.1470 |        5 |
| mango_khir     | clip_b    | cls       | corn   |     10 | 0.6306 ± 0.1136 | 0.4978 ± 0.1324 | NA           | 0.2411 ± 0.1487 |        5 |
| mango_khir     | clip_b    | cls       | corn   |     50 | 0.6331 ± 0.0070 | 0.5959 ± 0.0167 | NA           | 0.0452 ± 0.0038 |        5 |
| mango_khir     | clip_b    | cls       | corn   |    nan | 0.3263 ± 0.0000 | 0.3215 ± 0.0000 | NA           | 0.0822 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | linear |      1 | 0.5372 ± 0.0632 | 0.3565 ± 0.0970 | NA           | 0.5397 ± 0.3010 |        5 |
| mango_khir     | clip_b    | cls       | linear |      5 | 0.6424 ± 0.1164 | 0.4886 ± 0.1527 | NA           | 0.2562 ± 0.1404 |        5 |
| mango_khir     | clip_b    | cls       | linear |     10 | 0.7180 ± 0.1407 | 0.5742 ± 0.1832 | NA           | 0.2493 ± 0.1504 |        5 |
| mango_khir     | clip_b    | cls       | linear |     50 | 0.6408 ± 0.0000 | 0.6142 ± 0.0000 | NA           | 0.0411 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | linear |    nan | 0.3263 ± 0.0000 | 0.3215 ± 0.0000 | NA           | 0.0822 ± 0.0000 |        5 |
| mango_khir     | clip_b    | cls       | proto  |      1 | 0.5570 ± 0.0738 | 0.3496 ± 0.1082 | NA           | 0.6288 ± 0.4080 |        5 |
| mango_khir     | clip_b    | cls       | proto  |      5 | 0.6680 ± 0.1463 | 0.5237 ± 0.1861 | NA           | 0.2699 ± 0.1854 |        5 |
| mango_khir     | clip_b    | cls       | proto  |     10 | 0.6490 ± 0.0899 | 0.5036 ± 0.1005 | NA           | 0.2616 ± 0.1399 |        5 |
| mango_khir     | clip_b    | cls       | proto  |     50 | 0.6301 ± 0.0975 | 0.4987 ± 0.1026 | NA           | 0.1753 ± 0.0220 |        5 |
| mango_khir     | clip_b    | cls       | proto  |    nan | 0.5617 ± 0.0000 | 0.4339 ± 0.0000 | NA           | 0.1712 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |      1 | 0.6022 ± 0.1019 | 0.4462 ± 0.0614 | NA           | 0.2726 ± 0.2241 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |      5 | 0.7642 ± 0.0780 | 0.6343 ± 0.0526 | NA           | 0.1288 ± 0.0586 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |     10 | 0.7256 ± 0.0581 | 0.6362 ± 0.0590 | NA           | 0.1712 ± 0.0989 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |     50 | 0.6390 ± 0.0087 | 0.6132 ± 0.0174 | NA           | 0.0438 ± 0.0061 |        5 |
| mango_khir     | dinov2_b  | cls       | corn   |    nan | 0.6143 ± 0.0000 | 0.5484 ± 0.0000 | NA           | 0.0548 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |      1 | 0.5990 ± 0.0928 | 0.4491 ± 0.0744 | NA           | 0.2301 ± 0.1652 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |      5 | 0.7316 ± 0.0525 | 0.6090 ± 0.0305 | NA           | 0.1493 ± 0.0536 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |     10 | 0.7008 ± 0.0395 | 0.6154 ± 0.0465 | NA           | 0.1932 ± 0.0795 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |     50 | 0.6350 ± 0.0040 | 0.6054 ± 0.0082 | NA           | 0.0466 ± 0.0031 |        5 |
| mango_khir     | dinov2_b  | cls       | linear |    nan | 0.6280 ± 0.0000 | 0.5837 ± 0.0000 | NA           | 0.0479 ± 0.0000 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |      1 | 0.5832 ± 0.0944 | 0.4179 ± 0.0344 | NA           | 0.3973 ± 0.3027 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |      5 | 0.7526 ± 0.0730 | 0.6103 ± 0.0274 | NA           | 0.1534 ± 0.0584 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |     10 | 0.7287 ± 0.0586 | 0.6299 ± 0.0442 | NA           | 0.1685 ± 0.0930 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |     50 | 0.7858 ± 0.0336 | 0.6779 ± 0.0368 | NA           | 0.1041 ± 0.0239 |        5 |
| mango_khir     | dinov2_b  | cls       | proto  |    nan | 0.8286 ± 0.0000 | 0.7373 ± 0.0000 | NA           | 0.0685 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |      1 | 0.5287 ± 0.1210 | 0.4196 ± 0.0827 | NA           | 0.3534 ± 0.2838 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |      5 | 0.6507 ± 0.0850 | 0.5448 ± 0.1064 | NA           | 0.1658 ± 0.0882 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |     10 | 0.6587 ± 0.0712 | 0.5841 ± 0.0614 | NA           | 0.1863 ± 0.1174 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |     50 | 0.6317 ± 0.0034 | 0.5984 ± 0.0074 | NA           | 0.0493 ± 0.0031 |        5 |
| mango_khir     | dinov2_s  | cls       | corn   |    nan | 0.5996 ± 0.0000 | 0.5068 ± 0.0000 | NA           | 0.0616 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |      1 | 0.5210 ± 0.1144 | 0.4055 ± 0.0678 | NA           | 0.3342 ± 0.2435 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |      5 | 0.7005 ± 0.0767 | 0.5814 ± 0.0879 | NA           | 0.1671 ± 0.0862 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |     10 | 0.6702 ± 0.0823 | 0.5907 ± 0.0867 | NA           | 0.1890 ± 0.0851 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |     50 | 0.6277 ± 0.0087 | 0.5894 ± 0.0196 | NA           | 0.0534 ± 0.0089 |        5 |
| mango_khir     | dinov2_s  | cls       | linear |    nan | 0.6280 ± 0.0000 | 0.5837 ± 0.0000 | NA           | 0.0479 ± 0.0000 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |      1 | 0.5142 ± 0.1122 | 0.3975 ± 0.0836 | NA           | 0.4384 ± 0.3508 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |      5 | 0.6427 ± 0.0924 | 0.5284 ± 0.1170 | NA           | 0.2068 ± 0.1194 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |     10 | 0.6598 ± 0.0543 | 0.5759 ± 0.0554 | NA           | 0.1945 ± 0.1092 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |     50 | 0.6652 ± 0.1064 | 0.5833 ± 0.1121 | NA           | 0.1219 ± 0.0276 |        5 |
| mango_khir     | dinov2_s  | cls       | proto  |    nan | 0.7278 ± 0.0000 | 0.6446 ± 0.0000 | NA           | 0.1096 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | corn   |      1 | 0.5236 ± 0.0383 | 0.3211 ± 0.0587 | NA           | 0.5534 ± 0.3075 |        5 |
| mango_khir     | resnet50  | cls       | corn   |      5 | 0.6229 ± 0.1176 | 0.4938 ± 0.1350 | NA           | 0.4384 ± 0.2381 |        5 |
| mango_khir     | resnet50  | cls       | corn   |     10 | 0.6158 ± 0.0420 | 0.5364 ± 0.0662 | NA           | 0.4014 ± 0.1465 |        5 |
| mango_khir     | resnet50  | cls       | corn   |     50 | 0.6389 ± 0.0074 | 0.6132 ± 0.0156 | NA           | 0.0438 ± 0.0061 |        5 |
| mango_khir     | resnet50  | cls       | corn   |    nan | 0.5669 ± 0.0000 | 0.3967 ± 0.0000 | NA           | 0.0753 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | linear |      1 | 0.5186 ± 0.0258 | 0.3142 ± 0.0571 | NA           | 0.5493 ± 0.2996 |        5 |
| mango_khir     | resnet50  | cls       | linear |      5 | 0.6094 ± 0.0973 | 0.4720 ± 0.1083 | NA           | 0.4671 ± 0.2408 |        5 |
| mango_khir     | resnet50  | cls       | linear |     10 | 0.6095 ± 0.0340 | 0.5264 ± 0.0469 | NA           | 0.4123 ± 0.1272 |        5 |
| mango_khir     | resnet50  | cls       | linear |     50 | 0.6346 ± 0.0125 | 0.6038 ± 0.0275 | NA           | 0.0479 ± 0.0119 |        5 |
| mango_khir     | resnet50  | cls       | linear |    nan | 0.6143 ± 0.0000 | 0.5484 ± 0.0000 | NA           | 0.0548 ± 0.0000 |        5 |
| mango_khir     | resnet50  | cls       | proto  |      1 | 0.5236 ± 0.0450 | 0.3174 ± 0.0639 | NA           | 0.5932 ± 0.3401 |        5 |
| mango_khir     | resnet50  | cls       | proto  |      5 | 0.6104 ± 0.1197 | 0.4698 ± 0.1404 | NA           | 0.4890 ± 0.2355 |        5 |
| mango_khir     | resnet50  | cls       | proto  |     10 | 0.5929 ± 0.0322 | 0.5024 ± 0.0485 | NA           | 0.4959 ± 0.1325 |        5 |
| mango_khir     | resnet50  | cls       | proto  |     50 | 0.6131 ± 0.0248 | 0.5202 ± 0.0454 | NA           | 0.3753 ± 0.0886 |        5 |
| mango_khir     | resnet50  | cls       | proto  |    nan | 0.6326 ± 0.0000 | 0.5467 ± 0.0000 | NA           | 0.3425 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | corn   |      1 | 0.7754 ± 0.0270 | 0.5758 ± 0.0520 | NA           | 0.3946 ± 0.0752 |        5 |
| ninepeach      | clip_b    | cls       | corn   |      5 | 0.8180 ± 0.0179 | 0.6695 ± 0.0313 | NA           | 0.3312 ± 0.0265 |        5 |
| ninepeach      | clip_b    | cls       | corn   |     10 | 0.8557 ± 0.0195 | 0.7405 ± 0.0375 | NA           | 0.2627 ± 0.0360 |        5 |
| ninepeach      | clip_b    | cls       | corn   |     50 | 0.8987 ± 0.0062 | 0.8222 ± 0.0118 | NA           | 0.1836 ± 0.0125 |        5 |
| ninepeach      | clip_b    | cls       | corn   |    nan | 0.9221 ± 0.0000 | 0.8520 ± 0.0000 | NA           | 0.1319 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | linear |      1 | 0.7760 ± 0.0311 | 0.5735 ± 0.0618 | NA           | 0.4019 ± 0.0788 |        5 |
| ninepeach      | clip_b    | cls       | linear |      5 | 0.8105 ± 0.0290 | 0.6510 ± 0.0552 | NA           | 0.3338 ± 0.0374 |        5 |
| ninepeach      | clip_b    | cls       | linear |     10 | 0.8509 ± 0.0308 | 0.7251 ± 0.0621 | NA           | 0.2608 ± 0.0408 |        5 |
| ninepeach      | clip_b    | cls       | linear |     50 | 0.9023 ± 0.0090 | 0.8239 ± 0.0211 | NA           | 0.1713 ± 0.0109 |        5 |
| ninepeach      | clip_b    | cls       | linear |    nan | 0.9277 ± 0.0000 | 0.8625 ± 0.0000 | NA           | 0.1224 ± 0.0000 |        5 |
| ninepeach      | clip_b    | cls       | proto  |      1 | 0.7608 ± 0.0285 | 0.5603 ± 0.0495 | NA           | 0.4463 ± 0.0730 |        5 |
| ninepeach      | clip_b    | cls       | proto  |      5 | 0.8160 ± 0.0177 | 0.6551 ± 0.0409 | NA           | 0.3468 ± 0.0351 |        5 |
| ninepeach      | clip_b    | cls       | proto  |     10 | 0.8476 ± 0.0266 | 0.7211 ± 0.0508 | NA           | 0.2853 ± 0.0484 |        5 |
| ninepeach      | clip_b    | cls       | proto  |     50 | 0.8756 ± 0.0036 | 0.7809 ± 0.0083 | NA           | 0.2321 ± 0.0106 |        5 |
| ninepeach      | clip_b    | cls       | proto  |    nan | 0.8804 ± 0.0000 | 0.7941 ± 0.0000 | NA           | 0.2237 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |      1 | 0.7941 ± 0.0310 | 0.5856 ± 0.0685 | NA           | 0.3824 ± 0.1030 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |      5 | 0.8777 ± 0.0148 | 0.7631 ± 0.0292 | NA           | 0.2141 ± 0.0258 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |     10 | 0.8981 ± 0.0083 | 0.8033 ± 0.0184 | NA           | 0.1728 ± 0.0103 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |     50 | 0.9194 ± 0.0033 | 0.8447 ± 0.0056 | NA           | 0.1380 ± 0.0053 |        5 |
| ninepeach      | dinov2_b  | cls       | corn   |    nan | 0.9416 ± 0.0000 | 0.8881 ± 0.0000 | NA           | 0.0975 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |      1 | 0.7935 ± 0.0244 | 0.5927 ± 0.0493 | NA           | 0.3816 ± 0.0901 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |      5 | 0.8681 ± 0.0125 | 0.7446 ± 0.0263 | NA           | 0.2199 ± 0.0158 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |     10 | 0.8944 ± 0.0140 | 0.7958 ± 0.0299 | NA           | 0.1728 ± 0.0189 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |     50 | 0.9190 ± 0.0067 | 0.8454 ± 0.0130 | NA           | 0.1373 ± 0.0108 |        5 |
| ninepeach      | dinov2_b  | cls       | linear |    nan | 0.9442 ± 0.0000 | 0.8939 ± 0.0000 | NA           | 0.0937 ± 0.0000 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |      1 | 0.7771 ± 0.0280 | 0.5492 ± 0.0644 | NA           | 0.4390 ± 0.0954 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |      5 | 0.8638 ± 0.0124 | 0.7305 ± 0.0254 | NA           | 0.2535 ± 0.0299 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |     10 | 0.8945 ± 0.0113 | 0.7934 ± 0.0223 | NA           | 0.1870 ± 0.0179 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |     50 | 0.9131 ± 0.0042 | 0.8312 ± 0.0080 | NA           | 0.1518 ± 0.0077 |        5 |
| ninepeach      | dinov2_b  | cls       | proto  |    nan | 0.9214 ± 0.0000 | 0.8490 ± 0.0000 | NA           | 0.1358 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |      1 | 0.7702 ± 0.0149 | 0.5590 ± 0.0308 | NA           | 0.4382 ± 0.0720 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |      5 | 0.8685 ± 0.0157 | 0.7499 ± 0.0215 | NA           | 0.2352 ± 0.0302 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |     10 | 0.8956 ± 0.0131 | 0.8008 ± 0.0267 | NA           | 0.1824 ± 0.0266 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |     50 | 0.9232 ± 0.0060 | 0.8548 ± 0.0120 | NA           | 0.1335 ± 0.0108 |        5 |
| ninepeach      | dinov2_s  | cls       | corn   |    nan | 0.9353 ± 0.0000 | 0.8767 ± 0.0000 | NA           | 0.1090 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |      1 | 0.7707 ± 0.0169 | 0.5637 ± 0.0490 | NA           | 0.4413 ± 0.0753 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |      5 | 0.8723 ± 0.0126 | 0.7553 ± 0.0202 | NA           | 0.2214 ± 0.0228 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |     10 | 0.9001 ± 0.0159 | 0.8105 ± 0.0304 | NA           | 0.1702 ± 0.0301 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |     50 | 0.9261 ± 0.0059 | 0.8606 ± 0.0115 | NA           | 0.1266 ± 0.0100 |        5 |
| ninepeach      | dinov2_s  | cls       | linear |    nan | 0.9353 ± 0.0000 | 0.8767 ± 0.0000 | NA           | 0.1090 ± 0.0000 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |      1 | 0.7447 ± 0.0238 | 0.5085 ± 0.0559 | NA           | 0.5067 ± 0.0491 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |      5 | 0.8670 ± 0.0100 | 0.7416 ± 0.0230 | NA           | 0.2467 ± 0.0313 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |     10 | 0.8938 ± 0.0154 | 0.7951 ± 0.0312 | NA           | 0.1901 ± 0.0340 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |     50 | 0.9174 ± 0.0090 | 0.8432 ± 0.0190 | NA           | 0.1442 ± 0.0159 |        5 |
| ninepeach      | dinov2_s  | cls       | proto  |    nan | 0.9279 ± 0.0000 | 0.8637 ± 0.0000 | NA           | 0.1243 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | corn   |      1 | 0.7482 ± 0.0884 | 0.5249 ± 0.0867 | NA           | 0.5071 ± 0.1276 |        5 |
| ninepeach      | resnet50  | cls       | corn   |      5 | 0.8691 ± 0.0358 | 0.7552 ± 0.0574 | NA           | 0.2447 ± 0.0858 |        5 |
| ninepeach      | resnet50  | cls       | corn   |     10 | 0.8893 ± 0.0196 | 0.7935 ± 0.0373 | NA           | 0.1958 ± 0.0394 |        5 |
| ninepeach      | resnet50  | cls       | corn   |     50 | 0.9137 ± 0.0080 | 0.8386 ± 0.0142 | NA           | 0.1472 ± 0.0159 |        5 |
| ninepeach      | resnet50  | cls       | corn   |    nan | 0.9172 ± 0.0000 | 0.8414 ± 0.0000 | NA           | 0.1396 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | linear |      1 | 0.7648 ± 0.0756 | 0.5774 ± 0.0914 | NA           | 0.4608 ± 0.1150 |        5 |
| ninepeach      | resnet50  | cls       | linear |      5 | 0.8601 ± 0.0355 | 0.7354 ± 0.0577 | NA           | 0.2524 ± 0.0876 |        5 |
| ninepeach      | resnet50  | cls       | linear |     10 | 0.8843 ± 0.0235 | 0.7810 ± 0.0425 | NA           | 0.1996 ± 0.0455 |        5 |
| ninepeach      | resnet50  | cls       | linear |     50 | 0.9124 ± 0.0065 | 0.8358 ± 0.0136 | NA           | 0.1491 ± 0.0113 |        5 |
| ninepeach      | resnet50  | cls       | linear |    nan | 0.9306 ± 0.0000 | 0.8693 ± 0.0000 | NA           | 0.1185 ± 0.0000 |        5 |
| ninepeach      | resnet50  | cls       | proto  |      1 | 0.7298 ± 0.0894 | 0.4808 ± 0.0725 | NA           | 0.5656 ± 0.1113 |        5 |
| ninepeach      | resnet50  | cls       | proto  |      5 | 0.8564 ± 0.0427 | 0.7229 ± 0.0779 | NA           | 0.2826 ± 0.1034 |        5 |
| ninepeach      | resnet50  | cls       | proto  |     10 | 0.8774 ± 0.0191 | 0.7676 ± 0.0387 | NA           | 0.2291 ± 0.0423 |        5 |
| ninepeach      | resnet50  | cls       | proto  |     50 | 0.8998 ± 0.0140 | 0.8119 ± 0.0256 | NA           | 0.1755 ± 0.0276 |        5 |
| ninepeach      | resnet50  | cls       | proto  |    nan | 0.9213 ± 0.0000 | 0.8549 ± 0.0000 | NA           | 0.1358 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | corn   |      1 | 0.3606 ± 0.0224 | 0.1539 ± 0.0577 | NA           | 0.9839 ± 0.2795 |        5 |
| raspgrade      | clip_b    | cls       | corn   |      5 | 0.3577 ± 0.0148 | 0.1762 ± 0.0203 | NA           | 1.1937 ± 0.1103 |        5 |
| raspgrade      | clip_b    | cls       | corn   |     10 | 0.3706 ± 0.0281 | 0.2045 ± 0.0253 | NA           | 1.1082 ± 0.1608 |        5 |
| raspgrade      | clip_b    | cls       | corn   |     50 | 0.4050 ± 0.0254 | 0.2486 ± 0.0165 | NA           | 0.8724 ± 0.0714 |        5 |
| raspgrade      | clip_b    | cls       | corn   |    nan | 0.4214 ± 0.0000 | 0.1950 ± 0.0000 | NA           | 0.3224 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | linear |      1 | 0.3579 ± 0.0186 | 0.1501 ± 0.0520 | NA           | 1.0557 ± 0.2447 |        5 |
| raspgrade      | clip_b    | cls       | linear |      5 | 0.3391 ± 0.0147 | 0.1582 ± 0.0177 | NA           | 1.3495 ± 0.1165 |        5 |
| raspgrade      | clip_b    | cls       | linear |     10 | 0.3505 ± 0.0151 | 0.1839 ± 0.0247 | NA           | 1.2713 ± 0.1681 |        5 |
| raspgrade      | clip_b    | cls       | linear |     50 | 0.4114 ± 0.0145 | 0.2611 ± 0.0162 | NA           | 0.9268 ± 0.0702 |        5 |
| raspgrade      | clip_b    | cls       | linear |    nan | 0.4012 ± 0.0000 | 0.2160 ± 0.0000 | NA           | 0.3183 ± 0.0000 |        5 |
| raspgrade      | clip_b    | cls       | proto  |      1 | 0.3128 ± 0.0287 | 0.1266 ± 0.0443 | NA           | 1.0596 ± 0.4179 |        5 |
| raspgrade      | clip_b    | cls       | proto  |      5 | 0.3592 ± 0.0245 | 0.1808 ± 0.0293 | NA           | 1.2145 ± 0.2359 |        5 |
| raspgrade      | clip_b    | cls       | proto  |     10 | 0.3565 ± 0.0262 | 0.1969 ± 0.0205 | NA           | 1.2014 ± 0.1838 |        5 |
| raspgrade      | clip_b    | cls       | proto  |     50 | 0.3884 ± 0.0152 | 0.2404 ± 0.0124 | NA           | 1.0399 ± 0.0543 |        5 |
| raspgrade      | clip_b    | cls       | proto  |    nan | 0.3986 ± 0.0000 | 0.2518 ± 0.0000 | NA           | 1.0164 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |      1 | 0.3480 ± 0.0206 | 0.1488 ± 0.0314 | NA           | 1.0219 ± 0.0914 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |      5 | 0.3721 ± 0.0286 | 0.1763 ± 0.0431 | NA           | 1.0806 ± 0.1502 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |     10 | 0.3961 ± 0.0263 | 0.2031 ± 0.0261 | NA           | 0.9765 ± 0.1465 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |     50 | 0.4425 ± 0.0152 | 0.2815 ± 0.0183 | NA           | 1.0120 ± 0.0975 |        5 |
| raspgrade      | dinov2_b  | cls       | corn   |    nan | 0.3578 ± 0.0000 | 0.1874 ± 0.0000 | NA           | 0.3361 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |      1 | 0.3486 ± 0.0168 | 0.1528 ± 0.0327 | NA           | 1.0347 ± 0.0936 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |      5 | 0.3701 ± 0.0322 | 0.1783 ± 0.0512 | NA           | 1.2000 ± 0.1544 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |     10 | 0.3844 ± 0.0314 | 0.1994 ± 0.0377 | NA           | 1.0760 ± 0.1683 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |     50 | 0.4371 ± 0.0127 | 0.2876 ± 0.0156 | NA           | 1.0202 ± 0.0837 |        5 |
| raspgrade      | dinov2_b  | cls       | linear |    nan | 0.3868 ± 0.0000 | 0.2284 ± 0.0000 | NA           | 0.3292 ± 0.0000 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |      1 | 0.3299 ± 0.0407 | 0.1425 ± 0.0262 | NA           | 1.1954 ± 0.1729 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |      5 | 0.3774 ± 0.0195 | 0.1862 ± 0.0365 | NA           | 1.0820 ± 0.1893 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |     10 | 0.3906 ± 0.0174 | 0.2051 ± 0.0233 | NA           | 1.0290 ± 0.1274 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |     50 | 0.4095 ± 0.0015 | 0.2452 ± 0.0097 | NA           | 1.0891 ± 0.0696 |        5 |
| raspgrade      | dinov2_b  | cls       | proto  |    nan | 0.4106 ± 0.0000 | 0.2610 ± 0.0000 | NA           | 1.0587 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |      1 | 0.3547 ± 0.0301 | 0.1773 ± 0.0384 | NA           | 1.0948 ± 0.1530 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |      5 | 0.3810 ± 0.0090 | 0.2017 ± 0.0198 | NA           | 1.0664 ± 0.1618 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |     10 | 0.4027 ± 0.0093 | 0.2336 ± 0.0140 | NA           | 1.0653 ± 0.1778 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |     50 | 0.4387 ± 0.0104 | 0.2949 ± 0.0140 | NA           | 0.9339 ± 0.1024 |        5 |
| raspgrade      | dinov2_s  | cls       | corn   |    nan | 0.3668 ± 0.0000 | 0.2271 ± 0.0000 | NA           | 0.3320 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |      1 | 0.3426 ± 0.0436 | 0.1727 ± 0.0374 | NA           | 1.1735 ± 0.2680 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |      5 | 0.3697 ± 0.0097 | 0.1952 ± 0.0226 | NA           | 1.1773 ± 0.1701 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |     10 | 0.3947 ± 0.0124 | 0.2282 ± 0.0145 | NA           | 1.1820 ± 0.1599 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |     50 | 0.4294 ± 0.0047 | 0.2937 ± 0.0048 | NA           | 0.9885 ± 0.0972 |        5 |
| raspgrade      | dinov2_s  | cls       | linear |    nan | 0.4240 ± 0.0000 | 0.3040 ± 0.0000 | NA           | 0.2992 ± 0.0000 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |      1 | 0.3422 ± 0.0473 | 0.1728 ± 0.0380 | NA           | 1.2096 ± 0.3227 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |      5 | 0.3759 ± 0.0151 | 0.1998 ± 0.0250 | NA           | 1.0839 ± 0.1849 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |     10 | 0.3905 ± 0.0021 | 0.2257 ± 0.0166 | NA           | 1.1577 ± 0.1584 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |     50 | 0.4099 ± 0.0154 | 0.2569 ± 0.0201 | NA           | 1.0044 ± 0.0965 |        5 |
| raspgrade      | dinov2_s  | cls       | proto  |    nan | 0.4241 ± 0.0000 | 0.2837 ± 0.0000 | NA           | 0.8566 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | corn   |      1 | 0.3132 ± 0.0280 | 0.1477 ± 0.0361 | NA           | 1.2350 ± 0.2062 |        5 |
| raspgrade      | resnet50  | cls       | corn   |      5 | 0.3597 ± 0.0309 | 0.1963 ± 0.0410 | NA           | 1.1817 ± 0.2646 |        5 |
| raspgrade      | resnet50  | cls       | corn   |     10 | 0.3820 ± 0.0229 | 0.2253 ± 0.0355 | NA           | 1.1019 ± 0.2053 |        5 |
| raspgrade      | resnet50  | cls       | corn   |     50 | 0.4449 ± 0.0185 | 0.2977 ± 0.0226 | NA           | 0.8475 ± 0.0836 |        5 |
| raspgrade      | resnet50  | cls       | corn   |    nan | 0.3821 ± 0.0000 | 0.2336 ± 0.0000 | NA           | 0.3279 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | linear |      1 | 0.3068 ± 0.0421 | 0.1480 ± 0.0348 | NA           | 1.2954 ± 0.3275 |        5 |
| raspgrade      | resnet50  | cls       | linear |      5 | 0.3508 ± 0.0283 | 0.1864 ± 0.0416 | NA           | 1.2601 ± 0.2730 |        5 |
| raspgrade      | resnet50  | cls       | linear |     10 | 0.3775 ± 0.0180 | 0.2190 ± 0.0293 | NA           | 1.1956 ± 0.2272 |        5 |
| raspgrade      | resnet50  | cls       | linear |     50 | 0.4390 ± 0.0189 | 0.2956 ± 0.0243 | NA           | 0.8899 ± 0.1107 |        5 |
| raspgrade      | resnet50  | cls       | linear |    nan | 0.3728 ± 0.0000 | 0.2572 ± 0.0000 | NA           | 0.3306 ± 0.0000 |        5 |
| raspgrade      | resnet50  | cls       | proto  |      1 | 0.2944 ± 0.0399 | 0.1394 ± 0.0364 | NA           | 1.4268 ± 0.2502 |        5 |
| raspgrade      | resnet50  | cls       | proto  |      5 | 0.3402 ± 0.0285 | 0.1797 ± 0.0330 | NA           | 1.3197 ± 0.2667 |        5 |
| raspgrade      | resnet50  | cls       | proto  |     10 | 0.3618 ± 0.0279 | 0.2044 ± 0.0277 | NA           | 1.2631 ± 0.2190 |        5 |
| raspgrade      | resnet50  | cls       | proto  |     50 | 0.3950 ± 0.0117 | 0.2494 ± 0.0246 | NA           | 1.0074 ± 0.0635 |        5 |
| raspgrade      | resnet50  | cls       | proto  |    nan | 0.4136 ± 0.0000 | 0.2806 ± 0.0000 | NA           | 0.8757 ± 0.0000 |        5 |

Definition: an adjacent-grade error earns credit 1/2 and a skipped grade credit 0, so the penalty ratio is 1:2 exactly as the plan states; per-class precision/recall are the mean credit over samples predicted-as / labelled-as that class, F1 is their harmonic mean, and the macro average runs over the ordinal class list (same convention as `macro_f1`). `macro_f1` here is recomputed from the re-fitted head and must equal T2's value for the same cell -- `outputs/E1ORD_XCHECK.txt` records that comparison, and a non-zero mismatch means this table measures a different pipeline. Runs live under `exp = E1ord` so they never enter T2 or the paired tests.

## E4 ordinal ablation: CORN ordinal head vs linear head (paired by seed)

| view           | encoder   | variant   |     shot | metric   |   n_pairs |   corn |   linear |   delta_corn_minus_linear |   sd_diff |         t |        p |   corn_better_pairs |   p_bonferroni |   p_holm | survives_bonferroni_0.05   |   n_tests_in_family |
|:---------------|:----------|:----------|---------:|:---------|----------:|-------:|---------:|--------------------------:|----------:|----------:|---------:|--------------------:|---------------:|---------:|:---------------------------|--------------------:|
| banana3        | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.6883 |   0.7284 |                   -0.0401 |    0.0696 |   -1.2880 |   0.2672 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.4552 |   0.5112 |                   -0.0560 |    0.0513 |   -2.4387 |   0.0713 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.8291 |   0.8217 |                    0.0074 |    0.0069 |    2.4051 |   0.0739 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.6977 |   0.6933 |                    0.0044 |    0.0089 |    1.0991 |   0.3334 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.8536 |   0.8468 |                    0.0067 |    0.0091 |    1.6652 |   0.1712 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.7347 |   0.7249 |                    0.0098 |    0.0200 |    1.0998 |   0.3331 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.8920 |   0.8949 |                   -0.0030 |    0.0078 |   -0.8466 |   0.4449 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.7997 |   0.8075 |                   -0.0078 |    0.0142 |   -1.2322 |   0.2854 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | clip_b    | cls       | nan      | cost_f1  |         5 | 0.9358 |   0.9327 |                    0.0031 |    0.0000 |  inf      |   0.0000 |                   5 |         0.0000 |   0.0000 | True                       |                 400 |
| banana3        | clip_b    | cls       | nan      | macro_f1 |         5 | 0.8803 |   0.8745 |                    0.0058 |    0.0000 |  inf      |   0.0000 |                   5 |         0.0000 |   0.0000 | True                       |                 400 |
| banana3        | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.7304 |   0.6955 |                    0.0349 |    0.0408 |    1.9114 |   0.1285 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.4475 |   0.4678 |                   -0.0203 |    0.0592 |   -0.7669 |   0.4859 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.8519 |   0.8448 |                    0.0071 |    0.0110 |    1.4501 |   0.2206 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.7311 |   0.7224 |                    0.0087 |    0.0281 |    0.6909 |   0.5276 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.8664 |   0.8734 |                   -0.0070 |    0.0134 |   -1.1734 |   0.3057 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.7611 |   0.7730 |                   -0.0119 |    0.0277 |   -0.9622 |   0.3904 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.9200 |   0.9281 |                   -0.0081 |    0.0066 |   -2.7735 |   0.0502 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.8572 |   0.8719 |                   -0.0147 |    0.0120 |   -2.7443 |   0.0517 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_b  | cls       | nan      | cost_f1  |         5 | 0.9570 |   0.9540 |                    0.0030 |    0.0000 |  inf      |   0.0000 |                   5 |         0.0000 |   0.0000 | True                       |                 400 |
| banana3        | dinov2_b  | cls       | nan      | macro_f1 |         5 | 0.9231 |   0.9175 |                    0.0056 |    0.0000 |  inf      |   0.0000 |                   5 |         0.0000 |   0.0000 | True                       |                 400 |
| banana3        | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.7416 |   0.7417 |                   -0.0001 |    0.0165 |   -0.0079 |   0.9941 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.4742 |   0.5093 |                   -0.0351 |    0.0607 |   -1.2940 |   0.2653 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.8504 |   0.8455 |                    0.0049 |    0.0140 |    0.7821 |   0.4779 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.7334 |   0.7232 |                    0.0102 |    0.0302 |    0.7527 |   0.4935 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.8748 |   0.8785 |                   -0.0038 |    0.0186 |   -0.4536 |   0.6737 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.7784 |   0.7821 |                   -0.0037 |    0.0368 |   -0.2246 |   0.8333 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.9434 |   0.9441 |                   -0.0006 |    0.0046 |   -0.3113 |   0.7712 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.8988 |   0.9009 |                   -0.0021 |    0.0107 |   -0.4398 |   0.6828 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.9662 |   0.9718 |                   -0.0057 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana3        | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.9417 |   0.9537 |                   -0.0120 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana3        | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.6890 |   0.6772 |                    0.0119 |    0.0255 |    1.0419 |   0.3563 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.4498 |   0.4637 |                   -0.0140 |    0.0407 |   -0.7673 |   0.4857 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.7483 |   0.7525 |                   -0.0042 |    0.0169 |   -0.5571 |   0.6071 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.5743 |   0.5950 |                   -0.0206 |    0.0270 |   -1.7107 |   0.1623 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.8073 |   0.8135 |                   -0.0062 |    0.0097 |   -1.4346 |   0.2247 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.6771 |   0.6855 |                   -0.0083 |    0.0146 |   -1.2734 |   0.2718 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.8841 |   0.8900 |                   -0.0059 |    0.0083 |   -1.5783 |   0.1896 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.7809 |   0.7915 |                   -0.0106 |    0.0117 |   -2.0271 |   0.1126 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana3        | resnet50  | cls       | nan      | cost_f1  |         5 | 0.9295 |   0.9409 |                   -0.0114 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana3        | resnet50  | cls       | nan      | macro_f1 |         5 | 0.8630 |   0.8859 |                   -0.0229 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana4        | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.8285 |   0.8285 |                    0.0000 |    0.0154 |    0.0022 |   0.9984 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.6263 |   0.6200 |                    0.0063 |    0.0427 |    0.3293 |   0.7584 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.9436 |   0.9483 |                   -0.0047 |    0.0044 |   -2.3820 |   0.0758 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.8840 |   0.8969 |                   -0.0129 |    0.0101 |   -2.8702 |   0.0455 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.9548 |   0.9511 |                    0.0036 |    0.0083 |    0.9811 |   0.3821 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.9075 |   0.8994 |                    0.0081 |    0.0181 |    1.0051 |   0.3717 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.9767 |   0.9778 |                   -0.0010 |    0.0024 |   -0.9588 |   0.3920 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.9528 |   0.9551 |                   -0.0022 |    0.0049 |   -1.0043 |   0.3720 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | clip_b    | cls       | nan      | cost_f1  |         5 | 0.9860 |   0.9885 |                   -0.0025 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana4        | clip_b    | cls       | nan      | macro_f1 |         5 | 0.9716 |   0.9768 |                   -0.0052 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana4        | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.8466 |   0.8501 |                   -0.0034 |    0.0116 |   -0.6614 |   0.5445 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.7086 |   0.7310 |                   -0.0224 |    0.0224 |   -2.2357 |   0.0890 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.9527 |   0.9554 |                   -0.0028 |    0.0017 |   -3.6096 |   0.0226 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.8993 |   0.9052 |                   -0.0059 |    0.0034 |   -3.8783 |   0.0179 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.9604 |   0.9664 |                   -0.0060 |    0.0057 |   -2.3752 |   0.0764 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.9176 |   0.9303 |                   -0.0126 |    0.0115 |   -2.4506 |   0.0704 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.9741 |   0.9750 |                   -0.0009 |    0.0031 |   -0.6698 |   0.5397 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.9468 |   0.9491 |                   -0.0022 |    0.0063 |   -0.7977 |   0.4697 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_b  | cls       | nan      | cost_f1  |         5 | 0.9872 |   0.9911 |                   -0.0038 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana4        | dinov2_b  | cls       | nan      | macro_f1 |         5 | 0.9742 |   0.9820 |                   -0.0078 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana4        | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.8447 |   0.8470 |                   -0.0023 |    0.0094 |   -0.5463 |   0.6139 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.6867 |   0.6904 |                   -0.0037 |    0.0240 |   -0.3489 |   0.7448 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.9545 |   0.9560 |                   -0.0014 |    0.0044 |   -0.7331 |   0.5042 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.9044 |   0.9080 |                   -0.0036 |    0.0098 |   -0.8165 |   0.4601 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.9636 |   0.9683 |                   -0.0047 |    0.0034 |   -3.1470 |   0.0346 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.9255 |   0.9355 |                   -0.0100 |    0.0071 |   -3.1370 |   0.0349 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.9775 |   0.9795 |                   -0.0021 |    0.0023 |   -1.9684 |   0.1204 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.9544 |   0.9587 |                   -0.0043 |    0.0048 |   -2.0323 |   0.1119 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.9911 |   0.9923 |                   -0.0012 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana4        | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.9819 |   0.9846 |                   -0.0026 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana4        | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.7940 |   0.7810 |                    0.0130 |    0.0157 |    1.8564 |   0.1370 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.5915 |   0.5700 |                    0.0215 |    0.0389 |    1.2376 |   0.2836 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.8820 |   0.8806 |                    0.0014 |    0.0044 |    0.6952 |   0.5252 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.7469 |   0.7479 |                   -0.0010 |    0.0116 |   -0.1912 |   0.8577 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| banana4        | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.8993 |   0.9042 |                   -0.0049 |    0.0007 |  -16.0341 |   0.0001 |                   0 |         0.0354 |   0.0299 | True                       |                 400 |
| banana4        | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.7814 |   0.7933 |                   -0.0119 |    0.0010 |  -26.1913 |   0.0000 |                   0 |         0.0051 |   0.0043 | True                       |                 400 |
| banana4        | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.9313 |   0.9416 |                   -0.0103 |    0.0032 |   -7.2398 |   0.0019 |                   0 |         0.7727 |   0.6490 | False                      |                 400 |
| banana4        | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.8527 |   0.8761 |                   -0.0235 |    0.0064 |   -8.1628 |   0.0012 |                   0 |         0.4905 |   0.4132 | False                      |                 400 |
| banana4        | resnet50  | cls       | nan      | cost_f1  |         5 | 0.9796 |   0.9834 |                   -0.0038 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| banana4        | resnet50  | cls       | nan      | macro_f1 |         5 | 0.9588 |   0.9665 |                   -0.0078 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| field4_banana  | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.8592 |   0.8592 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.6826 |   0.6826 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.8866 |   0.8866 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.7576 |   0.7576 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.9202 |   0.9202 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.8308 |   0.8308 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.9637 |   0.9637 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.9249 |   0.9249 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       | nan      | cost_f1  |         5 | 0.9990 |   0.9990 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | clip_b    | cls       | nan      | macro_f1 |         5 | 0.9980 |   0.9980 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.8817 |   0.8817 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.7467 |   0.7467 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.8986 |   0.8986 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.7766 |   0.7766 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.9491 |   0.9491 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.8945 |   0.8945 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.9875 |   0.9875 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.9743 |   0.9743 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       | nan      | cost_f1  |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_b  | cls       | nan      | macro_f1 |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.8330 |   0.8330 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.6217 |   0.6217 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.8958 |   0.8958 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.7704 |   0.7704 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.9463 |   0.9463 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.8918 |   0.8918 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.9824 |   0.9824 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.9638 |   0.9638 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.9990 |   0.9990 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.9980 |   0.9980 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.9129 |   0.9129 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.8181 |   0.8181 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.9246 |   0.9246 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.8427 |   0.8427 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.9170 |   0.9170 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.8263 |   0.8263 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.9597 |   0.9597 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.9176 |   0.9176 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       | nan      | cost_f1  |         5 | 0.9940 |   0.9940 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_banana  | resnet50  | cls       | nan      | macro_f1 |         5 | 0.9880 |   0.9880 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.8813 |   0.8813 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.7469 |   0.7469 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.9731 |   0.9731 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.9455 |   0.9455 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.9851 |   0.9851 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.9695 |   0.9695 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.9980 |   0.9980 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.9960 |   0.9960 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       | nan      | cost_f1  |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | clip_b    | cls       | nan      | macro_f1 |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.9312 |   0.9312 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.8513 |   0.8513 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.9936 |   0.9936 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.9872 |   0.9872 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.9982 |   0.9982 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.9964 |   0.9964 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       | nan      | cost_f1  |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_b  | cls       | nan      | macro_f1 |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.9111 |   0.9111 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.8190 |   0.8190 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.9833 |   0.9833 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.9664 |   0.9664 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.9956 |   0.9956 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.9912 |   0.9912 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.9996 |   0.9996 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.9992 |   0.9992 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       | nan      | cost_f1  |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | dinov2_s  | cls       | nan      | macro_f1 |         5 | 1.0000 |   1.0000 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.8667 |   0.8667 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.7115 |   0.7115 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.9634 |   0.9634 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.9258 |   0.9258 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.9820 |   0.9820 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.9631 |   0.9631 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.9942 |   0.9942 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.9884 |   0.9884 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       | nan      | cost_f1  |         5 | 0.9990 |   0.9990 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| field4_mango   | resnet50  | cls       | nan      | macro_f1 |         5 | 0.9980 |   0.9980 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.5964 |   0.5931 |                    0.0033 |    0.0042 |    1.7648 |   0.1524 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.3601 |   0.3533 |                    0.0068 |    0.0078 |    1.9568 |   0.1220 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.6746 |   0.6794 |                   -0.0049 |    0.0050 |   -2.1807 |   0.0947 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.4443 |   0.4540 |                   -0.0097 |    0.0071 |   -3.0613 |   0.0376 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.7098 |   0.7144 |                   -0.0046 |    0.0167 |   -0.6152 |   0.5717 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.5102 |   0.5219 |                   -0.0117 |    0.0187 |   -1.3985 |   0.2345 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.7866 |   0.7992 |                   -0.0125 |    0.0116 |   -2.4130 |   0.0733 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.6392 |   0.6536 |                   -0.0144 |    0.0208 |   -1.5483 |   0.1965 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | clip_b    | cls       | nan      | cost_f1  |         5 | 0.8650 |   0.8914 |                   -0.0264 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_apple  | clip_b    | cls       | nan      | macro_f1 |         5 | 0.7764 |   0.8163 |                   -0.0399 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_apple  | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.6182 |   0.5982 |                    0.0200 |    0.0153 |    2.9110 |   0.0436 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.3895 |   0.3736 |                    0.0160 |    0.0128 |    2.7890 |   0.0494 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.7407 |   0.7350 |                    0.0057 |    0.0116 |    1.0907 |   0.3367 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.5647 |   0.5591 |                    0.0057 |    0.0190 |    0.6665 |   0.5416 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.7865 |   0.7862 |                    0.0003 |    0.0134 |    0.0516 |   0.9613 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.6391 |   0.6463 |                   -0.0072 |    0.0106 |   -1.5058 |   0.2066 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.8468 |   0.8565 |                   -0.0097 |    0.0074 |   -2.9234 |   0.0431 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.7365 |   0.7492 |                   -0.0127 |    0.0128 |   -2.2127 |   0.0913 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_b  | cls       | nan      | cost_f1  |         5 | 0.8889 |   0.8891 |                   -0.0001 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_apple  | dinov2_b  | cls       | nan      | macro_f1 |         5 | 0.8103 |   0.8216 |                   -0.0113 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_apple  | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.6379 |   0.6331 |                    0.0048 |    0.0079 |    1.3551 |   0.2469 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.4226 |   0.4178 |                    0.0048 |    0.0149 |    0.7196 |   0.5116 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.7388 |   0.7254 |                    0.0133 |    0.0095 |    3.1517 |   0.0345 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.5645 |   0.5537 |                    0.0109 |    0.0147 |    1.6504 |   0.1742 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.7952 |   0.7935 |                    0.0017 |    0.0092 |    0.4206 |   0.6957 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.6559 |   0.6603 |                   -0.0045 |    0.0091 |   -1.0906 |   0.3367 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.8550 |   0.8512 |                    0.0038 |    0.0105 |    0.8153 |   0.4606 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.7461 |   0.7477 |                   -0.0016 |    0.0199 |   -0.1764 |   0.8685 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.8927 |   0.8937 |                   -0.0010 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_apple  | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.8052 |   0.8069 |                   -0.0017 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_apple  | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.5647 |   0.5448 |                    0.0199 |    0.0284 |    1.5652 |   0.1926 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.3463 |   0.3210 |                    0.0253 |    0.0282 |    2.0070 |   0.1152 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.7099 |   0.7165 |                   -0.0066 |    0.0133 |   -1.1041 |   0.3315 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.5089 |   0.5246 |                   -0.0156 |    0.0164 |   -2.1279 |   0.1004 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.7811 |   0.7828 |                   -0.0018 |    0.0051 |   -0.7652 |   0.4868 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.6231 |   0.6271 |                   -0.0040 |    0.0098 |   -0.9181 |   0.4105 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.8200 |   0.8278 |                   -0.0078 |    0.0181 |   -0.9619 |   0.3906 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.6923 |   0.7061 |                   -0.0138 |    0.0266 |   -1.1618 |   0.3099 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_apple  | resnet50  | cls       | nan      | cost_f1  |         5 | 0.8741 |   0.8918 |                   -0.0178 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_apple  | resnet50  | cls       | nan      | macro_f1 |         5 | 0.7956 |   0.8348 |                   -0.0392 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_banana | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.5966 |   0.5909 |                    0.0057 |    0.0088 |    1.4337 |   0.2250 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.3286 |   0.3195 |                    0.0091 |    0.0323 |    0.6306 |   0.5625 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.6515 |   0.6570 |                   -0.0055 |    0.0074 |   -1.6570 |   0.1729 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.4079 |   0.4188 |                   -0.0109 |    0.0070 |   -3.4748 |   0.0255 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.6974 |   0.7033 |                   -0.0058 |    0.0098 |   -1.3280 |   0.2549 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.4767 |   0.4972 |                   -0.0205 |    0.0206 |   -2.2308 |   0.0895 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.7939 |   0.8053 |                   -0.0114 |    0.0040 |   -6.3375 |   0.0032 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.6366 |   0.6570 |                   -0.0204 |    0.0019 |  -24.1845 |   0.0000 |                   0 |         0.0069 |   0.0059 | True                       |                 400 |
| fruit12_banana | clip_b    | cls       | nan      | cost_f1  |         5 | 0.8550 |   0.8715 |                   -0.0165 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_banana | clip_b    | cls       | nan      | macro_f1 |         5 | 0.7196 |   0.7832 |                   -0.0636 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_banana | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.6410 |   0.6397 |                    0.0014 |    0.0093 |    0.3273 |   0.7598 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.3900 |   0.3874 |                    0.0026 |    0.0329 |    0.1778 |   0.8675 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.7391 |   0.7459 |                   -0.0067 |    0.0115 |   -1.3095 |   0.2605 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.5357 |   0.5541 |                   -0.0184 |    0.0252 |   -1.6335 |   0.1777 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.7635 |   0.7737 |                   -0.0103 |    0.0065 |   -3.5376 |   0.0241 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.6024 |   0.6217 |                   -0.0194 |    0.0132 |   -3.2906 |   0.0302 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.8429 |   0.8521 |                   -0.0092 |    0.0064 |   -3.1873 |   0.0333 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.7280 |   0.7497 |                   -0.0217 |    0.0130 |   -3.7182 |   0.0205 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_b  | cls       | nan      | cost_f1  |         5 | 0.8685 |   0.8726 |                   -0.0040 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_banana | dinov2_b  | cls       | nan      | macro_f1 |         5 | 0.7927 |   0.8187 |                   -0.0260 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_banana | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.6521 |   0.6475 |                    0.0047 |    0.0112 |    0.9346 |   0.4029 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.3803 |   0.3711 |                    0.0091 |    0.0365 |    0.5603 |   0.6052 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.7649 |   0.7748 |                   -0.0099 |    0.0090 |   -2.4736 |   0.0687 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.5643 |   0.5841 |                   -0.0197 |    0.0168 |   -2.6276 |   0.0583 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.7806 |   0.7917 |                   -0.0110 |    0.0131 |   -1.8774 |   0.1337 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.6113 |   0.6277 |                   -0.0163 |    0.0234 |   -1.5636 |   0.1930 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.8470 |   0.8587 |                   -0.0117 |    0.0051 |   -5.1319 |   0.0068 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.7191 |   0.7459 |                   -0.0269 |    0.0119 |   -5.0311 |   0.0073 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.9079 |   0.9303 |                   -0.0224 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_banana | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.8308 |   0.8814 |                   -0.0506 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_banana | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.6171 |   0.6166 |                    0.0005 |    0.0113 |    0.0997 |   0.9254 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.3409 |   0.3376 |                    0.0033 |    0.0213 |    0.3468 |   0.7462 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.6892 |   0.6983 |                   -0.0091 |    0.0073 |   -2.7967 |   0.0490 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.4651 |   0.4782 |                   -0.0131 |    0.0098 |   -2.9897 |   0.0403 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.7213 |   0.7340 |                   -0.0126 |    0.0083 |   -3.3867 |   0.0276 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.5044 |   0.5306 |                   -0.0263 |    0.0135 |   -4.3416 |   0.0122 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.8216 |   0.8321 |                   -0.0105 |    0.0081 |   -2.8815 |   0.0449 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.6715 |   0.6945 |                   -0.0230 |    0.0130 |   -3.9653 |   0.0166 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_banana | resnet50  | cls       | nan      | cost_f1  |         5 | 0.9007 |   0.9100 |                   -0.0093 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_banana | resnet50  | cls       | nan      | macro_f1 |         5 | 0.8069 |   0.8442 |                   -0.0373 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_mango  | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.6350 |   0.6334 |                    0.0016 |    0.0123 |    0.2962 |   0.7818 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.4146 |   0.4169 |                   -0.0023 |    0.0168 |   -0.2995 |   0.7795 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.7589 |   0.7632 |                   -0.0043 |    0.0106 |   -0.9190 |   0.4101 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.6210 |   0.6413 |                   -0.0204 |    0.0131 |   -3.4841 |   0.0253 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.7935 |   0.8087 |                   -0.0152 |    0.0107 |   -3.1786 |   0.0336 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.6709 |   0.6978 |                   -0.0269 |    0.0246 |   -2.4460 |   0.0708 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.8629 |   0.8739 |                   -0.0110 |    0.0084 |   -2.9435 |   0.0422 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.7944 |   0.8062 |                   -0.0117 |    0.0155 |   -1.6932 |   0.1657 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | clip_b    | cls       | nan      | cost_f1  |         5 | 0.8773 |   0.8885 |                   -0.0111 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_mango  | clip_b    | cls       | nan      | macro_f1 |         5 | 0.8130 |   0.8347 |                   -0.0216 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_mango  | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.7184 |   0.7066 |                    0.0117 |    0.0059 |    4.4488 |   0.0113 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.5079 |   0.4995 |                    0.0083 |    0.0174 |    1.0728 |   0.3438 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.8390 |   0.8328 |                    0.0062 |    0.0126 |    1.1008 |   0.3328 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.7320 |   0.7275 |                    0.0045 |    0.0242 |    0.4189 |   0.6968 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.8587 |   0.8646 |                   -0.0059 |    0.0091 |   -1.4542 |   0.2196 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.7645 |   0.7766 |                   -0.0121 |    0.0131 |   -2.0680 |   0.1075 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.9218 |   0.9280 |                   -0.0062 |    0.0054 |   -2.5616 |   0.0625 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.8727 |   0.8802 |                   -0.0074 |    0.0073 |   -2.2696 |   0.0858 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_b  | cls       | nan      | cost_f1  |         5 | 0.9293 |   0.9360 |                   -0.0068 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_mango  | dinov2_b  | cls       | nan      | macro_f1 |         5 | 0.8849 |   0.8924 |                   -0.0075 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_mango  | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.7310 |   0.7226 |                    0.0085 |    0.0116 |    1.6310 |   0.1782 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.5254 |   0.5211 |                    0.0043 |    0.0104 |    0.9287 |   0.4056 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.8458 |   0.8373 |                    0.0085 |    0.0226 |    0.8427 |   0.4468 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.7388 |   0.7295 |                    0.0093 |    0.0327 |    0.6370 |   0.5588 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.8725 |   0.8658 |                    0.0068 |    0.0066 |    2.2809 |   0.0847 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.7855 |   0.7763 |                    0.0092 |    0.0108 |    1.9093 |   0.1289 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.9260 |   0.9352 |                   -0.0093 |    0.0122 |   -1.6953 |   0.1653 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.8773 |   0.8899 |                   -0.0127 |    0.0225 |   -1.2607 |   0.2759 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.9142 |   0.9470 |                   -0.0328 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_mango  | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.8561 |   0.9066 |                   -0.0505 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_mango  | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.6695 |   0.6690 |                    0.0005 |    0.0068 |    0.1719 |   0.8719 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.4693 |   0.4736 |                   -0.0042 |    0.0114 |   -0.8290 |   0.4537 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.8036 |   0.8008 |                    0.0027 |    0.0090 |    0.6804 |   0.5336 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.6895 |   0.6997 |                   -0.0102 |    0.0168 |   -1.3621 |   0.2448 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.8353 |   0.8340 |                    0.0012 |    0.0062 |    0.4487 |   0.6769 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.7282 |   0.7357 |                   -0.0075 |    0.0080 |   -2.0807 |   0.1059 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.8977 |   0.9061 |                   -0.0084 |    0.0125 |   -1.5031 |   0.2072 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.8473 |   0.8590 |                   -0.0117 |    0.0114 |   -2.2961 |   0.0833 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| fruit12_mango  | resnet50  | cls       | nan      | cost_f1  |         5 | 0.9238 |   0.9271 |                   -0.0033 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| fruit12_mango  | resnet50  | cls       | nan      | macro_f1 |         5 | 0.8767 |   0.8836 |                   -0.0069 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| mango_khir     | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.5469 |   0.5372 |                    0.0097 |    0.0229 |    0.9464 |   0.3975 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.3752 |   0.3565 |                    0.0187 |    0.0155 |    2.6987 |   0.0542 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.6766 |   0.6424 |                    0.0341 |    0.0262 |    2.9134 |   0.0435 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.5287 |   0.4886 |                    0.0401 |    0.0198 |    4.5249 |   0.0106 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.6306 |   0.7180 |                   -0.0874 |    0.1432 |   -1.3642 |   0.2442 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.4978 |   0.5742 |                   -0.0765 |    0.1448 |   -1.1811 |   0.3030 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.6331 |   0.6408 |                   -0.0077 |    0.0070 |   -2.4495 |   0.0705 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.5959 |   0.6142 |                   -0.0183 |    0.0167 |   -2.4495 |   0.0705 |                   0 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       | nan      | cost_f1  |         5 | 0.3263 |   0.3263 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| mango_khir     | clip_b    | cls       | nan      | macro_f1 |         5 | 0.3215 |   0.3215 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.6022 |   0.5990 |                    0.0033 |    0.0101 |    0.7228 |   0.5098 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.4462 |   0.4491 |                   -0.0028 |    0.0259 |   -0.2459 |   0.8179 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.7642 |   0.7316 |                    0.0326 |    0.0498 |    1.4640 |   0.2170 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.6343 |   0.6090 |                    0.0252 |    0.0447 |    1.2610 |   0.2758 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.7256 |   0.7008 |                    0.0248 |    0.0207 |    2.6782 |   0.0553 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.6362 |   0.6154 |                    0.0208 |    0.0174 |    2.6731 |   0.0556 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.6390 |   0.6350 |                    0.0039 |    0.0088 |    1.0000 |   0.3739 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.6132 |   0.6054 |                    0.0078 |    0.0175 |    1.0000 |   0.3739 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_b  | cls       | nan      | cost_f1  |         5 | 0.6143 |   0.6280 |                   -0.0137 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| mango_khir     | dinov2_b  | cls       | nan      | macro_f1 |         5 | 0.5484 |   0.5837 |                   -0.0354 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| mango_khir     | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.5287 |   0.5210 |                    0.0078 |    0.0122 |    1.4233 |   0.2277 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.4196 |   0.4055 |                    0.0140 |    0.0241 |    1.3030 |   0.2625 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.6507 |   0.7005 |                   -0.0498 |    0.0780 |   -1.4287 |   0.2263 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.5448 |   0.5814 |                   -0.0366 |    0.0509 |   -1.6103 |   0.1826 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.6587 |   0.6702 |                   -0.0114 |    0.0557 |   -0.4587 |   0.6702 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.5841 |   0.5907 |                   -0.0066 |    0.0503 |   -0.2937 |   0.7836 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.6317 |   0.6277 |                    0.0040 |    0.0057 |    1.5618 |   0.1934 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.5984 |   0.5894 |                    0.0090 |    0.0130 |    1.5445 |   0.1973 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.5996 |   0.6280 |                   -0.0284 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| mango_khir     | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.5068 |   0.5837 |                   -0.0769 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| mango_khir     | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.5236 |   0.5186 |                    0.0050 |    0.0151 |    0.7436 |   0.4984 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.3211 |   0.3142 |                    0.0069 |    0.0120 |    1.2885 |   0.2670 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.6229 |   0.6094 |                    0.0135 |    0.0219 |    1.3774 |   0.2404 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.4938 |   0.4720 |                    0.0219 |    0.0308 |    1.5902 |   0.1870 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.6158 |   0.6095 |                    0.0063 |    0.0169 |    0.8413 |   0.4475 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.5364 |   0.5264 |                    0.0099 |    0.0302 |    0.7339 |   0.5037 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.6389 |   0.6346 |                    0.0043 |    0.0059 |    1.5997 |   0.1849 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.6132 |   0.6038 |                    0.0094 |    0.0133 |    1.5737 |   0.1907 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| mango_khir     | resnet50  | cls       | nan      | cost_f1  |         5 | 0.5669 |   0.6143 |                   -0.0474 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| mango_khir     | resnet50  | cls       | nan      | macro_f1 |         5 | 0.3967 |   0.5484 |                   -0.1516 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| ninepeach      | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.7754 |   0.7760 |                   -0.0007 |    0.0043 |   -0.3467 |   0.7463 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.5758 |   0.5735 |                    0.0023 |    0.0110 |    0.4624 |   0.6678 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.8180 |   0.8105 |                    0.0076 |    0.0260 |    0.6514 |   0.5503 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.6695 |   0.6510 |                    0.0186 |    0.0478 |    0.8692 |   0.4338 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.8557 |   0.8509 |                    0.0048 |    0.0154 |    0.6949 |   0.5254 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.7405 |   0.7251 |                    0.0154 |    0.0360 |    0.9544 |   0.3939 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.8987 |   0.9023 |                   -0.0036 |    0.0119 |   -0.6780 |   0.5350 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.8222 |   0.8239 |                   -0.0018 |    0.0219 |   -0.1792 |   0.8665 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | clip_b    | cls       | nan      | cost_f1  |         5 | 0.9221 |   0.9277 |                   -0.0056 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| ninepeach      | clip_b    | cls       | nan      | macro_f1 |         5 | 0.8520 |   0.8625 |                   -0.0105 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| ninepeach      | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.7941 |   0.7935 |                    0.0006 |    0.0079 |    0.1690 |   0.8740 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.5856 |   0.5927 |                   -0.0071 |    0.0298 |   -0.5323 |   0.6227 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.8777 |   0.8681 |                    0.0096 |    0.0093 |    2.3043 |   0.0825 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.7631 |   0.7446 |                    0.0185 |    0.0191 |    2.1677 |   0.0961 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.8981 |   0.8944 |                    0.0037 |    0.0067 |    1.2555 |   0.2776 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.8033 |   0.7958 |                    0.0075 |    0.0122 |    1.3684 |   0.2430 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.9194 |   0.9190 |                    0.0004 |    0.0036 |    0.2648 |   0.8042 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.8447 |   0.8454 |                   -0.0007 |    0.0079 |   -0.2025 |   0.8494 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_b  | cls       | nan      | cost_f1  |         5 | 0.9416 |   0.9442 |                   -0.0026 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| ninepeach      | dinov2_b  | cls       | nan      | macro_f1 |         5 | 0.8881 |   0.8939 |                   -0.0057 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| ninepeach      | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.7702 |   0.7707 |                   -0.0006 |    0.0116 |   -0.1060 |   0.9207 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.5590 |   0.5637 |                   -0.0047 |    0.0436 |   -0.2432 |   0.8198 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.8685 |   0.8723 |                   -0.0038 |    0.0064 |   -1.3409 |   0.2510 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.7499 |   0.7553 |                   -0.0054 |    0.0093 |   -1.2962 |   0.2646 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.8956 |   0.9001 |                   -0.0046 |    0.0068 |   -1.5015 |   0.2076 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.8008 |   0.8105 |                   -0.0097 |    0.0107 |   -2.0369 |   0.1113 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.9232 |   0.9261 |                   -0.0029 |    0.0030 |   -2.1959 |   0.0931 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.8548 |   0.8606 |                   -0.0058 |    0.0080 |   -1.6259 |   0.1793 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.9353 |   0.9353 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| ninepeach      | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.8767 |   0.8767 |                    0.0000 |    0.0000 |  nan      | nan      |                   0 |       nan      |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.7482 |   0.7648 |                   -0.0167 |    0.0180 |   -2.0752 |   0.1066 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.5249 |   0.5774 |                   -0.0526 |    0.0427 |   -2.7520 |   0.0513 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.8691 |   0.8601 |                    0.0090 |    0.0088 |    2.2922 |   0.0837 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.7552 |   0.7354 |                    0.0198 |    0.0167 |    2.6482 |   0.0571 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.8893 |   0.8843 |                    0.0050 |    0.0091 |    1.2129 |   0.2919 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.7935 |   0.7810 |                    0.0125 |    0.0160 |    1.7492 |   0.1552 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.9137 |   0.9124 |                    0.0013 |    0.0054 |    0.5452 |   0.6146 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.8386 |   0.8358 |                    0.0028 |    0.0108 |    0.5819 |   0.5919 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| ninepeach      | resnet50  | cls       | nan      | cost_f1  |         5 | 0.9172 |   0.9306 |                   -0.0134 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| ninepeach      | resnet50  | cls       | nan      | macro_f1 |         5 | 0.8414 |   0.8693 |                   -0.0279 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| raspgrade      | clip_b    | cls       |   1.0000 | cost_f1  |         5 | 0.3606 |   0.3579 |                    0.0028 |    0.0083 |    0.7511 |   0.4943 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | clip_b    | cls       |   1.0000 | macro_f1 |         5 | 0.1539 |   0.1501 |                    0.0037 |    0.0081 |    1.0331 |   0.3599 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | clip_b    | cls       |   5.0000 | cost_f1  |         5 | 0.3577 |   0.3391 |                    0.0186 |    0.0128 |    3.2640 |   0.0310 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | clip_b    | cls       |   5.0000 | macro_f1 |         5 | 0.1762 |   0.1582 |                    0.0180 |    0.0062 |    6.5339 |   0.0028 |                   5 |         1.0000 |   0.9497 | False                      |                 400 |
| raspgrade      | clip_b    | cls       |  10.0000 | cost_f1  |         5 | 0.3706 |   0.3505 |                    0.0202 |    0.0143 |    3.1632 |   0.0341 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | clip_b    | cls       |  10.0000 | macro_f1 |         5 | 0.2045 |   0.1839 |                    0.0207 |    0.0104 |    4.4573 |   0.0112 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | clip_b    | cls       |  50.0000 | cost_f1  |         5 | 0.4050 |   0.4114 |                   -0.0064 |    0.0161 |   -0.8814 |   0.4279 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | clip_b    | cls       |  50.0000 | macro_f1 |         5 | 0.2486 |   0.2611 |                   -0.0125 |    0.0140 |   -1.9862 |   0.1180 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | clip_b    | cls       | nan      | cost_f1  |         5 | 0.4214 |   0.4012 |                    0.0201 |    0.0000 |  inf      |   0.0000 |                   5 |         0.0000 |   0.0000 | True                       |                 400 |
| raspgrade      | clip_b    | cls       | nan      | macro_f1 |         5 | 0.1950 |   0.2160 |                   -0.0210 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| raspgrade      | dinov2_b  | cls       |   1.0000 | cost_f1  |         5 | 0.3480 |   0.3486 |                   -0.0006 |    0.0130 |   -0.1015 |   0.9240 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_b  | cls       |   1.0000 | macro_f1 |         5 | 0.1488 |   0.1528 |                   -0.0040 |    0.0080 |   -1.1106 |   0.3290 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_b  | cls       |   5.0000 | cost_f1  |         5 | 0.3721 |   0.3701 |                    0.0020 |    0.0107 |    0.4079 |   0.7042 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_b  | cls       |   5.0000 | macro_f1 |         5 | 0.1763 |   0.1783 |                   -0.0021 |    0.0115 |   -0.4060 |   0.7055 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_b  | cls       |  10.0000 | cost_f1  |         5 | 0.3961 |   0.3844 |                    0.0117 |    0.0080 |    3.2781 |   0.0306 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_b  | cls       |  10.0000 | macro_f1 |         5 | 0.2031 |   0.1994 |                    0.0037 |    0.0172 |    0.4841 |   0.6536 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_b  | cls       |  50.0000 | cost_f1  |         5 | 0.4425 |   0.4371 |                    0.0054 |    0.0077 |    1.5517 |   0.1957 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_b  | cls       |  50.0000 | macro_f1 |         5 | 0.2815 |   0.2876 |                   -0.0060 |    0.0056 |   -2.4014 |   0.0742 |                   1 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_b  | cls       | nan      | cost_f1  |         5 | 0.3578 |   0.3868 |                   -0.0290 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| raspgrade      | dinov2_b  | cls       | nan      | macro_f1 |         5 | 0.1874 |   0.2284 |                   -0.0410 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| raspgrade      | dinov2_s  | cls       |   1.0000 | cost_f1  |         5 | 0.3547 |   0.3426 |                    0.0121 |    0.0276 |    0.9818 |   0.3818 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_s  | cls       |   1.0000 | macro_f1 |         5 | 0.1773 |   0.1727 |                    0.0046 |    0.0229 |    0.4486 |   0.6770 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_s  | cls       |   5.0000 | cost_f1  |         5 | 0.3810 |   0.3697 |                    0.0113 |    0.0095 |    2.6512 |   0.0569 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_s  | cls       |   5.0000 | macro_f1 |         5 | 0.2017 |   0.1952 |                    0.0065 |    0.0044 |    3.2930 |   0.0301 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_s  | cls       |  10.0000 | cost_f1  |         5 | 0.4027 |   0.3947 |                    0.0080 |    0.0109 |    1.6505 |   0.1742 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_s  | cls       |  10.0000 | macro_f1 |         5 | 0.2336 |   0.2282 |                    0.0055 |    0.0112 |    1.0947 |   0.3351 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_s  | cls       |  50.0000 | cost_f1  |         5 | 0.4387 |   0.4294 |                    0.0093 |    0.0071 |    2.9435 |   0.0422 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_s  | cls       |  50.0000 | macro_f1 |         5 | 0.2949 |   0.2937 |                    0.0012 |    0.0125 |    0.2210 |   0.8360 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | dinov2_s  | cls       | nan      | cost_f1  |         5 | 0.3668 |   0.4240 |                   -0.0572 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| raspgrade      | dinov2_s  | cls       | nan      | macro_f1 |         5 | 0.2271 |   0.3040 |                   -0.0768 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |
| raspgrade      | resnet50  | cls       |   1.0000 | cost_f1  |         5 | 0.3132 |   0.3068 |                    0.0064 |    0.0168 |    0.8548 |   0.4408 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | resnet50  | cls       |   1.0000 | macro_f1 |         5 | 0.1477 |   0.1480 |                   -0.0003 |    0.0115 |   -0.0518 |   0.9612 |                   2 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | resnet50  | cls       |   5.0000 | cost_f1  |         5 | 0.3597 |   0.3508 |                    0.0090 |    0.0063 |    3.1678 |   0.0339 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | resnet50  | cls       |   5.0000 | macro_f1 |         5 | 0.1963 |   0.1864 |                    0.0099 |    0.0068 |    3.2740 |   0.0307 |                   5 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | resnet50  | cls       |  10.0000 | cost_f1  |         5 | 0.3820 |   0.3775 |                    0.0045 |    0.0054 |    1.8618 |   0.1361 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | resnet50  | cls       |  10.0000 | macro_f1 |         5 | 0.2253 |   0.2190 |                    0.0063 |    0.0066 |    2.1547 |   0.0975 |                   4 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | resnet50  | cls       |  50.0000 | cost_f1  |         5 | 0.4449 |   0.4390 |                    0.0059 |    0.0078 |    1.7024 |   0.1639 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | resnet50  | cls       |  50.0000 | macro_f1 |         5 | 0.2977 |   0.2956 |                    0.0021 |    0.0095 |    0.4906 |   0.6494 |                   3 |         1.0000 |   1.0000 | False                      |                 400 |
| raspgrade      | resnet50  | cls       | nan      | cost_f1  |         5 | 0.3821 |   0.3728 |                    0.0093 |    0.0000 |  inf      |   0.0000 |                   5 |         0.0000 |   0.0000 | True                       |                 400 |
| raspgrade      | resnet50  | cls       | nan      | macro_f1 |         5 | 0.2336 |   0.2572 |                   -0.0236 |    0.0000 | -inf      |   0.0000 |                   0 |         0.0000 |   0.0000 | True                       |                 400 |

`delta_corn_minus_linear` is the seed-paired mean difference (positive = CORN higher). `corn_better_pairs` counts seeds on which CORN is better under each metric's own direction (off-by-one is better when smaller). Both heads are fitted on the identical support of the identical cell, so the comparison isolates the ordinal constraint.

## Open-set rejection (mean ± sd over seeds)

| view                 | encoder   | variant   | protocol           | score       |   shot | auroc           | fpr95           | oscr            | known_acc       |   n_known_test |   n_unknown_test | thin   |   n_runs |
|:---------------------|:----------|:----------|:-------------------|:------------|-------:|:----------------|:----------------|:----------------|:----------------|---------------:|-----------------:|:-------|---------:|
| banana3              | dinov2_s  | cls       | P1_out_of_grade    | energy      |      5 | 0.4934 ± 0.1328 | 0.9495 ± 0.0463 | 0.4227 ± 0.0971 | 0.7649 ± 0.0103 |            112 |               66 | False  |        3 |
| banana3              | dinov2_s  | cls       | P1_out_of_grade    | energy      |    nan | 0.3534 ± 0.0000 | 0.9545 ± 0.0000 | 0.3513 ± 0.0000 | 0.9643 ± 0.0000 |            112 |               66 | False  |        3 |
| banana3              | dinov2_s  | cls       | P1_out_of_grade    | knn         |      5 | 0.8182 ± 0.0116 | 0.9040 ± 0.0231 | 0.6394 ± 0.0123 | 0.7649 ± 0.0103 |            112 |               66 | False  |        3 |
| banana3              | dinov2_s  | cls       | P1_out_of_grade    | knn         |    nan | 0.8678 ± 0.0000 | 0.8182 ± 0.0000 | 0.8447 ± 0.0000 | 0.9643 ± 0.0000 |            112 |               66 | False  |        3 |
| banana3              | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.8186 ± 0.0157 | 0.9091 ± 0.0303 | 0.6426 ± 0.0081 | 0.7649 ± 0.0103 |            112 |               66 | False  |        3 |
| banana3              | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.8999 ± 0.0000 | 0.7576 ± 0.0000 | 0.8738 ± 0.0000 | 0.9643 ± 0.0000 |            112 |               66 | False  |        3 |
| banana3              | dinov2_s  | cls       | P1_out_of_grade    | msp         |      5 | 0.4934 ± 0.1328 | 0.9495 ± 0.0463 | 0.4227 ± 0.0971 | 0.7649 ± 0.0103 |            112 |               66 | False  |        3 |
| banana3              | dinov2_s  | cls       | P1_out_of_grade    | msp         |    nan | 0.3534 ± 0.0000 | 0.9545 ± 0.0000 | 0.3513 ± 0.0000 | 0.9643 ± 0.0000 |            112 |               66 | False  |        3 |
| banana3              | dinov2_s  | cls       | P2_unseen_interior | energy      |      5 | 0.5317 ± 0.1586 | 0.9313 ± 0.0937 | 0.5120 ± 0.1689 | 0.8793 ± 0.0610 |            117 |               51 | False  |        6 |
| banana3              | dinov2_s  | cls       | P2_unseen_interior | energy      |    nan | 0.7042 ± 0.2200 | 0.7711 ± 0.1789 | 0.7001 ± 0.2203 | 0.9668 ± 0.0105 |            117 |               51 | False  |        6 |
| banana3              | dinov2_s  | cls       | P2_unseen_interior | knn         |      5 | 0.4169 ± 0.0335 | 0.9362 ± 0.0160 | 0.3873 ± 0.0491 | 0.8793 ± 0.0610 |            117 |               51 | False  |        6 |
| banana3              | dinov2_s  | cls       | P2_unseen_interior | knn         |    nan | 0.5469 ± 0.0281 | 0.8692 ± 0.0715 | 0.5424 ± 0.0324 | 0.9668 ± 0.0105 |            117 |               51 | False  |        6 |
| banana3              | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.4778 ± 0.0471 | 0.9319 ± 0.0355 | 0.4491 ± 0.0631 | 0.8793 ± 0.0610 |            117 |               51 | False  |        6 |
| banana3              | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.5754 ± 0.0078 | 0.8904 ± 0.0303 | 0.5704 ± 0.0131 | 0.9668 ± 0.0105 |            117 |               51 | False  |        6 |
| banana3              | dinov2_s  | cls       | P2_unseen_interior | msp         |      5 | 0.5317 ± 0.1586 | 0.9313 ± 0.0937 | 0.5120 ± 0.1689 | 0.8793 ± 0.0610 |            117 |               51 | False  |        6 |
| banana3              | dinov2_s  | cls       | P2_unseen_interior | msp         |    nan | 0.7042 ± 0.2200 | 0.7711 ± 0.1789 | 0.7001 ± 0.2203 | 0.9668 ± 0.0105 |            117 |               51 | False  |        6 |
| banana3              | dinov2_s  | cls       | P3_foreign         | energy      |      5 | 0.6707 ± 0.1148 | 0.8313 ± 0.0867 | 0.5284 ± 0.0555 | 0.7472 ± 0.0446 |            178 |              168 | False  |        3 |
| banana3              | dinov2_s  | cls       | P3_foreign         | energy      |    nan | 0.6677 ± 0.0000 | 0.8988 ± 0.0000 | 0.6546 ± 0.0000 | 0.9551 ± 0.0000 |            178 |              168 | False  |        3 |
| banana3              | dinov2_s  | cls       | P3_foreign         | knn         |      5 | 0.9589 ± 0.0031 | 0.3016 ± 0.0540 | 0.7315 ± 0.0469 | 0.7472 ± 0.0446 |            178 |              168 | False  |        3 |
| banana3              | dinov2_s  | cls       | P3_foreign         | knn         |    nan | 0.9782 ± 0.0000 | 0.0893 ± 0.0000 | 0.9454 ± 0.0000 | 0.9551 ± 0.0000 |            178 |              168 | False  |        3 |
| banana3              | dinov2_s  | cls       | P3_foreign         | mahalanobis |      5 | 0.9672 ± 0.0115 | 0.1944 ± 0.1429 | 0.7340 ± 0.0492 | 0.7472 ± 0.0446 |            178 |              168 | False  |        3 |
| banana3              | dinov2_s  | cls       | P3_foreign         | mahalanobis |    nan | 0.9794 ± 0.0000 | 0.0833 ± 0.0000 | 0.9462 ± 0.0000 | 0.9551 ± 0.0000 |            178 |              168 | False  |        3 |
| banana3              | dinov2_s  | cls       | P3_foreign         | msp         |      5 | 0.6612 ± 0.0392 | 0.8413 ± 0.1263 | 0.5313 ± 0.0204 | 0.7472 ± 0.0446 |            178 |              168 | False  |        3 |
| banana3              | dinov2_s  | cls       | P3_foreign         | msp         |    nan | 0.6722 ± 0.0000 | 0.8452 ± 0.0000 | 0.6614 ± 0.0000 | 0.9551 ± 0.0000 |            178 |              168 | False  |        3 |
| banana3              | resnet50  | cls       | P1_out_of_grade    | energy      |      5 | 0.3956 ± 0.1963 | 0.9848 ± 0.0262 | 0.2601 ± 0.1861 | 0.5565 ± 0.1254 |            112 |               66 | False  |        3 |
| banana3              | resnet50  | cls       | P1_out_of_grade    | energy      |    nan | 0.7385 ± 0.0000 | 0.8182 ± 0.0000 | 0.6572 ± 0.0000 | 0.8393 ± 0.0000 |            112 |               66 | False  |        3 |
| banana3              | resnet50  | cls       | P1_out_of_grade    | knn         |      5 | 0.8403 ± 0.0154 | 0.8131 ± 0.0463 | 0.4673 ± 0.1202 | 0.5565 ± 0.1254 |            112 |               66 | False  |        3 |
| banana3              | resnet50  | cls       | P1_out_of_grade    | knn         |    nan | 0.9091 ± 0.0000 | 0.5909 ± 0.0000 | 0.7829 ± 0.0000 | 0.8393 ± 0.0000 |            112 |               66 | False  |        3 |
| banana3              | resnet50  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.8384 ± 0.0211 | 0.8333 ± 0.0546 | 0.4694 ± 0.1227 | 0.5565 ± 0.1254 |            112 |               66 | False  |        3 |
| banana3              | resnet50  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.9393 ± 0.0000 | 0.5455 ± 0.0000 | 0.8048 ± 0.0000 | 0.8393 ± 0.0000 |            112 |               66 | False  |        3 |
| banana3              | resnet50  | cls       | P1_out_of_grade    | msp         |      5 | 0.3956 ± 0.1963 | 0.9848 ± 0.0262 | 0.2601 ± 0.1861 | 0.5565 ± 0.1254 |            112 |               66 | False  |        3 |
| banana3              | resnet50  | cls       | P1_out_of_grade    | msp         |    nan | 0.7385 ± 0.0000 | 0.8182 ± 0.0000 | 0.6572 ± 0.0000 | 0.8393 ± 0.0000 |            112 |               66 | False  |        3 |
| banana3              | resnet50  | cls       | P2_unseen_interior | energy      |      5 | 0.5342 ± 0.1493 | 0.9590 ± 0.0495 | 0.4758 ± 0.1282 | 0.8091 ± 0.0463 |            117 |               51 | False  |        6 |
| banana3              | resnet50  | cls       | P2_unseen_interior | energy      |    nan | 0.7581 ± 0.0001 | 0.8396 ± 0.0039 | 0.7361 ± 0.0232 | 0.9405 ± 0.0565 |            117 |               51 | False  |        6 |
| banana3              | resnet50  | cls       | P2_unseen_interior | knn         |      5 | 0.3899 ± 0.0642 | 0.9313 ± 0.0280 | 0.3360 ± 0.0593 | 0.8091 ± 0.0463 |            117 |               51 | False  |        6 |
| banana3              | resnet50  | cls       | P2_unseen_interior | knn         |    nan | 0.5046 ± 0.0744 | 0.8822 ± 0.0213 | 0.4901 ± 0.0586 | 0.9405 ± 0.0565 |            117 |               51 | False  |        6 |
| banana3              | resnet50  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.4467 ± 0.1052 | 0.9155 ± 0.0441 | 0.3943 ± 0.0952 | 0.8091 ± 0.0463 |            117 |               51 | False  |        6 |
| banana3              | resnet50  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.5762 ± 0.0836 | 0.8936 ± 0.0092 | 0.5560 ± 0.0615 | 0.9405 ± 0.0565 |            117 |               51 | False  |        6 |
| banana3              | resnet50  | cls       | P2_unseen_interior | msp         |      5 | 0.5342 ± 0.1493 | 0.9590 ± 0.0495 | 0.4758 ± 0.1282 | 0.8091 ± 0.0463 |            117 |               51 | False  |        6 |
| banana3              | resnet50  | cls       | P2_unseen_interior | msp         |    nan | 0.7581 ± 0.0001 | 0.8396 ± 0.0039 | 0.7361 ± 0.0232 | 0.9405 ± 0.0565 |            117 |               51 | False  |        6 |
| banana3              | resnet50  | cls       | P3_foreign         | energy      |      5 | 0.6618 ± 0.0166 | 0.9286 ± 0.0315 | 0.4732 ± 0.0243 | 0.6667 ± 0.0288 |            178 |              168 | False  |        3 |
| banana3              | resnet50  | cls       | P3_foreign         | energy      |    nan | 0.6612 ± 0.0000 | 0.8869 ± 0.0000 | 0.6256 ± 0.0000 | 0.8933 ± 0.0000 |            178 |              168 | False  |        3 |
| banana3              | resnet50  | cls       | P3_foreign         | knn         |      5 | 0.9807 ± 0.0070 | 0.1587 ± 0.0698 | 0.6581 ± 0.0302 | 0.6667 ± 0.0288 |            178 |              168 | False  |        3 |
| banana3              | resnet50  | cls       | P3_foreign         | knn         |    nan | 0.9932 ± 0.0000 | 0.0298 ± 0.0000 | 0.8903 ± 0.0000 | 0.8933 ± 0.0000 |            178 |              168 | False  |        3 |
| banana3              | resnet50  | cls       | P3_foreign         | mahalanobis |      5 | 0.9795 ± 0.0056 | 0.1567 ± 0.0566 | 0.6580 ± 0.0254 | 0.6667 ± 0.0288 |            178 |              168 | False  |        3 |
| banana3              | resnet50  | cls       | P3_foreign         | mahalanobis |    nan | 0.9943 ± 0.0000 | 0.0238 ± 0.0000 | 0.8894 ± 0.0000 | 0.8933 ± 0.0000 |            178 |              168 | False  |        3 |
| banana3              | resnet50  | cls       | P3_foreign         | msp         |      5 | 0.6233 ± 0.0649 | 0.9008 ± 0.0513 | 0.4551 ± 0.0521 | 0.6667 ± 0.0288 |            178 |              168 | False  |        3 |
| banana3              | resnet50  | cls       | P3_foreign         | msp         |    nan | 0.6172 ± 0.0000 | 0.8929 ± 0.0000 | 0.5882 ± 0.0000 | 0.8933 ± 0.0000 |            178 |              168 | False  |        3 |
| banana4              | dinov2_s  | cls       | P1_out_of_grade    | energy      |      5 | 0.6033 ± 0.1805 | 0.9351 ± 0.0589 | 0.5988 ± 0.1785 | 0.9331 ± 0.0662 |            264 |              113 | False  |        3 |
| banana4              | dinov2_s  | cls       | P1_out_of_grade    | energy      |    nan | 0.5366 ± 0.0000 | 1.0000 ± 0.0000 | 0.5366 ± 0.0000 | 1.0000 ± 0.0000 |            264 |              113 | False  |        3 |
| banana4              | dinov2_s  | cls       | P1_out_of_grade    | knn         |      5 | 0.8036 ± 0.0279 | 0.8584 ± 0.1457 | 0.7464 ± 0.0571 | 0.9331 ± 0.0662 |            264 |              113 | False  |        3 |
| banana4              | dinov2_s  | cls       | P1_out_of_grade    | knn         |    nan | 0.9285 ± 0.0000 | 0.3717 ± 0.0000 | 0.9285 ± 0.0000 | 1.0000 ± 0.0000 |            264 |              113 | False  |        3 |
| banana4              | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.8238 ± 0.0358 | 0.7994 ± 0.0850 | 0.7685 ± 0.0573 | 0.9331 ± 0.0662 |            264 |              113 | False  |        3 |
| banana4              | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.9132 ± 0.0000 | 0.4425 ± 0.0000 | 0.9132 ± 0.0000 | 1.0000 ± 0.0000 |            264 |              113 | False  |        3 |
| banana4              | dinov2_s  | cls       | P1_out_of_grade    | msp         |      5 | 0.6033 ± 0.1805 | 0.9351 ± 0.0589 | 0.5988 ± 0.1785 | 0.9331 ± 0.0662 |            264 |              113 | False  |        3 |
| banana4              | dinov2_s  | cls       | P1_out_of_grade    | msp         |    nan | 0.5366 ± 0.0000 | 1.0000 ± 0.0000 | 0.5366 ± 0.0000 | 1.0000 ± 0.0000 |            264 |              113 | False  |        3 |
| banana4              | dinov2_s  | cls       | P2_unseen_interior | energy      |      5 | 0.6965 ± 0.2175 | 0.7494 ± 0.3658 | 0.6905 ± 0.2206 | 0.9397 ± 0.0541 |            223 |              110 | False  |        6 |
| banana4              | dinov2_s  | cls       | P2_unseen_interior | energy      |    nan | 0.6895 ± 0.3291 | 0.5325 ± 0.5122 | 0.6895 ± 0.3291 | 0.9869 ± 0.0144 |            223 |              110 | False  |        6 |
| banana4              | dinov2_s  | cls       | P2_unseen_interior | knn         |      5 | 0.6723 ± 0.1343 | 0.8697 ± 0.0838 | 0.6221 ± 0.0996 | 0.9397 ± 0.0541 |            223 |              110 | False  |        6 |
| banana4              | dinov2_s  | cls       | P2_unseen_interior | knn         |    nan | 0.9633 ± 0.0073 | 0.2390 ± 0.0228 | 0.9502 ± 0.0070 | 0.9869 ± 0.0144 |            223 |              110 | False  |        6 |
| banana4              | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.7663 ± 0.0555 | 0.8011 ± 0.0663 | 0.7167 ± 0.0260 | 0.9397 ± 0.0541 |            223 |              110 | False  |        6 |
| banana4              | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.9385 ± 0.0107 | 0.4844 ± 0.1963 | 0.9254 ± 0.0250 | 0.9869 ± 0.0144 |            223 |              110 | False  |        6 |
| banana4              | dinov2_s  | cls       | P2_unseen_interior | msp         |      5 | 0.6965 ± 0.2175 | 0.7494 ± 0.3658 | 0.6905 ± 0.2206 | 0.9397 ± 0.0541 |            223 |              110 | False  |        6 |
| banana4              | dinov2_s  | cls       | P2_unseen_interior | msp         |    nan | 0.6895 ± 0.3291 | 0.5325 ± 0.5122 | 0.6895 ± 0.3291 | 0.9869 ± 0.0144 |            223 |              110 | False  |        6 |
| banana4              | dinov2_s  | cls       | P3_rotten          | energy      |      5 | 0.6023 ± 0.0644 | 0.9009 ± 0.0776 | 0.5780 ± 0.0631 | 0.9266 ± 0.0252 |            377 |              185 | False  |        3 |
| banana4              | dinov2_s  | cls       | P3_rotten          | energy      |    nan | 0.8105 ± 0.0000 | 0.6324 ± 0.0000 | 0.8053 ± 0.0000 | 0.9841 ± 0.0000 |            377 |              185 | False  |        3 |
| banana4              | dinov2_s  | cls       | P3_rotten          | knn         |      5 | 0.8747 ± 0.0163 | 0.6432 ± 0.2202 | 0.8071 ± 0.0077 | 0.9266 ± 0.0252 |            377 |              185 | False  |        3 |
| banana4              | dinov2_s  | cls       | P3_rotten          | knn         |    nan | 0.9789 ± 0.0000 | 0.0973 ± 0.0000 | 0.9631 ± 0.0000 | 0.9841 ± 0.0000 |            377 |              185 | False  |        3 |
| banana4              | dinov2_s  | cls       | P3_rotten          | mahalanobis |      5 | 0.8960 ± 0.0268 | 0.5892 ± 0.2250 | 0.8295 ± 0.0148 | 0.9266 ± 0.0252 |            377 |              185 | False  |        3 |
| banana4              | dinov2_s  | cls       | P3_rotten          | mahalanobis |    nan | 0.9524 ± 0.0000 | 0.2270 ± 0.0000 | 0.9366 ± 0.0000 | 0.9841 ± 0.0000 |            377 |              185 | False  |        3 |
| banana4              | dinov2_s  | cls       | P3_rotten          | msp         |      5 | 0.6581 ± 0.0667 | 0.8829 ± 0.0900 | 0.6399 ± 0.0657 | 0.9266 ± 0.0252 |            377 |              185 | False  |        3 |
| banana4              | dinov2_s  | cls       | P3_rotten          | msp         |    nan | 0.8170 ± 0.0000 | 0.7243 ± 0.0000 | 0.8137 ± 0.0000 | 0.9841 ± 0.0000 |            377 |              185 | False  |        3 |
| banana4              | resnet50  | cls       | P1_out_of_grade    | energy      |      5 | 0.5211 ± 0.0958 | 0.9410 ± 0.0399 | 0.4579 ± 0.0613 | 0.7891 ± 0.0662 |            264 |              113 | False  |        3 |
| banana4              | resnet50  | cls       | P1_out_of_grade    | energy      |    nan | 0.5896 ± 0.0000 | 0.9912 ± 0.0000 | 0.5896 ± 0.0000 | 0.9924 ± 0.0000 |            264 |              113 | False  |        3 |
| banana4              | resnet50  | cls       | P1_out_of_grade    | knn         |      5 | 0.7826 ± 0.0330 | 0.7021 ± 0.1608 | 0.6098 ± 0.0698 | 0.7891 ± 0.0662 |            264 |              113 | False  |        3 |
| banana4              | resnet50  | cls       | P1_out_of_grade    | knn         |    nan | 0.9123 ± 0.0000 | 0.3097 ± 0.0000 | 0.9056 ± 0.0000 | 0.9924 ± 0.0000 |            264 |              113 | False  |        3 |
| banana4              | resnet50  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.7961 ± 0.0229 | 0.6903 ± 0.1573 | 0.6239 ± 0.0716 | 0.7891 ± 0.0662 |            264 |              113 | False  |        3 |
| banana4              | resnet50  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.8804 ± 0.0000 | 0.4248 ± 0.0000 | 0.8737 ± 0.0000 | 0.9924 ± 0.0000 |            264 |              113 | False  |        3 |
| banana4              | resnet50  | cls       | P1_out_of_grade    | msp         |      5 | 0.5211 ± 0.0958 | 0.9410 ± 0.0399 | 0.4579 ± 0.0613 | 0.7891 ± 0.0662 |            264 |              113 | False  |        3 |
| banana4              | resnet50  | cls       | P1_out_of_grade    | msp         |    nan | 0.5896 ± 0.0000 | 0.9912 ± 0.0000 | 0.5896 ± 0.0000 | 0.9924 ± 0.0000 |            264 |              113 | False  |        3 |
| banana4              | resnet50  | cls       | P2_unseen_interior | energy      |      5 | 0.6675 ± 0.1557 | 0.9130 ± 0.0821 | 0.6374 ± 0.1697 | 0.8709 ± 0.0760 |            223 |              110 | False  |        6 |
| banana4              | resnet50  | cls       | P2_unseen_interior | energy      |    nan | 0.7998 ± 0.1937 | 0.5714 ± 0.4695 | 0.7995 ± 0.1941 | 0.9757 ± 0.0267 |            223 |              110 | False  |        6 |
| banana4              | resnet50  | cls       | P2_unseen_interior | knn         |      5 | 0.5376 ± 0.1780 | 0.8825 ± 0.1184 | 0.4428 ± 0.1582 | 0.8709 ± 0.0760 |            223 |              110 | False  |        6 |
| banana4              | resnet50  | cls       | P2_unseen_interior | knn         |    nan | 0.8824 ± 0.0462 | 0.4156 ± 0.1067 | 0.8588 ± 0.0203 | 0.9757 ± 0.0267 |            223 |              110 | False  |        6 |
| banana4              | resnet50  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.6323 ± 0.1487 | 0.8545 ± 0.1325 | 0.5389 ± 0.1318 | 0.8709 ± 0.0760 |            223 |              110 | False  |        6 |
| banana4              | resnet50  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.8601 ± 0.0700 | 0.5097 ± 0.0605 | 0.8363 ± 0.0438 | 0.9757 ± 0.0267 |            223 |              110 | False  |        6 |
| banana4              | resnet50  | cls       | P2_unseen_interior | msp         |      5 | 0.6675 ± 0.1557 | 0.9130 ± 0.0821 | 0.6374 ± 0.1697 | 0.8709 ± 0.0760 |            223 |              110 | False  |        6 |
| banana4              | resnet50  | cls       | P2_unseen_interior | msp         |    nan | 0.7998 ± 0.1937 | 0.5714 ± 0.4695 | 0.7995 ± 0.1941 | 0.9757 ± 0.0267 |            223 |              110 | False  |        6 |
| banana4              | resnet50  | cls       | P3_rotten          | energy      |      5 | 0.6593 ± 0.0889 | 0.8631 ± 0.1215 | 0.5461 ± 0.0283 | 0.7816 ± 0.0629 |            377 |              185 | False  |        3 |
| banana4              | resnet50  | cls       | P3_rotten          | energy      |    nan | 0.7947 ± 0.0000 | 0.7946 ± 0.0000 | 0.7839 ± 0.0000 | 0.9655 ± 0.0000 |            377 |              185 | False  |        3 |
| banana4              | resnet50  | cls       | P3_rotten          | knn         |      5 | 0.7846 ± 0.0268 | 0.7730 ± 0.1749 | 0.5944 ± 0.0773 | 0.7816 ± 0.0629 |            377 |              185 | False  |        3 |
| banana4              | resnet50  | cls       | P3_rotten          | knn         |    nan | 0.9574 ± 0.0000 | 0.1892 ± 0.0000 | 0.9234 ± 0.0000 | 0.9655 ± 0.0000 |            377 |              185 | False  |        3 |
| banana4              | resnet50  | cls       | P3_rotten          | mahalanobis |      5 | 0.8320 ± 0.0703 | 0.7297 ± 0.2442 | 0.6434 ± 0.1112 | 0.7816 ± 0.0629 |            377 |              185 | False  |        3 |
| banana4              | resnet50  | cls       | P3_rotten          | mahalanobis |    nan | 0.9255 ± 0.0000 | 0.3459 ± 0.0000 | 0.8920 ± 0.0000 | 0.9655 ± 0.0000 |            377 |              185 | False  |        3 |
| banana4              | resnet50  | cls       | P3_rotten          | msp         |      5 | 0.6550 ± 0.0540 | 0.9171 ± 0.0368 | 0.5551 ± 0.0076 | 0.7816 ± 0.0629 |            377 |              185 | False  |        3 |
| banana4              | resnet50  | cls       | P3_rotten          | msp         |    nan | 0.8002 ± 0.0000 | 0.7459 ± 0.0000 | 0.7915 ± 0.0000 | 0.9655 ± 0.0000 |            377 |              185 | False  |        3 |
| f360rot              | dinov2_s  | cls       | P3_rotten          | energy      |      5 | 0.8332 ± 0.0099 | 0.9605 ± 0.0324 | 0.6992 ± 0.0070 | 0.8299 ± 0.0053 |           1811 |              650 | False  |        3 |
| f360rot              | dinov2_s  | cls       | P3_rotten          | energy      |    nan | 0.6025 ± 0.0000 | 0.9985 ± 0.0000 | 0.6005 ± 0.0000 | 0.9884 ± 0.0000 |           1811 |              650 | False  |        3 |
| f360rot              | dinov2_s  | cls       | P3_rotten          | knn         |      5 | 0.8969 ± 0.0161 | 0.6549 ± 0.0913 | 0.7514 ± 0.0181 | 0.8299 ± 0.0053 |           1811 |              650 | False  |        3 |
| f360rot              | dinov2_s  | cls       | P3_rotten          | knn         |    nan | 0.8700 ± 0.0000 | 0.7954 ± 0.0000 | 0.8636 ± 0.0000 | 0.9884 ± 0.0000 |           1811 |              650 | False  |        3 |
| f360rot              | dinov2_s  | cls       | P3_rotten          | mahalanobis |      5 | 0.8779 ± 0.0112 | 0.6313 ± 0.1112 | 0.7457 ± 0.0141 | 0.8299 ± 0.0053 |           1811 |              650 | False  |        3 |
| f360rot              | dinov2_s  | cls       | P3_rotten          | mahalanobis |    nan | 0.9567 ± 0.0000 | 0.3400 ± 0.0000 | 0.9476 ± 0.0000 | 0.9884 ± 0.0000 |           1811 |              650 | False  |        3 |
| f360rot              | dinov2_s  | cls       | P3_rotten          | msp         |      5 | 0.5110 ± 0.0079 | 1.0000 ± 0.0000 | 0.4568 ± 0.0057 | 0.8299 ± 0.0053 |           1811 |              650 | False  |        3 |
| f360rot              | dinov2_s  | cls       | P3_rotten          | msp         |    nan | 0.3516 ± 0.0000 | 1.0000 ± 0.0000 | 0.3516 ± 0.0000 | 0.9884 ± 0.0000 |           1811 |              650 | False  |        3 |
| f360rot              | resnet50  | cls       | P3_rotten          | energy      |      5 | 0.9081 ± 0.0090 | 0.6195 ± 0.1454 | 0.6853 ± 0.0269 | 0.7508 ± 0.0203 |           1811 |              650 | False  |        3 |
| f360rot              | resnet50  | cls       | P3_rotten          | energy      |    nan | 0.6717 ± 0.0000 | 0.9277 ± 0.0000 | 0.6494 ± 0.0000 | 0.9503 ± 0.0000 |           1811 |              650 | False  |        3 |
| f360rot              | resnet50  | cls       | P3_rotten          | knn         |      5 | 0.9077 ± 0.0087 | 0.6872 ± 0.0784 | 0.6896 ± 0.0264 | 0.7508 ± 0.0203 |           1811 |              650 | False  |        3 |
| f360rot              | resnet50  | cls       | P3_rotten          | knn         |    nan | 0.9582 ± 0.0000 | 0.2769 ± 0.0000 | 0.9167 ± 0.0000 | 0.9503 ± 0.0000 |           1811 |              650 | False  |        3 |
| f360rot              | resnet50  | cls       | P3_rotten          | mahalanobis |      5 | 0.9088 ± 0.0134 | 0.7108 ± 0.0717 | 0.6961 ± 0.0121 | 0.7508 ± 0.0203 |           1811 |              650 | False  |        3 |
| f360rot              | resnet50  | cls       | P3_rotten          | mahalanobis |    nan | 0.9630 ± 0.0000 | 0.2677 ± 0.0000 | 0.9167 ± 0.0000 | 0.9503 ± 0.0000 |           1811 |              650 | False  |        3 |
| f360rot              | resnet50  | cls       | P3_rotten          | msp         |      5 | 0.5536 ± 0.0176 | 0.9979 ± 0.0018 | 0.4574 ± 0.0119 | 0.7508 ± 0.0203 |           1811 |              650 | False  |        3 |
| f360rot              | resnet50  | cls       | P3_rotten          | msp         |    nan | 0.4005 ± 0.0000 | 1.0000 ± 0.0000 | 0.3985 ± 0.0000 | 0.9503 ± 0.0000 |           1811 |              650 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_foreign         | energy      |      5 | 0.9875 ± 0.0064 | 0.0751 ± 0.0516 | 0.9864 ± 0.0067 | 0.9985 ± 0.0006 |            900 |              630 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_foreign         | energy      |    nan | 0.9911 ± 0.0000 | 0.0429 ± 0.0000 | 0.9911 ± 0.0000 | 1.0000 ± 0.0000 |            900 |              630 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_foreign         | knn         |      5 | 0.9945 ± 0.0019 | 0.0085 ± 0.0033 | 0.9930 ± 0.0022 | 0.9985 ± 0.0006 |            900 |              630 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_foreign         | knn         |    nan | 0.9995 ± 0.0000 | 0.0000 ± 0.0000 | 0.9995 ± 0.0000 | 1.0000 ± 0.0000 |            900 |              630 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_foreign         | mahalanobis |      5 | 0.9931 ± 0.0039 | 0.0196 ± 0.0192 | 0.9918 ± 0.0042 | 0.9985 ± 0.0006 |            900 |              630 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_foreign         | mahalanobis |    nan | 0.9933 ± 0.0000 | 0.0016 ± 0.0000 | 0.9933 ± 0.0000 | 1.0000 ± 0.0000 |            900 |              630 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_foreign         | msp         |      5 | 0.9846 ± 0.0072 | 0.0894 ± 0.0531 | 0.9838 ± 0.0074 | 0.9985 ± 0.0006 |            900 |              630 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_foreign         | msp         |    nan | 0.9887 ± 0.0000 | 0.0492 ± 0.0000 | 0.9887 ± 0.0000 | 1.0000 ± 0.0000 |            900 |              630 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_rotten          | energy      |      5 | 0.8830 ± 0.0060 | 0.4874 ± 0.0238 | 0.8826 ± 0.0059 | 0.9985 ± 0.0006 |            900 |              900 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_rotten          | energy      |    nan | 0.9143 ± 0.0000 | 0.3622 ± 0.0000 | 0.9143 ± 0.0000 | 1.0000 ± 0.0000 |            900 |              900 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_rotten          | knn         |      5 | 0.9432 ± 0.0080 | 0.2985 ± 0.0178 | 0.9424 ± 0.0080 | 0.9985 ± 0.0006 |            900 |              900 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_rotten          | knn         |    nan | 0.9871 ± 0.0000 | 0.0578 ± 0.0000 | 0.9871 ± 0.0000 | 1.0000 ± 0.0000 |            900 |              900 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_rotten          | mahalanobis |      5 | 0.9550 ± 0.0064 | 0.2567 ± 0.0373 | 0.9542 ± 0.0066 | 0.9985 ± 0.0006 |            900 |              900 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_rotten          | mahalanobis |    nan | 0.9902 ± 0.0000 | 0.0311 ± 0.0000 | 0.9902 ± 0.0000 | 1.0000 ± 0.0000 |            900 |              900 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_rotten          | msp         |      5 | 0.8832 ± 0.0071 | 0.4833 ± 0.0161 | 0.8830 ± 0.0070 | 0.9985 ± 0.0006 |            900 |              900 | False  |        3 |
| ffr                  | dinov2_s  | cls       | P3_rotten          | msp         |    nan | 0.9195 ± 0.0000 | 0.3722 ± 0.0000 | 0.9195 ± 0.0000 | 1.0000 ± 0.0000 |            900 |              900 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_foreign         | energy      |      5 | 0.9621 ± 0.0246 | 0.2169 ± 0.1514 | 0.9414 ± 0.0233 | 0.9696 ± 0.0061 |            900 |              630 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_foreign         | energy      |    nan | 0.9875 ± 0.0000 | 0.0302 ± 0.0000 | 0.9821 ± 0.0000 | 0.9922 ± 0.0000 |            900 |              630 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_foreign         | knn         |      5 | 0.9634 ± 0.0094 | 0.2921 ± 0.0870 | 0.9380 ± 0.0127 | 0.9696 ± 0.0061 |            900 |              630 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_foreign         | knn         |    nan | 0.9989 ± 0.0000 | 0.0000 ± 0.0000 | 0.9912 ± 0.0000 | 0.9922 ± 0.0000 |            900 |              630 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_foreign         | mahalanobis |      5 | 0.9855 ± 0.0070 | 0.0767 ± 0.0763 | 0.9580 ± 0.0109 | 0.9696 ± 0.0061 |            900 |              630 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_foreign         | mahalanobis |    nan | 0.9974 ± 0.0000 | 0.0016 ± 0.0000 | 0.9896 ± 0.0000 | 0.9922 ± 0.0000 |            900 |              630 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_foreign         | msp         |      5 | 0.9576 ± 0.0297 | 0.2672 ± 0.1397 | 0.9379 ± 0.0283 | 0.9696 ± 0.0061 |            900 |              630 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_foreign         | msp         |    nan | 0.9862 ± 0.0000 | 0.0159 ± 0.0000 | 0.9819 ± 0.0000 | 0.9922 ± 0.0000 |            900 |              630 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_rotten          | energy      |      5 | 0.8295 ± 0.0300 | 0.6011 ± 0.1546 | 0.8180 ± 0.0270 | 0.9696 ± 0.0061 |            900 |              900 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_rotten          | energy      |    nan | 0.9029 ± 0.0000 | 0.3456 ± 0.0000 | 0.8998 ± 0.0000 | 0.9922 ± 0.0000 |            900 |              900 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_rotten          | knn         |      5 | 0.8749 ± 0.0375 | 0.4993 ± 0.1085 | 0.8546 ± 0.0369 | 0.9696 ± 0.0061 |            900 |              900 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_rotten          | knn         |    nan | 0.9743 ± 0.0000 | 0.1411 ± 0.0000 | 0.9675 ± 0.0000 | 0.9922 ± 0.0000 |            900 |              900 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_rotten          | mahalanobis |      5 | 0.9253 ± 0.0130 | 0.3389 ± 0.0595 | 0.9032 ± 0.0138 | 0.9696 ± 0.0061 |            900 |              900 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_rotten          | mahalanobis |    nan | 0.9794 ± 0.0000 | 0.1122 ± 0.0000 | 0.9721 ± 0.0000 | 0.9922 ± 0.0000 |            900 |              900 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_rotten          | msp         |      5 | 0.8274 ± 0.0317 | 0.6330 ± 0.1539 | 0.8172 ± 0.0293 | 0.9696 ± 0.0061 |            900 |              900 | False  |        3 |
| ffr                  | resnet50  | cls       | P3_rotten          | msp         |    nan | 0.8989 ± 0.0000 | 0.3533 ± 0.0000 | 0.8972 ± 0.0000 | 0.9922 ± 0.0000 |            900 |              900 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P1_out_of_grade    | energy      |      5 | 0.5513 ± 0.0414 | 0.9181 ± 0.0730 | 0.3742 ± 0.0704 | 0.6602 ± 0.1583 |            155 |               57 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P1_out_of_grade    | energy      |    nan | 0.7161 ± 0.0000 | 0.9649 ± 0.0000 | 0.6337 ± 0.0000 | 0.8323 ± 0.0000 |            155 |               57 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P1_out_of_grade    | knn         |      5 | 0.6996 ± 0.0695 | 0.8830 ± 0.0203 | 0.4844 ± 0.1368 | 0.6602 ± 0.1583 |            155 |               57 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P1_out_of_grade    | knn         |    nan | 0.7331 ± 0.0000 | 0.5789 ± 0.0000 | 0.6241 ± 0.0000 | 0.8323 ± 0.0000 |            155 |               57 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.6993 ± 0.0366 | 0.8830 ± 0.0203 | 0.4770 ± 0.1181 | 0.6602 ± 0.1583 |            155 |               57 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.7461 ± 0.0000 | 0.6316 ± 0.0000 | 0.6298 ± 0.0000 | 0.8323 ± 0.0000 |            155 |               57 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P1_out_of_grade    | msp         |      5 | 0.5513 ± 0.0414 | 0.9181 ± 0.0730 | 0.3742 ± 0.0704 | 0.6602 ± 0.1583 |            155 |               57 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P1_out_of_grade    | msp         |    nan | 0.7161 ± 0.0000 | 0.9649 ± 0.0000 | 0.6337 ± 0.0000 | 0.8323 ± 0.0000 |            155 |               57 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P2_unseen_interior | energy      |      5 | 0.5977 ± 0.0920 | 0.9584 ± 0.0319 | 0.4832 ± 0.1082 | 0.6951 ± 0.0556 |            105 |               48 | False  |        6 |
| fruit12_apple        | dinov2_s  | cls       | P2_unseen_interior | energy      |    nan | 0.6365 ± 0.1274 | 0.8451 ± 0.0556 | 0.6138 ± 0.1155 | 0.9206 ± 0.0069 |            105 |               48 | False  |        6 |
| fruit12_apple        | dinov2_s  | cls       | P2_unseen_interior | knn         |      5 | 0.5389 ± 0.0696 | 0.9358 ± 0.0684 | 0.3844 ± 0.0663 | 0.6951 ± 0.0556 |            105 |               48 | False  |        6 |
| fruit12_apple        | dinov2_s  | cls       | P2_unseen_interior | knn         |    nan | 0.6795 ± 0.0844 | 0.9569 ± 0.0244 | 0.6368 ± 0.0688 | 0.9206 ± 0.0069 |            105 |               48 | False  |        6 |
| fruit12_apple        | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.5776 ± 0.0691 | 0.9566 ± 0.0339 | 0.4158 ± 0.0714 | 0.6951 ± 0.0556 |            105 |               48 | False  |        6 |
| fruit12_apple        | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.6713 ± 0.0492 | 0.9371 ± 0.0232 | 0.6309 ± 0.0354 | 0.9206 ± 0.0069 |            105 |               48 | False  |        6 |
| fruit12_apple        | dinov2_s  | cls       | P2_unseen_interior | msp         |      5 | 0.5977 ± 0.0920 | 0.9584 ± 0.0319 | 0.4832 ± 0.1082 | 0.6951 ± 0.0556 |            105 |               48 | False  |        6 |
| fruit12_apple        | dinov2_s  | cls       | P2_unseen_interior | msp         |    nan | 0.6365 ± 0.1274 | 0.8451 ± 0.0556 | 0.6138 ± 0.1155 | 0.9206 ± 0.0069 |            105 |               48 | False  |        6 |
| fruit12_apple        | dinov2_s  | cls       | P3_foreign         | energy      |      5 | 0.7793 ± 0.1333 | 0.8080 ± 0.2119 | 0.5294 ± 0.1262 | 0.6509 ± 0.1226 |            212 |              500 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_foreign         | energy      |    nan | 0.7215 ± 0.0000 | 0.9080 ± 0.0000 | 0.6471 ± 0.0000 | 0.8160 ± 0.0000 |            212 |              500 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_foreign         | knn         |      5 | 0.9406 ± 0.0309 | 0.3787 ± 0.2545 | 0.6177 ± 0.1251 | 0.6509 ± 0.1226 |            212 |              500 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_foreign         | knn         |    nan | 0.9771 ± 0.0000 | 0.0000 ± 0.0000 | 0.7934 ± 0.0000 | 0.8160 ± 0.0000 |            212 |              500 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_foreign         | mahalanobis |      5 | 0.9522 ± 0.0110 | 0.2793 ± 0.1712 | 0.6222 ± 0.1277 | 0.6509 ± 0.1226 |            212 |              500 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_foreign         | mahalanobis |    nan | 0.9812 ± 0.0000 | 0.0840 ± 0.0000 | 0.7984 ± 0.0000 | 0.8160 ± 0.0000 |            212 |              500 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_foreign         | msp         |      5 | 0.7421 ± 0.1647 | 0.7967 ± 0.2304 | 0.5091 ± 0.1426 | 0.6509 ± 0.1226 |            212 |              500 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_foreign         | msp         |    nan | 0.6952 ± 0.0000 | 0.9060 ± 0.0000 | 0.6313 ± 0.0000 | 0.8160 ± 0.0000 |            212 |              500 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_rotten          | energy      |      5 | 0.5815 ± 0.0462 | 0.8758 ± 0.0742 | 0.3587 ± 0.0885 | 0.5597 ± 0.1126 |            212 |               51 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_rotten          | energy      |    nan | 0.5125 ± 0.0000 | 0.9216 ± 0.0000 | 0.4648 ± 0.0000 | 0.8160 ± 0.0000 |            212 |               51 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_rotten          | knn         |      5 | 0.7501 ± 0.0212 | 0.8039 ± 0.0899 | 0.4378 ± 0.0887 | 0.5597 ± 0.1126 |            212 |               51 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_rotten          | knn         |    nan | 0.8205 ± 0.0000 | 0.7059 ± 0.0000 | 0.6848 ± 0.0000 | 0.8160 ± 0.0000 |            212 |               51 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_rotten          | mahalanobis |      5 | 0.7811 ± 0.0091 | 0.8497 ± 0.0113 | 0.4617 ± 0.0909 | 0.5597 ± 0.1126 |            212 |               51 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_rotten          | mahalanobis |    nan | 0.8108 ± 0.0000 | 0.7451 ± 0.0000 | 0.6751 ± 0.0000 | 0.8160 ± 0.0000 |            212 |               51 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_rotten          | msp         |      5 | 0.5695 ± 0.0398 | 0.8497 ± 0.0493 | 0.3525 ± 0.0572 | 0.5597 ± 0.1126 |            212 |               51 | False  |        3 |
| fruit12_apple        | dinov2_s  | cls       | P3_rotten          | msp         |    nan | 0.5014 ± 0.0000 | 0.9216 ± 0.0000 | 0.4556 ± 0.0000 | 0.8160 ± 0.0000 |            212 |               51 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P1_out_of_grade    | energy      |      5 | 0.6327 ± 0.0901 | 0.8538 ± 0.2532 | 0.3876 ± 0.0842 | 0.6280 ± 0.1970 |            155 |               57 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P1_out_of_grade    | energy      |    nan | 0.7337 ± 0.0000 | 0.9649 ± 0.0000 | 0.6658 ± 0.0000 | 0.8710 ± 0.0000 |            155 |               57 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P1_out_of_grade    | knn         |      5 | 0.6924 ± 0.0784 | 0.7836 ± 0.0203 | 0.4567 ± 0.1615 | 0.6280 ± 0.1970 |            155 |               57 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P1_out_of_grade    | knn         |    nan | 0.7301 ± 0.0000 | 0.7018 ± 0.0000 | 0.6415 ± 0.0000 | 0.8710 ± 0.0000 |            155 |               57 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.6964 ± 0.0102 | 0.8129 ± 0.0203 | 0.4483 ± 0.1325 | 0.6280 ± 0.1970 |            155 |               57 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.7520 ± 0.0000 | 0.6491 ± 0.0000 | 0.6601 ± 0.0000 | 0.8710 ± 0.0000 |            155 |               57 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P1_out_of_grade    | msp         |      5 | 0.6327 ± 0.0901 | 0.8538 ± 0.2532 | 0.3876 ± 0.0842 | 0.6280 ± 0.1970 |            155 |               57 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P1_out_of_grade    | msp         |    nan | 0.7337 ± 0.0000 | 0.9649 ± 0.0000 | 0.6658 ± 0.0000 | 0.8710 ± 0.0000 |            155 |               57 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P2_unseen_interior | energy      |      5 | 0.5703 ± 0.0855 | 0.9255 ± 0.0711 | 0.4472 ± 0.0970 | 0.7001 ± 0.1064 |            105 |               48 | False  |        6 |
| fruit12_apple        | resnet50  | cls       | P2_unseen_interior | energy      |    nan | 0.6374 ± 0.1318 | 0.9314 ± 0.0067 | 0.6104 ± 0.1196 | 0.9036 ± 0.0013 |            105 |               48 | False  |        6 |
| fruit12_apple        | resnet50  | cls       | P2_unseen_interior | knn         |      5 | 0.5489 ± 0.0920 | 0.9042 ± 0.0928 | 0.3976 ± 0.0539 | 0.7001 ± 0.1064 |            105 |               48 | False  |        6 |
| fruit12_apple        | resnet50  | cls       | P2_unseen_interior | knn         |    nan | 0.6933 ± 0.1135 | 0.9429 ± 0.0398 | 0.6456 ± 0.1012 | 0.9036 ± 0.0013 |            105 |               48 | False  |        6 |
| fruit12_apple        | resnet50  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.6140 ± 0.0890 | 0.9559 ± 0.0338 | 0.4508 ± 0.0804 | 0.7001 ± 0.1064 |            105 |               48 | False  |        6 |
| fruit12_apple        | resnet50  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.7223 ± 0.0676 | 0.9371 ± 0.0232 | 0.6722 ± 0.0641 | 0.9036 ± 0.0013 |            105 |               48 | False  |        6 |
| fruit12_apple        | resnet50  | cls       | P2_unseen_interior | msp         |      5 | 0.5703 ± 0.0855 | 0.9255 ± 0.0711 | 0.4472 ± 0.0970 | 0.7001 ± 0.1064 |            105 |               48 | False  |        6 |
| fruit12_apple        | resnet50  | cls       | P2_unseen_interior | msp         |    nan | 0.6374 ± 0.1318 | 0.9314 ± 0.0067 | 0.6104 ± 0.1196 | 0.9036 ± 0.0013 |            105 |               48 | False  |        6 |
| fruit12_apple        | resnet50  | cls       | P3_foreign         | energy      |      5 | 0.6657 ± 0.0653 | 0.9520 ± 0.0416 | 0.3763 ± 0.0715 | 0.5330 ± 0.1397 |            212 |              500 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_foreign         | energy      |    nan | 0.8730 ± 0.0000 | 0.8740 ± 0.0000 | 0.7689 ± 0.0000 | 0.8491 ± 0.0000 |            212 |              500 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_foreign         | knn         |      5 | 0.9235 ± 0.0816 | 0.3940 ± 0.5179 | 0.4926 ± 0.1164 | 0.5330 ± 0.1397 |            212 |              500 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_foreign         | knn         |    nan | 0.9791 ± 0.0000 | 0.0040 ± 0.0000 | 0.8438 ± 0.0000 | 0.8491 ± 0.0000 |            212 |              500 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_foreign         | mahalanobis |      5 | 0.9528 ± 0.0225 | 0.3240 ± 0.2962 | 0.5079 ± 0.1418 | 0.5330 ± 0.1397 |            212 |              500 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_foreign         | mahalanobis |    nan | 0.9762 ± 0.0000 | 0.0040 ± 0.0000 | 0.8409 ± 0.0000 | 0.8491 ± 0.0000 |            212 |              500 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_foreign         | msp         |      5 | 0.6666 ± 0.0749 | 0.9587 ± 0.0378 | 0.3929 ± 0.1256 | 0.5330 ± 0.1397 |            212 |              500 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_foreign         | msp         |    nan | 0.8632 ± 0.0000 | 0.8140 ± 0.0000 | 0.7657 ± 0.0000 | 0.8491 ± 0.0000 |            212 |              500 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_rotten          | energy      |      5 | 0.6215 ± 0.0490 | 0.8758 ± 0.0113 | 0.3192 ± 0.0780 | 0.4969 ± 0.0708 |            212 |               51 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_rotten          | energy      |    nan | 0.6438 ± 0.0000 | 0.9804 ± 0.0000 | 0.5793 ± 0.0000 | 0.8491 ± 0.0000 |            212 |               51 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_rotten          | knn         |      5 | 0.6599 ± 0.0080 | 0.8889 ± 0.0408 | 0.3308 ± 0.0619 | 0.4969 ± 0.0708 |            212 |               51 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_rotten          | knn         |    nan | 0.8189 ± 0.0000 | 0.8627 ± 0.0000 | 0.7134 ± 0.0000 | 0.8491 ± 0.0000 |            212 |               51 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_rotten          | mahalanobis |      5 | 0.7259 ± 0.0321 | 0.9085 ± 0.0113 | 0.3832 ± 0.0457 | 0.4969 ± 0.0708 |            212 |               51 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_rotten          | mahalanobis |    nan | 0.8343 ± 0.0000 | 0.7255 ± 0.0000 | 0.7235 ± 0.0000 | 0.8491 ± 0.0000 |            212 |               51 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_rotten          | msp         |      5 | 0.6334 ± 0.0372 | 0.9020 ± 0.0340 | 0.3296 ± 0.0455 | 0.4969 ± 0.0708 |            212 |               51 | False  |        3 |
| fruit12_apple        | resnet50  | cls       | P3_rotten          | msp         |    nan | 0.6465 ± 0.0000 | 0.9804 ± 0.0000 | 0.5871 ± 0.0000 | 0.8491 ± 0.0000 |            212 |               51 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P1_out_of_grade    | energy      |      5 | 0.6040 ± 0.0352 | 0.8815 ± 0.0898 | 0.5056 ± 0.0259 | 0.7662 ± 0.0392 |            790 |               45 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P1_out_of_grade    | energy      |    nan | 0.8562 ± 0.0000 | 0.6889 ± 0.0000 | 0.8374 ± 0.0000 | 0.9595 ± 0.0000 |            790 |               45 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P1_out_of_grade    | knn         |      5 | 0.7342 ± 0.0193 | 0.7333 ± 0.0000 | 0.5750 ± 0.0383 | 0.7662 ± 0.0392 |            790 |               45 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P1_out_of_grade    | knn         |    nan | 0.8321 ± 0.0000 | 0.5556 ± 0.0000 | 0.8083 ± 0.0000 | 0.9595 ± 0.0000 |            790 |               45 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.7617 ± 0.0078 | 0.7185 ± 0.0513 | 0.6021 ± 0.0549 | 0.7662 ± 0.0392 |            790 |               45 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.8649 ± 0.0000 | 0.4889 ± 0.0000 | 0.8393 ± 0.0000 | 0.9595 ± 0.0000 |            790 |               45 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P1_out_of_grade    | msp         |      5 | 0.6040 ± 0.0352 | 0.8815 ± 0.0898 | 0.5056 ± 0.0259 | 0.7662 ± 0.0392 |            790 |               45 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P1_out_of_grade    | msp         |    nan | 0.8562 ± 0.0000 | 0.6889 ± 0.0000 | 0.8374 ± 0.0000 | 0.9595 ± 0.0000 |            790 |               45 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P2_unseen_interior | energy      |      5 | 0.6362 ± 0.0571 | 0.8965 ± 0.0812 | 0.5364 ± 0.0930 | 0.7847 ± 0.1074 |            264 |              219 | False  |        6 |
| fruit12_banana       | dinov2_s  | cls       | P2_unseen_interior | energy      |    nan | 0.7866 ± 0.0647 | 0.8554 ± 0.0567 | 0.7798 ± 0.0644 | 0.9586 ± 0.0044 |            264 |              219 | False  |        6 |
| fruit12_banana       | dinov2_s  | cls       | P2_unseen_interior | knn         |      5 | 0.5372 ± 0.0385 | 0.9520 ± 0.0170 | 0.4695 ± 0.0670 | 0.7847 ± 0.1074 |            264 |              219 | False  |        6 |
| fruit12_banana       | dinov2_s  | cls       | P2_unseen_interior | knn         |    nan | 0.7259 ± 0.0255 | 0.8755 ± 0.0113 | 0.7060 ± 0.0227 | 0.9586 ± 0.0044 |            264 |              219 | False  |        6 |
| fruit12_banana       | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.5690 ± 0.0433 | 0.9420 ± 0.0305 | 0.4978 ± 0.0794 | 0.7847 ± 0.1074 |            264 |              219 | False  |        6 |
| fruit12_banana       | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.7128 ± 0.0129 | 0.9081 ± 0.0144 | 0.6935 ± 0.0103 | 0.9586 ± 0.0044 |            264 |              219 | False  |        6 |
| fruit12_banana       | dinov2_s  | cls       | P2_unseen_interior | msp         |      5 | 0.6362 ± 0.0571 | 0.8965 ± 0.0812 | 0.5364 ± 0.0930 | 0.7847 ± 0.1074 |            264 |              219 | False  |        6 |
| fruit12_banana       | dinov2_s  | cls       | P2_unseen_interior | msp         |    nan | 0.7866 ± 0.0647 | 0.8554 ± 0.0567 | 0.7798 ± 0.0644 | 0.9586 ± 0.0044 |            264 |              219 | False  |        6 |
| fruit12_banana       | dinov2_s  | cls       | P3_rotten          | energy      |      5 | 0.4468 ± 0.1610 | 0.9524 ± 0.0656 | 0.3186 ± 0.1493 | 0.6511 ± 0.1286 |            835 |               49 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P3_rotten          | energy      |    nan | 0.7663 ± 0.0000 | 0.7959 ± 0.0000 | 0.7453 ± 0.0000 | 0.9425 ± 0.0000 |            835 |               49 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P3_rotten          | knn         |      5 | 0.8093 ± 0.0172 | 0.6599 ± 0.0312 | 0.5556 ± 0.0963 | 0.6511 ± 0.1286 |            835 |               49 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P3_rotten          | knn         |    nan | 0.8753 ± 0.0000 | 0.5306 ± 0.0000 | 0.8365 ± 0.0000 | 0.9425 ± 0.0000 |            835 |               49 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P3_rotten          | mahalanobis |      5 | 0.8290 ± 0.0076 | 0.6939 ± 0.0000 | 0.5690 ± 0.1056 | 0.6511 ± 0.1286 |            835 |               49 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P3_rotten          | mahalanobis |    nan | 0.9022 ± 0.0000 | 0.4898 ± 0.0000 | 0.8617 ± 0.0000 | 0.9425 ± 0.0000 |            835 |               49 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P3_rotten          | msp         |      5 | 0.4390 ± 0.1504 | 0.9524 ± 0.0656 | 0.3196 ± 0.1467 | 0.6511 ± 0.1286 |            835 |               49 | False  |        3 |
| fruit12_banana       | dinov2_s  | cls       | P3_rotten          | msp         |    nan | 0.7550 ± 0.0000 | 0.7347 ± 0.0000 | 0.7349 ± 0.0000 | 0.9425 ± 0.0000 |            835 |               49 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P1_out_of_grade    | energy      |      5 | 0.5547 ± 0.0976 | 0.9407 ± 0.0679 | 0.3342 ± 0.0197 | 0.5713 ± 0.0354 |            790 |               45 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P1_out_of_grade    | energy      |    nan | 0.7733 ± 0.0000 | 0.7333 ± 0.0000 | 0.7509 ± 0.0000 | 0.9418 ± 0.0000 |            790 |               45 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P1_out_of_grade    | knn         |      5 | 0.7449 ± 0.0091 | 0.7185 ± 0.0128 | 0.4524 ± 0.0418 | 0.5713 ± 0.0354 |            790 |               45 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P1_out_of_grade    | knn         |    nan | 0.8629 ± 0.0000 | 0.6222 ± 0.0000 | 0.8196 ± 0.0000 | 0.9418 ± 0.0000 |            790 |               45 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.7866 ± 0.0314 | 0.7111 ± 0.0222 | 0.4693 ± 0.0532 | 0.5713 ± 0.0354 |            790 |               45 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.8770 ± 0.0000 | 0.5778 ± 0.0000 | 0.8343 ± 0.0000 | 0.9418 ± 0.0000 |            790 |               45 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P1_out_of_grade    | msp         |      5 | 0.5547 ± 0.0976 | 0.9407 ± 0.0679 | 0.3342 ± 0.0197 | 0.5713 ± 0.0354 |            790 |               45 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P1_out_of_grade    | msp         |    nan | 0.7733 ± 0.0000 | 0.7333 ± 0.0000 | 0.7509 ± 0.0000 | 0.9418 ± 0.0000 |            790 |               45 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P2_unseen_interior | energy      |      5 | 0.5356 ± 0.0957 | 0.9159 ± 0.0336 | 0.4019 ± 0.1448 | 0.7023 ± 0.1937 |            264 |              219 | False  |        6 |
| fruit12_banana       | resnet50  | cls       | P2_unseen_interior | energy      |    nan | 0.7145 ± 0.0879 | 0.9031 ± 0.0390 | 0.7037 ± 0.0893 | 0.9380 ± 0.0234 |            264 |              219 | False  |        6 |
| fruit12_banana       | resnet50  | cls       | P2_unseen_interior | knn         |      5 | 0.5285 ± 0.0659 | 0.9605 ± 0.0149 | 0.4156 ± 0.1029 | 0.7023 ± 0.1937 |            264 |              219 | False  |        6 |
| fruit12_banana       | resnet50  | cls       | P2_unseen_interior | knn         |    nan | 0.6983 ± 0.0196 | 0.8533 ± 0.0494 | 0.6653 ± 0.0062 | 0.9380 ± 0.0234 |            264 |              219 | False  |        6 |
| fruit12_banana       | resnet50  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.5262 ± 0.0598 | 0.9522 ± 0.0255 | 0.4300 ± 0.1014 | 0.7023 ± 0.1937 |            264 |              219 | False  |        6 |
| fruit12_banana       | resnet50  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.7082 ± 0.0164 | 0.8654 ± 0.0477 | 0.6757 ± 0.0020 | 0.9380 ± 0.0234 |            264 |              219 | False  |        6 |
| fruit12_banana       | resnet50  | cls       | P2_unseen_interior | msp         |      5 | 0.5356 ± 0.0957 | 0.9159 ± 0.0336 | 0.4019 ± 0.1448 | 0.7023 ± 0.1937 |            264 |              219 | False  |        6 |
| fruit12_banana       | resnet50  | cls       | P2_unseen_interior | msp         |    nan | 0.7145 ± 0.0879 | 0.9031 ± 0.0390 | 0.7037 ± 0.0893 | 0.9380 ± 0.0234 |            264 |              219 | False  |        6 |
| fruit12_banana       | resnet50  | cls       | P3_rotten          | energy      |      5 | 0.5033 ± 0.1051 | 0.9320 ± 0.0118 | 0.2974 ± 0.0410 | 0.5345 ± 0.0304 |            835 |               49 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P3_rotten          | energy      |    nan | 0.8003 ± 0.0000 | 0.6327 ± 0.0000 | 0.7684 ± 0.0000 | 0.9269 ± 0.0000 |            835 |               49 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P3_rotten          | knn         |      5 | 0.8934 ± 0.0178 | 0.4218 ± 0.1047 | 0.4878 ± 0.0369 | 0.5345 ± 0.0304 |            835 |               49 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P3_rotten          | knn         |    nan | 0.9041 ± 0.0000 | 0.4082 ± 0.0000 | 0.8436 ± 0.0000 | 0.9269 ± 0.0000 |            835 |               49 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P3_rotten          | mahalanobis |      5 | 0.8912 ± 0.0144 | 0.4082 ± 0.1060 | 0.4877 ± 0.0382 | 0.5345 ± 0.0304 |            835 |               49 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P3_rotten          | mahalanobis |    nan | 0.9299 ± 0.0000 | 0.4082 ± 0.0000 | 0.8670 ± 0.0000 | 0.9269 ± 0.0000 |            835 |               49 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P3_rotten          | msp         |      5 | 0.4470 ± 0.0976 | 0.9456 ± 0.0118 | 0.2706 ± 0.0507 | 0.5345 ± 0.0304 |            835 |               49 | False  |        3 |
| fruit12_banana       | resnet50  | cls       | P3_rotten          | msp         |    nan | 0.7504 ± 0.0000 | 0.8163 ± 0.0000 | 0.7251 ± 0.0000 | 0.9269 ± 0.0000 |            835 |               49 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P1_out_of_grade    | energy      |      5 | 0.4994 ± 0.0292 | 0.9535 ± 0.0233 | 0.3661 ± 0.0557 | 0.6386 ± 0.0219 |             95 |               43 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P1_out_of_grade    | energy      |    nan | 0.7023 ± 0.0000 | 0.8140 ± 0.0000 | 0.6433 ± 0.0000 | 0.8737 ± 0.0000 |             95 |               43 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P1_out_of_grade    | knn         |      5 | 0.8248 ± 0.0830 | 0.9070 ± 0.1611 | 0.5421 ± 0.0481 | 0.6386 ± 0.0219 |             95 |               43 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P1_out_of_grade    | knn         |    nan | 0.9067 ± 0.0000 | 0.4884 ± 0.0000 | 0.7905 ± 0.0000 | 0.8737 ± 0.0000 |             95 |               43 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.8623 ± 0.0792 | 0.7829 ± 0.3560 | 0.5647 ± 0.0291 | 0.6386 ± 0.0219 |             95 |               43 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.9422 ± 0.0000 | 0.4651 ± 0.0000 | 0.8296 ± 0.0000 | 0.8737 ± 0.0000 |             95 |               43 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P1_out_of_grade    | msp         |      5 | 0.4994 ± 0.0292 | 0.9535 ± 0.0233 | 0.3661 ± 0.0557 | 0.6386 ± 0.0219 |             95 |               43 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P1_out_of_grade    | msp         |    nan | 0.7023 ± 0.0000 | 0.8140 ± 0.0000 | 0.6433 ± 0.0000 | 0.8737 ± 0.0000 |             95 |               43 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P2_unseen_interior | energy      |      5 | 0.6200 ± 0.1207 | 0.9581 ± 0.0294 | 0.6003 ± 0.1153 | 0.9189 ± 0.0309 |             88 |               45 | False  |        6 |
| fruit12_mango        | dinov2_s  | cls       | P2_unseen_interior | energy      |    nan | 0.6825 ± 0.1274 | 0.8756 ± 0.0389 | 0.6760 ± 0.1230 | 0.9725 ± 0.0052 |             88 |               45 | False  |        6 |
| fruit12_mango        | dinov2_s  | cls       | P2_unseen_interior | knn         |      5 | 0.5747 ± 0.0931 | 0.8593 ± 0.1569 | 0.5491 ± 0.0745 | 0.9189 ± 0.0309 |             88 |               45 | False  |        6 |
| fruit12_mango        | dinov2_s  | cls       | P2_unseen_interior | knn         |    nan | 0.6219 ± 0.0733 | 0.9000 ± 0.1095 | 0.6146 ± 0.0715 | 0.9725 ± 0.0052 |             88 |               45 | False  |        6 |
| fruit12_mango        | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.5926 ± 0.0787 | 0.8778 ± 0.1661 | 0.5723 ± 0.0688 | 0.9189 ± 0.0309 |             88 |               45 | False  |        6 |
| fruit12_mango        | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.6522 ± 0.0758 | 0.9111 ± 0.0974 | 0.6432 ± 0.0723 | 0.9725 ± 0.0052 |             88 |               45 | False  |        6 |
| fruit12_mango        | dinov2_s  | cls       | P2_unseen_interior | msp         |      5 | 0.6200 ± 0.1207 | 0.9581 ± 0.0294 | 0.6003 ± 0.1153 | 0.9189 ± 0.0309 |             88 |               45 | False  |        6 |
| fruit12_mango        | dinov2_s  | cls       | P2_unseen_interior | msp         |    nan | 0.6825 ± 0.1274 | 0.8756 ± 0.0389 | 0.6760 ± 0.1230 | 0.9725 ± 0.0052 |             88 |               45 | False  |        6 |
| fruit12_mango        | dinov2_s  | cls       | P3_rotten          | energy      |      5 | 0.3543 ± 0.0695 | 0.9667 ± 0.0577 | 0.2895 ± 0.0426 | 0.7053 ± 0.0151 |            138 |               30 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P3_rotten          | energy      |    nan | 0.4070 ± 0.0000 | 0.9333 ± 0.0000 | 0.3908 ± 0.0000 | 0.9058 ± 0.0000 |            138 |               30 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P3_rotten          | knn         |      5 | 0.5593 ± 0.0173 | 0.9333 ± 0.0882 | 0.4079 ± 0.0068 | 0.7053 ± 0.0151 |            138 |               30 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P3_rotten          | knn         |    nan | 0.5865 ± 0.0000 | 0.8667 ± 0.0000 | 0.5362 ± 0.0000 | 0.9058 ± 0.0000 |            138 |               30 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P3_rotten          | mahalanobis |      5 | 0.5421 ± 0.0304 | 0.8889 ± 0.1388 | 0.4039 ± 0.0185 | 0.7053 ± 0.0151 |            138 |               30 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P3_rotten          | mahalanobis |    nan | 0.5886 ± 0.0000 | 0.9000 ± 0.0000 | 0.5457 ± 0.0000 | 0.9058 ± 0.0000 |            138 |               30 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P3_rotten          | msp         |      5 | 0.3238 ± 0.0370 | 0.9778 ± 0.0385 | 0.2711 ± 0.0282 | 0.7053 ± 0.0151 |            138 |               30 | False  |        3 |
| fruit12_mango        | dinov2_s  | cls       | P3_rotten          | msp         |    nan | 0.3843 ± 0.0000 | 0.9333 ± 0.0000 | 0.3684 ± 0.0000 | 0.9058 ± 0.0000 |            138 |               30 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P1_out_of_grade    | energy      |      5 | 0.5825 ± 0.1336 | 0.9767 ± 0.0233 | 0.4678 ± 0.1266 | 0.7404 ± 0.0580 |             95 |               43 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P1_out_of_grade    | energy      |    nan | 0.7520 ± 0.0000 | 0.8372 ± 0.0000 | 0.7244 ± 0.0000 | 0.9263 ± 0.0000 |             95 |               43 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P1_out_of_grade    | knn         |      5 | 0.7755 ± 0.0910 | 0.7132 ± 0.1363 | 0.5834 ± 0.0546 | 0.7404 ± 0.0580 |             95 |               43 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P1_out_of_grade    | knn         |    nan | 0.8778 ± 0.0000 | 0.6279 ± 0.0000 | 0.8203 ± 0.0000 | 0.9263 ± 0.0000 |             95 |               43 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.8012 ± 0.0268 | 0.7364 ± 0.1548 | 0.6156 ± 0.0306 | 0.7404 ± 0.0580 |             95 |               43 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.8825 ± 0.0000 | 0.6977 ± 0.0000 | 0.8259 ± 0.0000 | 0.9263 ± 0.0000 |             95 |               43 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P1_out_of_grade    | msp         |      5 | 0.5825 ± 0.1336 | 0.9767 ± 0.0233 | 0.4678 ± 0.1266 | 0.7404 ± 0.0580 |             95 |               43 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P1_out_of_grade    | msp         |    nan | 0.7520 ± 0.0000 | 0.8372 ± 0.0000 | 0.7244 ± 0.0000 | 0.9263 ± 0.0000 |             95 |               43 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P2_unseen_interior | energy      |      5 | 0.6531 ± 0.1193 | 0.8974 ± 0.1153 | 0.5743 ± 0.0700 | 0.8091 ± 0.0605 |             88 |               45 | False  |        6 |
| fruit12_mango        | resnet50  | cls       | P2_unseen_interior | energy      |    nan | 0.7221 ± 0.0303 | 0.8578 ± 0.1071 | 0.7039 ± 0.0222 | 0.9223 ± 0.0145 |             88 |               45 | False  |        6 |
| fruit12_mango        | resnet50  | cls       | P2_unseen_interior | knn         |      5 | 0.6798 ± 0.0708 | 0.8337 ± 0.1464 | 0.5631 ± 0.0552 | 0.8091 ± 0.0605 |             88 |               45 | False  |        6 |
| fruit12_mango        | resnet50  | cls       | P2_unseen_interior | knn         |    nan | 0.7538 ± 0.1003 | 0.6933 ± 0.2483 | 0.7157 ± 0.0899 | 0.9223 ± 0.0145 |             88 |               45 | False  |        6 |
| fruit12_mango        | resnet50  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.7492 ± 0.1087 | 0.8052 ± 0.2105 | 0.6243 ± 0.0577 | 0.8091 ± 0.0605 |             88 |               45 | False  |        6 |
| fruit12_mango        | resnet50  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.7812 ± 0.0850 | 0.7578 ± 0.2215 | 0.7431 ± 0.0736 | 0.9223 ± 0.0145 |             88 |               45 | False  |        6 |
| fruit12_mango        | resnet50  | cls       | P2_unseen_interior | msp         |      5 | 0.6531 ± 0.1193 | 0.8974 ± 0.1153 | 0.5743 ± 0.0700 | 0.8091 ± 0.0605 |             88 |               45 | False  |        6 |
| fruit12_mango        | resnet50  | cls       | P2_unseen_interior | msp         |    nan | 0.7221 ± 0.0303 | 0.8578 ± 0.1071 | 0.7039 ± 0.0222 | 0.9223 ± 0.0145 |             88 |               45 | False  |        6 |
| fruit12_mango        | resnet50  | cls       | P3_rotten          | energy      |      5 | 0.3700 ± 0.0782 | 0.9667 ± 0.0577 | 0.3009 ± 0.0651 | 0.6932 ± 0.0865 |            138 |               30 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P3_rotten          | energy      |    nan | 0.4041 ± 0.0000 | 0.9667 ± 0.0000 | 0.3853 ± 0.0000 | 0.8841 ± 0.0000 |            138 |               30 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P3_rotten          | knn         |      5 | 0.5329 ± 0.0655 | 0.9222 ± 0.0385 | 0.3809 ± 0.0343 | 0.6932 ± 0.0865 |            138 |               30 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P3_rotten          | knn         |    nan | 0.5546 ± 0.0000 | 0.9333 ± 0.0000 | 0.5157 ± 0.0000 | 0.8841 ± 0.0000 |            138 |               30 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P3_rotten          | mahalanobis |      5 | 0.5626 ± 0.0440 | 0.9222 ± 0.0385 | 0.4247 ± 0.0366 | 0.6932 ± 0.0865 |            138 |               30 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P3_rotten          | mahalanobis |    nan | 0.6046 ± 0.0000 | 0.9667 ± 0.0000 | 0.5616 ± 0.0000 | 0.8841 ± 0.0000 |            138 |               30 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P3_rotten          | msp         |      5 | 0.3706 ± 0.0564 | 0.9667 ± 0.0577 | 0.3005 ± 0.0508 | 0.6932 ± 0.0865 |            138 |               30 | False  |        3 |
| fruit12_mango        | resnet50  | cls       | P3_rotten          | msp         |    nan | 0.4082 ± 0.0000 | 0.9667 ± 0.0000 | 0.3915 ± 0.0000 | 0.8841 ± 0.0000 |            138 |               30 | False  |        3 |
| fruit12_x_apple      | dinov2_s  | cls       | P2c_unseen_species | energy      |      5 | 0.6230 ± 0.1495 | 0.9151 ± 0.1103 | 0.4157 ± 0.1780 | 0.5810 ± 0.1530 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | dinov2_s  | cls       | P2c_unseen_species | energy      |    nan | 0.6771 ± 0.0000 | 0.8774 ± 0.0000 | 0.6543 ± 0.0000 | 0.9250 ± 0.0000 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | dinov2_s  | cls       | P2c_unseen_species | knn         |      5 | 0.9463 ± 0.0094 | 0.2736 ± 0.0779 | 0.5569 ± 0.1636 | 0.5810 ± 0.1530 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | dinov2_s  | cls       | P2c_unseen_species | knn         |    nan | 0.9678 ± 0.0000 | 0.2170 ± 0.0000 | 0.9009 ± 0.0000 | 0.9250 ± 0.0000 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | dinov2_s  | cls       | P2c_unseen_species | mahalanobis |      5 | 0.9325 ± 0.0093 | 0.3553 ± 0.0530 | 0.5518 ± 0.1602 | 0.5810 ± 0.1530 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | dinov2_s  | cls       | P2c_unseen_species | mahalanobis |    nan | 0.9555 ± 0.0000 | 0.2594 ± 0.0000 | 0.8916 ± 0.0000 | 0.9250 ± 0.0000 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | dinov2_s  | cls       | P2c_unseen_species | msp         |      5 | 0.6128 ± 0.1328 | 0.9214 ± 0.0831 | 0.4135 ± 0.1766 | 0.5810 ± 0.1530 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | dinov2_s  | cls       | P2c_unseen_species | msp         |    nan | 0.6661 ± 0.0000 | 0.9009 ± 0.0000 | 0.6468 ± 0.0000 | 0.9250 ± 0.0000 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | resnet50  | cls       | P2c_unseen_species | energy      |      5 | 0.6575 ± 0.0541 | 0.9104 ± 0.0822 | 0.3481 ± 0.0931 | 0.4916 ± 0.0841 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | resnet50  | cls       | P2c_unseen_species | energy      |    nan | 0.7561 ± 0.0000 | 0.8396 ± 0.0000 | 0.7253 ± 0.0000 | 0.9096 ± 0.0000 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | resnet50  | cls       | P2c_unseen_species | knn         |      5 | 0.8256 ± 0.0424 | 0.5582 ± 0.2112 | 0.4071 ± 0.0787 | 0.4916 ± 0.0841 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | resnet50  | cls       | P2c_unseen_species | knn         |    nan | 0.8610 ± 0.0000 | 0.6745 ± 0.0000 | 0.7920 ± 0.0000 | 0.9096 ± 0.0000 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | resnet50  | cls       | P2c_unseen_species | mahalanobis |      5 | 0.8002 ± 0.0432 | 0.7091 ± 0.2478 | 0.4139 ± 0.0832 | 0.4916 ± 0.0841 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | resnet50  | cls       | P2c_unseen_species | mahalanobis |    nan | 0.9079 ± 0.0000 | 0.6132 ± 0.0000 | 0.8333 ± 0.0000 | 0.9096 ± 0.0000 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | resnet50  | cls       | P2c_unseen_species | msp         |      5 | 0.5822 ± 0.1278 | 0.9182 ± 0.0806 | 0.3270 ± 0.1159 | 0.4916 ± 0.0841 |            973 |              212 | False  |        3 |
| fruit12_x_apple      | resnet50  | cls       | P2c_unseen_species | msp         |    nan | 0.7501 ± 0.0000 | 0.8208 ± 0.0000 | 0.7188 ± 0.0000 | 0.9096 ± 0.0000 |            973 |              212 | False  |        3 |
| fruit12_x_banana     | dinov2_s  | cls       | P2c_unseen_species | energy      |      5 | 0.6839 ± 0.0896 | 0.8918 ± 0.0802 | 0.4232 ± 0.0258 | 0.5590 ± 0.0875 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | dinov2_s  | cls       | P2c_unseen_species | energy      |    nan | 0.6897 ± 0.0000 | 0.8874 ± 0.0000 | 0.6248 ± 0.0000 | 0.8400 ± 0.0000 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | dinov2_s  | cls       | P2c_unseen_species | knn         |      5 | 0.9383 ± 0.0157 | 0.4188 ± 0.1396 | 0.5303 ± 0.0714 | 0.5590 ± 0.0875 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | dinov2_s  | cls       | P2c_unseen_species | knn         |    nan | 0.9768 ± 0.0000 | 0.1054 ± 0.0000 | 0.8195 ± 0.0000 | 0.8400 ± 0.0000 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | dinov2_s  | cls       | P2c_unseen_species | mahalanobis |      5 | 0.9480 ± 0.0094 | 0.3054 ± 0.1183 | 0.5366 ± 0.0775 | 0.5590 ± 0.0875 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | dinov2_s  | cls       | P2c_unseen_species | mahalanobis |    nan | 0.9688 ± 0.0000 | 0.2287 ± 0.0000 | 0.8126 ± 0.0000 | 0.8400 ± 0.0000 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | dinov2_s  | cls       | P2c_unseen_species | msp         |      5 | 0.6745 ± 0.0521 | 0.9050 ± 0.0668 | 0.4177 ± 0.0365 | 0.5590 ± 0.0875 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | dinov2_s  | cls       | P2c_unseen_species | msp         |    nan | 0.6714 ± 0.0000 | 0.8551 ± 0.0000 | 0.6093 ± 0.0000 | 0.8400 ± 0.0000 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | resnet50  | cls       | P2c_unseen_species | energy      |      5 | 0.6398 ± 0.0512 | 0.8890 ± 0.0546 | 0.3793 ± 0.0509 | 0.5486 ± 0.0721 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | resnet50  | cls       | P2c_unseen_species | energy      |    nan | 0.7465 ± 0.0000 | 0.8994 ± 0.0000 | 0.6714 ± 0.0000 | 0.8400 ± 0.0000 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | resnet50  | cls       | P2c_unseen_species | knn         |      5 | 0.8395 ± 0.0707 | 0.5154 ± 0.0778 | 0.4594 ± 0.0178 | 0.5486 ± 0.0721 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | resnet50  | cls       | P2c_unseen_species | knn         |    nan | 0.9154 ± 0.0000 | 0.4156 ± 0.0000 | 0.7755 ± 0.0000 | 0.8400 ± 0.0000 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | resnet50  | cls       | P2c_unseen_species | mahalanobis |      5 | 0.8655 ± 0.0460 | 0.4727 ± 0.0758 | 0.4832 ± 0.0437 | 0.5486 ± 0.0721 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | resnet50  | cls       | P2c_unseen_species | mahalanobis |    nan | 0.9137 ± 0.0000 | 0.4275 ± 0.0000 | 0.7746 ± 0.0000 | 0.8400 ± 0.0000 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | resnet50  | cls       | P2c_unseen_species | msp         |      5 | 0.6227 ± 0.0365 | 0.9082 ± 0.0460 | 0.3777 ± 0.0514 | 0.5486 ± 0.0721 |            350 |              835 | False  |        3 |
| fruit12_x_banana     | resnet50  | cls       | P2c_unseen_species | msp         |    nan | 0.7511 ± 0.0000 | 0.9257 ± 0.0000 | 0.6816 ± 0.0000 | 0.8400 ± 0.0000 |            350 |              835 | False  |        3 |
| fruit12_x_mango      | dinov2_s  | cls       | P2c_unseen_species | energy      |      5 | 0.5310 ± 0.1489 | 0.9130 ± 0.0145 | 0.3325 ± 0.1064 | 0.5769 ± 0.0740 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | dinov2_s  | cls       | P2c_unseen_species | energy      |    nan | 0.7982 ± 0.0000 | 0.8478 ± 0.0000 | 0.7678 ± 0.0000 | 0.9255 ± 0.0000 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | dinov2_s  | cls       | P2c_unseen_species | knn         |      5 | 0.8527 ± 0.0152 | 0.8647 ± 0.0625 | 0.5284 ± 0.0844 | 0.5769 ± 0.0740 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | dinov2_s  | cls       | P2c_unseen_species | knn         |    nan | 0.9577 ± 0.0000 | 0.2681 ± 0.0000 | 0.8939 ± 0.0000 | 0.9255 ± 0.0000 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | dinov2_s  | cls       | P2c_unseen_species | mahalanobis |      5 | 0.8118 ± 0.0178 | 0.9034 ± 0.0493 | 0.5112 ± 0.0867 | 0.5769 ± 0.0740 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | dinov2_s  | cls       | P2c_unseen_species | mahalanobis |    nan | 0.8790 ± 0.0000 | 0.8333 ± 0.0000 | 0.8321 ± 0.0000 | 0.9255 ± 0.0000 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | dinov2_s  | cls       | P2c_unseen_species | msp         |      5 | 0.5001 ± 0.1225 | 0.9227 ± 0.0182 | 0.3127 ± 0.0816 | 0.5769 ± 0.0740 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | dinov2_s  | cls       | P2c_unseen_species | msp         |    nan | 0.7811 ± 0.0000 | 0.8406 ± 0.0000 | 0.7541 ± 0.0000 | 0.9255 ± 0.0000 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | resnet50  | cls       | P2c_unseen_species | energy      |      5 | 0.4914 ± 0.1290 | 0.9517 ± 0.0233 | 0.2745 ± 0.0684 | 0.5030 ± 0.0405 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | resnet50  | cls       | P2c_unseen_species | energy      |    nan | 0.7070 ± 0.0000 | 0.8841 ± 0.0000 | 0.6733 ± 0.0000 | 0.8978 ± 0.0000 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | resnet50  | cls       | P2c_unseen_species | knn         |      5 | 0.7919 ± 0.0198 | 0.8744 ± 0.0233 | 0.4091 ± 0.0485 | 0.5030 ± 0.0405 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | resnet50  | cls       | P2c_unseen_species | knn         |    nan | 0.8903 ± 0.0000 | 0.4638 ± 0.0000 | 0.8061 ± 0.0000 | 0.8978 ± 0.0000 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | resnet50  | cls       | P2c_unseen_species | mahalanobis |      5 | 0.7751 ± 0.0165 | 0.8792 ± 0.0274 | 0.4064 ± 0.0217 | 0.5030 ± 0.0405 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | resnet50  | cls       | P2c_unseen_species | mahalanobis |    nan | 0.8594 ± 0.0000 | 0.6594 ± 0.0000 | 0.7837 ± 0.0000 | 0.8978 ± 0.0000 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | resnet50  | cls       | P2c_unseen_species | msp         |      5 | 0.4743 ± 0.1155 | 0.9444 ± 0.0293 | 0.2662 ± 0.0683 | 0.5030 ± 0.0405 |           1047 |              138 | False  |        3 |
| fruit12_x_mango      | resnet50  | cls       | P2c_unseen_species | msp         |    nan | 0.6932 ± 0.0000 | 0.8841 ± 0.0000 | 0.6635 ± 0.0000 | 0.8978 ± 0.0000 |           1047 |              138 | False  |        3 |
| fruits360_x_apple    | dinov2_s  | cls       | P2_leave_one_fruit | energy      |      5 | 0.9213 ± 0.0044 | 0.4511 ± 0.0139 | 0.7148 ± 0.0117 | 0.7634 ± 0.0153 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | dinov2_s  | cls       | P2_leave_one_fruit | energy      |    nan | 0.9779 ± 0.0000 | 0.1017 ± 0.0000 | 0.8819 ± 0.0000 | 0.9001 ± 0.0000 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | dinov2_s  | cls       | P2_leave_one_fruit | knn         |      5 | 0.9500 ± 0.0060 | 0.2845 ± 0.0542 | 0.7334 ± 0.0090 | 0.7634 ± 0.0153 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | dinov2_s  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9978 ± 0.0000 | 0.0069 ± 0.0000 | 0.8984 ± 0.0000 | 0.9001 ± 0.0000 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9596 ± 0.0024 | 0.2517 ± 0.0301 | 0.7424 ± 0.0152 | 0.7634 ± 0.0153 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9910 ± 0.0000 | 0.0172 ± 0.0000 | 0.8918 ± 0.0000 | 0.9001 ± 0.0000 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | dinov2_s  | cls       | P2_leave_one_fruit | msp         |      5 | 0.9482 ± 0.0024 | 0.3063 ± 0.0163 | 0.7359 ± 0.0130 | 0.7634 ± 0.0153 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | dinov2_s  | cls       | P2_leave_one_fruit | msp         |    nan | 0.9735 ± 0.0000 | 0.1086 ± 0.0000 | 0.8791 ± 0.0000 | 0.9001 ± 0.0000 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | resnet50  | cls       | P2_leave_one_fruit | energy      |      5 | 0.8712 ± 0.0107 | 0.4615 ± 0.0296 | 0.6273 ± 0.0086 | 0.7010 ± 0.0067 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | resnet50  | cls       | P2_leave_one_fruit | energy      |    nan | 0.9717 ± 0.0000 | 0.1448 ± 0.0000 | 0.8475 ± 0.0000 | 0.8697 ± 0.0000 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | resnet50  | cls       | P2_leave_one_fruit | knn         |      5 | 0.8674 ± 0.0036 | 0.6195 ± 0.0155 | 0.6390 ± 0.0038 | 0.7010 ± 0.0067 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | resnet50  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9906 ± 0.0000 | 0.0362 ± 0.0000 | 0.8625 ± 0.0000 | 0.8697 ± 0.0000 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9090 ± 0.0052 | 0.5770 ± 0.0127 | 0.6628 ± 0.0013 | 0.7010 ± 0.0067 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9666 ± 0.0000 | 0.2155 ± 0.0000 | 0.8433 ± 0.0000 | 0.8697 ± 0.0000 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | resnet50  | cls       | P2_leave_one_fruit | msp         |      5 | 0.8899 ± 0.0162 | 0.4690 ± 0.0398 | 0.6367 ± 0.0062 | 0.7010 ± 0.0067 |           1351 |              580 | False  |        3 |
| fruits360_x_apple    | resnet50  | cls       | P2_leave_one_fruit | msp         |    nan | 0.9758 ± 0.0000 | 0.1190 ± 0.0000 | 0.8547 ± 0.0000 | 0.8697 ± 0.0000 |           1351 |              580 | False  |        3 |
| fruits360_x_cucumber | dinov2_s  | cls       | P2_leave_one_fruit | energy      |      5 | 0.9500 ± 0.0049 | 0.3189 ± 0.0560 | 0.7350 ± 0.0039 | 0.7740 ± 0.0046 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | dinov2_s  | cls       | P2_leave_one_fruit | energy      |    nan | 0.9944 ± 0.0000 | 0.0033 ± 0.0000 | 0.9157 ± 0.0000 | 0.9209 ± 0.0000 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | dinov2_s  | cls       | P2_leave_one_fruit | knn         |      5 | 0.9990 ± 0.0001 | 0.0000 ± 0.0000 | 0.7730 ± 0.0046 | 0.7740 ± 0.0046 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | dinov2_s  | cls       | P2_leave_one_fruit | knn         |    nan | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.9209 ± 0.0000 | 0.9209 ± 0.0000 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9990 ± 0.0004 | 0.0000 ± 0.0000 | 0.7730 ± 0.0050 | 0.7740 ± 0.0046 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9999 ± 0.0000 | 0.0000 ± 0.0000 | 0.9208 ± 0.0000 | 0.9209 ± 0.0000 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | dinov2_s  | cls       | P2_leave_one_fruit | msp         |      5 | 0.8663 ± 0.0166 | 0.6889 ± 0.0684 | 0.6899 ± 0.0107 | 0.7740 ± 0.0046 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | dinov2_s  | cls       | P2_leave_one_fruit | msp         |    nan | 0.9942 ± 0.0000 | 0.0200 ± 0.0000 | 0.9159 ± 0.0000 | 0.9209 ± 0.0000 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | resnet50  | cls       | P2_leave_one_fruit | energy      |      5 | 0.8223 ± 0.0088 | 0.7144 ± 0.0126 | 0.5986 ± 0.0028 | 0.7108 ± 0.0060 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | resnet50  | cls       | P2_leave_one_fruit | energy      |    nan | 0.9786 ± 0.0000 | 0.1167 ± 0.0000 | 0.8684 ± 0.0000 | 0.8860 ± 0.0000 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | resnet50  | cls       | P2_leave_one_fruit | knn         |      5 | 0.9921 ± 0.0006 | 0.0467 ± 0.0058 | 0.7058 ± 0.0061 | 0.7108 ± 0.0060 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | resnet50  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9999 ± 0.0000 | 0.0000 ± 0.0000 | 0.8858 ± 0.0000 | 0.8860 ± 0.0000 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9949 ± 0.0004 | 0.0300 ± 0.0000 | 0.7077 ± 0.0056 | 0.7108 ± 0.0060 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9986 ± 0.0000 | 0.0067 ± 0.0000 | 0.8847 ± 0.0000 | 0.8860 ± 0.0000 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | resnet50  | cls       | P2_leave_one_fruit | msp         |      5 | 0.7587 ± 0.0119 | 0.8011 ± 0.0195 | 0.5703 ± 0.0129 | 0.7108 ± 0.0060 |           1631 |              300 | False  |        3 |
| fruits360_x_cucumber | resnet50  | cls       | P2_leave_one_fruit | msp         |    nan | 0.9813 ± 0.0000 | 0.1067 ± 0.0000 | 0.8731 ± 0.0000 | 0.8860 ± 0.0000 |           1631 |              300 | False  |        3 |
| fruits360_x_orange   | dinov2_s  | cls       | P2_leave_one_fruit | energy      |      5 | 0.9162 ± 0.0065 | 0.5333 ± 0.0657 | 0.7084 ± 0.0139 | 0.7719 ± 0.0149 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | dinov2_s  | cls       | P2_leave_one_fruit | energy      |    nan | 0.9308 ± 0.0000 | 0.5067 ± 0.0000 | 0.8567 ± 0.0000 | 0.9214 ± 0.0000 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | dinov2_s  | cls       | P2_leave_one_fruit | knn         |      5 | 0.9857 ± 0.0057 | 0.0400 ± 0.0636 | 0.7620 ± 0.0122 | 0.7719 ± 0.0149 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | dinov2_s  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9998 ± 0.0000 | 0.0000 ± 0.0000 | 0.9214 ± 0.0000 | 0.9214 ± 0.0000 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9836 ± 0.0030 | 0.0178 ± 0.0102 | 0.7621 ± 0.0141 | 0.7719 ± 0.0149 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9948 ± 0.0000 | 0.0000 ± 0.0000 | 0.9167 ± 0.0000 | 0.9214 ± 0.0000 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | dinov2_s  | cls       | P2_leave_one_fruit | msp         |      5 | 0.8096 ± 0.0403 | 0.8511 ± 0.1136 | 0.6438 ± 0.0170 | 0.7719 ± 0.0149 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | dinov2_s  | cls       | P2_leave_one_fruit | msp         |    nan | 0.9694 ± 0.0000 | 0.1667 ± 0.0000 | 0.8963 ± 0.0000 | 0.9214 ± 0.0000 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | resnet50  | cls       | P2_leave_one_fruit | energy      |      5 | 0.7881 ± 0.0181 | 0.7111 ± 0.0509 | 0.5576 ± 0.0035 | 0.6829 ± 0.0163 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | resnet50  | cls       | P2_leave_one_fruit | energy      |    nan | 0.8990 ± 0.0000 | 0.5000 ± 0.0000 | 0.7985 ± 0.0000 | 0.8838 ± 0.0000 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | resnet50  | cls       | P2_leave_one_fruit | knn         |      5 | 0.7306 ± 0.0067 | 0.8000 ± 0.0346 | 0.5284 ± 0.0082 | 0.6829 ± 0.0163 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | resnet50  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9804 ± 0.0000 | 0.1133 ± 0.0000 | 0.8683 ± 0.0000 | 0.8838 ± 0.0000 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.8625 ± 0.0131 | 0.6978 ± 0.0491 | 0.6094 ± 0.0122 | 0.6829 ± 0.0163 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9224 ± 0.0000 | 0.3933 ± 0.0000 | 0.8168 ± 0.0000 | 0.8838 ± 0.0000 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | resnet50  | cls       | P2_leave_one_fruit | msp         |      5 | 0.8057 ± 0.0229 | 0.7400 ± 0.0416 | 0.5746 ± 0.0115 | 0.6829 ± 0.0163 |           1781 |              150 | False  |        3 |
| fruits360_x_orange   | resnet50  | cls       | P2_leave_one_fruit | msp         |    nan | 0.9323 ± 0.0000 | 0.4800 ± 0.0000 | 0.8338 ± 0.0000 | 0.8838 ± 0.0000 |           1781 |              150 | False  |        3 |
| fruits360_x_pear     | dinov2_s  | cls       | P2_leave_one_fruit | energy      |      5 | 0.9093 ± 0.0042 | 0.4974 ± 0.0323 | 0.7646 ± 0.0027 | 0.8340 ± 0.0028 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | dinov2_s  | cls       | P2_leave_one_fruit | energy      |    nan | 0.9773 ± 0.0000 | 0.1397 ± 0.0000 | 0.9705 ± 0.0000 | 0.9905 ± 0.0000 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | dinov2_s  | cls       | P2_leave_one_fruit | knn         |      5 | 0.9530 ± 0.0043 | 0.2875 ± 0.0415 | 0.8000 ± 0.0051 | 0.8340 ± 0.0028 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | dinov2_s  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9988 ± 0.0000 | 0.0000 ± 0.0000 | 0.9899 ± 0.0000 | 0.9905 ± 0.0000 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9594 ± 0.0046 | 0.2986 ± 0.0419 | 0.8094 ± 0.0044 | 0.8340 ± 0.0028 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9836 ± 0.0000 | 0.0776 ± 0.0000 | 0.9753 ± 0.0000 | 0.9905 ± 0.0000 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | dinov2_s  | cls       | P2_leave_one_fruit | msp         |      5 | 0.9429 ± 0.0153 | 0.3651 ± 0.0990 | 0.8020 ± 0.0103 | 0.8340 ± 0.0028 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | dinov2_s  | cls       | P2_leave_one_fruit | msp         |    nan | 0.9860 ± 0.0000 | 0.0554 ± 0.0000 | 0.9798 ± 0.0000 | 0.9905 ± 0.0000 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | resnet50  | cls       | P2_leave_one_fruit | energy      |      5 | 0.8737 ± 0.0087 | 0.6526 ± 0.0315 | 0.6572 ± 0.0087 | 0.7430 ± 0.0102 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | resnet50  | cls       | P2_leave_one_fruit | energy      |    nan | 0.9536 ± 0.0000 | 0.3149 ± 0.0000 | 0.9130 ± 0.0000 | 0.9534 ± 0.0000 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | resnet50  | cls       | P2_leave_one_fruit | knn         |      5 | 0.8658 ± 0.0115 | 0.5632 ± 0.0123 | 0.6558 ± 0.0124 | 0.7430 ± 0.0102 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | resnet50  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9895 ± 0.0000 | 0.0576 ± 0.0000 | 0.9450 ± 0.0000 | 0.9534 ± 0.0000 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9146 ± 0.0036 | 0.4383 ± 0.0046 | 0.6933 ± 0.0092 | 0.7430 ± 0.0102 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9568 ± 0.0000 | 0.2727 ± 0.0000 | 0.9139 ± 0.0000 | 0.9534 ± 0.0000 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | resnet50  | cls       | P2_leave_one_fruit | msp         |      5 | 0.8799 ± 0.0116 | 0.6179 ± 0.0460 | 0.6758 ± 0.0195 | 0.7430 ± 0.0102 |           1480 |              451 | False  |        3 |
| fruits360_x_pear     | resnet50  | cls       | P2_leave_one_fruit | msp         |    nan | 0.9427 ± 0.0000 | 0.3326 ± 0.0000 | 0.9088 ± 0.0000 | 0.9534 ± 0.0000 |           1480 |              451 | False  |        3 |
| fruits360_x_tomato   | dinov2_s  | cls       | P2_leave_one_fruit | energy      |      5 | 0.6955 ± 0.0182 | 0.9384 ± 0.0153 | 0.5536 ± 0.0146 | 0.7622 ± 0.0100 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | dinov2_s  | cls       | P2_leave_one_fruit | energy      |    nan | 0.7535 ± 0.0000 | 0.8091 ± 0.0000 | 0.6798 ± 0.0000 | 0.9126 ± 0.0000 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | dinov2_s  | cls       | P2_leave_one_fruit | knn         |      5 | 0.9610 ± 0.0034 | 0.2192 ± 0.0143 | 0.7343 ± 0.0135 | 0.7622 ± 0.0100 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | dinov2_s  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9967 ± 0.0000 | 0.0121 ± 0.0000 | 0.9099 ± 0.0000 | 0.9126 ± 0.0000 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9512 ± 0.0048 | 0.2828 ± 0.0866 | 0.7315 ± 0.0129 | 0.7622 ± 0.0100 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | dinov2_s  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9874 ± 0.0000 | 0.0576 ± 0.0000 | 0.9010 ± 0.0000 | 0.9126 ± 0.0000 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | dinov2_s  | cls       | P2_leave_one_fruit | msp         |      5 | 0.6987 ± 0.0235 | 0.9364 ± 0.0210 | 0.5528 ± 0.0199 | 0.7622 ± 0.0100 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | dinov2_s  | cls       | P2_leave_one_fruit | msp         |    nan | 0.8215 ± 0.0000 | 0.6545 ± 0.0000 | 0.7443 ± 0.0000 | 0.9126 ± 0.0000 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | resnet50  | cls       | P2_leave_one_fruit | energy      |      5 | 0.6066 ± 0.0464 | 0.9000 ± 0.0424 | 0.4280 ± 0.0361 | 0.6733 ± 0.0201 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | resnet50  | cls       | P2_leave_one_fruit | energy      |    nan | 0.6882 ± 0.0000 | 0.9303 ± 0.0000 | 0.6050 ± 0.0000 | 0.8738 ± 0.0000 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | resnet50  | cls       | P2_leave_one_fruit | knn         |      5 | 0.8748 ± 0.0088 | 0.5687 ± 0.0258 | 0.6006 ± 0.0231 | 0.6733 ± 0.0201 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | resnet50  | cls       | P2_leave_one_fruit | knn         |    nan | 0.9906 ± 0.0000 | 0.0394 ± 0.0000 | 0.8665 ± 0.0000 | 0.8738 ± 0.0000 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |      5 | 0.9194 ± 0.0088 | 0.4121 ± 0.0648 | 0.6294 ± 0.0213 | 0.6733 ± 0.0201 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | resnet50  | cls       | P2_leave_one_fruit | mahalanobis |    nan | 0.9608 ± 0.0000 | 0.1970 ± 0.0000 | 0.8398 ± 0.0000 | 0.8738 ± 0.0000 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | resnet50  | cls       | P2_leave_one_fruit | msp         |      5 | 0.6303 ± 0.0135 | 0.9364 ± 0.0121 | 0.4494 ± 0.0069 | 0.6733 ± 0.0201 |           1601 |              330 | False  |        3 |
| fruits360_x_tomato   | resnet50  | cls       | P2_leave_one_fruit | msp         |    nan | 0.8288 ± 0.0000 | 0.7303 ± 0.0000 | 0.7355 ± 0.0000 | 0.8738 ± 0.0000 |           1601 |              330 | False  |        3 |
| mango_khir           | dinov2_s  | cls       | P2_unseen_interior | energy      |      5 | 0.7189 ± 0.0652 | 0.8039 ± 0.0836 | 0.6434 ± 0.1735 | 0.8667 ± 0.2309 |             10 |              136 | True   |        3 |
| mango_khir           | dinov2_s  | cls       | P2_unseen_interior | energy      |    nan | 0.7088 ± 0.0000 | 0.9853 ± 0.0000 | 0.6904 ± 0.0000 | 0.8000 ± 0.0000 |             10 |              136 | True   |        3 |
| mango_khir           | dinov2_s  | cls       | P2_unseen_interior | knn         |      5 | 0.8145 ± 0.0208 | 0.6642 ± 0.0740 | 0.6890 ± 0.1975 | 0.8667 ± 0.2309 |             10 |              136 | True   |        3 |
| mango_khir           | dinov2_s  | cls       | P2_unseen_interior | knn         |    nan | 0.7824 ± 0.0000 | 0.8676 ± 0.0000 | 0.7154 ± 0.0000 | 0.8000 ± 0.0000 |             10 |              136 | True   |        3 |
| mango_khir           | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.8093 ± 0.0753 | 0.6471 ± 0.1431 | 0.6897 ± 0.2001 | 0.8667 ± 0.2309 |             10 |              136 | True   |        3 |
| mango_khir           | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.7956 ± 0.0000 | 0.8088 ± 0.0000 | 0.7235 ± 0.0000 | 0.8000 ± 0.0000 |             10 |              136 | True   |        3 |
| mango_khir           | dinov2_s  | cls       | P2_unseen_interior | msp         |      5 | 0.7189 ± 0.0652 | 0.8039 ± 0.0836 | 0.6434 ± 0.1735 | 0.8667 ± 0.2309 |             10 |              136 | True   |        3 |
| mango_khir           | dinov2_s  | cls       | P2_unseen_interior | msp         |    nan | 0.7088 ± 0.0000 | 0.9853 ± 0.0000 | 0.6904 ± 0.0000 | 0.8000 ± 0.0000 |             10 |              136 | True   |        3 |
| mango_khir           | resnet50  | cls       | P2_unseen_interior | energy      |      5 | 0.6260 ± 0.0360 | 0.9436 ± 0.0405 | 0.5995 ± 0.0423 | 0.8667 ± 0.1528 |             10 |              136 | True   |        3 |
| mango_khir           | resnet50  | cls       | P2_unseen_interior | energy      |    nan | 0.6338 ± 0.0000 | 1.0000 ± 0.0000 | 0.6250 ± 0.0000 | 0.9000 ± 0.0000 |             10 |              136 | True   |        3 |
| mango_khir           | resnet50  | cls       | P2_unseen_interior | knn         |      5 | 0.7125 ± 0.0409 | 0.9314 ± 0.0449 | 0.6071 ± 0.0862 | 0.8667 ± 0.1528 |             10 |              136 | True   |        3 |
| mango_khir           | resnet50  | cls       | P2_unseen_interior | knn         |    nan | 0.7235 ± 0.0000 | 0.9632 ± 0.0000 | 0.7199 ± 0.0000 | 0.9000 ± 0.0000 |             10 |              136 | True   |        3 |
| mango_khir           | resnet50  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.7088 ± 0.0496 | 0.9412 ± 0.0382 | 0.6083 ± 0.1570 | 0.8667 ± 0.1528 |             10 |              136 | True   |        3 |
| mango_khir           | resnet50  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.7015 ± 0.0000 | 0.9779 ± 0.0000 | 0.6993 ± 0.0000 | 0.9000 ± 0.0000 |             10 |              136 | True   |        3 |
| mango_khir           | resnet50  | cls       | P2_unseen_interior | msp         |      5 | 0.6260 ± 0.0360 | 0.9436 ± 0.0405 | 0.5995 ± 0.0423 | 0.8667 ± 0.1528 |             10 |              136 | True   |        3 |
| mango_khir           | resnet50  | cls       | P2_unseen_interior | msp         |    nan | 0.6338 ± 0.0000 | 1.0000 ± 0.0000 | 0.6250 ± 0.0000 | 0.9000 ± 0.0000 |             10 |              136 | True   |        3 |
| ninepeach            | dinov2_s  | cls       | P1_out_of_grade    | energy      |      5 | 0.3388 ± 0.1400 | 0.9665 ± 0.0305 | 0.3219 ± 0.1355 | 0.8453 ± 0.0839 |            334 |              189 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P1_out_of_grade    | energy      |    nan | 0.4683 ± 0.0000 | 0.9788 ± 0.0000 | 0.4642 ± 0.0000 | 0.9431 ± 0.0000 |            334 |              189 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P1_out_of_grade    | knn         |      5 | 0.6064 ± 0.0152 | 0.9559 ± 0.0081 | 0.5134 ± 0.0337 | 0.8453 ± 0.0839 |            334 |              189 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P1_out_of_grade    | knn         |    nan | 0.7209 ± 0.0000 | 0.8677 ± 0.0000 | 0.6819 ± 0.0000 | 0.9431 ± 0.0000 |            334 |              189 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.6108 ± 0.0333 | 0.9330 ± 0.0122 | 0.5238 ± 0.0596 | 0.8453 ± 0.0839 |            334 |              189 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.7121 ± 0.0000 | 0.9206 ± 0.0000 | 0.6716 ± 0.0000 | 0.9431 ± 0.0000 |            334 |              189 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P1_out_of_grade    | msp         |      5 | 0.3388 ± 0.1400 | 0.9665 ± 0.0305 | 0.3219 ± 0.1355 | 0.8453 ± 0.0839 |            334 |              189 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P1_out_of_grade    | msp         |    nan | 0.4683 ± 0.0000 | 0.9788 ± 0.0000 | 0.4642 ± 0.0000 | 0.9431 ± 0.0000 |            334 |              189 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P2_unseen_interior | energy      |      5 | 0.6418 ± 0.1840 | 0.8530 ± 0.1061 | 0.5933 ± 0.2105 | 0.8533 ± 0.1126 |            300 |              111 | False  |        6 |
| ninepeach            | dinov2_s  | cls       | P2_unseen_interior | energy      |    nan | 0.5829 ± 0.3881 | 0.6960 ± 0.3282 | 0.5780 ± 0.3841 | 0.9377 ± 0.0523 |            300 |              111 | False  |        6 |
| ninepeach            | dinov2_s  | cls       | P2_unseen_interior | knn         |      5 | 0.6285 ± 0.2556 | 0.8131 ± 0.1976 | 0.5172 ± 0.1476 | 0.8533 ± 0.1126 |            300 |              111 | False  |        6 |
| ninepeach            | dinov2_s  | cls       | P2_unseen_interior | knn         |    nan | 0.7397 ± 0.1662 | 0.7600 ± 0.2234 | 0.6940 ± 0.1179 | 0.9377 ± 0.0523 |            300 |              111 | False  |        6 |
| ninepeach            | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.6668 ± 0.2128 | 0.7922 ± 0.2127 | 0.5582 ± 0.1096 | 0.8533 ± 0.1126 |            300 |              111 | False  |        6 |
| ninepeach            | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.6825 ± 0.1852 | 0.8138 ± 0.1645 | 0.6399 ± 0.1400 | 0.9377 ± 0.0523 |            300 |              111 | False  |        6 |
| ninepeach            | dinov2_s  | cls       | P2_unseen_interior | msp         |      5 | 0.6418 ± 0.1840 | 0.8530 ± 0.1061 | 0.5933 ± 0.2105 | 0.8533 ± 0.1126 |            300 |              111 | False  |        6 |
| ninepeach            | dinov2_s  | cls       | P2_unseen_interior | msp         |    nan | 0.5829 ± 0.3881 | 0.6960 ± 0.3282 | 0.5780 ± 0.3841 | 0.9377 ± 0.0523 |            300 |              111 | False  |        6 |
| ninepeach            | dinov2_s  | cls       | P3_foreign         | energy      |      5 | 0.7290 ± 0.0830 | 0.8115 ± 0.0275 | 0.5892 ± 0.0575 | 0.7655 ± 0.0628 |            523 |              168 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P3_foreign         | energy      |    nan | 0.8216 ± 0.0000 | 0.7560 ± 0.0000 | 0.7679 ± 0.0000 | 0.8987 ± 0.0000 |            523 |              168 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P3_foreign         | knn         |      5 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.7655 ± 0.0628 | 0.7655 ± 0.0628 |            523 |              168 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P3_foreign         | knn         |    nan | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.8987 ± 0.0000 | 0.8987 ± 0.0000 |            523 |              168 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P3_foreign         | mahalanobis |      5 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.7655 ± 0.0628 | 0.7655 ± 0.0628 |            523 |              168 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P3_foreign         | mahalanobis |    nan | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.8987 ± 0.0000 | 0.8987 ± 0.0000 |            523 |              168 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P3_foreign         | msp         |      5 | 0.7149 ± 0.0685 | 0.8214 ± 0.0273 | 0.5839 ± 0.0507 | 0.7655 ± 0.0628 |            523 |              168 | False  |        3 |
| ninepeach            | dinov2_s  | cls       | P3_foreign         | msp         |    nan | 0.7581 ± 0.0000 | 0.8333 ± 0.0000 | 0.7228 ± 0.0000 | 0.8987 ± 0.0000 |            523 |              168 | False  |        3 |
| ninepeach            | resnet50  | cls       | P1_out_of_grade    | energy      |      5 | 0.2931 ± 0.1444 | 0.9859 ± 0.0200 | 0.2639 ± 0.1277 | 0.8084 ± 0.0893 |            334 |              189 | False  |        3 |
| ninepeach            | resnet50  | cls       | P1_out_of_grade    | energy      |    nan | 0.2353 ± 0.0000 | 0.9841 ± 0.0000 | 0.2283 ± 0.0000 | 0.9042 ± 0.0000 |            334 |              189 | False  |        3 |
| ninepeach            | resnet50  | cls       | P1_out_of_grade    | knn         |      5 | 0.7201 ± 0.0158 | 0.9242 ± 0.0133 | 0.5835 ± 0.0871 | 0.8084 ± 0.0893 |            334 |              189 | False  |        3 |
| ninepeach            | resnet50  | cls       | P1_out_of_grade    | knn         |    nan | 0.6738 ± 0.0000 | 0.8571 ± 0.0000 | 0.6136 ± 0.0000 | 0.9042 ± 0.0000 |            334 |              189 | False  |        3 |
| ninepeach            | resnet50  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.6747 ± 0.0796 | 0.9118 ± 0.0031 | 0.5559 ± 0.1294 | 0.8084 ± 0.0893 |            334 |              189 | False  |        3 |
| ninepeach            | resnet50  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.7009 ± 0.0000 | 0.8307 ± 0.0000 | 0.6333 ± 0.0000 | 0.9042 ± 0.0000 |            334 |              189 | False  |        3 |
| ninepeach            | resnet50  | cls       | P1_out_of_grade    | msp         |      5 | 0.2931 ± 0.1444 | 0.9859 ± 0.0200 | 0.2639 ± 0.1277 | 0.8084 ± 0.0893 |            334 |              189 | False  |        3 |
| ninepeach            | resnet50  | cls       | P1_out_of_grade    | msp         |    nan | 0.2353 ± 0.0000 | 0.9841 ± 0.0000 | 0.2283 ± 0.0000 | 0.9042 ± 0.0000 |            334 |              189 | False  |        3 |
| ninepeach            | resnet50  | cls       | P2_unseen_interior | energy      |      5 | 0.5140 ± 0.3495 | 0.8176 ± 0.1930 | 0.4984 ± 0.3490 | 0.8840 ± 0.0905 |            300 |              111 | False  |        6 |
| ninepeach            | resnet50  | cls       | P2_unseen_interior | energy      |    nan | 0.5819 ± 0.3230 | 0.7411 ± 0.2394 | 0.5723 ± 0.3229 | 0.9304 ± 0.0443 |            300 |              111 | False  |        6 |
| ninepeach            | resnet50  | cls       | P2_unseen_interior | knn         |      5 | 0.6194 ± 0.2046 | 0.9320 ± 0.0651 | 0.5483 ± 0.1331 | 0.8840 ± 0.0905 |            300 |              111 | False  |        6 |
| ninepeach            | resnet50  | cls       | P2_unseen_interior | knn         |    nan | 0.6233 ± 0.1116 | 0.9147 ± 0.0539 | 0.5867 ± 0.0797 | 0.9304 ± 0.0443 |            300 |              111 | False  |        6 |
| ninepeach            | resnet50  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.6419 ± 0.1541 | 0.9297 ± 0.0652 | 0.5765 ± 0.0896 | 0.8840 ± 0.0905 |            300 |              111 | False  |        6 |
| ninepeach            | resnet50  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.5794 ± 0.1766 | 0.9304 ± 0.0466 | 0.5406 ± 0.1419 | 0.9304 ± 0.0443 |            300 |              111 | False  |        6 |
| ninepeach            | resnet50  | cls       | P2_unseen_interior | msp         |      5 | 0.5140 ± 0.3495 | 0.8176 ± 0.1930 | 0.4984 ± 0.3490 | 0.8840 ± 0.0905 |            300 |              111 | False  |        6 |
| ninepeach            | resnet50  | cls       | P2_unseen_interior | msp         |    nan | 0.5819 ± 0.3230 | 0.7411 ± 0.2394 | 0.5723 ± 0.3229 | 0.9304 ± 0.0443 |            300 |              111 | False  |        6 |
| ninepeach            | resnet50  | cls       | P3_foreign         | energy      |      5 | 0.8095 ± 0.0403 | 0.9107 ± 0.0519 | 0.6782 ± 0.0531 | 0.7909 ± 0.0539 |            523 |              168 | False  |        3 |
| ninepeach            | resnet50  | cls       | P3_foreign         | energy      |    nan | 0.9429 ± 0.0000 | 0.3155 ± 0.0000 | 0.8619 ± 0.0000 | 0.8948 ± 0.0000 |            523 |              168 | False  |        3 |
| ninepeach            | resnet50  | cls       | P3_foreign         | knn         |      5 | 0.9967 ± 0.0018 | 0.0179 ± 0.0215 | 0.7887 ± 0.0524 | 0.7909 ± 0.0539 |            523 |              168 | False  |        3 |
| ninepeach            | resnet50  | cls       | P3_foreign         | knn         |    nan | 0.9975 ± 0.0000 | 0.0119 ± 0.0000 | 0.8929 ± 0.0000 | 0.8948 ± 0.0000 |            523 |              168 | False  |        3 |
| ninepeach            | resnet50  | cls       | P3_foreign         | mahalanobis |      5 | 0.9968 ± 0.0013 | 0.0218 ± 0.0182 | 0.7888 ± 0.0528 | 0.7909 ± 0.0539 |            523 |              168 | False  |        3 |
| ninepeach            | resnet50  | cls       | P3_foreign         | mahalanobis |    nan | 0.9989 ± 0.0000 | 0.0060 ± 0.0000 | 0.8939 ± 0.0000 | 0.8948 ± 0.0000 |            523 |              168 | False  |        3 |
| ninepeach            | resnet50  | cls       | P3_foreign         | msp         |      5 | 0.7568 ± 0.0278 | 0.9048 ± 0.0935 | 0.6444 ± 0.0460 | 0.7909 ± 0.0539 |            523 |              168 | False  |        3 |
| ninepeach            | resnet50  | cls       | P3_foreign         | msp         |    nan | 0.9070 ± 0.0000 | 0.5595 ± 0.0000 | 0.8365 ± 0.0000 | 0.8948 ± 0.0000 |            523 |              168 | False  |        3 |
| raspgrade            | dinov2_s  | cls       | P1_out_of_grade    | energy      |      5 | 0.5428 ± 0.0568 | 0.8889 ± 0.0481 | 0.1856 ± 0.0308 | 0.3606 ± 0.0833 |            720 |               12 | True   |        3 |
| raspgrade            | dinov2_s  | cls       | P1_out_of_grade    | energy      |    nan | 0.4056 ± 0.0000 | 1.0000 ± 0.0000 | 0.3588 ± 0.0000 | 0.7750 ± 0.0000 |            720 |               12 | True   |        3 |
| raspgrade            | dinov2_s  | cls       | P1_out_of_grade    | knn         |      5 | 0.4324 ± 0.0261 | 1.0000 ± 0.0000 | 0.1730 ± 0.0509 | 0.3606 ± 0.0833 |            720 |               12 | True   |        3 |
| raspgrade            | dinov2_s  | cls       | P1_out_of_grade    | knn         |    nan | 0.4944 ± 0.0000 | 0.9167 ± 0.0000 | 0.3878 ± 0.0000 | 0.7750 ± 0.0000 |            720 |               12 | True   |        3 |
| raspgrade            | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.4988 ± 0.0467 | 0.9722 ± 0.0481 | 0.1954 ± 0.0489 | 0.3606 ± 0.0833 |            720 |               12 | True   |        3 |
| raspgrade            | dinov2_s  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.5197 ± 0.0000 | 0.9167 ± 0.0000 | 0.4111 ± 0.0000 | 0.7750 ± 0.0000 |            720 |               12 | True   |        3 |
| raspgrade            | dinov2_s  | cls       | P1_out_of_grade    | msp         |      5 | 0.5682 ± 0.0787 | 0.9167 ± 0.0000 | 0.1976 ± 0.0272 | 0.3606 ± 0.0833 |            720 |               12 | True   |        3 |
| raspgrade            | dinov2_s  | cls       | P1_out_of_grade    | msp         |    nan | 0.3438 ± 0.0000 | 1.0000 ± 0.0000 | 0.3097 ± 0.0000 | 0.7750 ± 0.0000 |            720 |               12 | True   |        3 |
| raspgrade            | dinov2_s  | cls       | P2_unseen_interior | energy      |      5 | 0.5113 ± 0.0201 | 0.9428 ± 0.0360 | 0.2021 ± 0.0901 | 0.3853 ± 0.1275 |            209 |               43 | False  |        9 |
| raspgrade            | dinov2_s  | cls       | P2_unseen_interior | energy      |    nan | 0.6059 ± 0.1015 | 0.8679 ± 0.0883 | 0.5341 ± 0.1021 | 0.8253 ± 0.0702 |            209 |               43 | False  |        9 |
| raspgrade            | dinov2_s  | cls       | P2_unseen_interior | knn         |      5 | 0.5255 ± 0.0406 | 0.9559 ± 0.0312 | 0.2224 ± 0.0712 | 0.3853 ± 0.1275 |            209 |               43 | False  |        9 |
| raspgrade            | dinov2_s  | cls       | P2_unseen_interior | knn         |    nan | 0.5732 ± 0.0945 | 0.9222 ± 0.0328 | 0.4840 ± 0.0664 | 0.8253 ± 0.0702 |            209 |               43 | False  |        9 |
| raspgrade            | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.5297 ± 0.0507 | 0.9574 ± 0.0275 | 0.2234 ± 0.0705 | 0.3853 ± 0.1275 |            209 |               43 | False  |        9 |
| raspgrade            | dinov2_s  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.5589 ± 0.0738 | 0.9507 ± 0.0362 | 0.4735 ± 0.0494 | 0.8253 ± 0.0702 |            209 |               43 | False  |        9 |
| raspgrade            | dinov2_s  | cls       | P2_unseen_interior | msp         |      5 | 0.5052 ± 0.0257 | 0.9473 ± 0.0419 | 0.2046 ± 0.0977 | 0.3853 ± 0.1275 |            209 |               43 | False  |        9 |
| raspgrade            | dinov2_s  | cls       | P2_unseen_interior | msp         |    nan | 0.5827 ± 0.1322 | 0.9050 ± 0.0495 | 0.5227 ± 0.1321 | 0.8253 ± 0.0702 |            209 |               43 | False  |        9 |
| raspgrade            | resnet50  | cls       | P1_out_of_grade    | energy      |      5 | 0.5774 ± 0.0448 | 0.9722 ± 0.0481 | 0.2254 ± 0.0808 | 0.3745 ± 0.0826 |            720 |               12 | True   |        3 |
| raspgrade            | resnet50  | cls       | P1_out_of_grade    | energy      |    nan | 0.4811 ± 0.0000 | 1.0000 ± 0.0000 | 0.4197 ± 0.0000 | 0.7583 ± 0.0000 |            720 |               12 | True   |        3 |
| raspgrade            | resnet50  | cls       | P1_out_of_grade    | knn         |      5 | 0.5289 ± 0.0307 | 1.0000 ± 0.0000 | 0.2115 ± 0.0653 | 0.3745 ± 0.0826 |            720 |               12 | True   |        3 |
| raspgrade            | resnet50  | cls       | P1_out_of_grade    | knn         |    nan | 0.6115 ± 0.0000 | 0.9167 ± 0.0000 | 0.4670 ± 0.0000 | 0.7583 ± 0.0000 |            720 |               12 | True   |        3 |
| raspgrade            | resnet50  | cls       | P1_out_of_grade    | mahalanobis |      5 | 0.6014 ± 0.0548 | 0.9722 ± 0.0481 | 0.2397 ± 0.0731 | 0.3745 ± 0.0826 |            720 |               12 | True   |        3 |
| raspgrade            | resnet50  | cls       | P1_out_of_grade    | mahalanobis |    nan | 0.6090 ± 0.0000 | 0.8333 ± 0.0000 | 0.4601 ± 0.0000 | 0.7583 ± 0.0000 |            720 |               12 | True   |        3 |
| raspgrade            | resnet50  | cls       | P1_out_of_grade    | msp         |      5 | 0.5453 ± 0.0254 | 0.9444 ± 0.0481 | 0.2162 ± 0.0760 | 0.3745 ± 0.0826 |            720 |               12 | True   |        3 |
| raspgrade            | resnet50  | cls       | P1_out_of_grade    | msp         |    nan | 0.4764 ± 0.0000 | 1.0000 ± 0.0000 | 0.4192 ± 0.0000 | 0.7583 ± 0.0000 |            720 |               12 | True   |        3 |
| raspgrade            | resnet50  | cls       | P2_unseen_interior | energy      |      5 | 0.5082 ± 0.0322 | 0.9493 ± 0.0275 | 0.1806 ± 0.0688 | 0.3555 ± 0.0962 |            209 |               43 | False  |        9 |
| raspgrade            | resnet50  | cls       | P2_unseen_interior | energy      |    nan | 0.6137 ± 0.1427 | 0.8833 ± 0.0892 | 0.5347 ± 0.1433 | 0.8119 ± 0.0831 |            209 |               43 | False  |        9 |
| raspgrade            | resnet50  | cls       | P2_unseen_interior | knn         |      5 | 0.5253 ± 0.0526 | 0.9429 ± 0.0364 | 0.1863 ± 0.0469 | 0.3555 ± 0.0962 |            209 |               43 | False  |        9 |
| raspgrade            | resnet50  | cls       | P2_unseen_interior | knn         |    nan | 0.5671 ± 0.0816 | 0.9248 ± 0.0170 | 0.4700 ± 0.0482 | 0.8119 ± 0.0831 |            209 |               43 | False  |        9 |
| raspgrade            | resnet50  | cls       | P2_unseen_interior | mahalanobis |      5 | 0.5263 ± 0.0517 | 0.9366 ± 0.0246 | 0.1914 ± 0.0437 | 0.3555 ± 0.0962 |            209 |               43 | False  |        9 |
| raspgrade            | resnet50  | cls       | P2_unseen_interior | mahalanobis |    nan | 0.5503 ± 0.0651 | 0.9219 ± 0.0517 | 0.4529 ± 0.0235 | 0.8119 ± 0.0831 |            209 |               43 | False  |        9 |
| raspgrade            | resnet50  | cls       | P2_unseen_interior | msp         |      5 | 0.5109 ± 0.0263 | 0.9523 ± 0.0293 | 0.1864 ± 0.0720 | 0.3555 ± 0.0962 |            209 |               43 | False  |        9 |
| raspgrade            | resnet50  | cls       | P2_unseen_interior | msp         |    nan | 0.6006 ± 0.1697 | 0.8981 ± 0.0757 | 0.5347 ± 0.1536 | 0.8119 ± 0.0831 |            209 |               43 | False  |        9 |

## Cross-domain

| view   | encoder   | variant   | head   |   shot | align   | acc             | macro_f1        |   n_runs |
|:-------|:----------|:----------|:-------|-------:|:--------|:----------------|:----------------|---------:|
| b3->b4 | clip_b    | cls       | linear |      0 | bn      | 0.8806 ± 0.0000 | 0.8828 ± 0.0000 |        3 |
| b3->b4 | clip_b    | cls       | linear |      0 | nan     | 0.7851 ± 0.0000 | 0.7731 ± 0.0000 |        3 |
| b3->b4 | clip_b    | cls       | linear |      1 | bn      | 0.8877 ± 0.0055 | 0.8898 ± 0.0054 |        3 |
| b3->b4 | clip_b    | cls       | linear |      1 | nan     | 0.8002 ± 0.0015 | 0.7921 ± 0.0008 |        3 |
| b3->b4 | clip_b    | cls       | linear |      5 | bn      | 0.9010 ± 0.0107 | 0.9023 ± 0.0111 |        3 |
| b3->b4 | clip_b    | cls       | linear |      5 | nan     | 0.8302 ± 0.0080 | 0.8243 ± 0.0086 |        3 |
| b3->b4 | clip_b    | cls       | linear |     10 | bn      | 0.9098 ± 0.0070 | 0.9109 ± 0.0076 |        3 |
| b3->b4 | clip_b    | cls       | linear |     10 | nan     | 0.8656 ± 0.0203 | 0.8623 ± 0.0223 |        3 |
| b3->b4 | clip_b    | cls       | proto  |      0 | bn      | 0.8143 ± 0.0000 | 0.8082 ± 0.0000 |        3 |
| b3->b4 | clip_b    | cls       | proto  |      0 | nan     | 0.6844 ± 0.0000 | 0.5680 ± 0.0000 |        3 |
| b3->b4 | clip_b    | cls       | proto  |      1 | bn      | 0.8205 ± 0.0031 | 0.8146 ± 0.0032 |        3 |
| b3->b4 | clip_b    | cls       | proto  |      1 | nan     | 0.6844 ± 0.0000 | 0.5680 ± 0.0000 |        3 |
| b3->b4 | clip_b    | cls       | proto  |      5 | bn      | 0.8302 ± 0.0027 | 0.8242 ± 0.0024 |        3 |
| b3->b4 | clip_b    | cls       | proto  |      5 | nan     | 0.6844 ± 0.0000 | 0.5680 ± 0.0000 |        3 |
| b3->b4 | clip_b    | cls       | proto  |     10 | bn      | 0.8364 ± 0.0031 | 0.8305 ± 0.0030 |        3 |
| b3->b4 | clip_b    | cls       | proto  |     10 | nan     | 0.6870 ± 0.0046 | 0.5729 ± 0.0061 |        3 |
| b3->b4 | dinov2_b  | cls       | linear |      0 | bn      | 0.8753 ± 0.0000 | 0.8717 ± 0.0000 |        3 |
| b3->b4 | dinov2_b  | cls       | linear |      0 | nan     | 0.8886 ± 0.0000 | 0.8866 ± 0.0000 |        3 |
| b3->b4 | dinov2_b  | cls       | linear |      1 | bn      | 0.8798 ± 0.0055 | 0.8771 ± 0.0071 |        3 |
| b3->b4 | dinov2_b  | cls       | linear |      1 | nan     | 0.8921 ± 0.0041 | 0.8911 ± 0.0052 |        3 |
| b3->b4 | dinov2_b  | cls       | linear |      5 | bn      | 0.9125 ± 0.0027 | 0.9128 ± 0.0027 |        3 |
| b3->b4 | dinov2_b  | cls       | linear |      5 | nan     | 0.9063 ± 0.0067 | 0.9066 ± 0.0069 |        3 |
| b3->b4 | dinov2_b  | cls       | linear |     10 | bn      | 0.9204 ± 0.0080 | 0.9214 ± 0.0085 |        3 |
| b3->b4 | dinov2_b  | cls       | linear |     10 | nan     | 0.9169 ± 0.0107 | 0.9180 ± 0.0113 |        3 |
| b3->b4 | dinov2_b  | cls       | proto  |      0 | bn      | 0.8462 ± 0.0000 | 0.8394 ± 0.0000 |        3 |
| b3->b4 | dinov2_b  | cls       | proto  |      0 | nan     | 0.8329 ± 0.0000 | 0.8344 ± 0.0000 |        3 |
| b3->b4 | dinov2_b  | cls       | proto  |      1 | bn      | 0.8497 ± 0.0015 | 0.8434 ± 0.0018 |        3 |
| b3->b4 | dinov2_b  | cls       | proto  |      1 | nan     | 0.8347 ± 0.0015 | 0.8362 ± 0.0016 |        3 |
| b3->b4 | dinov2_b  | cls       | proto  |      5 | bn      | 0.8576 ± 0.0031 | 0.8524 ± 0.0034 |        3 |
| b3->b4 | dinov2_b  | cls       | proto  |      5 | nan     | 0.8426 ± 0.0015 | 0.8446 ± 0.0015 |        3 |
| b3->b4 | dinov2_b  | cls       | proto  |     10 | bn      | 0.8691 ± 0.0041 | 0.8648 ± 0.0044 |        3 |
| b3->b4 | dinov2_b  | cls       | proto  |     10 | nan     | 0.8470 ± 0.0015 | 0.8491 ± 0.0015 |        3 |
| b3->b4 | dinov2_s  | cls       | linear |      0 | bn      | 0.9072 ± 0.0000 | 0.9094 ± 0.0000 |        3 |
| b3->b4 | dinov2_s  | cls       | linear |      0 | nan     | 0.9151 ± 0.0000 | 0.9172 ± 0.0000 |        3 |
| b3->b4 | dinov2_s  | cls       | linear |      1 | bn      | 0.9080 ± 0.0015 | 0.9104 ± 0.0014 |        3 |
| b3->b4 | dinov2_s  | cls       | linear |      1 | nan     | 0.9178 ± 0.0046 | 0.9200 ± 0.0045 |        3 |
| b3->b4 | dinov2_s  | cls       | linear |      5 | bn      | 0.9169 ± 0.0031 | 0.9191 ± 0.0030 |        3 |
| b3->b4 | dinov2_s  | cls       | linear |      5 | nan     | 0.9222 ± 0.0031 | 0.9242 ± 0.0030 |        3 |
| b3->b4 | dinov2_s  | cls       | linear |     10 | bn      | 0.9284 ± 0.0096 | 0.9303 ± 0.0093 |        3 |
| b3->b4 | dinov2_s  | cls       | linear |     10 | nan     | 0.9284 ± 0.0027 | 0.9302 ± 0.0027 |        3 |
| b3->b4 | dinov2_s  | cls       | proto  |      0 | bn      | 0.8568 ± 0.0000 | 0.8582 ± 0.0000 |        3 |
| b3->b4 | dinov2_s  | cls       | proto  |      0 | nan     | 0.7003 ± 0.0000 | 0.6693 ± 0.0000 |        3 |
| b3->b4 | dinov2_s  | cls       | proto  |      1 | bn      | 0.8603 ± 0.0031 | 0.8618 ± 0.0031 |        3 |
| b3->b4 | dinov2_s  | cls       | proto  |      1 | nan     | 0.7038 ± 0.0041 | 0.6751 ± 0.0056 |        3 |
| b3->b4 | dinov2_s  | cls       | proto  |      5 | bn      | 0.8718 ± 0.0015 | 0.8734 ± 0.0015 |        3 |
| b3->b4 | dinov2_s  | cls       | proto  |      5 | nan     | 0.7171 ± 0.0041 | 0.6948 ± 0.0054 |        3 |
| b3->b4 | dinov2_s  | cls       | proto  |     10 | bn      | 0.8824 ± 0.0015 | 0.8842 ± 0.0013 |        3 |
| b3->b4 | dinov2_s  | cls       | proto  |     10 | nan     | 0.7268 ± 0.0027 | 0.7081 ± 0.0026 |        3 |
| b3->b4 | resnet50  | cls       | linear |      0 | bn      | 0.6631 ± 0.0000 | 0.6535 ± 0.0000 |        3 |
| b3->b4 | resnet50  | cls       | linear |      0 | nan     | 0.8064 ± 0.0000 | 0.8102 ± 0.0000 |        3 |
| b3->b4 | resnet50  | cls       | linear |      1 | bn      | 0.6755 ± 0.0041 | 0.6683 ± 0.0045 |        3 |
| b3->b4 | resnet50  | cls       | linear |      1 | nan     | 0.8099 ± 0.0015 | 0.8138 ± 0.0015 |        3 |
| b3->b4 | resnet50  | cls       | linear |      5 | bn      | 0.7109 ± 0.0186 | 0.7088 ± 0.0211 |        3 |
| b3->b4 | resnet50  | cls       | linear |      5 | nan     | 0.8179 ± 0.0155 | 0.8220 ± 0.0156 |        3 |
| b3->b4 | resnet50  | cls       | linear |     10 | bn      | 0.7374 ± 0.0166 | 0.7380 ± 0.0152 |        3 |
| b3->b4 | resnet50  | cls       | linear |     10 | nan     | 0.8294 ± 0.0093 | 0.8334 ± 0.0091 |        3 |
| b3->b4 | resnet50  | cls       | proto  |      0 | bn      | 0.6578 ± 0.0000 | 0.6363 ± 0.0000 |        3 |
| b3->b4 | resnet50  | cls       | proto  |      0 | nan     | 0.5729 ± 0.0000 | 0.5126 ± 0.0000 |        3 |
| b3->b4 | resnet50  | cls       | proto  |      1 | bn      | 0.6578 ± 0.0027 | 0.6359 ± 0.0031 |        3 |
| b3->b4 | resnet50  | cls       | proto  |      1 | nan     | 0.5729 ± 0.0000 | 0.5123 ± 0.0001 |        3 |
| b3->b4 | resnet50  | cls       | proto  |      5 | bn      | 0.6649 ± 0.0015 | 0.6447 ± 0.0013 |        3 |
| b3->b4 | resnet50  | cls       | proto  |      5 | nan     | 0.5791 ± 0.0015 | 0.5208 ± 0.0019 |        3 |
| b3->b4 | resnet50  | cls       | proto  |     10 | bn      | 0.6702 ± 0.0031 | 0.6507 ± 0.0022 |        3 |
| b3->b4 | resnet50  | cls       | proto  |     10 | nan     | 0.5844 ± 0.0041 | 0.5278 ± 0.0059 |        3 |
| b4->b3 | clip_b    | cls       | linear |      0 | bn      | 0.8146 ± 0.0000 | 0.8023 ± 0.0000 |        3 |
| b4->b3 | clip_b    | cls       | linear |      0 | nan     | 0.6517 ± 0.0000 | 0.6323 ± 0.0000 |        3 |
| b4->b3 | clip_b    | cls       | linear |      1 | bn      | 0.8071 ± 0.0032 | 0.7940 ± 0.0042 |        3 |
| b4->b3 | clip_b    | cls       | linear |      1 | nan     | 0.6573 ± 0.0149 | 0.6388 ± 0.0154 |        3 |
| b4->b3 | clip_b    | cls       | linear |      5 | bn      | 0.8240 ± 0.0032 | 0.8142 ± 0.0039 |        3 |
| b4->b3 | clip_b    | cls       | linear |      5 | nan     | 0.7079 ± 0.0149 | 0.6910 ± 0.0110 |        3 |
| b4->b3 | clip_b    | cls       | linear |     10 | bn      | 0.8240 ± 0.0032 | 0.8141 ± 0.0028 |        3 |
| b4->b3 | clip_b    | cls       | linear |     10 | nan     | 0.7584 ± 0.0257 | 0.7436 ± 0.0310 |        3 |
| b4->b3 | clip_b    | cls       | proto  |      0 | bn      | 0.7472 ± 0.0000 | 0.7389 ± 0.0000 |        3 |
| b4->b3 | clip_b    | cls       | proto  |      0 | nan     | 0.5112 ± 0.0000 | 0.5020 ± 0.0000 |        3 |
| b4->b3 | clip_b    | cls       | proto  |      1 | bn      | 0.7491 ± 0.0032 | 0.7416 ± 0.0035 |        3 |
| b4->b3 | clip_b    | cls       | proto  |      1 | nan     | 0.5112 ± 0.0000 | 0.5020 ± 0.0000 |        3 |
| b4->b3 | clip_b    | cls       | proto  |      5 | bn      | 0.7491 ± 0.0032 | 0.7420 ± 0.0028 |        3 |
| b4->b3 | clip_b    | cls       | proto  |      5 | nan     | 0.5112 ± 0.0000 | 0.5020 ± 0.0000 |        3 |
| b4->b3 | clip_b    | cls       | proto  |     10 | bn      | 0.7528 ± 0.0000 | 0.7452 ± 0.0000 |        3 |
| b4->b3 | clip_b    | cls       | proto  |     10 | nan     | 0.5112 ± 0.0000 | 0.5020 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | linear |      0 | bn      | 0.7528 ± 0.0000 | 0.7482 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | linear |      0 | nan     | 0.6461 ± 0.0000 | 0.6198 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | linear |      1 | bn      | 0.7509 ± 0.0032 | 0.7454 ± 0.0024 |        3 |
| b4->b3 | dinov2_b  | cls       | linear |      1 | nan     | 0.6536 ± 0.0117 | 0.6305 ± 0.0170 |        3 |
| b4->b3 | dinov2_b  | cls       | linear |      5 | bn      | 0.7678 ± 0.0065 | 0.7654 ± 0.0069 |        3 |
| b4->b3 | dinov2_b  | cls       | linear |      5 | nan     | 0.7079 ± 0.0195 | 0.7017 ± 0.0232 |        3 |
| b4->b3 | dinov2_b  | cls       | linear |     10 | bn      | 0.7865 ± 0.0203 | 0.7834 ± 0.0205 |        3 |
| b4->b3 | dinov2_b  | cls       | linear |     10 | nan     | 0.7453 ± 0.0086 | 0.7419 ± 0.0071 |        3 |
| b4->b3 | dinov2_b  | cls       | proto  |      0 | bn      | 0.7303 ± 0.0000 | 0.7225 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | proto  |      0 | nan     | 0.5843 ± 0.0000 | 0.5695 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | proto  |      1 | bn      | 0.7303 ± 0.0000 | 0.7225 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | proto  |      1 | nan     | 0.5843 ± 0.0000 | 0.5695 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | proto  |      5 | bn      | 0.7303 ± 0.0000 | 0.7225 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | proto  |      5 | nan     | 0.5955 ± 0.0000 | 0.5852 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | proto  |     10 | bn      | 0.7303 ± 0.0000 | 0.7225 ± 0.0000 |        3 |
| b4->b3 | dinov2_b  | cls       | proto  |     10 | nan     | 0.5974 ± 0.0032 | 0.5878 ± 0.0044 |        3 |
| b4->b3 | dinov2_s  | cls       | linear |      0 | bn      | 0.8034 ± 0.0000 | 0.8028 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | linear |      0 | nan     | 0.8090 ± 0.0000 | 0.8073 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | linear |      1 | bn      | 0.8127 ± 0.0065 | 0.8114 ± 0.0057 |        3 |
| b4->b3 | dinov2_s  | cls       | linear |      1 | nan     | 0.8090 ± 0.0097 | 0.8073 ± 0.0094 |        3 |
| b4->b3 | dinov2_s  | cls       | linear |      5 | bn      | 0.8221 ± 0.0086 | 0.8200 ± 0.0089 |        3 |
| b4->b3 | dinov2_s  | cls       | linear |      5 | nan     | 0.8277 ± 0.0086 | 0.8260 ± 0.0090 |        3 |
| b4->b3 | dinov2_s  | cls       | linear |     10 | bn      | 0.8446 ± 0.0227 | 0.8418 ± 0.0223 |        3 |
| b4->b3 | dinov2_s  | cls       | linear |     10 | nan     | 0.8371 ± 0.0097 | 0.8348 ± 0.0093 |        3 |
| b4->b3 | dinov2_s  | cls       | proto  |      0 | bn      | 0.7809 ± 0.0000 | 0.7694 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | proto  |      0 | nan     | 0.6966 ± 0.0000 | 0.6996 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | proto  |      1 | bn      | 0.7809 ± 0.0000 | 0.7694 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | proto  |      1 | nan     | 0.6966 ± 0.0000 | 0.6996 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | proto  |      5 | bn      | 0.7809 ± 0.0000 | 0.7694 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | proto  |      5 | nan     | 0.6966 ± 0.0000 | 0.6996 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | proto  |     10 | bn      | 0.7809 ± 0.0000 | 0.7694 ± 0.0000 |        3 |
| b4->b3 | dinov2_s  | cls       | proto  |     10 | nan     | 0.6966 ± 0.0000 | 0.6996 ± 0.0000 |        3 |
| b4->b3 | resnet50  | cls       | linear |      0 | bn      | 0.5730 ± 0.0000 | 0.5723 ± 0.0000 |        3 |
| b4->b3 | resnet50  | cls       | linear |      0 | nan     | 0.5112 ± 0.0000 | 0.4736 ± 0.0000 |        3 |
| b4->b3 | resnet50  | cls       | linear |      1 | bn      | 0.5787 ± 0.0056 | 0.5761 ± 0.0045 |        3 |
| b4->b3 | resnet50  | cls       | linear |      1 | nan     | 0.5112 ± 0.0000 | 0.4736 ± 0.0000 |        3 |
| b4->b3 | resnet50  | cls       | linear |      5 | bn      | 0.6479 ± 0.0213 | 0.6450 ± 0.0219 |        3 |
| b4->b3 | resnet50  | cls       | linear |      5 | nan     | 0.5599 ± 0.0032 | 0.5403 ± 0.0081 |        3 |
| b4->b3 | resnet50  | cls       | linear |     10 | bn      | 0.6910 ± 0.0225 | 0.6904 ± 0.0239 |        3 |
| b4->b3 | resnet50  | cls       | linear |     10 | nan     | 0.5918 ± 0.0227 | 0.5779 ± 0.0275 |        3 |
| b4->b3 | resnet50  | cls       | proto  |      0 | bn      | 0.7191 ± 0.0000 | 0.7088 ± 0.0000 |        3 |
| b4->b3 | resnet50  | cls       | proto  |      0 | nan     | 0.6629 ± 0.0000 | 0.6595 ± 0.0000 |        3 |
| b4->b3 | resnet50  | cls       | proto  |      1 | bn      | 0.7210 ± 0.0032 | 0.7109 ± 0.0037 |        3 |
| b4->b3 | resnet50  | cls       | proto  |      1 | nan     | 0.6629 ± 0.0000 | 0.6595 ± 0.0000 |        3 |
| b4->b3 | resnet50  | cls       | proto  |      5 | bn      | 0.7228 ± 0.0032 | 0.7125 ± 0.0033 |        3 |
| b4->b3 | resnet50  | cls       | proto  |      5 | nan     | 0.6629 ± 0.0000 | 0.6595 ± 0.0000 |        3 |
| b4->b3 | resnet50  | cls       | proto  |     10 | bn      | 0.7266 ± 0.0032 | 0.7162 ± 0.0033 |        3 |
| b4->b3 | resnet50  | cls       | proto  |     10 | nan     | 0.6629 ± 0.0000 | 0.6595 ± 0.0000 |        3 |
| banana | clip_b    | cls       | linear |      0 | bn      | 0.7620 ± 0.0000 | 0.7527 ± 0.0000 |        3 |
| banana | clip_b    | cls       | linear |      0 | nan     | 0.6060 ± 0.0000 | 0.5435 ± 0.0000 |        3 |
| banana | clip_b    | cls       | linear |      1 | bn      | 0.7740 ± 0.0053 | 0.7660 ± 0.0061 |        3 |
| banana | clip_b    | cls       | linear |      1 | nan     | 0.6160 ± 0.0020 | 0.5588 ± 0.0030 |        3 |
| banana | clip_b    | cls       | linear |      5 | bn      | 0.7853 ± 0.0050 | 0.7793 ± 0.0056 |        3 |
| banana | clip_b    | cls       | linear |      5 | nan     | 0.6447 ± 0.0012 | 0.6028 ± 0.0010 |        3 |
| banana | clip_b    | cls       | linear |     10 | bn      | 0.7947 ± 0.0110 | 0.7895 ± 0.0121 |        3 |
| banana | clip_b    | cls       | linear |     10 | nan     | 0.6653 ± 0.0042 | 0.6316 ± 0.0056 |        3 |
| banana | clip_b    | cls       | proto  |      0 | bn      | 0.5800 ± 0.0000 | 0.5726 ± 0.0000 |        3 |
| banana | clip_b    | cls       | proto  |      0 | nan     | 0.5880 ± 0.0000 | 0.5383 ± 0.0000 |        3 |
| banana | clip_b    | cls       | proto  |      1 | bn      | 0.5780 ± 0.0020 | 0.5704 ± 0.0026 |        3 |
| banana | clip_b    | cls       | proto  |      1 | nan     | 0.5927 ± 0.0031 | 0.5455 ± 0.0043 |        3 |
| banana | clip_b    | cls       | proto  |      5 | bn      | 0.5813 ± 0.0012 | 0.5742 ± 0.0011 |        3 |
| banana | clip_b    | cls       | proto  |      5 | nan     | 0.6013 ± 0.0031 | 0.5611 ± 0.0030 |        3 |
| banana | clip_b    | cls       | proto  |     10 | bn      | 0.5860 ± 0.0020 | 0.5793 ± 0.0024 |        3 |
| banana | clip_b    | cls       | proto  |     10 | nan     | 0.5987 ± 0.0012 | 0.5620 ± 0.0016 |        3 |
| banana | dinov2_b  | cls       | linear |      0 | bn      | 0.7800 ± 0.0000 | 0.7761 ± 0.0000 |        3 |
| banana | dinov2_b  | cls       | linear |      0 | nan     | 0.6780 ± 0.0000 | 0.6625 ± 0.0000 |        3 |
| banana | dinov2_b  | cls       | linear |      1 | bn      | 0.7813 ± 0.0070 | 0.7773 ± 0.0072 |        3 |
| banana | dinov2_b  | cls       | linear |      1 | nan     | 0.6760 ± 0.0035 | 0.6601 ± 0.0042 |        3 |
| banana | dinov2_b  | cls       | linear |      5 | bn      | 0.8113 ± 0.0136 | 0.8093 ± 0.0143 |        3 |
| banana | dinov2_b  | cls       | linear |      5 | nan     | 0.6980 ± 0.0053 | 0.6868 ± 0.0059 |        3 |
| banana | dinov2_b  | cls       | linear |     10 | bn      | 0.8327 ± 0.0162 | 0.8314 ± 0.0168 |        3 |
| banana | dinov2_b  | cls       | linear |     10 | nan     | 0.7187 ± 0.0122 | 0.7107 ± 0.0138 |        3 |
| banana | dinov2_b  | cls       | proto  |      0 | bn      | 0.6140 ± 0.0000 | 0.6134 ± 0.0000 |        3 |
| banana | dinov2_b  | cls       | proto  |      0 | nan     | 0.5520 ± 0.0000 | 0.5102 ± 0.0000 |        3 |
| banana | dinov2_b  | cls       | proto  |      1 | bn      | 0.6140 ± 0.0000 | 0.6134 ± 0.0000 |        3 |
| banana | dinov2_b  | cls       | proto  |      1 | nan     | 0.5520 ± 0.0000 | 0.5102 ± 0.0000 |        3 |
| banana | dinov2_b  | cls       | proto  |      5 | bn      | 0.6153 ± 0.0023 | 0.6147 ± 0.0022 |        3 |
| banana | dinov2_b  | cls       | proto  |      5 | nan     | 0.5560 ± 0.0000 | 0.5170 ± 0.0000 |        3 |
| banana | dinov2_b  | cls       | proto  |     10 | bn      | 0.6187 ± 0.0012 | 0.6181 ± 0.0012 |        3 |
| banana | dinov2_b  | cls       | proto  |     10 | nan     | 0.5533 ± 0.0012 | 0.5149 ± 0.0009 |        3 |
| banana | dinov2_s  | cls       | linear |      0 | bn      | 0.8280 ± 0.0000 | 0.8268 ± 0.0000 |        3 |
| banana | dinov2_s  | cls       | linear |      0 | nan     | 0.7140 ± 0.0000 | 0.7013 ± 0.0000 |        3 |
| banana | dinov2_s  | cls       | linear |      1 | bn      | 0.8293 ± 0.0042 | 0.8282 ± 0.0043 |        3 |
| banana | dinov2_s  | cls       | linear |      1 | nan     | 0.7127 ± 0.0070 | 0.6994 ± 0.0072 |        3 |
| banana | dinov2_s  | cls       | linear |      5 | bn      | 0.8400 ± 0.0131 | 0.8390 ± 0.0136 |        3 |
| banana | dinov2_s  | cls       | linear |      5 | nan     | 0.7287 ± 0.0031 | 0.7185 ± 0.0039 |        3 |
| banana | dinov2_s  | cls       | linear |     10 | bn      | 0.8487 ± 0.0204 | 0.8479 ± 0.0210 |        3 |
| banana | dinov2_s  | cls       | linear |     10 | nan     | 0.7427 ± 0.0031 | 0.7340 ± 0.0042 |        3 |
| banana | dinov2_s  | cls       | proto  |      0 | bn      | 0.6100 ± 0.0000 | 0.6095 ± 0.0000 |        3 |
| banana | dinov2_s  | cls       | proto  |      0 | nan     | 0.5480 ± 0.0000 | 0.4873 ± 0.0000 |        3 |
| banana | dinov2_s  | cls       | proto  |      1 | bn      | 0.6107 ± 0.0012 | 0.6102 ± 0.0012 |        3 |
| banana | dinov2_s  | cls       | proto  |      1 | nan     | 0.5467 ± 0.0012 | 0.4864 ± 0.0008 |        3 |
| banana | dinov2_s  | cls       | proto  |      5 | bn      | 0.6127 ± 0.0023 | 0.6122 ± 0.0024 |        3 |
| banana | dinov2_s  | cls       | proto  |      5 | nan     | 0.5500 ± 0.0000 | 0.4920 ± 0.0000 |        3 |
| banana | dinov2_s  | cls       | proto  |     10 | bn      | 0.6147 ± 0.0012 | 0.6142 ± 0.0012 |        3 |
| banana | dinov2_s  | cls       | proto  |     10 | nan     | 0.5513 ± 0.0012 | 0.4945 ± 0.0009 |        3 |
| banana | resnet50  | cls       | linear |      0 | bn      | 0.5060 ± 0.0000 | 0.3532 ± 0.0000 |        3 |
| banana | resnet50  | cls       | linear |      0 | nan     | 0.4920 ± 0.0000 | 0.3298 ± 0.0000 |        3 |
| banana | resnet50  | cls       | linear |      1 | bn      | 0.5120 ± 0.0020 | 0.3679 ± 0.0075 |        3 |
| banana | resnet50  | cls       | linear |      1 | nan     | 0.4940 ± 0.0053 | 0.3375 ± 0.0083 |        3 |
| banana | resnet50  | cls       | linear |      5 | bn      | 0.5187 ± 0.0114 | 0.3863 ± 0.0233 |        3 |
| banana | resnet50  | cls       | linear |      5 | nan     | 0.4920 ± 0.0092 | 0.3442 ± 0.0125 |        3 |
| banana | resnet50  | cls       | linear |     10 | bn      | 0.5387 ± 0.0136 | 0.4261 ± 0.0216 |        3 |
| banana | resnet50  | cls       | linear |     10 | nan     | 0.5107 ± 0.0070 | 0.3859 ± 0.0095 |        3 |
| banana | resnet50  | cls       | proto  |      0 | bn      | 0.7060 ± 0.0000 | 0.7024 ± 0.0000 |        3 |
| banana | resnet50  | cls       | proto  |      0 | nan     | 0.6040 ± 0.0000 | 0.5798 ± 0.0000 |        3 |
| banana | resnet50  | cls       | proto  |      1 | bn      | 0.7100 ± 0.0020 | 0.7065 ± 0.0020 |        3 |
| banana | resnet50  | cls       | proto  |      1 | nan     | 0.6047 ± 0.0012 | 0.5809 ± 0.0013 |        3 |
| banana | resnet50  | cls       | proto  |      5 | bn      | 0.7107 ± 0.0031 | 0.7072 ± 0.0030 |        3 |
| banana | resnet50  | cls       | proto  |      5 | nan     | 0.6153 ± 0.0081 | 0.5948 ± 0.0101 |        3 |
| banana | resnet50  | cls       | proto  |     10 | bn      | 0.7140 ± 0.0020 | 0.7105 ± 0.0022 |        3 |
| banana | resnet50  | cls       | proto  |     10 | nan     | 0.6307 ± 0.0031 | 0.6137 ± 0.0037 |        3 |
| mango  | clip_b    | cls       | linear |      0 | bn      | 0.8740 ± 0.0000 | 0.8726 ± 0.0000 |        3 |
| mango  | clip_b    | cls       | linear |      0 | nan     | 0.8220 ± 0.0000 | 0.8172 ± 0.0000 |        3 |
| mango  | clip_b    | cls       | linear |      1 | bn      | 0.8780 ± 0.0035 | 0.8767 ± 0.0036 |        3 |
| mango  | clip_b    | cls       | linear |      1 | nan     | 0.8400 ± 0.0174 | 0.8366 ± 0.0187 |        3 |
| mango  | clip_b    | cls       | linear |      5 | bn      | 0.8860 ± 0.0040 | 0.8850 ± 0.0042 |        3 |
| mango  | clip_b    | cls       | linear |      5 | nan     | 0.8813 ± 0.0129 | 0.8800 ± 0.0133 |        3 |
| mango  | clip_b    | cls       | linear |     10 | bn      | 0.9000 ± 0.0069 | 0.8993 ± 0.0070 |        3 |
| mango  | clip_b    | cls       | linear |     10 | nan     | 0.9007 ± 0.0012 | 0.9000 ± 0.0012 |        3 |
| mango  | clip_b    | cls       | proto  |      0 | bn      | 0.8580 ± 0.0000 | 0.8570 ± 0.0000 |        3 |
| mango  | clip_b    | cls       | proto  |      0 | nan     | 0.8300 ± 0.0000 | 0.8252 ± 0.0000 |        3 |
| mango  | clip_b    | cls       | proto  |      1 | bn      | 0.8620 ± 0.0020 | 0.8611 ± 0.0020 |        3 |
| mango  | clip_b    | cls       | proto  |      1 | nan     | 0.8300 ± 0.0020 | 0.8252 ± 0.0022 |        3 |
| mango  | clip_b    | cls       | proto  |      5 | bn      | 0.8727 ± 0.0031 | 0.8718 ± 0.0030 |        3 |
| mango  | clip_b    | cls       | proto  |      5 | nan     | 0.8547 ± 0.0064 | 0.8516 ± 0.0069 |        3 |
| mango  | clip_b    | cls       | proto  |     10 | bn      | 0.8780 ± 0.0092 | 0.8771 ± 0.0093 |        3 |
| mango  | clip_b    | cls       | proto  |     10 | nan     | 0.8700 ± 0.0053 | 0.8679 ± 0.0055 |        3 |
| mango  | dinov2_b  | cls       | linear |      0 | bn      | 0.8860 ± 0.0000 | 0.8845 ± 0.0000 |        3 |
| mango  | dinov2_b  | cls       | linear |      0 | nan     | 0.9080 ± 0.0000 | 0.9072 ± 0.0000 |        3 |
| mango  | dinov2_b  | cls       | linear |      1 | bn      | 0.8927 ± 0.0023 | 0.8914 ± 0.0024 |        3 |
| mango  | dinov2_b  | cls       | linear |      1 | nan     | 0.9107 ± 0.0012 | 0.9099 ± 0.0012 |        3 |
| mango  | dinov2_b  | cls       | linear |      5 | bn      | 0.9080 ± 0.0131 | 0.9072 ± 0.0135 |        3 |
| mango  | dinov2_b  | cls       | linear |      5 | nan     | 0.9233 ± 0.0081 | 0.9229 ± 0.0082 |        3 |
| mango  | dinov2_b  | cls       | linear |     10 | bn      | 0.9320 ± 0.0104 | 0.9317 ± 0.0106 |        3 |
| mango  | dinov2_b  | cls       | linear |     10 | nan     | 0.9473 ± 0.0064 | 0.9472 ± 0.0065 |        3 |
| mango  | dinov2_b  | cls       | proto  |      0 | bn      | 0.9160 ± 0.0000 | 0.9154 ± 0.0000 |        3 |
| mango  | dinov2_b  | cls       | proto  |      0 | nan     | 0.9600 ± 0.0000 | 0.9599 ± 0.0000 |        3 |
| mango  | dinov2_b  | cls       | proto  |      1 | bn      | 0.9180 ± 0.0035 | 0.9174 ± 0.0035 |        3 |
| mango  | dinov2_b  | cls       | proto  |      1 | nan     | 0.9607 ± 0.0012 | 0.9606 ± 0.0012 |        3 |
| mango  | dinov2_b  | cls       | proto  |      5 | bn      | 0.9280 ± 0.0035 | 0.9276 ± 0.0035 |        3 |
| mango  | dinov2_b  | cls       | proto  |      5 | nan     | 0.9680 ± 0.0053 | 0.9680 ± 0.0053 |        3 |
| mango  | dinov2_b  | cls       | proto  |     10 | bn      | 0.9360 ± 0.0040 | 0.9357 ± 0.0040 |        3 |
| mango  | dinov2_b  | cls       | proto  |     10 | nan     | 0.9747 ± 0.0031 | 0.9746 ± 0.0031 |        3 |
| mango  | dinov2_s  | cls       | linear |      0 | bn      | 0.8640 ± 0.0000 | 0.8616 ± 0.0000 |        3 |
| mango  | dinov2_s  | cls       | linear |      0 | nan     | 0.9000 ± 0.0000 | 0.8991 ± 0.0000 |        3 |
| mango  | dinov2_s  | cls       | linear |      1 | bn      | 0.8660 ± 0.0053 | 0.8637 ± 0.0056 |        3 |
| mango  | dinov2_s  | cls       | linear |      1 | nan     | 0.9033 ± 0.0095 | 0.9025 ± 0.0097 |        3 |
| mango  | dinov2_s  | cls       | linear |      5 | bn      | 0.8707 ± 0.0061 | 0.8685 ± 0.0065 |        3 |
| mango  | dinov2_s  | cls       | linear |      5 | nan     | 0.9020 ± 0.0111 | 0.9011 ± 0.0115 |        3 |
| mango  | dinov2_s  | cls       | linear |     10 | bn      | 0.9000 ± 0.0131 | 0.8990 ± 0.0136 |        3 |
| mango  | dinov2_s  | cls       | linear |     10 | nan     | 0.9253 ± 0.0046 | 0.9249 ± 0.0047 |        3 |
| mango  | dinov2_s  | cls       | proto  |      0 | bn      | 0.8880 ± 0.0000 | 0.8866 ± 0.0000 |        3 |
| mango  | dinov2_s  | cls       | proto  |      0 | nan     | 0.9500 ± 0.0000 | 0.9499 ± 0.0000 |        3 |
| mango  | dinov2_s  | cls       | proto  |      1 | bn      | 0.8940 ± 0.0020 | 0.8928 ± 0.0021 |        3 |
| mango  | dinov2_s  | cls       | proto  |      1 | nan     | 0.9520 ± 0.0000 | 0.9519 ± 0.0000 |        3 |
| mango  | dinov2_s  | cls       | proto  |      5 | bn      | 0.9047 ± 0.0050 | 0.9038 ± 0.0052 |        3 |
| mango  | dinov2_s  | cls       | proto  |      5 | nan     | 0.9600 ± 0.0020 | 0.9599 ± 0.0020 |        3 |
| mango  | dinov2_s  | cls       | proto  |     10 | bn      | 0.9120 ± 0.0020 | 0.9113 ± 0.0020 |        3 |
| mango  | dinov2_s  | cls       | proto  |     10 | nan     | 0.9647 ± 0.0023 | 0.9646 ± 0.0023 |        3 |
| mango  | resnet50  | cls       | linear |      0 | bn      | 0.5460 ± 0.0000 | 0.4543 ± 0.0000 |        3 |
| mango  | resnet50  | cls       | linear |      0 | nan     | 0.5540 ± 0.0000 | 0.4680 ± 0.0000 |        3 |
| mango  | resnet50  | cls       | linear |      1 | bn      | 0.5527 ± 0.0031 | 0.4704 ± 0.0045 |        3 |
| mango  | resnet50  | cls       | linear |      1 | nan     | 0.5640 ± 0.0040 | 0.4867 ± 0.0066 |        3 |
| mango  | resnet50  | cls       | linear |      5 | bn      | 0.5987 ± 0.0234 | 0.5495 ± 0.0305 |        3 |
| mango  | resnet50  | cls       | linear |      5 | nan     | 0.6333 ± 0.0219 | 0.5926 ± 0.0300 |        3 |
| mango  | resnet50  | cls       | linear |     10 | bn      | 0.6700 ± 0.0472 | 0.6472 ± 0.0575 |        3 |
| mango  | resnet50  | cls       | linear |     10 | nan     | 0.7140 ± 0.0295 | 0.6990 ± 0.0335 |        3 |
| mango  | resnet50  | cls       | proto  |      0 | bn      | 0.6920 ± 0.0000 | 0.6920 ± 0.0000 |        3 |
| mango  | resnet50  | cls       | proto  |      0 | nan     | 0.7200 ± 0.0000 | 0.7180 ± 0.0000 |        3 |
| mango  | resnet50  | cls       | proto  |      1 | bn      | 0.7027 ± 0.0031 | 0.7026 ± 0.0031 |        3 |
| mango  | resnet50  | cls       | proto  |      1 | nan     | 0.7300 ± 0.0020 | 0.7286 ± 0.0021 |        3 |
| mango  | resnet50  | cls       | proto  |      5 | bn      | 0.7220 ± 0.0106 | 0.7220 ± 0.0105 |        3 |
| mango  | resnet50  | cls       | proto  |      5 | nan     | 0.7593 ± 0.0023 | 0.7586 ± 0.0025 |        3 |
| mango  | resnet50  | cls       | proto  |     10 | bn      | 0.7447 ± 0.0223 | 0.7446 ± 0.0223 |        3 |
| mango  | resnet50  | cls       | proto  |     10 | nan     | 0.7840 ± 0.0140 | 0.7839 ± 0.0139 |        3 |

## Paired tests: DINOv2-S vs ResNet-50 (linear head, macro-F1, paired by seed)

| view           |   shot |   n_pairs |   mean_diff_dinov2_minus_resnet |    sd_diff |         t |           p |   p_bonferroni |    p_holm | survives_bonferroni_0.05   |   n_tests_in_family |
|:---------------|-------:|----------:|--------------------------------:|-----------:|----------:|------------:|---------------:|----------:|:---------------------------|--------------------:|
| banana3        |      1 |         5 |                      0.0456064  | 0.0563394  |  1.81008  | 0.144533    |      1         | 1         | False                      |                  40 |
| banana3        |      5 |         5 |                      0.128247   | 0.0638177  |  4.49355  | 0.0108762   |      0.435047  | 0.337161  | False                      |                  40 |
| banana3        |     10 |         5 |                      0.0965976  | 0.0446567  |  4.83687  | 0.00841917  |      0.336767  | 0.277833  | False                      |                  40 |
| banana3        |     50 |         5 |                      0.109433   | 0.0274575  |  8.91193  | 0.000876316 |      0.0350526 | 0.0350526 | True                       |                  40 |
| banana4        |      1 |         5 |                      0.120438   | 0.0400048  |  6.73189  | 0.00253671  |      0.101468  | 0.0989317 | False                      |                  40 |
| banana4        |      5 |         5 |                      0.16014    | 0.0659338  |  5.43096  | 0.00557633  |      0.223053  | 0.200748  | False                      |                  40 |
| banana4        |     10 |         5 |                      0.142212   | 0.0510696  |  6.22671  | 0.00338767  |      0.135507  | 0.128732  | False                      |                  40 |
| banana4        |     50 |         5 |                      0.082554   | 0.0400099  |  4.61377  | 0.00992748  |      0.397099  | 0.317679  | False                      |                  40 |
| field4_banana  |      1 |         5 |                     -0.19649    | 0.133548   | -3.28994  | 0.0302171   |      1         | 0.815863  | False                      |                  40 |
| field4_banana  |      5 |         5 |                     -0.0723549  | 0.0950555  | -1.70206  | 0.163958    |      1         | 1         | False                      |                  40 |
| field4_banana  |     10 |         5 |                      0.0654597  | 0.0296071  |  4.94383  | 0.00779541  |      0.311817  | 0.265044  | False                      |                  40 |
| field4_banana  |     50 |         5 |                      0.0462107  | 0.0352565  |  2.93081  | 0.0427791   |      1         | 1         | False                      |                  40 |
| field4_mango   |      1 |         5 |                      0.107465   | 0.0693761  |  3.46371  | 0.0257305   |      1         | 0.746185  | False                      |                  40 |
| field4_mango   |      5 |         5 |                      0.0405884  | 0.0311236  |  2.91607  | 0.0434138   |      1         | 1         | False                      |                  40 |
| field4_mango   |     10 |         5 |                      0.0281418  | 0.0306839  |  2.05082  | 0.109589    |      1         | 1         | False                      |                  40 |
| field4_mango   |     50 |         5 |                      0.0108026  | 0.00701708 |  3.44237  | 0.0262368   |      1         | 0.746185  | False                      |                  40 |
| fruit12_apple  |      1 |         5 |                      0.0968025  | 0.0946516  |  2.28688  | 0.0841457   |      1         | 1         | False                      |                  40 |
| fruit12_apple  |      5 |         5 |                      0.029093   | 0.0358429  |  1.81497  | 0.143714    |      1         | 1         | False                      |                  40 |
| fruit12_apple  |     10 |         5 |                      0.0332312  | 0.0369976  |  2.00843  | 0.115005    |      1         | 1         | False                      |                  40 |
| fruit12_apple  |     50 |         5 |                      0.0415643  | 0.0175633  |  5.29174  | 0.00612128  |      0.244851  | 0.214245  | False                      |                  40 |
| fruit12_banana |      1 |         5 |                      0.0335274  | 0.0728007  |  1.02979  | 0.361301    |      1         | 1         | False                      |                  40 |
| fruit12_banana |      5 |         5 |                      0.105868   | 0.0738454  |  3.20572  | 0.032722    |      1         | 0.850772  | False                      |                  40 |
| fruit12_banana |     10 |         5 |                      0.0970304  | 0.0790673  |  2.74407  | 0.0516884   |      1         | 1         | False                      |                  40 |
| fruit12_banana |     50 |         5 |                      0.0514449  | 0.0191332  |  6.01229  | 0.00385353  |      0.154141  | 0.142581  | False                      |                  40 |
| fruit12_mango  |      1 |         5 |                      0.0474898  | 0.098567   |  1.07734  | 0.341965    |      1         | 1         | False                      |                  40 |
| fruit12_mango  |      5 |         5 |                      0.0297555  | 0.0825274  |  0.80622  | 0.465317    |      1         | 1         | False                      |                  40 |
| fruit12_mango  |     10 |         5 |                      0.0406519  | 0.052394   |  1.73494  | 0.157769    |      1         | 1         | False                      |                  40 |
| fruit12_mango  |     50 |         5 |                      0.0308881  | 0.0238255  |  2.8989   | 0.0441665   |      1         | 1         | False                      |                  40 |
| mango_khir     |      1 |         5 |                      0.0913651  | 0.100033   |  2.04231  | 0.110653    |      1         | 1         | False                      |                  40 |
| mango_khir     |      5 |         5 |                      0.109446   | 0.160209   |  1.52756  | 0.201337    |      1         | 1         | False                      |                  40 |
| mango_khir     |     10 |         5 |                      0.0642696  | 0.0930455  |  1.54453  | 0.197345    |      1         | 1         | False                      |                  40 |
| mango_khir     |     50 |         5 |                     -0.0143371  | 0.0147194  | -2.17799  | 0.0949572   |      1         | 1         | False                      |                  40 |
| ninepeach      |      1 |         5 |                     -0.0137348  | 0.114421   | -0.268412 | 0.801657    |      1         | 1         | False                      |                  40 |
| ninepeach      |      5 |         5 |                      0.0199641  | 0.0506451  |  0.881449 | 0.427856    |      1         | 1         | False                      |                  40 |
| ninepeach      |     10 |         5 |                      0.0294721  | 0.0219287  |  3.00526  | 0.0397355   |      1         | 0.993387  | False                      |                  40 |
| ninepeach      |     50 |         5 |                      0.0248594  | 0.0136478  |  4.07299  | 0.0151856   |      0.607424  | 0.455568  | False                      |                  40 |
| raspgrade      |      1 |         5 |                      0.0246959  | 0.0540106  |  1.02242  | 0.364381    |      1         | 1         | False                      |                  40 |
| raspgrade      |      5 |         5 |                      0.00878635 | 0.0314762  |  0.624181 | 0.566343    |      1         | 1         | False                      |                  40 |
| raspgrade      |     10 |         5 |                      0.00921883 | 0.0333269  |  0.618537 | 0.569705    |      1         | 1         | False                      |                  40 |
| raspgrade      |     50 |         5 |                     -0.00193298 | 0.0253316  | -0.170628 | 0.872799    |      1         | 1         | False                      |                  40 |

`n_tests_in_family` is the size of this family (40). Raw p is corrected twice (Bonferroni and Holm); the verdict column is the strict one. **1 of 40 survive Bonferroni at alpha=0.05** -- that count, not the raw p-values, is what a significance statement may cite.

## Calibration arm: per-class thresholds fitted on val

| view           | encoder   | protocol           | score       |   shot | auroc           | oscr_at_fpr5_rule   | ccr_fpr5_before   | ccr_accept_all   | rej_sd_before   | rej_sd_after    | ccr_cal         | fpr_cal         | known_accept_cal   |   n_runs |   classes_no_tau_max | calib_src   |
|:---------------|:----------|:-------------------|:------------|-------:|:----------------|:--------------------|:------------------|:-----------------|:----------------|:----------------|:----------------|:----------------|:-------------------|---------:|---------------------:|:------------|
| banana3        | dinov2_s  | P1_out_of_grade    | energy      |      5 | 0.4934 ± 0.1328 | 0.4227 ± 0.0971     | 0.1042 ± 0.0849   | 0.7649 ± 0.0103  | 0.0136 ± 0.0090 | 0.0147 ± 0.0082 | 0.7351 ± 0.0052 | 0.9697 ± 0.0401 | 0.9464 ± 0.0179    |        3 |                    0 | val         |
| banana3        | dinov2_s  | P1_out_of_grade    | energy      |    nan | 0.3534 ± 0.0000 | 0.3513 ± 0.0000     | 0.0268 ± 0.0000   | 0.9643 ± 0.0000  | 0.0228 ± 0.0000 | 0.0196 ± 0.0000 | 0.9464 ± 0.0000 | 1.0000 ± 0.0000 | 0.9821 ± 0.0000    |        3 |                    0 | val         |
| banana3        | dinov2_s  | P1_out_of_grade    | knn         |      5 | 0.8182 ± 0.0116 | 0.6394 ± 0.0123     | 0.4851 ± 0.0287   | 0.7649 ± 0.0103  | 0.0048 ± 0.0000 | 0.0076 ± 0.0047 | 0.7321 ± 0.0179 | 0.9091 ± 0.0152 | 0.9524 ± 0.0052    |        3 |                    0 | val         |
| banana3        | dinov2_s  | P1_out_of_grade    | knn         |    nan | 0.8678 ± 0.0000 | 0.8447 ± 0.0000     | 0.6607 ± 0.0000   | 0.9643 ± 0.0000  | 0.0048 ± 0.0000 | 0.0132 ± 0.0000 | 0.9196 ± 0.0000 | 0.8030 ± 0.0000 | 0.9464 ± 0.0000    |        3 |                    0 | val         |
| banana3        | dinov2_s  | P1_out_of_grade    | mahalanobis |      5 | 0.8186 ± 0.0157 | 0.6426 ± 0.0081     | 0.5060 ± 0.0136   | 0.7649 ± 0.0103  | 0.0076 ± 0.0048 | 0.0077 ± 0.0046 | 0.7351 ± 0.0136 | 0.9040 ± 0.0487 | 0.9554 ± 0.0000    |        3 |                    0 | val         |
| banana3        | dinov2_s  | P1_out_of_grade    | mahalanobis |    nan | 0.8999 ± 0.0000 | 0.8738 ± 0.0000     | 0.7500 ± 0.0000   | 0.9643 ± 0.0000  | 0.0048 ± 0.0000 | 0.0132 ± 0.0000 | 0.9196 ± 0.0000 | 0.8182 ± 0.0000 | 0.9464 ± 0.0000    |        3 |                    0 | val         |
| banana3        | dinov2_s  | P1_out_of_grade    | msp         |      5 | 0.4934 ± 0.1328 | 0.4227 ± 0.0971     | 0.1042 ± 0.0849   | 0.7649 ± 0.0103  | 0.0136 ± 0.0090 | 0.0147 ± 0.0082 | 0.7351 ± 0.0052 | 0.9697 ± 0.0401 | 0.9464 ± 0.0179    |        3 |                    0 | val         |
| banana3        | dinov2_s  | P1_out_of_grade    | msp         |    nan | 0.3534 ± 0.0000 | 0.3513 ± 0.0000     | 0.0268 ± 0.0000   | 0.9643 ± 0.0000  | 0.0228 ± 0.0000 | 0.0196 ± 0.0000 | 0.9464 ± 0.0000 | 1.0000 ± 0.0000 | 0.9821 ± 0.0000    |        3 |                    0 | val         |
| banana3        | dinov2_s  | P2_unseen_interior | energy      |      5 | 0.5317 ± 0.1586 | 0.5120 ± 0.1689     | 0.2036 ± 0.2024   | 0.8793 ± 0.0610  | 0.0194 ± 0.0111 | 0.0170 ± 0.0133 | 0.8458 ± 0.0511 | 0.9024 ± 0.1177 | 0.9307 ± 0.0247    |        6 |                    0 | val         |
| banana3        | dinov2_s  | P2_unseen_interior | energy      |    nan | 0.7042 ± 0.2200 | 0.7001 ± 0.2203     | 0.4467 ± 0.3301   | 0.9668 ± 0.0105  | 0.0502 ± 0.0094 | 0.0600 ± 0.0202 | 0.9254 ± 0.0213 | 0.7793 ± 0.1879 | 0.9383 ± 0.0073    |        6 |                    0 | val         |
| banana3        | dinov2_s  | P2_unseen_interior | knn         |      5 | 0.4169 ± 0.0335 | 0.3873 ± 0.0491     | 0.0629 ± 0.0293   | 0.8793 ± 0.0610  | 0.0091 ± 0.0073 | 0.0105 ± 0.0062 | 0.8605 ± 0.0536 | 0.9460 ± 0.0135 | 0.9620 ± 0.0098    |        6 |                    0 | val         |
| banana3        | dinov2_s  | P2_unseen_interior | knn         |    nan | 0.5469 ± 0.0281 | 0.5424 ± 0.0324     | 0.1310 ± 0.0031   | 0.9668 ± 0.0105  | 0.0258 ± 0.0172 | 0.0284 ± 0.0035 | 0.9461 ± 0.0159 | 0.9264 ± 0.0268 | 0.9589 ± 0.0018    |        6 |                    0 | val         |
| banana3        | dinov2_s  | P2_unseen_interior | mahalanobis |      5 | 0.4778 ± 0.0471 | 0.4491 ± 0.0631     | 0.0882 ± 0.0432   | 0.8793 ± 0.0610  | 0.0163 ± 0.0141 | 0.0139 ± 0.0115 | 0.8549 ± 0.0586 | 0.9422 ± 0.0180 | 0.9522 ± 0.0059    |        6 |                    0 | val         |
| banana3        | dinov2_s  | P2_unseen_interior | mahalanobis |    nan | 0.5754 ± 0.0078 | 0.5704 ± 0.0131     | 0.1413 ± 0.0512   | 0.9668 ± 0.0105  | 0.0336 ± 0.0086 | 0.0325 ± 0.0010 | 0.9422 ± 0.0116 | 0.8806 ± 0.0410 | 0.9550 ± 0.0025    |        6 |                    0 | val         |
| banana3        | dinov2_s  | P2_unseen_interior | msp         |      5 | 0.5317 ± 0.1586 | 0.5120 ± 0.1689     | 0.2036 ± 0.2024   | 0.8793 ± 0.0610  | 0.0194 ± 0.0111 | 0.0170 ± 0.0133 | 0.8458 ± 0.0511 | 0.9024 ± 0.1177 | 0.9307 ± 0.0247    |        6 |                    0 | val         |
| banana3        | dinov2_s  | P2_unseen_interior | msp         |    nan | 0.7042 ± 0.2200 | 0.7001 ± 0.2203     | 0.4467 ± 0.3301   | 0.9668 ± 0.0105  | 0.0502 ± 0.0094 | 0.0551 ± 0.0148 | 0.9254 ± 0.0213 | 0.7793 ± 0.1879 | 0.9425 ± 0.0026    |        6 |                    0 | val         |
| banana3        | resnet50  | P1_out_of_grade    | energy      |      5 | 0.3956 ± 0.1963 | 0.2601 ± 0.1861     | 0.0565 ± 0.0903   | 0.5565 ± 0.1254  | 0.0196 ± 0.0135 | 0.0262 ± 0.0173 | 0.5298 ± 0.1116 | 0.9798 ± 0.0350 | 0.9494 ± 0.0206    |        3 |                    0 | val         |
| banana3        | resnet50  | P1_out_of_grade    | energy      |    nan | 0.7385 ± 0.0000 | 0.6572 ± 0.0000     | 0.3393 ± 0.0000   | 0.8393 ± 0.0000  | 0.0312 ± 0.0000 | 0.0164 ± 0.0000 | 0.8214 ± 0.0000 | 0.9394 ± 0.0000 | 0.9821 ± 0.0000    |        3 |                    0 | val         |
| banana3        | resnet50  | P1_out_of_grade    | knn         |      5 | 0.8403 ± 0.0154 | 0.4673 ± 0.1202     | 0.2887 ± 0.0670   | 0.5565 ± 0.1254  | 0.0108 ± 0.0104 | 0.0195 ± 0.0128 | 0.5149 ± 0.1443 | 0.6061 ± 0.1818 | 0.9167 ± 0.0403    |        3 |                    0 | val         |
| banana3        | resnet50  | P1_out_of_grade    | knn         |    nan | 0.9091 ± 0.0000 | 0.7829 ± 0.0000     | 0.5982 ± 0.0000   | 0.8393 ± 0.0000  | 0.0228 ± 0.0000 | 0.0440 ± 0.0000 | 0.7946 ± 0.0000 | 0.4394 ± 0.0000 | 0.9107 ± 0.0000    |        3 |                    0 | val         |
| banana3        | resnet50  | P1_out_of_grade    | mahalanobis |      5 | 0.8384 ± 0.0211 | 0.4694 ± 0.1227     | 0.3095 ± 0.1267   | 0.5565 ± 0.1254  | 0.0048 ± 0.0000 | 0.0153 ± 0.0164 | 0.5060 ± 0.1301 | 0.6212 ± 0.1364 | 0.9018 ± 0.0389    |        3 |                    0 | val         |
| banana3        | resnet50  | P1_out_of_grade    | mahalanobis |    nan | 0.9393 ± 0.0000 | 0.8048 ± 0.0000     | 0.7589 ± 0.0000   | 0.8393 ± 0.0000  | 0.0228 ± 0.0000 | 0.0342 ± 0.0000 | 0.7946 ± 0.0000 | 0.3636 ± 0.0000 | 0.9196 ± 0.0000    |        3 |                    0 | val         |
| banana3        | resnet50  | P1_out_of_grade    | msp         |      5 | 0.3956 ± 0.1963 | 0.2601 ± 0.1861     | 0.0565 ± 0.0903   | 0.5565 ± 0.1254  | 0.0196 ± 0.0135 | 0.0262 ± 0.0173 | 0.5298 ± 0.1116 | 0.9798 ± 0.0350 | 0.9494 ± 0.0206    |        3 |                    0 | val         |
| banana3        | resnet50  | P1_out_of_grade    | msp         |    nan | 0.7385 ± 0.0000 | 0.6572 ± 0.0000     | 0.3393 ± 0.0000   | 0.8393 ± 0.0000  | 0.0312 ± 0.0000 | 0.0164 ± 0.0000 | 0.8214 ± 0.0000 | 0.9394 ± 0.0000 | 0.9821 ± 0.0000    |        3 |                    0 | val         |
| banana3        | resnet50  | P2_unseen_interior | energy      |      5 | 0.5342 ± 0.1493 | 0.4758 ± 0.1282     | 0.0993 ± 0.0975   | 0.8091 ± 0.0463  | 0.0149 ± 0.0132 | 0.0286 ± 0.0273 | 0.7714 ± 0.0475 | 0.9306 ± 0.0653 | 0.9228 ± 0.0260    |        6 |                    0 | val         |
| banana3        | resnet50  | P2_unseen_interior | energy      |    nan | 0.7581 ± 0.0001 | 0.7361 ± 0.0232     | 0.3668 ± 0.0554   | 0.9405 ± 0.0565  | 0.0171 ± 0.0077 | 0.0145 ± 0.0027 | 0.9205 ± 0.0440 | 0.8952 ± 0.0289 | 0.9714 ± 0.0032    |        6 |                    0 | val         |
| banana3        | resnet50  | P2_unseen_interior | knn         |      5 | 0.3899 ± 0.0642 | 0.3360 ± 0.0593     | 0.0494 ± 0.0532   | 0.8091 ± 0.0463  | 0.0134 ± 0.0085 | 0.0087 ± 0.0116 | 0.7927 ± 0.0497 | 0.9580 ± 0.0290 | 0.9644 ± 0.0100    |        6 |                    0 | val         |
| banana3        | resnet50  | P2_unseen_interior | knn         |    nan | 0.5046 ± 0.0744 | 0.4901 ± 0.0586     | 0.0545 ± 0.0339   | 0.9405 ± 0.0565  | 0.0236 ± 0.0196 | 0.0330 ± 0.0175 | 0.9244 ± 0.0483 | 0.9116 ± 0.0109 | 0.9629 ± 0.0062    |        6 |                    0 | val         |
| banana3        | resnet50  | P2_unseen_interior | mahalanobis |      5 | 0.4467 ± 0.1052 | 0.3943 ± 0.0952     | 0.0720 ± 0.0711   | 0.8091 ± 0.0463  | 0.0148 ± 0.0131 | 0.0155 ± 0.0141 | 0.7884 ± 0.0500 | 0.9263 ± 0.0346 | 0.9532 ± 0.0122    |        6 |                    0 | val         |
| banana3        | resnet50  | P2_unseen_interior | mahalanobis |    nan | 0.5762 ± 0.0836 | 0.5560 ± 0.0615     | 0.1005 ± 0.0584   | 0.9405 ± 0.0565  | 0.0149 ± 0.0101 | 0.0217 ± 0.0134 | 0.9077 ± 0.0580 | 0.8772 ± 0.0271 | 0.9504 ± 0.0112    |        6 |                    0 | val         |
| banana3        | resnet50  | P2_unseen_interior | msp         |      5 | 0.5342 ± 0.1493 | 0.4758 ± 0.1282     | 0.0993 ± 0.0975   | 0.8091 ± 0.0463  | 0.0149 ± 0.0132 | 0.0286 ± 0.0273 | 0.7714 ± 0.0475 | 0.9334 ± 0.0616 | 0.9228 ± 0.0260    |        6 |                    0 | val         |
| banana3        | resnet50  | P2_unseen_interior | msp         |    nan | 0.7581 ± 0.0001 | 0.7361 ± 0.0232     | 0.3668 ± 0.0554   | 0.9405 ± 0.0565  | 0.0171 ± 0.0077 | 0.0183 ± 0.0069 | 0.9244 ± 0.0483 | 0.8952 ± 0.0289 | 0.9754 ± 0.0011    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P1_out_of_grade    | energy      |      5 | 0.6033 ± 0.1805 | 0.5988 ± 0.1785     | 0.2197 ± 0.1702   | 0.9331 ± 0.0662  | 0.0584 ± 0.0090 | 0.0732 ± 0.0454 | 0.8725 ± 0.0539 | 0.7434 ± 0.1533 | 0.8763 ± 0.0504    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P1_out_of_grade    | energy      |    nan | 0.5366 ± 0.0000 | 0.5366 ± 0.0000     | 0.0947 ± 0.0000   | 1.0000 ± 0.0000  | 0.0481 ± 0.0000 | 0.0032 ± 0.0000 | 0.9129 ± 0.0000 | 0.7788 ± 0.0000 | 0.9129 ± 0.0000    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P1_out_of_grade    | knn         |      5 | 0.8036 ± 0.0279 | 0.7464 ± 0.0571     | 0.4141 ± 0.1245   | 0.9331 ± 0.0662  | 0.0420 ± 0.0177 | 0.0063 ± 0.0042 | 0.8902 ± 0.0657 | 0.7581 ± 0.0946 | 0.9558 ± 0.0044    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P1_out_of_grade    | knn         |    nan | 0.9285 ± 0.0000 | 0.9285 ± 0.0000     | 0.7159 ± 0.0000   | 1.0000 ± 0.0000  | 0.0455 ± 0.0000 | 0.0260 ± 0.0000 | 0.9242 ± 0.0000 | 0.3274 ± 0.0000 | 0.9242 ± 0.0000    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P1_out_of_grade    | mahalanobis |      5 | 0.8238 ± 0.0358 | 0.7685 ± 0.0573     | 0.4104 ± 0.0810   | 0.9331 ± 0.0662  | 0.0420 ± 0.0131 | 0.0093 ± 0.0057 | 0.8889 ± 0.0667 | 0.6785 ± 0.1606 | 0.9558 ± 0.0022    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P1_out_of_grade    | mahalanobis |    nan | 0.9132 ± 0.0000 | 0.9132 ± 0.0000     | 0.6742 ± 0.0000   | 1.0000 ± 0.0000  | 0.0377 ± 0.0000 | 0.0260 ± 0.0000 | 0.9242 ± 0.0000 | 0.3805 ± 0.0000 | 0.9242 ± 0.0000    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P1_out_of_grade    | msp         |      5 | 0.6033 ± 0.1805 | 0.5988 ± 0.1785     | 0.2197 ± 0.1702   | 0.9331 ± 0.0662  | 0.0584 ± 0.0090 | 0.0732 ± 0.0454 | 0.8725 ± 0.0539 | 0.7434 ± 0.1533 | 0.8763 ± 0.0504    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P1_out_of_grade    | msp         |    nan | 0.5366 ± 0.0000 | 0.5366 ± 0.0000     | 0.0947 ± 0.0000   | 1.0000 ± 0.0000  | 0.0481 ± 0.0000 | 0.0032 ± 0.0000 | 0.9129 ± 0.0000 | 0.7788 ± 0.0000 | 0.9129 ± 0.0000    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P2_unseen_interior | energy      |      5 | 0.6965 ± 0.2175 | 0.6905 ± 0.2206     | 0.4793 ± 0.2724   | 0.9397 ± 0.0541  | 0.0335 ± 0.0201 | 0.0327 ± 0.0197 | 0.8874 ± 0.0327 | 0.5476 ± 0.4802 | 0.9092 ± 0.0288    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P2_unseen_interior | energy      |    nan | 0.6895 ± 0.3291 | 0.6895 ± 0.3291     | 0.5495 ± 0.4296   | 0.9869 ± 0.0144  | 0.0287 ± 0.0028 | 0.0310 ± 0.0006 | 0.9207 ± 0.0034 | 0.5162 ± 0.5299 | 0.9226 ± 0.0013    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P2_unseen_interior | knn         |      5 | 0.6723 ± 0.1343 | 0.6221 ± 0.0996     | 0.3131 ± 0.1992   | 0.9397 ± 0.0541  | 0.0295 ± 0.0212 | 0.0124 ± 0.0061 | 0.8882 ± 0.0559 | 0.8632 ± 0.0706 | 0.9454 ± 0.0069    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P2_unseen_interior | knn         |    nan | 0.9633 ± 0.0073 | 0.9502 ± 0.0070     | 0.8138 ± 0.0563   | 0.9869 ± 0.0144  | 0.0281 ± 0.0021 | 0.0130 ± 0.0100 | 0.9229 ± 0.0304 | 0.1948 ± 0.0640 | 0.9360 ± 0.0161    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P2_unseen_interior | mahalanobis |      5 | 0.7663 ± 0.0555 | 0.7167 ± 0.0260     | 0.3854 ± 0.1656   | 0.9397 ± 0.0541  | 0.0282 ± 0.0180 | 0.0046 ± 0.0039 | 0.8888 ± 0.0523 | 0.8102 ± 0.0697 | 0.9447 ± 0.0080    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P2_unseen_interior | mahalanobis |    nan | 0.9385 ± 0.0107 | 0.9254 ± 0.0250     | 0.7827 ± 0.0124   | 0.9869 ± 0.0144  | 0.0192 ± 0.0120 | 0.0137 ± 0.0142 | 0.9225 ± 0.0259 | 0.3974 ± 0.0726 | 0.9356 ± 0.0116    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P2_unseen_interior | msp         |      5 | 0.6965 ± 0.2175 | 0.6905 ± 0.2206     | 0.4793 ± 0.2724   | 0.9397 ± 0.0541  | 0.0335 ± 0.0201 | 0.0321 ± 0.0185 | 0.8874 ± 0.0327 | 0.5476 ± 0.4802 | 0.9098 ± 0.0279    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P2_unseen_interior | msp         |    nan | 0.6895 ± 0.3291 | 0.6895 ± 0.3291     | 0.5495 ± 0.4296   | 0.9869 ± 0.0144  | 0.0287 ± 0.0028 | 0.0310 ± 0.0006 | 0.9207 ± 0.0034 | 0.5162 ± 0.5299 | 0.9226 ± 0.0013    |        6 |                    0 | val         |
| banana4        | dinov2_s  | P3_rotten          | energy      |      5 | 0.6023 ± 0.0644 | 0.5780 ± 0.0631     | 0.1636 ± 0.1177   | 0.9266 ± 0.0252  | 0.0386 ± 0.0085 | 0.0184 ± 0.0145 | 0.8939 ± 0.0351 | 0.8775 ± 0.0931 | 0.9514 ± 0.0160    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P3_rotten          | energy      |    nan | 0.8105 ± 0.0000 | 0.8053 ± 0.0000     | 0.1618 ± 0.0000   | 0.9841 ± 0.0000  | 0.0362 ± 0.0000 | 0.0254 ± 0.0000 | 0.9231 ± 0.0000 | 0.5892 ± 0.0000 | 0.9310 ± 0.0000    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P3_rotten          | knn         |      5 | 0.8747 ± 0.0163 | 0.8071 ± 0.0077     | 0.5190 ± 0.0081   | 0.9266 ± 0.0252  | 0.0536 ± 0.0231 | 0.0143 ± 0.0038 | 0.8753 ± 0.0279 | 0.4613 ± 0.0541 | 0.9469 ± 0.0027    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P3_rotten          | knn         |    nan | 0.9789 ± 0.0000 | 0.9631 ± 0.0000     | 0.8833 ± 0.0000   | 0.9841 ± 0.0000  | 0.0441 ± 0.0000 | 0.0229 ± 0.0000 | 0.9151 ± 0.0000 | 0.0486 ± 0.0000 | 0.9310 ± 0.0000    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P3_rotten          | mahalanobis |      5 | 0.8960 ± 0.0268 | 0.8295 ± 0.0148     | 0.5986 ± 0.0523   | 0.9266 ± 0.0252  | 0.0475 ± 0.0136 | 0.0097 ± 0.0045 | 0.8806 ± 0.0287 | 0.4180 ± 0.1073 | 0.9496 ± 0.0096    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P3_rotten          | mahalanobis |    nan | 0.9524 ± 0.0000 | 0.9366 ± 0.0000     | 0.7984 ± 0.0000   | 0.9841 ± 0.0000  | 0.0428 ± 0.0000 | 0.0271 ± 0.0000 | 0.9204 ± 0.0000 | 0.1946 ± 0.0000 | 0.9363 ± 0.0000    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P3_rotten          | msp         |      5 | 0.6581 ± 0.0667 | 0.6399 ± 0.0657     | 0.1645 ± 0.0868   | 0.9266 ± 0.0252  | 0.0385 ± 0.0154 | 0.0155 ± 0.0137 | 0.8948 ± 0.0222 | 0.8541 ± 0.1117 | 0.9487 ± 0.0120    |        3 |                    0 | val         |
| banana4        | dinov2_s  | P3_rotten          | msp         |    nan | 0.8170 ± 0.0000 | 0.8137 ± 0.0000     | 0.1273 ± 0.0000   | 0.9841 ± 0.0000  | 0.0478 ± 0.0000 | 0.0170 ± 0.0000 | 0.9204 ± 0.0000 | 0.6054 ± 0.0000 | 0.9204 ± 0.0000    |        3 |                    0 | val         |
| banana4        | resnet50  | P1_out_of_grade    | energy      |      5 | 0.5211 ± 0.0958 | 0.4579 ± 0.0613     | 0.0960 ± 0.0417   | 0.7891 ± 0.0662  | 0.0403 ± 0.0234 | 0.0610 ± 0.0460 | 0.7538 ± 0.0572 | 0.8584 ± 0.1073 | 0.8864 ± 0.0361    |        3 |                    0 | val         |
| banana4        | resnet50  | P1_out_of_grade    | energy      |    nan | 0.5896 ± 0.0000 | 0.5896 ± 0.0000     | 0.2083 ± 0.0000   | 0.9924 ± 0.0000  | 0.0636 ± 0.0000 | 0.0156 ± 0.0000 | 0.9091 ± 0.0000 | 0.8230 ± 0.0000 | 0.9091 ± 0.0000    |        3 |                    0 | val         |
| banana4        | resnet50  | P1_out_of_grade    | knn         |      5 | 0.7826 ± 0.0330 | 0.6098 ± 0.0698     | 0.2058 ± 0.0831   | 0.7891 ± 0.0662  | 0.0403 ± 0.0270 | 0.0126 ± 0.0071 | 0.7563 ± 0.0468 | 0.5752 ± 0.1763 | 0.9596 ± 0.0246    |        3 |                    0 | val         |
| banana4        | resnet50  | P1_out_of_grade    | knn         |    nan | 0.9123 ± 0.0000 | 0.9056 ± 0.0000     | 0.4659 ± 0.0000   | 0.9924 ± 0.0000  | 0.0013 ± 0.0000 | 0.0110 ± 0.0000 | 0.9508 ± 0.0000 | 0.3274 ± 0.0000 | 0.9583 ± 0.0000    |        3 |                    0 | val         |
| banana4        | resnet50  | P1_out_of_grade    | mahalanobis |      5 | 0.7961 ± 0.0229 | 0.6239 ± 0.0716     | 0.2247 ± 0.0631   | 0.7891 ± 0.0662  | 0.0403 ± 0.0340 | 0.0087 ± 0.0036 | 0.7588 ± 0.0514 | 0.5929 ± 0.1777 | 0.9621 ± 0.0197    |        3 |                    0 | val         |
| banana4        | resnet50  | P1_out_of_grade    | mahalanobis |    nan | 0.8804 ± 0.0000 | 0.8737 ± 0.0000     | 0.4924 ± 0.0000   | 0.9924 ± 0.0000  | 0.0221 ± 0.0000 | 0.0071 ± 0.0000 | 0.9205 ± 0.0000 | 0.4248 ± 0.0000 | 0.9280 ± 0.0000    |        3 |                    0 | val         |
| banana4        | resnet50  | P1_out_of_grade    | msp         |      5 | 0.5211 ± 0.0958 | 0.4579 ± 0.0613     | 0.0960 ± 0.0417   | 0.7891 ± 0.0662  | 0.0403 ± 0.0234 | 0.0610 ± 0.0460 | 0.7538 ± 0.0572 | 0.8584 ± 0.1073 | 0.8864 ± 0.0361    |        3 |                    0 | val         |
| banana4        | resnet50  | P1_out_of_grade    | msp         |    nan | 0.5896 ± 0.0000 | 0.5896 ± 0.0000     | 0.2083 ± 0.0000   | 0.9924 ± 0.0000  | 0.0636 ± 0.0000 | 0.0156 ± 0.0000 | 0.9091 ± 0.0000 | 0.8230 ± 0.0000 | 0.9091 ± 0.0000    |        3 |                    0 | val         |
| banana4        | resnet50  | P2_unseen_interior | energy      |      5 | 0.6675 ± 0.1557 | 0.6374 ± 0.1697     | 0.4027 ± 0.2262   | 0.8709 ± 0.0760  | 0.0369 ± 0.0161 | 0.0593 ± 0.0805 | 0.8198 ± 0.0725 | 0.6688 ± 0.2938 | 0.8791 ± 0.0805    |        6 |                    0 | val         |
| banana4        | resnet50  | P2_unseen_interior | energy      |    nan | 0.7998 ± 0.1937 | 0.7995 ± 0.1941     | 0.6028 ± 0.2583   | 0.9757 ± 0.0267  | 0.0159 ± 0.0084 | 0.0308 ± 0.0056 | 0.9083 ± 0.0022 | 0.5584 ± 0.4837 | 0.9140 ± 0.0040    |        6 |                    0 | val         |
| banana4        | resnet50  | P2_unseen_interior | knn         |      5 | 0.5376 ± 0.1780 | 0.4428 ± 0.1582     | 0.1449 ± 0.0973   | 0.8709 ± 0.0760  | 0.0382 ± 0.0193 | 0.0169 ± 0.0141 | 0.8261 ± 0.0757 | 0.8825 ± 0.1178 | 0.9490 ± 0.0120    |        6 |                    0 | val         |
| banana4        | resnet50  | P2_unseen_interior | knn         |    nan | 0.8824 ± 0.0462 | 0.8588 ± 0.0203     | 0.5302 ± 0.1289   | 0.9757 ± 0.0267  | 0.0154 ± 0.0161 | 0.0129 ± 0.0060 | 0.9446 ± 0.0214 | 0.5136 ± 0.0846 | 0.9690 ± 0.0053    |        6 |                    0 | val         |
| banana4        | resnet50  | P2_unseen_interior | mahalanobis |      5 | 0.6323 ± 0.1487 | 0.5389 ± 0.1318     | 0.1973 ± 0.1570   | 0.8709 ± 0.0760  | 0.0374 ± 0.0221 | 0.0197 ± 0.0236 | 0.8244 ± 0.0838 | 0.8403 ± 0.1266 | 0.9410 ± 0.0249    |        6 |                    0 | val         |
| banana4        | resnet50  | P2_unseen_interior | mahalanobis |    nan | 0.8601 ± 0.0700 | 0.8363 ± 0.0438     | 0.5101 ± 0.2248   | 0.9757 ± 0.0267  | 0.0321 ± 0.0147 | 0.0058 ± 0.0023 | 0.9109 ± 0.0337 | 0.5201 ± 0.0420 | 0.9353 ± 0.0070    |        6 |                    0 | val         |
| banana4        | resnet50  | P2_unseen_interior | msp         |      5 | 0.6675 ± 0.1557 | 0.6374 ± 0.1697     | 0.4027 ± 0.2262   | 0.8709 ± 0.0760  | 0.0369 ± 0.0161 | 0.0593 ± 0.0805 | 0.8198 ± 0.0725 | 0.6688 ± 0.2938 | 0.8791 ± 0.0805    |        6 |                    0 | val         |
| banana4        | resnet50  | P2_unseen_interior | msp         |    nan | 0.7998 ± 0.1937 | 0.7995 ± 0.1941     | 0.6028 ± 0.2583   | 0.9757 ± 0.0267  | 0.0159 ± 0.0084 | 0.0308 ± 0.0056 | 0.9083 ± 0.0022 | 0.5584 ± 0.4837 | 0.9140 ± 0.0040    |        6 |                    0 | val         |
| banana4        | resnet50  | P3_rotten          | energy      |      5 | 0.6593 ± 0.0889 | 0.5461 ± 0.0283     | 0.1813 ± 0.0292   | 0.7816 ± 0.0629  | 0.0156 ± 0.0079 | 0.0227 ± 0.0146 | 0.7577 ± 0.0673 | 0.8829 ± 0.0680 | 0.9408 ± 0.0107    |        3 |                    0 | val         |
| banana4        | resnet50  | P3_rotten          | energy      |    nan | 0.7947 ± 0.0000 | 0.7839 ± 0.0000     | 0.3395 ± 0.0000   | 0.9655 ± 0.0000  | 0.0164 ± 0.0000 | 0.0180 ± 0.0000 | 0.9257 ± 0.0000 | 0.7189 ± 0.0000 | 0.9390 ± 0.0000    |        3 |                    0 | val         |
| banana4        | resnet50  | P3_rotten          | knn         |      5 | 0.7846 ± 0.0268 | 0.5944 ± 0.0773     | 0.2661 ± 0.0589   | 0.7816 ± 0.0629  | 0.0529 ± 0.0292 | 0.0264 ± 0.0122 | 0.7347 ± 0.0608 | 0.6378 ± 0.0715 | 0.9469 ± 0.0053    |        3 |                    0 | val         |
| banana4        | resnet50  | P3_rotten          | knn         |    nan | 0.9574 ± 0.0000 | 0.9234 ± 0.0000     | 0.7851 ± 0.0000   | 0.9655 ± 0.0000  | 0.0224 ± 0.0000 | 0.0151 ± 0.0000 | 0.9310 ± 0.0000 | 0.2432 ± 0.0000 | 0.9655 ± 0.0000    |        3 |                    0 | val         |
| banana4        | resnet50  | P3_rotten          | mahalanobis |      5 | 0.8320 ± 0.0703 | 0.6434 ± 0.1112     | 0.3882 ± 0.1413   | 0.7816 ± 0.0629  | 0.0537 ± 0.0182 | 0.0246 ± 0.0112 | 0.7471 ± 0.0698 | 0.6054 ± 0.1471 | 0.9540 ± 0.0067    |        3 |                    0 | val         |
| banana4        | resnet50  | P3_rotten          | mahalanobis |    nan | 0.9255 ± 0.0000 | 0.8920 ± 0.0000     | 0.6021 ± 0.0000   | 0.9655 ± 0.0000  | 0.0402 ± 0.0000 | 0.0072 ± 0.0000 | 0.8912 ± 0.0000 | 0.3351 ± 0.0000 | 0.9257 ± 0.0000    |        3 |                    0 | val         |
| banana4        | resnet50  | P3_rotten          | msp         |      5 | 0.6550 ± 0.0540 | 0.5551 ± 0.0076     | 0.1963 ± 0.0231   | 0.7816 ± 0.0629  | 0.0293 ± 0.0165 | 0.0228 ± 0.0039 | 0.7489 ± 0.0641 | 0.8775 ± 0.0466 | 0.9302 ± 0.0120    |        3 |                    0 | val         |
| banana4        | resnet50  | P3_rotten          | msp         |    nan | 0.8002 ± 0.0000 | 0.7915 ± 0.0000     | 0.2997 ± 0.0000   | 0.9655 ± 0.0000  | 0.0315 ± 0.0000 | 0.0230 ± 0.0000 | 0.9019 ± 0.0000 | 0.6000 ± 0.0000 | 0.9098 ± 0.0000    |        3 |                    0 | val         |
| f360rot        | dinov2_s  | P3_rotten          | energy      |      5 | 0.8332 ± 0.0099 | 0.6992 ± 0.0070     | 0.5380 ± 0.0459   | 0.8299 ± 0.0053  | 0.0726 ± 0.0025 | 0.0729 ± 0.0048 | 0.7839 ± 0.0063 | 0.7846 ± 0.0615 | 0.9210 ± 0.0053    |        3 |                    1 | val         |
| f360rot        | dinov2_s  | P3_rotten          | energy      |    nan | 0.6025 ± 0.0000 | 0.6005 ± 0.0000     | 0.3214 ± 0.0000   | 0.9884 ± 0.0000  | 0.0706 ± 0.0000 | 0.0361 ± 0.0000 | 0.9227 ± 0.0000 | 0.8231 ± 0.0000 | 0.9299 ± 0.0000    |        3 |                    1 | val         |
| f360rot        | dinov2_s  | P3_rotten          | knn         |      5 | 0.8969 ± 0.0161 | 0.7514 ± 0.0181     | 0.6096 ± 0.0741   | 0.8299 ± 0.0053  | 0.1058 ± 0.0034 | 0.0652 ± 0.0047 | 0.7835 ± 0.0033 | 0.7523 ± 0.0838 | 0.9179 ± 0.0068    |        3 |                    1 | val         |
| f360rot        | dinov2_s  | P3_rotten          | knn         |    nan | 0.8700 ± 0.0000 | 0.8636 ± 0.0000     | 0.6836 ± 0.0000   | 0.9884 ± 0.0000  | 0.0853 ± 0.0000 | 0.0417 ± 0.0000 | 0.9188 ± 0.0000 | 0.7431 ± 0.0000 | 0.9271 ± 0.0000    |        3 |                    1 | val         |
| f360rot        | dinov2_s  | P3_rotten          | mahalanobis |      5 | 0.8779 ± 0.0112 | 0.7457 ± 0.0141     | 0.5605 ± 0.0349   | 0.8299 ± 0.0053  | 0.1140 ± 0.0034 | 0.0609 ± 0.0082 | 0.7837 ± 0.0066 | 0.6067 ± 0.1480 | 0.9168 ± 0.0016    |        3 |                    1 | val         |
| f360rot        | dinov2_s  | P3_rotten          | mahalanobis |    nan | 0.9567 ± 0.0000 | 0.9476 ± 0.0000     | 0.9072 ± 0.0000   | 0.9884 ± 0.0000  | 0.1160 ± 0.0000 | 0.0491 ± 0.0000 | 0.9260 ± 0.0000 | 0.0646 ± 0.0000 | 0.9348 ± 0.0000    |        3 |                    1 | val         |
| f360rot        | dinov2_s  | P3_rotten          | msp         |      5 | 0.5110 ± 0.0079 | 0.4568 ± 0.0057     | 0.2568 ± 0.0414   | 0.8299 ± 0.0053  | 0.0834 ± 0.0057 | 0.0837 ± 0.0028 | 0.7900 ± 0.0098 | 0.8200 ± 0.0529 | 0.8995 ± 0.0025    |        3 |                    1 | val         |
| f360rot        | dinov2_s  | P3_rotten          | msp         |    nan | 0.3516 ± 0.0000 | 0.3516 ± 0.0000     | 0.0768 ± 0.0000   | 0.9884 ± 0.0000  | 0.0682 ± 0.0000 | 0.0371 ± 0.0000 | 0.9348 ± 0.0000 | 0.7908 ± 0.0000 | 0.9376 ± 0.0000    |        3 |                    1 | val         |
| f360rot        | resnet50  | P3_rotten          | energy      |      5 | 0.9081 ± 0.0090 | 0.6853 ± 0.0269     | 0.5408 ± 0.0625   | 0.7508 ± 0.0203  | 0.1102 ± 0.0045 | 0.0711 ± 0.0109 | 0.7062 ± 0.0226 | 0.2918 ± 0.0410 | 0.9067 ± 0.0036    |        3 |                    1 | val         |
| f360rot        | resnet50  | P3_rotten          | energy      |    nan | 0.6717 ± 0.0000 | 0.6494 ± 0.0000     | 0.3009 ± 0.0000   | 0.9503 ± 0.0000  | 0.0651 ± 0.0000 | 0.0396 ± 0.0000 | 0.8945 ± 0.0000 | 0.6538 ± 0.0000 | 0.9321 ± 0.0000    |        3 |                    1 | val         |
| f360rot        | resnet50  | P3_rotten          | knn         |      5 | 0.9077 ± 0.0087 | 0.6896 ± 0.0264     | 0.6021 ± 0.0403   | 0.7508 ± 0.0203  | 0.1250 ± 0.0059 | 0.0749 ± 0.0096 | 0.7123 ± 0.0212 | 0.5390 ± 0.1077 | 0.9155 ± 0.0015    |        3 |                    1 | val         |
| f360rot        | resnet50  | P3_rotten          | knn         |    nan | 0.9582 ± 0.0000 | 0.9167 ± 0.0000     | 0.8564 ± 0.0000   | 0.9503 ± 0.0000  | 0.0783 ± 0.0000 | 0.0405 ± 0.0000 | 0.8990 ± 0.0000 | 0.0108 ± 0.0000 | 0.9365 ± 0.0000    |        3 |                    1 | val         |
| f360rot        | resnet50  | P3_rotten          | mahalanobis |      5 | 0.9088 ± 0.0134 | 0.6961 ± 0.0121     | 0.6190 ± 0.0053   | 0.7508 ± 0.0203  | 0.1081 ± 0.0017 | 0.0769 ± 0.0083 | 0.7138 ± 0.0193 | 0.3877 ± 0.1232 | 0.9129 ± 0.0033    |        3 |                    1 | val         |
| f360rot        | resnet50  | P3_rotten          | mahalanobis |    nan | 0.9630 ± 0.0000 | 0.9167 ± 0.0000     | 0.8592 ± 0.0000   | 0.9503 ± 0.0000  | 0.1297 ± 0.0000 | 0.0665 ± 0.0000 | 0.8763 ± 0.0000 | 0.0400 ± 0.0000 | 0.9172 ± 0.0000    |        3 |                    1 | val         |
| f360rot        | resnet50  | P3_rotten          | msp         |      5 | 0.5536 ± 0.0176 | 0.4574 ± 0.0119     | 0.2496 ± 0.0640   | 0.7508 ± 0.0203  | 0.0852 ± 0.0066 | 0.0811 ± 0.0079 | 0.7130 ± 0.0188 | 0.7200 ± 0.1093 | 0.8877 ± 0.0041    |        3 |                    1 | val         |
| f360rot        | resnet50  | P3_rotten          | msp         |    nan | 0.4005 ± 0.0000 | 0.3985 ± 0.0000     | 0.0812 ± 0.0000   | 0.9503 ± 0.0000  | 0.0648 ± 0.0000 | 0.0429 ± 0.0000 | 0.8967 ± 0.0000 | 0.7369 ± 0.0000 | 0.9255 ± 0.0000    |        3 |                    1 | val         |
| fruit12_apple  | dinov2_s  | P1_out_of_grade    | energy      |      5 | 0.5513 ± 0.0414 | 0.3742 ± 0.0704     | 0.0559 ± 0.0556   | 0.6602 ± 0.1583  | 0.0177 ± 0.0085 | 0.0123 ± 0.0068 | 0.6237 ± 0.1607 | 0.9474 ± 0.0526 | 0.9290 ± 0.0194    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P1_out_of_grade    | energy      |    nan | 0.7161 ± 0.0000 | 0.6337 ± 0.0000     | 0.2903 ± 0.0000   | 0.8323 ± 0.0000  | 0.0230 ± 0.0000 | 0.0345 ± 0.0000 | 0.7871 ± 0.0000 | 0.9298 ± 0.0000 | 0.9226 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P1_out_of_grade    | knn         |      5 | 0.6996 ± 0.0695 | 0.4844 ± 0.1368     | 0.1699 ± 0.1049   | 0.6602 ± 0.1583  | 0.0177 ± 0.0091 | 0.0071 ± 0.0059 | 0.6344 ± 0.1415 | 0.8129 ± 0.1128 | 0.9634 ± 0.0162    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P1_out_of_grade    | knn         |    nan | 0.7331 ± 0.0000 | 0.6241 ± 0.0000     | 0.0645 ± 0.0000   | 0.8323 ± 0.0000  | 0.0223 ± 0.0000 | 0.0352 ± 0.0000 | 0.7871 ± 0.0000 | 0.5789 ± 0.0000 | 0.9097 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P1_out_of_grade    | mahalanobis |      5 | 0.6993 ± 0.0366 | 0.4770 ± 0.1181     | 0.0817 ± 0.0476   | 0.6602 ± 0.1583  | 0.0175 ± 0.0178 | 0.0067 ± 0.0076 | 0.6194 ± 0.1400 | 0.7602 ± 0.1194 | 0.9441 ± 0.0244    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P1_out_of_grade    | mahalanobis |    nan | 0.7461 ± 0.0000 | 0.6298 ± 0.0000     | 0.0645 ± 0.0000   | 0.8323 ± 0.0000  | 0.0072 ± 0.0000 | 0.0061 ± 0.0000 | 0.7742 ± 0.0000 | 0.5965 ± 0.0000 | 0.9290 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P1_out_of_grade    | msp         |      5 | 0.5513 ± 0.0414 | 0.3742 ± 0.0704     | 0.0559 ± 0.0556   | 0.6602 ± 0.1583  | 0.0177 ± 0.0085 | 0.0123 ± 0.0068 | 0.6237 ± 0.1607 | 0.9474 ± 0.0526 | 0.9290 ± 0.0194    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P1_out_of_grade    | msp         |    nan | 0.7161 ± 0.0000 | 0.6337 ± 0.0000     | 0.2903 ± 0.0000   | 0.8323 ± 0.0000  | 0.0230 ± 0.0000 | 0.0345 ± 0.0000 | 0.7871 ± 0.0000 | 0.9298 ± 0.0000 | 0.9226 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P2_unseen_interior | energy      |      5 | 0.5977 ± 0.0920 | 0.4832 ± 0.1082     | 0.2528 ± 0.1323   | 0.6951 ± 0.0556  | 0.0340 ± 0.0161 | 0.0560 ± 0.0358 | 0.6683 ± 0.0688 | 0.8948 ± 0.0939 | 0.9004 ± 0.0689    |        6 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P2_unseen_interior | energy      |    nan | 0.6365 ± 0.1274 | 0.6138 ± 0.1155     | 0.2446 ± 0.1076   | 0.9206 ± 0.0069  | 0.0285 ± 0.0258 | 0.0168 ± 0.0124 | 0.8727 ± 0.0142 | 0.8128 ± 0.0003 | 0.9244 ± 0.0307    |        6 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P2_unseen_interior | knn         |      5 | 0.5389 ± 0.0696 | 0.3844 ± 0.0663     | 0.0669 ± 0.0521   | 0.6951 ± 0.0556  | 0.0415 ± 0.0087 | 0.0503 ± 0.0248 | 0.6285 ± 0.0698 | 0.8708 ± 0.0743 | 0.8826 ± 0.0191    |        6 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P2_unseen_interior | knn         |    nan | 0.6795 ± 0.0844 | 0.6368 ± 0.0688     | 0.1471 ± 0.0476   | 0.9206 ± 0.0069  | 0.0456 ± 0.0077 | 0.0349 ± 0.0062 | 0.8489 ± 0.0119 | 0.8530 ± 0.1154 | 0.9236 ± 0.0102    |        6 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P2_unseen_interior | mahalanobis |      5 | 0.5776 ± 0.0691 | 0.4158 ± 0.0714     | 0.1120 ± 0.0891   | 0.6951 ± 0.0556  | 0.0424 ± 0.0118 | 0.0471 ± 0.0278 | 0.6160 ± 0.0793 | 0.8317 ± 0.1151 | 0.8692 ± 0.0325    |        6 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P2_unseen_interior | mahalanobis |    nan | 0.6713 ± 0.0492 | 0.6309 ± 0.0354     | 0.1335 ± 0.0728   | 0.9206 ± 0.0069  | 0.0456 ± 0.0077 | 0.0370 ± 0.0039 | 0.8459 ± 0.0085 | 0.9091 ± 0.0540 | 0.9175 ± 0.0035    |        6 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P2_unseen_interior | msp         |      5 | 0.5977 ± 0.0920 | 0.4832 ± 0.1082     | 0.2528 ± 0.1323   | 0.6951 ± 0.0556  | 0.0340 ± 0.0161 | 0.0560 ± 0.0358 | 0.6683 ± 0.0688 | 0.8995 ± 0.0909 | 0.9004 ± 0.0689    |        6 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P2_unseen_interior | msp         |    nan | 0.6365 ± 0.1274 | 0.6138 ± 0.1155     | 0.2446 ± 0.1076   | 0.9206 ± 0.0069  | 0.0285 ± 0.0258 | 0.0168 ± 0.0124 | 0.8727 ± 0.0142 | 0.8128 ± 0.0003 | 0.9244 ± 0.0307    |        6 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P3_rotten          | energy      |      5 | 0.5815 ± 0.0462 | 0.3587 ± 0.0885     | 0.0723 ± 0.1212   | 0.5597 ± 0.1126  | 0.0315 ± 0.0256 | 0.0520 ± 0.0289 | 0.5393 ± 0.0994 | 0.7974 ± 0.1198 | 0.9104 ± 0.0245    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P3_rotten          | energy      |    nan | 0.5125 ± 0.0000 | 0.4648 ± 0.0000     | 0.0000 ± 0.0000   | 0.8160 ± 0.0000  | 0.0270 ± 0.0000 | 0.0291 ± 0.0000 | 0.7783 ± 0.0000 | 0.9412 ± 0.0000 | 0.9009 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P3_rotten          | knn         |      5 | 0.7501 ± 0.0212 | 0.4378 ± 0.0887     | 0.2311 ± 0.0340   | 0.5597 ± 0.1126  | 0.0319 ± 0.0079 | 0.0399 ± 0.0183 | 0.5110 ± 0.1225 | 0.6209 ± 0.0742 | 0.8899 ± 0.0448    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P3_rotten          | knn         |    nan | 0.8205 ± 0.0000 | 0.6848 ± 0.0000     | 0.3679 ± 0.0000   | 0.8160 ± 0.0000  | 0.0431 ± 0.0000 | 0.0294 ± 0.0000 | 0.7594 ± 0.0000 | 0.5686 ± 0.0000 | 0.9104 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P3_rotten          | mahalanobis |      5 | 0.7811 ± 0.0091 | 0.4617 ± 0.0909     | 0.2437 ± 0.0136   | 0.5597 ± 0.1126  | 0.0334 ± 0.0051 | 0.0305 ± 0.0181 | 0.5189 ± 0.1145 | 0.6275 ± 0.0196 | 0.9057 ± 0.0250    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P3_rotten          | mahalanobis |    nan | 0.8108 ± 0.0000 | 0.6751 ± 0.0000     | 0.4528 ± 0.0000   | 0.8160 ± 0.0000  | 0.0337 ± 0.0000 | 0.0410 ± 0.0000 | 0.7547 ± 0.0000 | 0.5686 ± 0.0000 | 0.9151 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P3_rotten          | msp         |      5 | 0.5695 ± 0.0398 | 0.3525 ± 0.0572     | 0.0660 ± 0.1103   | 0.5597 ± 0.1126  | 0.0261 ± 0.0068 | 0.0456 ± 0.0215 | 0.5330 ± 0.1062 | 0.7712 ± 0.0742 | 0.9198 ± 0.0236    |        3 |                    0 | val         |
| fruit12_apple  | dinov2_s  | P3_rotten          | msp         |    nan | 0.5014 ± 0.0000 | 0.4556 ± 0.0000     | 0.0047 ± 0.0000   | 0.8160 ± 0.0000  | 0.0441 ± 0.0000 | 0.0407 ± 0.0000 | 0.7877 ± 0.0000 | 0.8627 ± 0.0000 | 0.9151 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P1_out_of_grade    | energy      |      5 | 0.6327 ± 0.0901 | 0.3876 ± 0.0842     | 0.0839 ± 0.0782   | 0.6280 ± 0.1970  | 0.0177 ± 0.0176 | 0.0160 ± 0.0185 | 0.6000 ± 0.1969 | 0.8596 ± 0.2431 | 0.9527 ± 0.0207    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P1_out_of_grade    | energy      |    nan | 0.7337 ± 0.0000 | 0.6658 ± 0.0000     | 0.3613 ± 0.0000   | 0.8710 ± 0.0000  | 0.0230 ± 0.0000 | 0.0126 ± 0.0000 | 0.8452 ± 0.0000 | 0.9649 ± 0.0000 | 0.9548 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P1_out_of_grade    | knn         |      5 | 0.6924 ± 0.0784 | 0.4567 ± 0.1615     | 0.1118 ± 0.0742   | 0.6280 ± 0.1970  | 0.0125 ± 0.0085 | 0.0206 ± 0.0090 | 0.5892 ± 0.1742 | 0.7076 ± 0.0791 | 0.9226 ± 0.0171    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P1_out_of_grade    | knn         |    nan | 0.7301 ± 0.0000 | 0.6415 ± 0.0000     | 0.0645 ± 0.0000   | 0.8710 ± 0.0000  | 0.0374 ± 0.0000 | 0.0363 ± 0.0000 | 0.8000 ± 0.0000 | 0.6667 ± 0.0000 | 0.9290 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P1_out_of_grade    | mahalanobis |      5 | 0.6964 ± 0.0102 | 0.4483 ± 0.1325     | 0.0602 ± 0.0099   | 0.6280 ± 0.1970  | 0.0227 ± 0.0148 | 0.0266 ± 0.0186 | 0.5871 ± 0.1718 | 0.6784 ± 0.0829 | 0.9097 ± 0.0171    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P1_out_of_grade    | mahalanobis |    nan | 0.7520 ± 0.0000 | 0.6601 ± 0.0000     | 0.0774 ± 0.0000   | 0.8710 ± 0.0000  | 0.0223 ± 0.0000 | 0.0327 ± 0.0000 | 0.8258 ± 0.0000 | 0.6491 ± 0.0000 | 0.9548 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P1_out_of_grade    | msp         |      5 | 0.6327 ± 0.0901 | 0.3876 ± 0.0842     | 0.0839 ± 0.0782   | 0.6280 ± 0.1970  | 0.0177 ± 0.0176 | 0.0160 ± 0.0185 | 0.6000 ± 0.1969 | 0.8596 ± 0.2431 | 0.9527 ± 0.0207    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P1_out_of_grade    | msp         |    nan | 0.7337 ± 0.0000 | 0.6658 ± 0.0000     | 0.3613 ± 0.0000   | 0.8710 ± 0.0000  | 0.0230 ± 0.0000 | 0.0126 ± 0.0000 | 0.8452 ± 0.0000 | 0.9649 ± 0.0000 | 0.9548 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P2_unseen_interior | energy      |      5 | 0.5703 ± 0.0855 | 0.4472 ± 0.0970     | 0.1571 ± 0.0586   | 0.7001 ± 0.1064  | 0.0237 ± 0.0215 | 0.0175 ± 0.0188 | 0.6614 ± 0.1179 | 0.8946 ± 0.0918 | 0.9142 ± 0.0646    |        6 |                    0 | val         |
| fruit12_apple  | resnet50  | P2_unseen_interior | energy      |    nan | 0.6374 ± 0.1318 | 0.6104 ± 0.1196     | 0.3566 ± 0.1101   | 0.9036 ± 0.0013  | 0.0352 ± 0.0332 | 0.0527 ± 0.0127 | 0.8346 ± 0.0275 | 0.8311 ± 0.0709 | 0.8828 ± 0.0281    |        6 |                    0 | val         |
| fruit12_apple  | resnet50  | P2_unseen_interior | knn         |      5 | 0.5489 ± 0.0920 | 0.3976 ± 0.0539     | 0.0363 ± 0.0298   | 0.7001 ± 0.1064  | 0.0328 ± 0.0094 | 0.0514 ± 0.0273 | 0.6326 ± 0.1094 | 0.7798 ± 0.1408 | 0.8753 ± 0.0272    |        6 |                    0 | val         |
| fruit12_apple  | resnet50  | P2_unseen_interior | knn         |    nan | 0.6933 ± 0.1135 | 0.6456 ± 0.1012     | 0.1774 ± 0.0874   | 0.9036 ± 0.0013  | 0.0389 ± 0.0150 | 0.0480 ± 0.0321 | 0.8181 ± 0.0011 | 0.8099 ± 0.1398 | 0.8897 ± 0.0061    |        6 |                    0 | val         |
| fruit12_apple  | resnet50  | P2_unseen_interior | mahalanobis |      5 | 0.6140 ± 0.0890 | 0.4508 ± 0.0804     | 0.1132 ± 0.1019   | 0.7001 ± 0.1064  | 0.0437 ± 0.0095 | 0.0473 ± 0.0376 | 0.6358 ± 0.0976 | 0.8033 ± 0.0824 | 0.8741 ± 0.0331    |        6 |                    0 | val         |
| fruit12_apple  | resnet50  | P2_unseen_interior | mahalanobis |    nan | 0.7223 ± 0.0676 | 0.6722 ± 0.0641     | 0.1733 ± 0.1231   | 0.9036 ± 0.0013  | 0.0389 ± 0.0150 | 0.0343 ± 0.0164 | 0.8367 ± 0.0015 | 0.7984 ± 0.1068 | 0.9036 ± 0.0013    |        6 |                    0 | val         |
| fruit12_apple  | resnet50  | P2_unseen_interior | msp         |      5 | 0.5703 ± 0.0855 | 0.4472 ± 0.0970     | 0.1571 ± 0.0586   | 0.7001 ± 0.1064  | 0.0237 ± 0.0215 | 0.0175 ± 0.0188 | 0.6614 ± 0.1179 | 0.8946 ± 0.0918 | 0.9142 ± 0.0646    |        6 |                    0 | val         |
| fruit12_apple  | resnet50  | P2_unseen_interior | msp         |    nan | 0.6374 ± 0.1318 | 0.6104 ± 0.1196     | 0.3566 ± 0.1101   | 0.9036 ± 0.0013  | 0.0352 ± 0.0332 | 0.0519 ± 0.0136 | 0.8394 ± 0.0223 | 0.8358 ± 0.0658 | 0.8924 ± 0.0177    |        6 |                    0 | val         |
| fruit12_apple  | resnet50  | P3_rotten          | energy      |      5 | 0.6215 ± 0.0490 | 0.3192 ± 0.0780     | 0.0991 ± 0.1043   | 0.4969 ± 0.0708  | 0.0362 ± 0.0060 | 0.0284 ± 0.0057 | 0.4780 ± 0.0849 | 0.8301 ± 0.1115 | 0.9481 ± 0.0142    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P3_rotten          | energy      |    nan | 0.6438 ± 0.0000 | 0.5793 ± 0.0000     | 0.2028 ± 0.0000   | 0.8491 ± 0.0000  | 0.0351 ± 0.0000 | 0.0229 ± 0.0000 | 0.8113 ± 0.0000 | 0.9216 ± 0.0000 | 0.9198 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P3_rotten          | knn         |      5 | 0.6599 ± 0.0080 | 0.3308 ± 0.0619     | 0.0959 ± 0.0586   | 0.4969 ± 0.0708  | 0.0365 ± 0.0000 | 0.0365 ± 0.0100 | 0.4575 ± 0.0779 | 0.8105 ± 0.0927 | 0.9135 ± 0.0119    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P3_rotten          | knn         |    nan | 0.8189 ± 0.0000 | 0.7134 ± 0.0000     | 0.5094 ± 0.0000   | 0.8491 ± 0.0000  | 0.0363 ± 0.0000 | 0.0407 ± 0.0000 | 0.7783 ± 0.0000 | 0.5490 ± 0.0000 | 0.9009 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P3_rotten          | mahalanobis |      5 | 0.7259 ± 0.0321 | 0.3832 ± 0.0457     | 0.2013 ± 0.0284   | 0.4969 ± 0.0708  | 0.0377 ± 0.0048 | 0.0290 ± 0.0127 | 0.4638 ± 0.0826 | 0.8039 ± 0.0855 | 0.9167 ± 0.0027    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P3_rotten          | mahalanobis |    nan | 0.8343 ± 0.0000 | 0.7235 ± 0.0000     | 0.4340 ± 0.0000   | 0.8491 ± 0.0000  | 0.0363 ± 0.0000 | 0.0475 ± 0.0000 | 0.7736 ± 0.0000 | 0.4706 ± 0.0000 | 0.9009 ± 0.0000    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P3_rotten          | msp         |      5 | 0.6334 ± 0.0372 | 0.3296 ± 0.0455     | 0.1258 ± 0.0684   | 0.4969 ± 0.0708  | 0.0211 ± 0.0152 | 0.0331 ± 0.0240 | 0.4748 ± 0.0849 | 0.8105 ± 0.0884 | 0.9418 ± 0.0276    |        3 |                    0 | val         |
| fruit12_apple  | resnet50  | P3_rotten          | msp         |    nan | 0.6465 ± 0.0000 | 0.5871 ± 0.0000     | 0.1745 ± 0.0000   | 0.8491 ± 0.0000  | 0.0414 ± 0.0000 | 0.0229 ± 0.0000 | 0.8066 ± 0.0000 | 0.9412 ± 0.0000 | 0.9198 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P1_out_of_grade    | energy      |      5 | 0.6040 ± 0.0352 | 0.5056 ± 0.0259     | 0.1844 ± 0.0548   | 0.7662 ± 0.0392  | 0.0161 ± 0.0145 | 0.0212 ± 0.0186 | 0.7422 ± 0.0322 | 0.8667 ± 0.0385 | 0.9312 ± 0.0285    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P1_out_of_grade    | energy      |    nan | 0.8562 ± 0.0000 | 0.8374 ± 0.0000     | 0.5582 ± 0.0000   | 0.9595 ± 0.0000  | 0.0629 ± 0.0000 | 0.0299 ± 0.0000 | 0.9329 ± 0.0000 | 0.6444 ± 0.0000 | 0.9519 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P1_out_of_grade    | knn         |      5 | 0.7342 ± 0.0193 | 0.5750 ± 0.0383     | 0.1827 ± 0.0279   | 0.7662 ± 0.0392  | 0.0096 ± 0.0053 | 0.0124 ± 0.0019 | 0.7257 ± 0.0552 | 0.7259 ± 0.0642 | 0.9359 ± 0.0148    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P1_out_of_grade    | knn         |    nan | 0.8321 ± 0.0000 | 0.8083 ± 0.0000     | 0.5038 ± 0.0000   | 0.9595 ± 0.0000  | 0.0034 ± 0.0000 | 0.0161 ± 0.0000 | 0.9203 ± 0.0000 | 0.4889 ± 0.0000 | 0.9494 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P1_out_of_grade    | mahalanobis |      5 | 0.7617 ± 0.0078 | 0.6021 ± 0.0549     | 0.2658 ± 0.0648   | 0.7662 ± 0.0392  | 0.0106 ± 0.0096 | 0.0131 ± 0.0099 | 0.7291 ± 0.0483 | 0.7037 ± 0.0679 | 0.9354 ± 0.0088    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P1_out_of_grade    | mahalanobis |    nan | 0.8649 ± 0.0000 | 0.8393 ± 0.0000     | 0.5278 ± 0.0000   | 0.9595 ± 0.0000  | 0.0060 ± 0.0000 | 0.0090 ± 0.0000 | 0.9101 ± 0.0000 | 0.4889 ± 0.0000 | 0.9367 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P1_out_of_grade    | msp         |      5 | 0.6040 ± 0.0352 | 0.5056 ± 0.0259     | 0.1844 ± 0.0548   | 0.7662 ± 0.0392  | 0.0161 ± 0.0145 | 0.0212 ± 0.0186 | 0.7422 ± 0.0322 | 0.8667 ± 0.0385 | 0.9312 ± 0.0285    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P1_out_of_grade    | msp         |    nan | 0.8562 ± 0.0000 | 0.8374 ± 0.0000     | 0.5582 ± 0.0000   | 0.9595 ± 0.0000  | 0.0629 ± 0.0000 | 0.0299 ± 0.0000 | 0.9329 ± 0.0000 | 0.6444 ± 0.0000 | 0.9519 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P2_unseen_interior | energy      |      5 | 0.6362 ± 0.0571 | 0.5364 ± 0.0930     | 0.1791 ± 0.0709   | 0.7847 ± 0.1074  | 0.0258 ± 0.0246 | 0.0240 ± 0.0254 | 0.7576 ± 0.0992 | 0.9129 ± 0.0623 | 0.9539 ± 0.0193    |        6 |                    0 | val         |
| fruit12_banana | dinov2_s  | P2_unseen_interior | energy      |    nan | 0.7866 ± 0.0647 | 0.7798 ± 0.0644     | 0.4167 ± 0.1037   | 0.9586 ± 0.0044  | 0.1873 ± 0.0934 | 0.1685 ± 0.0349 | 0.8920 ± 0.0311 | 0.6008 ± 0.1380 | 0.8991 ± 0.0305    |        6 |                    0 | val         |
| fruit12_banana | dinov2_s  | P2_unseen_interior | knn         |      5 | 0.5372 ± 0.0385 | 0.4695 ± 0.0670     | 0.1448 ± 0.1222   | 0.7847 ± 0.1074  | 0.0608 ± 0.0182 | 0.0410 ± 0.0035 | 0.7620 ± 0.1008 | 0.9589 ± 0.0174 | 0.9610 ± 0.0164    |        6 |                    0 | val         |
| fruit12_banana | dinov2_s  | P2_unseen_interior | knn         |    nan | 0.7259 ± 0.0255 | 0.7060 ± 0.0227     | 0.3953 ± 0.0525   | 0.9586 ± 0.0044  | 0.1093 ± 0.0081 | 0.0523 ± 0.0186 | 0.9199 ± 0.0172 | 0.8146 ± 0.0420 | 0.9491 ± 0.0225    |        6 |                    0 | val         |
| fruit12_banana | dinov2_s  | P2_unseen_interior | mahalanobis |      5 | 0.5690 ± 0.0433 | 0.4978 ± 0.0794     | 0.1908 ± 0.1280   | 0.7847 ± 0.1074  | 0.0441 ± 0.0193 | 0.0326 ± 0.0169 | 0.7578 ± 0.1030 | 0.9381 ± 0.0318 | 0.9451 ± 0.0215    |        6 |                    0 | val         |
| fruit12_banana | dinov2_s  | P2_unseen_interior | mahalanobis |    nan | 0.7128 ± 0.0129 | 0.6935 ± 0.0103     | 0.3931 ± 0.0714   | 0.9586 ± 0.0044  | 0.1093 ± 0.0081 | 0.0716 ± 0.0107 | 0.9085 ± 0.0047 | 0.8686 ± 0.0461 | 0.9378 ± 0.0101    |        6 |                    0 | val         |
| fruit12_banana | dinov2_s  | P2_unseen_interior | msp         |      5 | 0.6362 ± 0.0571 | 0.5364 ± 0.0930     | 0.1791 ± 0.0709   | 0.7847 ± 0.1074  | 0.0258 ± 0.0246 | 0.0240 ± 0.0254 | 0.7576 ± 0.0992 | 0.9129 ± 0.0623 | 0.9539 ± 0.0193    |        6 |                    0 | val         |
| fruit12_banana | dinov2_s  | P2_unseen_interior | msp         |    nan | 0.7866 ± 0.0647 | 0.7798 ± 0.0644     | 0.4167 ± 0.1037   | 0.9586 ± 0.0044  | 0.1873 ± 0.0934 | 0.1696 ± 0.0336 | 0.8939 ± 0.0290 | 0.6017 ± 0.1389 | 0.9010 ± 0.0285    |        6 |                    0 | val         |
| fruit12_banana | dinov2_s  | P3_rotten          | energy      |      5 | 0.4468 ± 0.1610 | 0.3186 ± 0.1493     | 0.0683 ± 0.0641   | 0.6511 ± 0.1286  | 0.0428 ± 0.0287 | 0.0424 ± 0.0270 | 0.6311 ± 0.1256 | 0.9184 ± 0.0612 | 0.9190 ± 0.0460    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P3_rotten          | energy      |    nan | 0.7663 ± 0.0000 | 0.7453 ± 0.0000     | 0.3461 ± 0.0000   | 0.9425 ± 0.0000  | 0.1698 ± 0.0000 | 0.0963 ± 0.0000 | 0.9234 ± 0.0000 | 0.8163 ± 0.0000 | 0.9545 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P3_rotten          | knn         |      5 | 0.8093 ± 0.0172 | 0.5556 ± 0.0963     | 0.2567 ± 0.0913   | 0.6511 ± 0.1286  | 0.0828 ± 0.0184 | 0.0436 ± 0.0066 | 0.6331 ± 0.1179 | 0.8163 ± 0.0707 | 0.9613 ± 0.0210    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P3_rotten          | knn         |    nan | 0.8753 ± 0.0000 | 0.8365 ± 0.0000     | 0.5102 ± 0.0000   | 0.9425 ± 0.0000  | 0.1211 ± 0.0000 | 0.0639 ± 0.0000 | 0.9006 ± 0.0000 | 0.7347 ± 0.0000 | 0.9389 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P3_rotten          | mahalanobis |      5 | 0.8290 ± 0.0076 | 0.5690 ± 0.1056     | 0.2782 ± 0.0950   | 0.6511 ± 0.1286  | 0.0858 ± 0.0194 | 0.0508 ± 0.0020 | 0.6359 ± 0.1215 | 0.7891 ± 0.0514 | 0.9609 ± 0.0132    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P3_rotten          | mahalanobis |    nan | 0.9022 ± 0.0000 | 0.8617 ± 0.0000     | 0.6060 ± 0.0000   | 0.9425 ± 0.0000  | 0.1189 ± 0.0000 | 0.0703 ± 0.0000 | 0.8958 ± 0.0000 | 0.6939 ± 0.0000 | 0.9353 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P3_rotten          | msp         |      5 | 0.4390 ± 0.1504 | 0.3196 ± 0.1467     | 0.0383 ± 0.0301   | 0.6511 ± 0.1286  | 0.0431 ± 0.0274 | 0.0306 ± 0.0185 | 0.6347 ± 0.1267 | 0.9184 ± 0.0540 | 0.9269 ± 0.0318    |        3 |                    0 | val         |
| fruit12_banana | dinov2_s  | P3_rotten          | msp         |    nan | 0.7550 ± 0.0000 | 0.7349 ± 0.0000     | 0.2503 ± 0.0000   | 0.9425 ± 0.0000  | 0.1366 ± 0.0000 | 0.0915 ± 0.0000 | 0.9138 ± 0.0000 | 0.8163 ± 0.0000 | 0.9449 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P1_out_of_grade    | energy      |      5 | 0.5547 ± 0.0976 | 0.3342 ± 0.0197     | 0.1025 ± 0.0234   | 0.5713 ± 0.0354  | 0.0094 ± 0.0136 | 0.0150 ± 0.0135 | 0.5451 ± 0.0367 | 0.9481 ± 0.0559 | 0.9456 ± 0.0044    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P1_out_of_grade    | energy      |    nan | 0.7733 ± 0.0000 | 0.7509 ± 0.0000     | 0.1759 ± 0.0000   | 0.9418 ± 0.0000  | 0.0503 ± 0.0000 | 0.0530 ± 0.0000 | 0.8848 ± 0.0000 | 0.7556 ± 0.0000 | 0.9076 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P1_out_of_grade    | knn         |      5 | 0.7449 ± 0.0091 | 0.4524 ± 0.0418     | 0.2266 ± 0.0937   | 0.5713 ± 0.0354  | 0.0062 ± 0.0060 | 0.0063 ± 0.0015 | 0.5481 ± 0.0384 | 0.7407 ± 0.0257 | 0.9574 ± 0.0130    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P1_out_of_grade    | knn         |    nan | 0.8629 ± 0.0000 | 0.8196 ± 0.0000     | 0.5241 ± 0.0000   | 0.9418 ± 0.0000  | 0.0155 ± 0.0000 | 0.0169 ± 0.0000 | 0.9000 ± 0.0000 | 0.5778 ± 0.0000 | 0.9468 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P1_out_of_grade    | mahalanobis |      5 | 0.7866 ± 0.0314 | 0.4693 ± 0.0532     | 0.2603 ± 0.1121   | 0.5713 ± 0.0354  | 0.0071 ± 0.0048 | 0.0124 ± 0.0084 | 0.5460 ± 0.0372 | 0.7185 ± 0.0257 | 0.9494 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P1_out_of_grade    | mahalanobis |    nan | 0.8770 ± 0.0000 | 0.8343 ± 0.0000     | 0.4975 ± 0.0000   | 0.9418 ± 0.0000  | 0.0124 ± 0.0000 | 0.0108 ± 0.0000 | 0.9114 ± 0.0000 | 0.6444 ± 0.0000 | 0.9608 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P1_out_of_grade    | msp         |      5 | 0.5547 ± 0.0976 | 0.3342 ± 0.0197     | 0.1025 ± 0.0234   | 0.5713 ± 0.0354  | 0.0094 ± 0.0136 | 0.0150 ± 0.0135 | 0.5451 ± 0.0367 | 0.9481 ± 0.0559 | 0.9456 ± 0.0044    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P1_out_of_grade    | msp         |    nan | 0.7733 ± 0.0000 | 0.7509 ± 0.0000     | 0.1759 ± 0.0000   | 0.9418 ± 0.0000  | 0.0503 ± 0.0000 | 0.0530 ± 0.0000 | 0.8848 ± 0.0000 | 0.7556 ± 0.0000 | 0.9076 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P2_unseen_interior | energy      |      5 | 0.5356 ± 0.0957 | 0.4019 ± 0.1448     | 0.1116 ± 0.1162   | 0.7023 ± 0.1937  | 0.0062 ± 0.0045 | 0.0108 ± 0.0146 | 0.6697 ± 0.1882 | 0.8990 ± 0.0373 | 0.9369 ± 0.0207    |        6 |                    0 | val         |
| fruit12_banana | resnet50  | P2_unseen_interior | energy      |    nan | 0.7145 ± 0.0879 | 0.7037 ± 0.0893     | 0.2887 ± 0.1586   | 0.9380 ± 0.0234  | 0.1813 ± 0.0868 | 0.1841 ± 0.0395 | 0.8961 ± 0.0356 | 0.7976 ± 0.0184 | 0.9159 ± 0.0282    |        6 |                    0 | val         |
| fruit12_banana | resnet50  | P2_unseen_interior | knn         |      5 | 0.5285 ± 0.0659 | 0.4156 ± 0.1029     | 0.0961 ± 0.0795   | 0.7023 ± 0.1937  | 0.0553 ± 0.0136 | 0.0270 ± 0.0181 | 0.6678 ± 0.1781 | 0.9503 ± 0.0087 | 0.9454 ± 0.0175    |        6 |                    0 | val         |
| fruit12_banana | resnet50  | P2_unseen_interior | knn         |    nan | 0.6983 ± 0.0196 | 0.6653 ± 0.0062     | 0.3025 ± 0.0379   | 0.9380 ± 0.0234  | 0.0833 ± 0.0235 | 0.0124 ± 0.0121 | 0.8866 ± 0.0335 | 0.8170 ± 0.0297 | 0.9451 ± 0.0104    |        6 |                    0 | val         |
| fruit12_banana | resnet50  | P2_unseen_interior | mahalanobis |      5 | 0.5262 ± 0.0598 | 0.4300 ± 0.1014     | 0.1578 ± 0.0713   | 0.7023 ± 0.1937  | 0.0312 ± 0.0218 | 0.0103 ± 0.0063 | 0.6730 ± 0.1774 | 0.9521 ± 0.0204 | 0.9586 ± 0.0208    |        6 |                    0 | val         |
| fruit12_banana | resnet50  | P2_unseen_interior | mahalanobis |    nan | 0.7082 ± 0.0164 | 0.6757 ± 0.0020     | 0.2795 ± 0.0216   | 0.9380 ± 0.0234  | 0.0892 ± 0.0301 | 0.0146 ± 0.0154 | 0.9010 ± 0.0285 | 0.8388 ± 0.0135 | 0.9594 ± 0.0053    |        6 |                    0 | val         |
| fruit12_banana | resnet50  | P2_unseen_interior | msp         |      5 | 0.5356 ± 0.0957 | 0.4019 ± 0.1448     | 0.1116 ± 0.1162   | 0.7023 ± 0.1937  | 0.0062 ± 0.0045 | 0.0108 ± 0.0146 | 0.6697 ± 0.1882 | 0.9001 ± 0.0365 | 0.9369 ± 0.0207    |        6 |                    0 | val         |
| fruit12_banana | resnet50  | P2_unseen_interior | msp         |    nan | 0.7145 ± 0.0879 | 0.7037 ± 0.0893     | 0.2887 ± 0.1586   | 0.9380 ± 0.0234  | 0.1813 ± 0.0868 | 0.1841 ± 0.0395 | 0.8961 ± 0.0356 | 0.7976 ± 0.0184 | 0.9159 ± 0.0282    |        6 |                    0 | val         |
| fruit12_banana | resnet50  | P3_rotten          | energy      |      5 | 0.5033 ± 0.1051 | 0.2974 ± 0.0410     | 0.0263 ± 0.0291   | 0.5345 ± 0.0304  | 0.0184 ± 0.0127 | 0.0271 ± 0.0161 | 0.5194 ± 0.0277 | 0.8980 ± 0.0408 | 0.9433 ± 0.0054    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P3_rotten          | energy      |    nan | 0.8003 ± 0.0000 | 0.7684 ± 0.0000     | 0.4299 ± 0.0000   | 0.9269 ± 0.0000  | 0.1698 ± 0.0000 | 0.1241 ± 0.0000 | 0.8862 ± 0.0000 | 0.7959 ± 0.0000 | 0.9210 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P3_rotten          | knn         |      5 | 0.8934 ± 0.0178 | 0.4878 ± 0.0369     | 0.3569 ± 0.0716   | 0.5345 ± 0.0304  | 0.0921 ± 0.0274 | 0.0349 ± 0.0112 | 0.5146 ± 0.0247 | 0.7007 ± 0.1389 | 0.9681 ± 0.0140    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P3_rotten          | knn         |    nan | 0.9041 ± 0.0000 | 0.8436 ± 0.0000     | 0.4455 ± 0.0000   | 0.9269 ± 0.0000  | 0.0942 ± 0.0000 | 0.0126 ± 0.0000 | 0.8838 ± 0.0000 | 0.6327 ± 0.0000 | 0.9473 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P3_rotten          | mahalanobis |      5 | 0.8912 ± 0.0144 | 0.4877 ± 0.0382     | 0.2978 ± 0.1281   | 0.5345 ± 0.0304  | 0.0807 ± 0.0335 | 0.0416 ± 0.0084 | 0.5134 ± 0.0290 | 0.6735 ± 0.1744 | 0.9597 ± 0.0096    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P3_rotten          | mahalanobis |    nan | 0.9299 ± 0.0000 | 0.8670 ± 0.0000     | 0.6467 ± 0.0000   | 0.9269 ± 0.0000  | 0.1172 ± 0.0000 | 0.0244 ± 0.0000 | 0.8970 ± 0.0000 | 0.6939 ± 0.0000 | 0.9617 ± 0.0000    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P3_rotten          | msp         |      5 | 0.4470 ± 0.0976 | 0.2706 ± 0.0507     | 0.0152 ± 0.0222   | 0.5345 ± 0.0304  | 0.0229 ± 0.0097 | 0.0280 ± 0.0110 | 0.5174 ± 0.0260 | 0.9116 ± 0.0118 | 0.9373 ± 0.0037    |        3 |                    0 | val         |
| fruit12_banana | resnet50  | P3_rotten          | msp         |    nan | 0.7504 ± 0.0000 | 0.7251 ± 0.0000     | 0.3281 ± 0.0000   | 0.9269 ± 0.0000  | 0.0939 ± 0.0000 | 0.0978 ± 0.0000 | 0.8826 ± 0.0000 | 0.8163 ± 0.0000 | 0.9138 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P1_out_of_grade    | energy      |      5 | 0.4994 ± 0.0292 | 0.3661 ± 0.0557     | 0.1474 ± 0.0640   | 0.6386 ± 0.0219  | 0.0237 ± 0.0141 | 0.0274 ± 0.0184 | 0.6000 ± 0.0459 | 0.9612 ± 0.0269 | 0.9298 ± 0.0540    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P1_out_of_grade    | energy      |    nan | 0.7023 ± 0.0000 | 0.6433 ± 0.0000     | 0.4105 ± 0.0000   | 0.8737 ± 0.0000  | 0.0289 ± 0.0000 | 0.0189 ± 0.0000 | 0.7579 ± 0.0000 | 0.8140 ± 0.0000 | 0.8421 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P1_out_of_grade    | knn         |      5 | 0.8248 ± 0.0830 | 0.5421 ± 0.0481     | 0.4456 ± 0.1011   | 0.6386 ± 0.0219  | 0.0556 ± 0.0000 | 0.0641 ± 0.0449 | 0.5895 ± 0.0279 | 0.6744 ± 0.2243 | 0.9193 ± 0.0475    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P1_out_of_grade    | knn         |    nan | 0.9067 ± 0.0000 | 0.7905 ± 0.0000     | 0.6000 ± 0.0000   | 0.8737 ± 0.0000  | 0.0344 ± 0.0000 | 0.0900 ± 0.0000 | 0.7789 ± 0.0000 | 0.3721 ± 0.0000 | 0.8947 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P1_out_of_grade    | mahalanobis |      5 | 0.8623 ± 0.0792 | 0.5647 ± 0.0291     | 0.4702 ± 0.0955   | 0.6386 ± 0.0219  | 0.0396 ± 0.0276 | 0.0641 ± 0.0365 | 0.5895 ± 0.0279 | 0.6124 ± 0.3035 | 0.9193 ± 0.0580    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P1_out_of_grade    | mahalanobis |    nan | 0.9422 ± 0.0000 | 0.8296 ± 0.0000     | 0.7684 ± 0.0000   | 0.8737 ± 0.0000  | 0.0344 ± 0.0000 | 0.0567 ± 0.0000 | 0.8105 ± 0.0000 | 0.2791 ± 0.0000 | 0.9263 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P1_out_of_grade    | msp         |      5 | 0.4994 ± 0.0292 | 0.3661 ± 0.0557     | 0.1474 ± 0.0640   | 0.6386 ± 0.0219  | 0.0237 ± 0.0141 | 0.0307 ± 0.0238 | 0.6035 ± 0.0425 | 0.9612 ± 0.0269 | 0.9333 ± 0.0530    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P1_out_of_grade    | msp         |    nan | 0.7023 ± 0.0000 | 0.6433 ± 0.0000     | 0.4105 ± 0.0000   | 0.8737 ± 0.0000  | 0.0289 ± 0.0000 | 0.0189 ± 0.0000 | 0.7579 ± 0.0000 | 0.8140 ± 0.0000 | 0.8421 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P2_unseen_interior | energy      |      5 | 0.6200 ± 0.1207 | 0.6003 ± 0.1153     | 0.2494 ± 0.2156   | 0.9189 ± 0.0309  | 0.0360 ± 0.0233 | 0.0216 ± 0.0179 | 0.8797 ± 0.0400 | 0.9274 ± 0.0473 | 0.9368 ± 0.0360    |        6 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P2_unseen_interior | energy      |    nan | 0.6825 ± 0.1274 | 0.6760 ± 0.1230     | 0.2560 ± 0.1436   | 0.9725 ± 0.0052  | 0.0097 ± 0.0032 | 0.0306 ± 0.0134 | 0.9163 ± 0.0328 | 0.8667 ± 0.0730 | 0.9217 ± 0.0387    |        6 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P2_unseen_interior | knn         |      5 | 0.5747 ± 0.0931 | 0.5491 ± 0.0745     | 0.2195 ± 0.0803   | 0.9189 ± 0.0309  | 0.0411 ± 0.0236 | 0.0516 ± 0.0494 | 0.8717 ± 0.0567 | 0.9333 ± 0.0953 | 0.9282 ± 0.0712    |        6 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P2_unseen_interior | knn         |    nan | 0.6219 ± 0.0733 | 0.6146 ± 0.0715     | 0.3751 ± 0.0250   | 0.9725 ± 0.0052  | 0.0568 ± 0.0014 | 0.0778 ± 0.0725 | 0.8819 ± 0.0823 | 0.9033 ± 0.0402 | 0.9094 ± 0.0875    |        6 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P2_unseen_interior | mahalanobis |      5 | 0.5926 ± 0.0787 | 0.5723 ± 0.0688     | 0.2857 ± 0.0397   | 0.9189 ± 0.0309  | 0.0411 ± 0.0236 | 0.0573 ± 0.0531 | 0.8718 ± 0.0518 | 0.9159 ± 0.0923 | 0.9264 ± 0.0699    |        6 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P2_unseen_interior | mahalanobis |    nan | 0.6522 ± 0.0758 | 0.6432 ± 0.0723     | 0.3485 ± 0.0166   | 0.9725 ± 0.0052  | 0.0568 ± 0.0014 | 0.0609 ± 0.0667 | 0.9043 ± 0.0695 | 0.8533 ± 0.0146 | 0.9261 ± 0.0809    |        6 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P2_unseen_interior | msp         |      5 | 0.6200 ± 0.1207 | 0.6003 ± 0.1153     | 0.2494 ± 0.2156   | 0.9189 ± 0.0309  | 0.0360 ± 0.0233 | 0.0233 ± 0.0165 | 0.8815 ± 0.0404 | 0.9311 ± 0.0487 | 0.9386 ± 0.0362    |        6 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P2_unseen_interior | msp         |    nan | 0.6825 ± 0.1274 | 0.6760 ± 0.1230     | 0.2560 ± 0.1436   | 0.9725 ± 0.0052  | 0.0097 ± 0.0032 | 0.0306 ± 0.0134 | 0.9163 ± 0.0328 | 0.8667 ± 0.0730 | 0.9217 ± 0.0387    |        6 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P3_rotten          | energy      |      5 | 0.3543 ± 0.0695 | 0.2895 ± 0.0426     | 0.0000 ± 0.0000   | 0.7053 ± 0.0151  | 0.0197 ± 0.0113 | 0.0416 ± 0.0447 | 0.6836 ± 0.0233 | 0.9889 ± 0.0192 | 0.9493 ± 0.0383    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P3_rotten          | energy      |    nan | 0.4070 ± 0.0000 | 0.3908 ± 0.0000     | 0.0000 ± 0.0000   | 0.9058 ± 0.0000  | 0.0191 ± 0.0000 | 0.0291 ± 0.0000 | 0.8551 ± 0.0000 | 0.9333 ± 0.0000 | 0.9348 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P3_rotten          | knn         |      5 | 0.5593 ± 0.0173 | 0.4079 ± 0.0068     | 0.1353 ± 0.0798   | 0.7053 ± 0.0151  | 0.0641 ± 0.0160 | 0.0629 ± 0.0375 | 0.6594 ± 0.0145 | 0.8889 ± 0.0839 | 0.9324 ± 0.0335    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P3_rotten          | knn         |    nan | 0.5865 ± 0.0000 | 0.5362 ± 0.0000     | 0.2464 ± 0.0000   | 0.9058 ± 0.0000  | 0.0382 ± 0.0000 | 0.0893 ± 0.0000 | 0.8333 ± 0.0000 | 0.9667 ± 0.0000 | 0.9275 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P3_rotten          | mahalanobis |      5 | 0.5421 ± 0.0304 | 0.4039 ± 0.0185     | 0.1256 ± 0.0412   | 0.7053 ± 0.0151  | 0.0590 ± 0.0248 | 0.0650 ± 0.0385 | 0.6667 ± 0.0192 | 0.8778 ± 0.0694 | 0.9396 ± 0.0293    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P3_rotten          | mahalanobis |    nan | 0.5886 ± 0.0000 | 0.5457 ± 0.0000     | 0.2391 ± 0.0000   | 0.9058 ± 0.0000  | 0.0382 ± 0.0000 | 0.0629 ± 0.0000 | 0.8623 ± 0.0000 | 0.9667 ± 0.0000 | 0.9565 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P3_rotten          | msp         |      5 | 0.3238 ± 0.0370 | 0.2711 ± 0.0282     | 0.0048 ± 0.0084   | 0.7053 ± 0.0151  | 0.0195 ± 0.0111 | 0.0244 ± 0.0201 | 0.6884 ± 0.0192 | 0.9778 ± 0.0385 | 0.9614 ± 0.0182    |        3 |                    0 | val         |
| fruit12_mango  | dinov2_s  | P3_rotten          | msp         |    nan | 0.3843 ± 0.0000 | 0.3684 ± 0.0000     | 0.0000 ± 0.0000   | 0.9058 ± 0.0000  | 0.0191 ± 0.0000 | 0.0269 ± 0.0000 | 0.8551 ± 0.0000 | 0.9333 ± 0.0000 | 0.9420 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P1_out_of_grade    | energy      |      5 | 0.5825 ± 0.1336 | 0.4678 ± 0.1266     | 0.2105 ± 0.0737   | 0.7404 ± 0.0580  | 0.0326 ± 0.0214 | 0.0244 ± 0.0102 | 0.6982 ± 0.0475 | 0.8837 ± 0.1452 | 0.9368 ± 0.0380    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P1_out_of_grade    | energy      |    nan | 0.7520 ± 0.0000 | 0.7244 ± 0.0000     | 0.5368 ± 0.0000   | 0.9263 ± 0.0000  | 0.0078 ± 0.0000 | 0.0522 ± 0.0000 | 0.7895 ± 0.0000 | 0.8140 ± 0.0000 | 0.8105 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P1_out_of_grade    | knn         |      5 | 0.7755 ± 0.0910 | 0.5834 ± 0.0546     | 0.3333 ± 0.1159   | 0.7404 ± 0.0580  | 0.0344 ± 0.0211 | 0.0511 ± 0.0158 | 0.6702 ± 0.0717 | 0.6124 ± 0.1776 | 0.8982 ± 0.0370    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P1_out_of_grade    | knn         |    nan | 0.8778 ± 0.0000 | 0.8203 ± 0.0000     | 0.6316 ± 0.0000   | 0.9263 ± 0.0000  | 0.0556 ± 0.0000 | 0.1678 ± 0.0000 | 0.7684 ± 0.0000 | 0.3488 ± 0.0000 | 0.8211 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P1_out_of_grade    | mahalanobis |      5 | 0.8012 ± 0.0268 | 0.6156 ± 0.0306     | 0.4281 ± 0.0161   | 0.7404 ± 0.0580  | 0.0415 ± 0.0244 | 0.0700 ± 0.0376 | 0.6596 ± 0.0701 | 0.5814 ± 0.1208 | 0.8737 ± 0.0316    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P1_out_of_grade    | mahalanobis |    nan | 0.8825 ± 0.0000 | 0.8259 ± 0.0000     | 0.5895 ± 0.0000   | 0.9263 ± 0.0000  | 0.0556 ± 0.0000 | 0.1689 ± 0.0000 | 0.7474 ± 0.0000 | 0.2558 ± 0.0000 | 0.8000 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P1_out_of_grade    | msp         |      5 | 0.5825 ± 0.1336 | 0.4678 ± 0.1266     | 0.2105 ± 0.0737   | 0.7404 ± 0.0580  | 0.0326 ± 0.0214 | 0.0244 ± 0.0102 | 0.6982 ± 0.0475 | 0.8837 ± 0.1452 | 0.9368 ± 0.0380    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P1_out_of_grade    | msp         |    nan | 0.7520 ± 0.0000 | 0.7244 ± 0.0000     | 0.5368 ± 0.0000   | 0.9263 ± 0.0000  | 0.0078 ± 0.0000 | 0.0522 ± 0.0000 | 0.7895 ± 0.0000 | 0.8140 ± 0.0000 | 0.8105 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P2_unseen_interior | energy      |      5 | 0.6531 ± 0.1193 | 0.5743 ± 0.0700     | 0.2886 ± 0.1550   | 0.8091 ± 0.0605  | 0.0227 ± 0.0136 | 0.0388 ± 0.0263 | 0.7723 ± 0.0573 | 0.8393 ± 0.1103 | 0.8993 ± 0.0411    |        6 |                    0 | val         |
| fruit12_mango  | resnet50  | P2_unseen_interior | energy      |    nan | 0.7221 ± 0.0303 | 0.7039 ± 0.0222     | 0.3969 ± 0.0364   | 0.9223 ± 0.0145  | 0.0360 ± 0.0006 | 0.0558 ± 0.0286 | 0.8673 ± 0.0040 | 0.8056 ± 0.1156 | 0.8951 ± 0.0029    |        6 |                    0 | val         |
| fruit12_mango  | resnet50  | P2_unseen_interior | knn         |      5 | 0.6798 ± 0.0708 | 0.5631 ± 0.0552     | 0.2633 ± 0.0647   | 0.8091 ± 0.0605  | 0.0266 ± 0.0112 | 0.0198 ± 0.0144 | 0.7569 ± 0.0476 | 0.8133 ± 0.0943 | 0.9309 ± 0.0470    |        6 |                    0 | val         |
| fruit12_mango  | resnet50  | P2_unseen_interior | knn         |    nan | 0.7538 ± 0.1003 | 0.7157 ± 0.0899     | 0.4291 ± 0.0717   | 0.9223 ± 0.0145  | 0.0311 ± 0.0267 | 0.0759 ± 0.0612 | 0.8377 ± 0.0836 | 0.6833 ± 0.0183 | 0.8870 ± 0.1003    |        6 |                    0 | val         |
| fruit12_mango  | resnet50  | P2_unseen_interior | mahalanobis |      5 | 0.7492 ± 0.1087 | 0.6243 ± 0.0577     | 0.4040 ± 0.0695   | 0.8091 ± 0.0605  | 0.0167 ± 0.0081 | 0.0404 ± 0.0335 | 0.7434 ± 0.0590 | 0.7178 ± 0.1453 | 0.9135 ± 0.0815    |        6 |                    0 | val         |
| fruit12_mango  | resnet50  | P2_unseen_interior | mahalanobis |    nan | 0.7812 ± 0.0850 | 0.7431 ± 0.0736     | 0.4623 ± 0.0707   | 0.9223 ± 0.0145  | 0.0352 ± 0.0223 | 0.0459 ± 0.0321 | 0.8272 ± 0.0597 | 0.5656 ± 0.0596 | 0.8658 ± 0.0646    |        6 |                    0 | val         |
| fruit12_mango  | resnet50  | P2_unseen_interior | msp         |      5 | 0.6531 ± 0.1193 | 0.5743 ± 0.0700     | 0.2886 ± 0.1550   | 0.8091 ± 0.0605  | 0.0227 ± 0.0136 | 0.0388 ± 0.0263 | 0.7723 ± 0.0573 | 0.8393 ± 0.1103 | 0.8993 ± 0.0411    |        6 |                    0 | val         |
| fruit12_mango  | resnet50  | P2_unseen_interior | msp         |    nan | 0.7221 ± 0.0303 | 0.7039 ± 0.0222     | 0.3969 ± 0.0364   | 0.9223 ± 0.0145  | 0.0360 ± 0.0006 | 0.0558 ± 0.0286 | 0.8673 ± 0.0040 | 0.8167 ± 0.1278 | 0.8951 ± 0.0029    |        6 |                    0 | val         |
| fruit12_mango  | resnet50  | P3_rotten          | energy      |      5 | 0.3700 ± 0.0782 | 0.3009 ± 0.0651     | 0.0580 ± 0.0453   | 0.6932 ± 0.0865  | 0.0366 ± 0.0085 | 0.0425 ± 0.0323 | 0.6594 ± 0.0767 | 0.9444 ± 0.0962 | 0.8937 ± 0.0365    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P3_rotten          | energy      |    nan | 0.4041 ± 0.0000 | 0.3853 ± 0.0000     | 0.0000 ± 0.0000   | 0.8841 ± 0.0000  | 0.0234 ± 0.0000 | 0.0503 ± 0.0000 | 0.8188 ± 0.0000 | 0.9000 ± 0.0000 | 0.8841 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P3_rotten          | knn         |      5 | 0.5329 ± 0.0655 | 0.3809 ± 0.0343     | 0.0918 ± 0.0733   | 0.6932 ± 0.0865  | 0.0533 ± 0.0229 | 0.0673 ± 0.0228 | 0.6401 ± 0.1156 | 0.8556 ± 0.0509 | 0.9227 ± 0.0399    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P3_rotten          | knn         |    nan | 0.5546 ± 0.0000 | 0.5157 ± 0.0000     | 0.2826 ± 0.0000   | 0.8841 ± 0.0000  | 0.0587 ± 0.0000 | 0.1276 ± 0.0000 | 0.7754 ± 0.0000 | 0.9333 ± 0.0000 | 0.8478 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P3_rotten          | mahalanobis |      5 | 0.5626 ± 0.0440 | 0.4247 ± 0.0366     | 0.1280 ± 0.0658   | 0.6932 ± 0.0865  | 0.0440 ± 0.0149 | 0.0626 ± 0.0130 | 0.6377 ± 0.1007 | 0.8667 ± 0.0882 | 0.9082 ± 0.0254    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P3_rotten          | mahalanobis |    nan | 0.6046 ± 0.0000 | 0.5616 ± 0.0000     | 0.2536 ± 0.0000   | 0.8841 ± 0.0000  | 0.0587 ± 0.0000 | 0.1383 ± 0.0000 | 0.7391 ± 0.0000 | 0.9333 ± 0.0000 | 0.8043 ± 0.0000    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P3_rotten          | msp         |      5 | 0.3706 ± 0.0564 | 0.3005 ± 0.0508     | 0.0411 ± 0.0590   | 0.6932 ± 0.0865  | 0.0368 ± 0.0083 | 0.0287 ± 0.0175 | 0.6667 ± 0.0817 | 0.9444 ± 0.0962 | 0.9130 ± 0.0126    |        3 |                    0 | val         |
| fruit12_mango  | resnet50  | P3_rotten          | msp         |    nan | 0.4082 ± 0.0000 | 0.3915 ± 0.0000     | 0.0000 ± 0.0000   | 0.8841 ± 0.0000  | 0.0237 ± 0.0000 | 0.0240 ± 0.0000 | 0.7971 ± 0.0000 | 0.9333 ± 0.0000 | 0.8551 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P1_out_of_grade    | energy      |      5 | 0.3388 ± 0.1400 | 0.3219 ± 0.1355     | 0.0319 ± 0.0426   | 0.8453 ± 0.0839  | 0.0098 ± 0.0078 | 0.0187 ± 0.0187 | 0.8214 ± 0.0877 | 0.9735 ± 0.0183 | 0.9321 ± 0.0351    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P1_out_of_grade    | energy      |    nan | 0.4683 ± 0.0000 | 0.4642 ± 0.0000     | 0.0120 ± 0.0000   | 0.9431 ± 0.0000  | 0.0631 ± 0.0000 | 0.0383 ± 0.0000 | 0.9311 ± 0.0000 | 0.9841 ± 0.0000 | 0.9611 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P1_out_of_grade    | knn         |      5 | 0.6064 ± 0.0152 | 0.5134 ± 0.0337     | 0.1108 ± 0.0443   | 0.8453 ± 0.0839  | 0.0291 ± 0.0039 | 0.0238 ± 0.0057 | 0.7904 ± 0.0764 | 0.8765 ± 0.0081 | 0.9351 ± 0.0046    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P1_out_of_grade    | knn         |    nan | 0.7209 ± 0.0000 | 0.6819 ± 0.0000     | 0.2695 ± 0.0000   | 0.9431 ± 0.0000  | 0.0111 ± 0.0000 | 0.0044 ± 0.0000 | 0.9042 ± 0.0000 | 0.8730 ± 0.0000 | 0.9581 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P1_out_of_grade    | mahalanobis |      5 | 0.6108 ± 0.0333 | 0.5238 ± 0.0596     | 0.1108 ± 0.0304   | 0.8453 ± 0.0839  | 0.0179 ± 0.0000 | 0.0164 ± 0.0056 | 0.7964 ± 0.0794 | 0.8765 ± 0.0153 | 0.9391 ± 0.0086    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P1_out_of_grade    | mahalanobis |    nan | 0.7121 ± 0.0000 | 0.6716 ± 0.0000     | 0.2126 ± 0.0000   | 0.9431 ± 0.0000  | 0.0111 ± 0.0000 | 0.0044 ± 0.0000 | 0.8862 ± 0.0000 | 0.6402 ± 0.0000 | 0.9401 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P1_out_of_grade    | msp         |      5 | 0.3388 ± 0.1400 | 0.3219 ± 0.1355     | 0.0319 ± 0.0426   | 0.8453 ± 0.0839  | 0.0098 ± 0.0078 | 0.0180 ± 0.0174 | 0.8214 ± 0.0877 | 0.9735 ± 0.0183 | 0.9331 ± 0.0334    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P1_out_of_grade    | msp         |    nan | 0.4683 ± 0.0000 | 0.4642 ± 0.0000     | 0.0120 ± 0.0000   | 0.9431 ± 0.0000  | 0.0631 ± 0.0000 | 0.0383 ± 0.0000 | 0.9311 ± 0.0000 | 0.9841 ± 0.0000 | 0.9611 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | dinov2_s  | P2_unseen_interior | energy      |      5 | 0.6418 ± 0.1840 | 0.5933 ± 0.2105     | 0.2493 ± 0.1882   | 0.8533 ± 0.1126  | 0.0229 ± 0.0169 | 0.0160 ± 0.0114 | 0.8332 ± 0.1088 | 0.8364 ± 0.1325 | 0.9536 ± 0.0147    |        6 |                    0 | val         |
| ninepeach      | dinov2_s  | P2_unseen_interior | energy      |    nan | 0.5829 ± 0.3881 | 0.5780 ± 0.3841     | 0.4008 ± 0.4171   | 0.9377 ± 0.0523  | 0.0207 ± 0.0114 | 0.0130 ± 0.0127 | 0.9127 ± 0.0504 | 0.7410 ± 0.2788 | 0.9626 ± 0.0065    |        6 |                    0 | val         |
| ninepeach      | dinov2_s  | P2_unseen_interior | knn         |      5 | 0.6285 ± 0.2556 | 0.5172 ± 0.1476     | 0.2292 ± 0.1865   | 0.8533 ± 0.1126  | 0.0180 ± 0.0113 | 0.0123 ± 0.0099 | 0.8116 ± 0.1038 | 0.7735 ± 0.2461 | 0.9488 ± 0.0067    |        6 |                    0 | val         |
| ninepeach      | dinov2_s  | P2_unseen_interior | knn         |    nan | 0.7397 ± 0.1662 | 0.6940 ± 0.1179     | 0.4011 ± 0.1814   | 0.9377 ± 0.0523  | 0.0157 ± 0.0129 | 0.0013 ± 0.0000 | 0.9033 ± 0.0474 | 0.7824 ± 0.1890 | 0.9548 ± 0.0016    |        6 |                    0 | val         |
| ninepeach      | dinov2_s  | P2_unseen_interior | mahalanobis |      5 | 0.6668 ± 0.2128 | 0.5582 ± 0.1096     | 0.2339 ± 0.1605   | 0.8533 ± 0.1126  | 0.0135 ± 0.0057 | 0.0080 ± 0.0081 | 0.8165 ± 0.1059 | 0.7780 ± 0.2218 | 0.9513 ± 0.0064    |        6 |                    0 | val         |
| ninepeach      | dinov2_s  | P2_unseen_interior | mahalanobis |    nan | 0.6825 ± 0.1852 | 0.6399 ± 0.1400     | 0.3031 ± 0.1645   | 0.9377 ± 0.0523  | 0.0154 ± 0.0133 | 0.0122 ± 0.0021 | 0.8918 ± 0.0494 | 0.7331 ± 0.2430 | 0.9416 ± 0.0054    |        6 |                    0 | val         |
| ninepeach      | dinov2_s  | P2_unseen_interior | msp         |      5 | 0.6418 ± 0.1840 | 0.5933 ± 0.2105     | 0.2493 ± 0.1882   | 0.8533 ± 0.1126  | 0.0229 ± 0.0169 | 0.0160 ± 0.0114 | 0.8332 ± 0.1088 | 0.8364 ± 0.1325 | 0.9536 ± 0.0147    |        6 |                    0 | val         |
| ninepeach      | dinov2_s  | P2_unseen_interior | msp         |    nan | 0.5829 ± 0.3881 | 0.5780 ± 0.3841     | 0.4008 ± 0.4171   | 0.9377 ± 0.0523  | 0.0207 ± 0.0114 | 0.0130 ± 0.0127 | 0.9127 ± 0.0504 | 0.7410 ± 0.2788 | 0.9626 ± 0.0065    |        6 |                    0 | val         |
| ninepeach      | resnet50  | P1_out_of_grade    | energy      |      5 | 0.2931 ± 0.1444 | 0.2639 ± 0.1277     | 0.0259 ± 0.0307   | 0.8084 ± 0.0893  | 0.0284 ± 0.0066 | 0.0329 ± 0.0090 | 0.7804 ± 0.0974 | 0.9771 ± 0.0153 | 0.9391 ± 0.0225    |        3 |                    0 | val         |
| ninepeach      | resnet50  | P1_out_of_grade    | energy      |    nan | 0.2353 ± 0.0000 | 0.2283 ± 0.0000     | 0.0030 ± 0.0000   | 0.9042 ± 0.0000  | 0.0631 ± 0.0000 | 0.0586 ± 0.0000 | 0.8832 ± 0.0000 | 0.9630 ± 0.0000 | 0.9341 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | resnet50  | P1_out_of_grade    | knn         |      5 | 0.7201 ± 0.0158 | 0.5835 ± 0.0871     | 0.2665 ± 0.0838   | 0.8084 ± 0.0893  | 0.0246 ± 0.0000 | 0.0171 ± 0.0035 | 0.7615 ± 0.0890 | 0.8695 ± 0.0301 | 0.9411 ± 0.0113    |        3 |                    0 | val         |
| ninepeach      | resnet50  | P1_out_of_grade    | knn         |    nan | 0.6738 ± 0.0000 | 0.6136 ± 0.0000     | 0.2515 ± 0.0000   | 0.9042 ± 0.0000  | 0.0111 ± 0.0000 | 0.0046 ± 0.0000 | 0.8743 ± 0.0000 | 0.8254 ± 0.0000 | 0.9611 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | resnet50  | P1_out_of_grade    | mahalanobis |      5 | 0.6747 ± 0.0796 | 0.5559 ± 0.1294     | 0.2026 ± 0.1292   | 0.8084 ± 0.0893  | 0.0111 ± 0.0067 | 0.0164 ± 0.0034 | 0.7665 ± 0.0893 | 0.8748 ± 0.0081 | 0.9421 ± 0.0125    |        3 |                    0 | val         |
| ninepeach      | resnet50  | P1_out_of_grade    | mahalanobis |    nan | 0.7009 ± 0.0000 | 0.6333 ± 0.0000     | 0.2216 ± 0.0000   | 0.9042 ± 0.0000  | 0.0024 ± 0.0000 | 0.0114 ± 0.0000 | 0.8653 ± 0.0000 | 0.7672 ± 0.0000 | 0.9521 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | resnet50  | P1_out_of_grade    | msp         |      5 | 0.2931 ± 0.1444 | 0.2639 ± 0.1277     | 0.0259 ± 0.0307   | 0.8084 ± 0.0893  | 0.0284 ± 0.0066 | 0.0329 ± 0.0090 | 0.7804 ± 0.0974 | 0.9771 ± 0.0153 | 0.9391 ± 0.0225    |        3 |                    0 | val         |
| ninepeach      | resnet50  | P1_out_of_grade    | msp         |    nan | 0.2353 ± 0.0000 | 0.2283 ± 0.0000     | 0.0030 ± 0.0000   | 0.9042 ± 0.0000  | 0.0631 ± 0.0000 | 0.0586 ± 0.0000 | 0.8832 ± 0.0000 | 0.9630 ± 0.0000 | 0.9341 ± 0.0000    |        3 |                    0 | val         |
| ninepeach      | resnet50  | P2_unseen_interior | energy      |      5 | 0.5140 ± 0.3495 | 0.4984 ± 0.3490     | 0.2018 ± 0.2200   | 0.8840 ± 0.0905  | 0.0261 ± 0.0183 | 0.0221 ± 0.0155 | 0.8557 ± 0.0891 | 0.8251 ± 0.1858 | 0.9399 ± 0.0147    |        6 |                    0 | val         |
| ninepeach      | resnet50  | P2_unseen_interior | energy      |    nan | 0.5819 ± 0.3230 | 0.5723 ± 0.3229     | 0.2840 ± 0.3111   | 0.9304 ± 0.0443  | 0.0292 ± 0.0128 | 0.0082 ± 0.0066 | 0.9092 ± 0.0356 | 0.7500 ± 0.2689 | 0.9566 ± 0.0110    |        6 |                    0 | val         |
| ninepeach      | resnet50  | P2_unseen_interior | knn         |      5 | 0.6194 ± 0.2046 | 0.5483 ± 0.1331     | 0.2927 ± 0.1994   | 0.8840 ± 0.0905  | 0.0151 ± 0.0068 | 0.0073 ± 0.0055 | 0.8447 ± 0.0875 | 0.8894 ± 0.1089 | 0.9398 ± 0.0144    |        6 |                    0 | val         |
| ninepeach      | resnet50  | P2_unseen_interior | knn         |    nan | 0.6233 ± 0.1116 | 0.5867 ± 0.0797     | 0.1423 ± 0.0230   | 0.9304 ± 0.0443  | 0.0053 ± 0.0015 | 0.0106 ± 0.0023 | 0.8865 ± 0.0473 | 0.8766 ± 0.0957 | 0.9432 ± 0.0144    |        6 |                    0 | val         |
| ninepeach      | resnet50  | P2_unseen_interior | mahalanobis |      5 | 0.6419 ± 0.1541 | 0.5765 ± 0.0896     | 0.2608 ± 0.1781   | 0.8840 ± 0.0905  | 0.0147 ± 0.0072 | 0.0083 ± 0.0056 | 0.8469 ± 0.0820 | 0.8968 ± 0.0916 | 0.9388 ± 0.0114    |        6 |                    0 | val         |
| ninepeach      | resnet50  | P2_unseen_interior | mahalanobis |    nan | 0.5794 ± 0.1766 | 0.5406 ± 0.1419     | 0.1481 ± 0.0824   | 0.9304 ± 0.0443  | 0.0113 ± 0.0003 | 0.0138 ± 0.0058 | 0.8898 ± 0.0436 | 0.8856 ± 0.0957 | 0.9482 ± 0.0089    |        6 |                    0 | val         |
| ninepeach      | resnet50  | P2_unseen_interior | msp         |      5 | 0.5140 ± 0.3495 | 0.4984 ± 0.3490     | 0.2018 ± 0.2200   | 0.8840 ± 0.0905  | 0.0261 ± 0.0183 | 0.0221 ± 0.0155 | 0.8557 ± 0.0891 | 0.8251 ± 0.1858 | 0.9399 ± 0.0147    |        6 |                    0 | val         |
| ninepeach      | resnet50  | P2_unseen_interior | msp         |    nan | 0.5819 ± 0.3230 | 0.5723 ± 0.3229     | 0.2840 ± 0.3111   | 0.9304 ± 0.0443  | 0.0292 ± 0.0128 | 0.0082 ± 0.0066 | 0.9092 ± 0.0356 | 0.7500 ± 0.2689 | 0.9566 ± 0.0110    |        6 |                    0 | val         |
| raspgrade      | dinov2_s  | P1_out_of_grade    | energy      |      5 | 0.5428 ± 0.0568 | 0.1856 ± 0.0308     | 0.0106 ± 0.0081   | 0.3606 ± 0.0833  | 0.0393 ± 0.0192 | 0.0448 ± 0.0147 | 0.3458 ± 0.0869 | 0.8889 ± 0.0481 | 0.9319 ± 0.0174    |        3 |                    0 | val         |
| raspgrade      | dinov2_s  | P1_out_of_grade    | energy      |    nan | 0.4056 ± 0.0000 | 0.3588 ± 0.0000     | 0.0667 ± 0.0000   | 0.7750 ± 0.0000  | 0.2512 ± 0.0000 | 0.2900 ± 0.0000 | 0.7264 ± 0.0000 | 1.0000 ± 0.0000 | 0.8875 ± 0.0000    |        3 |                    0 | val         |
| raspgrade      | dinov2_s  | P1_out_of_grade    | knn         |      5 | 0.4324 ± 0.0261 | 0.1730 ± 0.0509     | 0.0218 ± 0.0100   | 0.3606 ± 0.0833  | 0.0346 ± 0.0205 | 0.0378 ± 0.0147 | 0.3347 ± 0.0890 | 0.9167 ± 0.0000 | 0.9037 ± 0.0278    |        3 |                    0 | val         |
| raspgrade      | dinov2_s  | P1_out_of_grade    | knn         |    nan | 0.4944 ± 0.0000 | 0.3878 ± 0.0000     | 0.0111 ± 0.0000   | 0.7750 ± 0.0000  | 0.0331 ± 0.0000 | 0.0468 ± 0.0000 | 0.7042 ± 0.0000 | 0.9167 ± 0.0000 | 0.9056 ± 0.0000    |        3 |                    0 | val         |
| raspgrade      | dinov2_s  | P1_out_of_grade    | mahalanobis |      5 | 0.4988 ± 0.0467 | 0.1954 ± 0.0489     | 0.0120 ± 0.0090   | 0.3606 ± 0.0833  | 0.0334 ± 0.0184 | 0.0448 ± 0.0106 | 0.3380 ± 0.0848 | 0.9444 ± 0.0481 | 0.9171 ± 0.0175    |        3 |                    0 | val         |
| raspgrade      | dinov2_s  | P1_out_of_grade    | mahalanobis |    nan | 0.5197 ± 0.0000 | 0.4111 ± 0.0000     | 0.0375 ± 0.0000   | 0.7750 ± 0.0000  | 0.0211 ± 0.0000 | 0.0293 ± 0.0000 | 0.6736 ± 0.0000 | 0.8333 ± 0.0000 | 0.8639 ± 0.0000    |        3 |                    0 | val         |
| raspgrade      | dinov2_s  | P1_out_of_grade    | msp         |      5 | 0.5682 ± 0.0787 | 0.1976 ± 0.0272     | 0.0194 ± 0.0174   | 0.3606 ± 0.0833  | 0.0295 ± 0.0036 | 0.0324 ± 0.0094 | 0.3458 ± 0.0898 | 0.9444 ± 0.0481 | 0.9435 ± 0.0160    |        3 |                    0 | val         |
| raspgrade      | dinov2_s  | P1_out_of_grade    | msp         |    nan | 0.3438 ± 0.0000 | 0.3097 ± 0.0000     | 0.0986 ± 0.0000   | 0.7750 ± 0.0000  | 0.1813 ± 0.0000 | 0.1581 ± 0.0000 | 0.7236 ± 0.0000 | 0.9167 ± 0.0000 | 0.8778 ± 0.0000    |        3 |                    0 | val         |
| raspgrade      | dinov2_s  | P2_unseen_interior | energy      |      5 | 0.5113 ± 0.0201 | 0.2021 ± 0.0901     | 0.0267 ± 0.0339   | 0.3853 ± 0.1275  | 0.0376 ± 0.0131 | 0.0510 ± 0.0224 | 0.3629 ± 0.1271 | 0.9273 ± 0.0494 | 0.9360 ± 0.0193    |        9 |                    0 | val         |
| raspgrade      | dinov2_s  | P2_unseen_interior | energy      |    nan | 0.6059 ± 0.1015 | 0.5341 ± 0.1021     | 0.1177 ± 0.0577   | 0.8253 ± 0.0702  | 0.2907 ± 0.0744 | 0.3107 ± 0.0413 | 0.7916 ± 0.0764 | 0.8419 ± 0.0772 | 0.9362 ± 0.0132    |        9 |                    0 | val         |
| raspgrade      | dinov2_s  | P2_unseen_interior | knn         |      5 | 0.5255 ± 0.0406 | 0.2224 ± 0.0712     | 0.0332 ± 0.0204   | 0.3853 ± 0.1275  | 0.0436 ± 0.0184 | 0.0731 ± 0.0498 | 0.3562 ± 0.1219 | 0.8698 ± 0.0319 | 0.8668 ± 0.0351    |        9 |                    0 | val         |
| raspgrade      | dinov2_s  | P2_unseen_interior | knn         |    nan | 0.5732 ± 0.0945 | 0.4840 ± 0.0664     | 0.0816 ± 0.0597   | 0.8253 ± 0.0702  | 0.0431 ± 0.0087 | 0.0842 ± 0.0324 | 0.7616 ± 0.0531 | 0.8898 ± 0.0442 | 0.9129 ± 0.0158    |        9 |                    0 | val         |
| raspgrade      | dinov2_s  | P2_unseen_interior | mahalanobis |      5 | 0.5297 ± 0.0507 | 0.2234 ± 0.0705     | 0.0353 ± 0.0235   | 0.3853 ± 0.1275  | 0.0404 ± 0.0176 | 0.0717 ± 0.0339 | 0.3562 ± 0.1205 | 0.8565 ± 0.0552 | 0.8654 ± 0.0374    |        9 |                    0 | val         |
| raspgrade      | dinov2_s  | P2_unseen_interior | mahalanobis |    nan | 0.5589 ± 0.0738 | 0.4735 ± 0.0494     | 0.0832 ± 0.0466   | 0.8253 ± 0.0702  | 0.0315 ± 0.0001 | 0.0802 ± 0.0235 | 0.7395 ± 0.0434 | 0.8640 ± 0.0377 | 0.8902 ± 0.0429    |        9 |                    0 | val         |
| raspgrade      | dinov2_s  | P2_unseen_interior | msp         |      5 | 0.5052 ± 0.0257 | 0.2046 ± 0.0977     | 0.0336 ± 0.0365   | 0.3853 ± 0.1275  | 0.0402 ± 0.0140 | 0.0409 ± 0.0168 | 0.3653 ± 0.1252 | 0.9353 ± 0.0586 | 0.9380 ± 0.0267    |        9 |                    0 | val         |
| raspgrade      | dinov2_s  | P2_unseen_interior | msp         |    nan | 0.5827 ± 0.1322 | 0.5227 ± 0.1321     | 0.1031 ± 0.0500   | 0.8253 ± 0.0702  | 0.1632 ± 0.0443 | 0.1456 ± 0.0564 | 0.7821 ± 0.0560 | 0.8448 ± 0.1031 | 0.9146 ± 0.0283    |        9 |                    0 | val         |
| raspgrade      | resnet50  | P1_out_of_grade    | energy      |      5 | 0.5774 ± 0.0448 | 0.2254 ± 0.0808     | 0.0324 ± 0.0234   | 0.3745 ± 0.0826  | 0.0359 ± 0.0136 | 0.0301 ± 0.0162 | 0.3579 ± 0.0826 | 0.9444 ± 0.0481 | 0.9454 ± 0.0264    |        3 |                    0 | val         |
| raspgrade      | resnet50  | P1_out_of_grade    | energy      |    nan | 0.4811 ± 0.0000 | 0.4197 ± 0.0000     | 0.0028 ± 0.0000   | 0.7583 ± 0.0000  | 0.2518 ± 0.0000 | 0.3118 ± 0.0000 | 0.7361 ± 0.0000 | 1.0000 ± 0.0000 | 0.9306 ± 0.0000    |        3 |                    0 | val         |
| raspgrade      | resnet50  | P1_out_of_grade    | knn         |      5 | 0.5289 ± 0.0307 | 0.2115 ± 0.0653     | 0.0690 ± 0.0667   | 0.3745 ± 0.0826  | 0.0236 ± 0.0025 | 0.0524 ± 0.0268 | 0.3574 ± 0.0896 | 0.9444 ± 0.0481 | 0.8847 ± 0.0241    |        3 |                    0 | val         |
| raspgrade      | resnet50  | P1_out_of_grade    | knn         |    nan | 0.6115 ± 0.0000 | 0.4670 ± 0.0000     | 0.0486 ± 0.0000   | 0.7583 ± 0.0000  | 0.0331 ± 0.0000 | 0.0412 ± 0.0000 | 0.7194 ± 0.0000 | 0.9167 ± 0.0000 | 0.9444 ± 0.0000    |        3 |                    0 | val         |
| raspgrade      | resnet50  | P1_out_of_grade    | mahalanobis |      5 | 0.6014 ± 0.0548 | 0.2397 ± 0.0731     | 0.0861 ± 0.0779   | 0.3745 ± 0.0826  | 0.0337 ± 0.0191 | 0.0341 ± 0.0059 | 0.3602 ± 0.0907 | 0.9167 ± 0.0833 | 0.8940 ± 0.0273    |        3 |                    0 | val         |
| raspgrade      | resnet50  | P1_out_of_grade    | mahalanobis |    nan | 0.6090 ± 0.0000 | 0.4601 ± 0.0000     | 0.0792 ± 0.0000   | 0.7583 ± 0.0000  | 0.0423 ± 0.0000 | 0.0502 ± 0.0000 | 0.7111 ± 0.0000 | 0.8333 ± 0.0000 | 0.9347 ± 0.0000    |        3 |                    0 | val         |
| raspgrade      | resnet50  | P1_out_of_grade    | msp         |      5 | 0.5453 ± 0.0254 | 0.2162 ± 0.0760     | 0.0153 ± 0.0064   | 0.3745 ± 0.0826  | 0.0392 ± 0.0126 | 0.0414 ± 0.0138 | 0.3606 ± 0.0790 | 0.9444 ± 0.0481 | 0.9319 ± 0.0431    |        3 |                    0 | val         |
| raspgrade      | resnet50  | P1_out_of_grade    | msp         |    nan | 0.4764 ± 0.0000 | 0.4192 ± 0.0000     | 0.0056 ± 0.0000   | 0.7583 ± 0.0000  | 0.1116 ± 0.0000 | 0.0795 ± 0.0000 | 0.7389 ± 0.0000 | 1.0000 ± 0.0000 | 0.9417 ± 0.0000    |        3 |                    0 | val         |
| raspgrade      | resnet50  | P2_unseen_interior | energy      |      5 | 0.5082 ± 0.0322 | 0.1806 ± 0.0688     | 0.0289 ± 0.0329   | 0.3555 ± 0.0962  | 0.0414 ± 0.0140 | 0.0503 ± 0.0194 | 0.3397 ± 0.0972 | 0.9150 ± 0.0431 | 0.9158 ± 0.0298    |        9 |                    0 | val         |
| raspgrade      | resnet50  | P2_unseen_interior | energy      |    nan | 0.6137 ± 0.1427 | 0.5347 ± 0.1433     | 0.1781 ± 0.1309   | 0.8119 ± 0.0831  | 0.2524 ± 0.0361 | 0.2472 ± 0.0675 | 0.7875 ± 0.0897 | 0.9224 ± 0.0643 | 0.9485 ± 0.0100    |        9 |                    0 | val         |
| raspgrade      | resnet50  | P2_unseen_interior | knn         |      5 | 0.5253 ± 0.0526 | 0.1863 ± 0.0469     | 0.0268 ± 0.0249   | 0.3555 ± 0.0962  | 0.0454 ± 0.0186 | 0.0649 ± 0.0473 | 0.3345 ± 0.0908 | 0.8296 ± 0.0605 | 0.8733 ± 0.0320    |        9 |                    0 | val         |
| raspgrade      | resnet50  | P2_unseen_interior | knn         |    nan | 0.5671 ± 0.0816 | 0.4700 ± 0.0482     | 0.1043 ± 0.0586   | 0.8119 ± 0.0831  | 0.0450 ± 0.0138 | 0.0673 ± 0.0226 | 0.7683 ± 0.0719 | 0.8827 ± 0.0550 | 0.9413 ± 0.0050    |        9 |                    0 | val         |
| raspgrade      | resnet50  | P2_unseen_interior | mahalanobis |      5 | 0.5263 ± 0.0517 | 0.1914 ± 0.0437     | 0.0310 ± 0.0229   | 0.3555 ± 0.0962  | 0.0408 ± 0.0166 | 0.0682 ± 0.0405 | 0.3374 ± 0.0934 | 0.8382 ± 0.0769 | 0.8760 ± 0.0448    |        9 |                    0 | val         |
| raspgrade      | resnet50  | P2_unseen_interior | mahalanobis |    nan | 0.5503 ± 0.0651 | 0.4529 ± 0.0235     | 0.0689 ± 0.0261   | 0.8119 ± 0.0831  | 0.0641 ± 0.0027 | 0.0661 ± 0.0225 | 0.7628 ± 0.0739 | 0.9043 ± 0.0437 | 0.9334 ± 0.0048    |        9 |                    0 | val         |
| raspgrade      | resnet50  | P2_unseen_interior | msp         |      5 | 0.5109 ± 0.0263 | 0.1864 ± 0.0720     | 0.0250 ± 0.0268   | 0.3555 ± 0.0962  | 0.0408 ± 0.0240 | 0.0460 ± 0.0198 | 0.3406 ± 0.0960 | 0.9131 ± 0.0344 | 0.9127 ± 0.0354    |        9 |                    0 | val         |
| raspgrade      | resnet50  | P2_unseen_interior | msp         |    nan | 0.6006 ± 0.1697 | 0.5347 ± 0.1536     | 0.1878 ± 0.1438   | 0.8119 ± 0.0831  | 0.1115 ± 0.0735 | 0.1326 ± 0.1148 | 0.7849 ± 0.0712 | 0.9060 ± 0.0856 | 0.9454 ± 0.0196    |        9 |                    0 | val         |

Read this table before making any claim about calibration.

**The comparison at a matched false-positive rate is the only one the plan allows.**
Per-class thresholds do not touch the scores; they move the cut. So at a matched global
FPR the calibrated arm cannot differ from the uncalibrated one -- the matched-FPR
numbers are therefore `oscr_at_fpr5_rule` and `ccr_fpr5_before`, and `ccr_cal` must never
be compared against `ccr_fpr5_before` as if the two had the same FPR. The honest summary
of this table is *threshold redistribution*: `ccr_cal` is bought with `fpr_cal`, which
sits near 0.95 precisely because the per-class 5%-quantile accepts ~95% of everything.
Per-class matched-FPR calibration (shifting all thresholds by one common offset until the
global FPR returns to 5%) is *not* computable from the stored arrays, because the
predicted class of each unknown sample was not kept; that is a limitation of the
measurement, not a result.

**`ccr_accept_all` is the column that decides whether calibration bought anything.**
A per-class threshold at the 5th percentile accepts ~95% of *known* samples by
construction — and also ~95% of unknown ones, because the threshold sits near the bottom
of the score distribution rather than at a fixed global FPR. So `fpr_cal` hovering near
0.95 is not a failure of the calibration, and `ccr_cal` rising above `ccr_fpr5_before` is
not by itself evidence of better rejection: compare `ccr_cal` with `ccr_accept_all`. If the
two are close, the calibrated arm accepted essentially everything and the only thing it
repairs is the *imbalance* of rejection across grades — which is what
`rej_sd_before/after` measures and what the plan asked about.

`ccr_fpr5_before` is the uncalibrated operating point (CCR at the global 5%-FPR threshold).
`rej_sd_before/after` are the
standard deviations of the per-class rejection rates at, respectively, the global
5%-FPR operating point and the calibrated one; a drop means the imbalance across grades
was a threshold artefact. `fpr_cal` is the false-positive rate that results from the
calibrated thresholds -- it is an outcome, not something that was tuned. Where `fpr_cal`
approaches 1.0 while `auroc` is below 0.5, the score ranking is inverted for that view
(unknowns look more in-distribution than knowns) and no per-class calibration can repair
it; the honest reading is that the ranking, not the threshold, is the problem.
`calib_src` says which pool the thresholds were fitted on (`val` is the normal case;
`support (no usable val split)` means the view had fewer than 20 calibration samples and
fell back to a pool the head was trained on, so its thresholds are optimistic).
`classes_no_tau_max` counts known classes with no calibration samples: those get
threshold -inf (everything predicted as them is accepted), which can only inflate FPR.


## Adapted backbones: full fine-tuning vs LoRA (mean ± sd over seeds)

| exp    | encoder       | view           |   shot | acc             | macro_f1        | off_by_one      |   n_runs |
|:-------|:--------------|:---------------|-------:|:----------------|:----------------|:----------------|---------:|
| E1ft   | resnet50_ft   | banana3        |      1 | 0.4457 ± 0.0767 | 0.4478 ± 0.0785 | 0.4419 ± 0.0234 |        3 |
| E1ft   | resnet50_ft   | banana3        |      5 | 0.6648 ± 0.0181 | 0.6211 ± 0.0341 | 0.2903 ± 0.0357 |        3 |
| E1ft   | resnet50_ft   | banana3        |     10 | 0.8109 ± 0.0197 | 0.7982 ± 0.0268 | 0.1685 ± 0.0368 |        3 |
| E1ft   | resnet50_ft   | banana3        |     50 | 0.9101 ± 0.0351 | 0.9056 ± 0.0360 | 0.0843 ± 0.0297 |        3 |
| E1ft   | resnet50_ft   | banana4        |      1 | 0.4881 ± 0.0854 | 0.4562 ± 0.1017 | 0.4067 ± 0.0201 |        3 |
| E1ft   | resnet50_ft   | banana4        |      5 | 0.8187 ± 0.0881 | 0.8195 ± 0.0901 | 0.1768 ± 0.0842 |        3 |
| E1ft   | resnet50_ft   | banana4        |     10 | 0.9461 ± 0.0284 | 0.9481 ± 0.0275 | 0.0539 ± 0.0284 |        3 |
| E1ft   | resnet50_ft   | banana4        |     50 | 0.9593 ± 0.0177 | 0.9609 ± 0.0168 | 0.0407 ± 0.0177 |        3 |
| E1ft   | resnet50_ft   | fruit12_apple  |      1 | 0.3994 ± 0.0545 | 0.3579 ± 0.0982 | 0.4953 ± 0.0465 |        3 |
| E1ft   | resnet50_ft   | fruit12_apple  |      5 | 0.5016 ± 0.0944 | 0.4904 ± 0.0895 | 0.3931 ± 0.0307 |        3 |
| E1ft   | resnet50_ft   | fruit12_apple  |     10 | 0.6682 ± 0.0945 | 0.6633 ± 0.0902 | 0.2814 ± 0.0746 |        3 |
| E1ft   | resnet50_ft   | fruit12_apple  |     50 | 0.7720 ± 0.0407 | 0.7589 ± 0.0472 | 0.1761 ± 0.0237 |        3 |
| E1ft   | resnet50_ft   | fruit12_banana |      1 | 0.3457 ± 0.0291 | 0.2950 ± 0.0348 | 0.5437 ± 0.0468 |        3 |
| E1ft   | resnet50_ft   | fruit12_banana |      5 | 0.5581 ± 0.1166 | 0.4666 ± 0.0732 | 0.3820 ± 0.1286 |        3 |
| E1ft   | resnet50_ft   | fruit12_banana |     10 | 0.7130 ± 0.0627 | 0.5933 ± 0.0207 | 0.2571 ± 0.0665 |        3 |
| E1ft   | resnet50_ft   | fruit12_banana |     50 | 0.9002 ± 0.0213 | 0.8269 ± 0.0317 | 0.0910 ± 0.0243 |        3 |
| E1lora | dinov2_s_lora | banana3        |      1 | 0.4569 ± 0.0626 | 0.4247 ± 0.0571 | 0.4719 ± 0.1217 |        3 |
| E1lora | dinov2_s_lora | banana3        |      5 | 0.7022 ± 0.1328 | 0.6936 ± 0.1362 | 0.2659 ± 0.1208 |        3 |
| E1lora | dinov2_s_lora | banana3        |     10 | 0.6685 ± 0.2004 | 0.6508 ± 0.2123 | 0.2790 ± 0.1915 |        3 |
| E1lora | dinov2_s_lora | banana3        |     50 | 0.8390 ± 0.1234 | 0.8252 ± 0.1375 | 0.1554 ± 0.1187 |        3 |
| E1lora | dinov2_s_lora | banana4        |      1 | 0.6101 ± 0.0417 | 0.6027 ± 0.0319 | 0.3501 ± 0.0530 |        3 |
| E1lora | dinov2_s_lora | banana4        |      5 | 0.8815 ± 0.0464 | 0.8835 ± 0.0434 | 0.1141 ± 0.0453 |        3 |
| E1lora | dinov2_s_lora | banana4        |     10 | 0.9072 ± 0.0666 | 0.9032 ± 0.0765 | 0.0920 ± 0.0651 |        3 |
| E1lora | dinov2_s_lora | banana4        |     50 | 0.9646 ± 0.0131 | 0.9660 ± 0.0128 | 0.0354 ± 0.0131 |        3 |
| E1lora | dinov2_s_lora | field4_banana  |      1 | 0.6487 ± 0.1223 | 0.6460 ± 0.1241 | 0.3513 ± 0.1223 |        3 |
| E1lora | dinov2_s_lora | field4_banana  |      5 | 0.7987 ± 0.1365 | 0.7905 ± 0.1427 | 0.2013 ± 0.1365 |        3 |
| E1lora | dinov2_s_lora | field4_banana  |     10 | 0.9073 ± 0.0980 | 0.9057 ± 0.1006 | 0.0927 ± 0.0980 |        3 |
| E1lora | dinov2_s_lora | field4_banana  |     50 | 0.9793 ± 0.0110 | 0.9793 ± 0.0110 | 0.0207 ± 0.0110 |        3 |
| E1lora | dinov2_s_lora | field4_mango   |      1 | 0.7580 ± 0.1571 | 0.7532 ± 0.1591 | 0.2420 ± 0.1571 |        3 |
| E1lora | dinov2_s_lora | field4_mango   |      5 | 0.9033 ± 0.0180 | 0.9025 ± 0.0187 | 0.0967 ± 0.0180 |        3 |
| E1lora | dinov2_s_lora | field4_mango   |     10 | 0.9640 ± 0.0457 | 0.9639 ± 0.0459 | 0.0360 ± 0.0457 |        3 |
| E1lora | dinov2_s_lora | field4_mango   |     50 | 0.9980 ± 0.0020 | 0.9980 ± 0.0020 | 0.0020 ± 0.0020 |        3 |
| E1lora | dinov2_s_lora | fruit12_apple  |      1 | 0.4119 ± 0.0547 | 0.3754 ± 0.0612 | 0.4465 ± 0.0438 |        3 |
| E1lora | dinov2_s_lora | fruit12_apple  |      5 | 0.5676 ± 0.0786 | 0.5613 ± 0.0855 | 0.3648 ± 0.0284 |        3 |
| E1lora | dinov2_s_lora | fruit12_apple  |     10 | 0.6525 ± 0.0870 | 0.6457 ± 0.0809 | 0.2862 ± 0.0700 |        3 |
| E1lora | dinov2_s_lora | fruit12_apple  |     50 | 0.6777 ± 0.0734 | 0.6790 ± 0.0731 | 0.2736 ± 0.0544 |        3 |
| E1lora | dinov2_s_lora | fruit12_banana |      1 | 0.3904 ± 0.0661 | 0.3343 ± 0.0454 | 0.5453 ± 0.0503 |        3 |
| E1lora | dinov2_s_lora | fruit12_banana |      5 | 0.6044 ± 0.0350 | 0.5342 ± 0.0296 | 0.3489 ± 0.0500 |        3 |
| E1lora | dinov2_s_lora | fruit12_banana |     10 | 0.7641 ± 0.0635 | 0.6587 ± 0.0567 | 0.2116 ± 0.0614 |        3 |
| E1lora | dinov2_s_lora | fruit12_banana |     50 | 0.9074 ± 0.0116 | 0.8310 ± 0.0193 | 0.0786 ± 0.0126 |        3 |
| E1lora | dinov2_s_lora | fruit12_mango  |      1 | 0.3406 ± 0.0908 | 0.3089 ± 0.0813 | 0.4638 ± 0.0217 |        3 |
| E1lora | dinov2_s_lora | fruit12_mango  |      5 | 0.7512 ± 0.0418 | 0.7534 ± 0.0385 | 0.1957 ± 0.0507 |        3 |
| E1lora | dinov2_s_lora | fruit12_mango  |     10 | 0.8599 ± 0.0471 | 0.8615 ± 0.0466 | 0.1159 ± 0.0403 |        3 |
| E1lora | dinov2_s_lora | fruit12_mango  |     50 | 0.7585 ± 0.1926 | 0.7383 ± 0.2275 | 0.2295 ± 0.1968 |        3 |

## Zero-shot / few-shot VLM baselines

| exp              | view           | encoder                | acc             | macro_f1        | off_by_one      | unparsed_rate   | n_test            | test_ids_sha256   |   n_runs |
|:-----------------|:---------------|:-----------------------|:----------------|:----------------|:----------------|:----------------|:------------------|:------------------|---------:|
| B1_clip_zeroshot | banana3        | clip-vit-large-patch14 | 0.3989 ± 0.0000 | 0.2767 ± 0.0000 | 0.2978 ± 0.0000 | NA              | 178.0000 ± 0.0000 | d19e7959b3742cdc  |        1 |
| B1_clip_zeroshot | banana4        | clip-vit-large-patch14 | 0.6472 ± 0.0000 | 0.6043 ± 0.0000 | 0.3528 ± 0.0000 | NA              | 377.0000 ± 0.0000 | 9ea1b14112408081  |        1 |
| B1_clip_zeroshot | field4_banana  | clip-vit-large-patch14 | 0.3875 ± 0.0000 | 0.3458 ± 0.0000 | 0.6125 ± 0.0000 | NA              | 400.0000 ± 0.0000 | 2e9d7b7ff2b398a0  |        1 |
| B1_clip_zeroshot | field4_mango   | clip-vit-large-patch14 | 0.3325 ± 0.0000 | 0.3303 ± 0.0000 | 0.6675 ± 0.0000 | NA              | 400.0000 ± 0.0000 | fe7deb0522736dac  |        1 |
| B1_clip_zeroshot | fruit12_apple  | clip-vit-large-patch14 | 0.6085 ± 0.0000 | 0.6128 ± 0.0000 | 0.3349 ± 0.0000 | NA              | 212.0000 ± 0.0000 | afa277c8c152e9a9  |        1 |
| B1_clip_zeroshot | fruit12_banana | clip-vit-large-patch14 | 0.3163 ± 0.0000 | 0.2989 ± 0.0000 | 0.4345 ± 0.0000 | NA              | 313.0000 ± 0.0000 | ad6fc465eb2f6954  |        1 |
| B1_clip_zeroshot | fruit12_mango  | clip-vit-large-patch14 | 0.6449 ± 0.0000 | 0.5877 ± 0.0000 | 0.2826 ± 0.0000 | NA              | 138.0000 ± 0.0000 | 6104495893c0fa40  |        1 |
| B1_clip_zeroshot | mango_khir     | clip-vit-large-patch14 | 0.9384 ± 0.0000 | 0.3967 ± 0.0000 | 0.0479 ± 0.0000 | NA              | 146.0000 ± 0.0000 | fba88d573ce5f762  |        1 |
| B1_clip_zeroshot | ninepeach      | clip-vit-large-patch14 | 0.2902 ± 0.0000 | 0.1500 ± 0.0000 | 0.7098 ± 0.0000 | NA              | 379.0000 ± 0.0000 | 8875dd6b7fee6ace  |        1 |
| B1_clip_zeroshot | raspgrade      | clip-vit-large-patch14 | 0.2036 ± 0.0000 | 0.1075 ± 0.0000 | 0.4887 ± 0.0000 | NA              | 221.0000 ± 0.0000 | 50bed6a89c5f6610  |        1 |
| B2_qwen_5shot    | banana3        | Qwen2-VL-7B-Instruct   | 0.7667 ± 0.0000 | 0.7593 ± 0.0000 | 0.2250 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | d6682e82ae7a8066  |        1 |
| B2_qwen_5shot    | banana4        | Qwen2-VL-7B-Instruct   | 0.9417 ± 0.0000 | 0.9412 ± 0.0000 | 0.0583 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 88c2380550adcc76  |        1 |
| B2_qwen_5shot    | field4_banana  | Qwen2-VL-7B-Instruct   | 0.9917 ± 0.0000 | 0.9917 ± 0.0000 | 0.0083 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | daa56ffff1bb428d  |        1 |
| B2_qwen_5shot    | field4_mango   | Qwen2-VL-7B-Instruct   | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 88c057d56eb7a0cf  |        1 |
| B2_qwen_5shot    | fruit12_apple  | Qwen2-VL-7B-Instruct   | 0.6333 ± 0.0000 | 0.5874 ± 0.0000 | 0.2833 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 676a1335e3dfa7fb  |        1 |
| B2_qwen_5shot    | fruit12_banana | Qwen2-VL-7B-Instruct   | 0.4917 ± 0.0000 | 0.4364 ± 0.0000 | 0.2167 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 1cac724512211017  |        1 |
| B2_qwen_5shot    | fruit12_mango  | Qwen2-VL-7B-Instruct   | 0.7500 ± 0.0000 | 0.7520 ± 0.0000 | 0.1333 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 88440929d0c55470  |        1 |
| B2_qwen_zeroshot | banana3        | Qwen2-VL-7B-Instruct   | 0.6000 ± 0.0000 | 0.5696 ± 0.0000 | 0.3250 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | d6682e82ae7a8066  |        1 |
| B2_qwen_zeroshot | banana4        | Qwen2-VL-7B-Instruct   | 0.9250 ± 0.0000 | 0.9240 ± 0.0000 | 0.0750 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 88c2380550adcc76  |        1 |
| B2_qwen_zeroshot | field4_banana  | Qwen2-VL-7B-Instruct   | 0.9833 ± 0.0000 | 0.9833 ± 0.0000 | 0.0167 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | daa56ffff1bb428d  |        1 |
| B2_qwen_zeroshot | field4_mango   | Qwen2-VL-7B-Instruct   | 0.7750 ± 0.0000 | 0.7630 ± 0.0000 | 0.2250 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 88c057d56eb7a0cf  |        1 |
| B2_qwen_zeroshot | fruit12_apple  | Qwen2-VL-7B-Instruct   | 0.5833 ± 0.0000 | 0.5422 ± 0.0000 | 0.3917 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 676a1335e3dfa7fb  |        1 |
| B2_qwen_zeroshot | fruit12_banana | Qwen2-VL-7B-Instruct   | 0.5333 ± 0.0000 | 0.4729 ± 0.0000 | 0.1917 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 1cac724512211017  |        1 |
| B2_qwen_zeroshot | fruit12_mango  | Qwen2-VL-7B-Instruct   | 0.7917 ± 0.0000 | 0.7707 ± 0.0000 | 0.1250 ± 0.0000 | 0.0000 ± 0.0000 | 120.0000 ± 0.0000 | 88440929d0c55470  |        1 |

## Negative controls (must not exceed chance)

| view           | encoder   | control         |   shot | acc             | macro_f1        |   n_runs |
|:---------------|:----------|:----------------|-------:|:----------------|:----------------|---------:|
| banana3        | clip_b    | random_features |      5 | 0.3390 ± 0.0803 | 0.3311 ± 0.0698 |        3 |
| banana3        | clip_b    | shuffle_labels  |      5 | 0.1835 ± 0.0702 | 0.1755 ± 0.0567 |        3 |
| banana3        | dinov2_b  | random_features |      5 | 0.3390 ± 0.0803 | 0.3311 ± 0.0698 |        3 |
| banana3        | dinov2_b  | shuffle_labels  |      5 | 0.1367 ± 0.0141 | 0.1384 ± 0.0140 |        3 |
| banana3        | dinov2_s  | random_features |      5 | 0.3951 ± 0.0568 | 0.3762 ± 0.0589 |        3 |
| banana3        | dinov2_s  | shuffle_labels  |      5 | 0.1330 ± 0.0227 | 0.1307 ± 0.0243 |        3 |
| banana3        | resnet50  | random_features |      5 | 0.3708 ± 0.0393 | 0.3635 ± 0.0328 |        3 |
| banana3        | resnet50  | shuffle_labels  |      5 | 0.2004 ± 0.0141 | 0.1984 ± 0.0141 |        3 |
| banana4        | clip_b    | random_features |      5 | 0.3572 ± 0.0177 | 0.3491 ± 0.0175 |        3 |
| banana4        | clip_b    | shuffle_labels  |      5 | 0.0274 ± 0.0077 | 0.0261 ± 0.0078 |        3 |
| banana4        | dinov2_b  | random_features |      5 | 0.3572 ± 0.0177 | 0.3491 ± 0.0175 |        3 |
| banana4        | dinov2_b  | shuffle_labels  |      5 | 0.0177 ± 0.0241 | 0.0156 ± 0.0208 |        3 |
| banana4        | dinov2_s  | random_features |      5 | 0.3360 ± 0.0246 | 0.3318 ± 0.0214 |        3 |
| banana4        | dinov2_s  | shuffle_labels  |      5 | 0.0159 ± 0.0096 | 0.0144 ± 0.0080 |        3 |
| banana4        | resnet50  | random_features |      5 | 0.3298 ± 0.0366 | 0.3212 ± 0.0301 |        3 |
| banana4        | resnet50  | shuffle_labels  |      5 | 0.0964 ± 0.0452 | 0.0791 ± 0.0350 |        3 |
| field4_banana  | clip_b    | random_features |      5 | 0.5153 ± 0.0167 | 0.5086 ± 0.0109 |        3 |
| field4_banana  | clip_b    | shuffle_labels  |      5 | 0.2173 ± 0.0813 | 0.1885 ± 0.0697 |        3 |
| field4_banana  | dinov2_b  | random_features |      5 | 0.5153 ± 0.0167 | 0.5086 ± 0.0109 |        3 |
| field4_banana  | dinov2_b  | shuffle_labels  |      5 | 0.1927 ± 0.1252 | 0.1695 ± 0.1019 |        3 |
| field4_banana  | dinov2_s  | random_features |      5 | 0.5000 ± 0.0164 | 0.4980 ± 0.0145 |        3 |
| field4_banana  | dinov2_s  | shuffle_labels  |      5 | 0.2460 ± 0.0572 | 0.2088 ± 0.0503 |        3 |
| field4_banana  | resnet50  | random_features |      5 | 0.4953 ± 0.0237 | 0.4953 ± 0.0238 |        3 |
| field4_banana  | resnet50  | shuffle_labels  |      5 | 0.1733 ± 0.0403 | 0.1594 ± 0.0293 |        3 |
| field4_mango   | clip_b    | random_features |      5 | 0.5087 ± 0.0220 | 0.4949 ± 0.0333 |        3 |
| field4_mango   | clip_b    | shuffle_labels  |      5 | 0.0400 ± 0.0072 | 0.0386 ± 0.0070 |        3 |
| field4_mango   | dinov2_b  | random_features |      5 | 0.5087 ± 0.0220 | 0.4949 ± 0.0333 |        3 |
| field4_mango   | dinov2_b  | shuffle_labels  |      5 | 0.0080 ± 0.0080 | 0.0079 ± 0.0079 |        3 |
| field4_mango   | dinov2_s  | random_features |      5 | 0.5020 ± 0.0203 | 0.4941 ± 0.0258 |        3 |
| field4_mango   | dinov2_s  | shuffle_labels  |      5 | 0.0200 ± 0.0183 | 0.0198 ± 0.0181 |        3 |
| field4_mango   | resnet50  | random_features |      5 | 0.4907 ± 0.0240 | 0.4889 ± 0.0239 |        3 |
| field4_mango   | resnet50  | shuffle_labels  |      5 | 0.0460 ± 0.0288 | 0.0443 ± 0.0268 |        3 |
| fruit12_apple  | clip_b    | random_features |      5 | 0.3333 ± 0.0237 | 0.3265 ± 0.0248 |        3 |
| fruit12_apple  | clip_b    | shuffle_labels  |      5 | 0.2343 ± 0.0384 | 0.2297 ± 0.0304 |        3 |
| fruit12_apple  | dinov2_b  | random_features |      5 | 0.3333 ± 0.0237 | 0.3265 ± 0.0248 |        3 |
| fruit12_apple  | dinov2_b  | shuffle_labels  |      5 | 0.2075 ± 0.0125 | 0.2010 ± 0.0098 |        3 |
| fruit12_apple  | dinov2_s  | random_features |      5 | 0.3333 ± 0.0307 | 0.3133 ± 0.0321 |        3 |
| fruit12_apple  | dinov2_s  | shuffle_labels  |      5 | 0.2028 ± 0.0330 | 0.2013 ± 0.0310 |        3 |
| fruit12_apple  | resnet50  | random_features |      5 | 0.3318 ± 0.0054 | 0.3100 ± 0.0125 |        3 |
| fruit12_apple  | resnet50  | shuffle_labels  |      5 | 0.1840 ± 0.0377 | 0.1833 ± 0.0395 |        3 |
| fruit12_banana | clip_b    | random_features |      5 | 0.3014 ± 0.0533 | 0.2525 ± 0.0173 |        3 |
| fruit12_banana | clip_b    | shuffle_labels  |      5 | 0.2523 ± 0.0985 | 0.2154 ± 0.0636 |        3 |
| fruit12_banana | dinov2_b  | random_features |      5 | 0.3014 ± 0.0533 | 0.2525 ± 0.0173 |        3 |
| fruit12_banana | dinov2_b  | shuffle_labels  |      5 | 0.1836 ± 0.0361 | 0.1507 ± 0.0335 |        3 |
| fruit12_banana | dinov2_s  | random_features |      5 | 0.3146 ± 0.0096 | 0.2656 ± 0.0066 |        3 |
| fruit12_banana | dinov2_s  | shuffle_labels  |      5 | 0.2076 ± 0.0458 | 0.1597 ± 0.0401 |        3 |
| fruit12_banana | resnet50  | random_features |      5 | 0.3437 ± 0.0590 | 0.2791 ± 0.0347 |        3 |
| fruit12_banana | resnet50  | shuffle_labels  |      5 | 0.2471 ± 0.0613 | 0.1928 ± 0.0305 |        3 |
| fruit12_mango  | clip_b    | random_features |      5 | 0.3382 ± 0.0182 | 0.3366 ± 0.0161 |        3 |
| fruit12_mango  | clip_b    | shuffle_labels  |      5 | 0.2005 ± 0.0586 | 0.1920 ± 0.0660 |        3 |
| fruit12_mango  | dinov2_b  | random_features |      5 | 0.3382 ± 0.0182 | 0.3366 ± 0.0161 |        3 |
| fruit12_mango  | dinov2_b  | shuffle_labels  |      5 | 0.1763 ± 0.0544 | 0.1636 ± 0.0657 |        3 |
| fruit12_mango  | dinov2_s  | random_features |      5 | 0.2923 ± 0.0293 | 0.2896 ± 0.0299 |        3 |
| fruit12_mango  | dinov2_s  | shuffle_labels  |      5 | 0.1546 ± 0.0399 | 0.1500 ± 0.0407 |        3 |
| fruit12_mango  | resnet50  | random_features |      5 | 0.3382 ± 0.0399 | 0.3357 ± 0.0436 |        3 |
| fruit12_mango  | resnet50  | shuffle_labels  |      5 | 0.1618 ± 0.0858 | 0.1532 ± 0.0827 |        3 |
| mango_khir     | clip_b    | random_features |      5 | 0.2717 ± 0.0979 | 0.1768 ± 0.0507 |        3 |
| mango_khir     | clip_b    | shuffle_labels  |      5 | 0.0982 ± 0.0324 | 0.0907 ± 0.0543 |        3 |
| mango_khir     | dinov2_b  | random_features |      5 | 0.2717 ± 0.0979 | 0.1768 ± 0.0507 |        3 |
| mango_khir     | dinov2_b  | shuffle_labels  |      5 | 0.0639 ± 0.0285 | 0.0852 ± 0.0719 |        3 |
| mango_khir     | dinov2_s  | random_features |      5 | 0.3059 ± 0.0811 | 0.1949 ± 0.0338 |        3 |
| mango_khir     | dinov2_s  | shuffle_labels  |      5 | 0.0776 ± 0.0259 | 0.1020 ± 0.0964 |        3 |
| mango_khir     | resnet50  | random_features |      5 | 0.3311 ± 0.0910 | 0.2141 ± 0.0488 |        3 |
| mango_khir     | resnet50  | shuffle_labels  |      5 | 0.2169 ± 0.1478 | 0.1532 ± 0.0178 |        3 |
| ninepeach      | clip_b    | random_features |      5 | 0.3384 ± 0.0083 | 0.3175 ± 0.0224 |        3 |
| ninepeach      | clip_b    | shuffle_labels  |      5 | 0.1906 ± 0.0995 | 0.1970 ± 0.0968 |        3 |
| ninepeach      | dinov2_b  | random_features |      5 | 0.3384 ± 0.0083 | 0.3175 ± 0.0224 |        3 |
| ninepeach      | dinov2_b  | shuffle_labels  |      5 | 0.1268 ± 0.0367 | 0.1359 ± 0.0356 |        3 |
| ninepeach      | dinov2_s  | random_features |      5 | 0.3021 ± 0.0069 | 0.2994 ± 0.0102 |        3 |
| ninepeach      | dinov2_s  | shuffle_labels  |      5 | 0.1281 ± 0.0369 | 0.1328 ± 0.0330 |        3 |
| ninepeach      | resnet50  | random_features |      5 | 0.3321 ± 0.0383 | 0.3230 ± 0.0319 |        3 |
| ninepeach      | resnet50  | shuffle_labels  |      5 | 0.0758 ± 0.0141 | 0.0817 ± 0.0163 |        3 |
| raspgrade      | clip_b    | random_features |      5 | 0.1840 ± 0.0392 | 0.1209 ± 0.0139 |        3 |
| raspgrade      | clip_b    | shuffle_labels  |      5 | 0.2477 ± 0.0709 | 0.1491 ± 0.0211 |        3 |
| raspgrade      | dinov2_b  | random_features |      5 | 0.1840 ± 0.0392 | 0.1209 ± 0.0139 |        3 |
| raspgrade      | dinov2_b  | shuffle_labels  |      5 | 0.2632 ± 0.1207 | 0.1432 ± 0.0420 |        3 |
| raspgrade      | dinov2_s  | random_features |      5 | 0.1703 ± 0.0096 | 0.1181 ± 0.0031 |        3 |
| raspgrade      | dinov2_s  | shuffle_labels  |      5 | 0.2268 ± 0.0999 | 0.1301 ± 0.0414 |        3 |
| raspgrade      | resnet50  | random_features |      5 | 0.2555 ± 0.0557 | 0.1479 ± 0.0108 |        3 |
| raspgrade      | resnet50  | shuffle_labels  |      5 | 0.2218 ± 0.0845 | 0.1280 ± 0.0172 |        3 |

`shuffle_labels` rotates the class names of the support set by a non-zero offset: every
support label changes and the class multiset is preserved, so the head can exploit only
feature geometry. Expect macro-F1 at or *below* 1/C -- below is normal, because the
rotation maps each class to a specific wrong one and the test split is imbalanced. What
matters is that it never exceeds chance. `random_features` keeps the labels and replaces
the features with Gaussian noise. Judge both on macro-F1 (chance = 1/C); accuracy has a
high floor on these splits.


## Efficiency (E5)

| kind      | name              | timm_id                          |           params |   latency_ms_b1 |   peak_mem_mb_b32 | gpu                     | note                                       |
|:----------|:------------------|:---------------------------------|-----------------:|----------------:|------------------:|:------------------------|:-------------------------------------------|
| encoder   | dinov2_s          | vit_small_patch14_dinov2.lvd142m |      2.16288e+07 |            4.87 |             254.1 | NVIDIA GeForce RTX 4090 | nan                                        |
| encoder   | dinov2_b          | vit_base_patch14_dinov2.lvd142m  |      8.57249e+07 |            4.96 |             643.2 | NVIDIA GeForce RTX 4090 | nan                                        |
| encoder   | clip_b            | vit_base_patch16_clip_224.openai |      8.57994e+07 |            4.43 |             576   | NVIDIA GeForce RTX 4090 | nan                                        |
| encoder   | resnet50          | resnet50.a1_in1k                 |      2.3508e+07  |            5.21 |             435.5 | NVIDIA GeForce RTX 4090 | nan                                        |
| head      | linear_probe      |                                  |   1155           |          nan    |             nan   | NVIDIA GeForce RTX 4090 | nan                                        |
| head      | prototype         |                                  |      0           |          nan    |             nan   | NVIDIA GeForce RTX 4090 | nan                                        |
| head      | lora_r8           |                                  | 228960           |          nan    |             nan   | NVIDIA GeForce RTX 4090 | nan                                        |
| train_mem | finetune_resnet50 |                                  |    nan           |          nan    |            1645.8 | NVIDIA GeForce RTX 4090 | one training step, batch 16 (repo default) |
| train_mem | lora_dinov2_s     |                                  |    nan           |          nan    |             965.1 | NVIDIA GeForce RTX 4090 | one training step, batch 16 (repo default) |
| head      | finetune_resnet50 |                                  |      2.3508e+07  |          nan    |             nan   | NVIDIA GeForce RTX 4090 | nan                                        |

Latency is encoder-only, batch 1, median of 20 passes after warm-up, with a CUDA synchronisation around each pass. It excludes image decoding and is a relative comparison, not a deployment figure. At batch 1 the time is dominated by launch overhead, so a 4x smaller ViT is *not* 4x faster -- dinov2_s and dinov2_b come out within ~2 ms of each other. Read `params` and `peak_mem_mb_b32` for the cost story, not `latency_ms_b1`. If this table was produced while another job was using the CPU, the launch-bound numbers are inflated; the driver re-measures it with an idle card at the end of every cycle.


## Plan v2.0 analyses (arm difficulty, family flip, score families, adjacent-grade rejection, collapse and thin cells)

Computed by `analyze_v2.py` from the stored score arrays; the file is reproduced here verbatim so REPORT.md is self-contained.

# Plan v2.0 analyses computed from stored score arrays

Generated by `analyze_v2.py`. Every number here is recomputed from `results/*.json` + `results/scores/*.npz`; nothing is typed by hand.

Definitions that travel with the numbers:

- a **cell** = (view, encoder, variant, protocol, unknown, shot, seed); `n_cells` counts them, `n_runs` counts result files (they differ only where a variant or head is part of the run but not of the cell key).

- **family** prob = {msp, energy}; dist = {mahalanobis, knn}.

- **`delta_pp` = (reject rate on the ADJACENT grade − reject rate on the DISTANT grade) × 100**. A NEGATIVE value is the desirable direction: the score rejects far grades more often than near ones. Read the sign before reading the size.

- a view with fewer than 30 test images on either side is thin: E2 skips those cells and T16 lists them; their numbers are descriptive only.

## T11_auroc_by_arm

| arm                | family   |   n_cells |   n_runs |   auroc_mean |   auroc_sd |   oscr_mean |   fpr95_mean | arm_desc                                                  |
|:-------------------|:---------|----------:|---------:|-------------:|-----------:|------------:|-------------:|:----------------------------------------------------------|
| P1_out_of_grade    | dist     |   14.0000 | 168.0000 |       0.7603 |     0.1269 |      0.6181 |       0.7494 | P1 terminal level out-of-grade                            |
| P1_out_of_grade    | prob     |   14.0000 | 168.0000 |       0.5534 |     0.1658 |      0.4646 |       0.9242 | P1 terminal level out-of-grade                            |
| P2_leave_one_fruit | dist     |   10.0000 | 120.0000 |       0.9585 |     0.0551 |      0.8006 |       0.1985 | P2_leave_one_fruit                                        |
| P2_leave_one_fruit | prob     |   10.0000 | 120.0000 |       0.8779 |     0.1063 |      0.7409 |       0.4808 | P2_leave_one_fruit                                        |
| P2_unseen_interior | dist     |   32.0000 | 384.0000 |       0.6310 |     0.1461 |      0.5449 |       0.8646 | P2 unseen grade (incl. first)                             |
| P2_unseen_interior | prob     |   32.0000 | 384.0000 |       0.6302 |     0.1740 |      0.5646 |       0.8616 | P2 unseen grade (incl. first)                             |
| P2c_unseen_species | dist     |    6.0000 |  72.0000 |       0.8909 |     0.0639 |      0.6546 |       0.5123 | P2 leave-one-species-out (fruit12; species, NOT cultivar) |
| P2c_unseen_species | prob     |    6.0000 |  72.0000 |       0.6575 |     0.1093 |      0.5200 |       0.8939 | P2 leave-one-species-out (fruit12; species, NOT cultivar) |
| P3_foreign         | dist     |    8.0000 |  96.0000 |       0.9822 |     0.0236 |      0.8287 |       0.0926 | P3b cross-dataset foreign fruit                           |
| P3_foreign         | prob     |    8.0000 |  96.0000 |       0.7977 |     0.1387 |      0.7068 |       0.6482 | P3b cross-dataset foreign fruit                           |
| P3_rotten          | dist     |   12.0000 | 144.0000 |       0.8320 |     0.1395 |      0.7163 |       0.5737 | P3a decayed class                                         |
| P3_rotten          | prob     |   12.0000 | 144.0000 |       0.6318 |     0.1911 |      0.5660 |       0.8198 | P3a decayed class                                         |

## T11b_auroc_by_arm_score

| arm                | score       |   n_cells |   n_runs |   auroc_mean |   auroc_sd |   auroc_min |   auroc_max | arm_desc                                                  |
|:-------------------|:------------|----------:|---------:|-------------:|-----------:|------------:|------------:|:----------------------------------------------------------|
| P1_out_of_grade    | energy      |   14.0000 |  84.0000 |       0.5547 |     0.1650 |      0.1269 |      0.8562 | P1 terminal level out-of-grade                            |
| P1_out_of_grade    | knn         |   14.0000 |  84.0000 |       0.7523 |     0.1304 |      0.4051 |      0.9285 | P1 terminal level out-of-grade                            |
| P1_out_of_grade    | mahalanobis |   14.0000 |  84.0000 |       0.7682 |     0.1235 |      0.4450 |      0.9427 | P1 terminal level out-of-grade                            |
| P1_out_of_grade    | msp         |   14.0000 |  84.0000 |       0.5521 |     0.1675 |      0.1269 |      0.8562 | P1 terminal level out-of-grade                            |
| P2_leave_one_fruit | energy      |   10.0000 |  60.0000 |       0.8740 |     0.1110 |      0.5592 |      0.9944 | P2_leave_one_fruit                                        |
| P2_leave_one_fruit | knn         |   10.0000 |  60.0000 |       0.9562 |     0.0687 |      0.7261 |      1.0000 | P2_leave_one_fruit                                        |
| P2_leave_one_fruit | mahalanobis |   10.0000 |  60.0000 |       0.9608 |     0.0373 |      0.8504 |      0.9999 | P2_leave_one_fruit                                        |
| P2_leave_one_fruit | msp         |   10.0000 |  60.0000 |       0.8818 |     0.1021 |      0.6147 |      0.9942 | P2_leave_one_fruit                                        |
| P2_unseen_interior | energy      |   32.0000 | 192.0000 |       0.6312 |     0.1731 |      0.1710 |      0.9900 | P2 unseen grade (incl. first)                             |
| P2_unseen_interior | knn         |   32.0000 | 192.0000 |       0.6221 |     0.1521 |      0.3244 |      0.9700 | P2 unseen grade (incl. first)                             |
| P2_unseen_interior | mahalanobis |   32.0000 | 192.0000 |       0.6399 |     0.1396 |      0.3264 |      0.9483 | P2 unseen grade (incl. first)                             |
| P2_unseen_interior | msp         |   32.0000 | 192.0000 |       0.6293 |     0.1754 |      0.1710 |      0.9900 | P2 unseen grade (incl. first)                             |
| P2c_unseen_species | energy      |    6.0000 |  36.0000 |       0.6668 |     0.1079 |      0.3780 |      0.7982 | P2 leave-one-species-out (fruit12; species, NOT cultivar) |
| P2c_unseen_species | knn         |    6.0000 |  36.0000 |       0.8969 |     0.0638 |      0.7637 |      0.9768 | P2 leave-one-species-out (fruit12; species, NOT cultivar) |
| P2c_unseen_species | mahalanobis |    6.0000 |  36.0000 |       0.8848 |     0.0644 |      0.7583 |      0.9688 | P2 leave-one-species-out (fruit12; species, NOT cultivar) |
| P2c_unseen_species | msp         |    6.0000 |  36.0000 |       0.6483 |     0.1114 |      0.3862 |      0.7811 | P2 leave-one-species-out (fruit12; species, NOT cultivar) |
| P3_foreign         | energy      |    8.0000 |  48.0000 |       0.8083 |     0.1361 |      0.5390 |      0.9923 | P3b cross-dataset foreign fruit                           |
| P3_foreign         | knn         |    8.0000 |  48.0000 |       0.9801 |     0.0290 |      0.8293 |      1.0000 | P3b cross-dataset foreign fruit                           |
| P3_foreign         | mahalanobis |    8.0000 |  48.0000 |       0.9842 |     0.0166 |      0.9278 |      1.0000 | P3b cross-dataset foreign fruit                           |
| P3_foreign         | msp         |    8.0000 |  48.0000 |       0.7872 |     0.1418 |      0.5487 |      0.9900 | P3b cross-dataset foreign fruit                           |
| P3_rotten          | energy      |   12.0000 |  72.0000 |       0.6593 |     0.1864 |      0.2742 |      0.9143 | P3a decayed class                                         |
| P3_rotten          | knn         |   12.0000 |  72.0000 |       0.8239 |     0.1425 |      0.4587 |      0.9871 | P3a decayed class                                         |
| P3_rotten          | mahalanobis |   12.0000 |  72.0000 |       0.8402 |     0.1369 |      0.5118 |      0.9902 | P3a decayed class                                         |
| P3_rotten          | msp         |   12.0000 |  72.0000 |       0.6044 |     0.1931 |      0.2862 |      0.9195 | P3a decayed class                                         |

## T12_family_flip

| hidden_at   | family   |   n_cells |   n_runs |   auroc_mean |   auroc_sd |
|:------------|:---------|----------:|---------:|-------------:|-----------:|
| first       | dist     |   16.0000 | 192.0000 |       0.6568 |     0.1454 |
| first       | prob     |   16.0000 | 192.0000 |       0.5680 |     0.1546 |
| last        | dist     |   14.0000 | 168.0000 |       0.7603 |     0.1269 |
| last        | prob     |   14.0000 | 168.0000 |       0.5534 |     0.1658 |
| middle      | dist     |   16.0000 | 192.0000 |       0.6052 |     0.1426 |
| middle      | prob     |   16.0000 | 192.0000 |       0.6925 |     0.1704 |

## T12b_family_flip_by_view

| view           | hidden_at   |   dist |   prob |   dist_minus_prob | better_family   |
|:---------------|:------------|-------:|-------:|------------------:|:----------------|
| banana3        | first       | 0.5164 | 0.5902 |           -0.0738 | prob            |
| banana4        | first       | 0.8504 | 0.5296 |            0.3208 | dist            |
| fruit12_apple  | first       | 0.6243 | 0.5306 |            0.0937 | dist            |
| fruit12_banana | first       | 0.5969 | 0.7161 |           -0.1192 | prob            |
| fruit12_mango  | first       | 0.6093 | 0.6232 |           -0.0139 | prob            |
| mango_khir     | first       | 0.7560 | 0.6719 |            0.0841 | dist            |
| ninepeach      | first       | 0.8139 | 0.3019 |            0.5119 | dist            |
| raspgrade      | first       | 0.4869 | 0.5802 |           -0.0932 | prob            |
| banana3        | last        | 0.8664 | 0.4952 |            0.3712 | dist            |
| banana4        | last        | 0.8551 | 0.5627 |            0.2924 | dist            |
| fruit12_apple  | last        | 0.7186 | 0.6585 |            0.0602 | dist            |
| fruit12_banana | last        | 0.8080 | 0.6971 |            0.1110 | dist            |
| fruit12_mango  | last        | 0.8591 | 0.6341 |            0.2251 | dist            |
| ninepeach      | last        | 0.6775 | 0.3339 |            0.3436 | dist            |
| raspgrade      | last        | 0.5370 | 0.4926 |            0.0444 | dist            |
| banana3        | middle      | 0.4672 | 0.6739 |           -0.2067 | prob            |
| banana4        | middle      | 0.7128 | 0.8971 |           -0.1843 | prob            |
| fruit12_apple  | middle      | 0.6372 | 0.6904 |           -0.0533 | prob            |
| fruit12_banana | middle      | 0.6546 | 0.6204 |            0.0343 | dist            |
| fruit12_mango  | middle      | 0.7421 | 0.7156 |            0.0265 | dist            |
| ninepeach      | middle      | 0.4815 | 0.8584 |           -0.3769 | prob            |
| raspgrade      | middle      | 0.5733 | 0.5422 |            0.0312 | dist            |

## T13_score_corr

| score_a     | score_b     | family_a   | family_b   | same_family   | subset   |   n_cells |   spearman |   pearson |   median_abs_diff |   frac_identical |
|:------------|:------------|:-----------|:-----------|:--------------|:---------|----------:|-----------:|----------:|------------------:|-----------------:|
| energy      | knn         | prob       | dist       | False         | all      |       246 |     0.4408 |    0.3804 |            0.1411 |           0.0000 |
| energy      | knn         | prob       | dist       | False         | known=2  |       114 |    -0.2471 |   -0.2810 |            0.1685 |           0.0000 |
| energy      | knn         | prob       | dist       | False         | known>=3 |        24 |     0.0339 |    0.0209 |            0.0387 |           0.0000 |
| energy      | mahalanobis | prob       | dist       | False         | all      |       246 |     0.5212 |    0.4672 |            0.1500 |           0.0000 |
| energy      | mahalanobis | prob       | dist       | False         | known=2  |       114 |    -0.1047 |   -0.1085 |            0.1648 |           0.0000 |
| energy      | mahalanobis | prob       | dist       | False         | known>=3 |        24 |     0.3557 |    0.3778 |            0.0407 |           0.0000 |
| mahalanobis | knn         | dist       | dist       | True          | all      |       246 |     0.9715 |    0.9682 |            0.0251 |           0.0122 |
| mahalanobis | knn         | dist       | dist       | True          | known=2  |       114 |     0.9297 |    0.9286 |            0.0431 |           0.0000 |
| mahalanobis | knn         | dist       | dist       | True          | known>=3 |        24 |     0.8383 |    0.8075 |            0.0133 |           0.0000 |
| msp         | energy      | prob       | prob       | True          | all      |       246 |     0.9327 |    0.9422 |            0.0020 |           0.4634 |
| msp         | energy      | prob       | prob       | True          | known=2  |       114 |     1.0000 |    1.0000 |            0.0000 |           1.0000 |
| msp         | energy      | prob       | prob       | True          | known>=3 |        24 |     0.8113 |    0.8072 |            0.0156 |           0.0000 |
| msp         | knn         | prob       | dist       | False         | all      |       246 |     0.3613 |    0.3104 |            0.1702 |           0.0000 |
| msp         | knn         | prob       | dist       | False         | known=2  |       114 |    -0.2471 |   -0.2810 |            0.1685 |           0.0000 |
| msp         | knn         | prob       | dist       | False         | known>=3 |        24 |    -0.0226 |   -0.1484 |            0.0343 |           0.0000 |
| msp         | mahalanobis | prob       | dist       | False         | all      |       246 |     0.4632 |    0.4133 |            0.1695 |           0.0000 |
| msp         | mahalanobis | prob       | dist       | False         | known=2  |       114 |    -0.1047 |   -0.1085 |            0.1648 |           0.0000 |
| msp         | mahalanobis | prob       | dist       | False         | known>=3 |        24 |     0.2609 |    0.2212 |            0.0423 |           0.0000 |

## T14_adjacent

| protocol           | family   |   n_cells |   delta_pp_mean |   pct_cells_positive |
|:-------------------|:---------|----------:|----------------:|---------------------:|
| P1_out_of_grade    | dist     |   42.0000 |          0.7178 |              52.9762 |
| P1_out_of_grade    | prob     |   42.0000 |          0.8274 |              36.9048 |
| P2_unseen_interior | dist     |   54.0000 |         -1.0139 |              48.1481 |
| P2_unseen_interior | prob     |   54.0000 |         -6.7028 |              36.5741 |

## T14b_granularity

|   n_levels | family   |   n_cells |   n_views |   delta_pp_mean |   pct_cells_positive |
|-----------:|:---------|----------:|----------:|----------------:|---------------------:|
|          3 | dist     |   72.0000 |    6.0000 |          0.0385 |              53.1250 |
|          3 | prob     |   72.0000 |    6.0000 |         -4.0188 |              38.1944 |
|          5 | dist     |   24.0000 |    1.0000 |         -1.1409 |              41.6667 |
|          5 | prob     |   24.0000 |    1.0000 |         -1.5770 |              32.2917 |

## T15_collapsed

Collapsed cells: **16 runs** over 2 (view, protocol, hidden-grade) combinations.

| view       | encoder   | protocol           | unknown   |     shot |   n_runs |   known_acc |   majority_share | single_class   |
|:-----------|:----------|:-------------------|:----------|---------:|---------:|------------:|-----------------:|:---------------|
| banana3    | resnet50  | P1_out_of_grade    | overripe  |   5.0000 |        4 |      0.5446 |           0.5446 | False          |
| mango_khir | dinov2_s  | P2_unseen_interior | UnRipe    | nan      |       12 |      0.8000 |           0.8000 | True           |

## T16_small_n (threshold n >= 30 on both sides)

4 (view, protocol, hidden-grade, shot) groups fall below 30 on one side. They keep their numbers but must be labelled *descriptive* in the paper; the seed bootstrap interval is in `T16b_seed_bootstrap.csv`.

| arm                | view       | protocol           | unknown   |     shot |   n_known |   n_unknown |   n_runs |   auroc_mean |   auroc_min |   auroc_max |
|:-------------------|:-----------|:-------------------|:----------|---------:|----------:|------------:|---------:|-------------:|------------:|------------:|
| P1_out_of_grade    | raspgrade  | P1_out_of_grade    | grade5    |   5.0000 |  720.0000 |     12.0000 |  24.0000 |       0.5369 |      0.4051 |      0.6633 |
| P1_out_of_grade    | raspgrade  | P1_out_of_grade    | grade5    | nan      |  720.0000 |     12.0000 |  24.0000 |       0.4927 |      0.3438 |      0.6115 |
| P2_unseen_interior | mango_khir | P2_unseen_interior | UnRipe    |   5.0000 |   10.0000 |    136.0000 |  24.0000 |       0.7169 |      0.5904 |      0.8699 |
| P2_unseen_interior | mango_khir | P2_unseen_interior | UnRipe    | nan      |   10.0000 |    136.0000 |  24.0000 |       0.7110 |      0.6338 |      0.7956 |

### Seed bootstrap CI for the thin cells (unit = seed)

| view       | encoder   | protocol           | unknown   | score       |   shot |   n_seeds |   mean |     lo |     hi |
|:-----------|:----------|:-------------------|:----------|:------------|-------:|----------:|-------:|-------:|-------:|
| mango_khir | dinov2_s  | P2_unseen_interior | UnRipe    | energy      | 5.0000 |         3 | 0.7189 | 0.6801 | 0.7941 |
| mango_khir | dinov2_s  | P2_unseen_interior | UnRipe    | knn         | 5.0000 |         3 | 0.8145 | 0.7971 | 0.8375 |
| mango_khir | dinov2_s  | P2_unseen_interior | UnRipe    | mahalanobis | 5.0000 |         3 | 0.8093 | 0.7250 | 0.8699 |
| mango_khir | dinov2_s  | P2_unseen_interior | UnRipe    | msp         | 5.0000 |         3 | 0.7189 | 0.6801 | 0.7941 |
| mango_khir | resnet50  | P2_unseen_interior | UnRipe    | energy      | 5.0000 |         3 | 0.6260 | 0.5904 | 0.6625 |
| mango_khir | resnet50  | P2_unseen_interior | UnRipe    | knn         | 5.0000 |         3 | 0.7125 | 0.6699 | 0.7515 |
| mango_khir | resnet50  | P2_unseen_interior | UnRipe    | mahalanobis | 5.0000 |         3 | 0.7088 | 0.6699 | 0.7647 |
| mango_khir | resnet50  | P2_unseen_interior | UnRipe    | msp         | 5.0000 |         3 | 0.6260 | 0.5904 | 0.6625 |
| raspgrade  | dinov2_s  | P1_out_of_grade    | grade5    | energy      | 5.0000 |         3 | 0.5428 | 0.4791 | 0.5880 |
| raspgrade  | dinov2_s  | P1_out_of_grade    | grade5    | knn         | 5.0000 |         3 | 0.4324 | 0.4051 | 0.4571 |
| raspgrade  | dinov2_s  | P1_out_of_grade    | grade5    | mahalanobis | 5.0000 |         3 | 0.4988 | 0.4712 | 0.5279 |
| raspgrade  | dinov2_s  | P1_out_of_grade    | grade5    | msp         | 5.0000 |         3 | 0.5682 | 0.4861 | 0.6429 |
| raspgrade  | resnet50  | P1_out_of_grade    | grade5    | energy      | 5.0000 |         3 | 0.5774 | 0.5328 | 0.6223 |
| raspgrade  | resnet50  | P1_out_of_grade    | grade5    | knn         | 5.0000 |         3 | 0.5289 | 0.5050 | 0.5635 |
| raspgrade  | resnet50  | P1_out_of_grade    | grade5    | mahalanobis | 5.0000 |         3 | 0.6014 | 0.5591 | 0.6633 |
| raspgrade  | resnet50  | P1_out_of_grade    | grade5    | msp         | 5.0000 |         3 | 0.5453 | 0.5160 | 0.5615 |


## Notes that must travel with these numbers

1. **MSP and Energy are rank-equivalent on two-class known sets -- and only there.**
   The earlier text here said `E = -log p_max`, which is wrong: the energy score is
   `logsumexp(z)`, a free energy, not a transform of the maximum probability. The real
   mechanism is narrower. With exactly two known classes the logits enter softmax as
   `(z1, z2)`, so `MSP = sigmoid(|z1-z2|)` and `Energy = log(2 cosh((z1-z2)/2))`; both are
   strictly increasing in `|z1-z2|`, so every rank-based statistic -- AUROC, FPR@95TPR,
   OSCR -- is *identical* for the two scores. With three or more known classes that
   identity is gone (measured: P3_foreign 0.645 vs 0.664 on the same runs). The
   consequence for the paper: on P1/P2 cells MSP and Energy are one signal, not two; the
   measured cell-level Spearman over the whole E2 grid is 0.91, not the 0.99 the plan
   quoted, and it is 1.000 exactly on the two-class cells.
2. **OSCR counts only correctly-classified accepted knowns** in the CCR term. An open-set
   method that rejects everything would otherwise score perfectly on the known side.
3. **There are four unknown arms, and P1/P2 are two instances of one operation.**
   P1 hides the terminal grade; P2 hides any non-terminal grade, *including the first*
   (the code loops `ordn[:-1]`, so "first" is a P2 case, not an extra protocol); P3a
   hides the decayed class; P3b is a cross-dataset foreign fruit. P1 and P2 are the same
   "hide one level" operation with different positions on the ordinal scale -- do not
   write them as two different phenomena. P2 needs at least three grades: hiding the
   single non-terminal grade of a two-grade view would leave one known class, which is
   not a classification problem. P3b's unknown differs in species AND camera AND
   lighting by construction (`FOREIGN_PAIRS` is deliberately cross-dataset), so a high
   P3b AUROC is "not-this-fruit AND not-this-camera" and is not attributable to foreign
   matter alone.
4. **Support is drawn from train, evaluation is on test**, and no hyper-parameter is
   selected on val, so the val split contributes nothing to any number here.
5. **The adapted arms (E1ft, E1lora) train with random crop/flip**, while the frozen
   arms see one deterministic centre crop. The asymmetry favours the adapted arms; the
   claims about frozen features are therefore conservative.
6. **Group leakage is asserted to zero on every dataset**; a non-zero count aborts the
   build. For fruit12 the group is the source photograph, not the crop.
7. **Test splits are not class-balanced, so accuracy has a high floor.** The
   `fruit12_banana` test split is 67% Ripe; a predictor that collapses to a single class
   scores acc 0.673 there with macro-F1 0.28 (this is exactly what the shuffled-label
   control does for one seed). Read macro-F1 as primary, and read the negative controls
   in macro-F1, not accuracy.
8. **FPR@95TPR is the FPR at the largest threshold whose TPR is still >= 95%**, and each
   record also stores the TPR actually reached (`tpr_at_fpr95`). The earlier definition
   (`np.percentile(known_scores, 5)`) is a different operating point and was wrong by up
   to 0.163 FPR; all E2 numbers were recomputed from the stored score arrays by
   `recompute_e2.py` (no re-training, same arrays).
9. **`VERIFY.md` is a self-consistency check only** -- it re-feeds the stored arrays into
   the same metric code. `VERIFY_INDEP.md` is the independent one: AUROC by the
   Mann-Whitney rank formula (no sklearn), FPR@95 by an explicit threshold sweep, and
   known accuracy recomputed from the stored predictions. It must report 0 violations;
   `final_check.py` fails the build otherwise.
10. **Cross-domain (E3) is binary, same-crop, controlled->field, four pairs.** The label
   map keeps Raw/Ripe only; fruit12's Overripe is dropped, and the pairs are
   banana3<->banana4 plus fruit12->field4 for banana and mango. Do not describe this as
   multi-grade or cross-crop; the numbers do not support either.
11. **Paired tests carry Bonferroni and Holm columns and a verdict.** The family size is
   the number of tests in the table itself (`n_tests_in_family`); the verdict column is
   the strict Bonferroni one. An uncorrected p<0.05 among ~32 tests is what chance
   produces, so "significant" must mean "survives correction", and the count that
   survives is the finding.
12. **Cells with fewer than 30 test images on either side are marked `thin` in T3.**
   Their AUROC is still printed (dropping it would hide data) but it is *descriptive*:
   the seed-bootstrap interval in `outputs/T16b_seed_bootstrap.csv` is the number to
   quote next to it. Known-side cells whose predictions collapse to a single class are
   listed in `outputs/T15_collapsed.csv`; their `known_acc` equals the majority share by
   construction and every open-set number computed on them is an artefact of that
   collapse.
13. **The `P2c` arm is *unseen species*, not unseen cultivar.** `fruit12`'s Apple /
   Banana / Mango differ in colour, shape and texture, so its AUROC measures species
   separability. The internal view key still reads `P2c_unseen_cultivar` (renaming it
   would change every config hash and create a second arm beside the first); every table
   here prints it as `P2c_unseen_species`, and the paper must not use the word
   "cultivar" unless NinePeach is added.


## Failures

No recorded failures.

## Unreadable result files

unreadable result files: 0

## Run inventory

exp
B1_clip_zeroshot      10
B2_qwen_5shot          7
B2_qwen_zeroshot       7
E1                  3540
E1ap                2000
E1ft                  48
E1lora                84
E1ord               3000
E2                  3264
E3                   768