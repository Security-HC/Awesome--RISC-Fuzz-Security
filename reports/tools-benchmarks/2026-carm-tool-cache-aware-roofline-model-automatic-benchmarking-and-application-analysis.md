# CARM Tool: Cache-Aware Roofline Model Automatic Benchmarking and Application Analysis

## 基本信息

- 作者：José Morgado、Leonel Sousa、Aleksandar Ilic
- 发表日期：2026-05-28
- 更新日期：2026-05-28
- 来源：arXiv
- 来源编号：2605.29740v1
- 研究类别：RISC-V Fuzzing 研究、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2605.29740v1](http://arxiv.org/abs/2605.29740v1)
- PDF：[https://arxiv.org/pdf/2605.29740v1](https://arxiv.org/pdf/2605.29740v1)
- 分析模式：仅元数据分析

## 摘要

In recent years, HPC systems and CPU architectures as their central components, have become increasingly complex, making application development and optimization quite challenging. In this respect, intuitive performance models like the Cache-aware Roofline Model (CARM) offer effective guidance by providing insights into bottlenecks that limit the application's ability to reach the system's maximum performance. To fully exploit the benefits of CARM optimization guidance for application development, automatic tools for cross-architecture model construction and in-depth application characterization are absolutely essential. Given a plethora of existing CPU architectures, the current landscape of CARM-enabled tools covers either vendor-specific (Intel Advisor), not sufficiently developed (ARM) or simply non-existing (AMD, RISC-V) tools. This is a particular gap that this work intends to close by bringing automatic CARM support to all major CPU architectures and ISAs, i.e., x86 (Intel, AMD), ARM, and RISC-V, by developing assembly microbenchmarks specifically tailored to cover a full performance spectrum of modern CPUs (from scalar to all supported vector ISA extensions) for both computational units and all memory hierarchy levels. Additionally, this work integrates application analysis within the CARM framework using performance counters and dynamic binary instrumentation. Experimental results show that the CARM roofs constructed with the proposed automated framework provide less than a 1% deviation across various tested architectural maximums.

## 研究问题

In recent years, HPC systems and CPU architectures as their central components, have become increasingly complex, making application development and optimization quite challenging. In this respect, intuitive performance models like the Cache-aware Roofline Model (CARM) offer effective guidance by providing insights into bottlenecks that limit the application's ability to reach the system's maximum performance. To fully exploit the benefits of CARM optimization guidance for application development, automatic tools for cross-architecture model construction and in-depth application characterization are absolutely essential. Given a plethora of existing CPU architectures, the current landscape of CARM-enabled tools covers either vendor-specific (Intel Advisor), not sufficiently developed (ARM) or simply non-existing (AMD, RISC-V) tools. This is a particular gap that this work intends to close by bringing automatic CARM support to all major CPU architectures and ISAs, i.e., x86 (Intel, AMD), ARM, and RISC-V, by developing assembly microbenchmarks specifically tailored to cover a full performance spectrum of modern CPUs (from scalar to all supported vector ISA extensions) for both computational units and all memory hierarchy levels. Additionally, this work integrates application analysis within the CARM framework using performance counters and dynamic binary instrumentation. Experimental results show that the CARM roofs constructed with the proposed automated framework provide less than a 1% deviation across various tested architectural maximums.

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
