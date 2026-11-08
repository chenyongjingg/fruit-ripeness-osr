# 交接说明（回来了先读这一份）

## 一句话

4090 服务器上有一条**无人值守、可断点续跑**的实验流水线，`master2.sh` 每 15 分钟一轮，
把「解码数据 → 抽冻结特征 → 闭环小样本 → 开放集拒识 → 跨域迁移 → 负对照 → 端到端微调
→ CLIP/Qwen2-VL 基线 → 汇总报表」全部跑完；每个实验结果是 `results/` 下一个以**配置哈希**
命名的 JSON，跑过的不会重跑，写文件是原子的，中途断电最坏只丢当前那一个。

本机会关机不影响：脚本用 `setsid nohup` 挂在服务器上，与 SSH 会话无关。

## 现在怎么查

```bash
tail -20 /root/rio/logs/master.log      # 每轮的起止与磁盘余量
cat /root/rio/outputs/status.json       # 已完成各类实验的计数
cat /root/rio/outputs/REPORT.md         # 汇总表（每轮重生成）
cat /root/rio/outputs/VERIFY.md         # 用同一套指标代码重算已存分数数组（自洽核对）
cat /root/rio/outputs/VERIFY_INDEP.md   # **独立实现**：秩公式 AUROC / 阈值扫描 FPR95 / 已知准确率
                                        # （VERIFY.md 抓不出"指标定义本身错"，这一份能）
nvidia-smi                              # 有占用=正在抽特征或在跑 VLM 基线
```

停止：`touch /root/rio/STOP`（当前这一轮跑完就停，不会杀掉正在写的文件）；
重启：`bash /root/rio/START.sh`（幂等：已在跑就只打印 `already_running`）。

**死掉也会自己回来**：`watchdog.sh` 每 5 分钟查一次驱动是否还在（`STOP` 在就什么都不做），
不在就用同样方式拉起；`START.sh` 会同时保证它在跑。注意它防的是"驱动**退出**"
（OOM killer、信号），防不了"整台容器重启后没人登录"——那种情况仍然要靠 `.bashrc` 钩子。

**卡死会自己恢复**：每个阶段都套了 `timeout`（`master2.sh` 里的 `guard` 函数，e2/e2calib 5 h、
e1/e3/lora 3 h、其余 1–2 h）。任何一步挂住，到点被 TERM，日志里留一行 `[阶段] rc=124`，
循环继续走下一轮。容器里没有 cron/systemd，这是唯一能保证"不会整夜卡在一步上"的办法。

**掉线/重启后的自动恢复**：容器里没有 cron、也没有 systemd（`systemctl` 不存在），
所以没法做真正的开机自启。退而求其次：`/root/.bashrc` 末尾挂了一段
`rio-pipeline-autostart`——**任何人登录一个交互 shell 时**，如果 `STOP` 不在、而
`master2.sh` 不在跑，就自动拉起。这只在「SSH 会话建立」时触发，**不保证宿主重启后自动恢复**；
真正的保护是「每个阶段幂等 + 结果按配置哈希落盘」，任何时刻手动 `START.sh` 都能接着跑。

## 数据在哪

| 你要的 | 位置 |
|---|---|
| 每一条实验的原始指标 | `/root/rio/results/*.json`（含 config + metrics） |
| 汇总长表（写作直接用） | `/root/rio/outputs/master.csv` |
| 分表 | `T1_datasets` 数据集、`T2_closed_set` 闭环、**`T2b_per_class_ap` 每类 AP（长尾）**、`T3_open_set` 开放集、`T4_cross_domain` 跨域（含 `align` 列）、`T6_baselines` 零样本/5-shot 基线、`T7_adapted` 满量微调 vs LoRA、`T8_controls` 负对照、`T9_efficiency` 参数量/延迟/显存、`T10_calibration` 校准后的逐类拒识 |
| 配对检验 | `/root/rio/outputs/T5_paired_tests.csv`（DINOv2-S vs ResNet-50，按 seed 配对 t 检验） |
| 图 | `/root/rio/outputs/figures/*.png` |
| 开放集分数原始数组 | `/root/rio/results/scores/*.npz`（known/unknown 分数，可自己重画 ROC/OSCR） |

## 必须先知道的三件事（写作时不能省）

1. **数据集**。计划书点名的四个里，**RaspGrade 与 NinePeach 已经拿到并并入**
   （见 §4：RaspGrade = 5 级实例 crop；NinePeach = 果园实拍 3 级、无品种），
   Ataulfo（芒果品种）与黑莓两项仍拿不到（Google Drive / Roboflow 需要登录）。
   基线是四个**公开可直接下载**的 HF 数据集：banana3（三级）、banana4（四级含 rotten）、
   fruit12（苹果/香蕉/芒果 × 四级，含 rotten）、field4（田间 Raw/Ripe，两种水果）。
   **2026-11-08 补上计划书点名的 Kaggle 集**（用你的账号，凭证只在
   `C:\Users\33378\__hort_work\.kagglecred` 与本机内存里，服务器上没有）：
   - `mango_khir` = Kaggle `srabon00/mango-ripening-stage-classification`（Khirshapat，
     975 张，**911/43/21**，与计划书数字一致；无 split 文件夹、每颗果实拍两帧
     `GUTI_<id>_A/B` ⇒ 按**文件名分组**切分，卡里 `group_key: filename-group`）。
   - `fruits360` = Kaggle `moltean/fruits` 的**精选子集**（原始 8.8 GB 共 278 类，取
     6 个物种 62 类共 7,440 张，每类 120 张，按官方 Training/Validation/Test）。
     用它跑计划书 §4.5 的 **P2「留一水果」** 开放集协议。
   - `ffr` = Kaggle `sriramr/fruits-fresh-and-rotten-for-classification`（3.8 GB、
     13,599 张）的**精选子集**：每个 (split, class) 取 300 张 ⇒ 3,600 张 / 6 类
     （`Fresh|Rotten` × Apple/Banana/Orange），train 1800 / test 1800，类别完全均衡。
     **该压缩包把整棵树存了两份**（`dataset/dataset/...` 与 `dataset/...`），按文件名
     去重后 13,599 张重复被丢弃——所以子集是 3,600 张而不是 7,200 行。它承担计划书
     §4.5 P3 的**腐烂**那一半，且是**独立于已有 P1/P2 数据集**的来源；
     该视图**只跑 P3_rotten**：E1 与零样本基线都关掉，因为它的三个"等级"其实是物种，
     在物种上算 off-by-one 或让 CLIP 去"评成熟度"都是无意义的数字。
   - `f360rot` = `moltean/fruits` 精选子集**加上它唯一的腐烂类** `Apple Rotten 1`
     （650 张）。计划书 §4.5 的 P3 原文写的就是「Fruits-360 的 rotten 类」；原始集合里
     **只有这一类是腐烂的**，且只存在于 `fruits-360_3-body-problem` 这版、全在 `Training/`
     下（没有 test 划分）。所以我另建 `f360rot`（8,090 张 = 上面 7,440 + 650），
     **不动 `fruits360` 那份**（它的内容已经进了结果哈希），把那 650 张写到 `test/`：
     这一类**从不出现在任何协议的已知集里**，所以"写到 test"不是重新切分标注数据。
     已知集 = 61 个有 train 图的类（`Pear 14` 的 120 张全在 val/test，代码里排除，
     否则会有一个头永远预测不出、只能拉低已知准确率的类）；未知 = `Apple Rotten 1`。
     与 `ffr` 的分工：`ffr` 是**另一个数据集**的腐烂证据（独立来源），`f360rot` 是
     **计划书原话那个类**，两者互相印证，写作时不要合并成一个数字。
   **f360rot 在服务器上的存档**：本机 `D:/kag/f360rot_subset.zip` 79,846,719 B，
     服务器 `data/raw/f360rot/data.zip` 同尺寸、sha256 一致（`3334eb30…`）。
   **必须写明的三点**：① Khirshapat 是**极端长尾**（21 张 OverRipe），开放集协议在该集
   上**不可估计**，代码里用 `min_te_each=10` 主动跳过、只留 E1 小样本结果；
   ② Fruits-360 的类别数字（"Apple 5"）是**数据集自己的编号，不是成熟度序**，
   所以留一水果时已知类保持原样、不做任何等级汇总；
   ③ 服务器出口 IP 被 Kaggle 的 reCAPTCHA 挡住（`/api/v1/*` 一律 404），
   这四个压缩包（`fruits360` / `f360rot` / `mango_khir` / `ffr`）都是**本机下载后
   SFTP 推上去的**，不是服务器自己下的。
2. **水果12 官方划分有泄漏**：3591 张源照片里有 360 张跨了 train/val/test（同一张照片
   裁出的多个 box 被分到不同集合）。我按**源照片**重新做了分组分层划分，卡里记
   `split_was_regrouped: true`。所有数据集的 `group_leak_count` 断言为 0。
3. **术语是 open-set 不是 open-world**。计划书 v1.3 已改；"open-world orchard
   environment" 是园艺术语（Li Zhang 2023），正文必须显式区分。

## 方法实现与计划书的差异（完整清单在 `/root/rio/README_SERVER.md` §6）

**已经补上的（2026-11-08 审查后新增）**

- **LoRA**（`run_lora.py`，DINOv2-S 的 qkv+proj 挂 r=8/α=16，骨干冻结，lr=1e-3、
  30 epoch；与 E1ft 同一套训练增强；结果在 `T7_adapted`）。现在由 `master2.sh` 在
  Qwen 基线之后直接调用（早先是单独的 `lora_loop.sh`；同跑会 OOM）。
- **P2 真正实现**（计划书 §4.5 的"unseen cultivar"）：`E2` 新增
  `protocol=P2c_unseen_cultivar`，按水果做留一——fruit12 的 apple/banana/mango 各自整类
  作为未知，已知集是**另外两种水果**的四个等级（rotten 排除，避免与 P3 混淆）。
  之前的 `P2_unseen_interior` 是"藏掉一个内部等级"，不是计划书的 P2。
- **相邻等级误拒 + 校准**（计划书 §4.5 第三条）：`--stage e2 --calib`，逐类阈值取
  **val 划分**上该类分数的 5% 分位（val 与 train 按组不相交），再在 test 上报
  CCR / FPR / 各类拒识率；表 `T10_calibration` 同时给出校准前后**各类拒识率的标准差**，
  用来判断"等级间拒识不均衡"是不是阈值造成的假象。
- **RQ3 的第三档「特征层对齐」**（计划书 §4.3(c)，原文标"可选"）：`--align bn`——
  用**目标域 train 划分**的均值/标准差逐维 z-score（只用目标域图像，**不用目标域标签**），
  同一变换套到源域特征上，再重新 L2 归一化；三种头不变。`config.align` 只在用到时才写进
  配置里（所以**任何已有 E3 的 run id 都不动**），`T4_cross_domain` 按 `align` 分组，
  对齐与非对齐不混均。实测 banana3→banana4、proto 头、0-shot：**0.700 → 0.857**。
- **每类 AP**（计划书闭环指标里的 long-tail 项）：E1 只存硬预测，AP 需要概率，所以由
  `ap_extra.py` 用**独立 exp 键 `E1ap`** 重拟合同样的格子（不移动任何已有 run id），
  表 `T2b_per_class_ap`，并在 `REPORT.md` 里单列一节。它自带 `--self-test`。
- **双通道特征消融**：计划书说 CLS token 与 patch mean 都存，之前只评了 CLS。
  现在 `--stage e1 --variants mean` 跑 dinov2_s/dinov2_b/clip_b × 3 seeds（`T2_closed_set`
  的 `variant` 列区分）。
- **E5 效率实验**：`efficiency.py` 实测四个编码器的参数量、batch-1 中位延迟
  （20 次、带 CUDA sync）、batch-32 峰值显存，加上三种头/适配的可训练参数
  （linear probe 从特征维度算、LoRA/微调从结果 JSON 读，不手估）。表 `T9_efficiency`。
- **计划书字面的「留一水果」P2**（2026-11-08 补）：`stage_e2f` 在 `fruits360` 上
  依次把 Apple / Pear / Cucumber / Tomato / Orange **整个物种**当作未知类
  （`protocol=P2_leave_one_fruit`，`view=fruits360_x_<fruit>`），已知类是**其余所有
  水果的所有类**，不做任何跨水果的等级汇总。每格 5×2×4×2×3 = 240 个 run；
  未知侧测试样本 150–580 张、已知侧 1,351–1,781 张（写论文时按 `n_unknown_test` 报）。
  它与 `P2c_unseen_cultivar`（fruit12 留一水果但汇总等级）是两条不同协议，**不能合并报告**。
- **计划书 P3 的「异物」那一半**（2026-11-08 补）：计划书 §4.5 把 P3 定义成「腐烂果
  **与异物**」，腐烂那一半由 `banana4`/`fruit12`/`ffr` 的 `P3_rotten` 承担；异物那一半
  由 `stage_e2x` 新增的 `protocol=P3_foreign` 承担——已知类是某数据集的正常等级，
  **未知图像来自另一个数据集的另一个物种**（计划书原话「跨数据集水果图像作异物」）。
  三对：`banana3 ← fruit12 的芒果`、`fruit12_apple ← field4 的芒果`、
  `ffr 新鲜三类 ← fruits360 的黄瓜/番茄`。共 3 对 × 2 编码器 × 2 档 × 3 seed × 4 分数
  = 144 个 run（已完成 144/144）。**必须写进论文的坦白**：异物集与已知集在物种之外
  还差在拍摄条件，所以高 AUROC 的含义是「不是这种水果 **且** 不是这台相机」；
  真实产线上的异物与水果同一光路。实测（2 编码器 × 3 seed 的均值）：

  | 已知 ← 异物 | MSP | Energy | Mahalanobis | kNN |
  |---|---|---|---|---|
  | banana3 ← fruit12 芒果（全量支撑） | 0.645 | 0.664 | **0.987** | **0.986** |
  | fruit12_apple ← field4 芒果（全量支撑） | 0.779 | 0.797 | **0.979** | **0.978** |
  | ffr 新鲜三类 ← fruits360 黄瓜/番茄（全量支撑） | **0.987** | 0.989 | 0.995 | 0.999 |

  5-shot 支撑下 mahalanobis/kNN 分别掉到 0.973 / 0.970（banana3←芒果）、
  0.952 / 0.932（fruit12_apple←芒果）。**四个分数在这里分道扬镳**：只要异物与已知
  在特征空间里不是"近邻"，距离类分数接近满分，而 softmax 类分数（MSP/Energy）
  会自信地把异物分进某一已知类——这正是要在论文里报告的（分数选择比编码器选择
  更决定拒识效果）。注意 ffr←黄瓜/番茄那一行**不能当作反例证据**：那对异物与已知
  差得远，MSP 也拿到了 0.987。
- **失败不再是静默的**：E1/E2/E3/E2c 的异常写进 `logs/failures.jsonl`，
  `REPORT.md` 有独立的 `## Failures` 节——**列在这里的实验不在任何结果表里**。

**仍然是偏离、必须写进论文的**

- DINOv2 用 224 输入（原生 518），单卡吞吐考虑。
- 两级视图（field4）没有 P1/P2——只有一个"内部等级"，藏掉后只剩一类，不是分类问题
  （代码里有 `len(ordn) >= 3` 守卫，这类视图直接跳过，不再产出失败记录）。
- **没有有序回归头（CORN/CORAL）**：计划书把"序数性"列为动机之一，但实现里闭环只有
  linear probe / prototype / LoRA 三种；`off_by_one_rate` 与 ordinal MAE 是**评估**层面的
  序数指标，不是模型层面的序数归纳偏置。写作时不能声称做了序数回归。
- **没有 mask-preactivation 消融**（计划书 §4.x 提到的遮挡敏感性检查）。
- **没有新类发现（k-means / Sinkhorn 后处理）**：计划书把这一步标成"加分项"，
  流水线只做**拒识**，不判断未知样本到底是什么。写作时不能声称做了新类发现。
- **没有 5 级及以上等级的数据集**：现有最强的是 fruit12 的四级（unripe/ripe/overripe/rotten），
  所以"等级数增加时退化"的趋势无法给出来。
- **Fruits-360 是精选子集，不是全集**：原集 278 类 / 13.6 万张，这里取 6 个物种
  62 类、每类 120 张（7,440 张）。理由是上传带宽（服务器出口被 Kaggle 挡、只能本机
  SFTP 推，实测 ~190 KB/s）。**采样规则必须写进论文**：按文件路径排序后等距抽样，
  每类保留 120 张，因此每类的测试集只有约 31 张。
- **`VERIFY.md` 不是独立实现**：它把存下来的分数数组重新喂给**同一个** `open_set_metrics`，
  只能抓"存的数和分数对不上"，不能验证指标定义本身对。文档里已如实标注。
- 四个"撞车核查"文献（E-CLIP、YOLOE、Grounding-DINO、Li Zhang 2023）**没有联网核实原文**。

## 更正台账（2026-11-08 审查当天发现，都会改动数字）

| # | 缺陷 | 症状 | 处理 |
|---|---|---|---|
| 1 | Qwen 5-shot 示例图的标签用了内部类名（`Raw_Banana`）而选项是显示名（`raw`） | 模型照抄示例 ⇒ 全部 `__unparsed__` ⇒ `acc=0.000, unparsed=1.000`（field4 两个视图） | 改用 `fwd[c]`；删掉旧 `B2_qwen_5shot__*.json` 重算。**实测修复后 field4_banana 5-shot acc=0.992、unparsed=0.000** |
| 2 | 基线取测试集时**没有先按视图过滤类**，`_cap` 是按 `label_name` 分组的 ⇒ 别的水果混进来 | `field4_banana` 的 120 张预算变成 240 行，其中一半是芒果，且被当成错误计分 | 先 `label_name.isin(labels)` 再 `_cap`，并加 `assert`；**全部 B1/B2 结果已删除重算**。CLIP 实测：banana3 0.399、fruit12_banana 0.316（≈随机），远低于冻结特征的 0.87 |
| 3 | 校准最初把阈值拟合在**支撑集**上 | 头就是在支撑集上训练的 ⇒ 分数被抬高 ⇒ 拒掉 77% 的已知样本 | 改拟合在 **val**（与 train/test 按组不相交）；结果里带 `calib_source` |
| 4 | 负对照原来是**逐样本独立抽标签**，每个样本约有 1/C 概率抽到自己的真标签 | 15 个支撑样本里平均留下 ~5 个真标签 ⇒ 某个 seed 的 macro-F1 打到 0.46（随机水平 0.33），对照"没死" | 改成**按类别整环平移**（每个样本的标签都变、类别多重集不变）；重算 84 个 run，现在 macro-F1 全部 ≤ 随机水平 |
| 5 | `report.py` 的配对 t 检验没按 `variant` 过滤 | 平均池化臂加入后同一 (view,shot,seed) 有两行 ⇒ 每轮结束 `report.py` 直接崩，REPORT.md 不再更新 | 过滤 `variant=="cls"`；已实测跑通 |
| 6 | `VERIFY.md` **验证了零个文件却报绿**：分数数组叫 `<run_id>.npz`，实验记录叫 `<EXP>__<dataset>__<run_id>.json`，而代码按 `<run_id>.json` 去找 ⇒ 1764 个文件全部 `continue`，最后照样打印 "mismatches: 0" | 一个**永远不会失败**的检查，比没有检查更糟 | 改成按 `*__<run_id>.json` 解析，解析不到计为失败并单独计数；实测 **1820/1820 全部解析、0 未匹配、0 不符** |
| 7 | 校准的 `config.calib` 字符串写死为 `per_class_support_q05`，而代码早已改成在 **val** 上拟合 | 两种不同方法共用同一个 run_id ⇒ 改了方法旧结果不会重算（正是"配置哈希不含数据选择"的老坑） | 字符串改成 `per_class_val_q05`；旧的 912 条已移到 `results/_retired_20261108_calib_label/`（不删，留档），下一轮自动重算 |
| 8 | Fig.4 一直画不出来 / 画出来是空的 | 三处叠加：分数数组名里没有 `E2__` 前缀（globbing 0 个）、按 `shot==50` 过滤（E2 的 shot 只有 `{None,5}`）、`np.load` 未关闭 1800 个 fd 触发 "Too many open files"；修好后还把两个尺度不同的分数（mahalanobis −2500 vs energy ~1）画在同一根轴上，变成一根尖刺 | 按 JSON 里 `exp/shot/variant/calib` 筛 + `with np.load` 关闭 + **一格只画一种分数**；现已出图（4 格，energy 的 known/unknown 分布） |
| 9 | **FPR@95TPR 的定义和代码不一致**：代码用 `np.percentile(known, 5)` 当阈值，那不是"TPR=95% 的操作点" | 插值分位数会让 TPR 落到 95% 以下（实测 90/95=0.947），有并列分时还能差一整个并列块 ⇒ 与独立实现最大差 **0.163 FPR** | `open_set_metrics` 改成"TPR 仍 ≥95% 的最大阈值"，并额外存 `tpr_at_fpr95`；**用 `recompute_e2.py` 从已存的分数数组重算 1056 条（不重训）**；新的 `verify_indep.py` 独立复算 AUROC（秩公式，不走 sklearn）/FPR95/已知准确率 ⇒ **1056 条 0 违规，AUROC 差 2e-16** |
| 10 | `e2_fruit_out` 用「去掉最后一个空格后的部分」定义水果 ⇒ `Apple Braeburn 1`、`Apple Red Yellow 2` 都不算 `Apple` | 留一「Apple」时苹果的其他品种还留在**已知类**里：号称"没见过的水果"其实见过 | 改成**取第一个词**当物种；6 个物种 / 62 类 / 4,788 个果实实例，按 (类, 编号) 分组后 **0 个跨划分** |
| 11 | 最小测试数守卫只卡了未知侧 | `P2_unseen_interior` 藏 UnRipe 时未知侧 137 张、**已知侧只有 9 张**，AUROC 照算不误，192 个 run 已落盘 | 两侧都卡（`min_te_each`，默认 1 不改变任何主集行为）；**删掉那 192 个 mango_khir E2 结果和对应 npz**，重算后该集不再产出开放集数字 |
| 12 | Fruits Fresh and Rotten 压缩包把**整棵树存了两份**（`dataset/dataset/train/...` 与 `dataset/train/...`，各 13,599 张） | 若直接按目录切子集，输出里每张图会**各出现两次**（同名同字节）：不是跨划分泄漏，但白白翻倍、并让"每类多少张"变成谎话（实测 27,198 个成员 / 13,599 张不同图） | 切子集时按 `(split, 类别, 文件名)` 去重，打印 `duplicates_skipped: 13599`；成品 3,600 张 / 6 类 × 600 / train 1800 + test 1800，`group_leak_count=0` |
| 13 | `f360rot` 视图的已知集直接取"所有非 rotten 类"，没检查这些类**在 train 里有没有图** | `Pear 14` 的 120 张全在 val/test ⇒ 它会进已知集，却永远拿不到支撑样本、头永远预测不出它 ⇒ **已知准确率被一个与拒识无关的原因拉低**，而所有表都照常打印 | 已知集改为"在 train 里有 ≥10 张图的类"（实测 61 类，`Pear 14` 被排除）；`E.e2` 本来就会把不在已知集/未知集里的行整行丢掉，所以它的测试图不会进任何分子分母 |
| 14 | `srv.py`（本机→服务器的助手）**永远退出 0**，只把远端 RC 打印成一行 `RC= <n>` | `until python srv.py "..."; do sleep; done` **第一轮就退出**；`python srv.py put A B && echo done` 在传输**还没完**时就打印，我据此判定"上传被截断"，同时另开了一条并行上传——而原件几分钟后自己传完、sha256 与本地完全一致 | 等待条件一律 `grep -q 'RC= 0'` 或直接断言对象（远端 `sha256sum` / 结果 JSON 计数）；判"传完"只认**内容相等**。当前 `data/raw/f360rot/data.zip` 与 `D:/kag/f360rot_subset.zip` 同为 79,846,719 B、sha256 `3334eb30…` |

第 1、2、4 条的共同点：**配置哈希不含数据选择/标签构造**，所以修完代码不删旧结果就会一直复用错的数字。删之前都核过是哪些文件。
第 10 条是同一类错的另一面：**证据是我自己写的分组函数**，而它把"苹果品种"排除在"Apple"之外——
名字对不上时**没有任何检查会报错**，因为 `group_leak_count` 只看分组是否跨划分，不看分组是否等于物种。

判据（这次真正学到的）：**一个"应该掉到随机"的对照，要用随机水平去判，而不是用一个凭感觉的数**。
`banana4`/`fruit12_*` 的闭环视图是 **3 类**（腐烂类被留作 P3 的未知），我一开始按数据集的 4 个等级
算随机水平（0.25），于是把一个**本来就在随机水平上**的对照判成了"高出 0.088"。同理，判对照要看
**macro-F1**：`fruit12_banana` 的测试集 68% 是 Ripe，塌缩成单类的预测器准确率就有 0.673。

## 结果目前长什么样（会随流水线继续跑更新，详见 REPORT.md）

- 闭环 few-shot：全 **10** 个视图 × 4 编码器 × 2 头 × {1,5,10,50,全量} × 5 seeds 已完成。
  冻结特征随 shot 单调上升；DINOv2 在多数视图 ≤50 shot 优于 ResNet-50，但
  **field4_banana 1-shot 上冻结 ResNet-50 反而更强（0.821 vs DINOv2-S 0.660 / DINOv2-B 0.756）
  ——这个反例要写进去**。
- 开放集：Mahalanobis / kNN 明显强于 MSP / Energy；banana3 的 P1（藏掉 overripe）上
  MSP/Energy 的 12 个 run 均值 **0.495**、值域 **0.276–0.739**（`probe_b3_p1.py`），
  其中 6 个 run 落在 0.28–0.35 ——未知等级反而更"自信"，这是可以写的发现；
  但**不能写成"该格低于 0.5"**，因为同一格里也有 0.74 的 run。
- **P3 腐烂（`P3_rotten`）跨四个来源**（AUROC，每个数 = 该数据集全部 run 的均值，
  含 2 编码器 × 2 档支撑 × 3 seed）：

  | 数据集 | MSP | Energy | Mahalanobis | kNN | runs |
  |---|---|---|---|---|---|
  | `ffr`（fresh vs rotten，独立数据集） | 0.882 | 0.882 | **0.963** | 0.945 | 48 |
  | `f360rot`（Apple Rotten 1 vs 61 个 Fruits-360 类） | 0.454 | 0.754 | **0.957** | （跑完再填） | 48 |
  | `banana4`（第四个等级 = rotten） | 0.733 | 0.717 | **0.901** | 0.899 | 96 |
  | `fruit12`（三视图，第四个等级 = rotten） | 0.519 | 0.534 | **0.750** | 0.730 | 288 |

  ⇒ **同一个"腐烂"任务，换个数据集就从"几乎无法拒识"（fruit12，MSP 0.52）变到 0.96**：
  这是要写的结论——腐烂类的可分性取决于它属于哪个数据集（拍摄条件、腐烂程度、
  与已知类的远近），不是单纯"腐烂 vs 正常"。`f360rot` 上 MSP 掉到 0.454（低于随机），
  与 banana3 的 P1（0.353）同一种现象：**未知类在 softmax 上反而更"自信"**。
- **P3 异物（`P3_foreign`，192 个 run = 4 对 × 2 编码器 × 2 支撑档 × 3 seed × 4 分数）**：见上面 §"已经补上的"那张表；
  结论是 **MSP/Energy 会把异物自信地分进已知类（0.64–0.80），
  Mahalanobis/kNN 接近满分（0.93–0.99）**。
- 负对照：打乱支撑集标签后掉到随机水平。
- CLIP 零样本、Qwen2-VL-7B INT4 零样本/5-shot 已重算（见上面更正台账第 1、2 条）。
  **CLIP 零样本基本等于随机**（banana3 0.399/macro-F1 0.277、fruit12_banana 0.316/0.299），
  而冻结 DINOv2 + 线性探针在 banana3 全量上 0.90 左右——这是论文 "zero-shot VLM 不够用"
  这一段的直接证据。Qwen 在 field4（田间两分类）上反而很强：零样本 0.983、5-shot 0.992，
  与冻结特征不在同一个难度上，写作时要分开讲，不能混成一句"VLM 不如特征模型"。
- **校准臂的覆盖范围**：阈值只在 **val** 上拟合。`ffr` 的压缩包只有 train/test
  （没有 val），所以它**没有校准臂**——旧代码在这种情况下会退回**支撑集**拟合，
  而那正是头训练过、分数被抬高的一批样本（早期实测拒掉 77% 的已知样本）。
  现在这类视图直接跳过、`T10_calibration` 里没有它的行，这是正确信号。
- **校准臂已覆盖最终视图集**（2026-11-08 12:00 UTC 重跑完）：**1,296 个校准 run**，
  `REPORT.md` 的 T10 有 **860 行**、覆盖 10 个视图名（含 `ninepeach` 与 `raspgrade`）；
  全部 `calib_src = val`，**没有一行退回支撑集**（grep `support (no usable val split)`
  只命中说明文字本身）。`ffr`（无 val）与 `mango_khir`（val 只有 9 行）**没有校准臂**——
  缺失是正确信号，不是漏跑。
- 校准臂目前的诚实读数：有的视图 `auroc < 0.5`（未知样本反而更像"正常"），
  这时逐类阈值**改不了排序**，`fpr_cal` 会趋近 1.0。`T10_calibration` 下面那段说明
  就是给这个情况写的，别把"校准后 FPR 变高"当成 bug。

## 还没做/需要你补的

- 扩展层数据集（**OPALM**、Kaggle 芒果）——按计划书 9.4 的"最低配置"条款砍掉；
  **OPALM 至今没有尝试过**（计划书列为优先级 3 的"加分项"），不要写成"做过但失败"。
- 5 等级数据集**已经有了**（RaspGrade，见 §4）；但它的等级粒度曲线只有 1 个视图，
  且该视图全部臂贴近随机（见 §9），所以"级数效应"的推断仍然做不了。
- 序数回归头、遮挡消融没做，见上。
- 计划书的 `P2` 现在叫 `P2c_unseen_species`（fruit12 留一物种）。"同一水果、没见过的
  栽培品种"这一类**做不了**：四个原数据集没有品种标注，NinePeach 归档里也没有
  （见 §7 第 1 条）。写作时"品种级"一律列限制，不出现"品种级"字样。

---

# v2.0 对齐（2026-11-08）

计划书 `D:\Horticulturae\...计划书 v2.0` 落地后，流水线做了这些改动。全部改动都在
`/root/rio` 上跑通并验证过，不是"打算做"。

## 1. 报告口径修复（§5.2 的 13+1 条）

| # | 修法 | 落点 |
|---|---|---|
| 1 | energy = `logsumexp(z)`，NOT `−log p_max`；二类已知集上 MSP/Energy 按构造秩等价 | `report.py` Note#1 |
| 2 | 四臂表述（P1/P2 是同一"留一级"操作的两种实例；P3b 声明物种+相机+光照混淆） | `report.py` Note#3 |
| 3 | `P2c_unseen_cultivar` → `P2c_unseen_species` | `rio/common.py` 的 `display_view`/`display_protocol`，load 时统一改写 ⇒ 所有表/图/报告一起变，`final_check` 断言旧名只在"这就是旧名"的句子里出现 |
| 4 | 校准只在匹配 FPR 下比较；新增 `oscr_at_fpr5_rule`/`ccr_fpr5_before` | `report.py` T10 |
| 5 | 相邻等级误拒降级为分析章节 | `analyze_v2.py` T14 |
| 6 | n≥30 门槛 + 薄格标 descriptive + seed bootstrap CI | `report.py` T3(`thin`)、`analyze_v2.py` T16/T16b |
| 7 | 配对检验报 raw p + Bonferroni/Holm（检验族大小随视图数变） | `report.py` `correct_multiple()` ⇒ 并入 NinePeach 后是 **1/40 存活**（此前 1/32）；引用一律写存活数，不写族大小以外的口径 |
| 8 | 基线报 n + `test_ids_sha256` | `report.py` T6 |
| 9 | E3 明确是二分类 4 对 | `report.py` Note#10 |
| 10 | **结果封印**：每条结果带 `view/ordinal/known/meta_sha256/meta_sha256_live` | `seal_of()` + `already()` 比对 ⇒ 数据一改，旧结果自动重算 |
| 11 | `weighted_f1`（相邻=1、跳级=2）实现并启用 | `ord_extra.py` / `E1ord` 臂 |
| 12 | E2f 补完 | 5 个物种、228 runs |
| 13 | "首个"→"据我们所知" | 写稿项，不在代码里 |

**新增的两条护栏**（§6）：漂移检查（`seal.py --full` / `already()`）、塌缩检测
（`analyze_v2.py` T15 + `final_check` 第 14 条）。

## 2. 封印（fix #10）怎么工作

- `save_result()` 每次写结果时附带 `seal`；`already()` 读出旧封印，只要 `view` /
  `ordinal` / `meta_sha256_live` 任一与当前数据不符就**重算**并打 `[drift]` 日志。
- 封印**不进配置哈希**——进去会给 10k 个已有 run 换发新 id、逼一遍全量重跑。
  哈希仍标识"实验"，封印标识"这次实验跑在什么数据上"。
- 历史结果由 `seal.py` 回填，标 `seal_source: derived`，并在 `outputs/SEAL_REPORT.md`
  写明：**派生封印只说明"与今天的数据一致"，不说明"当时就是用今天的数据跑的"**；
  card 与 live 的哈希对比是唯一能把这两句话分开的证据。
- `seal.py` 默认增量（只看上次 marker 之后的结果），可以安全放进 15 分钟循环。
- **`--min-age-min 30` 会让"跑完立刻封印"永远封不到最新结果**（避免和正在写结果的进程抢写），
  而 `final_check` 的 `unsealed(>30min)` 是一条**要等 30 分钟才可能变红**的检查。
  2026-11-08 实测：一个 11:22 写下的校准结果在 11:33 的封印轮里被跳过，
  直到 12:0x 的 `final_check` 才报 `sealed=11401 unsealed(>30min)=1`。
  ⇒ **收尾流程固定为：跑完 → 等 >30 分钟 → 再 `seal.py` 一次 → `final_check`**。
- **`ap_extra.py` / `ord_extra.py` 每轮会重写一部分 E1ap/E1ord 结果**（日志 `ok=2000
  skipped=0` / `ok=3000 skipped=0`）。本轮实测：12:10 之后重写的是 E1ap **400** + E1ord
  **600** = 1,000 个文件，正好等于 `final_check` 里 `sealed=11728` 与总数 `12728` 之差。
  所以那不是"缺封印"，而是这 1,000 个还在 30 分钟窗口内、按 seal 的契约不算证据。
  停掉驱动后必须按上一条补一次 `seal.py`，否则 30 分钟后这 1,000 个会变成真缺口。

## 3. 新增的分析层 `analyze_v2.py`（T11–T16）

只读已存分数数组，不重跑模型。三个**必须跟数字一起走**的结论：

1. **MSP 与 Energy 在二类已知集上是恒等的**：114/114 个格子的 AUROC 完全相同
   （`frac_identical = 1.000`，占全格 114/246）。这不是"相关 0.99"，是**定理**
   （两者都单调于 |z₁−z₂|）。把二类格与三类格混在一起算相关系数会得到 0.933——
   那个数既不是前者也不是后者。
2. **"藏首级距离类赢、藏中间级概率类赢"不能当规律写**。实测（全部有格视图的**格均值**，含
   RaspGrade 与 NinePeach）：藏首级 dist 0.657 vs prob 0.568；藏中间级 prob 0.693 vs
   dist 0.605；藏末级 dist 0.760 vs prob 0.553。计划书里的 **0.845/0.856 vs 0.530 只是
   banana4 一个视图**（T12b 逐位命中 0.850 vs 0.530），而中间级的 0.785/0.564/0.616 在
   现有网格里**任何格子都对不上**。逐视图（T12b：首级 8 个视图、中间级与末级各 7 个——
   `mango_khir` 的末级未知侧不足 `min_te_each`）才是可复现的表述：
   **藏首级 dist 赢 4 / prob 赢 4；藏中间级 dist 3 : prob 4；藏末级 dist 7:0**。
   也就是说唯一稳健的规律是"末级距离族全胜"。
3. **塌缩格 16 runs / 2 组**：`mango_khir` P2 藏 UnRipe（32 个 run 里 12 个，known=10，
   预测塌缩到单类）+ `banana3` P1 藏 overripe 5-shot（4 个 run，known_acc 恰等于多数类占比）。

## 4. 新数据集

- **RaspGrade**（HF `FBK-TeV/RaspGrade`，CC-BY-NC-4.0）：200 张传送带图像，
  **5 个等级是实例多边形不是图像标签**（每张图都含多于一等级的浆果，图像级标签只能是
  多数投票）。所以按多边形切出 **5,043 个浆果 crop**（class 0 = 整串区域，丢弃；
  0 个退化多边形被丢），`group` = 源图像 ⇒ 按图像分组切分，`group_leak_count = 0`。
  切分 3556/755/732，测试侧：grade1 148、grade2 523、grade3 43、grade4 6、grade5 12
  ⇒ **grade4 的开放集格根本不产生结果**（`min_te_each=10` 在未知侧 6 张时跳过），
  **grade5 只有 P1 一格、未知侧 n=12**（T16 标 descriptive）。卡里记了
  `unit: berry instance (polygon crop), NOT image` 与真实样本量（200 张源图）。
- **NinePeach**（figshare 27125373，8.8 GB）**已下载并核对完成**：`api.figshare.com`
  与 `ndownloader` 对本 pod 的出口 IP 一律 403（走集群代理与直连都一样），但 302 指向的
  **Cloudflare R2 可以直连**（`--noproxy '*'`，约 1.5–3 MB/s），而 figshare 签发的 URL
  只有 **10 秒**有效期（请求必须在 10 秒内**开始**，开始后可以一直传）。于是用本机代理
  签 URL、交给 pod 追加写：`np_fetch.py`，断点续传按 pod 上的文件大小算偏移。
  实测 **8,838,332,680 B、md5 `e0fb0a2dfbab161546d398aef17ad081` 与 figshare 记录一致**。
  实测内容：**1,245 张 jpg / 1,245 个 VOC xml / 3,493 个框 / 3 类
  （immature 1,618、mature 1,168、semi-mature 707）/ 无品种 / 无 test 目录**。
  计划书说 3,849 张、9 品种 —— **张数与品种数都不成立**（`outputs/NINEPEACH_VERIFY.md`）。
  建库：3,493 个实例 crop，按源照片分组切分 2446/524/523，组数 1,245，泄漏 0，
  test 逐类 223/189/111。
  **EXIF 方向陷阱**：1,245 张图全部横存（4032×3024，orientation=6）而 xml 声明竖版
  3024×4032，直接裁剪会得到越界框（第一次 build 就死在
  `Coordinate 'lower' is less than 'upper'`）。修法 = `ImageOps.exif_transpose` 后再裁，
  并对"转置后尺寸 ≠ xml 声明尺寸"做**硬断言**（`card.json`：`exif_transposed=1245`、
  `xml_size_mismatch=0`）。

## 5. 现在的验收状态
`python3 final_check.py` → **PASSED 57 / 57，FAILURES: 0**（2026-11-08 17:00 UTC 实测，
含 NinePeach 归档校验与卡片一致性两条）（计划书第 1 周的验收线是
39/39）。新增的 14 条里，有 4 条第一次跑就是红的（P2c 计数、T9 训练显存、8 个未封印结果、
REPORT 里残留旧名），逐条修掉之后才是全绿——这几条不是装饰。

## 6. 计划书里的阶段名现在能照抄了

计划书第 1／3 周的检查清单写的是 `--stage seal`、`--stage aggregate --v2`、
`--stage figures --v2`、`--stage report --rebuild`、`--stage verify --seeds 3`，
而流水线里这些工作一直由独立脚本承担（`seal.py`、`analyze_v2.py`、`fig_v2.py`、
`report.py`、`verify_indep.py`、`final_check.py`）。现在 `run.py` 把这些名字接成别名，
**逐个脚本原名调用、非零退出原样上抛**（不是重新实现一遍检查）：

| 计划书命令 | 实际执行 |
|---|---|
| `run.py --stage seal --write …` | `seal.py`（断言的键集固定在文件里，`--write` 只记录） |
| `run.py --stage aggregate --v2` | `analyze_v2.py [--bootstrap N]` → T11–T16（含 T14b 粒度） |
| `run.py --stage figures --v2` | `fig_v2.py` → `outputs/figures/fig_v2_{arms,flip}.pdf` |
| `run.py --stage report --rebuild` | `report.py`（无增量模式，本来每次全量重建） |
| `run.py --stage verify --seeds 3` | `verify_indep.py` + `final_check.py` |
| `run.py --stage validate --fix-leak-check` | `final_check.py`（防泄漏断言无条件跑） |

计划书其它名字是**已有名字的另一种叫法**：`experiments` → `--stage e1` / `--stage e2`；
`baselines` → `run_baselines.py`；`recalibrate --matched-fpr` → `--stage e2 --calib` +
`report.py` 的 T10；`scripts/add_dataset.py` → `rio/data.py` 里的 decoder 由
`--stage prepare` 驱动。这张表也写在 `README_SERVER.md` §1。

## 7. 计划书 vs 实测：`PLAN_VS_DATA.md`

计划书自己也写错了数字，逐条列在 **`/root/rio/PLAN_VS_DATA.md`**（本机同目录一份）。
最要紧的四条：

1. **NinePeach 张数与品种**：计划书写 3,849 张 / 9 品种；归档实测见
   `outputs/NINEPEACH_VERIFY.md`（`np_verify.py` 生成），**归档里没有 cultivar 字段**，
   所以"9 品种留出"做不成 —— 按计划书 §4.4 自己写的分支走"部分升级、品种级列限制"。
2. **塌缩格是 16 不是 12**：`mango_khir` 12 + `banana3` 4（`outputs/T15_collapsed.csv`）。
   12 是单组数被当成了总数。
3. **RQ2 的 0.990/0.984 不对应任何一格**：全格是 0.933/0.972，而 known=2 子集上
   msp–energy 是 **1.000 且逐位相同**（114/114）。写"0.99"既弱化了机制又对不上数。
   跨族相关实测区间是 **0.36–0.52**（计划书写 0.45–0.54，下界不成立）。
4. **C4(a) 的翻转律是单数据集数字**：0.85/0.53 只出现在 `banana4`；逐视图看，
   藏首级 dist 赢 4/8、藏中间级 3/7、**藏末级 dist 7/7**。只有最后一条能当规律写。

## 8. 5 级数据集：RaspGrade 的粒度曲线（T14b）

`outputs/T14b_granularity.csv`（`analyze_v2.py` 新增）：

| n_levels | family | n_cells | n_views | delta_pp_mean | pct_cells_positive |
|---|---|---|---|---|---|
| 3 | dist | 72 | 6 | +0.04 | 53.1 |
| 3 | prob | 72 | 6 | −4.02 | 38.2 |
| 5 | dist | 24 | 1 | −1.14 | 41.7 |
| 5 | prob | 24 | 1 | −1.58 | 32.3 |

`delta_pp = (拒识相邻等级率 − 拒识远等级率) × 100`：**负值才是想要的方向**（远的更容易拒）。
读法：3 级下概率族确实按"离得越远越容易拒"工作（−4.02pp），距离族基本为零（+0.04）；
5 级下两族都是负的但幅度小，**而且 5 级只有 raspgrade 一个视图（n_views=1）**
⇒ 这一行只能当单数据集证据，不能拿来做"等级数越多越难"的推断。
（并入 NinePeach 后 3 级的 `n_cells` 从 60→72、`n_views` 从 5→6，方向不变。）

## 9. NinePeach 并进来了，两个新视图各给出一条"必须先看逐视图"的结果

1. **NinePeach（果园实拍、12 MP、实例 crop）的概率族显著低于随机**：P1 藏 mature 时
   prob **0.334**（dist 0.678）；P2 藏 immature 时 prob **0.302**（dist 0.814）；
   P2 藏 semi-mature 时 prob **0.858**（dist 0.482）；P3_foreign（芒果作异物）
   prob 0.805 / dist **0.999**（`probe_np_arms.py`，每格 24 run）。
   这不是"族翻转"的又一例，是**同一个分数把未知样本排得更可信**。
   稿件只能陈述方向与幅度，不能解释成"田野场景更容易过自信"——没有实验把
   "过自信"与"背景占比/尺度"分开。
2. **RaspGrade 全部臂贴近随机**：P1 dist 0.537 / prob 0.493；P2 藏 grade1 0.487/0.580、
   藏 grade2 0.536/0.467、藏 grade3 0.611/0.618。crop 短边中位数 166 px
   （`probe_crop_stats.py`），所以**不是**"切得太小"。它作为 5 级粒度的唯一证据，
   结论只能写"在这个视图上免训练分数没有可用的开放集能力"，不能写"级数越多越难"。
3. 这两条合起来的写稿要求：**四臂均值必须带视图构成**。P1 的距离族均值随语料
   0.82（并入前）→ 0.774（含 RaspGrade）→ **0.760**（含 NinePeach），变化全部来自
   "又并进来一个难视图"，不是模型变了。
