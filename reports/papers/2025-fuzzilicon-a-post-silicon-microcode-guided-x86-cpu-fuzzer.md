# Fuzzilicon: A Post-Silicon Microcode-Guided x86 CPU Fuzzer

## 基本信息

- 作者：Johannes Lenzen、Mohamadreza Rostami、Lichao Wu、Ahmad-Reza Sadeghi
- 发表日期：2025-12-29
- 更新日期：2025-12-29
- 来源：arXiv
- 来源编号：2512.23438v1
- 研究类别：Processor and CPU Fuzzing、Microarchitecture Security、RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[http://arxiv.org/abs/2512.23438v1](http://arxiv.org/abs/2512.23438v1)
- PDF：[https://arxiv.org/pdf/2512.23438v1](https://arxiv.org/pdf/2512.23438v1)
- 分析模式：仅元数据分析

## 摘要

Modern CPUs are black boxes, proprietary, and increasingly characterized by sophisticated microarchitectural flaws that evade traditional analysis. While some of these critical vulnerabilities have been uncovered through cumbersome manual effort, building an automated and systematic vulnerability detection framework for real-world post-silicon processors remains a challenge. In this paper, we present Fuzzilicon, the first post-silicon fuzzing framework for real-world x86 CPUs that brings deep introspection into the microcode and microarchitectural layers. Fuzzilicon automates the discovery of vulnerabilities that were previously only detectable through extensive manual reverse engineering, and bridges the visibility gap by introducing microcode-level instrumentation. At the core of Fuzzilicon is a novel technique for extracting feedback directly from the processor's microarchitecture, enabled by reverse-engineering Intel's proprietary microcode update interface. We develop a minimally intrusive instrumentation method and integrate it with a hypervisor-based fuzzing harness to enable precise, feedback-guided input generation, without access to Register Transfer Level (RTL). Applied to Intel's Goldmont microarchitecture, Fuzzilicon introduces 5 significant findings, including two previously unknown microcode-level speculative-execution vulnerabilities. Besides, the Fuzzilicon framework automatically rediscover the $μ$Spectre class of vulnerabilities, which were detected manually in the previous work. Fuzzilicon reduces coverage collection overhead by up to 31$\times$ compared to baseline techniques and achieves 16.27% unique microcode coverage of hookable locations, the first empirical baseline of its kind. As a practical, coverage-guided, and scalable approach to post-silicon fuzzing, Fuzzilicon establishes a new foundation to automate the discovery of complex CPU vulnerabilities.

## 研究问题

Modern CPUs are black boxes, proprietary, and increasingly characterized by sophisticated microarchitectural flaws that evade traditional analysis. While some of these critical vulnerabilities have been uncovered through cumbersome manual effort, building an automated and systematic vulnerability detection framework for real-world post-silicon processors remains a challenge. In this paper, we present Fuzzilicon, the first post-silicon fuzzing framework for real-world x86 CPUs that brings deep introspection into the microcode and microarchitectural layers. Fuzzilicon automates the discovery of vulnerabilities that were previously only detectable through extensive manual reverse engineering, and bridges the visibility gap by introducing microcode-level instrumentation. At the core of Fuzzilicon is a novel technique for extracting feedback directly from the processor's microarchitecture, enabled by reverse-engineering Intel's proprietary microcode update interface. We develop a minimally intrusive instrumentation method and integrate it with a hypervisor-based fuzzing harness to enable precise, feedback-guided input generation, without access to Register Transfer Level (RTL). Applied to Intel's Goldmont microarchitecture, Fuzzilicon introduces 5 significant findings, including two previously unknown microcode-level speculative-execution vulnerabilities. Besides, the Fuzzilicon framework automatically rediscover the $μ$Spectre class of vulnerabilities, which were detected manually in the previous work. Fuzzilicon reduces coverage collection overhead by up to 31$\times$ compared to baseline techniques and achieves 16.27% unique microcode coverage of hookable locations, the first empirical baseline of its kind. As a practical, coverage-guided, and scalable approach to post-silicon fuzzing, Fuzzilicon establishes a new foundation to automate the discovery of complex CPU vulnerabilities.

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
