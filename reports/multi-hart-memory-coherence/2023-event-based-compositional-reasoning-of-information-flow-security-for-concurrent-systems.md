# Event-based Compositional Reasoning of Information-Flow Security for Concurrent Systems

## 基本信息

- 作者：Yongwang Zhao、David Sanan、Fuyuan Zhang、Yang Liu
- 发表日期：2023-09-17
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：B·强邻近（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Multi-Hart, Memory Consistency & Cache Coherence、Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: multicore；verification/fuzzing method: verification, formal verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2309.09141v1](http://arxiv.org/abs/2309.09141v1)
- PDF：[https://arxiv.org/pdf/2309.09141v1](https://arxiv.org/pdf/2309.09141v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 12 页，提取 72790 字符

## 摘要

High assurance of information-flow security (IFS) for concurrent systems is challenging. A promising way for formal verification of concurrent systems is the rely-guarantee method. However, existing compositional reasoning approaches for IFS concentrate on language-based IFS. It is often not applicable for system-level security, such as multicore operating system kernels, in which secrecy of actions should also be considered. On the other hand, existing studies on the rely-guarantee method are basically built on concurrent programming languages, by which semantics of concurrent systems cannot be completely captured in a straightforward way. In order to formally verify state-action based IFS for concurrent systems, we propose a rely-guarantee-based compositional reasoning approach for IFS in this paper. We first design a language by incorporating ``Event'' into concurrent languages and give the IFS semantics of the language. As a primitive element, events offer an extremely neat framework for modeling system and are not necessarily atomic in our language. For compositional reasoning of IFS, we use rely-guarantee specification to define new forms of unwinding conditions (UCs) on events, i.e., event UCs. By a rely-guarantee proof system of the language and the soundness of event UCs, we have that event UCs imply IFS of concurrent systems. In such a way, we relax the atomicity constraint of actions in traditional UCs and provide a compositional reasoning way for IFS in which security proof of systems can be discharged by independent security proof on individual events. Finally, we mechanize the approach in Isabelle/HOL and develop a formal specification and its IFS proof for multicore separation kernels as a study case according to an industrial standard -- ARINC 653.

## 研究问题

并发系统信息流安全的形式化验证，特别是多核操作系统内核中的状态-动作级安全属性，现有方法缺乏组合推理能力，且 rely-guarantee 方法主要针对编程语言级并发，难以直接应用于系统级建模。

## Introduction 梳理

现有信息流安全验证工作大多针对单核微内核或基于语言的属性，未解决多核并发系统的组合推理问题。既有的 rely-guarantee 方法基于并发编程语言，难以直接建模系统级行为（如中断、调度）。本文提出一种基于事件的语言 π-Core，并给出 rely-guarantee 证明系统，实现状态-动作级信息流安全的组合验证，首次对多核分离内核进行 IFS 形式化验证。

## 方法

提出事件语言 π-Core，支持事件系统、并行组合及非确定性；定义小步展开条件（UCs）并证明其蕴含安全属性；给出 rely-guarantee 证明规则，将安全证明分解为单个事件的局部证明；基于 guarantee 条件定义事件级 UCs，并证明其蕴含小步 UCs；使用 Isabelle/HOL 机械化所有定义和证明。输入是事件规约，反馈/覆盖无，Oracle 是安全策略和展开条件，DUT 是 π-Core 模型，平台为 Isabelle/HOL，需要 golden model（安全策略/展开条件）。

## 实验与评估

以多核分离内核（符合 ARINC 653）为案例，形式化规约包含调度、读写采样事件，并定义安全域和策略。通过 rely-guarantee 证明系统验证了事件 UCs 满足，从而推出系统满足 noninfluence 和 nonleakage。baseline 无实验对比，实验预算未确认，统计未确认，bug/CVE 未确认，开销为证明工作量和 Isabelle/HOL 证明规模（未量化），Artifact 包括 Isabelle/HOL 形式化源码（作为补充材料提供）。

## 核心贡献

1. 提出事件语言 π-Core 及其操作语义；2. 定义状态-动作级 IFS 的展开定理；3. 构建 π-Core 的 Rely-Guarantee 证明系统并证明其正确性；4. 提出事件级展开条件实现 IFS 的组合推理；5. 在 Isabelle/HOL 中机械化所有工作；6. 首次形式化验证多核分离内核的 IFS。

## 与本仓库研究主线的关系

强邻近：论文聚焦多核并发系统的信息流安全验证，采用 rely-guarantee 方法处理多核间干扰/共享状态问题，与内存一致性验证（多 hart/一致性）在组合推理和并发干扰建模上有方法借鉴，但不直接涉及 fuzzing、硬件测试或 RTL 级验证。

## 结论

提出一种基于 rely-guarantee 的组合推理方法，可验证并发系统状态-动作级信息流安全，并通过多核分离内核案例证明了可行性。未来工作包括研究 π-Core 精化及安全保持性，以及完整实现 ARINC 653 规约。

## 局限性

案例中的规约是高度抽象的，未覆盖完整 ARINC 653 服务；依赖事件均为基本事件（BasicEvt）的假设；仅针对确定性安全策略（非非确定性）；证明的自动化程度有限（手工交互式定理证明）。

## 详细阅读分析

本文提供严谨的形式化推理框架，特别值得关注的是事件级展开条件如何降低证明复杂度，以及 rely-guarantee 的并发组合证明规则。对验证多核操作系统安全的研究者有重要参考价值。

## 后续核验问题

- π-Core 语言的事件级展开条件能否推广到其他并发系统（如硬件缓存一致性协议）？
- 是否可以将此方法与硬件 fuzzing 结合，例如生成满足展开条件的事件序列作为测试用例？
- 文中假设所有事件是基本事件（BasicEvt），该假设在实际多核系统中是否容易满足？如何放松？
