# ATLAS: AI-Assisted Threat-to-Assertion Learning for System-on-Chip Security Verification

## 基本信息

- 作者：Ishraq Tashdid、Kimia Tasnia、Alexander Garcia、Jonathan Valamehr、Sazadur Rahman
- 发表日期：2026-03-01
- 更新日期：2026-04-23
- 来源：arXiv
- 来源编号：2603.01170v2
- 研究类别：RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2603.01170v2](http://arxiv.org/abs/2603.01170v2)
- PDF：[https://arxiv.org/pdf/2603.01170v2](https://arxiv.org/pdf/2603.01170v2)
- 分析模式：仅元数据分析

## 摘要

This work presents ATLAS, an LLM-driven framework that bridges standardized threat modeling and property-based formal verification for System-on-Chip (SoC) security. Starting from vulnerability knowledge bases such as Common Weakness Enumeration (CWE), ATLAS identifies SoC-specific assets, maps relevant weaknesses, and generates assertion-based security properties and JasperGold scripts for verification. By combining asset-centric analysis with standardized threat model templates and multi-source SoC context, ATLAS automates the transformation from vulnerability reasoning to formal proof. Evaluated on three HACK@DAC benchmarks, ATLAS detected 39/48 CWEs and generated correct properties for 33 of those bugs, advancing automated, knowledge-driven SoC security verification toward a secure-by-design paradigm.

## 研究问题

This work presents ATLAS, an LLM-driven framework that bridges standardized threat modeling and property-based formal verification for System-on-Chip (SoC) security. Starting from vulnerability knowledge bases such as Common Weakness Enumeration (CWE), ATLAS identifies SoC-specific assets, maps relevant weaknesses, and generates assertion-based security properties and JasperGold scripts for verification. By combining asset-centric analysis with standardized threat model templates and multi-source SoC context, ATLAS automates the transformation from vulnerability reasoning to formal proof. Evaluated on three HACK@DAC benchmarks, ATLAS detected 39/48 CWEs and generated correct properties for 33 of those bugs, advancing automated, knowledge-driven SoC security verification toward a secure-by-design paradigm.

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
