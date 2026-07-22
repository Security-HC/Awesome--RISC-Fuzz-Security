# The Emergence of Hardware Fuzzing: A Critical Review of its Significance

## 基本信息

- 作者：Raghul Saravanan、Sai Manoj Pudukotai Dinakarrao
- 发表日期：2024-03-19
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：摘要级
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: processor, soc；verification/fuzzing method: fuzz, verification, formal verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2403.12812v1](http://arxiv.org/abs/2403.12812v1)
- PDF：[https://arxiv.org/pdf/2403.12812v1](https://arxiv.org/pdf/2403.12812v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

In recent years, there has been a notable surge in attention towards hardware security, driven by the increasing complexity and integration of processors, SoCs, and third-party IPs aimed at delivering advanced solutions. However, this complexity also introduces vulnerabilities and bugs into hardware systems, necessitating early detection during the IC design cycle to uphold system integrity and mitigate re-engineering costs. While the Design Verification (DV) community employs dynamic and formal verification strategies, they encounter challenges such as scalability for intricate designs and significant human intervention, leading to prolonged verification durations. As an alternative approach, hardware fuzzing, inspired by software testing methodologies, has gained prominence for its efficacy in identifying bugs within complex hardware designs. Despite the introduction of various hardware fuzzing techniques, obstacles such as inefficient conversion of hardware modules into software models impede their effectiveness. This Systematization of Knowledge (SoK) initiative delves into the fundamental principles of existing hardware fuzzing, methodologies, and their applicability across diverse hardware designs. Additionally, it evaluates factors such as the utilization of golden reference models (GRMs), coverage metrics, and toolchains to gauge their potential for broader adoption, akin to traditional formal verification methods. Furthermore, this work examines the reliability of existing hardware fuzzing techniques in identifying vulnerabilities and identifies research gaps for future advancements in design verification techniques.

## 研究问题

摘要级初步判断（未核验正文）：In recent years, there has been a notable surge in attention towards hardware security, driven by the increasing complexity and integration of processors, SoCs, and third-party IPs aimed at delivering advanced solutions. However, this complexity also introduces vulnerabilities and bugs into hardware systems, necessitating early detection during the IC design cycle to uphold system integrity and mitigate re-engineering costs. While the Design Verification (DV) community employs dynamic and formal verification strategies, they encounter challenges such as scalability for intricate designs and significant human intervention, leading to prolonged verification durations. As an alternative approach, hardware fuzzing, inspired by software testing methodologies, has gained prominence for its efficacy in identifying bugs within complex hardware designs. Despite the introduction of various hardware fuzzing techniques, obstacles such as inefficient conversion of hardware modules into software models impede their effectiveness. This Systematization of Knowledge (SoK) initiative delves into the fundamental principles of existing hardware fuzzing, methodologies, and their applicability across diverse hardware designs. Additionally, it evaluates factors such as the utilization of golden reference models (GRMs), coverage metrics, and toolchains to gauge their potential for broader adoption, akin to traditional formal verification methods. Furthermore, this work examines the reliability of existing hardware fuzzing techniques in identifying vulnerabilities and identifies research gaps for future advancements in design verification techniques.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《The Emergence of Hardware Fuzzing: A Critical Review of its Significance》，初步归入“RTL & SoC Hardware Fuzzing”。

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
