# Lyra: A Hardware-Accelerated RISC-V Verification Framework with Generative Model-Based Processor Fuzzing

## 基本信息

- 作者：Juncheng Huo、Yunfan Gao、Xinxin Liu、Sa Wang、Yungang Bao、Xitong Gao、Kan Shi
- 发表日期：2025-12-15
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=9）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: processor fuzzing；hardware/processor object: risc-v, processor, soc；verification/fuzzing method: fuzz, verification
- 论文页面：[http://arxiv.org/abs/2512.13686v3](http://arxiv.org/abs/2512.13686v3)
- PDF：[https://arxiv.org/pdf/2512.13686v3](https://arxiv.org/pdf/2512.13686v3)
- 分析模式：摘要级占位（未全文核验）

## 摘要

As processor designs grow more complex, verification remains bottlenecked by slow software simulation and low-quality random test stimuli. Recent research has applied software fuzzers to hardware verification, but these rely on semantically blind random mutations that may generate shallow, low-quality stimuli unable to explore complex behaviors. These limitations result in slow coverage convergence and prohibitively high verification costs. In this paper, we present Lyra, a heterogeneous RISC-V verification framework that addresses both challenges by pairing hardware-accelerated verification with an ISA-aware generative model. Lyra executes the DUT and reference model concurrently on an FPGA SoC, enabling high-throughput differential checking and hardware-level coverage collection. Instead of creating verification stimuli randomly or through simple mutations, we train a domain-specialized generative model, LyraGen, with inherent semantic awareness to generate high-quality, semantically rich instruction sequences. Empirical results show Lyra achieves up to $1.27\times$ higher coverage and accelerates end-to-end verification by up to $107\times$ to $3343\times$ compared to state-of-the-art software fuzzers, while consistently demonstrating lower convergence difficulty.

## 研究问题

摘要级初步判断（未核验正文）：As processor designs grow more complex, verification remains bottlenecked by slow software simulation and low-quality random test stimuli. Recent research has applied software fuzzers to hardware verification, but these rely on semantically blind random mutations that may generate shallow, low-quality stimuli unable to explore complex behaviors. These limitations result in slow coverage convergence and prohibitively high verification costs. In this paper, we present Lyra, a heterogeneous RISC-V verification framework that addresses both challenges by pairing hardware-accelerated verification with an ISA-aware generative model. Lyra executes the DUT and reference model concurrently on an FPGA SoC, enabling high-throughput differential checking and hardware-level coverage collection. Instead of creating verification stimuli randomly or through simple mutations, we train a domain-specialized generative model, LyraGen, with inherent semantic awareness to generate high-quality, semantically rich instruction sequences. Empirical results show Lyra achieves up to $1.27\times$ higher coverage and accelerates end-to-end verification by up to $107\times$ to $3343\times$ compared to state-of-the-art software fuzzers, while consistently demonstrating lower convergence difficulty.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Lyra: A Hardware-Accelerated RISC-V Verification Framework with Generative Model-Based Processor Fuzzing》，初步归入“RISC-V Processor Fuzzing”。

## 与本仓库研究主线的关系

该条目已通过自动相关性筛选，但尚未完成人工或全文级核验。

## 结论

尚未核验正文，因此不对论文最终结论作确定性概括。

## 局限性

尚未核验正文。至少需要检查方法是否只适用于特定 ISA、处理器、协议、仿真器或人工模板，以及实验是否存在目标泄漏和基线不公平。

## 详细阅读分析

优先阅读 Introduction、Background/Threat Model、Method、Evaluation、Limitations/Discussion，并核对官方论文页、DOI、Artifact 和代码仓库。

## 后续核验问题

- 论文的在线反馈信号和最终 Oracle 分别是什么？
- 实验是否包含公平的 random、通用 RTL coverage 和领域专用 coverage 基线？
- 论文是否提供开源 Artifact、真实漏洞、CVE 或可复现 PoC？
