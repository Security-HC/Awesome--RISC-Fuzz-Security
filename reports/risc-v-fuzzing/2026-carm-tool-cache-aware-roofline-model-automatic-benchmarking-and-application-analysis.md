# CARM Tool: Cache-Aware Roofline Model Automatic Benchmarking and Application Analysis

## 基本信息

- 作者：José Morgado、Leonel Sousa、Aleksandar Ilic
- 发表日期：2026-05-28
- 更新日期：2026-05-28
- 来源：arXiv
- 来源编号：2605.29740v1
- 研究类别：RISC-V Fuzzing 研究、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2605.29740v1](http://arxiv.org/abs/2605.29740v1)
- PDF：[https://arxiv.org/pdf/2605.29740v1](https://arxiv.org/pdf/2605.29740v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

In recent years, HPC systems and CPU architectures as their central components, have become increasingly complex, making application development and optimization quite challenging. In this respect, intuitive performance models like the Cache-aware Roofline Model (CARM) offer effective guidance by providing insights into bottlenecks that limit the application's ability to reach the system's maximum performance. To fully exploit the benefits of CARM optimization guidance for application development, automatic tools for cross-architecture model construction and in-depth application characterization are absolutely essential. Given a plethora of existing CPU architectures, the current landscape of CARM-enabled tools covers either vendor-specific (Intel Advisor), not sufficiently developed (ARM) or simply non-existing (AMD, RISC-V) tools. This is a particular gap that this work intends to close by bringing automatic CARM support to all major CPU architectures and ISAs, i.e., x86 (Intel, AMD), ARM, and RISC-V, by developing assembly microbenchmarks specifically tailored to cover a full performance spectrum of modern CPUs (from scalar to all supported vector ISA extensions) for both computational units and all memory hierarchy levels. Additionally, this work integrates application analysis within the CARM framework using performance counters and dynamic binary instrumentation. Experimental results show that the CARM roofs constructed with the proposed automated framework provide less than a 1% deviation across various tested architectural maximums.

## 研究问题

现有CARM（缓存感知Roofline模型）工具主要支持Intel架构，缺乏对AMD、ARM和RISC-V等主流架构的自动跨平台支持，导致开发者在多架构平台上进行性能优化时缺乏有效的工具。

## Introduction 梳理

本文介绍CARM Tool，一个开源、自动化的跨架构CARM基准测试和应用分析工具。通过开发针对不同ISA（x86、ARM、RISC-V）的汇编微基准，覆盖从标量到向量扩展的性能范围，并集成性能计数器和动态二进制插桩（DBI）进行应用特征分析。实验表明，该工具构建的CARM屋顶与理论最大值偏差小于1%。

## 方法

1. 自动生成汇编微基准：针对不同ISA和向量扩展（如AVX、NEON、RVV），设计内存带宽和峰值浮点性能的微基准。2. 自动基准测试模块：Python脚本协调生成和执行，支持缓存级别探测、混合指令类型（内存+浮点）等。3. 应用分析：通过PAPI（性能计数器）和DynamoRIO（DBI）提取应用特征，计算算术强度和GFLOPS。4. GUI界面：提供结果可视化。

## 实验与评估

在Intel Skylake-X、AMD Zen 3、ARM Vulcan和RISC-V C920上测试，CARM屋顶参数与理论值偏差小于1%。通过内存曲线和混合基准验证了不同负载下的性能界限。

## 结论

提出的CARM Tool成功填补了跨架构CARM工具的空白，为Intel、AMD、ARM和RISC-V提供统一的自动基准测试和应用分析能力，具有高精度和易用性。

## 局限性

1. RISC-V的DBI支持尚处早期阶段（DynamoRIO支持不完整）。2. 缓存大小检测在ARM和RISC-V上需手动配置（x86通过cpuid自动检测）。3. PMU分析目前仅支持区域（ROI）分析，缺乏全应用分析。4. 微基准依赖于汇编语言，可能难以扩展到新兴ISA或专有指令集。

## 详细阅读分析

该工具的核心创新在于通过精心设计的汇编微基准自动生成跨架构CARM，避免了传统模拟方法的时间成本。微基准策略针对每个架构的负载/存储单元、FMA单元等硬件特征进行优化，确保测量到真实上限。同时，结合PMU和DBI两种分析方式，提供了灵活的应用特征提取路径。但DBI在RISC-V上的缺失限制了其全架构覆盖能力，且PAPI事件选择受限于硬件支持。

## 后续跟进问题

- 如何扩展该工具以支持更多新兴ISA（如RISC-V向量扩展1.0后续版本）？
- 能否通过硬件性能计数器实现全应用分析，而不仅仅是ROI？
- 如何优化微基准设计以适应不同微架构的乱序执行和预取行为？
- 是否支持多核/众核系统的缓存一致性和带宽共享分析？
- 如何将CARM Tool集成到自动调优框架中，实现动态指导优化？
