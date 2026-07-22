# Teapot: Efficiently Uncovering Spectre Gadgets in COTS Binaries

## 基本信息

- 作者：Fangzheng Lin、Zhongfa Wang、Hiroshi Sasaki
- 发表日期：2024-11-18
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor；verification/fuzzing method: fuzz；security relevance: speculative execution
- 论文页面：[http://arxiv.org/abs/2411.11624v2](http://arxiv.org/abs/2411.11624v2)
- PDF：[https://arxiv.org/pdf/2411.11624v2](https://arxiv.org/pdf/2411.11624v2)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Speculative execution is crucial in enhancing modern processor performance but can introduce Spectre-type vulnerabilities that may leak sensitive information. Detecting Spectre gadgets from programs has been a research focus to enhance the analysis and understanding of Spectre attacks. However, one of the problems of existing approaches is that they rely on the presence of source code (or are impractical in terms of run-time performance and gadget detection ability). This paper presents Teapot, the first Spectre gadget scanner that works on COTS binaries with comparable performance to compiler-based alternatives. As its core principle, we introduce Speculation Shadows, a novel approach that separates the binary code for normal execution and speculation simulation in order to improve run-time efficiency. Teapot is based on static binary rewriting. It instruments the program to simulate the effects of speculative execution and also adds integrity checks to detect Spectre gadgets at run time. By leveraging fuzzing, Teapot succeeds in efficiently detecting Spectre gadgets. Evaluations show that Teapot outperforms both performance (more than 20x performant) and gadget detection ability than a previously proposed binary-based approach.

## 研究问题

摘要级初步判断（未核验正文）：Speculative execution is crucial in enhancing modern processor performance but can introduce Spectre-type vulnerabilities that may leak sensitive information. Detecting Spectre gadgets from programs has been a research focus to enhance the analysis and understanding of Spectre attacks. However, one of the problems of existing approaches is that they rely on the presence of source code (or are impractical in terms of run-time performance and gadget detection ability). This paper presents Teapot, the first Spectre gadget scanner that works on COTS binaries with comparable performance to compiler-based alternatives. As its core principle, we introduce Speculation Shadows, a novel approach that separates the binary code for normal execution and speculation simulation in order to improve run-time efficiency. Teapot is based on static binary rewriting. It instruments the program to simulate the effects of speculative execution and also adds integrity checks to detect Spectre gadgets at run time. By leveraging fuzzing, Teapot succeeds in efficiently detecting Spectre gadgets. Evaluations show that Teapot outperforms both performance (more than 20x performant) and gadget detection ability than a previously proposed binary-based approach.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Teapot: Efficiently Uncovering Spectre Gadgets in COTS Binaries》，初步归入“Microarchitectural Security Testing”。

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
