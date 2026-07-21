# Security Enclave Architecture for Heterogeneous Security Primitives for Supply-Chain Attacks

## 基本信息

- 作者：Kshitij Raj、Atri Chatterjee、Patanjali SLPSK、Swarup Bhunia、Sandip Ray
- 发表日期：2025-07-15
- 更新日期：2025-07-15
- 来源：arXiv
- 来源编号：2507.10971v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2507.10971v1](http://arxiv.org/abs/2507.10971v1)
- PDF：[https://arxiv.org/pdf/2507.10971v1](https://arxiv.org/pdf/2507.10971v1)
- 分析模式：仅元数据分析

## 摘要

Designing secure architectures for system-on-chip (SoC) platforms is a highly intricate and time-intensive task, often requiring months of development and meticulous verification. Even minor architectural oversights can lead to critical vulnerabilities that undermine the security of the entire chip. In response to this challenge, we introduce CITADEL, a modular security framework aimed at streamlining the creation of robust security architectures for SoCs. CITADEL offers a configurable, plug-and-play subsystem composed of custom intellectual property (IP) blocks, enabling the construction of diverse security mechanisms tailored to specific threats. As a concrete demonstration, we instantiate CITADEL to defend against supply-chain threats, illustrating how the framework adapts to one of the most pressing concerns in hardware security. This paper explores the range of obstacles encountered when building a unified security architecture capable of addressing multiple attack vectors and presents CITADEL's strategies for overcoming them. Through several real-world case studies, we showcase the practical implementation of CITADEL and present a thorough evaluation of its impact on silicon area and power consumption across various ASIC technologies. Results indicate that CITADEL introduces only minimal resource overhead, making it a practical solution for enhancing SoC security.

## 研究问题

Designing secure architectures for system-on-chip (SoC) platforms is a highly intricate and time-intensive task, often requiring months of development and meticulous verification. Even minor architectural oversights can lead to critical vulnerabilities that undermine the security of the entire chip. In response to this challenge, we introduce CITADEL, a modular security framework aimed at streamlining the creation of robust security architectures for SoCs. CITADEL offers a configurable, plug-and-play subsystem composed of custom intellectual property (IP) blocks, enabling the construction of diverse security mechanisms tailored to specific threats. As a concrete demonstration, we instantiate CITADEL to defend against supply-chain threats, illustrating how the framework adapts to one of the most pressing concerns in hardware security. This paper explores the range of obstacles encountered when building a unified security architecture capable of addressing multiple attack vectors and presents CITADEL's strategies for overcoming them. Through several real-world case studies, we showcase the practical implementation of CITADEL and present a thorough evaluation of its impact on silicon area and power consumption across various ASIC technologies. Results indicate that CITADEL introduces only minimal resource overhead, making it a practical solution for enhancing SoC security.

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
