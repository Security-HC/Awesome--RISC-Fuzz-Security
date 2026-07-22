# SimFuzz: Similarity-guided Block-level Mutation for RISC-V Processor Fuzzing

## 基本信息

- 作者：Hao Lyu、Jingzheng Wu、Xiang Ling、Yicheng Zhong、Zhiyuan Li、Tianyue Luo
- 发表日期：2026-01-17
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2601.11838v1](http://arxiv.org/abs/2601.11838v1)
- PDF：[https://arxiv.org/pdf/2601.11838v1](https://arxiv.org/pdf/2601.11838v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

The Instruction Set Architecture (ISA) defines processor operations and serves as the interface between hardware and software. As an open ISA, RISC-V lowers the barriers to processor design and encourages widespread adoption, but also exposes processors to security risks such as functional bugs. Processor fuzzing is a powerful technique for automatically detecting these bugs. However, existing fuzzing methods suffer from two main limitations. First, their emphasis on redundant test case generation causes them to overlook cross-processor corner cases. Second, they rely too heavily on coverage guidance. Current coverage metrics are biased and inefficient, and become ineffective once coverage growth plateaus. To overcome these limitations, we propose SimFuzz, a fuzzing framework that constructs a high-quality seed corpus from historical bug-triggering inputs and employs similarity-guided, block-level mutation to efficiently explore the processor input space. By introducing instruction similarity, SimFuzz expands the input space around seeds while preserving control-flow structure, enabling deeper exploration without relying on coverage feedback. We evaluate SimFuzz on three widely used open-source RISC-V processors: Rocket, BOOM, and XiangShan, and discover 17 bugs in total, including 14 previously unknown issues, 7 of which have been assigned CVE identifiers. These bugs affect the decode and memory units, cause instruction and data errors, and can lead to kernel instability or system crashes. Experimental results show that SimFuzz achieves up to 73.22% multiplexer coverage on the high-quality seed corpus. Our findings highlight critical security bugs in mainstream RISC-V processors and offer actionable insights for improving functional verification.

## 研究问题

摘要级初步判断（未核验正文）：The Instruction Set Architecture (ISA) defines processor operations and serves as the interface between hardware and software. As an open ISA, RISC-V lowers the barriers to processor design and encourages widespread adoption, but also exposes processors to security risks such as functional bugs. Processor fuzzing is a powerful technique for automatically detecting these bugs. However, existing fuzzing methods suffer from two main limitations. First, their emphasis on redundant test case generation causes them to overlook cross-processor corner cases. Second, they rely too heavily on coverage guidance. Current coverage metrics are biased and inefficient, and become ineffective once coverage growth plateaus. To overcome these limitations, we propose SimFuzz, a fuzzing framework that constructs a high-quality seed corpus from historical bug-triggering inputs and employs similarity-guided, block-level mutation to efficiently explore the processor input space. By introducing instruction similarity, SimFuzz expands the input space around seeds while preserving control-flow structure, enabling deeper exploration without relying on coverage feedback. We evaluate SimFuzz on three widely used open-source RISC-V processors: Rocket, BOOM, and XiangShan, and discover 17 bugs in total, including 14 previously unknown issues, 7 of which have been assigned CVE identifiers. These bugs affect the decode and memory units, cause instruction and data errors, and can lead to kernel instability or system crashes. Experimental results show that SimFuzz achieves up to 73.22% multiplexer coverage on the high-quality seed corpus. Our findings highlight critical security bugs in mainstream RISC-V processors and offer actionable insights for improving functional verification.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《SimFuzz: Similarity-guided Block-level Mutation for RISC-V Processor Fuzzing》，初步归入“RISC-V Processor Fuzzing”。

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
