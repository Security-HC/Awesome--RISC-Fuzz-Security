# From CISC to RISC: language-model guided assembly transpilation

## 基本信息

- 作者：Ahmed Heakl、Chaimaa Abi、Rania Hossam、Abdulrahman Mahmoud
- 发表日期：2024-11-25
- 更新日期：2024-11-25
- 来源：arXiv
- 来源编号：2411.16341v1
- 研究类别：RISC-V Fuzzing 研究、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2411.16341v1](http://arxiv.org/abs/2411.16341v1)
- PDF：[https://arxiv.org/pdf/2411.16341v1](https://arxiv.org/pdf/2411.16341v1)
- 分析模式：仅元数据分析

## 摘要

The transition from x86 to ARM architecture is becoming increasingly common across various domains, primarily driven by ARM's energy efficiency and improved performance across traditional sectors. However, this ISA shift poses significant challenges, mainly due to the extensive legacy ecosystem of x86 software and lack of portability across proprietary ecosystems and software stacks. This paper introduces CRT, a lightweight LLM-based transpiler that automatically converts x86 assembly to ARM assembly. Our approach bridges the fundamental architectural gap between x86's CISC-based and ARM's RISC-based computing paradigms while preserving program semantics and optimizing performance. We evaluate CRT on diverse real-world applications, achieving 79.25% translation accuracy from x86 to ARMv5 on our comprehensive test suite, and an 88.68% accuracy from x86 to RISC-V. In practical deployments on Apple M2 hardware (ARMv8), our transpiled code achieves 1.73$\times$ speedup compared to Apple's Rosetta 2 virtualization engine, while delivering 2.41$\times$ memory efficiency and 1.47$\times$ better energy consumption. Through testing and analysis, we show that CRT successfully navigates the CISC/RISC divide and generates correctly executable RISC code despite machine ``language'' barriers. We release our code, models, training datasets, and benchmarks at: \url{https://ahmedheakl.github.io/asm2asm/}.

## 研究问题

The transition from x86 to ARM architecture is becoming increasingly common across various domains, primarily driven by ARM's energy efficiency and improved performance across traditional sectors. However, this ISA shift poses significant challenges, mainly due to the extensive legacy ecosystem of x86 software and lack of portability across proprietary ecosystems and software stacks. This paper introduces CRT, a lightweight LLM-based transpiler that automatically converts x86 assembly to ARM assembly. Our approach bridges the fundamental architectural gap between x86's CISC-based and ARM's RISC-based computing paradigms while preserving program semantics and optimizing performance. We evaluate CRT on diverse real-world applications, achieving 79.25% translation accuracy from x86 to ARMv5 on our comprehensive test suite, and an 88.68% accuracy from x86 to RISC-V. In practical deployments on Apple M2 hardware (ARMv8), our transpiled code achieves 1.73$\times$ speedup compared to Apple's Rosetta 2 virtualization engine, while delivering 2.41$\times$ memory efficiency and 1.47$\times$ better energy consumption. Through testing and analysis, we show that CRT successfully navigates the CISC/RISC divide and generates correctly executable RISC code despite machine ``language'' barriers. We release our code, models, training datasets, and benchmarks at: \url{https://ahmedheakl.github.io/asm2asm/}.

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
