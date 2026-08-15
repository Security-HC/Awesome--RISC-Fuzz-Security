# SymbFuzz: Symbolic Execution Guided Hardware Fuzzing

## 基本信息

- 作者：S. Miftah、Amisha Srivastava、Hyunmin Kim、Shiyi Wei、Kanad Basu
- 发表日期：2025-10-17
- 会议/期刊：Micro
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: processor, rtl；verification/fuzzing method: fuzz, random testing, verification, validation；security relevance: security, vulnerability
- 论文页面：[https://doi.org/10.1145/3725843.3756131](https://doi.org/10.1145/3725843.3756131)
- PDF：[https://dl.acm.org/doi/pdf/10.1145/3725843.3756131](https://dl.acm.org/doi/pdf/10.1145/3725843.3756131)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Modern hardware incorporates reusable designs to reduce cost and time to market, inadvertently increasing exposure to security vulnerabilities. While formal verification and simulation-based approaches have been traditionally utilized to mitigate these vulnerabilities, formal techniques are hindered by scalability issues, while conventional simulation methods frequently overlook critical edge cases. Fuzzing, as a simulation-based strategy, has demonstrated considerable promise in enhancing the security of both software and hardware; however, it is impeded by challenges such as limited input coverage, difficulties in traversing branching paths, and the complexity of managing circuit parameters, in addition to the limited adaptability of existing hardware fuzzing techniques within industrial workflows. To address these limitations, we propose SymbFuzz, an innovative hybrid hardware fuzzing methodology that leverages symbolic execution to achieve superior coverage. SymbFuzz is the first hardware fuzzing technique to be implemented on the industry-standard Universal Verification Methodology (UVM), facilitating seamless integration into commercial hardware verification flows. SymbFuzz was evaluated on a diverse set of processor RTLs, including OpenTitan (Ibex), CVA6, Rocket-Core, and Mor1kx. These designs span a range of processor architectures and complexities. SymbFuzz detected all bugs previously found by existing fuzzers and additionally uncovered 14 new bugs, including a vulnerability in OpenTitan, reported in the CWE 2025 database. It also achieved up to 6.8 × faster convergence compared to traditional UVM random testing and over 2 × 104 additional functional coverage points compared to state-of-the-art fuzzers, demonstrating its effectiveness in improving RTL validation across varied processor architectures.

## 研究问题

摘要级初步判断（未核验正文）：Modern hardware incorporates reusable designs to reduce cost and time to market, inadvertently increasing exposure to security vulnerabilities. While formal verification and simulation-based approaches have been traditionally utilized to mitigate these vulnerabilities, formal techniques are hindered by scalability issues, while conventional simulation methods frequently overlook critical edge cases. Fuzzing, as a simulation-based strategy, has demonstrated considerable promise in enhancing the security of both software and hardware; however, it is impeded by challenges such as limited input coverage, difficulties in traversing branching paths, and the complexity of managing circuit parameters, in addition to the limited adaptability of existing hardware fuzzing techniques within industrial workflows. To address these limitations, we propose SymbFuzz, an innovative hybrid hardware fuzzing methodology that leverages symbolic execution to achieve superior coverage. SymbFuzz is the first hardware fuzzing technique to be implemented on the industry-standard Universal Verification Methodology (UVM), facilitating seamless integration into commercial hardware verification flows. SymbFuzz was evaluated on a diverse set of processor RTLs, including OpenTitan (Ibex), CVA6, Rocket-Core, and Mor1kx. These designs span a range of processor architectures and complexities. SymbFuzz detected all bugs previously found by existing fuzzers and additionally uncovered 14 new bugs, including a vulnerability in OpenTitan, reported in the CWE 2025 database. It also achieved up to 6.8 × faster convergence compared to traditional UVM random testing and over 2 × 104 additional functional coverage points compared to state-of-the-art fuzzers, demonstrating its effectiveness in improving RTL validation across varied processor architectures.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《SymbFuzz: Symbolic Execution Guided Hardware Fuzzing》，初步归入“RTL & SoC Hardware Fuzzing”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
