# Fuzzing Hardware Like Software

## 基本信息

- 作者：Timothy Trippel、K. Shin、A. Chernyakhovsky、Garret Kelly、Dominic Rizzo、Matthew Hicks
- 发表日期：2021-02-03
- 更新日期：2021-02-03
- 来源：arXiv
- 来源编号：2102.02308v1
- 研究类别：RTL 与硬件验证
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[https://www.semanticscholar.org/paper/de7eff32b91ab9c2a73077e5e7258a3877ffcb94](https://www.semanticscholar.org/paper/de7eff32b91ab9c2a73077e5e7258a3877ffcb94)
- PDF：[https://arxiv.org/pdf/2102.02308v1](https://arxiv.org/pdf/2102.02308v1)
- 分析模式：仅元数据分析

## 摘要

Hardware flaws are permanent and potent: hardware cannot be patched once fabricated, and any flaws may undermine any software executing on top. Consequently, verification time dominates implementation time. The gold standard in hardware Design Verification (DV) is concentrated at two extremes: random dynamic verification and formal verification. Both struggle to root out the subtle flaws in complex hardware that often manifest as security vulnerabilities. The root problem with random verification is its undirected nature, making it inefficient, while formal verification is constrained by the state-space explosion problem, making it infeasible against complex designs. What is needed is a solution that is directed, yet under-constrained. Instead of making incremental improvements to existing DV approaches, we leverage the observation that existing software fuzzers already provide such a solution, and adapt them for hardware DV. Specifically, we translate RTL hardware to a software model and fuzz that model. The central challenge we address is how best to mitigate the differences between the hardware execution model and software execution model. This includes: 1) how to represent test cases, 2) what is the hardware equivalent of a crash, 3) what is an appropriate coverage metric, and 4) how to create a general-purpose fuzzing harness for hardware. To evaluate our approach, we fuzz four IP blocks from Google's OpenTitan SoC. Our experiments reveal a two orders-of-magnitude reduction in run time to achieve Finite State Machine (FSM) coverage over traditional dynamic verification schemes. Moreover, with our design-agnostic harness, we achieve over 88% HDL line coverage in three out of four of our designs -- even without any initial seeds.

## 研究问题

Hardware flaws are permanent and potent: hardware cannot be patched once fabricated, and any flaws may undermine any software executing on top. Consequently, verification time dominates implementation time. The gold standard in hardware Design Verification (DV) is concentrated at two extremes: random dynamic verification and formal verification. Both struggle to root out the subtle flaws in complex hardware that often manifest as security vulnerabilities. The root problem with random verification is its undirected nature, making it inefficient, while formal verification is constrained by the state-space explosion problem, making it infeasible against complex designs. What is needed is a solution that is directed, yet under-constrained. Instead of making incremental improvements to existing DV approaches, we leverage the observation that existing software fuzzers already provide such a solution, and adapt them for hardware DV. Specifically, we translate RTL hardware to a software model and fuzz that model. The central challenge we address is how best to mitigate the differences between the hardware execution model and software execution model. This includes: 1) how to represent test cases, 2) what is the hardware equivalent of a crash, 3) what is an appropriate coverage metric, and 4) how to create a general-purpose fuzzing harness for hardware. To evaluate our approach, we fuzz four IP blocks from Google's OpenTitan SoC. Our experiments reveal a two orders-of-magnitude reduction in run time to achieve Finite State Machine (FSM) coverage over traditional dynamic verification schemes. Moreover, with our design-agnostic harness, we achieve over 88% HDL line coverage in three out of four of our designs -- even without any initial seeds.

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
