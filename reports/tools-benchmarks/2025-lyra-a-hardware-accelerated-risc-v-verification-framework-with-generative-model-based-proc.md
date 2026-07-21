# Lyra: A Hardware-Accelerated RISC-V Verification Framework with Generative Model-Based Processor Fuzzing

## 基本信息

- 作者：Juncheng Huo、Yunfan Gao、Xinxin Liu、Sa Wang、Yungang Bao、Xitong Gao、Kan Shi
- 发表日期：2025-12-15
- 更新日期：2026-03-04
- 来源：arXiv
- 来源编号：2512.13686v3
- 研究类别：RISC-V Fuzzing 研究、处理器与 CPU Fuzzing、RTL 与硬件验证、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：5
- 论文页面：[http://arxiv.org/abs/2512.13686v3](http://arxiv.org/abs/2512.13686v3)
- PDF：[https://arxiv.org/pdf/2512.13686v3](https://arxiv.org/pdf/2512.13686v3)
- 分析模式：仅元数据分析

## 摘要

As processor designs grow more complex, verification remains bottlenecked by slow software simulation and low-quality random test stimuli. Recent research has applied software fuzzers to hardware verification, but these rely on semantically blind random mutations that may generate shallow, low-quality stimuli unable to explore complex behaviors. These limitations result in slow coverage convergence and prohibitively high verification costs. In this paper, we present Lyra, a heterogeneous RISC-V verification framework that addresses both challenges by pairing hardware-accelerated verification with an ISA-aware generative model. Lyra executes the DUT and reference model concurrently on an FPGA SoC, enabling high-throughput differential checking and hardware-level coverage collection. Instead of creating verification stimuli randomly or through simple mutations, we train a domain-specialized generative model, LyraGen, with inherent semantic awareness to generate high-quality, semantically rich instruction sequences. Empirical results show Lyra achieves up to $1.27\times$ higher coverage and accelerates end-to-end verification by up to $107\times$ to $3343\times$ compared to state-of-the-art software fuzzers, while consistently demonstrating lower convergence difficulty.

## 研究问题

As processor designs grow more complex, verification remains bottlenecked by slow software simulation and low-quality random test stimuli. Recent research has applied software fuzzers to hardware verification, but these rely on semantically blind random mutations that may generate shallow, low-quality stimuli unable to explore complex behaviors. These limitations result in slow coverage convergence and prohibitively high verification costs. In this paper, we present Lyra, a heterogeneous RISC-V verification framework that addresses both challenges by pairing hardware-accelerated verification with an ISA-aware generative model. Lyra executes the DUT and reference model concurrently on an FPGA SoC, enabling high-throughput differential checking and hardware-level coverage collection. Instead of creating verification stimuli randomly or through simple mutations, we train a domain-specialized generative model, LyraGen, with inherent semantic awareness to generate high-quality, semantically rich instruction sequences. Empirical results show Lyra achieves up to $1.27\times$ higher coverage and accelerates end-to-end verification by up to $107\times$ to $3343\times$ compared to state-of-the-art software fuzzers, while consistently demonstrating lower convergence difficulty.

## Introduction 梳理

当前为基于题名和摘要生成的记录。配置 OPENAI_API_KEY 或 DEEPSEEK_API_KEY 后，可以启用全文阅读分析。

## 方法

等待全文提取后补充。

## 实验与评估

等待全文提取后补充。

## 结论

等待全文提取后补充。

## 局限性

等待全文提取后补充。初步阅读时应重点检查适用架构、测试对象、oracle 设计、覆盖率指标和复现实验条件。

## 详细阅读分析

等待全文提取后补充。建议结合论文 PDF、开源 artifact、实验对象和可迁移到 RISC-V/处理器 fuzzing 的部分继续分析。

## 后续跟进问题

- 论文是否提供开源实现或实验 artifact？
- 方法是否可以迁移到 RISC-V core、RTL 仿真器或真实处理器？
- 论文依赖什么 oracle、覆盖率指标或差分测试对象？
