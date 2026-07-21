# FuzzBox: Blending Fuzzing into Emulation for Binary-Only Embedded Targets

## 基本信息

- 作者：Carmine Cesarano、Roberto Natella
- 发表日期：2025-09-06
- 更新日期：2025-09-06
- 来源：arXiv
- 来源编号：2509.05643v1
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2509.05643v1](http://arxiv.org/abs/2509.05643v1)
- PDF：[https://arxiv.org/pdf/2509.05643v1](https://arxiv.org/pdf/2509.05643v1)
- 分析模式：仅元数据分析

## 摘要

Coverage-guided fuzzing has been widely applied to address zero-day vulnerabilities in general-purpose software and operating systems. This approach relies on instrumenting the target code at compile time. However, applying it to industrial systems remains challenging, due to proprietary and closed-source compiler toolchains and lack of access to source code. FuzzBox addresses these limitations by integrating emulation with fuzzing: it dynamically instruments code during execution in a virtualized environment, for the injection of fuzz inputs, failure detection, and coverage analysis, without requiring source code recompilation and hardware-specific dependencies. We show the effectiveness of FuzzBox through experiments in the context of a proprietary MILS (Multiple Independent Levels of Security) hypervisor for industrial applications. Additionally, we analyze the applicability of FuzzBox across commercial IoT firmware, showcasing its broad portability.

## 研究问题

Coverage-guided fuzzing has been widely applied to address zero-day vulnerabilities in general-purpose software and operating systems. This approach relies on instrumenting the target code at compile time. However, applying it to industrial systems remains challenging, due to proprietary and closed-source compiler toolchains and lack of access to source code. FuzzBox addresses these limitations by integrating emulation with fuzzing: it dynamically instruments code during execution in a virtualized environment, for the injection of fuzz inputs, failure detection, and coverage analysis, without requiring source code recompilation and hardware-specific dependencies. We show the effectiveness of FuzzBox through experiments in the context of a proprietary MILS (Multiple Independent Levels of Security) hypervisor for industrial applications. Additionally, we analyze the applicability of FuzzBox across commercial IoT firmware, showcasing its broad portability.

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
