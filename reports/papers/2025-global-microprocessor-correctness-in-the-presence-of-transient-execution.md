# Global Microprocessor Correctness in the Presence of Transient Execution

## 基本信息

- 作者：Andrew T. Walter、Konstantinos Athanasiou、Panagiotis Manolios
- 发表日期：2025-06-20
- 更新日期：2025-06-20
- 来源：arXiv
- 来源编号：2506.17154v1
- 研究类别：RISC-V Fuzzing、Microarchitecture Security
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2506.17154v1](http://arxiv.org/abs/2506.17154v1)
- PDF：[https://arxiv.org/pdf/2506.17154v1](https://arxiv.org/pdf/2506.17154v1)
- 分析模式：仅元数据分析

## 摘要

Correctness for microprocessors is generally understood to be conformance with the associated instruction set architecture (ISA). This is the basis for one of the most important abstractions in computer science, allowing hardware designers to develop highly-optimized processors that are functionally "equivalent" to an ideal processor that executes instructions atomically. This specification is almost always informal, e.g., commercial microprocessors generally do not come with conformance specifications. In this paper, we advocate for the use of formal specifications, using the theory of refinement. We introduce notions of correctness that can be used to deal with transient execution attacks, including Meltdown and Spectre. Such attacks have shown that ubiquitous microprocessor optimizations, appearing in numerous processors for decades, are inherently buggy. Unlike alternative approaches that use non-interference properties, our notion of correctness is global, meaning it is single specification that: formalizes conformance, includes functional correctness and is parameterized by an microarchitecture. We introduce action skipping refinement, a new type of refinement and we describe how our notions of refinement can be decomposed into properties that are more amenable to automated verification using the the concept of shared-resource commitment refinement maps. We do this in the context of formal, fully executable bit- and cycle-accurate models of an ISA and a microprocessor. Finally, we show how light-weight formal methods based on property-based testing can be used to identify transient execution bugs.

## 研究问题

Correctness for microprocessors is generally understood to be conformance with the associated instruction set architecture (ISA). This is the basis for one of the most important abstractions in computer science, allowing hardware designers to develop highly-optimized processors that are functionally "equivalent" to an ideal processor that executes instructions atomically. This specification is almost always informal, e.g., commercial microprocessors generally do not come with conformance specifications. In this paper, we advocate for the use of formal specifications, using the theory of refinement. We introduce notions of correctness that can be used to deal with transient execution attacks, including Meltdown and Spectre. Such attacks have shown that ubiquitous microprocessor optimizations, appearing in numerous processors for decades, are inherently buggy. Unlike alternative approaches that use non-interference properties, our notion of correctness is global, meaning it is single specification that: formalizes conformance, includes functional correctness and is parameterized by an microarchitecture. We introduce action skipping refinement, a new type of refinement and we describe how our notions of refinement can be decomposed into properties that are more amenable to automated verification using the the concept of shared-resource commitment refinement maps. We do this in the context of formal, fully executable bit- and cycle-accurate models of an ISA and a microprocessor. Finally, we show how light-weight formal methods based on property-based testing can be used to identify transient execution bugs.

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
