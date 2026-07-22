# HybriDIFT: Scalable Memory-Aware Dynamic Information Flow Tracking for Hardware

## 基本信息

- 作者：Flavien Solt、Kaveh Razavi
- 发表日期：2024-10-27
- 会议/期刊：未记录
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: processor, rtl；verification/fuzzing method: information flow tracking；security relevance: leakage
- 论文页面：[https://doi.org/10.1145/3676536.3676658](https://doi.org/10.1145/3676536.3676658)
- PDF：[https://dl.acm.org/doi/pdf/10.1145/3676536.3676658](https://dl.acm.org/doi/pdf/10.1145/3676536.3676658)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Designing correct and secure hardware is challenging. Dynamic information flow tracking (DIFT) enhances RTL testing flows, for example, by providing formal guarantees on detecting information leakage. However, existing DIFT solutions do not scale to large memories encountered in complex processors. A formal analysis of existing DIFT mechanisms reveals the two factors that fundamentally limit the scalability of instrumenting memories: existing mechanisms enforce that all memory words must be accessible simultaneously, and dependent reads and writes must happen concurrently. These aspects that are detrimental to scalability are all due to precise tracking of implicit flows for every memory word, which is not required in many scenarios of interest. Based on this insight, we design HybriDIFT, a module-level DIFT memory instrumentation based on SRAM deduplication and on a single state bit that tracks implicit information flows. HybriDIFT can automatically identify memories and their protocols by combining static and dynamic analysis. HybriDIFT is precise in practice and scalable to RTL designs that feature large memories. We evaluate HybriDIFT by automatically instrumenting a set of open-source hardware designs. With Verilator, HybriDIFT accelerates build time by 1.06× to 3.5× and simulation by 2.6× to 5.1× on default target configurations, and instruments a larger OpenC910 configuration that was out of reach for the state-of-the-art DIFT mechanisms, while preserving sufficient precision for all known applications.

## 研究问题

摘要级初步判断（未核验正文）：Designing correct and secure hardware is challenging. Dynamic information flow tracking (DIFT) enhances RTL testing flows, for example, by providing formal guarantees on detecting information leakage. However, existing DIFT solutions do not scale to large memories encountered in complex processors. A formal analysis of existing DIFT mechanisms reveals the two factors that fundamentally limit the scalability of instrumenting memories: existing mechanisms enforce that all memory words must be accessible simultaneously, and dependent reads and writes must happen concurrently. These aspects that are detrimental to scalability are all due to precise tracking of implicit flows for every memory word, which is not required in many scenarios of interest. Based on this insight, we design HybriDIFT, a module-level DIFT memory instrumentation based on SRAM deduplication and on a single state bit that tracks implicit information flows. HybriDIFT can automatically identify memories and their protocols by combining static and dynamic analysis. HybriDIFT is precise in practice and scalable to RTL designs that feature large memories. We evaluate HybriDIFT by automatically instrumenting a set of open-source hardware designs. With Verilator, HybriDIFT accelerates build time by 1.06× to 3.5× and simulation by 2.6× to 5.1× on default target configurations, and instruments a larger OpenC910 configuration that was out of reach for the state-of-the-art DIFT mechanisms, while preserving sufficient precision for all known applications.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《HybriDIFT: Scalable Memory-Aware Dynamic Information Flow Tracking for Hardware》，初步归入“Coverage, Oracles & Fuzzing Methodology”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
