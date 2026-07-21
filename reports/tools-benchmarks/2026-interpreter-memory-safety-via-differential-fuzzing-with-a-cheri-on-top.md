# Interpreter Memory Safety via Differential Fuzzing with a CHERI on Top

## 基本信息

- 作者：Kai Feng、Huanting Wang、Jeremy Singer、Zheng Wang
- 发表日期：2026-06-11
- 更新日期：2026-07-14
- 来源：OpenAlex
- 来源编号：https://openalex.org/W7164318503
- 研究类别：RISC-V Fuzzing 研究、处理器与 CPU Fuzzing、微架构安全、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[https://doi.org/10.1145/3814942.3816133](https://doi.org/10.1145/3814942.3816133)
- PDF：[https://doi.org/10.1145/3814942.3816133](https://doi.org/10.1145/3814942.3816133)
- 分析模式：仅元数据分析

## 摘要

Memory safety is a critical issue in embedded systems. Although high-level languages like MicroPython simplify IoT development, their C-based runtimes remain vulnerable to memory errors triggered by Python code or native extensions. The CHERI (Capability Hardware Enhanced RISC Instructions) architecture offers hardware-enforced memory safety, but its effectiveness for exposing latent bugs in real-world interpreters has not yet been fully explored. We present diffCHERI:FruitFly, a novel differential testing framework for systematically uncovering memory defects in MicroPython across conventional (x86/ARM) and CHERI-enabled (Arm Morello) platforms. We mine historic vulnerabilities from diverse Python runtimes to extract recurring stress patterns, then use a large language model to generate new test programs, and apply Concrete Syntax Tree (CST) mutation to diversify inputs.

## 研究问题

Memory safety is a critical issue in embedded systems. Although high-level languages like MicroPython simplify IoT development, their C-based runtimes remain vulnerable to memory errors triggered by Python code or native extensions. The CHERI (Capability Hardware Enhanced RISC Instructions) architecture offers hardware-enforced memory safety, but its effectiveness for exposing latent bugs in real-world interpreters has not yet been fully explored. We present diffCHERI:FruitFly, a novel differential testing framework for systematically uncovering memory defects in MicroPython across conventional (x86/ARM) and CHERI-enabled (Arm Morello) platforms. We mine historic vulnerabilities from diverse Python runtimes to extract recurring stress patterns, then use a large language model to generate new test programs, and apply Concrete Syntax Tree (CST) mutation to diversify inputs.

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
