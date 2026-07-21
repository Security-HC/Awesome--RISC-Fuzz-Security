# ProtocolLLM: RTL Benchmark for SystemVerilog Generation of Communication Protocols

## 基本信息

- 作者：Arnav Sheth、Ivaxi Sheth、Mario Fritz
- 发表日期：2025-06-09
- 更新日期：2025-07-15
- 来源：arXiv
- 来源编号：2506.07945v2
- 研究类别：RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2506.07945v2](http://arxiv.org/abs/2506.07945v2)
- PDF：[https://arxiv.org/pdf/2506.07945v2](https://arxiv.org/pdf/2506.07945v2)
- 分析模式：仅元数据分析

## 摘要

Recent advances in large language models (LLMs) have demonstrated strong performance in generating code for general-purpose programming languages. However, their potential for hardware description languages (HDLs), such as SystemVerilog, remains largely unexplored. HDL code generation poses unique challenges due to strict timing semantics, concurrency, and synthesizability constraints essential for correct hardware functionality. Further, HDL-based design flows encompass a broad set of tasks beyond structural code generation, including testbench development, assertion-based verification, timing closure, and protocol-level integration for on-chip communication. In this work, we evaluate the capabilities of both open-source and state-of-the-art LLMs in generating synthesizable and functionally accurate SystemVerilog implementations of widely used communication protocols that are critical components of embedded and System-on-Chip (SoC) systems. We introduce ProtocolLLM, the first benchmark suite specifically targeting these protocols with tasks spanning multiple design abstraction levels and varying prompt specificity. Our evaluation method also focuses on timing correctness in addition to synthesizability and syntactic correctness. We observe that most of the models fail to generate SystemVerilog code for communication protocols that follow timing constrains.

## 研究问题

Recent advances in large language models (LLMs) have demonstrated strong performance in generating code for general-purpose programming languages. However, their potential for hardware description languages (HDLs), such as SystemVerilog, remains largely unexplored. HDL code generation poses unique challenges due to strict timing semantics, concurrency, and synthesizability constraints essential for correct hardware functionality. Further, HDL-based design flows encompass a broad set of tasks beyond structural code generation, including testbench development, assertion-based verification, timing closure, and protocol-level integration for on-chip communication. In this work, we evaluate the capabilities of both open-source and state-of-the-art LLMs in generating synthesizable and functionally accurate SystemVerilog implementations of widely used communication protocols that are critical components of embedded and System-on-Chip (SoC) systems. We introduce ProtocolLLM, the first benchmark suite specifically targeting these protocols with tasks spanning multiple design abstraction levels and varying prompt specificity. Our evaluation method also focuses on timing correctness in addition to synthesizability and syntactic correctness. We observe that most of the models fail to generate SystemVerilog code for communication protocols that follow timing constrains.

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
