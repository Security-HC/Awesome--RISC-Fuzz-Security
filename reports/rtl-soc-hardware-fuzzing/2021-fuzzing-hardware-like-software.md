# Fuzzing Hardware Like Software

## 基本信息

- 作者：Timothy Trippel、Kang G. Shin、Alex Chernyakhovsky、Garret Kelly、Dominic Rizzo、Matthew Hicks
- 发表日期：2021-02-03
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：B·强邻近（score=90）
- 证据等级：摘要级
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：manual adjacent seed title
- 论文页面：[http://arxiv.org/abs/2102.02308v1](http://arxiv.org/abs/2102.02308v1)
- PDF：[https://arxiv.org/pdf/2102.02308v1](https://arxiv.org/pdf/2102.02308v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Hardware flaws are permanent and potent: hardware cannot be patched once fabricated, and any flaws may undermine any software executing on top. Consequently, verification time dominates implementation time. The gold standard in hardware Design Verification (DV) is concentrated at two extremes: random dynamic verification and formal verification. Both struggle to root out the subtle flaws in complex hardware that often manifest as security vulnerabilities. The root problem with random verification is its undirected nature, making it inefficient, while formal verification is constrained by the state-space explosion problem, making it infeasible against complex designs. What is needed is a solution that is directed, yet under-constrained. Instead of making incremental improvements to existing DV approaches, we leverage the observation that existing software fuzzers already provide such a solution, and adapt them for hardware DV. Specifically, we translate RTL hardware to a software model and fuzz that model. The central challenge we address is how best to mitigate the differences between the hardware execution model and software execution model. This includes: 1) how to represent test cases, 2) what is the hardware equivalent of a crash, 3) what is an appropriate coverage metric, and 4) how to create a general-purpose fuzzing harness for hardware. To evaluate our approach, we fuzz four IP blocks from Google's OpenTitan SoC. Our experiments reveal a two orders-of-magnitude reduction in run time to achieve Finite State Machine (FSM) coverage over traditional dynamic verification schemes. Moreover, with our design-agnostic harness, we achieve over 88% HDL line coverage in three out of four of our designs -- even without any initial seeds.

## 研究问题

摘要级初步判断（未核验正文）：Hardware flaws are permanent and potent: hardware cannot be patched once fabricated, and any flaws may undermine any software executing on top. Consequently, verification time dominates implementation time. The gold standard in hardware Design Verification (DV) is concentrated at two extremes: random dynamic verification and formal verification. Both struggle to root out the subtle flaws in complex hardware that often manifest as security vulnerabilities. The root problem with random verification is its undirected nature, making it inefficient, while formal verification is constrained by the state-space explosion problem, making it infeasible against complex designs. What is needed is a solution that is directed, yet under-constrained. Instead of making incremental improvements to existing DV approaches, we leverage the observation that existing software fuzzers already provide such a solution, and adapt them for hardware DV. Specifically, we translate RTL hardware to a software model and fuzz that model. The central challenge we address is how best to mitigate the differences between the hardware execution model and software execution model. This includes: 1) how to represent test cases, 2) what is the hardware equivalent of a crash, 3) what is an appropriate coverage metric, and 4) how to create a general-purpose fuzzing harness for hardware. To evaluate our approach, we fuzz four IP blocks from Google's OpenTitan SoC. Our experiments reveal a two orders-of-magnitude reduction in run time to achieve Finite State Machine (FSM) coverage over traditional dynamic verification schemes. Moreover, with our design-agnostic harness, we achieve over 88% HDL line coverage in three out of four of our designs -- even without any initial seeds.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Fuzzing Hardware Like Software》，初步归入“RTL & SoC Hardware Fuzzing”。

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
