# Multi-target Coverage-based Greybox Fuzzing

## 基本信息

- 作者：Masami Ichikawa
- 发表日期：2026-03-26
- 更新日期：2026-03-26
- 来源：arXiv
- 来源编号：2603.25354v1
- 研究类别：RISC-V Fuzzing 研究
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2603.25354v1](http://arxiv.org/abs/2603.25354v1)
- PDF：[https://arxiv.org/pdf/2603.25354v1](https://arxiv.org/pdf/2603.25354v1)
- 分析模式：仅元数据分析

## 摘要

In recent years, fuzzing has been widely applied not only to application software but also to system software, including the Linux kernel and firmware, and has become a powerful technique for vulnerability discovery. Among these approaches, Coverage-based grey-box fuzzing, which utilizes runtime code coverage information, has become the dominant methodology. Conventional fuzzing techniques primarily target a single software component and have paid little attention to cooperative execution with other software. However, modern system software architectures commonly consist of firmware and an operating system that operate cooperatively through well-defined interfaces, such as OpenSBI in the RISC-V architecture and OP-TEE in the ARM architecture. In this study, we investigate fuzzing techniques for architectures in which an operating system and firmware operate cooperatively. In particular, we propose a fuzzing method that enables deeper exploration of the system by leveraging the code coverage of each cooperating software component as feedback, compared to conventional Single-target fuzzing. To observe the execution of the operating system and firmware in a unified manner, our method adopts QEMU as a virtualization environment and executes fuzzing by booting the system within a virtual machine. This enables the measurement of code coverage across software boundaries. Furthermore, we implemented the proposed method as a Multi-target Coverage-based Greybox Fuzzer called MTCFuzz and evaluated its effectiveness.

## 研究问题

In recent years, fuzzing has been widely applied not only to application software but also to system software, including the Linux kernel and firmware, and has become a powerful technique for vulnerability discovery. Among these approaches, Coverage-based grey-box fuzzing, which utilizes runtime code coverage information, has become the dominant methodology. Conventional fuzzing techniques primarily target a single software component and have paid little attention to cooperative execution with other software. However, modern system software architectures commonly consist of firmware and an operating system that operate cooperatively through well-defined interfaces, such as OpenSBI in the RISC-V architecture and OP-TEE in the ARM architecture. In this study, we investigate fuzzing techniques for architectures in which an operating system and firmware operate cooperatively. In particular, we propose a fuzzing method that enables deeper exploration of the system by leveraging the code coverage of each cooperating software component as feedback, compared to conventional Single-target fuzzing. To observe the execution of the operating system and firmware in a unified manner, our method adopts QEMU as a virtualization environment and executes fuzzing by booting the system within a virtual machine. This enables the measurement of code coverage across software boundaries. Furthermore, we implemented the proposed method as a Multi-target Coverage-based Greybox Fuzzer called MTCFuzz and evaluated its effectiveness.

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
