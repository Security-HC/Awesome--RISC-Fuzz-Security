# Emulation-based System-on-Chip Security Verification: Challenges and Opportunities

## 基本信息

- 作者：Tanvir Rahman、Shuvagata Saha、Ahmed Y. Alhurubi、Sujan Kumar Saha、Farimah Farahmandi、Mark Tehranipoor
- 发表日期：2026-04-16
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：B·强邻近（score=5）
- 证据等级：摘要级
- 标签：Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: rtl, system-on-chip, soc；verification/fuzzing method: verification, validation, formal verification；security relevance: security, vulnerability
- 论文页面：[http://arxiv.org/abs/2604.15073v1](http://arxiv.org/abs/2604.15073v1)
- PDF：[https://arxiv.org/pdf/2604.15073v1](https://arxiv.org/pdf/2604.15073v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Increasing system-on-chip (SoC) heterogeneity, deep hardware/software integration, and the proliferation of third-party intellectual property (IP) have brought security validation to the forefront of semiconductor design. While simulation and formal verification remain indispensable, they often struggle to expose vulnerabilities that emerge only under realistic execution conditions, long software-driven interactions, and adversarial stimuli. In this context, hardware emulation is emerging as an increasingly important pre-silicon verification technology because it enables higher-throughput execution of RTL designs under realistic hardware/software workloads while preserving sufficient fidelity for security-oriented analysis. This paper presents a comprehensive survey and perspective on emulation-based security verification and validation. We organize the landscape of prior work across assertion-based security checking, coverage-driven exploration, adversarial testing, information-flow tracking, fault injection, and side-channel-oriented evaluation. We provide a structured view of emulation-enabled security verification workflows, including instrumentation, stimulus generation, runtime monitoring, and evidence-driven analysis. We also examine practical challenges related to observability, scalability, property specification, and the definition of security-oriented coverage metrics for emulation-based verification. Finally, we discuss emerging directions such as AI-assisted emulation, digital security twins, chiplet-scale security exploration, automated vulnerability assessment, and cloud-scale secure emulation. Overall, this paper positions emulation as a promising foundation for the next generation of pre-silicon hardware security assurance.

## 研究问题

摘要级初步判断（未核验正文）：Increasing system-on-chip (SoC) heterogeneity, deep hardware/software integration, and the proliferation of third-party intellectual property (IP) have brought security validation to the forefront of semiconductor design. While simulation and formal verification remain indispensable, they often struggle to expose vulnerabilities that emerge only under realistic execution conditions, long software-driven interactions, and adversarial stimuli. In this context, hardware emulation is emerging as an increasingly important pre-silicon verification technology because it enables higher-throughput execution of RTL designs under realistic hardware/software workloads while preserving sufficient fidelity for security-oriented analysis. This paper presents a comprehensive survey and perspective on emulation-based security verification and validation. We organize the landscape of prior work across assertion-based security checking, coverage-driven exploration, adversarial testing, information-flow tracking, fault injection, and side-channel-oriented evaluation. We provide a structured view of emulation-enabled security verification workflows, including instrumentation, stimulus generation, runtime monitoring, and evidence-driven analysis. We also examine practical challenges related to observability, scalability, property specification, and the definition of security-oriented coverage metrics for emulation-based verification. Finally, we discuss emerging directions such as AI-assisted emulation, digital security twins, chiplet-scale security exploration, automated vulnerability assessment, and cloud-scale secure emulation. Overall, this paper positions emulation as a promising foundation for the next generation of pre-silicon hardware security assurance.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Emulation-based System-on-Chip Security Verification: Challenges and Opportunities》，初步归入“Coverage, Oracles & Fuzzing Methodology”。

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
