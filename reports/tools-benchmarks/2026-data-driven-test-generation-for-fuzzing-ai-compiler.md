# Data-driven Test Generation for Fuzzing AI Compiler

## 基本信息

- 作者：Qingchao Shen
- 发表日期：2026-01-24
- 更新日期：2026-01-24
- 来源：arXiv
- 来源编号：2601.17450v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2601.17450v1](http://arxiv.org/abs/2601.17450v1)
- PDF：[https://arxiv.org/pdf/2601.17450v1](https://arxiv.org/pdf/2601.17450v1)
- 分析模式：仅元数据分析

## 摘要

Artificial Intelligence (AI) compilers are critical for efficiently deploying AI models across diverse hardware platforms. However, they remain prone to bugs that can compromise both compiler reliability and model correctness. Thus, ensuring the quality of AI compilers is crucial. In this work, we present a unified data-driven testing framework that systematically addresses stage-specific challenges in AI compilers. Specifically, OPERA migrates tests for AI libraries to test various operator conversion logic in the model loading stage. OATest synthesizes diverse optimization-aware computational graphs for testing high-level optimizations. HARMONY generates and mutates diverse low-level IR seeds to generate hardware-optimization-aware tests for testing low-level optimizations. Together, these techniques provide a comprehensive, stage-aware framework that enhances testing coverage and effectiveness, detecting 266 previously unknown bugs in four widely used AI compilers.

## 研究问题

Artificial Intelligence (AI) compilers are critical for efficiently deploying AI models across diverse hardware platforms. However, they remain prone to bugs that can compromise both compiler reliability and model correctness. Thus, ensuring the quality of AI compilers is crucial. In this work, we present a unified data-driven testing framework that systematically addresses stage-specific challenges in AI compilers. Specifically, OPERA migrates tests for AI libraries to test various operator conversion logic in the model loading stage. OATest synthesizes diverse optimization-aware computational graphs for testing high-level optimizations. HARMONY generates and mutates diverse low-level IR seeds to generate hardware-optimization-aware tests for testing low-level optimizations. Together, these techniques provide a comprehensive, stage-aware framework that enhances testing coverage and effectiveness, detecting 266 previously unknown bugs in four widely used AI compilers.

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
