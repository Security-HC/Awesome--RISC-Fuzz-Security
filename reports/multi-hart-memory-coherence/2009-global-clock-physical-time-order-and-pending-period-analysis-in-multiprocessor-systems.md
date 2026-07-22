# Global Clock, Physical Time Order and Pending Period Analysis in Multiprocessor Systems

## 基本信息

- 作者：Yunji Chen、Tianshi Chen、Weiwu Hu
- 发表日期：2009-03-29
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=7）
- 证据等级：摘要级
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：strong phrase in abstract: memory consistency verification；hardware/processor object: processor, memory consistency；verification/fuzzing method: verification
- 论文页面：[http://arxiv.org/abs/0903.4961v2](http://arxiv.org/abs/0903.4961v2)
- PDF：[https://arxiv.org/pdf/0903.4961v2](https://arxiv.org/pdf/0903.4961v2)
- 分析模式：摘要级占位（未全文核验）

## 摘要

In multiprocessor systems, various problems are treated with Lamport's logical clock and the resultant logical time orders between operations. However, one often needs to face the high complexities caused by the lack of logical time order information in practice. In this paper, we utilize the \emph{global clock} to infuse the so-called \emph{pending period} to each operation in a multiprocessor system, where the pending period is a time interval that contains the performed time of the operation. Further, we define the \emph{physical time order} for any two operations with disjoint pending periods. The physical time order is obeyed by any real execution in multiprocessor systems due to that it is part of the truly happened operation orders restricted by global clock, and it is then proven to be independent and consistent with traditional logical time orders. The above novel yet fundamental concepts enables new effective approaches for analyzing multiprocessor systems, which are named \emph{pending period analysis} as a whole. As a consequence of pending period analysis, many important problems of multiprocessor systems can be tackled effectively. As a significant application example, complete memory consistency verification, which was known as an NP-hard problem, can be solved with the complexity of $O(n^2)$ (where $n$ is the number of operations). Moreover, the two event ordering problems, which were proven to be Co-NP-Hard and NP-hard respectively, can both be solved with the time complexity of O(n) if restricted by pending period information.

## 研究问题

摘要级初步判断（未核验正文）：In multiprocessor systems, various problems are treated with Lamport's logical clock and the resultant logical time orders between operations. However, one often needs to face the high complexities caused by the lack of logical time order information in practice. In this paper, we utilize the \emph{global clock} to infuse the so-called \emph{pending period} to each operation in a multiprocessor system, where the pending period is a time interval that contains the performed time of the operation. Further, we define the \emph{physical time order} for any two operations with disjoint pending periods. The physical time order is obeyed by any real execution in multiprocessor systems due to that it is part of the truly happened operation orders restricted by global clock, and it is then proven to be independent and consistent with traditional logical time orders. The above novel yet fundamental concepts enables new effective approaches for analyzing multiprocessor systems, which are named \emph{pending period analysis} as a whole. As a consequence of pending period analysis, many important problems of multiprocessor systems can be tackled effectively. As a significant application example, complete memory consistency verification, which was known as an NP-hard problem, can be solved with the complexity of $O(n^2)$ (where $n$ is the number of operations). Moreover, the two event ordering problems, which were proven to be Co-NP-Hard and NP-hard respectively, can both be solved with the time complexity of O(n) if restricted by pending period information.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Global Clock, Physical Time Order and Pending Period Analysis in Multiprocessor Systems》，初步归入“Multi-Hart, Memory Consistency & Cache Coherence”。

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
