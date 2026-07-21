# ConnChecker: Automated Root-Cause Analysis for Formal Connectivity Check via Graph

## 基本信息

- 作者：Do Ngoc Tiep、Nguyen Linh Anh、Luu Danh Minh
- 发表日期：2026-03-09
- 更新日期：2026-03-09
- 来源：arXiv
- 来源编号：2603.07943v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2603.07943v1](http://arxiv.org/abs/2603.07943v1)
- PDF：[https://arxiv.org/pdf/2603.07943v1](https://arxiv.org/pdf/2603.07943v1)
- 分析模式：仅元数据分析

## 摘要

Formal connectivity checking offers scalable verification of signal paths in complex SoC designs, but debugging counterexamples remains a manual and time-consuming process. ConnChecker introduces a new graph-based perspective for automating root-cause analysis by integrating formal tool outputs such as structural/functional dependency graphs and counterexamples report. It begins with automatic failure categorization, routing each counterexample to one of three targeted analysis flows. These flows localize failure points and suggest corrective actions or hints for manual inspection. Evaluated on two industrial SoCs, ConnChecker achieved up to 80\% reduction in debugging time, especially for complex cases, demonstrating its scalability and effectiveness across diverse connectivity scenarios.

## 研究问题

Formal connectivity checking offers scalable verification of signal paths in complex SoC designs, but debugging counterexamples remains a manual and time-consuming process. ConnChecker introduces a new graph-based perspective for automating root-cause analysis by integrating formal tool outputs such as structural/functional dependency graphs and counterexamples report. It begins with automatic failure categorization, routing each counterexample to one of three targeted analysis flows. These flows localize failure points and suggest corrective actions or hints for manual inspection. Evaluated on two industrial SoCs, ConnChecker achieved up to 80\% reduction in debugging time, especially for complex cases, demonstrating its scalability and effectiveness across diverse connectivity scenarios.

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
