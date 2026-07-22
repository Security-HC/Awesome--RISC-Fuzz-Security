# HiFuzz: Hierarchical Reinforcement Learning for Semantic-Aware and Adaptive CPU Fuzzing

## 基本信息

- 作者：Ya Wang、Hanwei Fan、Zhenguo Liu、Xiaofeng Zhou、Yangdi Lyu、Jiang Xu、Wei Zhang
- 发表日期：2026-07-07
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2607.06619v1](http://arxiv.org/abs/2607.06619v1)
- PDF：[https://arxiv.org/pdf/2607.06619v1](https://arxiv.org/pdf/2607.06619v1)
- 分析模式：DeepSeek PDF 首 8 页与末 2 页文本：deepseek-v4-flash

## 摘要

Modern processor verification struggles to reach deep architectural states due to the inefficiencies of traditional mutation-based fuzzing. We propose HiFuzz, a novel hierarchical reinforcement learning framework that replaces mutation with a structured, two-layer generation process: a Program Agent for global layout and a Basic Block Agent for precise instruction filling. To overcome reward sparsity, HiFuzz integrates an adaptive coverage reward mechanism and a semantic-aware basic block encoder providing intrinsic feedback. Extensive evaluations on three real-world RISC-V cores demonstrate that HiFuzz significantly outperforms state-of-the-art fuzzers in coverage and bug detection.

## 研究问题

传统变异式处理器fuzzing难以到达深度架构状态，且现有建设性生成方法缺乏学习机制；将强化学习应用于建设性程序生成面临动作空间复杂、奖励稀疏和偏置三大挑战。

## Introduction 梳理

现有验证方法（约束随机验证、形式验证和硬件fuzzing）在应对现代处理器复杂度时存在不足：变异式fuzzing（如DifuzzRTL）生成程序语义有效性低，难以到达深层次状态；建设性生成（如Cascade）虽然能构造有效程序，但基于随机启发式，缺乏学习能力。最近基于RL的fuzzer（如ChatFuzz、GenHuzz）采用扁平令牌序列生成，未利用程序结构，且存在策略优化与DUT绑定、奖励稀疏等问题。本文针对这些问题提出HiFuzz，通过层次化RL、语义感知编码器和自适应覆盖奖励机制实现高效、平衡的探索。核心贡献包括：可配置测试生成框架、双智能体RL架构、语义感知基本块编码器、自适应覆盖奖励机制，以及在三款RISC-V处理器上的全面评估。

## 方法

{'DUT_platform': '三款RISC-V处理器：Rocket（有序，Chisel）、BOOM（乱序，Chisel）、CVA6（六阶段，SystemVerilog）。仿真基于Cocotb和Verilator。', 'feedback': '两种奖励信号：1) 内在奖励——由语义感知基本块编码器计算生成基本块的新颖性（基于在线聚类距离），无需RTL仿真；2) 外在奖励——自适应覆盖奖励机制(ACRM)基于UCB算法，对每个模块的覆盖增益按权重求和，动态平衡探索。覆盖指标包括行覆盖、信号翻转覆盖、多路选择器覆盖、控制寄存器覆盖。', 'golden_model': '需要，Spike作为行为参考模型。', 'input_generation': '基于层次化配置的构造性生成：全局配置（内存布局、基本块数量、控制流模板）由Program Agent决定；基本块内指令序列（指令类别混合、终止模式）由Basic Block Agent决定。两者协作生成完整RISC-V程序，并通过整体验证确保有效性。', 'oracle': '使用Spike作为参考模型（golden model），对比处理器行为以检测bug。'}

## 实验与评估

{'artifact': '未确认。', 'baselines': 'DifuzzRTL、ProcessorFuzz、Cascade。', 'bug_CVE': '使用Encarsia注入的bug集合，共15个（Rocket 8个混合+7个条件，BOOM 8个混合+7个条件）。HiFuzz检测到Rocket混合7/8、条件5/7；BOOM混合11/15、条件5/15。具体检测结果见附录表。未提及CVE。', 'experiment_budget': '每个DUT进行24小时fuzzing，使用相同CPU核数，覆盖生成、RL推理/更新、RTL仿真和覆盖收集。', 'overhead': '生成时间（排除仿真）：HiFuzz生成时间占总时间30.5%（7.32小时），高于Cascade（4.4%）但低于ProcessorFuzz（52.5%）。BB编码器训练一次离线，不计入24小时预算。', 'statistics': '主指标：控制寄存器覆盖点（Rocket），总覆盖（CVA6行+翻转）。额外报告：每测试覆盖、模块级覆盖、MUX覆盖、行/翻转百分比。结果：HiFuzz在Rocket上控制寄存器覆盖相比Cascade提升48.9%，每测试覆盖提升3.3倍；在CVA6上总覆盖提升7.2%。'}

## 核心贡献

1) 提出层次化RL双智能体架构，分解程序生成为全局结构和局部指令填充；2) 设计语义感知基本块编码器，提供无仿真内在奖励；3) 开发基于UCB的自适应覆盖奖励机制，缓解探索偏置；4) 在三个真实RISC-V核心上展示优于现有fuzzer的覆盖率和bug检测。

## 与本仓库研究主线的关系

直接相关：主题为RISC-V处理器fuzzing，与多处理器/内存一致性验证路径不同，但提出的层次化生成和奖励机制可借鉴于更复杂的验证场景。方法提供模块级覆盖分解思路，对多harts场景可能适用。

## 结论

HiFuzz通过层次化RL、语义感知内在奖励和自适应覆盖奖励机制，显著提升了RISC-V处理器fuzzing的覆盖率和bug检测能力，在三款核心上优于现有方法。

## 局限性

评估集中于单核RISC-V处理器，未涉及多核、内存一致性或更复杂微架构；奖励设计依赖模块级分解，可能不适用于高度耦合的设计；BB编码器需要离线训练，对新型ISA扩展需重新训练；仅针对RISC-V G子集，未验证扩展指令集。

## 详细阅读分析

评估部分充分，但存在潜在不足：1) 基线选择不包括任何基于RL的fuzzer（如GenHuzz），虽然文中给出结构对比但无实验；2) 奖励稀疏问题在BB编码器下缓解，但内在奖励与微架构行为的相关性未直接验证；3) 模块分解策略可能对非Chisel设计需要手动定义；4) bug检测实验注入的bug数量有限，且部分bug未被任何fuzzer检测到（如表VII中BOOM Mix-ups #3,#13为零检测），说明测试集难度不一。

## 后续核验问题

- 1) HiFuzz的单层次组件的通用性如何？是否可推广到多核或复杂SoC？
- 2) BB编码器的预训练语料大小和生成方式是否影响新颖性度量？
- 3) 如何在保持语义约束的同时，让RL代理更细粒度控制指令选择？
- 4) 奖励平衡机制能否自适应模块数量的增加？
- 5) 与GenHuzz等RL fuzzer的直接性能对比如何？
