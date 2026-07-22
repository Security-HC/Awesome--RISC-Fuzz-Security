# Microarchitectural Leakage Templates and Their Application to Cache-Based Side Channels

## 基本信息

- 作者：Ahmad Ibrahim、Hamed Nemati、Till Schlüter、Nils Ole Tippenhauer、Christian Rossow
- 发表日期：2022-11-25
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, cpu, microarchitectural；verification/fuzzing method: fuzz；security relevance: vulnerability, side channel, leakage
- 论文页面：[http://arxiv.org/abs/2211.13958v1](http://arxiv.org/abs/2211.13958v1)
- PDF：[https://arxiv.org/pdf/2211.13958v1](https://arxiv.org/pdf/2211.13958v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

The complexity of modern processor architectures has given rise to sophisticated interactions among their components. Such interactions may result in potential attack vectors in terms of side channels, possibly available to user-land exploits to leak secret data. Exploitation and countering of such side channels require a detailed understanding of the target component. However, such detailed information is commonly unpublished for many CPUs. In this paper, we introduce the concept of Leakage Templates to abstractly describe specific side channels and identify their occurrences in binary applications. We design and implement Plumber, a framework to derive the generic Leakage Templates from individual code sequences that are known to cause leakage (e.g., found by prior work). Plumber uses a combination of instruction fuzzing, instructions' operand mutation and statistical analysis to explore undocumented behavior of microarchitectural optimizations and derive sufficient conditions on vulnerable code inputs that, if hold can trigger a distinguishing behavior. Using Plumber we identified novel leakage primitives based on Leakage Templates (for ARM Cortex-A53 and -A72 cores), in particular related to previction (a new premature cache eviction), and prefetching behavior. We show the utility of Leakage Templates by re-identifying a prefetcher-based vulnerability in OpenSSL 1.1.0g first reported by Shin et al. [40].

## 研究问题

摘要级初步判断（未核验正文）：The complexity of modern processor architectures has given rise to sophisticated interactions among their components. Such interactions may result in potential attack vectors in terms of side channels, possibly available to user-land exploits to leak secret data. Exploitation and countering of such side channels require a detailed understanding of the target component. However, such detailed information is commonly unpublished for many CPUs. In this paper, we introduce the concept of Leakage Templates to abstractly describe specific side channels and identify their occurrences in binary applications. We design and implement Plumber, a framework to derive the generic Leakage Templates from individual code sequences that are known to cause leakage (e.g., found by prior work). Plumber uses a combination of instruction fuzzing, instructions' operand mutation and statistical analysis to explore undocumented behavior of microarchitectural optimizations and derive sufficient conditions on vulnerable code inputs that, if hold can trigger a distinguishing behavior. Using Plumber we identified novel leakage primitives based on Leakage Templates (for ARM Cortex-A53 and -A72 cores), in particular related to previction (a new premature cache eviction), and prefetching behavior. We show the utility of Leakage Templates by re-identifying a prefetcher-based vulnerability in OpenSSL 1.1.0g first reported by Shin et al. [40].

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Microarchitectural Leakage Templates and Their Application to Cache-Based Side Channels》，初步归入“Microarchitectural Security Testing”。

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
