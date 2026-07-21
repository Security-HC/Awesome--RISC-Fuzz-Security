# LASA: Enhancing SoC Security Verification with LLM-Aided Property Generation

## 基本信息

- 作者：Dinesh Reddy Ankireddy、Sudipta Paria、Aritra Dasgupta、Sandip Ray、Swarup Bhunia
- 发表日期：2025-06-22
- 更新日期：2025-06-22
- 来源：arXiv
- 来源编号：2506.17865v1
- 研究类别：RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2506.17865v1](http://arxiv.org/abs/2506.17865v1)
- PDF：[https://arxiv.org/pdf/2506.17865v1](https://arxiv.org/pdf/2506.17865v1)
- 分析模式：仅元数据分析

## 摘要

Ensuring the security of modern System-on-Chip (SoC) designs poses significant challenges due to increasing complexity and distributed assets across the intellectual property (IP) blocks. Formal property verification (FPV) provides the capability to model and validate design behaviors through security properties with model checkers; however, current practices require significant manual efforts to create such properties, making them time-consuming, costly, and error-prone. The emergence of Large Language Models (LLMs) has showcased remarkable proficiency across diverse domains, including HDL code generation and verification tasks. Current LLM-based techniques often produce vacuous assertions and lack efficient prompt generation, comprehensive verification, and bug detection. This paper presents LASA, a novel framework that leverages LLMs and retrieval-augmented generation (RAG) to produce non-vacuous security properties and SystemVerilog Assertions (SVA) from design specifications and related documentation for bus-based SoC designs. LASA integrates commercial EDA tool for FPV to generate coverage metrics and iteratively refines prompts through a feedback loop to enhance coverage. The effectiveness of LASA is validated through various open-source SoC designs, demonstrating high coverage values with an average of ~88\%, denoting comprehensive verification through efficient generation of security properties and SVAs. LASA also demonstrates bug detection capabilities, identifying five unique bugs in the buggy OpenTitan SoC from Hack@DAC'24 competition.

## 研究问题

Ensuring the security of modern System-on-Chip (SoC) designs poses significant challenges due to increasing complexity and distributed assets across the intellectual property (IP) blocks. Formal property verification (FPV) provides the capability to model and validate design behaviors through security properties with model checkers; however, current practices require significant manual efforts to create such properties, making them time-consuming, costly, and error-prone. The emergence of Large Language Models (LLMs) has showcased remarkable proficiency across diverse domains, including HDL code generation and verification tasks. Current LLM-based techniques often produce vacuous assertions and lack efficient prompt generation, comprehensive verification, and bug detection. This paper presents LASA, a novel framework that leverages LLMs and retrieval-augmented generation (RAG) to produce non-vacuous security properties and SystemVerilog Assertions (SVA) from design specifications and related documentation for bus-based SoC designs. LASA integrates commercial EDA tool for FPV to generate coverage metrics and iteratively refines prompts through a feedback loop to enhance coverage. The effectiveness of LASA is validated through various open-source SoC designs, demonstrating high coverage values with an average of ~88\%, denoting comprehensive verification through efficient generation of security properties and SVAs. LASA also demonstrates bug detection capabilities, identifying five unique bugs in the buggy OpenTitan SoC from Hack@DAC'24 competition.

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
