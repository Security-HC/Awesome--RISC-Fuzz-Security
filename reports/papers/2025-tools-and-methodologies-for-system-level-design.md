# Tools and Methodologies for System-Level Design

## 基本信息

- 作者：Shuvra S. Bhattacharyya、Marilyn Wolf
- 发表日期：2025-07-13
- 更新日期：2025-07-13
- 来源：arXiv
- 来源编号：2507.09660v1
- 研究类别：RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2507.09660v1](http://arxiv.org/abs/2507.09660v1)
- PDF：[https://arxiv.org/pdf/2507.09660v1](https://arxiv.org/pdf/2507.09660v1)
- 分析模式：仅元数据分析

## 摘要

System-level design, once the province of board designers, has now become a central concern for chip designers. Because chip design is a less forgiving design medium -- design cycles are longer and mistakes are harder to correct -- system-on-chip designers need a more extensive tool suite than may be used by board designers and a variety of tools and methodologies have been developed for system-level design of systems-on-chips (SoCs). System-level design is less amenable to synthesis than are logic or physical design. As a result, system-level tools concentrate on modeling, simulation, design space exploration, and design verification. The goal of modeling is to correctly capture the system's operational semantics, which helps with both implementation and verification. The study of models of computation provides a framework for the description of digital systems. Not only do we need to understand a particular style of computation, such as dataflow, but we also need to understand how different models of computation can reliably communicate with each other. Design space exploration tools, such as hardware/software co-design, develop candidate designs to understand trade-offs. Simulation can be used not only to verify functional correctness but also to supply performance and power/energy information for design analysis. This chapter employs two applications -- video and neural networks -- as examples. Both are leading-edge applications that illustrate many important aspects of system-level design.

## 研究问题

System-level design, once the province of board designers, has now become a central concern for chip designers. Because chip design is a less forgiving design medium -- design cycles are longer and mistakes are harder to correct -- system-on-chip designers need a more extensive tool suite than may be used by board designers and a variety of tools and methodologies have been developed for system-level design of systems-on-chips (SoCs). System-level design is less amenable to synthesis than are logic or physical design. As a result, system-level tools concentrate on modeling, simulation, design space exploration, and design verification. The goal of modeling is to correctly capture the system's operational semantics, which helps with both implementation and verification. The study of models of computation provides a framework for the description of digital systems. Not only do we need to understand a particular style of computation, such as dataflow, but we also need to understand how different models of computation can reliably communicate with each other. Design space exploration tools, such as hardware/software co-design, develop candidate designs to understand trade-offs. Simulation can be used not only to verify functional correctness but also to supply performance and power/energy information for design analysis. This chapter employs two applications -- video and neural networks -- as examples. Both are leading-edge applications that illustrate many important aspects of system-level design.

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
