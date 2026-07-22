# DiveFuzz: Enhancing CPU Fuzzing via Diverse Instruction Construction

## 基本信息

- 作者：Zihui Guo、Miaomiao Yuan、Yanqi Yang、Liwei Chen、Gang Shi、Dan Meng
- 发表日期：2025-11-19
- 会议/期刊：未记录
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[https://doi.org/10.1145/3719027.3765167](https://doi.org/10.1145/3719027.3765167)
- PDF：[https://dl.acm.org/doi/pdf/10.1145/3719027.3765167](https://dl.acm.org/doi/pdf/10.1145/3719027.3765167)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Comprehensive exploration of the CPU architectural states in fuzzing is akin to generating diverse test cases, which include a reasonable distribution of opcode and diversity in instruction execution results (typically measured through write-back data). However, our analysis of state-of-the-art CPU fuzzers reveals that they exhibit high repetition in write-back data and an imbalanced distribution of opcodes during fuzzing. This paper presents DiveFuzz, which diversifies write-back data by finely controlling the operands of instructions at runtime, coupled with correlated contextual semantics, to generate instruction streams with diverse write-back data and semantic associations. Furthermore, DiveFuzz introduces a novel mutator that monitors the fuzzing process to dynamically adjust opcode distribution and accurately eliminate false positives. Our evaluations show that DiveFuzz significantly increases the diversity of instruction write-back data and achieves a more balanced opcode distribution compared to state-of-the-art fuzzers. Across five common coverage metrics, DiveFuzz achieves coverage 204× faster than DifuzzRTL and 114× faster than Cascade. We evaluated DiveFuzz on four well-known open-source RISC-V CPUs—XiangShan, CVA6, Rocket, and NutShell—uncovering 26 new bugs, 15 of which have CVE identifiers.

## 研究问题

摘要级初步判断（未核验正文）：Comprehensive exploration of the CPU architectural states in fuzzing is akin to generating diverse test cases, which include a reasonable distribution of opcode and diversity in instruction execution results (typically measured through write-back data). However, our analysis of state-of-the-art CPU fuzzers reveals that they exhibit high repetition in write-back data and an imbalanced distribution of opcodes during fuzzing. This paper presents DiveFuzz, which diversifies write-back data by finely controlling the operands of instructions at runtime, coupled with correlated contextual semantics, to generate instruction streams with diverse write-back data and semantic associations. Furthermore, DiveFuzz introduces a novel mutator that monitors the fuzzing process to dynamically adjust opcode distribution and accurately eliminate false positives. Our evaluations show that DiveFuzz significantly increases the diversity of instruction write-back data and achieves a more balanced opcode distribution compared to state-of-the-art fuzzers. Across five common coverage metrics, DiveFuzz achieves coverage 204× faster than DifuzzRTL and 114× faster than Cascade. We evaluated DiveFuzz on four well-known open-source RISC-V CPUs—XiangShan, CVA6, Rocket, and NutShell—uncovering 26 new bugs, 15 of which have CVE identifiers.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《DiveFuzz: Enhancing CPU Fuzzing via Diverse Instruction Construction》，初步归入“RISC-V Processor Fuzzing”。

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
