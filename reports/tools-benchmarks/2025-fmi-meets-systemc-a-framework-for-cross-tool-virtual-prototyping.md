# FMI Meets SystemC: A Framework for Cross-Tool Virtual Prototyping

## 基本信息

- 作者：Nils Bosbach、Meik Schmidt、Lukas Jünger、Matthias Berthold、Rainer Leupers
- 发表日期：2025-07-24
- 更新日期：2025-10-27
- 来源：arXiv
- 来源编号：2507.18339v3
- 研究类别：RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2507.18339v3](http://arxiv.org/abs/2507.18339v3)
- PDF：[https://arxiv.org/pdf/2507.18339v3](https://arxiv.org/pdf/2507.18339v3)
- 分析模式：仅元数据分析

## 摘要

As systems become more complex, the demand for thorough testing and virtual prototyping grows. To simulate whole systems, multiple tools are usually needed to cover different parts. These parts include the hardware of a system and the environment with which the system interacts. The Functional Mock-up Interface (FMI) standard for co-simulation can be used to connect these tools. The control part of modern systems is usually a computing unit, such as a System-on-a-Chip (SoC) or Microcontroller Unit (MCU), which executes software from a connected memory and interacts with peripherals. To develop software without requiring access to physical hardware, full-system simulators, the so-called Virtual Platforms (VPs), are commonly used. The IEEE-standardized framework for VP development is SystemC TLM. SystemC provides interfaces and concepts that enable modular design and model exchange. However, SystemC lacks native FMI support, which limits the integration into broader co-simulation environments. This paper presents a novel framework to control and interact with SystemC-based VPs using the FMI. We present a case study showing how a simulated temperature sensor in a SystemC simulation can obtain temperature values from an external tool via FMI. This approach allows the unmodified target software to run on the VP and receive realistic environmental input data such as temperature, velocity, or acceleration values from other tools. Thus, extensive software testing and verification is enabled. By having tests ready and the software pre-tested using a VP once the physical hardware is available, certifications like ISO 26262 can be done earlier.

## 研究问题

As systems become more complex, the demand for thorough testing and virtual prototyping grows. To simulate whole systems, multiple tools are usually needed to cover different parts. These parts include the hardware of a system and the environment with which the system interacts. The Functional Mock-up Interface (FMI) standard for co-simulation can be used to connect these tools. The control part of modern systems is usually a computing unit, such as a System-on-a-Chip (SoC) or Microcontroller Unit (MCU), which executes software from a connected memory and interacts with peripherals. To develop software without requiring access to physical hardware, full-system simulators, the so-called Virtual Platforms (VPs), are commonly used. The IEEE-standardized framework for VP development is SystemC TLM. SystemC provides interfaces and concepts that enable modular design and model exchange. However, SystemC lacks native FMI support, which limits the integration into broader co-simulation environments. This paper presents a novel framework to control and interact with SystemC-based VPs using the FMI. We present a case study showing how a simulated temperature sensor in a SystemC simulation can obtain temperature values from an external tool via FMI. This approach allows the unmodified target software to run on the VP and receive realistic environmental input data such as temperature, velocity, or acceleration values from other tools. Thus, extensive software testing and verification is enabled. By having tests ready and the software pre-tested using a VP once the physical hardware is available, certifications like ISO 26262 can be done earlier.

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
