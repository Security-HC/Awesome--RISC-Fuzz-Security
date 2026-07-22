# PAGURUS: Low-Overhead Dynamic Information Flow Tracking on Loosely Coupled Accelerators

## 基本信息

- 作者：Luca Piccolboni、Giuseppe Di Guglielmo、Luca P. Carloni
- 发表日期：2019-12-18
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, processor；verification/fuzzing method: information flow tracking；security relevance: security, leakage
- 论文页面：[http://arxiv.org/abs/1912.11153v1](http://arxiv.org/abs/1912.11153v1)
- PDF：[https://arxiv.org/pdf/1912.11153v1](https://arxiv.org/pdf/1912.11153v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Software-based attacks exploit bugs or vulnerabilities to get unauthorized access or leak confidential information. Dynamic information flow tracking (DIFT) is a security technique to track spurious information flows and provide strong security guarantees against such attacks. To secure heterogeneous systems, the spurious information flows must be tracked through all their components, including processors, accelerators (i.e., application-specific hardware components) and memories. We present PAGURUS, a flexible methodology to design a low-overhead shell circuit that adds DIFT support to accelerators. The shell uses a coarse-grain DIFT approach, thus not requiring to make modifications to the accelerator's implementation. We analyze the performance and area overhead of the DIFT shell on FPGAs and we propose a metric, called information leakage, to measure its security guarantees. We perform a design-space exploration to show that we can synthesize accelerators with different characteristics in terms of performance, cost and security guarantees. We also present a case study where we use the DIFT shell to secure an accelerator running on a embedded platform with a DIFT-enhanced RISC-V core.

## 研究问题

摘要级初步判断（未核验正文）：Software-based attacks exploit bugs or vulnerabilities to get unauthorized access or leak confidential information. Dynamic information flow tracking (DIFT) is a security technique to track spurious information flows and provide strong security guarantees against such attacks. To secure heterogeneous systems, the spurious information flows must be tracked through all their components, including processors, accelerators (i.e., application-specific hardware components) and memories. We present PAGURUS, a flexible methodology to design a low-overhead shell circuit that adds DIFT support to accelerators. The shell uses a coarse-grain DIFT approach, thus not requiring to make modifications to the accelerator's implementation. We analyze the performance and area overhead of the DIFT shell on FPGAs and we propose a metric, called information leakage, to measure its security guarantees. We perform a design-space exploration to show that we can synthesize accelerators with different characteristics in terms of performance, cost and security guarantees. We also present a case study where we use the DIFT shell to secure an accelerator running on a embedded platform with a DIFT-enhanced RISC-V core.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《PAGURUS: Low-Overhead Dynamic Information Flow Tracking on Loosely Coupled Accelerators》，初步归入“Coverage, Oracles & Fuzzing Methodology”。

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
