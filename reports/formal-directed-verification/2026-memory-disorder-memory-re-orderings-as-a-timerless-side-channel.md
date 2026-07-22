# Memory DisOrder: Memory Re-orderings as a Timerless Side-channel

## 基本信息

- 作者：Sean Siddens、Sanya Srivastava、Reese Levine、Josiah Dykstra、Tyler Sorensen
- 发表日期：2026-01-13
- 会议/期刊：arXiv
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: processor, cpu；verification/fuzzing method: fuzz；security relevance: vulnerability
- 论文页面：[http://arxiv.org/abs/2601.08770v1](http://arxiv.org/abs/2601.08770v1)
- PDF：[https://arxiv.org/pdf/2601.08770v1](https://arxiv.org/pdf/2601.08770v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

To improve efficiency, nearly all parallel processing units (CPUs and GPUs) implement relaxed memory models in which memory operations may be re-ordered, i.e., executed out-of-order. Prior testing work in this area found that memory re-orderings are observed more frequently when other cores are active, e.g., stressing the memory system, which likely triggers aggressive hardware optimizations. In this work, we present Memory DisOrder: a timerless side-channel that uses memory re-orderings to infer activity on other processes. We first perform a fuzzing campaign and show that many mainstream processors (X86/Arm/Apple CPUs, NVIDIA/AMD/Apple GPUs) are susceptible to cross-process signals. We then show how the vulnerability can be used to implement classic attacks, including a covert channel, achieving up to 16 bits/second with 95% accuracy on an Apple M3 GPU, and application fingerprinting, achieving reliable closed-world DNN architecture fingerprinting on several CPUs and an Apple M3 GPU. Finally, we explore how low-level system details can be exploited to increase re-orderings, showing the potential for a covert channel to achieve nearly 30K bits/second on X86 CPUs. More precise attacks can likely be developed as the vulnerability becomes better understood.

## 研究问题

摘要级初步判断（未核验正文）：To improve efficiency, nearly all parallel processing units (CPUs and GPUs) implement relaxed memory models in which memory operations may be re-ordered, i.e., executed out-of-order. Prior testing work in this area found that memory re-orderings are observed more frequently when other cores are active, e.g., stressing the memory system, which likely triggers aggressive hardware optimizations. In this work, we present Memory DisOrder: a timerless side-channel that uses memory re-orderings to infer activity on other processes. We first perform a fuzzing campaign and show that many mainstream processors (X86/Arm/Apple CPUs, NVIDIA/AMD/Apple GPUs) are susceptible to cross-process signals. We then show how the vulnerability can be used to implement classic attacks, including a covert channel, achieving up to 16 bits/second with 95% accuracy on an Apple M3 GPU, and application fingerprinting, achieving reliable closed-world DNN architecture fingerprinting on several CPUs and an Apple M3 GPU. Finally, we explore how low-level system details can be exploited to increase re-orderings, showing the potential for a covert channel to achieve nearly 30K bits/second on X86 CPUs. More precise attacks can likely be developed as the vulnerability becomes better understood.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Memory DisOrder: Memory Re-orderings as a Timerless Side-channel》，初步归入“Formal & Directed Processor Verification”。

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
