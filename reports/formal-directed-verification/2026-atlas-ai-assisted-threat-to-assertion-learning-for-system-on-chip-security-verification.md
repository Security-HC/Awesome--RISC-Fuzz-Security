# ATLAS: AI-Assisted Threat-to-Assertion Learning for System-on-Chip Security Verification

## 基本信息

- 作者：Ishraq Tashdid、Kimia Tasnia、Alexander Garcia、Jonathan Valamehr、Sazadur Rahman
- 发表日期：2026-07-26
- 会议/期刊：ACM/IEEE Design Automation Conference (DAC)
- 主分类：形式化与定向处理器验证
- 相关性：B·强邻近（score=5）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: system-on-chip, soc；verification/fuzzing method: verification, formal verification；security relevance: security, vulnerability
- 论文页面：[https://doi.org/10.1145/3770743.3804400](https://doi.org/10.1145/3770743.3804400)
- PDF：[https://dl.acm.org/doi/pdf/10.1145/3770743.3804400?download=true](https://dl.acm.org/doi/pdf/10.1145/3770743.3804400?download=true)
- 分析模式：摘要级占位（未全文核验）

## 摘要

This work presents ATLAS, an LLM-driven framework that bridges standardized threat modeling and property-based formal verification for System-on-Chip (SoC) security. Starting from vulnerability knowledge bases such as Common Weakness Enumeration (CWE), the framework identifies SoC-specific assets, maps relevant weaknesses, and generates assertion-based security properties and JasperGold scripts for verification. By combining asset-centric analysis with standardized threat model templates, it automates the transformation from vulnerability reasoning to formal proof. Evaluated on three HACK@DAC benchmarks, ATLAS detected 39/48 CWEs and, out of that 39, ATLAS was able to generate correct properties for 33 of the bugs, advancing automated, knowledge-driven SoC security verification toward a secure-by-design paradigm.

## 研究问题

摘要级初步判断（未核验正文）：This work presents ATLAS, an LLM-driven framework that bridges standardized threat modeling and property-based formal verification for System-on-Chip (SoC) security. Starting from vulnerability knowledge bases such as Common Weakness Enumeration (CWE), the framework identifies SoC-specific assets, maps relevant weaknesses, and generates assertion-based security properties and JasperGold scripts for verification. By combining asset-centric analysis with standardized threat model templates, it automates the transformation from vulnerability reasoning to formal proof. Evaluated on three HACK@DAC benchmarks, ATLAS detected 39/48 CWEs and, out of that 39, ATLAS was able to generate correct properties for 33 of the bugs, advancing automated, knowledge-driven SoC security verification toward a secure-by-design paradigm.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《ATLAS: AI-Assisted Threat-to-Assertion Learning for System-on-Chip Security Verification》，初步归入“Formal & Directed Processor Verification”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
