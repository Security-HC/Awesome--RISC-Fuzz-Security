# DejaVuzz: Disclosing Transient Execution Bugs with Dynamic Swappable Memory and Differential Information Flow Tracking Assisted Processor Fuzzing

## 基本信息

- 作者：Jinyan Xu、Yangye Zhou、Xingzhi Zhang、Yinshuai Li、Qinhan Tan、Yinqian Zhang、Yajin Zhou、Rui Chang、Wenbo Shen
- 发表日期：2025-08-06
- 会议/期刊：未记录
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=10）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: processor fuzzing；hardware/processor object: processor, microarchitectural；verification/fuzzing method: fuzz, information flow tracking；security relevance: transient execution
- 论文页面：[https://doi.org/10.1145/3676642.3736115](https://doi.org/10.1145/3676642.3736115)
- PDF：[https://dl.acm.org/doi/pdf/10.1145/3676642.3736115](https://dl.acm.org/doi/pdf/10.1145/3676642.3736115)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 16 页，提取 87419 字符

## 摘要

Transient execution vulnerabilities have emerged as a critical threat to modern processors. Hardware fuzzing testing techniques have recently shown promising results in discovering transient execution bugs in large-scale out-of-order processor designs. However, their poor microarchitectural controllability and observability prevent them from effectively and efficiently detecting transient execution vulnerabilities.

## 研究问题

瞬态执行漏洞在乱序处理器中检测困难，现有硬件fuzzing方法在微架构可控性和可观测性方面存在不足，无法有效触发多样瞬态窗口且无法精确追踪敏感数据传播。

## Introduction 梳理

现有硬件fuzzing方法如SpecDoctor、IntroSpectre等在触发瞬态窗口时受限于地址空间冲突（类型有限、训练开销高），在观测敏感数据时缺乏覆盖率反馈和精确oracle（控制流过沾染）。本文提出动态可交换内存（swapMem）实现地址空间分时复用以增强可控性，提出差分信息流追踪（diffIFT）通过对比不同秘密实例的控制信号消除过沾染以增强可观测性，并构建DejaVuzz fuzzer实现更高效的漏洞检测。

## 方法

输入生成：基于种子随机生成触发指令，利用swapMem隔离训练和瞬态序列以生成任意瞬态窗口；训练推导策略根据瞬态窗口信息生成针对性训练；训练缩减策略通过逐一移除训练包并重仿真判断必要性。反馈/覆盖率：diffIFT生成污点，定义污点覆盖率（模块内污点寄存器数量作为索引记录覆盖点），引导变异。Oracle：首先检查瞬态窗口是否常量时间执行；若否则报告；若是则利用污点活性注释（绑定状态寄存器与污点寄存器）过滤不可利用泄露。DUT/平台：BOOM和XiangShan，使用Synopsys VCS仿真。是否需要golden model：否，采用差分测试（两个DUT实例加载不同秘密）。

## 实验与评估

baseline: 与SpecDoctor比较，并在BOOM上比较DejaVuzz*（随机训练）和DejaVuzz-（无污点覆盖率）。实验预算：2500个瞬态窗口，20,000次迭代（覆盖率实验），5次重复。统计：平均训练指令数（TO/ETO），覆盖点数，仿真时间。bug/CVE：发现5个新漏洞，分配6个CVE（CVE-2024-44590至44595）。开销：diffIFT编译时间比Base增加约2.2倍（BOOM 268 vs 122秒），仿真时间增加约2-3倍；CellIFT在BOOM上编译用时2856秒且仿真慢。Artifact：代码开源在https://github.com/sycuricon/DejaVuzz。

## 核心贡献

1) 总结了瞬态执行fuzzing的微架构可控性和可观测性挑战，提出swapMem和diffIFT两个原语。2) 基于原语设计DejaVuzz，包括训练推导/缩减、污点覆盖率、污点活性分析。3) 在真实处理器上发现5个新漏洞并分配CVE。

## 与本仓库研究主线的关系

直接相关（处理器Fuzzing、微架构安全自动测试、Oracle）。与多hart/一致性路径关系：论文聚焦单处理器内核，未涉及多hart或内存一致性验证，但diffIFT的差分思路可推广到一致性验证中的状态比较。

## 结论

DejaVuzz利用swapMem和diffIFT增强微架构可控性和可观测性，在BOOM和XiangShan上比SpecDoctor提升4.7倍覆盖率，发现5个新漏洞（6个CVE），证明了有效性。

## 局限性

1) diffIFT是近似解，可能因秘密对产生相同控制信号导致假阴性（可通过尝试不同秘密对缓解）。2) 训练缩减策略倾向于选择开销最小的训练序列，可能忽略需要更长时间训练的预测器。3) 生成的刺激只能在swapMem上运行，迁移到标准内存模型需手动拼接。4) 污点活性注释目前需手动进行，未来可考虑自动注释。

## 详细阅读分析

建议重点阅读第3节（Operating Primitives）、第4节（DejaVuzz Framework）、第6节（Evaluation）中的Table 3、Table 4、Figure 7。特别关注训练缩减策略和污点活性分析的设计细节。

## 后续核验问题

- 1) diffIFT的假阴性率如何定量评估？作者仅给出worst-case实验。
- 2) swapMem在真实硬件（如黑盒处理器）上的可移植性？
- 3) 能否将swapMem与多核/多hart场景结合用于一致性测试？
- 4) 污点活性注释能否自动化？
- 5) 与形式化验证方法相比，DejaVuzz的覆盖完备性如何？
