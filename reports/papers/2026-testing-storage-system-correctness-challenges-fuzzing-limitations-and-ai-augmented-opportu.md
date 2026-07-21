# Testing Storage-System Correctness: Challenges, Fuzzing Limitations, and AI-Augmented Opportunities

## 基本信息

- 作者：Ying Wang、Jiahui Chen、Dejun Jiang
- 发表日期：2026-02-02
- 更新日期：2026-02-06
- 来源：arXiv
- 来源编号：2602.02614v2
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2602.02614v2](http://arxiv.org/abs/2602.02614v2)
- PDF：[https://arxiv.org/pdf/2602.02614v2](https://arxiv.org/pdf/2602.02614v2)
- 分析模式：仅元数据分析

## 摘要

Storage systems are fundamental to modern computing infrastructures, yet ensuring their correctness remains challenging in practice. Despite decades of research on system testing, many storage-system failures (including durability, ordering, recovery, and consistency violations) remain difficult to expose systematically. This difficulty stems not primarily from insufficient testing tooling, but from intrinsic properties of storage-system execution, including nondeterministic interleavings, long-horizon state evolution, and correctness semantics that span multiple layers and execution phases. This survey adopts a storage-centric view of system testing and organizes existing techniques according to the execution properties and failure mechanisms they target. We review a broad spectrum of approaches, ranging from concurrency testing and long-running workloads to crash-consistency analysis, hardware-level semantic validation, and distributed fault injection, and analyze their fundamental strengths and limitations. Within this framework, we examine fuzzing as an automated testing paradigm, highlighting systematic mismatches between conventional fuzzing assumptions and storage-system semantics, and discuss how recent artificial intelligence advances may complement fuzzing through state-aware and semantic guidance. Overall, this survey provides a unified perspective on storage-system correctness testing and outlines key challenges

## 研究问题

Storage systems are fundamental to modern computing infrastructures, yet ensuring their correctness remains challenging in practice. Despite decades of research on system testing, many storage-system failures (including durability, ordering, recovery, and consistency violations) remain difficult to expose systematically. This difficulty stems not primarily from insufficient testing tooling, but from intrinsic properties of storage-system execution, including nondeterministic interleavings, long-horizon state evolution, and correctness semantics that span multiple layers and execution phases. This survey adopts a storage-centric view of system testing and organizes existing techniques according to the execution properties and failure mechanisms they target. We review a broad spectrum of approaches, ranging from concurrency testing and long-running workloads to crash-consistency analysis, hardware-level semantic validation, and distributed fault injection, and analyze their fundamental strengths and limitations. Within this framework, we examine fuzzing as an automated testing paradigm, highlighting systematic mismatches between conventional fuzzing assumptions and storage-system semantics, and discuss how recent artificial intelligence advances may complement fuzzing through state-aware and semantic guidance. Overall, this survey provides a unified perspective on storage-system correctness testing and outlines key challenges

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
