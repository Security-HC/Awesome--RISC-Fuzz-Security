# Microarchitectural Leakage Templates and Their Application to Cache-Based Side Channels

## 基本信息

- 作者：Ahmad Ibrahim、Hamed Nemati、Till Schlüter、Nils Ole Tippenhauer、Christian Rossow
- 发表日期：2022-11-25
- 更新日期：2022-11-25
- 来源：arXiv
- 来源编号：2211.13958v1
- 研究类别：处理器与 CPU Fuzzing、微架构安全、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2211.13958v1](http://arxiv.org/abs/2211.13958v1)
- PDF：[https://arxiv.org/pdf/2211.13958v1](https://arxiv.org/pdf/2211.13958v1)
- 分析模式：仅元数据分析

## 摘要

The complexity of modern processor architectures has given rise to sophisticated interactions among their components. Such interactions may result in potential attack vectors in terms of side channels, possibly available to user-land exploits to leak secret data. Exploitation and countering of such side channels require a detailed understanding of the target component. However, such detailed information is commonly unpublished for many CPUs. In this paper, we introduce the concept of Leakage Templates to abstractly describe specific side channels and identify their occurrences in binary applications. We design and implement Plumber, a framework to derive the generic Leakage Templates from individual code sequences that are known to cause leakage (e.g., found by prior work). Plumber uses a combination of instruction fuzzing, instructions' operand mutation and statistical analysis to explore undocumented behavior of microarchitectural optimizations and derive sufficient conditions on vulnerable code inputs that, if hold can trigger a distinguishing behavior. Using Plumber we identified novel leakage primitives based on Leakage Templates (for ARM Cortex-A53 and -A72 cores), in particular related to previction (a new premature cache eviction), and prefetching behavior. We show the utility of Leakage Templates by re-identifying a prefetcher-based vulnerability in OpenSSL 1.1.0g first reported by Shin et al. [40].

## 研究问题

The complexity of modern processor architectures has given rise to sophisticated interactions among their components. Such interactions may result in potential attack vectors in terms of side channels, possibly available to user-land exploits to leak secret data. Exploitation and countering of such side channels require a detailed understanding of the target component. However, such detailed information is commonly unpublished for many CPUs. In this paper, we introduce the concept of Leakage Templates to abstractly describe specific side channels and identify their occurrences in binary applications. We design and implement Plumber, a framework to derive the generic Leakage Templates from individual code sequences that are known to cause leakage (e.g., found by prior work). Plumber uses a combination of instruction fuzzing, instructions' operand mutation and statistical analysis to explore undocumented behavior of microarchitectural optimizations and derive sufficient conditions on vulnerable code inputs that, if hold can trigger a distinguishing behavior. Using Plumber we identified novel leakage primitives based on Leakage Templates (for ARM Cortex-A53 and -A72 cores), in particular related to previction (a new premature cache eviction), and prefetching behavior. We show the utility of Leakage Templates by re-identifying a prefetcher-based vulnerability in OpenSSL 1.1.0g first reported by Shin et al. [40].

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
