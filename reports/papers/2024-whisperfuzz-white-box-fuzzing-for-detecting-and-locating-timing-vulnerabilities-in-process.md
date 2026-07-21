# WhisperFuzz: White-Box Fuzzing for Detecting and Locating Timing Vulnerabilities in Processors

## 基本信息

- 作者：Pallavi Borkar、Chen Chen、Mohamadreza Rostami、Nikhilesh Singh、Rahul Kande、Ahmad-Reza Sadeghi、Chester Rebeiro、Jeyavijayan Rajendran
- 发表日期：2024-02-06
- 更新日期：2024-03-14
- 来源：arXiv
- 来源编号：2402.03704v2
- 研究类别：RISC-V Fuzzing、Microarchitecture Security、RTL and Hardware Verification
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[http://arxiv.org/abs/2402.03704v2](http://arxiv.org/abs/2402.03704v2)
- PDF：[https://arxiv.org/pdf/2402.03704v2](https://arxiv.org/pdf/2402.03704v2)
- 分析模式：仅元数据分析

## 摘要

Timing vulnerabilities in processors have emerged as a potent threat. As processors are the foundation of any computing system, identifying these flaws is imperative. Recently fuzzing techniques, traditionally used for detecting software vulnerabilities, have shown promising results for uncovering vulnerabilities in large-scale hardware designs, such as processors. Researchers have adapted black-box or grey-box fuzzing to detect timing vulnerabilities in processors. However, they cannot identify the locations or root causes of these timing vulnerabilities, nor do they provide coverage feedback to enable the designer's confidence in the processor's security. To address the deficiencies of the existing fuzzers, we present WhisperFuzz--the first white-box fuzzer with static analysis--aiming to detect and locate timing vulnerabilities in processors and evaluate the coverage of microarchitectural timing behaviors. WhisperFuzz uses the fundamental nature of processors' timing behaviors, microarchitectural state transitions, to localize timing vulnerabilities. WhisperFuzz automatically extracts microarchitectural state transitions from a processor design at the register-transfer level (RTL) and instruments the design to monitor the state transitions as coverage. Moreover, WhisperFuzz measures the time a design-under-test (DUT) takes to process tests, identifying any minor, abnormal variations that may hint at a timing vulnerability. WhisperFuzz detects 12 new timing vulnerabilities across advanced open-sourced RISC-V processors: BOOM, Rocket Core, and CVA6. Eight of these violate the zero latency requirements of the Zkt extension and are considered serious security vulnerabilities. Moreover, WhisperFuzz also pinpoints the locations of the new and the existing vulnerabilities.

## 研究问题

Timing vulnerabilities in processors have emerged as a potent threat. As processors are the foundation of any computing system, identifying these flaws is imperative. Recently fuzzing techniques, traditionally used for detecting software vulnerabilities, have shown promising results for uncovering vulnerabilities in large-scale hardware designs, such as processors. Researchers have adapted black-box or grey-box fuzzing to detect timing vulnerabilities in processors. However, they cannot identify the locations or root causes of these timing vulnerabilities, nor do they provide coverage feedback to enable the designer's confidence in the processor's security. To address the deficiencies of the existing fuzzers, we present WhisperFuzz--the first white-box fuzzer with static analysis--aiming to detect and locate timing vulnerabilities in processors and evaluate the coverage of microarchitectural timing behaviors. WhisperFuzz uses the fundamental nature of processors' timing behaviors, microarchitectural state transitions, to localize timing vulnerabilities. WhisperFuzz automatically extracts microarchitectural state transitions from a processor design at the register-transfer level (RTL) and instruments the design to monitor the state transitions as coverage. Moreover, WhisperFuzz measures the time a design-under-test (DUT) takes to process tests, identifying any minor, abnormal variations that may hint at a timing vulnerability. WhisperFuzz detects 12 new timing vulnerabilities across advanced open-sourced RISC-V processors: BOOM, Rocket Core, and CVA6. Eight of these violate the zero latency requirements of the Zkt extension and are considered serious security vulnerabilities. Moreover, WhisperFuzz also pinpoints the locations of the new and the existing vulnerabilities.

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
