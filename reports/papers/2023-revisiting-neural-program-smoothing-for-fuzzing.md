# Revisiting Neural Program Smoothing for Fuzzing

## 基本信息

- 作者：Maria-Irina Nicolae、Max Eisele、Andreas Zeller
- 发表日期：2023-09-28
- 更新日期：2023-09-28
- 来源：arXiv
- 来源编号：2309.16618v1
- 研究类别：Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2309.16618v1](http://arxiv.org/abs/2309.16618v1)
- PDF：[https://arxiv.org/pdf/2309.16618v1](https://arxiv.org/pdf/2309.16618v1)
- 分析模式：仅元数据分析

## 摘要

Testing with randomly generated inputs (fuzzing) has gained significant traction due to its capacity to expose program vulnerabilities automatically. Fuzz testing campaigns generate large amounts of data, making them ideal for the application of machine learning (ML). Neural program smoothing (NPS), a specific family of ML-guided fuzzers, aims to use a neural network as a smooth approximation of the program target for new test case generation. In this paper, we conduct the most extensive evaluation of NPS fuzzers against standard gray-box fuzzers (>11 CPU years and >5.5 GPU years), and make the following contributions: (1) We find that the original performance claims for NPS fuzzers do not hold; a gap we relate to fundamental, implementation, and experimental limitations of prior works. (2) We contribute the first in-depth analysis of the contribution of machine learning and gradient-based mutations in NPS. (3) We implement Neuzz++, which shows that addressing the practical limitations of NPS fuzzers improves performance, but that standard gray-box fuzzers almost always surpass NPS-based fuzzers. (4) As a consequence, we propose new guidelines targeted at benchmarking fuzzing based on machine learning, and present MLFuzz, a platform with GPU access for easy and reproducible evaluation of ML-based fuzzers. Neuzz++, MLFuzz, and all our data are public.

## 研究问题

Testing with randomly generated inputs (fuzzing) has gained significant traction due to its capacity to expose program vulnerabilities automatically. Fuzz testing campaigns generate large amounts of data, making them ideal for the application of machine learning (ML). Neural program smoothing (NPS), a specific family of ML-guided fuzzers, aims to use a neural network as a smooth approximation of the program target for new test case generation. In this paper, we conduct the most extensive evaluation of NPS fuzzers against standard gray-box fuzzers (>11 CPU years and >5.5 GPU years), and make the following contributions: (1) We find that the original performance claims for NPS fuzzers do not hold; a gap we relate to fundamental, implementation, and experimental limitations of prior works. (2) We contribute the first in-depth analysis of the contribution of machine learning and gradient-based mutations in NPS. (3) We implement Neuzz++, which shows that addressing the practical limitations of NPS fuzzers improves performance, but that standard gray-box fuzzers almost always surpass NPS-based fuzzers. (4) As a consequence, we propose new guidelines targeted at benchmarking fuzzing based on machine learning, and present MLFuzz, a platform with GPU access for easy and reproducible evaluation of ML-based fuzzers. Neuzz++, MLFuzz, and all our data are public.

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
