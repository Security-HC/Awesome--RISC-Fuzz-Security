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
- 分析模式：中文元数据分析

## 摘要

Memory safety is a critical issue in embedded systems. Although high-level languages like MicroPython simplify IoT development, their C-based runtimes remain vulnerable to memory errors triggered by Python code or native extensions. The CHERI (Capability Hardware Enhanced RISC Instructions) architecture offers hardware-enforced memory safety, but its effectiveness for exposing latent bugs in real-world interpreters has not yet been fully explored. We present diffCHERI:FruitFly, a novel differential testing framework for systematically uncovering memory defects in MicroPython across conventional (x86/ARM) and CHERI-enabled (Arm Morello) platforms. We mine historic vulnerabilities from diverse Python runtimes to extract recurring stress patterns, then use a large language model to generate new test programs, and apply Concrete Syntax Tree (CST) mutation to diversify inputs.

## 研究问题

Memory safety is a critical issue in embedded systems. Although high-level languages like MicroPython simplify IoT development, their C-based runtimes remain vulnerable to memory errors triggered by Python code or native extensions. The CHERI (Capability Hardware Enhanced RISC Instructions) architecture offers hardware-enforced memory safety, but its effectiveness for exposing latent bugs in real-world interpreters has not yet been fully explored. We present diffCHERI:FruitFly, a novel differential testing framework for systematically uncovering memory defects in MicroPython across conventional (x86/ARM) and CHERI-enabled (Arm Morello) platforms. We mine historic vulnerabilities from diverse Python runtimes to extract recurring stress patterns, then use a large language model to generate new test programs, and apply Concrete Syntax Tree (CST) mutation to diversify inputs.

## Introduction 梳理

该记录基于题名、摘要和元数据生成。论文来源为 未记录，当前分类为 RISC-V Fuzzing、Processor and CPU Fuzzing、Microarchitecture Security、Fuzzing Methodology、Tools and Benchmarks。从命中查询看，论文与 OpenAlex: ISA testing fuzzing；OpenAlex: RISC-V hardware fuzzing；OpenAlex: RISC-V processor fuzzing 相关。Introduction 部分应重点关注作者如何定义处理器/微架构/硬件 fuzzing 的验证缺口、现有方法的不足，以及本文声称的核心贡献。

## 方法

当前未进行 PDF 正文解析。可从摘要初步判断其方法线索；正式阅读时应提取 fuzz 输入生成策略、变异方式、覆盖率或反馈信号、oracle/差分对象、测试平台以及是否依赖仿真器、RTL 或真实硬件。

## 实验与评估

当前未进行 PDF 正文解析。后续应补充实验对象、baseline、发现 bug 数量、覆盖率提升、运行开销、复现条件和 artifact 可用性。

## 结论

当前结论基于摘要和元数据生成：该论文可能围绕处理器安全验证、fuzzing 效率、微架构漏洞发现或硬件测试自动化展开。需要结合正文确认作者最终证明的效果和适用边界。

## 局限性

当前未进行 PDF 正文解析。初步阅读时应重点检查：是否只覆盖特定 ISA/处理器/仿真器，是否依赖人工规则或特定 oracle，是否难以迁移到 RISC-V，是否缺少真实硬件验证，以及实验是否只在有限 benchmark 上成立。

## 详细阅读分析

元数据主题：Computer science、Fuzz testing、Programming language、Differential (mechanical device)、Interpreter、Code (set theory)、Frame (networking)、Memory safety、Encoding (memory)、Artificial intelligence、Semantics (computer science)、Key (lock)。建议优先阅读 Introduction、Threat Model/Background、Method、Evaluation 和 Discussion。如果该论文与 RISC-V 或处理器 fuzzing 强相关，应进一步记录其可复用的测试生成思路、覆盖率指标、oracle 设计和开源实现。

## 后续跟进问题

- 论文是否提供开源实现或实验 artifact？
- 方法是否可以迁移到 RISC-V core、RTL 仿真器或真实处理器？
- 论文依赖什么 oracle、覆盖率指标或差分测试对象？
