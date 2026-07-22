# Generalized Security-Preserving Refinement for Concurrent Systems

## 基本信息

- 作者：Huan Sun、David Sanán、Jingyi Wang、Yongwang Zhao、Jun Sun、Wenhai Wang
- 发表日期：2025-11-10
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：B·强邻近（score=5）
- 证据等级：摘要级
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：hardware/processor object: multicore；verification/fuzzing method: verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2511.06862v1](http://arxiv.org/abs/2511.06862v1)
- PDF：[https://arxiv.org/pdf/2511.06862v1](https://arxiv.org/pdf/2511.06862v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Ensuring compliance with Information Flow Security (IFS) is known to be challenging, especially for concurrent systems with large codebases such as multicore operating system (OS) kernels. Refinement, which verifies that an implementation preserves certain properties of a more abstract specification, is promising for tackling such challenges. However, in terms of refinement-based verification of security properties, existing techniques are still restricted to sequential systems or lack the expressiveness needed to capture complex security policies for concurrent systems. In this work, we present a generalized security-preserving refinement technique, particularly for verifying the IFS of concurrent systems governed by potentially complex security policies. We formalize the IFS properties for concurrent systems and present a refinement-based compositional approach to prove that the generalized security properties (e.g., intransitive noninterference) are preserved between implementation and abstraction. The key intuition enabling such reasoning, compared to previous refinement work, is to establish a step-mapping relation between the implementation and the abstraction, which is sufficient to ensure that every paired step (in the abstraction and the implementation, respectively) is either permitted or prohibited by the security policy. We apply our approach to verify two non-trivial case studies against a collection of security policies. Our proofs are fully mechanized in Isabelle/HOL, during which we identified that two covert channels previously reported in the ARINC 653 single-core standard also exist in the ARINC 653 multicore standard. We subsequently proved the correctness of the revised mechanism, showcasing the effectiveness of our approach.

## 研究问题

摘要级初步判断（未核验正文）：Ensuring compliance with Information Flow Security (IFS) is known to be challenging, especially for concurrent systems with large codebases such as multicore operating system (OS) kernels. Refinement, which verifies that an implementation preserves certain properties of a more abstract specification, is promising for tackling such challenges. However, in terms of refinement-based verification of security properties, existing techniques are still restricted to sequential systems or lack the expressiveness needed to capture complex security policies for concurrent systems. In this work, we present a generalized security-preserving refinement technique, particularly for verifying the IFS of concurrent systems governed by potentially complex security policies. We formalize the IFS properties for concurrent systems and present a refinement-based compositional approach to prove that the generalized security properties (e.g., intransitive noninterference) are preserved between implementation and abstraction. The key intuition enabling such reasoning, compared to previous refinement work, is to establish a step-mapping relation between the implementation and the abstraction, which is sufficient to ensure that every paired step (in the abstraction and the implementation, respectively) is either permitted or prohibited by the security policy. We apply our approach to verify two non-trivial case studies against a collection of security policies. Our proofs are fully mechanized in Isabelle/HOL, during which we identified that two covert channels previously reported in the ARINC 653 single-core standard also exist in the ARINC 653 multicore standard. We subsequently proved the correctness of the revised mechanism, showcasing the effectiveness of our approach.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Generalized Security-Preserving Refinement for Concurrent Systems》，初步归入“Multi-Hart, Memory Consistency & Cache Coherence”。

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
