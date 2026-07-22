# Shesha: Multi-head Microarchitectural Leakage Discovery in new-generation Intel Processors

## 基本信息

- 作者：Anirban Chakraborty、Nimish Mishra、Debdeep Mukhopadhyay
- 发表日期：2024-06-10
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, microarchitectural；verification/fuzzing method: fuzz；security relevance: side channel, transient execution, leakage
- 论文页面：[http://arxiv.org/abs/2406.06034v2](http://arxiv.org/abs/2406.06034v2)
- PDF：[https://arxiv.org/pdf/2406.06034v2](https://arxiv.org/pdf/2406.06034v2)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Transient execution attacks have been one of the widely explored microarchitectural side channels since the discovery of Spectre and Meltdown. However, much of the research has been driven by manual discovery of new transient paths through well-known speculative events. Although a few attempts exist in literature on automating transient leakage discovery, such tools focus on finding variants of known transient attacks and explore a small subset of instruction set. Further, they take a random fuzzing approach that does not scale as the complexity of search space increases. In this work, we identify that the search space of bad speculation is disjointedly fragmented into equivalence classes, and then use this observation to develop a framework named Shesha, inspired by Particle Swarm Optimization, which exhibits faster convergence rates than state-of-the-art fuzzing techniques for automatic discovery of transient execution attacks. We then use Shesha to explore the vast search space of extensions to the x86 Instruction Set Architecture (ISAs), thereby focusing on previously unexplored avenues of bad speculation. As such, we report five previously unreported transient execution paths in Instruction Set Extensions (ISEs) on new generation of Intel processors. We then perform extensive reverse engineering of each of the transient execution paths and provide root-cause analysis. Using the discovered transient execution paths, we develop attack building blocks to exhibit exploitable transient windows. Finally, we demonstrate data leakage from Fused Multiply-Add instructions through SIMD buffer and extract victim data from various cryptographic implementations.

## 研究问题

摘要级初步判断（未核验正文）：Transient execution attacks have been one of the widely explored microarchitectural side channels since the discovery of Spectre and Meltdown. However, much of the research has been driven by manual discovery of new transient paths through well-known speculative events. Although a few attempts exist in literature on automating transient leakage discovery, such tools focus on finding variants of known transient attacks and explore a small subset of instruction set. Further, they take a random fuzzing approach that does not scale as the complexity of search space increases. In this work, we identify that the search space of bad speculation is disjointedly fragmented into equivalence classes, and then use this observation to develop a framework named Shesha, inspired by Particle Swarm Optimization, which exhibits faster convergence rates than state-of-the-art fuzzing techniques for automatic discovery of transient execution attacks. We then use Shesha to explore the vast search space of extensions to the x86 Instruction Set Architecture (ISAs), thereby focusing on previously unexplored avenues of bad speculation. As such, we report five previously unreported transient execution paths in Instruction Set Extensions (ISEs) on new generation of Intel processors. We then perform extensive reverse engineering of each of the transient execution paths and provide root-cause analysis. Using the discovered transient execution paths, we develop attack building blocks to exhibit exploitable transient windows. Finally, we demonstrate data leakage from Fused Multiply-Add instructions through SIMD buffer and extract victim data from various cryptographic implementations.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Shesha: Multi-head Microarchitectural Leakage Discovery in new-generation Intel Processors》，初步归入“Microarchitectural Security Testing”。

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
