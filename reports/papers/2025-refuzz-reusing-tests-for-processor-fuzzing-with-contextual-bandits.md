# ReFuzz: Reusing Tests for Processor Fuzzing with Contextual Bandits

## 基本信息

- 作者：Chen Chen、Zaiyan Xu、Mohamadreza Rostami、David Liu、Dileep Kalathil、Ahmad-Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2025-12-04
- 更新日期：2025-12-08
- 来源：arXiv
- 来源编号：2512.04436v2
- 研究类别：Processor and CPU Fuzzing、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：3
- 论文页面：[http://arxiv.org/abs/2512.04436v2](http://arxiv.org/abs/2512.04436v2)
- PDF：[https://arxiv.org/pdf/2512.04436v2](https://arxiv.org/pdf/2512.04436v2)
- 分析模式：仅元数据分析

## 摘要

Processor designs rely on iterative modifications and reuse well-established designs. However, this reuse of prior designs also leads to similar vulnerabilities across multiple processors. As processors grow increasingly complex with iterative modifications, efficiently detecting vulnerabilities from modern processors is critical. Inspired by software fuzzing, hardware fuzzing has recently demonstrated its effectiveness in detecting processor vulnerabilities. Yet, to our best knowledge, existing processor fuzzers fuzz each design individually, lacking the capability to understand known vulnerabilities in prior processors to fine-tune fuzzing to identify similar or new variants of vulnerabilities. To address this gap, we present ReFuzz, an adaptive fuzzing framework that leverages contextual bandit to reuse highly effective tests from prior processors to fuzz a processor-under-test (PUT) within a given ISA. By intelligently mutating tests that trigger vulnerabilities in prior processors, ReFuzz effectively detects similar and new variants of vulnerabilities in PUTs. ReFuzz uncovered three new security vulnerabilities and two new functional bugs. ReFuzz detected one vulnerability by reusing a test that triggers a known vulnerability in a prior processor. One functional bug exists across three processors that share design modules. The second bug has two variants. Additionally, ReFuzz reuses highly effective tests to enhance efficiency in coverage, achieving an average 511.23x coverage speedup and up to 9.33% more total coverage, compared to existing fuzzers.

## 研究问题

Processor designs rely on iterative modifications and reuse well-established designs. However, this reuse of prior designs also leads to similar vulnerabilities across multiple processors. As processors grow increasingly complex with iterative modifications, efficiently detecting vulnerabilities from modern processors is critical. Inspired by software fuzzing, hardware fuzzing has recently demonstrated its effectiveness in detecting processor vulnerabilities. Yet, to our best knowledge, existing processor fuzzers fuzz each design individually, lacking the capability to understand known vulnerabilities in prior processors to fine-tune fuzzing to identify similar or new variants of vulnerabilities. To address this gap, we present ReFuzz, an adaptive fuzzing framework that leverages contextual bandit to reuse highly effective tests from prior processors to fuzz a processor-under-test (PUT) within a given ISA. By intelligently mutating tests that trigger vulnerabilities in prior processors, ReFuzz effectively detects similar and new variants of vulnerabilities in PUTs. ReFuzz uncovered three new security vulnerabilities and two new functional bugs. ReFuzz detected one vulnerability by reusing a test that triggers a known vulnerability in a prior processor. One functional bug exists across three processors that share design modules. The second bug has two variants. Additionally, ReFuzz reuses highly effective tests to enhance efficiency in coverage, achieving an average 511.23x coverage speedup and up to 9.33% more total coverage, compared to existing fuzzers.

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
