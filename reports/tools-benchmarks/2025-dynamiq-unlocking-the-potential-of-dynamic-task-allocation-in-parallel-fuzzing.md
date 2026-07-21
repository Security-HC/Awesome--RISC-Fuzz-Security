# DynamiQ: Unlocking the Potential of Dynamic Task Allocation in Parallel Fuzzing

## 基本信息

- 作者：Wenqi Yan、Toby Murray、Benjamin I. P. Rubinstein、Van-Thuan Pham
- 发表日期：2025-10-06
- 更新日期：2025-10-07
- 来源：arXiv
- 来源编号：2510.04469v2
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2510.04469v2](http://arxiv.org/abs/2510.04469v2)
- PDF：[https://arxiv.org/pdf/2510.04469v2](https://arxiv.org/pdf/2510.04469v2)
- 分析模式：仅元数据分析

## 摘要

We present DynamiQ, a full-fledged and optimized successor to AFLTeam that supports dynamic and adaptive parallel fuzzing. Unlike most existing approaches that treat individual seeds as tasks, DynamiQ leverages structural information from the program's call graph to define tasks and continuously refines task allocation using runtime feedback. This design significantly reduces redundant exploration and enhances fuzzing efficiency at scale. Built on top of the state-of-the-art LibAFL framework, DynamiQ incorporates several practical optimizations in both task allocation and task-aware fuzzing. Evaluated on 12 real-world targets from OSS-Fuzz and FuzzBench over 25,000 CPU hours, DynamiQ outperforms state-of-the-art parallel fuzzers in both code coverage and vulnerability discovery, uncovering 9 previously unknown bugs in widely used and extensively fuzzed open-source software.

## 研究问题

We present DynamiQ, a full-fledged and optimized successor to AFLTeam that supports dynamic and adaptive parallel fuzzing. Unlike most existing approaches that treat individual seeds as tasks, DynamiQ leverages structural information from the program's call graph to define tasks and continuously refines task allocation using runtime feedback. This design significantly reduces redundant exploration and enhances fuzzing efficiency at scale. Built on top of the state-of-the-art LibAFL framework, DynamiQ incorporates several practical optimizations in both task allocation and task-aware fuzzing. Evaluated on 12 real-world targets from OSS-Fuzz and FuzzBench over 25,000 CPU hours, DynamiQ outperforms state-of-the-art parallel fuzzers in both code coverage and vulnerability discovery, uncovering 9 previously unknown bugs in widely used and extensively fuzzed open-source software.

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
