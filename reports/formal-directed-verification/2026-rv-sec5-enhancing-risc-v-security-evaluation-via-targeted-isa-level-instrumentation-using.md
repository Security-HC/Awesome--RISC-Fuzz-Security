# RV-Sec5: Enhancing RISC-V Security Evaluation via Targeted ISA-Level Instrumentation using gem5

## 基本信息

- 作者：Muhammad Awais、Maria Mushtaq、Lirida Naviner、Florent Bruguier、Jawad Haj Yahya
- 发表日期：2026-02-11
- 会议/期刊：未记录
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: risc-v, microarchitectural；verification/fuzzing method: validation；security relevance: security
- 论文页面：[https://doi.org/10.1145/3793638.3793640](https://doi.org/10.1145/3793638.3793640)
- PDF：[https://doi.org/10.1145/3793638.3793640](https://doi.org/10.1145/3793638.3793640)
- 分析模式：摘要级占位（未全文核验）

## 摘要

The modularity of the RISC-V Instruction Set Architecture (ISA) has accelerated its adoption in security-critical domains, yet it introduces significant challenges for pre-silicon security validation. Current evaluation methods often rely on high-level emulation that overlooks microarchitectural side effects or post-silicon testing that identifies vulnerabilities too late in the design cycle. This paper presents RV-Sec5, a systematic framework for ISA-level security evaluation that leverages the gem5 simulator. Unlike standard simulators, RV-Sec5 introduces a methodology to map high-level security invariants—such as privilege isolation and memory protection—directly to automated, cycle-accurate instrumentation points within the ISA decoder. This approach bridges the semantic gap between abstract security policies and low-level hardware execution. We demonstrate the framework’s efficacy through a case study involving unauthorized Control and Status Register (CSR) modifications, showing how RV-Sec5 detects privilege escalation attempts and monitors microarchitectural anomalies, such as TLB flushes and cache state changes, in real-time.

## 研究问题

摘要级初步判断（未核验正文）：The modularity of the RISC-V Instruction Set Architecture (ISA) has accelerated its adoption in security-critical domains, yet it introduces significant challenges for pre-silicon security validation. Current evaluation methods often rely on high-level emulation that overlooks microarchitectural side effects or post-silicon testing that identifies vulnerabilities too late in the design cycle. This paper presents RV-Sec5, a systematic framework for ISA-level security evaluation that leverages the gem5 simulator. Unlike standard simulators, RV-Sec5 introduces a methodology to map high-level security invariants—such as privilege isolation and memory protection—directly to automated, cycle-accurate instrumentation points within the ISA decoder. This approach bridges the semantic gap between abstract security policies and low-level hardware execution. We demonstrate the framework’s efficacy through a case study involving unauthorized Control and Status Register (CSR) modifications, showing how RV-Sec5 detects privilege escalation attempts and monitors microarchitectural anomalies, such as TLB flushes and cache state changes, in real-time.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《RV-Sec5: Enhancing RISC-V Security Evaluation via Targeted ISA-Level Instrumentation using gem5》，初步归入“Formal & Directed Processor Verification”。

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
