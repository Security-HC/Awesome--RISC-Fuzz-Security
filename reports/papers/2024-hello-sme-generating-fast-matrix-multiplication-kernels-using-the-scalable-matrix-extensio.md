# Hello SME! Generating Fast Matrix Multiplication Kernels Using the Scalable Matrix Extension

## 基本信息

- 作者：Stefan Remke、Alexander Breuer
- 发表日期：2024-09-27
- 更新日期：2024-09-27
- 来源：arXiv
- 来源编号：2409.18779v1
- 研究类别：RISC-V Fuzzing、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2409.18779v1](http://arxiv.org/abs/2409.18779v1)
- PDF：[https://arxiv.org/pdf/2409.18779v1](https://arxiv.org/pdf/2409.18779v1)
- 分析模式：仅元数据分析

## 摘要

Modern central processing units (CPUs) feature single-instruction, multiple-data pipelines to accelerate compute-intensive floating-point and fixed-point workloads. Traditionally, these pipelines and corresponding instruction set architectures (ISAs) were designed for vector parallelism. In recent years, major hardware vendors have further increased the throughput of their CPUs by introducing matrix units with corresponding ISA extensions. The Scalable Matrix Extension (SME) has been announced for the Arm architecture in 2021 and Apple's M4 chip is the first to support SME. This paper presents an in-depth study of SME on M4. Our microbenchmarks determine the maximum floating-point and fixed-point throughput of M4's SME acceleration and study the achievable bandwidth for transfers to and from the matrix registers. Furthermore, we used the insights gained to design a just-in-time code generator for SME-based small matrix multiplications. The results presented show that M4's SME support is FP32-centric, with an achievable throughput of over 2.3 FP32 TFLOPS. To maximize read and write bandwidth, loading and storing to and from the matrix registers must be done in two steps. Our just-in-time generated small matrix multiplication kernels outperform the vendor-optimized BLAS implementation in almost all tested configurations.

## 研究问题

Modern central processing units (CPUs) feature single-instruction, multiple-data pipelines to accelerate compute-intensive floating-point and fixed-point workloads. Traditionally, these pipelines and corresponding instruction set architectures (ISAs) were designed for vector parallelism. In recent years, major hardware vendors have further increased the throughput of their CPUs by introducing matrix units with corresponding ISA extensions. The Scalable Matrix Extension (SME) has been announced for the Arm architecture in 2021 and Apple's M4 chip is the first to support SME. This paper presents an in-depth study of SME on M4. Our microbenchmarks determine the maximum floating-point and fixed-point throughput of M4's SME acceleration and study the achievable bandwidth for transfers to and from the matrix registers. Furthermore, we used the insights gained to design a just-in-time code generator for SME-based small matrix multiplications. The results presented show that M4's SME support is FP32-centric, with an achievable throughput of over 2.3 FP32 TFLOPS. To maximize read and write bandwidth, loading and storing to and from the matrix registers must be done in two steps. Our just-in-time generated small matrix multiplication kernels outperform the vendor-optimized BLAS implementation in almost all tested configurations.

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
