# Icicle: A Re-Designed Emulator for Grey-Box Firmware Fuzzing

## 基本信息

- 作者：Michael Chesser、Surya Nepal、Damith C. Ranasinghe
- 发表日期：2023-01-31
- 更新日期：2023-06-21
- 来源：arXiv
- 来源编号：2301.13346v2
- 研究类别：RISC-V Fuzzing、Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2301.13346v2](http://arxiv.org/abs/2301.13346v2)
- PDF：[https://arxiv.org/pdf/2301.13346v2](https://arxiv.org/pdf/2301.13346v2)
- 分析模式：仅元数据分析

## 摘要

Emulation-based fuzzers enable testing binaries without source code, and facilitate testing embedded applications where automated execution on the target hardware architecture is difficult and slow. The instrumentation techniques added to extract feedback and guide input mutations towards generating effective test cases is at the core of modern fuzzers. But, modern emulation-based fuzzers have evolved by re-purposing general-purpose emulators; consequently, developing and integrating fuzzing techniques, such as instrumentation methods, are difficult and often added in an ad-hoc manner, specific to an instruction set architecture (ISA). This limits state-of-the-art fuzzing techniques to few ISAs such as x86/x86-64 or ARM/AArch64; a significant problem for firmware fuzzing of diverse ISAs. This study presents our efforts to re-think emulation for fuzzing. We design and implement a fuzzing-specific, multi-architecture emulation framework -- Icicle. We demonstrate the capability to add instrumentation once, in an architecture agnostic manner, with low execution overhead. We employ Icicle as the emulator for a state-of-the-art ARM firmware fuzzer -- Fuzzware -- and replicate results. Significantly, we demonstrate the availability of new instrumentation in Icicle enabled the discovery of new bugs. We demonstrate the fidelity of Icicle and efficacy of architecture agnostic instrumentation by discovering LAVA-M benchmark bugs, requiring a known and specific operational capability of instrumentation techniques, across a diverse set of instruction set architectures (x86-64, ARM/AArch64, RISC-V, MIPS). Further, to demonstrate the effectiveness of Icicle to discover bugs in a currently unsupported architecture in emulation-based fuzzers, we perform a fuzzing campaign with real-world MSP430 firmware binaries and discovered 7 new bugs.

## 研究问题

Emulation-based fuzzers enable testing binaries without source code, and facilitate testing embedded applications where automated execution on the target hardware architecture is difficult and slow. The instrumentation techniques added to extract feedback and guide input mutations towards generating effective test cases is at the core of modern fuzzers. But, modern emulation-based fuzzers have evolved by re-purposing general-purpose emulators; consequently, developing and integrating fuzzing techniques, such as instrumentation methods, are difficult and often added in an ad-hoc manner, specific to an instruction set architecture (ISA). This limits state-of-the-art fuzzing techniques to few ISAs such as x86/x86-64 or ARM/AArch64; a significant problem for firmware fuzzing of diverse ISAs. This study presents our efforts to re-think emulation for fuzzing. We design and implement a fuzzing-specific, multi-architecture emulation framework -- Icicle. We demonstrate the capability to add instrumentation once, in an architecture agnostic manner, with low execution overhead. We employ Icicle as the emulator for a state-of-the-art ARM firmware fuzzer -- Fuzzware -- and replicate results. Significantly, we demonstrate the availability of new instrumentation in Icicle enabled the discovery of new bugs. We demonstrate the fidelity of Icicle and efficacy of architecture agnostic instrumentation by discovering LAVA-M benchmark bugs, requiring a known and specific operational capability of instrumentation techniques, across a diverse set of instruction set architectures (x86-64, ARM/AArch64, RISC-V, MIPS). Further, to demonstrate the effectiveness of Icicle to discover bugs in a currently unsupported architecture in emulation-based fuzzers, we perform a fuzzing campaign with real-world MSP430 firmware binaries and discovered 7 new bugs.

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
