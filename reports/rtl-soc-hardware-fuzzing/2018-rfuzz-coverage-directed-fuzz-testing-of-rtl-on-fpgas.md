# RFUZZ: Coverage-Directed Fuzz Testing of RTL on FPGAs

## 基本信息

- 作者：Kevin Laeufer、Jack Koenig、Donggyu Kim、J. Bachrach、Koushik Sen
- 发表日期：2018-11-05
- 会议/期刊：2018 IEEE/ACM International Conference on Computer-Aided Design (ICCAD)
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：B·强邻近（score=90）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：manual adjacent seed title
- 论文页面：[https://doi.org/10.1145/3240765.3240842](https://doi.org/10.1145/3240765.3240842)
- PDF：[https://dl.acm.org/doi/pdf/10.1145/3240765.3240842](https://dl.acm.org/doi/pdf/10.1145/3240765.3240842)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Dynamic verification is widely used to increase confidence in the correctness of RTL circuits during the pre-silicon design phase. Despite numerous attempts over the last decades to automate the stimuli generation based on coverage feedback, Coverage Directed Test Generation (CDG) has not found the widespread adoption that one would expect. Based on new ideas from the software testing community around coverage-guided mutational fuzz testing, we propose a new approach to the CDG problem which requires minimal setup and takes advantage of FPGA-accelerated simulation for rapid testing. We provide test input and coverage definitions that allow fuzz testing to be applied to RTL circuit verification. In addition we propose and implement a series of transformation passes that make it feasible to reset arbitrary RTL designs quickly, a requirement for deterministic test execution. Alongside this paper we provide rfuzz, a fully featured implementation of our testing methodology which we make available as open-source software to the research community. An empirical evaluation of RFUZZ shows promising results on archiving coverage for a wide range of different RTL designs ranging from communication IPs to an industry scale 64-bit CPU.

## 研究问题

摘要级初步判断（未核验正文）：Dynamic verification is widely used to increase confidence in the correctness of RTL circuits during the pre-silicon design phase. Despite numerous attempts over the last decades to automate the stimuli generation based on coverage feedback, Coverage Directed Test Generation (CDG) has not found the widespread adoption that one would expect. Based on new ideas from the software testing community around coverage-guided mutational fuzz testing, we propose a new approach to the CDG problem which requires minimal setup and takes advantage of FPGA-accelerated simulation for rapid testing. We provide test input and coverage definitions that allow fuzz testing to be applied to RTL circuit verification. In addition we propose and implement a series of transformation passes that make it feasible to reset arbitrary RTL designs quickly, a requirement for deterministic test execution. Alongside this paper we provide rfuzz, a fully featured implementation of our testing methodology which we make available as open-source software to the research community. An empirical evaluation of RFUZZ shows promising results on archiving coverage for a wide range of different RTL designs ranging from communication IPs to an industry scale 64-bit CPU.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《RFUZZ: Coverage-Directed Fuzz Testing of RTL on FPGAs》，初步归入“RTL & SoC Hardware Fuzzing”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
