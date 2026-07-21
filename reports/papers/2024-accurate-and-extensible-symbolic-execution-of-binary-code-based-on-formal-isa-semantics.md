# Accurate and Extensible Symbolic Execution of Binary Code based on Formal ISA Semantics

## 基本信息

- 作者：Sören Tempel、Tobias Brandt、Christoph Lüth、Christian Dietrich、Rolf Drechsler
- 发表日期：2024-04-05
- 更新日期：2025-01-20
- 来源：arXiv
- 来源编号：2404.04132v2
- 研究类别：RISC-V Fuzzing、RTL and Hardware Verification、Fuzzing Methodology
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2404.04132v2](http://arxiv.org/abs/2404.04132v2)
- PDF：[https://arxiv.org/pdf/2404.04132v2](https://arxiv.org/pdf/2404.04132v2)
- 分析模式：仅元数据分析

## 摘要

Symbolic execution is an SMT-based software verification and testing technique. Symbolic execution requires tracking performed computations during software simulation to reason about branches in the software under test. The prevailing approach on symbolic execution of binary code tracks computations by transforming the code to be tested to an architecture-independent IR and then symbolically executes this IR. However, the resulting IR must be semantically equivalent to the binary code, making this process complex and error-prone. The semantics of the binary code are specified by the targeted ISA, commonly given in natural language and requiring a manual implementation of the transformation to an IR. In recent years, the use of formal languages to describe ISA semantics in a machine-readable way has gained increased popularity. We investigate the utilization of such formal semantics for symbolic execution of binary code, achieving an accurate representation of instruction semantics. We present a prototype for the RISC-V ISA and conduct a case study to demonstrate that it can be easily extended to additional instructions. Furthermore, we perform an experimental comparison with prior work which resulted in the discovery of five previously unknown bugs in the ISA implementation of the popular IR-based symbolic executor angr.

## 研究问题

Symbolic execution is an SMT-based software verification and testing technique. Symbolic execution requires tracking performed computations during software simulation to reason about branches in the software under test. The prevailing approach on symbolic execution of binary code tracks computations by transforming the code to be tested to an architecture-independent IR and then symbolically executes this IR. However, the resulting IR must be semantically equivalent to the binary code, making this process complex and error-prone. The semantics of the binary code are specified by the targeted ISA, commonly given in natural language and requiring a manual implementation of the transformation to an IR. In recent years, the use of formal languages to describe ISA semantics in a machine-readable way has gained increased popularity. We investigate the utilization of such formal semantics for symbolic execution of binary code, achieving an accurate representation of instruction semantics. We present a prototype for the RISC-V ISA and conduct a case study to demonstrate that it can be easily extended to additional instructions. Furthermore, we perform an experimental comparison with prior work which resulted in the discovery of five previously unknown bugs in the ISA implementation of the popular IR-based symbolic executor angr.

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
