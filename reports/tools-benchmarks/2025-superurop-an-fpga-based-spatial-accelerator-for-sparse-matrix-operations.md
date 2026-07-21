# SuperUROP: An FPGA-Based Spatial Accelerator for Sparse Matrix Operations

## 基本信息

- 作者：Rishab Parthasarathy
- 发表日期：2025-09-15
- 更新日期：2025-09-15
- 来源：arXiv
- 来源编号：2509.11529v1
- 研究类别：RISC-V Fuzzing 研究、RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2509.11529v1](http://arxiv.org/abs/2509.11529v1)
- PDF：[https://arxiv.org/pdf/2509.11529v1](https://arxiv.org/pdf/2509.11529v1)
- 分析模式：仅元数据分析

## 摘要

Solving sparse systems of linear equations is a fundamental problem in the field of numerical methods, with applications spanning from circuit design to urban planning. These problems can have millions of constraints, such as when laying out transistors on a circuit, or trying to optimize traffic light timings, making fast sparse solvers extremely important. However, existing state-of-the-art software-level solutions for solving sparse linear systems, termed iterative solvers, are extremely inefficient on current hardware. This inefficiency can be attributed to two key reasons: (1) poor short-term data reuse, which causes frequent, irregular memory accesses, and (2) complex data dependencies, which limit parallelism. Hence, in this paper, we present an FPGA implementation of the existing Azul accelerator, an SRAM-only hardware accelerator that achieves both high memory bandwidth utilization and arithmetic intensity. Azul features a grid of tiles, each of which is composed of a processing element (PE) and a small independent SRAM memory, which are all connected over a network on chip (NoC). We implement Azul on FPGA using simple RISC-V CPU cores connected to a memory hierarchy of different FPGA memory modules. We utilize custom RISC-V ISA augmentations to implement a task-based programming model for the various PEs, allowing communication over the NoC. Finally, we design simple distributed test cases so that we can functionally verify the FPGA implementation, verifying equivalent performance to an architectural simulation of the Azul framework.

## 研究问题

Solving sparse systems of linear equations is a fundamental problem in the field of numerical methods, with applications spanning from circuit design to urban planning. These problems can have millions of constraints, such as when laying out transistors on a circuit, or trying to optimize traffic light timings, making fast sparse solvers extremely important. However, existing state-of-the-art software-level solutions for solving sparse linear systems, termed iterative solvers, are extremely inefficient on current hardware. This inefficiency can be attributed to two key reasons: (1) poor short-term data reuse, which causes frequent, irregular memory accesses, and (2) complex data dependencies, which limit parallelism. Hence, in this paper, we present an FPGA implementation of the existing Azul accelerator, an SRAM-only hardware accelerator that achieves both high memory bandwidth utilization and arithmetic intensity. Azul features a grid of tiles, each of which is composed of a processing element (PE) and a small independent SRAM memory, which are all connected over a network on chip (NoC). We implement Azul on FPGA using simple RISC-V CPU cores connected to a memory hierarchy of different FPGA memory modules. We utilize custom RISC-V ISA augmentations to implement a task-based programming model for the various PEs, allowing communication over the NoC. Finally, we design simple distributed test cases so that we can functionally verify the FPGA implementation, verifying equivalent performance to an architectural simulation of the Azul framework.

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
