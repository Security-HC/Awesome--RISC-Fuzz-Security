# RVISmith: Fuzzing Compilers for RVV Intrinsics

## 基本信息

- 作者：Yibo He、Cunjian Huang、Xianmiao Qu、Hongdeng Chen、Wei Yang、Tao Xie
- 发表日期：2025-07-04
- 更新日期：2025-07-04
- 来源：arXiv
- 来源编号：2507.03773v1
- 研究类别：RISC-V Fuzzing 研究、Fuzzing 方法论
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2507.03773v1](http://arxiv.org/abs/2507.03773v1)
- PDF：[https://arxiv.org/pdf/2507.03773v1](https://arxiv.org/pdf/2507.03773v1)
- 分析模式：仅元数据分析

## 摘要

Modern processors are equipped with single instruction multiple data (SIMD) instructions for fine-grained data parallelism. Compiler auto-vectorization techniques that target SIMD instructions face performance limitations due to insufficient information available at compile time, requiring programmers to manually manipulate SIMD instructions. SIMD intrinsics, a type of built-in function provided by modern compilers, enable programmers to manipulate SIMD instructions within high-level programming languages. Bugs in compilers for SIMD intrinsics can introduce potential threats to software security, producing unintended calculation results, data loss, program crashes, etc. To detect bugs in compilers for SIMD intrinsics, we propose RVISmith, a randomized fuzzer that generates well-defined C programs that include various invocation sequences of RVV (RISC-V Vector Extension) intrinsics. We design RVISmith to achieve the following objectives: (i) achieving high intrinsic coverage, (ii) improving sequence variety, and (iii) without known undefined behaviors. We implement RVISmith based on the ratified RVV intrinsic specification and evaluate our approach with three modern compilers: GCC, LLVM, and XuanTie. Experimental results show that RVISmith achieves 11.5 times higher intrinsic coverage than the state-of-the-art fuzzer for RVV intrinsics. By differential testing that compares results across different compilers, optimizations, and equivalent programs, we detect and report 13 previously unknown bugs of the three compilers under test to date. Of these bugs, 10 are confirmed and another 3 are fixed by the compiler developers.

## 研究问题

Modern processors are equipped with single instruction multiple data (SIMD) instructions for fine-grained data parallelism. Compiler auto-vectorization techniques that target SIMD instructions face performance limitations due to insufficient information available at compile time, requiring programmers to manually manipulate SIMD instructions. SIMD intrinsics, a type of built-in function provided by modern compilers, enable programmers to manipulate SIMD instructions within high-level programming languages. Bugs in compilers for SIMD intrinsics can introduce potential threats to software security, producing unintended calculation results, data loss, program crashes, etc. To detect bugs in compilers for SIMD intrinsics, we propose RVISmith, a randomized fuzzer that generates well-defined C programs that include various invocation sequences of RVV (RISC-V Vector Extension) intrinsics. We design RVISmith to achieve the following objectives: (i) achieving high intrinsic coverage, (ii) improving sequence variety, and (iii) without known undefined behaviors. We implement RVISmith based on the ratified RVV intrinsic specification and evaluate our approach with three modern compilers: GCC, LLVM, and XuanTie. Experimental results show that RVISmith achieves 11.5 times higher intrinsic coverage than the state-of-the-art fuzzer for RVV intrinsics. By differential testing that compares results across different compilers, optimizations, and equivalent programs, we detect and report 13 previously unknown bugs of the three compilers under test to date. Of these bugs, 10 are confirmed and another 3 are fixed by the compiler developers.

## Introduction 梳理

当前为基于题名和摘要生成的记录。配置 OPENAI_API_KEY 或 DEEPSEEK_API_KEY 后，可以启用全文阅读分析。

## 方法

等待全文提取后补充。

## 实验与评估

等待全文提取后补充。

## 结论

等待全文提取后补充。

## 局限性

等待全文提取后补充。初步阅读时应重点检查适用架构、测试对象、oracle 设计、覆盖率指标和复现实验条件。

## 详细阅读分析

等待全文提取后补充。建议结合论文 PDF、开源 artifact、实验对象和可迁移到 RISC-V/处理器 fuzzing 的部分继续分析。

## 后续跟进问题

- 论文是否提供开源实现或实验 artifact？
- 方法是否可以迁移到 RISC-V core、RTL 仿真器或真实处理器？
- 论文依赖什么 oracle、覆盖率指标或差分测试对象？
