# WhisperFuzz: White-Box Fuzzing for Detecting and Locating Timing Vulnerabilities in Processors

## 基本信息

- 作者：Pallavi Borkar、Chen Chen、Mohamadreza Rostami、Nikhilesh Singh、Rahul Kande、Ahmad-Reza Sadeghi、Chester Rebeiro、Jeyavijayan Rajendran
- 发表日期：2024-02-06
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、Microarchitectural Security Testing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2402.03704v2](http://arxiv.org/abs/2402.03704v2)
- PDF：[https://arxiv.org/pdf/2402.03704v2](https://arxiv.org/pdf/2402.03704v2)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Timing vulnerabilities in processors have emerged as a potent threat. As processors are the foundation of any computing system, identifying these flaws is imperative. Recently fuzzing techniques, traditionally used for detecting software vulnerabilities, have shown promising results for uncovering vulnerabilities in large-scale hardware designs, such as processors. Researchers have adapted black-box or grey-box fuzzing to detect timing vulnerabilities in processors. However, they cannot identify the locations or root causes of these timing vulnerabilities, nor do they provide coverage feedback to enable the designer's confidence in the processor's security. To address the deficiencies of the existing fuzzers, we present WhisperFuzz--the first white-box fuzzer with static analysis--aiming to detect and locate timing vulnerabilities in processors and evaluate the coverage of microarchitectural timing behaviors. WhisperFuzz uses the fundamental nature of processors' timing behaviors, microarchitectural state transitions, to localize timing vulnerabilities. WhisperFuzz automatically extracts microarchitectural state transitions from a processor design at the register-transfer level (RTL) and instruments the design to monitor the state transitions as coverage. Moreover, WhisperFuzz measures the time a design-under-test (DUT) takes to process tests, identifying any minor, abnormal variations that may hint at a timing vulnerability. WhisperFuzz detects 12 new timing vulnerabilities across advanced open-sourced RISC-V processors: BOOM, Rocket Core, and CVA6. Eight of these violate the zero latency requirements of the Zkt extension and are considered serious security vulnerabilities. Moreover, WhisperFuzz also pinpoints the locations of the new and the existing vulnerabilities.

## 研究问题

摘要级初步判断（未核验正文）：Timing vulnerabilities in processors have emerged as a potent threat. As processors are the foundation of any computing system, identifying these flaws is imperative. Recently fuzzing techniques, traditionally used for detecting software vulnerabilities, have shown promising results for uncovering vulnerabilities in large-scale hardware designs, such as processors. Researchers have adapted black-box or grey-box fuzzing to detect timing vulnerabilities in processors. However, they cannot identify the locations or root causes of these timing vulnerabilities, nor do they provide coverage feedback to enable the designer's confidence in the processor's security. To address the deficiencies of the existing fuzzers, we present WhisperFuzz--the first white-box fuzzer with static analysis--aiming to detect and locate timing vulnerabilities in processors and evaluate the coverage of microarchitectural timing behaviors. WhisperFuzz uses the fundamental nature of processors' timing behaviors, microarchitectural state transitions, to localize timing vulnerabilities. WhisperFuzz automatically extracts microarchitectural state transitions from a processor design at the register-transfer level (RTL) and instruments the design to monitor the state transitions as coverage. Moreover, WhisperFuzz measures the time a design-under-test (DUT) takes to process tests, identifying any minor, abnormal variations that may hint at a timing vulnerability. WhisperFuzz detects 12 new timing vulnerabilities across advanced open-sourced RISC-V processors: BOOM, Rocket Core, and CVA6. Eight of these violate the zero latency requirements of the Zkt extension and are considered serious security vulnerabilities. Moreover, WhisperFuzz also pinpoints the locations of the new and the existing vulnerabilities.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《WhisperFuzz: White-Box Fuzzing for Detecting and Locating Timing Vulnerabilities in Processors》，初步归入“RISC-V Processor Fuzzing”。

## 与本仓库研究主线的关系

该条目已通过自动相关性筛选，但尚未完成人工或全文级核验。

## 结论

尚未核验正文，因此不对论文最终结论作确定性概括。

## 局限性

尚未核验正文。至少需要检查方法是否只适用于特定 ISA、处理器、协议、仿真器或人工模板，以及实验是否存在目标泄漏和基线不公平。

## 详细阅读分析

优先阅读 Introduction、Background/Threat Model、Method、Evaluation、Limitations/Discussion，并核对官方论文页、DOI、Artifact 和代码仓库。

## 后续核验问题

- 论文的在线反馈信号和最终 Oracle 分别是什么？
- 实验是否包含公平的 random、通用 RTL coverage 和领域专用 coverage 基线？
- 论文是否提供开源 Artifact、真实漏洞、CVE 或可复现 PoC？
