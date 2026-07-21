# SimFuzz: Similarity-guided Block-level Mutation for RISC-V Processor Fuzzing

## 基本信息

- 作者：Hao Lyu、Jingzheng Wu、Xiang Ling、Yicheng Zhong、Zhiyuan Li、Tianyue Luo
- 发表日期：2026-01-17
- 更新日期：2026-01-17
- 来源：arXiv
- 来源编号：2601.11838v1
- 研究类别：RISC-V Fuzzing 研究、处理器与 CPU Fuzzing、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：5
- 论文页面：[http://arxiv.org/abs/2601.11838v1](http://arxiv.org/abs/2601.11838v1)
- PDF：[https://arxiv.org/pdf/2601.11838v1](https://arxiv.org/pdf/2601.11838v1)
- 分析模式：仅元数据分析

## 摘要

The Instruction Set Architecture (ISA) defines processor operations and serves as the interface between hardware and software. As an open ISA, RISC-V lowers the barriers to processor design and encourages widespread adoption, but also exposes processors to security risks such as functional bugs. Processor fuzzing is a powerful technique for automatically detecting these bugs. However, existing fuzzing methods suffer from two main limitations. First, their emphasis on redundant test case generation causes them to overlook cross-processor corner cases. Second, they rely too heavily on coverage guidance. Current coverage metrics are biased and inefficient, and become ineffective once coverage growth plateaus. To overcome these limitations, we propose SimFuzz, a fuzzing framework that constructs a high-quality seed corpus from historical bug-triggering inputs and employs similarity-guided, block-level mutation to efficiently explore the processor input space. By introducing instruction similarity, SimFuzz expands the input space around seeds while preserving control-flow structure, enabling deeper exploration without relying on coverage feedback. We evaluate SimFuzz on three widely used open-source RISC-V processors: Rocket, BOOM, and XiangShan, and discover 17 bugs in total, including 14 previously unknown issues, 7 of which have been assigned CVE identifiers. These bugs affect the decode and memory units, cause instruction and data errors, and can lead to kernel instability or system crashes. Experimental results show that SimFuzz achieves up to 73.22% multiplexer coverage on the high-quality seed corpus. Our findings highlight critical security bugs in mainstream RISC-V processors and offer actionable insights for improving functional verification.

## 研究问题

The Instruction Set Architecture (ISA) defines processor operations and serves as the interface between hardware and software. As an open ISA, RISC-V lowers the barriers to processor design and encourages widespread adoption, but also exposes processors to security risks such as functional bugs. Processor fuzzing is a powerful technique for automatically detecting these bugs. However, existing fuzzing methods suffer from two main limitations. First, their emphasis on redundant test case generation causes them to overlook cross-processor corner cases. Second, they rely too heavily on coverage guidance. Current coverage metrics are biased and inefficient, and become ineffective once coverage growth plateaus. To overcome these limitations, we propose SimFuzz, a fuzzing framework that constructs a high-quality seed corpus from historical bug-triggering inputs and employs similarity-guided, block-level mutation to efficiently explore the processor input space. By introducing instruction similarity, SimFuzz expands the input space around seeds while preserving control-flow structure, enabling deeper exploration without relying on coverage feedback. We evaluate SimFuzz on three widely used open-source RISC-V processors: Rocket, BOOM, and XiangShan, and discover 17 bugs in total, including 14 previously unknown issues, 7 of which have been assigned CVE identifiers. These bugs affect the decode and memory units, cause instruction and data errors, and can lead to kernel instability or system crashes. Experimental results show that SimFuzz achieves up to 73.22% multiplexer coverage on the high-quality seed corpus. Our findings highlight critical security bugs in mainstream RISC-V processors and offer actionable insights for improving functional verification.

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
