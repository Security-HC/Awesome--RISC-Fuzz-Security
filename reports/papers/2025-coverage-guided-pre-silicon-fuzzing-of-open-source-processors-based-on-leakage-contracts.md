# Coverage-Guided Pre-Silicon Fuzzing of Open-Source Processors based on Leakage Contracts

## 基本信息

- 作者：Gideon Geier、Pariya Hajipour、Jan Reineke
- 发表日期：2025-11-11
- 更新日期：2025-11-16
- 来源：arXiv
- 来源编号：2511.08443v2
- 研究类别：RISC-V Fuzzing、Microarchitecture Security、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[http://arxiv.org/abs/2511.08443v2](http://arxiv.org/abs/2511.08443v2)
- PDF：[https://arxiv.org/pdf/2511.08443v2](https://arxiv.org/pdf/2511.08443v2)
- 分析模式：仅元数据分析

## 摘要

Hardware-software leakage contracts have emerged as a formalism for specifying side-channel security guarantees of modern processors, yet verifying that a complex hardware design complies with its contract remains a major challenge. While verification provides strong guarantees, current verification approaches struggle to scale to industrial-sized designs. Conversely, prevalent hardware fuzzing approaches are designed to find functional correctness bugs, but are blind to information leaks like Spectre. To bridge this gap, we introduce a novel and scalable approach: coverage-guided hardware-software contract fuzzing. Our methodology leverages a self-compositional framework to make information leakage directly observable as microarchitectural state divergence. The core of our contribution is a new, security-oriented coverage metric, Self-Composition Deviation (SCD), which guides the fuzzer to explore execution paths that violate the leakage contract. We implemented this approach and performed an extensive evaluation on two open-source RISC-V cores: the in-order Rocket Core and the complex out-of-order BOOM core. Our results demonstrate that coverage-guided strategies outperform unguided fuzzing and that increased microarchitectural coverage leads to a faster discovery of security vulnerabilities in the BOOM core.

## 研究问题

Hardware-software leakage contracts have emerged as a formalism for specifying side-channel security guarantees of modern processors, yet verifying that a complex hardware design complies with its contract remains a major challenge. While verification provides strong guarantees, current verification approaches struggle to scale to industrial-sized designs. Conversely, prevalent hardware fuzzing approaches are designed to find functional correctness bugs, but are blind to information leaks like Spectre. To bridge this gap, we introduce a novel and scalable approach: coverage-guided hardware-software contract fuzzing. Our methodology leverages a self-compositional framework to make information leakage directly observable as microarchitectural state divergence. The core of our contribution is a new, security-oriented coverage metric, Self-Composition Deviation (SCD), which guides the fuzzer to explore execution paths that violate the leakage contract. We implemented this approach and performed an extensive evaluation on two open-source RISC-V cores: the in-order Rocket Core and the complex out-of-order BOOM core. Our results demonstrate that coverage-guided strategies outperform unguided fuzzing and that increased microarchitectural coverage leads to a faster discovery of security vulnerabilities in the BOOM core.

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
