# MicroWalk: A Framework for Finding Side Channels in Binaries

## 基本信息

- 作者：Jan Wichelmann、Ahmad Moghimi、Thomas Eisenbarth、Berk Sunar
- 发表日期：2018-08-16
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: cpu, microarchitectural；verification/fuzzing method: verification；security relevance: security, side channel, leakage
- 论文页面：[http://arxiv.org/abs/1808.05575v2](http://arxiv.org/abs/1808.05575v2)
- PDF：[https://arxiv.org/pdf/1808.05575v2](https://arxiv.org/pdf/1808.05575v2)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Microarchitectural side channels expose unprotected software to information leakage attacks where a software adversary is able to track runtime behavior of a benign process and steal secrets such as cryptographic keys. As suggested by incremental software patches for the RSA algorithm against variants of side-channel attacks within different versions of cryptographic libraries, protecting security-critical algorithms against side channels is an intricate task. Software protections avoid leakages by operating in constant time with a uniform resource usage pattern independent of the processed secret. In this respect, automated testing and verification of software binaries for leakage-free behavior is of importance, particularly when the source code is not available. In this work, we propose a novel technique based on Dynamic Binary Instrumentation and Mutual Information Analysis to efficiently locate and quantify memory based and control-flow based microarchitectural leakages. We develop a software framework named \tool~for side-channel analysis of binaries which can be extended to support new classes of leakage. For the first time, by utilizing \tool, we perform rigorous leakage analysis of two widely-used closed-source cryptographic libraries: \emph{Intel IPP} and \emph{Microsoft CNG}. We analyze $15$ different cryptographic implementations consisting of $112$ million instructions in about $105$ minutes of CPU time. By locating previously unknown leakages in hardened implementations, our results suggest that \tool~can efficiently find microarchitectural leakages in software binaries.

## 研究问题

摘要级初步判断（未核验正文）：Microarchitectural side channels expose unprotected software to information leakage attacks where a software adversary is able to track runtime behavior of a benign process and steal secrets such as cryptographic keys. As suggested by incremental software patches for the RSA algorithm against variants of side-channel attacks within different versions of cryptographic libraries, protecting security-critical algorithms against side channels is an intricate task. Software protections avoid leakages by operating in constant time with a uniform resource usage pattern independent of the processed secret. In this respect, automated testing and verification of software binaries for leakage-free behavior is of importance, particularly when the source code is not available. In this work, we propose a novel technique based on Dynamic Binary Instrumentation and Mutual Information Analysis to efficiently locate and quantify memory based and control-flow based microarchitectural leakages. We develop a software framework named \tool~for side-channel analysis of binaries which can be extended to support new classes of leakage. For the first time, by utilizing \tool, we perform rigorous leakage analysis of two widely-used closed-source cryptographic libraries: \emph{Intel IPP} and \emph{Microsoft CNG}. We analyze $15$ different cryptographic implementations consisting of $112$ million instructions in about $105$ minutes of CPU time. By locating previously unknown leakages in hardened implementations, our results suggest that \tool~can efficiently find microarchitectural leakages in software binaries.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《MicroWalk: A Framework for Finding Side Channels in Binaries》，初步归入“Microarchitectural Security Testing”。

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
