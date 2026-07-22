# MABFuzz: Multi-Armed Bandit Algorithms for Fuzzing Processors

## 基本信息

- 作者：Vasudev Gohil、Rahul Kande、Chen Chen、Ahmad-Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2023-11-24
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Microarchitectural Security Testing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2311.14594v1](http://arxiv.org/abs/2311.14594v1)
- PDF：[https://arxiv.org/pdf/2311.14594v1](https://arxiv.org/pdf/2311.14594v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 7 页，提取 34993 字符

## 摘要

As the complexities of processors keep increasing, the task of effectively verifying their integrity and security becomes ever more daunting. The intricate web of instructions, microarchitectural features, and interdependencies woven into modern processors pose a formidable challenge for even the most diligent verification and security engineers. To tackle this growing concern, recently, researchers have developed fuzzing techniques explicitly tailored for hardware processors. However, a prevailing issue with these hardware fuzzers is their heavy reliance on static strategies to make decisions in their algorithms. To address this problem, we develop a novel dynamic and adaptive decision-making framework, MABFuzz, that uses multi-armed bandit (MAB) algorithms to fuzz processors. MABFuzz is agnostic to, and hence, applicable to, any existing hardware fuzzer. In the process of designing MABFuzz, we encounter challenges related to the compatibility of MAB algorithms with fuzzers and maximizing their efficacy for fuzzing. We overcome these challenges by modifying the fuzzing process and tailoring MAB algorithms to accommodate special requirements for hardware fuzzing. We integrate three widely used MAB algorithms in a state-of-the-art hardware fuzzer and evaluate them on three popular RISC-V-based processors. Experimental results demonstrate the ability of MABFuzz to cover a broader spectrum of processors' intricate landscapes and doing so with remarkable efficiency. In particular, MABFuzz achieves up to 308x speedup in detecting vulnerabilities and up to 5x speedup in achieving coverage compared to a state-of-the-art technique.

## 研究问题

现有硬件处理器fuzzer严重依赖静态策略进行决策（如种子选择、变异算子选择），导致效率低下，无法自适应地平衡探索与利用，限制了漏洞检测和覆盖率的提升。

## Introduction 梳理

处理器复杂度持续增加，验证时间缩短，导致安全漏洞频发。硬件fuzzing虽被提出，但现有fuzzer（如TheHuzz）在种子选择、变异算子等方面依赖静态策略（如FIFO或随机），不能动态调整。先前工作[10]仅改进了变异算子选择，但未涉及其它决策点。本文提出MABFuzz，利用多臂老虎机（MAB）算法动态选择种子，以平衡探索与利用，提升漏洞检测速度和覆盖率。贡献包括：首次将MAB算法用于硬件fuzzer种子选择；修改MAB算法以适应fuzzing中奖励递减的特性；集成三种MAB算法；实验证明显著加速。

## 方法

输入生成：初始种子由随机指令生成，通过突变（如位翻转）产生新测试，并添加到对应arm的测试池中。反馈/Coverage：使用分支覆盖作为反馈指标，监测每轮模拟中覆盖的新分支点。Oracle：采用差分测试，以RISC-V ISA模拟器SPIKE作为golden reference model，比较硬件处理器的架构状态。DUT/平台：三个RISC-V开源处理器CVA6、Rocket Core、BOOM；仿真环境为Synopsys VCS，SoC平台为Chipyard。是否需要golden model：是，依赖ISA模拟器作为预期正确的参考。MAB算法：采用ε-greedy、UCB和EXP3三种算法，并针对硬件fuzzing做了修改（如重置饱和arm、归一化奖励）。

## 实验与评估

Baseline：TheHuzz（state-of-the-art仿真型处理器fuzzer）。实验预算：每个处理器运行50,000个测试，每个实验重复至少3次。统计：计算漏洞检测速度提升（倍数）和覆盖率提升（速度倍数和百分比增量）。Bug/CVE：检测到7个漏洞（V1–V7），分别对应CWE-440、1242、1202、1202、1252、1281、1201。开销：未明确报告具体时间或资源开销，仅提及实验平台（Intel Xeon，64线程，512GB RAM，2.6GHz）。Artifact：未提及是否公开代码或数据。

## 核心贡献

1) 第一个将多臂老虎机算法应用于硬件处理器fuzzer种子选择的框架MABFuzz。2) 解决了MAB与硬件fuzzing兼容性问题：设计了γ-窗口监测饱和臂，并修改MAB算法（重置计数/权重）以适应奖励递减特性。3) 在三个RISC-V处理器上集成并评估了三种MAB算法（ε-greedy、UCB、EXP3），证明其有效性。4) 漏洞检测速度最高提升308.89倍，覆盖率速度最高提升5.38倍，且覆盖率增量最高0.68%。

## 与本仓库研究主线的关系

直接相关。论文专注于RISC-V处理器fuzzing，提出基于MAB的动态种子选择方法，可应用于本仓库中处理器fuzzing研究。与多hart/一致性路径研究：本文仅处理单处理器fuzzing，未涉及多hart或内存一致性，但MAB算法可扩展至多hart环境下的种子选择或调度问题，作为一个方法借鉴。

## 结论

MABFuzz通过动态种子选择和自适应平衡探索/利用，显著优于静态策略的TheHuzz。在检测漏洞速度上最高提升308.89倍，在覆盖率上最高提升5.38倍，且平均覆盖率增量达0.68%。该方法与底层fuzzer无关，可适用于任何硬件fuzzer。

## 局限性

1) MABFuzz修改了标准MAB算法以适应硬件fuzzing，但缺乏对修改后算法的理论分析（如regret bound）。2) 当前仅应用于种子选择，其他决策点（如变异算子选择、测试长度）尚未探索。3) 实验仅在RISC-V处理器上进行，对其他指令集架构的适用性未知。4) 当基线已有很高覆盖率（如BOOM上TheHuzz达到>95%），MABFuzz的覆盖率提升有限。

## 详细阅读分析

建议重点阅读Section III-C和III-D，理解MAB算法如何修改以应对奖励递减（γ-窗口重置）以及算法1和2的具体实现。同时关注实验部分表I中不同MAB算法在不同漏洞上的表现差异，以理解算法选择的折衷。

## 后续核验问题

- MABFuzz能否应用于多处理器或多hart场景，用于调度不同hart的测试以加速一致性验证？
- MAB算法的理论分析（如regret bound）如何扩展到修改后的版本？
- 能否将MAB用于其他决策点（如变异算子选择、测试长度等）并与种子选择联合优化？
- MABFuzz在检测复杂微架构安全漏洞（如侧信道或瞬态执行漏洞）方面的效果如何？
