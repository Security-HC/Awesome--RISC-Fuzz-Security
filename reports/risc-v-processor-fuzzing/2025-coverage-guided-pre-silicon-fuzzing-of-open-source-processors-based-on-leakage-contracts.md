# Coverage-Guided Pre-Silicon Fuzzing of Open-Source Processors based on Leakage Contracts

## 基本信息

- 作者：Gideon Geier、Pariya Hajipour、Jan Reineke
- 发表日期：2025-11-11
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=8）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、Microarchitectural Security Testing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: risc-v, processor, microarchitectural；verification/fuzzing method: fuzz, coverage-guided, verification；security relevance: security, leakage
- 论文页面：[http://arxiv.org/abs/2511.08443v2](http://arxiv.org/abs/2511.08443v2)
- PDF：[https://arxiv.org/pdf/2511.08443v2](https://arxiv.org/pdf/2511.08443v2)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Hardware-software leakage contracts have emerged as a formalism for specifying side-channel security guarantees of modern processors, yet verifying that a complex hardware design complies with its contract remains a major challenge. While verification provides strong guarantees, current verification approaches struggle to scale to industrial-sized designs. Conversely, prevalent hardware fuzzing approaches are designed to find functional correctness bugs, but are blind to information leaks like Spectre. To bridge this gap, we introduce a novel and scalable approach: coverage-guided hardware-software contract fuzzing. Our methodology leverages a self-compositional framework to make information leakage directly observable as microarchitectural state divergence. The core of our contribution is a new, security-oriented coverage metric, Self-Composition Deviation (SCD), which guides the fuzzer to explore execution paths that violate the leakage contract. We implemented this approach and performed an extensive evaluation on two open-source RISC-V cores: the in-order Rocket Core and the complex out-of-order BOOM core. Our results demonstrate that coverage-guided strategies outperform unguided fuzzing and that increased microarchitectural coverage leads to a faster discovery of security vulnerabilities in the BOOM core.

## 研究问题

摘要级初步判断（未核验正文）：Hardware-software leakage contracts have emerged as a formalism for specifying side-channel security guarantees of modern processors, yet verifying that a complex hardware design complies with its contract remains a major challenge. While verification provides strong guarantees, current verification approaches struggle to scale to industrial-sized designs. Conversely, prevalent hardware fuzzing approaches are designed to find functional correctness bugs, but are blind to information leaks like Spectre. To bridge this gap, we introduce a novel and scalable approach: coverage-guided hardware-software contract fuzzing. Our methodology leverages a self-compositional framework to make information leakage directly observable as microarchitectural state divergence. The core of our contribution is a new, security-oriented coverage metric, Self-Composition Deviation (SCD), which guides the fuzzer to explore execution paths that violate the leakage contract. We implemented this approach and performed an extensive evaluation on two open-source RISC-V cores: the in-order Rocket Core and the complex out-of-order BOOM core. Our results demonstrate that coverage-guided strategies outperform unguided fuzzing and that increased microarchitectural coverage leads to a faster discovery of security vulnerabilities in the BOOM core.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Coverage-Guided Pre-Silicon Fuzzing of Open-Source Processors based on Leakage Contracts》，初步归入“RISC-V Processor Fuzzing”。

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
