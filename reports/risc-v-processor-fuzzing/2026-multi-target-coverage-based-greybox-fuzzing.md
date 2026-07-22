# Multi-target Coverage-based Greybox Fuzzing

## 基本信息

- 作者：Masami Ichikawa
- 发表日期：2026-03-26
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing
- 纳入依据：hardware/processor object: risc-v；verification/fuzzing method: fuzz；security relevance: vulnerability
- 论文页面：[http://arxiv.org/abs/2603.25354v1](http://arxiv.org/abs/2603.25354v1)
- PDF：[https://arxiv.org/pdf/2603.25354v1](https://arxiv.org/pdf/2603.25354v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

In recent years, fuzzing has been widely applied not only to application software but also to system software, including the Linux kernel and firmware, and has become a powerful technique for vulnerability discovery. Among these approaches, Coverage-based grey-box fuzzing, which utilizes runtime code coverage information, has become the dominant methodology. Conventional fuzzing techniques primarily target a single software component and have paid little attention to cooperative execution with other software. However, modern system software architectures commonly consist of firmware and an operating system that operate cooperatively through well-defined interfaces, such as OpenSBI in the RISC-V architecture and OP-TEE in the ARM architecture. In this study, we investigate fuzzing techniques for architectures in which an operating system and firmware operate cooperatively. In particular, we propose a fuzzing method that enables deeper exploration of the system by leveraging the code coverage of each cooperating software component as feedback, compared to conventional Single-target fuzzing. To observe the execution of the operating system and firmware in a unified manner, our method adopts QEMU as a virtualization environment and executes fuzzing by booting the system within a virtual machine. This enables the measurement of code coverage across software boundaries. Furthermore, we implemented the proposed method as a Multi-target Coverage-based Greybox Fuzzer called MTCFuzz and evaluated its effectiveness.

## 研究问题

摘要级初步判断（未核验正文）：In recent years, fuzzing has been widely applied not only to application software but also to system software, including the Linux kernel and firmware, and has become a powerful technique for vulnerability discovery. Among these approaches, Coverage-based grey-box fuzzing, which utilizes runtime code coverage information, has become the dominant methodology. Conventional fuzzing techniques primarily target a single software component and have paid little attention to cooperative execution with other software. However, modern system software architectures commonly consist of firmware and an operating system that operate cooperatively through well-defined interfaces, such as OpenSBI in the RISC-V architecture and OP-TEE in the ARM architecture. In this study, we investigate fuzzing techniques for architectures in which an operating system and firmware operate cooperatively. In particular, we propose a fuzzing method that enables deeper exploration of the system by leveraging the code coverage of each cooperating software component as feedback, compared to conventional Single-target fuzzing. To observe the execution of the operating system and firmware in a unified manner, our method adopts QEMU as a virtualization environment and executes fuzzing by booting the system within a virtual machine. This enables the measurement of code coverage across software boundaries. Furthermore, we implemented the proposed method as a Multi-target Coverage-based Greybox Fuzzer called MTCFuzz and evaluated its effectiveness.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Multi-target Coverage-based Greybox Fuzzing》，初步归入“RISC-V Processor Fuzzing”。

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
