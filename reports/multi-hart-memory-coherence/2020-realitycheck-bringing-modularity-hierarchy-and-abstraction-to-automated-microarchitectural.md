# RealityCheck: Bringing Modularity, Hierarchy, and Abstraction to Automated Microarchitectural Memory Consistency Verification

## 基本信息

- 作者：Yatin A. Manerkar、Daniel Lustig、Margaret Martonosi
- 发表日期：2020-03-09
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=9）
- 证据等级：摘要级
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：strong phrase in title: memory consistency verification；hardware/processor object: risc-v, processor, microarchitectural, soc；verification/fuzzing method: verification, litmus
- 论文页面：[http://arxiv.org/abs/2003.04892v1](http://arxiv.org/abs/2003.04892v1)
- PDF：[https://arxiv.org/pdf/2003.04892v1](https://arxiv.org/pdf/2003.04892v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Modern SoCs are heterogeneous parallel systems comprised of components developed by distinct teams and possibly even different vendors. The memory consistency model (MCM) of processors in such SoCs specifies the ordering rules which constrain the values that can be read by load instructions in parallel programs running on such systems. The implementation of required MCM orderings can span components which may be designed and implemented by many different teams. Ideally, each team would be able to specify the orderings enforced by their components independently and then connect them together when conducting MCM verification. However, no prior automated approach for formal hardware MCM verification provided this. To bring automated hardware MCM verification in line with the realities of the design process, we present RealityCheck, a methodology and tool for automated formal MCM verification of modular microarchitectural ordering specifications. RealityCheck allows users to specify their designs as a hierarchy of distinct modules connected to each other rather than a single flat specification. It can then automatically verify litmus test programs against these modular specifications. RealityCheck also provides support for abstraction, which enables scalable verification by breaking up the verification of the entire design into smaller verification problems. We present results for verifying litmus tests on 7 different designs using RealityCheck. These include in-order and out-of-order pipelines, a non-blocking cache, and a heterogeneous processor. Our case studies cover the TSO and RISC-V (RVWMO) weak memory models. RealityCheck is capable of verifying 98 RVWMO litmus tests in under 4 minutes each, and its capability for abstraction enables up to a 32.1% reduction in litmus test verification time for RVWMO.

## 研究问题

摘要级初步判断（未核验正文）：Modern SoCs are heterogeneous parallel systems comprised of components developed by distinct teams and possibly even different vendors. The memory consistency model (MCM) of processors in such SoCs specifies the ordering rules which constrain the values that can be read by load instructions in parallel programs running on such systems. The implementation of required MCM orderings can span components which may be designed and implemented by many different teams. Ideally, each team would be able to specify the orderings enforced by their components independently and then connect them together when conducting MCM verification. However, no prior automated approach for formal hardware MCM verification provided this. To bring automated hardware MCM verification in line with the realities of the design process, we present RealityCheck, a methodology and tool for automated formal MCM verification of modular microarchitectural ordering specifications. RealityCheck allows users to specify their designs as a hierarchy of distinct modules connected to each other rather than a single flat specification. It can then automatically verify litmus test programs against these modular specifications. RealityCheck also provides support for abstraction, which enables scalable verification by breaking up the verification of the entire design into smaller verification problems. We present results for verifying litmus tests on 7 different designs using RealityCheck. These include in-order and out-of-order pipelines, a non-blocking cache, and a heterogeneous processor. Our case studies cover the TSO and RISC-V (RVWMO) weak memory models. RealityCheck is capable of verifying 98 RVWMO litmus tests in under 4 minutes each, and its capability for abstraction enables up to a 32.1% reduction in litmus test verification time for RVWMO.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《RealityCheck: Bringing Modularity, Hierarchy, and Abstraction to Automated Microarchitectural Memory Consistency Verification》，初步归入“Multi-Hart, Memory Consistency & Cache Coherence”。

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
