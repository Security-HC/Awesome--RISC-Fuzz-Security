# Trusting the Trust Anchor: Towards Detecting Cross-Layer Vulnerabilities with Hardware Fuzzing

## 基本信息

- 作者：Chen Chen、Rahul Kande、Pouya Mahmoody、A. Sadeghi、J. Rajendran
- 发表日期：2022-06-06
- 会议/期刊：Design Automation Conference
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: risc-v, soc；verification/fuzzing method: fuzz, verification；security relevance: security, vulnerability
- 论文页面：[https://doi.org/10.1145/3489517.3530638](https://doi.org/10.1145/3489517.3530638)
- PDF：未记录
- 分析模式：摘要级占位（未全文核验）

## 摘要

The rise in the development of complex and application-specific commercial and open-source hardware and the shrinking verification time are causing numerous hardware-security vulnerabilities. Traditional verification techniques are limited in both scalability and completeness. Research in this direction is hindered due to the lack of robust testing benchmarks. In this paper, in collaboration with our industry partners, we built an ecosystem mimicking the hardware-development cycle where we inject bugs inspired by real-world vulnerabilities into RISC-V SoC design and organized an open-to-all bug-hunting competition. We equipped the participating researchers with industry-standard static and dynamic verification tools in a ready-to-use environment. The findings from our competition shed light on the strengths and weaknesses of the existing verification tools and highlight the potential for future research in developing new vulnerability detection techniques.

## 研究问题

摘要级初步判断（未核验正文）：The rise in the development of complex and application-specific commercial and open-source hardware and the shrinking verification time are causing numerous hardware-security vulnerabilities. Traditional verification techniques are limited in both scalability and completeness. Research in this direction is hindered due to the lack of robust testing benchmarks. In this paper, in collaboration with our industry partners, we built an ecosystem mimicking the hardware-development cycle where we inject bugs inspired by real-world vulnerabilities into RISC-V SoC design and organized an open-to-all bug-hunting competition. We equipped the participating researchers with industry-standard static and dynamic verification tools in a ready-to-use environment. The findings from our competition shed light on the strengths and weaknesses of the existing verification tools and highlight the potential for future research in developing new vulnerability detection techniques.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Trusting the Trust Anchor: Towards Detecting Cross-Layer Vulnerabilities with Hardware Fuzzing》，初步归入“RISC-V Processor Fuzzing”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
