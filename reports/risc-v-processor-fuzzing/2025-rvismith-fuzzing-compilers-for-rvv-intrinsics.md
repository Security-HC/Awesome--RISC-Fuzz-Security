# RVISmith: Fuzzing Compilers for RVV Intrinsics

## 基本信息

- 作者：Yibo He、Cunjian Huang、Xianmiao Qu、Hongdeng Chen、Wei Yang、Tao Xie
- 发表日期：2025-07-04
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, processor；verification/fuzzing method: fuzz, differential testing；security relevance: security
- 论文页面：[http://arxiv.org/abs/2507.03773v1](http://arxiv.org/abs/2507.03773v1)
- PDF：[https://arxiv.org/pdf/2507.03773v1](https://arxiv.org/pdf/2507.03773v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Modern processors are equipped with single instruction multiple data (SIMD) instructions for fine-grained data parallelism. Compiler auto-vectorization techniques that target SIMD instructions face performance limitations due to insufficient information available at compile time, requiring programmers to manually manipulate SIMD instructions. SIMD intrinsics, a type of built-in function provided by modern compilers, enable programmers to manipulate SIMD instructions within high-level programming languages. Bugs in compilers for SIMD intrinsics can introduce potential threats to software security, producing unintended calculation results, data loss, program crashes, etc. To detect bugs in compilers for SIMD intrinsics, we propose RVISmith, a randomized fuzzer that generates well-defined C programs that include various invocation sequences of RVV (RISC-V Vector Extension) intrinsics. We design RVISmith to achieve the following objectives: (i) achieving high intrinsic coverage, (ii) improving sequence variety, and (iii) without known undefined behaviors. We implement RVISmith based on the ratified RVV intrinsic specification and evaluate our approach with three modern compilers: GCC, LLVM, and XuanTie. Experimental results show that RVISmith achieves 11.5 times higher intrinsic coverage than the state-of-the-art fuzzer for RVV intrinsics. By differential testing that compares results across different compilers, optimizations, and equivalent programs, we detect and report 13 previously unknown bugs of the three compilers under test to date. Of these bugs, 10 are confirmed and another 3 are fixed by the compiler developers.

## 研究问题

摘要级初步判断（未核验正文）：Modern processors are equipped with single instruction multiple data (SIMD) instructions for fine-grained data parallelism. Compiler auto-vectorization techniques that target SIMD instructions face performance limitations due to insufficient information available at compile time, requiring programmers to manually manipulate SIMD instructions. SIMD intrinsics, a type of built-in function provided by modern compilers, enable programmers to manipulate SIMD instructions within high-level programming languages. Bugs in compilers for SIMD intrinsics can introduce potential threats to software security, producing unintended calculation results, data loss, program crashes, etc. To detect bugs in compilers for SIMD intrinsics, we propose RVISmith, a randomized fuzzer that generates well-defined C programs that include various invocation sequences of RVV (RISC-V Vector Extension) intrinsics. We design RVISmith to achieve the following objectives: (i) achieving high intrinsic coverage, (ii) improving sequence variety, and (iii) without known undefined behaviors. We implement RVISmith based on the ratified RVV intrinsic specification and evaluate our approach with three modern compilers: GCC, LLVM, and XuanTie. Experimental results show that RVISmith achieves 11.5 times higher intrinsic coverage than the state-of-the-art fuzzer for RVV intrinsics. By differential testing that compares results across different compilers, optimizations, and equivalent programs, we detect and report 13 previously unknown bugs of the three compilers under test to date. Of these bugs, 10 are confirmed and another 3 are fixed by the compiler developers.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《RVISmith: Fuzzing Compilers for RVV Intrinsics》，初步归入“RISC-V Processor Fuzzing”。

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
