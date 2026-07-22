# RTL2M$μ$PATH: Multi-$μ$PATH Synthesis with Applications to Hardware Security Verification

## 基本信息

- 作者：Yao Hsiao、Nikos Nikoleris、Artem Khyzha、Dominic P. Mulligan、Gustavo Petri、Christopher W. Fletcher、Caroline Trippel
- 发表日期：2024-09-28
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Multi-Hart, Memory Consistency & Cache Coherence、Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, microarchitecture, microarchitectural, rtl；verification/fuzzing method: verification；security relevance: security, side channel, leakage
- 论文页面：[http://arxiv.org/abs/2409.19478v1](http://arxiv.org/abs/2409.19478v1)
- PDF：[https://arxiv.org/pdf/2409.19478v1](https://arxiv.org/pdf/2409.19478v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

The Check tools automate formal memory consistency model and security verification of processors by analyzing abstract models of microarchitectures, called $μ$SPEC models. Despite the efficacy of this approach, a verification gap between $μ$SPEC models, which must be manually written, and RTL limits the Check tools' broad adoption. Our prior work, called RTL2$μ$SPEC, narrows this gap by automatically synthesizing formally verified $μ$SPEC models from SystemVerilog implementations of simple processors. But, RTL2$μ$SPEC assumes input designs where an instruction (e.g., a load) cannot exhibit more than one microarchitectural execution path ($μ$PATH, e.g., a cache hit or miss path) -- its single-execution-path assumption. In this paper, we first propose an automated approach and tool, called RTL2M$μ$PATH, that resolves RTL2$μ$SPEC's single-execution-path assumption. Given a SystemVerilog processor design, instruction encodings, and modest design metadata, RTL2M$μ$PATH finds a complete set of formally verified $μ$PATHs for each instruction. Next, we make an important observation: an instruction that can exhibit more than one $μ$PATH strongly indicates the presence of a microarchitectural side channel in the input design. Based on this observation, we then propose an automated approach and tool, called SynthLC, that extends RTL2M$μ$PATH with a symbolic information flow analysis to support synthesizing a variety of formally verified leakage contracts from SystemVerilog processor designs. Leakage contracts are foundational to state-of-the-art defenses against hardware side-channel attacks. SynthLC is the first automated methodology for formally verifying hardware adherence to them.

## 研究问题

摘要级初步判断（未核验正文）：The Check tools automate formal memory consistency model and security verification of processors by analyzing abstract models of microarchitectures, called $μ$SPEC models. Despite the efficacy of this approach, a verification gap between $μ$SPEC models, which must be manually written, and RTL limits the Check tools' broad adoption. Our prior work, called RTL2$μ$SPEC, narrows this gap by automatically synthesizing formally verified $μ$SPEC models from SystemVerilog implementations of simple processors. But, RTL2$μ$SPEC assumes input designs where an instruction (e.g., a load) cannot exhibit more than one microarchitectural execution path ($μ$PATH, e.g., a cache hit or miss path) -- its single-execution-path assumption. In this paper, we first propose an automated approach and tool, called RTL2M$μ$PATH, that resolves RTL2$μ$SPEC's single-execution-path assumption. Given a SystemVerilog processor design, instruction encodings, and modest design metadata, RTL2M$μ$PATH finds a complete set of formally verified $μ$PATHs for each instruction. Next, we make an important observation: an instruction that can exhibit more than one $μ$PATH strongly indicates the presence of a microarchitectural side channel in the input design. Based on this observation, we then propose an automated approach and tool, called SynthLC, that extends RTL2M$μ$PATH with a symbolic information flow analysis to support synthesizing a variety of formally verified leakage contracts from SystemVerilog processor designs. Leakage contracts are foundational to state-of-the-art defenses against hardware side-channel attacks. SynthLC is the first automated methodology for formally verifying hardware adherence to them.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《RTL2M$μ$PATH: Multi-$μ$PATH Synthesis with Applications to Hardware Security Verification》，初步归入“Multi-Hart, Memory Consistency & Cache Coherence”。

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
