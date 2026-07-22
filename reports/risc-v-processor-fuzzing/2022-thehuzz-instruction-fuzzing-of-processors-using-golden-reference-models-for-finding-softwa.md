# TheHuzz: Instruction Fuzzing of Processors Using Golden-Reference Models for Finding Software-Exploitable Vulnerabilities

## 基本信息

- 作者：Aakash Tyagi、Addison Crump、Ahmad-Reza Sadeghi、Garrett Persyn、Jeyavijayan Rajendran、Patrick Jauernig、Rahul Kande
- 发表日期：2022-01-24
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2201.09941v1](http://arxiv.org/abs/2201.09941v1)
- PDF：[https://arxiv.org/pdf/2201.09941v1](https://arxiv.org/pdf/2201.09941v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

The increasing complexity of modern processors poses many challenges to existing hardware verification tools and methodologies for detecting security-critical bugs. Recent attacks on processors have shown the fatal consequences of uncovering and exploiting hardware vulnerabilities. Fuzzing has emerged as a promising technique for detecting software vulnerabilities. Recently, a few hardware fuzzing techniques have been proposed. However, they suffer from several limitations, including non-applicability to commonly used Hardware Description Languages (HDLs) like Verilog and VHDL, the need for significant human intervention, and inability to capture many intrinsic hardware behaviors, such as signal transitions and floating wires. In this paper, we present the design and implementation of a novel hardware fuzzer, TheHuzz, that overcomes the aforementioned limitations and significantly improves the state of the art. We analyze the intrinsic behaviors of hardware designs in HDLs and then measure the coverage metrics that model such behaviors. TheHuzz generates assembly-level instructions to increase the desired coverage values, thereby finding many hardware bugs that are exploitable from software. We evaluate TheHuzz on four popular open-source processors and achieve 1.98x and 3.33x the speed compared to the industry-standard random regression approach and the state-of-the-art hardware fuzzer, DiffuzRTL, respectively. Using TheHuzz, we detected 11 bugs in these processors, including 8 new vulnerabilities, and we demonstrate exploits using the detected bugs. We also show that TheHuzz overcomes the limitations of formal verification tools from the semiconductor industry by comparing its findings to those discovered by the Cadence JasperGold tool.

## 研究问题

摘要级初步判断（未核验正文）：The increasing complexity of modern processors poses many challenges to existing hardware verification tools and methodologies for detecting security-critical bugs. Recent attacks on processors have shown the fatal consequences of uncovering and exploiting hardware vulnerabilities. Fuzzing has emerged as a promising technique for detecting software vulnerabilities. Recently, a few hardware fuzzing techniques have been proposed. However, they suffer from several limitations, including non-applicability to commonly used Hardware Description Languages (HDLs) like Verilog and VHDL, the need for significant human intervention, and inability to capture many intrinsic hardware behaviors, such as signal transitions and floating wires. In this paper, we present the design and implementation of a novel hardware fuzzer, TheHuzz, that overcomes the aforementioned limitations and significantly improves the state of the art. We analyze the intrinsic behaviors of hardware designs in HDLs and then measure the coverage metrics that model such behaviors. TheHuzz generates assembly-level instructions to increase the desired coverage values, thereby finding many hardware bugs that are exploitable from software. We evaluate TheHuzz on four popular open-source processors and achieve 1.98x and 3.33x the speed compared to the industry-standard random regression approach and the state-of-the-art hardware fuzzer, DiffuzRTL, respectively. Using TheHuzz, we detected 11 bugs in these processors, including 8 new vulnerabilities, and we demonstrate exploits using the detected bugs. We also show that TheHuzz overcomes the limitations of formal verification tools from the semiconductor industry by comparing its findings to those discovered by the Cadence JasperGold tool.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《TheHuzz: Instruction Fuzzing of Processors Using Golden-Reference Models for Finding Software-Exploitable Vulnerabilities》，初步归入“RISC-V Processor Fuzzing”。

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
