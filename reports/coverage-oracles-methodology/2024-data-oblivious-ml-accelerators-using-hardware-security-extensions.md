# Data-Oblivious ML Accelerators using Hardware Security Extensions

## 基本信息

- 作者：Hossam ElAtali、John Z. Jekel、Lachlan J. Gunn、N. Asokan
- 发表日期：2024-01-29
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: processor, cpu；verification/fuzzing method: information flow tracking；security relevance: security, side channel
- 论文页面：[http://arxiv.org/abs/2401.16583v1](http://arxiv.org/abs/2401.16583v1)
- PDF：[https://arxiv.org/pdf/2401.16583v1](https://arxiv.org/pdf/2401.16583v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Outsourced computation can put client data confidentiality at risk. Existing solutions are either inefficient or insufficiently secure: cryptographic techniques like fully-homomorphic encryption incur significant overheads, even with hardware assistance, while the complexity of hardware-assisted trusted execution environments has been exploited to leak secret data. Recent proposals such as BliMe and OISA show how dynamic information flow tracking (DIFT) enforced in hardware can protect client data efficiently. They are designed to protect CPU-only workloads. However, many outsourced computing applications, like machine learning, make extensive use of accelerators. We address this gap with Dolma, which applies DIFT to the Gemmini matrix multiplication accelerator, efficiently guaranteeing client data confidentiality, even in the presence of malicious/vulnerable software and side channel attacks on the server. We show that accelerators can allow DIFT logic optimizations that significantly reduce area overhead compared with general-purpose processor architectures. Dolma is integrated with the BliMe framework to achieve end-to-end security guarantees. We evaluate Dolma on an FPGA using a ResNet-50 DNN model and show that it incurs low overheads for large configurations ($4.4\%$, $16.7\%$, $16.5\%$ for performance, resource usage and power, respectively, with a 32x32 configuration).

## 研究问题

摘要级初步判断（未核验正文）：Outsourced computation can put client data confidentiality at risk. Existing solutions are either inefficient or insufficiently secure: cryptographic techniques like fully-homomorphic encryption incur significant overheads, even with hardware assistance, while the complexity of hardware-assisted trusted execution environments has been exploited to leak secret data. Recent proposals such as BliMe and OISA show how dynamic information flow tracking (DIFT) enforced in hardware can protect client data efficiently. They are designed to protect CPU-only workloads. However, many outsourced computing applications, like machine learning, make extensive use of accelerators. We address this gap with Dolma, which applies DIFT to the Gemmini matrix multiplication accelerator, efficiently guaranteeing client data confidentiality, even in the presence of malicious/vulnerable software and side channel attacks on the server. We show that accelerators can allow DIFT logic optimizations that significantly reduce area overhead compared with general-purpose processor architectures. Dolma is integrated with the BliMe framework to achieve end-to-end security guarantees. We evaluate Dolma on an FPGA using a ResNet-50 DNN model and show that it incurs low overheads for large configurations ($4.4\%$, $16.7\%$, $16.5\%$ for performance, resource usage and power, respectively, with a 32x32 configuration).

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Data-Oblivious ML Accelerators using Hardware Security Extensions》，初步归入“Coverage, Oracles & Fuzzing Methodology”。

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
