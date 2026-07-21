# FlexEmu: Towards Flexible MCU Peripheral Emulation (Extended Version)

## 基本信息

- 作者：Chongqing Lei、Zhen Ling、Xiangyu Xu、Shaofeng Li、Guangchi Liu、Kai Dong、Junzhou Luo
- 发表日期：2025-09-09
- 更新日期：2025-09-09
- 来源：arXiv
- 来源编号：2509.07615v1
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2509.07615v1](http://arxiv.org/abs/2509.07615v1)
- PDF：[https://arxiv.org/pdf/2509.07615v1](https://arxiv.org/pdf/2509.07615v1)
- 分析模式：仅元数据分析

## 摘要

Microcontroller units (MCUs) are widely used in embedded devices due to their low power consumption and cost-effectiveness. MCU firmware controls these devices and is vital to the security of embedded systems. However, performing dynamic security analyses for MCU firmware has remained challenging due to the lack of usable execution environments -- existing dynamic analyses cannot run on physical devices (e.g., insufficient computational resources), while building emulators is costly due to the massive amount of heterogeneous hardware, especially peripherals. Our work is based on the insight that MCU peripherals can be modeled in a two-fold manner. At the structural level, peripherals have diverse implementations but we can use a limited set of primitives to abstract peripherals because their hardware implementations are based on common hardware concepts. At the semantic level, peripherals have diverse functionalities. However, we can use a single unified semantic model to describe the same kind of peripherals because they exhibit similar functionalities. Building on this, we propose FlexEmu, a flexible MCU peripheral emulation framework. Once semantic models are created, FlexEmu automatically extracts peripheral-specific details to instantiate models and generate emulators accordingly. We have successfully applied FlexEmu to model 12 kinds of MCU peripherals. Our evaluation on 90 firmware samples across 15 different MCU platforms shows that the automatically generated emulators can faithfully replicate hardware behaviors and achieve a 98.48% unit test passing rate, outperforming state-of-the-art approaches. To demonstrate the implications of FlexEmu on firmware security, we use the generated emulators to fuzz three popular RTOSes and uncover 10 previously unknown bugs.

## 研究问题

Microcontroller units (MCUs) are widely used in embedded devices due to their low power consumption and cost-effectiveness. MCU firmware controls these devices and is vital to the security of embedded systems. However, performing dynamic security analyses for MCU firmware has remained challenging due to the lack of usable execution environments -- existing dynamic analyses cannot run on physical devices (e.g., insufficient computational resources), while building emulators is costly due to the massive amount of heterogeneous hardware, especially peripherals. Our work is based on the insight that MCU peripherals can be modeled in a two-fold manner. At the structural level, peripherals have diverse implementations but we can use a limited set of primitives to abstract peripherals because their hardware implementations are based on common hardware concepts. At the semantic level, peripherals have diverse functionalities. However, we can use a single unified semantic model to describe the same kind of peripherals because they exhibit similar functionalities. Building on this, we propose FlexEmu, a flexible MCU peripheral emulation framework. Once semantic models are created, FlexEmu automatically extracts peripheral-specific details to instantiate models and generate emulators accordingly. We have successfully applied FlexEmu to model 12 kinds of MCU peripherals. Our evaluation on 90 firmware samples across 15 different MCU platforms shows that the automatically generated emulators can faithfully replicate hardware behaviors and achieve a 98.48% unit test passing rate, outperforming state-of-the-art approaches. To demonstrate the implications of FlexEmu on firmware security, we use the generated emulators to fuzz three popular RTOSes and uncover 10 previously unknown bugs.

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
