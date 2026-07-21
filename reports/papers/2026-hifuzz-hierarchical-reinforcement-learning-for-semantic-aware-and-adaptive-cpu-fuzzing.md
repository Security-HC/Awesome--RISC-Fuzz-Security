# HiFuzz: Hierarchical Reinforcement Learning for Semantic-Aware and Adaptive CPU Fuzzing

## 基本信息

- 作者：Ya Wang、Hanwei Fan、Zhenguo Liu、Xiaofeng Zhou、Yangdi Lyu、Jiang Xu、Wei Zhang
- 发表日期：2026-07-07
- 更新日期：2026-07-07
- 来源：arXiv
- 来源编号：2607.06619v1
- 研究类别：RISC-V Fuzzing、Processor and CPU Fuzzing、Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[http://arxiv.org/abs/2607.06619v1](http://arxiv.org/abs/2607.06619v1)
- PDF：[https://arxiv.org/pdf/2607.06619v1](https://arxiv.org/pdf/2607.06619v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

Modern processor verification struggles to reach deep architectural states due to the inefficiencies of traditional mutation-based fuzzing. We propose HiFuzz, a novel hierarchical reinforcement learning framework that replaces mutation with a structured, two-layer generation process: a Program Agent for global layout and a Basic Block Agent for precise instruction filling. To overcome reward sparsity, HiFuzz integrates an adaptive coverage reward mechanism and a semantic-aware basic block encoder providing intrinsic feedback. Extensive evaluations on three real-world RISC-V cores demonstrate that HiFuzz significantly outperforms state-of-the-art fuzzers in coverage and bug detection.

## 研究问题

传统基于变异的处理器模糊测试由于生成程序语义有效性低、覆盖率信号稀疏，难以深入处理器微架构深层状态，且单一全局覆盖率优化易导致探索偏置（masking effect），忽视难覆盖模块。

## Introduction 梳理

随着摩尔定律放缓，处理器微架构复杂度激增，RISC-V生态扩张导致设计状态空间爆炸，功能验证占研发周期超70%。传统方法如约束随机验证效率低、形式化验证面临状态爆炸，硬件模糊测试成为可扩展方案。但现有变异或随机生成方法缺乏学习机制，探索盲目，难以生成有效程序。HiFuzz采用分层强化学习（HRL）框架，通过程序代理（Program Agent）和基本块代理（Basic Block Agent）结构化生成程序，引入语义感知基本块编码器（Semantic-Aware BB Encoder）提供内在奖励，以及基于UCB的自适应覆盖率奖励机制（ACRM）平衡模块探索。

## 方法

HiFuzz框架包含：1）可配置测试生成器，分层配置全局结构（内存布局、基本块数、控制流）和局部指令填充；2）双智能体HRL架构：程序代理（Rainbow DQN）选择全局配置，基本块代理（PPO）选择指令类别分布；3）语义感知基本块编码器：通过两阶段训练（自监督掩码语言建模+监督对比学习）生成DUT无关的嵌入向量，用于计算内在新颖性奖励；4）自适应覆盖率奖励机制：将覆盖率分解为模块级，使用UCB动态加权，避免探索偏置。训练时，内在奖励用于基本块代理，外在奖励（加权覆盖率增益）用于程序代理。

## 实验与评估

在三个开源RISC-V处理器（Rocket、BOOM、CV A6）上评估，与DifuzzRTL、ProcessorFuzz、Cascade对比。24小时实验中，HiFuzz在Rocket上控制寄存器覆盖率比Cascade提升48.9%，每测试覆盖率提升3.3倍；在CV A6上总覆盖率（Line+Toggle）提升7.2%。模块级分析显示ACRM有效将权重从饱和模块转向难覆盖模块（如FPU）。消融实验表明，加入BB编码器和ACRM后覆盖率相比仅用Dual-Agent基线提升51.87%。MUX覆盖率在BOOM上优势显著。此外，HiFuzz生成程序平均依赖链长度18.5，指令执行率96.7%。

## 结论

HiFuzz通过分层RL和语义感知内在奖励、自适应覆盖率机制，显著提升了处理器模糊测试的覆盖率和bug检测能力，在多种RISC-V核上均优于现有方法，验证了方法的通用性和有效性。

## 局限性

1）RL训练开销较大（30.5%生成时间用于RL），可能限制在资源受限场景的部署；2）BB编码器需要离线预训练，且依赖RISC-V指令集语义，扩展到其他ISA需重新训练；3）自适应机制依赖于模块划分，不同设计的模块粒度可能影响效果；4）当前仅在三个RISC-V核上验证，更广泛的处理器架构（如x86）未测试。

## 详细阅读分析

HiFuzz的核心创新在于将程序生成分解为全局和局部两层，分别用Rainbow DQN和PPO优化，解决了动作空间巨大和有效性约束问题。BB编码器通过结构化分词和两阶段训练实现了DUT无关的语义嵌入，为基本块代理提供即时反馈。ACRM基于UCB设计，其中探索项使用模块饱和度（1- cov/max_cov），利用项使用历史平均覆盖率增益，动态调整权重，有效缓解了全局优化中的掩蔽效应。实验表明，即使不依赖Chisel特定覆盖，在SV的CV A6上仍有效。与GenHuzz的对比虽无法直接数值比较，但程序质量指标（依赖链长度、执行率）优于其基于token的生成方式。

## 后续跟进问题

- HiFuzz的层次化强化学习框架能否扩展到多核处理器或异构SoC的模糊测试？
- BB编码器的两阶段训练是否可直接迁移到其他指令集（如ARM、x86）？需如何调整tokenizer和相似度度量？
- ACRM中的UCB参数（如β(t)的增长率、温度τ）对收敛性和探索平衡的敏感度如何？是否存在自适应调优方法？
- HiFuzz在检测安全漏洞（如预测执行侧信道）方面的能力是否优于现有模糊测试工具？报告了哪些具体bug？
- 与基于Transformer或图神经网络的生成模型相比，HiFuzz在覆盖率和生成效率上的优势是否显著？可进行公平比较实验。
