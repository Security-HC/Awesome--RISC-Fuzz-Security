# Trustworthy Software Project Generation : a Case Study with an Interactive Theorem Prover

## 基本信息

- 作者：Jian Fang、Yingfei Xiong
- 发表日期：2026-05-25
- 更新日期：2026-05-25
- 来源：arXiv
- 来源编号：2605.26017v1
- 研究类别：RISC-V Fuzzing、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2605.26017v1](http://arxiv.org/abs/2605.26017v1)
- PDF：[https://arxiv.org/pdf/2605.26017v1](https://arxiv.org/pdf/2605.26017v1)
- 分析模式：仅元数据分析

## 摘要

Generating code from natural-language requirements has become a primary route for LLM-assisted software development. Although LLMs can successfully complete small programming tasks, generating an entire complex project remains unreliable because subtle errors may survive compilation and testing. Verified programming can reduce this risk by requiring generated implementations to satisfy machine-checked specifications. Existing explorations mostly target verification-oriented languages and toolchains such as Dafny and Frama-C, but directly generating project-scale verified code with these systems remains difficult. This paper studies whether interactive theorem provers (ITPs) can support large-scale software generation. Because ITPs handle pure total functions but not effects such as I/O, our agent separates effectful code from pure logic: it implements the effects in the target language, proves the pure logic in an ITP, and extracts it for integration into the final project. We study this route through the fully automatic development of a CPU interpreter for all 47 instructions of the unprivileged RISC-V RV32I base: after the requirements are supplied, no human intervenes in synthesis, proof repair, extraction, or integration. With Rocq as the backend, the agent completes the project within 30 minutes, producing 1,859 lines of verified Rocq and extracting 2,848 lines of C++. The resulting interpreter passes all 265 LLM-generated tests covering the 47 instructions and exhibits zero crashes and zero hangs during 12 hours of AFL++ fuzzing. Under the same configuration, a Dafny-based backend fails to complete verification. Our observation is that Rocq exposes a concrete proof state when a proof attempt fails, giving the agent actionable feedback for repair. These results provide empirical evidence that ITP-based verified programming is a feasible route for LLM-generated software projects.

## 研究问题

Generating code from natural-language requirements has become a primary route for LLM-assisted software development. Although LLMs can successfully complete small programming tasks, generating an entire complex project remains unreliable because subtle errors may survive compilation and testing. Verified programming can reduce this risk by requiring generated implementations to satisfy machine-checked specifications. Existing explorations mostly target verification-oriented languages and toolchains such as Dafny and Frama-C, but directly generating project-scale verified code with these systems remains difficult. This paper studies whether interactive theorem provers (ITPs) can support large-scale software generation. Because ITPs handle pure total functions but not effects such as I/O, our agent separates effectful code from pure logic: it implements the effects in the target language, proves the pure logic in an ITP, and extracts it for integration into the final project. We study this route through the fully automatic development of a CPU interpreter for all 47 instructions of the unprivileged RISC-V RV32I base: after the requirements are supplied, no human intervenes in synthesis, proof repair, extraction, or integration. With Rocq as the backend, the agent completes the project within 30 minutes, producing 1,859 lines of verified Rocq and extracting 2,848 lines of C++. The resulting interpreter passes all 265 LLM-generated tests covering the 47 instructions and exhibits zero crashes and zero hangs during 12 hours of AFL++ fuzzing. Under the same configuration, a Dafny-based backend fails to complete verification. Our observation is that Rocq exposes a concrete proof state when a proof attempt fails, giving the agent actionable feedback for repair. These results provide empirical evidence that ITP-based verified programming is a feasible route for LLM-generated software projects.

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
