# Deterministic Fully-Static Whole-Binary Translation without Heuristics

## 基本信息

- 作者：Hongyu Chen、James McGowan、Michael Franz
- 发表日期：2026-05-08
- 更新日期：2026-05-13
- 来源：arXiv
- 来源编号：2605.08419v2
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2605.08419v2](http://arxiv.org/abs/2605.08419v2)
- PDF：[https://arxiv.org/pdf/2605.08419v2](https://arxiv.org/pdf/2605.08419v2)
- 分析模式：仅元数据分析

## 摘要

We present Elevator, the first binary translator that statically translates entire x86-64 executables to AArch64 without debug information, source code, or assumptions about code layout. Unlike existing systems, which rely on heuristics or runtime fallbacks to handle code-versus-data decoding errors, Elevator considers all possible interpretations of every byte and produces a separate translation for each feasible one ahead of time. Any byte may be interpreted as data, an opcode, or an opcode argument; we generate separate control flow paths for all interpretations, pruning only those leading to abnormal termination. Translations are built by composing code "tiles" automatically derived from a high-level description of the source ISA, yielding a nimble translation framework. The approach is deterministic and produces complete, self-contained binaries with no runtime component in the trusted code base. The principal cost is substantial code size expansion. The key benefit is that the output is the actual code that will run, enabling testing, validation, certification, and cryptographic signing prior to deployment, reducing risk compared to emulators or JIT compilers. We evaluate Elevator on a diverse corpus of real-world binaries, including the entire SPECint 2006 suite, demonstrating that static full-program binary translation can be both reliable and practical. Elevator achieves performance on par with or better than QEMU's user-mode JIT emulation.

## 研究问题

We present Elevator, the first binary translator that statically translates entire x86-64 executables to AArch64 without debug information, source code, or assumptions about code layout. Unlike existing systems, which rely on heuristics or runtime fallbacks to handle code-versus-data decoding errors, Elevator considers all possible interpretations of every byte and produces a separate translation for each feasible one ahead of time. Any byte may be interpreted as data, an opcode, or an opcode argument; we generate separate control flow paths for all interpretations, pruning only those leading to abnormal termination. Translations are built by composing code "tiles" automatically derived from a high-level description of the source ISA, yielding a nimble translation framework. The approach is deterministic and produces complete, self-contained binaries with no runtime component in the trusted code base. The principal cost is substantial code size expansion. The key benefit is that the output is the actual code that will run, enabling testing, validation, certification, and cryptographic signing prior to deployment, reducing risk compared to emulators or JIT compilers. We evaluate Elevator on a diverse corpus of real-world binaries, including the entire SPECint 2006 suite, demonstrating that static full-program binary translation can be both reliable and practical. Elevator achieves performance on par with or better than QEMU's user-mode JIT emulation.

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
