# Intelligent Graybox Fuzzing via ATPG-Guided Seed Generation and Submodule Analysis

## 基本信息

- 作者：Raghul Saravanan、Sudipta Paria、Aritra Dasgupta、Swarup Bhunia、Sai Manoj P D
- 发表日期：2025-09-25
- 更新日期：2026-01-26
- 来源：arXiv
- 来源编号：2509.20808v2
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2509.20808v2](http://arxiv.org/abs/2509.20808v2)
- PDF：[https://arxiv.org/pdf/2509.20808v2](https://arxiv.org/pdf/2509.20808v2)
- 分析模式：仅元数据分析

## 摘要

Hardware Fuzzing emerged as one of the crucial techniques for finding security flaws in modern hardware designs by testing a wide range of input scenarios. One of the main challenges is creating high-quality input seeds that maximize coverage and speed up verification. Coverage-Guided Fuzzing (CGF) methods help explore designs more effectively, but they struggle to focus on specific parts of the hardware. Existing Directed Gray-box Fuzzing (DGF) techniques like DirectFuzz try to solve this by generating targeted tests, but it has major drawbacks, such as supporting only limited hardware description languages, not scaling well to large circuits, and having issues with abstraction mismatches. To address these problems, we introduce a novel framework, PROFUZZ, that follows the DGF approach and combines fuzzing with Automatic Test Pattern Generation (ATPG) for more efficient fuzzing. By leveraging ATPG's structural analysis capabilities, PROFUZZ can generate precise input seeds that target specific design regions more effectively while maintaining high fuzzing throughput. Our experiments show that PROFUZZ scales 30x better than DirectFuzz when handling multiple target sites, improves coverage by 11.66%, and runs 2.76x faster, highlighting its scalability and effectiveness for directed fuzzing in complex hardware systems.

## 研究问题

Hardware Fuzzing emerged as one of the crucial techniques for finding security flaws in modern hardware designs by testing a wide range of input scenarios. One of the main challenges is creating high-quality input seeds that maximize coverage and speed up verification. Coverage-Guided Fuzzing (CGF) methods help explore designs more effectively, but they struggle to focus on specific parts of the hardware. Existing Directed Gray-box Fuzzing (DGF) techniques like DirectFuzz try to solve this by generating targeted tests, but it has major drawbacks, such as supporting only limited hardware description languages, not scaling well to large circuits, and having issues with abstraction mismatches. To address these problems, we introduce a novel framework, PROFUZZ, that follows the DGF approach and combines fuzzing with Automatic Test Pattern Generation (ATPG) for more efficient fuzzing. By leveraging ATPG's structural analysis capabilities, PROFUZZ can generate precise input seeds that target specific design regions more effectively while maintaining high fuzzing throughput. Our experiments show that PROFUZZ scales 30x better than DirectFuzz when handling multiple target sites, improves coverage by 11.66%, and runs 2.76x faster, highlighting its scalability and effectiveness for directed fuzzing in complex hardware systems.

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
