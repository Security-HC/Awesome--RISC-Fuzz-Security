# CuFuzz: Hardening CUDA Programs through Transformation and Fuzzing

## 基本信息

- 作者：Saurabh Singh、Ruobing Han、Jaewon Lee、Seonjin Na、Yonghae Kim、Taesoo Kim、Hyesoon Kim
- 发表日期：2026-01-03
- 更新日期：2026-01-03
- 来源：arXiv
- 来源编号：2601.01048v1
- 研究类别：处理器与 CPU Fuzzing、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2601.01048v1](http://arxiv.org/abs/2601.01048v1)
- PDF：[https://arxiv.org/pdf/2601.01048v1](https://arxiv.org/pdf/2601.01048v1)
- 分析模式：仅元数据分析

## 摘要

GPUs have gained significant popularity over the past decade, extending beyond their original role in graphics rendering. This evolution has brought GPU security and reliability to the forefront of concerns. Prior research has shown that CUDA's lack of memory safety can lead to serious vulnerabilities. While fuzzing is effective for finding such bugs on CPUs, equivalent tools for GPUs are lacking due to architectural differences and lack of built-in error detection. In this paper, we propose CuFuzz, a novel compiler-runtime co-design solution to extend state-of-the-art CPU fuzzing tools to GPU programs. CuFuzz transforms GPU programs into CPU programs using compiler IR-level transformations to enable effective fuzz testing. To the best of our knowledge, CuFuzz is the first mechanism to bring fuzzing support to CUDA, addressing a critical gap in GPU security research. By leveraging CPU memory error detectors such as Address Sanitizer, CuFuzz aims to uncover memory safety bugs and related correctness vulnerabilities in CUDA code, enhancing the security and reliability of GPU-accelerated applications. To ensure high fuzzing throughput, we introduce two compiler-runtime co-optimizations tailored for GPU code: Partial Representative Execution (PREX) and Access-Index Preserving Pruning (AXIPrune), achieving average throughput improvements of 32x with PREX and an additional 33% gain with AXIPrune on top of PREX-optimized code. Together, these optimizations can yield up to a 224.31x speedup. In our fuzzing campaigns, CuFuzz uncovered 122 security vulnerabilities in widely used benchmarks.

## 研究问题

GPUs have gained significant popularity over the past decade, extending beyond their original role in graphics rendering. This evolution has brought GPU security and reliability to the forefront of concerns. Prior research has shown that CUDA's lack of memory safety can lead to serious vulnerabilities. While fuzzing is effective for finding such bugs on CPUs, equivalent tools for GPUs are lacking due to architectural differences and lack of built-in error detection. In this paper, we propose CuFuzz, a novel compiler-runtime co-design solution to extend state-of-the-art CPU fuzzing tools to GPU programs. CuFuzz transforms GPU programs into CPU programs using compiler IR-level transformations to enable effective fuzz testing. To the best of our knowledge, CuFuzz is the first mechanism to bring fuzzing support to CUDA, addressing a critical gap in GPU security research. By leveraging CPU memory error detectors such as Address Sanitizer, CuFuzz aims to uncover memory safety bugs and related correctness vulnerabilities in CUDA code, enhancing the security and reliability of GPU-accelerated applications. To ensure high fuzzing throughput, we introduce two compiler-runtime co-optimizations tailored for GPU code: Partial Representative Execution (PREX) and Access-Index Preserving Pruning (AXIPrune), achieving average throughput improvements of 32x with PREX and an additional 33% gain with AXIPrune on top of PREX-optimized code. Together, these optimizations can yield up to a 224.31x speedup. In our fuzzing campaigns, CuFuzz uncovered 122 security vulnerabilities in widely used benchmarks.

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
