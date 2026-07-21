# täkōFormal: Enabling Robust Software for Programmable Memory Hierarchies (Extended Version)

## 基本信息

- 作者：Pranav Srinivasan、Manos Kapritsos、Yatin A. Manerkar
- 发表日期：2026-05-05
- 更新日期：2026-05-05
- 来源：arXiv
- 来源编号：2605.04172v1
- 研究类别：微架构安全
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2605.04172v1](http://arxiv.org/abs/2605.04172v1)
- PDF：[https://arxiv.org/pdf/2605.04172v1](https://arxiv.org/pdf/2605.04172v1)
- 分析模式：仅元数据分析

## 摘要

Accelerators provide large performance and energy-efficiency benefits, but can significantly change the hardware-software interface. The täkō programmable memory hierarchy accelerates data movement by enabling programmers to run user-defined callback functions triggered by cache misses, evictions, and writebacks. However, it also leads to drastically increased complexity and counterintuitive outcomes. In response, we develop an ISA-level memory consistency model (MCM) for täkō that captures the semantics of its operation, and we show how it enables programmers to formally reason about their täkō programs. We also prove the soundness of this ISA-level MCM by constructing a detailed täkō implementation model and verifying that all executions of the implementation model are allowed by our ISA-level MCM. Along the way, we discover useful insights about microarchitectural modeling and verification that are applicable to hardware in general. This is the extended version of the ISCA 2026 paper "täkōFormal: Enabling Robust Software for Programmable Memory Hierarchies". This version adds material on additional litmus tests to Section V to further explore the programmability of täkō using our ISA-level MCM.

## 研究问题

Accelerators provide large performance and energy-efficiency benefits, but can significantly change the hardware-software interface. The täkō programmable memory hierarchy accelerates data movement by enabling programmers to run user-defined callback functions triggered by cache misses, evictions, and writebacks. However, it also leads to drastically increased complexity and counterintuitive outcomes. In response, we develop an ISA-level memory consistency model (MCM) for täkō that captures the semantics of its operation, and we show how it enables programmers to formally reason about their täkō programs. We also prove the soundness of this ISA-level MCM by constructing a detailed täkō implementation model and verifying that all executions of the implementation model are allowed by our ISA-level MCM. Along the way, we discover useful insights about microarchitectural modeling and verification that are applicable to hardware in general. This is the extended version of the ISCA 2026 paper "täkōFormal: Enabling Robust Software for Programmable Memory Hierarchies". This version adds material on additional litmus tests to Section V to further explore the programmability of täkō using our ISA-level MCM.

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
