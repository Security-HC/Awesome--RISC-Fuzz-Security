# Lyra: A Hardware-Accelerated RISC-V Verification Framework with Generative Model-Based Processor Fuzzing

## 基本信息

- 作者：Juncheng Huo、Yunfan Gao、Xinxin Liu、Sa Wang、Yungang Bao、Xitong Gao、Kan Shi
- 发表日期：2025-12-15
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=9）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: processor fuzzing；hardware/processor object: risc-v, processor, soc；verification/fuzzing method: fuzz, verification
- 论文页面：[http://arxiv.org/abs/2512.13686v3](http://arxiv.org/abs/2512.13686v3)
- PDF：[https://arxiv.org/pdf/2512.13686v3](https://arxiv.org/pdf/2512.13686v3)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 7 页，提取 36625 字符

## 摘要

As processor designs grow more complex, verification remains bottlenecked by slow software simulation and low-quality random test stimuli. Recent research has applied software fuzzers to hardware verification, but these rely on semantically blind random mutations that may generate shallow, low-quality stimuli unable to explore complex behaviors. These limitations result in slow coverage convergence and prohibitively high verification costs. In this paper, we present Lyra, a heterogeneous RISC-V verification framework that addresses both challenges by pairing hardware-accelerated verification with an ISA-aware generative model. Lyra executes the DUT and reference model concurrently on an FPGA SoC, enabling high-throughput differential checking and hardware-level coverage collection. Instead of creating verification stimuli randomly or through simple mutations, we train a domain-specialized generative model, LyraGen, with inherent semantic awareness to generate high-quality, semantically rich instruction sequences. Empirical results show Lyra achieves up to $1.27\times$ higher coverage and accelerates end-to-end verification by up to $107\times$ to $3343\times$ compared to state-of-the-art software fuzzers, while consistently demonstrating lower convergence difficulty.

## 研究问题

处理器验证面临软件仿真速度慢（仅几十kHz）和随机测试质量低的问题，现有硬件fuzzer依赖盲随机变异（位翻转），缺乏指令语义理解，难以生成语义连贯的指令序列来触发深层微架构状态。

## Introduction 梳理

RISC-V处理器设计复杂性增加，验证占开发投入70%。现有验证方法依赖软件仿真和人工构造测试，效率低。软件fuzzer（如DifuzzRTL、Cascade）采用覆盖引导变异，但依赖盲随机变异，缺乏指令语义理解，难以生成语义连贯的指令序列来触发深层微架构状态。本文提出Lyra，结合硬件加速和ISA感知生成模型，以解决性能和语义双重瓶颈。

## 方法

输入生成：使用LyraGen（基于OPT-125M重新训练）生成RISC-V指令序列，训练数据来自软件fuzzer与FPGA测试床协同生成的<指令, 覆盖>对。反馈/coverage：基于Register Coverage指标，在FPGA上硬件收集覆盖数据并反馈给生成模型。Oracle：微分检查，DUT（RocketCore）与参考模型（软件ISA模拟器）在FPGA SoC上并行执行，硬件检查器逐指令比较。DUT/平台：RocketCore在FPGA PL运行，REF在ARM处理器运行。是否需要golden model：需要（软件ISA模拟器作为参考模型）。

## 实验与评估

baseline: DifuzzRTL和Cascade。实验预算：9.24 million <指令, 覆盖>对用于训练。统计：覆盖率最高1.27×高于DifuzzRTL，端到端速度提升107×至3343×（FP16），收敛难度（DCV）远低于baseline。bug/CVE：未报告。开销：训练58分钟（RTX 4090），FPGA实现使用Vivado 2020.2，100MHz。Artifact：未确认（论文未提供开源链接）。

## 核心贡献

1. 首次提出GPU-CPU-FPGA异构协同验证框架，将测试执行、微分检查、覆盖收集卸载到硬件，生成模型驱动高效激励生成。2. 开发LyraGen，通过RISC-V指令分词方案和监督覆盖条件训练，生成语义丰富的指令序列。3. 实验证明覆盖率最高提升1.27倍，端到端速度提升107-3343倍，收敛难度更低。

## 与本仓库研究主线的关系

直接相关。该论文是RISC-V处理器fuzzing的典型工作，同时涉及覆盖、Oracle、硬件加速。与多hart/一致性路径关系：论文未涉及多hart或内存一致性，专注于单核心RISC-V验证。可借鉴其硬件加速和生成模型方法，但一致性验证需要多核模型扩展。

## 结论

Lyra通过ISA感知生成模型和FPGA加速，解决语义盲点和仿真瓶颈，实现更高覆盖和更快吞吐。

## 局限性

未明确提及。可推断：依赖FPGA硬件平台，可能不适用于所有设计；模型生成指令需合法性检查和地址校正，增加开销；未报告发现具体bug数量；仅使用RocketCore一个DUT。

## 详细阅读分析

需要对RISC-V ISA、FPGA加速、生成模型（OPT）、微分检查机制有深入理解。建议阅读其引用的Encore、DifuzzRTL、Cascade。

## 后续核验问题

- Lyra能否扩展到多核RISC-V处理器验证？
- 模型训练数据中是否包含多hart交互场景？
- 如何确保生成指令不触发硬件安全漏洞？
- 与其他ML-based fuzzer（如ChatFuzz）对比结果如何？
- 代码和训练数据是否开源？
