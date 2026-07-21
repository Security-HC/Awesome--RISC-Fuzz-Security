# DiffSpec: Differential Testing with LLMs using Natural Language Specifications and Code Artifacts

## 基本信息

- 作者：Nikitha Rao、Elizabeth Gilbert、Harrison Green、Tahina Ramananandro、Nikhil Swamy、Claire Le Goues、Sarah Fakhoury
- 发表日期：2024-10-05
- 更新日期：2025-05-06
- 来源：arXiv
- 来源编号：2410.04249v3
- 研究类别：RISC-V Fuzzing、Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2410.04249v3](http://arxiv.org/abs/2410.04249v3)
- PDF：[https://arxiv.org/pdf/2410.04249v3](https://arxiv.org/pdf/2410.04249v3)
- 分析模式：仅元数据分析

## 摘要

Differential testing can be an effective way to find bugs in software systems with multiple implementations that conform to the same specification, like compilers, network protocol parsers, or language runtimes. Specifications for such systems are often standardized in natural language documents, like Instruction Set Architecture (ISA) specifications or IETF RFC's. Large Language Models (LLMs) have demonstrated potential in both generating tests and handling large volumes of natural language text, making them well-suited for analyzing artifacts like specification documents, bug reports, and code implementations. In this work, we leverage natural language and code artifacts to guide LLMs to generate targeted tests that highlight meaningful behavioral differences between implementations, including those corresponding to bugs. We introduce DiffSpec, a framework for generating differential tests with LLMs using prompt chaining. We demonstrate DiffSpec's efficacy on two different (extensively tested) systems, eBPF runtimes and Wasm validators. Using DiffSpec, we generated 1901 differentiating tests, uncovering at least four distinct and confirmed bugs in eBPF, including a kernel memory leak, inconsistent behavior in jump instructions, undefined behavior when using the stack pointer, and tests with infinite loops that hang the verifier in ebpf-for-windows. We also found 299 differentiating tests in Wasm validators pointing to two confirmed and fixed bugs.

## 研究问题

Differential testing can be an effective way to find bugs in software systems with multiple implementations that conform to the same specification, like compilers, network protocol parsers, or language runtimes. Specifications for such systems are often standardized in natural language documents, like Instruction Set Architecture (ISA) specifications or IETF RFC's. Large Language Models (LLMs) have demonstrated potential in both generating tests and handling large volumes of natural language text, making them well-suited for analyzing artifacts like specification documents, bug reports, and code implementations. In this work, we leverage natural language and code artifacts to guide LLMs to generate targeted tests that highlight meaningful behavioral differences between implementations, including those corresponding to bugs. We introduce DiffSpec, a framework for generating differential tests with LLMs using prompt chaining. We demonstrate DiffSpec's efficacy on two different (extensively tested) systems, eBPF runtimes and Wasm validators. Using DiffSpec, we generated 1901 differentiating tests, uncovering at least four distinct and confirmed bugs in eBPF, including a kernel memory leak, inconsistent behavior in jump instructions, undefined behavior when using the stack pointer, and tests with infinite loops that hang the verifier in ebpf-for-windows. We also found 299 differentiating tests in Wasm validators pointing to two confirmed and fixed bugs.

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
