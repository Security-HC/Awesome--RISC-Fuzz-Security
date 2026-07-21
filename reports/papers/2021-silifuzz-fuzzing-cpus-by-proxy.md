# SiliFuzz: Fuzzing CPUs by proxy

## 基本信息

- 作者：Kostya Serebryany、Maxim Lifantsev、Konstantin Shtoyk、Doug Kwan、Peter Hochschild
- 发表日期：2021-10-05
- 更新日期：2021-10-05
- 来源：arXiv
- 来源编号：2110.11519v1
- 研究类别：RTL and Hardware Verification
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2110.11519v1](http://arxiv.org/abs/2110.11519v1)
- PDF：[https://arxiv.org/pdf/2110.11519v1](https://arxiv.org/pdf/2110.11519v1)
- 分析模式：仅元数据分析

## 摘要

CPUs are becoming more complex with every generation, at both the logical and the physical levels. This potentially leads to more logic bugs and electrical defects in CPUs being overlooked during testing, which causes data corruption or other undesirable effects when these CPUs are used in production. These ever-present problems may also have simply become more evident as more CPUs are operated and monitored by large cloud providers. If the RTL ("source code") of a CPU were available, we could apply greybox fuzzing to the CPU model almost as we do to any other software [arXiv:2102.02308]. However our targets are general purpose x86_64 CPUs produced by third parties, where we do not have the RTL design, so in our case CPU implementations are opaque. Moreover, we are more interested in electrical defects as opposed to logic bugs. We present SiliFuzz, a work-in-progress system that finds CPU defects by fuzzing software proxies, like CPU simulators or disassemblers, and then executing the accumulated test inputs (known as the corpus) on actual CPUs on a large scale. The major difference between this work and traditional software fuzzing is that a software bug fixed once will be fixed for all installations of the software, while for CPU defects we have to test every individual core repeatedly over its lifetime due to wear and tear. In this paper we also analyze four groups of CPU defects that SiliFuzz has uncovered and describe patterns shared by other SiliFuzz findings.

## 研究问题

CPUs are becoming more complex with every generation, at both the logical and the physical levels. This potentially leads to more logic bugs and electrical defects in CPUs being overlooked during testing, which causes data corruption or other undesirable effects when these CPUs are used in production. These ever-present problems may also have simply become more evident as more CPUs are operated and monitored by large cloud providers. If the RTL ("source code") of a CPU were available, we could apply greybox fuzzing to the CPU model almost as we do to any other software [arXiv:2102.02308]. However our targets are general purpose x86_64 CPUs produced by third parties, where we do not have the RTL design, so in our case CPU implementations are opaque. Moreover, we are more interested in electrical defects as opposed to logic bugs. We present SiliFuzz, a work-in-progress system that finds CPU defects by fuzzing software proxies, like CPU simulators or disassemblers, and then executing the accumulated test inputs (known as the corpus) on actual CPUs on a large scale. The major difference between this work and traditional software fuzzing is that a software bug fixed once will be fixed for all installations of the software, while for CPU defects we have to test every individual core repeatedly over its lifetime due to wear and tear. In this paper we also analyze four groups of CPU defects that SiliFuzz has uncovered and describe patterns shared by other SiliFuzz findings.

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
