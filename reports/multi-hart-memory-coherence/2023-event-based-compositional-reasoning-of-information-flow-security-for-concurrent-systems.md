# Event-based Compositional Reasoning of Information-Flow Security for Concurrent Systems

## 基本信息

- 作者：Yongwang Zhao、David Sanan、Fuyuan Zhang、Yang Liu
- 发表日期：2023-09-17
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：B·强邻近（score=5）
- 证据等级：摘要级
- 标签：Multi-Hart, Memory Consistency & Cache Coherence、Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: multicore；verification/fuzzing method: verification, formal verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2309.09141v1](http://arxiv.org/abs/2309.09141v1)
- PDF：[https://arxiv.org/pdf/2309.09141v1](https://arxiv.org/pdf/2309.09141v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

High assurance of information-flow security (IFS) for concurrent systems is challenging. A promising way for formal verification of concurrent systems is the rely-guarantee method. However, existing compositional reasoning approaches for IFS concentrate on language-based IFS. It is often not applicable for system-level security, such as multicore operating system kernels, in which secrecy of actions should also be considered. On the other hand, existing studies on the rely-guarantee method are basically built on concurrent programming languages, by which semantics of concurrent systems cannot be completely captured in a straightforward way. In order to formally verify state-action based IFS for concurrent systems, we propose a rely-guarantee-based compositional reasoning approach for IFS in this paper. We first design a language by incorporating ``Event'' into concurrent languages and give the IFS semantics of the language. As a primitive element, events offer an extremely neat framework for modeling system and are not necessarily atomic in our language. For compositional reasoning of IFS, we use rely-guarantee specification to define new forms of unwinding conditions (UCs) on events, i.e., event UCs. By a rely-guarantee proof system of the language and the soundness of event UCs, we have that event UCs imply IFS of concurrent systems. In such a way, we relax the atomicity constraint of actions in traditional UCs and provide a compositional reasoning way for IFS in which security proof of systems can be discharged by independent security proof on individual events. Finally, we mechanize the approach in Isabelle/HOL and develop a formal specification and its IFS proof for multicore separation kernels as a study case according to an industrial standard -- ARINC 653.

## 研究问题

摘要级初步判断（未核验正文）：High assurance of information-flow security (IFS) for concurrent systems is challenging. A promising way for formal verification of concurrent systems is the rely-guarantee method. However, existing compositional reasoning approaches for IFS concentrate on language-based IFS. It is often not applicable for system-level security, such as multicore operating system kernels, in which secrecy of actions should also be considered. On the other hand, existing studies on the rely-guarantee method are basically built on concurrent programming languages, by which semantics of concurrent systems cannot be completely captured in a straightforward way. In order to formally verify state-action based IFS for concurrent systems, we propose a rely-guarantee-based compositional reasoning approach for IFS in this paper. We first design a language by incorporating ``Event'' into concurrent languages and give the IFS semantics of the language. As a primitive element, events offer an extremely neat framework for modeling system and are not necessarily atomic in our language. For compositional reasoning of IFS, we use rely-guarantee specification to define new forms of unwinding conditions (UCs) on events, i.e., event UCs. By a rely-guarantee proof system of the language and the soundness of event UCs, we have that event UCs imply IFS of concurrent systems. In such a way, we relax the atomicity constraint of actions in traditional UCs and provide a compositional reasoning way for IFS in which security proof of systems can be discharged by independent security proof on individual events. Finally, we mechanize the approach in Isabelle/HOL and develop a formal specification and its IFS proof for multicore separation kernels as a study case according to an industrial standard -- ARINC 653.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Event-based Compositional Reasoning of Information-Flow Security for Concurrent Systems》，初步归入“Multi-Hart, Memory Consistency & Cache Coherence”。

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
