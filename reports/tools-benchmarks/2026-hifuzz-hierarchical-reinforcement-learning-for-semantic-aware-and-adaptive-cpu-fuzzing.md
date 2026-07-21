# HiFuzz: Hierarchical Reinforcement Learning for Semantic-Aware and Adaptive CPU Fuzzing

## 基本信息

- 作者：Ya Wang、Hanwei Fan、Zhenguo Liu、Xiaofeng Zhou、Yangdi Lyu、Jiang Xu、Wei Zhang
- 发表日期：2026-07-07
- 更新日期：2026-07-07
- 来源：arXiv
- 来源编号：2607.06619v1
- 研究类别：RISC-V Fuzzing 研究、处理器与 CPU Fuzzing、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[http://arxiv.org/abs/2607.06619v1](http://arxiv.org/abs/2607.06619v1)
- PDF：[https://arxiv.org/pdf/2607.06619v1](https://arxiv.org/pdf/2607.06619v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

Modern processor verification struggles to reach deep architectural states due to the inefficiencies of traditional mutation-based fuzzing. We propose HiFuzz, a novel hierarchical reinforcement learning framework that replaces mutation with a structured, two-layer generation process: a Program Agent for global layout and a Basic Block Agent for precise instruction filling. To overcome reward sparsity, HiFuzz integrates an adaptive coverage reward mechanism and a semantic-aware basic block encoder providing intrinsic feedback. Extensive evaluations on three real-world RISC-V cores demonstrate that HiFuzz significantly outperforms state-of-the-art fuzzers in coverage and bug detection.

## 研究问题

传统基于变异的处理器fuzzing方法难以达到深层架构状态，主要面临三个挑战：复杂动作空间与结构依赖（构造性生成需逐指令生成而保持语义有效性）、稀疏反馈与延迟奖励（覆盖率信号仅在完整程序执行后获得）、奖励偏差与掩盖效应（单一聚合覆盖率导致易于覆盖模块主导奖励，忽略难覆盖组件）。

## Introduction 梳理

HiFuzz提出一种分层强化学习框架，取代传统变异操作，采用程序智能体（Program Agent）和基本块智能体（Basic Block Agent）两层级生成过程，分别负责全局布局和精确指令填充。通过语义感知基本块编码器（Semantic-Aware Basic Block Encoder）提供内在反馈，解决奖励稀疏性；通过自适应覆盖率奖励机制（Adaptive Coverage Reward Mechanism）基于UCB算法动态调整模块权重，缓解掩盖效应。在三个真实RISC-V核（Rocket、BOOM、CVA6）上的评估表明，HiFuzz在覆盖率和bug检测上显著优于现有最先进fuzzer。

## 方法

HiFuzz采用分层RL架构：1) 程序智能体（Rainbow DQN）选择全局配置（内存、基本块数、控制流结构等），动作空间为1375种离散配置；2) 基本块智能体（PPO）基于程序智能体输出生成基本块内指令序列，输出指令类别分布和终止模式。内在奖励来自语义感知基本块编码器，该编码器通过两阶段训练：第一阶段自监督掩码语言建模学习RISC-V语法，第二阶段对比学习对齐自定义基本块相似度指标。外在奖励通过自适应覆盖率奖励机制计算，将覆盖率分解到模块级别，使用UCB公式动态加权每个模块的覆盖率增益。两个奖励流在PPO中通过双优势actor损失分离。

## 实验与评估

在Rocket、BOOM、CVA6三个RISC-V核上进行了24小时fuzzing实验。主要指标：控制寄存器覆盖率（Rocket上HiFuzz达1,102,343，比Cascade提升48.9%；每测试覆盖率116.60，比Cascade的34.53提升3.3倍）；总覆盖率（CVA6上HiFuzz 55,241 vs Cascade 51,541，提升7.2%）；模块级覆盖率（fpuOpt等难覆盖模块提升显著，ACRM权重动态调整）；MUX覆盖率（Rocket上HiFuzz略优，BOOM上优势更大）；行/翻转覆盖率（HiFuzz达75.98%/67.58%，优于基线）。消融实验：仅双智能体基线比Cascade提升有限，加入BB编码器后显著提升，加入ACRM后达到最佳，整体比双智能体基线提升51.87%。

## 结论

HiFuzz通过分层RL、语义感知基本块编码器和自适应覆盖率奖励机制，有效解决了构造性生成中的控制-有效性困境、奖励稀疏性和掩盖效应，在多个RISC-V处理器上实现了更高的覆盖率和更好的bug检测能力。分层架构使得程序级和指令级决策解耦，内在奖励提供稠密学习信号，自适应机制平衡模块探索。

## 局限性

1) 实验限于三个RISC-V核，未验证在更复杂或不同ISA处理器上的通用性；2) BB编码器需离线训练，虽然复用但初始训练成本未计入fuzzing预算；3) 程序智能体动作空间大小（1375）基于经验设计，可能限制最优配置搜索；4) 自适应覆盖率奖励机制依赖于模块划分，不同设计的模块粒度和覆盖率可访问性不同；5) 与GenHuzz等方法的公平对比受限，因模拟后端和模型不同。

## 详细阅读分析

HiFuzz的核心创新在于将分层RL与语义感知编码器结合解决硬件fuzzing中的奖励稀疏问题。语义感知编码器通过两阶段训练（MLM+对比学习）学习基本块的微架构感知表示，从而在不运行RTL仿真的情况下提供内在奖励。自适应覆盖率奖励机制基于UCB的加权方式避免了传统单目标优化中的掩盖效应，使得fuzzer持续关注难覆盖模块。分层架构（程序智能体+基本块智能体）有效分解了生成任务，使得动作空间可控。实验设计较为全面，包括消融实验、跨DUT验证、模块级覆盖率分析。

## 后续跟进问题

- HiFuzz的分层RL架构是否可扩展到其他硬件设计（如GPU、加速器）的fuzzing？
- BB编码器的两阶段训练是否可以通过在线微调适应特定DUT的微架构？
- 自适应覆盖率奖励机制中的UCB参数（如β(t)动态策略）如何自动调优？
- HiFuzz生成的测试程序能否检测已知安全漏洞（如Meltdown/Spectre类型）？
- 与基于随机网络蒸馏（RND）的内在奖励相比，语义感知编码器的计算开销和效果优势如何量化？
