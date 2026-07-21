# GoldenFuzz: Generative Golden Reference Hardware Fuzzing

## 基本信息

- 作者：Lichao Wu、Mohamadreza Rostami、Huimin Li、Nikhilesh Singh、Ahmad-Reza Sadeghi
- 发表日期：2025-12-25
- 更新日期：2025-12-25
- 来源：arXiv
- 来源编号：2512.21524v1
- 研究类别：RISC-V Fuzzing 研究、RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[http://arxiv.org/abs/2512.21524v1](http://arxiv.org/abs/2512.21524v1)
- PDF：[https://arxiv.org/pdf/2512.21524v1](https://arxiv.org/pdf/2512.21524v1)
- 分析模式：仅元数据分析

## 摘要

Modern hardware systems, driven by demands for high performance and application-specific functionality, have grown increasingly complex, introducing large surfaces for bugs and security-critical vulnerabilities. Fuzzing has emerged as a scalable solution for discovering such flaws. Yet, existing hardware fuzzers suffer from limited semantic awareness, inefficient test refinement, and high computational overhead due to reliance on slow device simulation. In this paper, we present GoldenFuzz, a novel two-stage hardware fuzzing framework that partially decouples test case refinement from coverage and vulnerability exploration. GoldenFuzz leverages a fast, ISA-compliant Golden Reference Model (GRM) as a ``digital twin'' of the Device Under Test (DUT). It fuzzes the GRM first, enabling rapid, low-cost test case refinement, accelerating deep architectural exploration and vulnerability discovery on DUT. During the fuzzing pipeline, GoldenFuzz iteratively constructs test cases by concatenating carefully chosen instruction blocks that balance the subtle inter- and intra-instructions quality. A feedback-driven mechanism leveraging insights from both high- and low-coverage samples further enhances GoldenFuzz's capability in hardware state exploration. Our evaluation of three RISC-V processors, RocketChip, BOOM, and CVA6, demonstrates that GoldenFuzz significantly outperforms existing fuzzers in achieving the highest coverage with minimal test case length and computational overhead. GoldenFuzz uncovers all known vulnerabilities and discovers five new ones, four of which are classified as highly severe with CVSS v3 severity scores exceeding seven out of ten. It also identifies two previously unknown vulnerabilities in the commercial BA51-H core extension.

## 研究问题

Modern hardware systems, driven by demands for high performance and application-specific functionality, have grown increasingly complex, introducing large surfaces for bugs and security-critical vulnerabilities. Fuzzing has emerged as a scalable solution for discovering such flaws. Yet, existing hardware fuzzers suffer from limited semantic awareness, inefficient test refinement, and high computational overhead due to reliance on slow device simulation. In this paper, we present GoldenFuzz, a novel two-stage hardware fuzzing framework that partially decouples test case refinement from coverage and vulnerability exploration. GoldenFuzz leverages a fast, ISA-compliant Golden Reference Model (GRM) as a ``digital twin'' of the Device Under Test (DUT). It fuzzes the GRM first, enabling rapid, low-cost test case refinement, accelerating deep architectural exploration and vulnerability discovery on DUT. During the fuzzing pipeline, GoldenFuzz iteratively constructs test cases by concatenating carefully chosen instruction blocks that balance the subtle inter- and intra-instructions quality. A feedback-driven mechanism leveraging insights from both high- and low-coverage samples further enhances GoldenFuzz's capability in hardware state exploration. Our evaluation of three RISC-V processors, RocketChip, BOOM, and CVA6, demonstrates that GoldenFuzz significantly outperforms existing fuzzers in achieving the highest coverage with minimal test case length and computational overhead. GoldenFuzz uncovers all known vulnerabilities and discovers five new ones, four of which are classified as highly severe with CVSS v3 severity scores exceeding seven out of ten. It also identifies two previously unknown vulnerabilities in the commercial BA51-H core extension.

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
