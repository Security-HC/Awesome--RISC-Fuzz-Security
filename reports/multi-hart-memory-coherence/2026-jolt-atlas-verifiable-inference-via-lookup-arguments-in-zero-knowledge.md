# Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledge

## 基本信息

- 作者：Wyatt Benno、Alberto Centelles、Antoine Douchet、Khalil Gibran
- 发表日期：2026-02-19
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=7）
- 证据等级：摘要级
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：strong phrase in abstract: memory consistency verification；hardware/processor object: cpu, memory consistency；verification/fuzzing method: verification
- 论文页面：[http://arxiv.org/abs/2602.17452v1](http://arxiv.org/abs/2602.17452v1)
- PDF：[https://arxiv.org/pdf/2602.17452v1](https://arxiv.org/pdf/2602.17452v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

We present Jolt Atlas, a zero-knowledge machine learning (zkML) framework that extends the Jolt proving system to model inference. Unlike zkVMs (zero-knowledge virtual machines), which emulate CPU instruction execution, Jolt Atlas adapts Jolt's lookup-centric approach and applies it directly to ONNX tensor operations. The ONNX computational model eliminates the need for CPU registers and simplifies memory consistency verification. In addition, ONNX is an open-source, portable format, which makes it easy to share and deploy models across different frameworks, hardware platforms, and runtime environments without requiring framework-specific conversions. Our lookup arguments, which use sumcheck protocol, are well-suited for non-linear functions -- key building blocks in modern ML. We apply optimisations such as neural teleportation to reduce the size of lookup tables while preserving model accuracy, as well as several tensor-level verification optimisations detailed in this paper. We demonstrate that Jolt Atlas can prove model inference in memory-constrained environments -- a prover property commonly referred to as \textit{streaming}. Furthermore, we discuss how Jolt Atlas achieves zero-knowledge through the BlindFold technique, as introduced in Vega. In contrast to existing zkML frameworks, we show practical proving times for classification, embedding, automated reasoning, and small language models. Jolt Atlas enables cryptographic verification that can be run on-device, without specialised hardware. The resulting proofs are succinctly verifiable. This makes Jolt Atlas well-suited for privacy-centric and adversarial environments. In a companion work, we outline various use cases of Jolt Atlas, including how it serves as guardrails in agentic commerce and for trustless AI context (often referred to as \textit{AI memory}).

## 研究问题

摘要级初步判断（未核验正文）：We present Jolt Atlas, a zero-knowledge machine learning (zkML) framework that extends the Jolt proving system to model inference. Unlike zkVMs (zero-knowledge virtual machines), which emulate CPU instruction execution, Jolt Atlas adapts Jolt's lookup-centric approach and applies it directly to ONNX tensor operations. The ONNX computational model eliminates the need for CPU registers and simplifies memory consistency verification. In addition, ONNX is an open-source, portable format, which makes it easy to share and deploy models across different frameworks, hardware platforms, and runtime environments without requiring framework-specific conversions. Our lookup arguments, which use sumcheck protocol, are well-suited for non-linear functions -- key building blocks in modern ML. We apply optimisations such as neural teleportation to reduce the size of lookup tables while preserving model accuracy, as well as several tensor-level verification optimisations detailed in this paper. We demonstrate that Jolt Atlas can prove model inference in memory-constrained environments -- a prover property commonly referred to as \textit{streaming}. Furthermore, we discuss how Jolt Atlas achieves zero-knowledge through the BlindFold technique, as introduced in Vega. In contrast to existing zkML frameworks, we show practical proving times for classification, embedding, automated reasoning, and small language models. Jolt Atlas enables cryptographic verification that can be run on-device, without specialised hardware. The resulting proofs are succinctly verifiable. This makes Jolt Atlas well-suited for privacy-centric and adversarial environments. In a companion work, we outline various use cases of Jolt Atlas, including how it serves as guardrails in agentic commerce and for trustless AI context (often referred to as \textit{AI memory}).

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledge》，初步归入“Multi-Hart, Memory Consistency & Cache Coherence”。

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
