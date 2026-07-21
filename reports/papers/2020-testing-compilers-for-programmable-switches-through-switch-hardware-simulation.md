# Testing Compilers for Programmable Switches Through Switch Hardware Simulation

## 基本信息

- 作者：Michael D. Wong、Aatish Kishan Varma、Anirudh Sivaraman
- 发表日期：2020-05-05
- 更新日期：2020-10-27
- 来源：arXiv
- 来源编号：2005.02310v3
- 研究类别：RISC-V Fuzzing、RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2005.02310v3](http://arxiv.org/abs/2005.02310v3)
- PDF：[https://arxiv.org/pdf/2005.02310v3](https://arxiv.org/pdf/2005.02310v3)
- 分析模式：仅元数据分析

## 摘要

Programmable switches have emerged as powerful and flexible alternatives to fixed-function forwarding devices. But because of the unique hardware constraints of network switches, the design and implementation of compilers targeting these devices is tedious and error prone. Despite the important role that compilers play in software development, there is a dearth of tools for testing compilers for programmable network devices. We present Druzhba, a programmable switch simulator used for testing compilers targeting programmable packet-processing substrates. We show that we can model the low-level behavior of a switch's programmable hardware. We further show how our machine model can be used by compiler developers to target Druzhba as a compiler backend. Generated machine code programs are fed into Druzhba and tested using a fuzzing-based approach that allows compiler developers to test the correctness of their compilers. Using a program-synthesis-based compiler as a case study, we demonstrate how Druzhba has been successful in testing compiler-generated machine code for our simulated switch pipeline instruction set.

## 研究问题

Programmable switches have emerged as powerful and flexible alternatives to fixed-function forwarding devices. But because of the unique hardware constraints of network switches, the design and implementation of compilers targeting these devices is tedious and error prone. Despite the important role that compilers play in software development, there is a dearth of tools for testing compilers for programmable network devices. We present Druzhba, a programmable switch simulator used for testing compilers targeting programmable packet-processing substrates. We show that we can model the low-level behavior of a switch's programmable hardware. We further show how our machine model can be used by compiler developers to target Druzhba as a compiler backend. Generated machine code programs are fed into Druzhba and tested using a fuzzing-based approach that allows compiler developers to test the correctness of their compilers. Using a program-synthesis-based compiler as a case study, we demonstrate how Druzhba has been successful in testing compiler-generated machine code for our simulated switch pipeline instruction set.

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
