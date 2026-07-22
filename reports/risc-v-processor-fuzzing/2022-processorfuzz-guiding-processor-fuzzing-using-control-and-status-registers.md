# ProcessorFuzz: Guiding Processor Fuzzing using Control and Status Registers

## 基本信息

- 作者：Sadullah Canakci、Chathura Rajapaksha、Anoop Mysore Nataraja、Leila Delshadtehrani、Michael Taylor、Manuel Egele、Ajay Joshi
- 发表日期：2022-09-05
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in title: processor fuzzing；hardware/processor object: risc-v, processor, rtl；verification/fuzzing method: fuzz, verification；security relevance: security, side channel
- 论文页面：[http://arxiv.org/abs/2209.01789v1](http://arxiv.org/abs/2209.01789v1)
- PDF：[https://arxiv.org/pdf/2209.01789v1](https://arxiv.org/pdf/2209.01789v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

As the complexity of modern processors has increased over the years, developing effective verification strategies to identify bugs prior to manufacturing has become critical. Undiscovered micro-architectural bugs in processors can manifest as severe security vulnerabilities in the form of side channels, functional bugs, etc. Inspired by software fuzzing, a technique commonly used for software testing, multiple recent works use hardware fuzzing for the verification of Register-Transfer Level (RTL) designs. However, these works suffer from several limitations such as lack of support for widely-used Hardware Description Languages (HDLs) and misleading coverage-signals that misidentify "interesting" inputs. Towards overcoming these shortcomings, we present ProcessorFuzz, a processor fuzzer that guides the fuzzer with a novel CSR-transition coverage metric. ProcessorFuzz monitors the transitions in Control and Status Registers (CSRs) as CSRs are in charge of controlling and holding the state of the processor. Therefore, transitions in CSRs indicate a new processor state, and guiding the fuzzer based on this feedback enables ProcessorFuzz to explore new processor states. ProcessorFuzz is agnostic to the HDL and does not require any instrumentation in the processor design. Thus, it supports a wide range of RTL designs written in different hardware languages. We evaluated ProcessorFuzz with three real-world open-source processors -- Rocket, BOOM, and BlackParrot. ProcessorFuzz triggered a set of ground-truth bugs 1.23$\times$ faster (on average) than DIFUZZRTL. Moreover, our experiments exposed 8 new bugs across the three RISC-V cores and one new bug in a reference model. All nine bugs were confirmed by the developers of the corresponding projects.

## 研究问题

摘要级初步判断（未核验正文）：As the complexity of modern processors has increased over the years, developing effective verification strategies to identify bugs prior to manufacturing has become critical. Undiscovered micro-architectural bugs in processors can manifest as severe security vulnerabilities in the form of side channels, functional bugs, etc. Inspired by software fuzzing, a technique commonly used for software testing, multiple recent works use hardware fuzzing for the verification of Register-Transfer Level (RTL) designs. However, these works suffer from several limitations such as lack of support for widely-used Hardware Description Languages (HDLs) and misleading coverage-signals that misidentify "interesting" inputs. Towards overcoming these shortcomings, we present ProcessorFuzz, a processor fuzzer that guides the fuzzer with a novel CSR-transition coverage metric. ProcessorFuzz monitors the transitions in Control and Status Registers (CSRs) as CSRs are in charge of controlling and holding the state of the processor. Therefore, transitions in CSRs indicate a new processor state, and guiding the fuzzer based on this feedback enables ProcessorFuzz to explore new processor states. ProcessorFuzz is agnostic to the HDL and does not require any instrumentation in the processor design. Thus, it supports a wide range of RTL designs written in different hardware languages. We evaluated ProcessorFuzz with three real-world open-source processors -- Rocket, BOOM, and BlackParrot. ProcessorFuzz triggered a set of ground-truth bugs 1.23$\times$ faster (on average) than DIFUZZRTL. Moreover, our experiments exposed 8 new bugs across the three RISC-V cores and one new bug in a reference model. All nine bugs were confirmed by the developers of the corresponding projects.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《ProcessorFuzz: Guiding Processor Fuzzing using Control and Status Registers》，初步归入“RISC-V Processor Fuzzing”。

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
