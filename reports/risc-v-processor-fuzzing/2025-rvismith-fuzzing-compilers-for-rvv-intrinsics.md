# RVISmith: Fuzzing Compilers for RVV Intrinsics

## 基本信息

- 作者：Yibo He、Cunjian Huang、Xianmiao Qu、Hongdeng Chen、Wei Yang、Tao Xie
- 发表日期：2025-07-04
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, processor；verification/fuzzing method: fuzz, differential testing；security relevance: security
- 论文页面：[http://arxiv.org/abs/2507.03773v1](http://arxiv.org/abs/2507.03773v1)
- PDF：[https://arxiv.org/pdf/2507.03773v1](https://arxiv.org/pdf/2507.03773v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 15 页，提取 88355 字符

## 摘要

Modern processors are equipped with single instruction multiple data (SIMD) instructions for fine-grained data parallelism. Compiler auto-vectorization techniques that target SIMD instructions face performance limitations due to insufficient information available at compile time, requiring programmers to manually manipulate SIMD instructions. SIMD intrinsics, a type of built-in function provided by modern compilers, enable programmers to manipulate SIMD instructions within high-level programming languages. Bugs in compilers for SIMD intrinsics can introduce potential threats to software security, producing unintended calculation results, data loss, program crashes, etc. To detect bugs in compilers for SIMD intrinsics, we propose RVISmith, a randomized fuzzer that generates well-defined C programs that include various invocation sequences of RVV (RISC-V Vector Extension) intrinsics. We design RVISmith to achieve the following objectives: (i) achieving high intrinsic coverage, (ii) improving sequence variety, and (iii) without known undefined behaviors. We implement RVISmith based on the ratified RVV intrinsic specification and evaluate our approach with three modern compilers: GCC, LLVM, and XuanTie. Experimental results show that RVISmith achieves 11.5 times higher intrinsic coverage than the state-of-the-art fuzzer for RVV intrinsics. By differential testing that compares results across different compilers, optimizations, and equivalent programs, we detect and report 13 previously unknown bugs of the three compilers under test to date. Of these bugs, 10 are confirmed and another 3 are fixed by the compiler developers.

## 研究问题

编译器对SIMD intrinsics（特别是RVV intrinsics）的bug检测缺乏有效工具；现有fuzzer RIF覆盖率低（<7% intrinsics）且不支持复杂操作组合。

## Introduction 梳理

现有编译器测试方法（Csmith, YARPGen, EMI等）无法生成含SIMD intrinsics的程序；自动向量化研究只关注性能；RIF是唯一RVV intrinsics fuzzer但限制大。本文提出RVISmith，实现高intrinsic覆盖、序列多样性、避免未定义行为，并报告真实bug和未定义行为分类。

## 方法

输入生成：基于RVV intrinsic文档，随机选择ratio-aligned操作序列，通过向量寄存器分配构建数据流，再调度插入load/store intrinsics，最后生成完整C程序（含初始化、循环、打印）。反馈/coverage：无反馈（纯随机），但评估时用代码覆盖率和intrinsic覆盖率。Oracle：差分测试——跨编译器、跨优化、等效程序（不同调度算法）。DUT/平台：GCC、LLVM、XuanTie编译器；RISC-V 64位；用QEMU v9.1.0执行。是否需要golden model：否，依赖差分比较。

## 实验与评估

Baseline：RIF和Csmith。实验预算：覆盖率实验用10,000个程序；bug定量用1,500,000个程序（500,000种子×3调度）。统计：13个新bug（10确认、3已修复）→影响>20,000个intrinsics；intrinsic覆盖率比RIF高11.5倍（74.08% vs 6.39%）；代码覆盖率方面，RVISmith在GCC增加11.81%（124,948行）行覆盖。开销：生成时间占CPU时间0.021%、实际时间0.022%，大部分时间用于编译和执行。Artifact：源码在GitHub (yibo2000/RVISmith)，artifact在Zenodo (15548270)。

## 核心贡献

(1) 实现首个支持复杂RVV intrinsics组合的fuzzer；(2) 检测13个真实编译器bug；(3) 对GCC和LLVM多版本的实证研究；(4) 首次报告RVV intrinsics的未定义行为及其规避方法。

## 与本仓库研究主线的关系

直接相关：属于RISC-V处理器fuzzing范畴（编译器/指令集扩展测试），但专注于编译器而非硬件。不强邻近多hart/一致性验证，但差分测试和程序生成技术可借鉴于一致性验证场景（如用RVV指令测试内存模型）。方法借鉴价值高。

## 结论

RVISmith能有效检测RVV编译器bug，实现高intrinsic覆盖率，并在GCC、LLVM、XuanTie中发现13个新bug（10确认、3已修复），证明其有效性。

## 局限性

三方面：(1) 纯随机生成，缺乏覆盖引导，导致segment load/store intrinsics覆盖率低；(2) 仅生成单一strip-mining循环，未覆盖复杂控制流；(3) 对条件未定义intrinsics使用规则化数据生成，而非随机，可能遗漏某些场景。

## 详细阅读分析

等效程序检测能力弱（仅触发4个崩溃类bug），说明当前构造的等价性不够复杂；但跨编译器和跨优化策略对所有13个bug有效。作者指出未来可探索覆盖引导，以提高segment load/store intrinsics测试。

## 后续核验问题

- (1) 能否将RVISmith扩展到多hart或内存一致性验证？
- (2) 如何设计覆盖引导策略以覆盖segment load/store intrinsics？
- (3) 等效程序构造能否更有效（如引入不同数据依赖或控制流等价变换）？
- (4) 对其他ISA（如ARM Neon、x86 AVX）的SIMD intrinsics fuzzing，RVISmith的通用性如何？
