# The Correctness Illusion in LLM-Generated GPU Kernels

## 基本信息

- 作者：Dipankar Sarkar
- 发表日期：2026-06-18
- 更新日期：2026-06-18
- 来源：arXiv
- 来源编号：2606.20128v1
- 研究类别：Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2606.20128v1](http://arxiv.org/abs/2606.20128v1)
- PDF：[https://arxiv.org/pdf/2606.20128v1](https://arxiv.org/pdf/2606.20128v1)
- 分析模式：仅元数据分析

## 摘要

Benchmarks for LLM-generated GPU kernels (KernelBench, TritonBench, GEAK) score correctness through fixed-shape, small-sample allclose-style checks. The number of inputs varies between benchmarks. The shape, dtype, and tolerance are fixed for each kernel. We test that oracle empirically. We construct a controlled corpus of 24 Triton and CPU stand-in kernels (15 correct controls and 9 LLM-style buggy variants seeded with documented transcription errors) and re-evaluate it under op-schema-aware seeded fuzzing with a high-precision (fp64) CPU reference and per-(op, dtype) absolute tolerances. The seeded oracle flags 9 of 9 buggy kernels and passes 15 of 15 correct controls, at zero precision cost on controls. We extend the corpus to 26 ops (adding a flash-attention pair) and re-run the same protocol on five GPU classes (RTX 3060, A10, L40S, A100 SXM4, H100 NVL). The verdicts are identical across all five GPUs: 10 of 10 illusions caught and 16 of 16 controls clean. The corpus result is about LLM-style transcription bugs that the allclose-on-one-shape oracle certifies as correct, not about the bug rate of any specific deployed LLM. Every flagged failure replays byte-for-byte from a stored seed.

## 研究问题

Benchmarks for LLM-generated GPU kernels (KernelBench, TritonBench, GEAK) score correctness through fixed-shape, small-sample allclose-style checks. The number of inputs varies between benchmarks. The shape, dtype, and tolerance are fixed for each kernel. We test that oracle empirically. We construct a controlled corpus of 24 Triton and CPU stand-in kernels (15 correct controls and 9 LLM-style buggy variants seeded with documented transcription errors) and re-evaluate it under op-schema-aware seeded fuzzing with a high-precision (fp64) CPU reference and per-(op, dtype) absolute tolerances. The seeded oracle flags 9 of 9 buggy kernels and passes 15 of 15 correct controls, at zero precision cost on controls. We extend the corpus to 26 ops (adding a flash-attention pair) and re-run the same protocol on five GPU classes (RTX 3060, A10, L40S, A100 SXM4, H100 NVL). The verdicts are identical across all five GPUs: 10 of 10 illusions caught and 16 of 16 controls clean. The corpus result is about LLM-style transcription bugs that the allclose-on-one-shape oracle certifies as correct, not about the bug rate of any specific deployed LLM. Every flagged failure replays byte-for-byte from a stored seed.

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
