# HiFuzz: Hierarchical Reinforcement Learning for Semantic-Aware and Adaptive CPU Fuzzing

## 基本信息

- 作者：Ya Wang、Hanwei Fan、Zhenguo Liu、Xiaofeng Zhou、Yangdi Lyu、Jiang Xu、Wei Zhang
- 发表日期：2026-07-07
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2607.06619v1](http://arxiv.org/abs/2607.06619v1)
- PDF：[https://arxiv.org/pdf/2607.06619v1](https://arxiv.org/pdf/2607.06619v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 13 页，提取 57777 字符

## 摘要

Modern processor verification struggles to reach deep architectural states due to the inefficiencies of traditional mutation-based fuzzing. We propose HiFuzz, a novel hierarchical reinforcement learning framework that replaces mutation with a structured, two-layer generation process: a Program Agent for global layout and a Basic Block Agent for precise instruction filling. To overcome reward sparsity, HiFuzz integrates an adaptive coverage reward mechanism and a semantic-aware basic block encoder providing intrinsic feedback. Extensive evaluations on three real-world RISC-V cores demonstrate that HiFuzz significantly outperforms state-of-the-art fuzzers in coverage and bug detection.

## 研究问题

现代处理器验证中，基于变异的传统fuzzing效率低下，难以达到深层架构状态，且存在反馈稀疏、奖励偏差问题。

## Introduction 梳理

该论文指出现有处理器验证方法（约束随机验证、形式验证）面临状态爆炸和手动开销高的问题。硬件fuzzing虽作为替代方案，但变异方法破坏语义有效性，构造性方法缺乏学习能力。HiFuzz通过层次化强化学习解决三个挑战：复杂动作空间与结构依赖、稀疏反馈与延迟奖励、奖励偏差与掩蔽效应。贡献包括可配置生成框架、双智能体RL、语义感知BB编码器、自适应覆盖奖励机制及实验验证。

## 方法

输入生成：基于层次化构造生成程序，Program Agent（Rainbow DQN）选择全局配置（内存/BB数量/流），Basic Block Agent（PPO）输出指令类别分布，由约束生成器填充具体指令。反馈/覆盖：内在奖励来自BB编码器（Bi-LSTM）聚类距离新颖性；外奖励来自自适应覆盖奖励机制（ACRM），基于UCB动态加权模块级覆盖增益。Oracle：使用Spike作为参考模型进行差异检测。DUT/平台：Rocket、BOOM、CV A6，基于Cocotb、Verilator、Spike。是否需要golden model：是（Spike）。

## 实验与评估

baseline：DifuzzRTL、ProcessorFuzz、Cascade。实验预算：每个DUT 24小时单核。统计：控制寄存器覆盖（Rocket 1.1M vs Cascade 0.74M）、Line/Toggle覆盖（Rocket 75.98%/67.58%）、MUX覆盖（Rocket/BOOM曲线）、bug检测（Encarsia基准：HiFuzz 30/60 vs Cascade 26/60）。bug/CVE：检测到Encarsia中30个bug（BOOM 18/30）。开销：生成时间占30.5%（Rocket），生成测试数9454。Artifact：未确认，但配置可通过YAML文件复现。

## 核心贡献

1）提出层次化双智能体RL架构用于构造性程序生成；2）设计语义感知基本块编码器提供内在奖励；3）基于UCB的自适应覆盖奖励机制平衡模块探索；4）在三个真实RISC-V核上的实验验证。

## 与本仓库研究主线的关系

直接相关。专注于RISC-V处理器fuzzing，采用RL优化覆盖和bug检测，为多hart/一致性路径验证提供了可扩展的基础框架（当前限于单hart）。

## 结论

HiFuzz通过层次化RL、语义嵌入和自适应奖励机制，在三个RISC-V核上显著优于现有fuzzer，覆盖率和bug检测均有提升，且优势在更复杂的DUT上更明显。

## 局限性

仅评估开源RISC-V核（百万门级）；不支持多hart和A扩展；依赖模块级覆盖信号；迁移至其他ISA需替换tokenizer和生成器；报告未对多次随机种子取平均。

## 详细阅读分析

建议深入阅读方法部分（III节）、评估部分（V节）及附录（实现细节和超参数）。

## 后续核验问题

- 如何扩展HiFuzz以支持多hart和内存一致性验证？
- 在更大设计（如GPU或SoC）上表现如何？
- 与其他RL硬件fuzzer（如GenHuzz）有更详细的比较吗？
- BB编码器迁移到其他ISA（如ARM/x86）的具体成本是多少？
