# PowerFuzz: Power-Based Black-Box Firmware Fuzzing

## 基本信息

- 作者：Dakshina Tharindu、Sahan Sanjaya、Philip Baptist、Prabhat Mishra
- 发表日期：2026-06-23
- 更新日期：2026-06-23
- 来源：arXiv
- 来源编号：2606.24692v1
- 研究类别：RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2606.24692v1](http://arxiv.org/abs/2606.24692v1)
- PDF：[https://arxiv.org/pdf/2606.24692v1](https://arxiv.org/pdf/2606.24692v1)
- 分析模式：仅元数据分析

## 摘要

Fuzzing is widely used for software and hardware verification, offering an effective alternative to random testing. While gray-box fuzzers benefit from full visibility into the system under test and can leverage execution feedback such as branch coverage, these approaches are not applicable when verifying systems whose firmware or binaries are not publicly available. In such scenarios, obtaining coverage information for guiding the fuzzer becomes infeasible. In this paper, we introduce PowerFuzz, a statistical black-box fuzzing framework that leverages power side-channel measurements as a substitute for binary instrumentation, requiring no internal visibility into the target firmware. A central challenge in black-box firmware fuzzing is determining the executed branches during test execution. To address this challenge, we use power traces to identify branches utilizing a sliding window followed by a growing window full-trace correlation method. This approach also enables the construction of a high-level control-flow graph of the black-box firmware, which we utilize to drive the fuzzer to unexplored execution paths. Extensive evaluation using three embedded hardware platforms and ten firmware benchmarks demonstrates that PowerFuzz can provide branch coverage comparable (within 13.5%) to gray-box fuzzers while significantly outperforming (up to 22%) state-of-the-art black-box fuzzers.

## 研究问题

Fuzzing is widely used for software and hardware verification, offering an effective alternative to random testing. While gray-box fuzzers benefit from full visibility into the system under test and can leverage execution feedback such as branch coverage, these approaches are not applicable when verifying systems whose firmware or binaries are not publicly available. In such scenarios, obtaining coverage information for guiding the fuzzer becomes infeasible. In this paper, we introduce PowerFuzz, a statistical black-box fuzzing framework that leverages power side-channel measurements as a substitute for binary instrumentation, requiring no internal visibility into the target firmware. A central challenge in black-box firmware fuzzing is determining the executed branches during test execution. To address this challenge, we use power traces to identify branches utilizing a sliding window followed by a growing window full-trace correlation method. This approach also enables the construction of a high-level control-flow graph of the black-box firmware, which we utilize to drive the fuzzer to unexplored execution paths. Extensive evaluation using three embedded hardware platforms and ten firmware benchmarks demonstrates that PowerFuzz can provide branch coverage comparable (within 13.5%) to gray-box fuzzers while significantly outperforming (up to 22%) state-of-the-art black-box fuzzers.

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
