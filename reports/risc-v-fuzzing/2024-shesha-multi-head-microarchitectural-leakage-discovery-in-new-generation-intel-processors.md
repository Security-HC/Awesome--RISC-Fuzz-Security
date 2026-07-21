# Shesha: Multi-head Microarchitectural Leakage Discovery in new-generation Intel Processors

## 基本信息

- 作者：Anirban Chakraborty、Nimish Mishra、Debdeep Mukhopadhyay
- 发表日期：2024-06-10
- 更新日期：2024-06-14
- 来源：arXiv
- 来源编号：2406.06034v2
- 研究类别：RISC-V Fuzzing 研究、微架构安全、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[http://arxiv.org/abs/2406.06034v2](http://arxiv.org/abs/2406.06034v2)
- PDF：[https://arxiv.org/pdf/2406.06034v2](https://arxiv.org/pdf/2406.06034v2)
- 分析模式：仅元数据分析

## 摘要

Transient execution attacks have been one of the widely explored microarchitectural side channels since the discovery of Spectre and Meltdown. However, much of the research has been driven by manual discovery of new transient paths through well-known speculative events. Although a few attempts exist in literature on automating transient leakage discovery, such tools focus on finding variants of known transient attacks and explore a small subset of instruction set. Further, they take a random fuzzing approach that does not scale as the complexity of search space increases. In this work, we identify that the search space of bad speculation is disjointedly fragmented into equivalence classes, and then use this observation to develop a framework named Shesha, inspired by Particle Swarm Optimization, which exhibits faster convergence rates than state-of-the-art fuzzing techniques for automatic discovery of transient execution attacks. We then use Shesha to explore the vast search space of extensions to the x86 Instruction Set Architecture (ISAs), thereby focusing on previously unexplored avenues of bad speculation. As such, we report five previously unreported transient execution paths in Instruction Set Extensions (ISEs) on new generation of Intel processors. We then perform extensive reverse engineering of each of the transient execution paths and provide root-cause analysis. Using the discovered transient execution paths, we develop attack building blocks to exhibit exploitable transient windows. Finally, we demonstrate data leakage from Fused Multiply-Add instructions through SIMD buffer and extract victim data from various cryptographic implementations.

## 研究问题

Transient execution attacks have been one of the widely explored microarchitectural side channels since the discovery of Spectre and Meltdown. However, much of the research has been driven by manual discovery of new transient paths through well-known speculative events. Although a few attempts exist in literature on automating transient leakage discovery, such tools focus on finding variants of known transient attacks and explore a small subset of instruction set. Further, they take a random fuzzing approach that does not scale as the complexity of search space increases. In this work, we identify that the search space of bad speculation is disjointedly fragmented into equivalence classes, and then use this observation to develop a framework named Shesha, inspired by Particle Swarm Optimization, which exhibits faster convergence rates than state-of-the-art fuzzing techniques for automatic discovery of transient execution attacks. We then use Shesha to explore the vast search space of extensions to the x86 Instruction Set Architecture (ISAs), thereby focusing on previously unexplored avenues of bad speculation. As such, we report five previously unreported transient execution paths in Instruction Set Extensions (ISEs) on new generation of Intel processors. We then perform extensive reverse engineering of each of the transient execution paths and provide root-cause analysis. Using the discovered transient execution paths, we develop attack building blocks to exhibit exploitable transient windows. Finally, we demonstrate data leakage from Fused Multiply-Add instructions through SIMD buffer and extract victim data from various cryptographic implementations.

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
