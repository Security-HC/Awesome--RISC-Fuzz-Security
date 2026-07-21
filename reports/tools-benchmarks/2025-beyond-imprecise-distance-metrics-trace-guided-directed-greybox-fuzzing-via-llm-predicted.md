# Beyond Imprecise Distance Metrics: Trace-Guided Directed Greybox Fuzzing via LLM-Predicted Call Stacks

## 基本信息

- 作者：Yifan Zhang、Xin Zhang
- 发表日期：2025-10-27
- 更新日期：2026-01-31
- 来源：arXiv
- 来源编号：2510.23101v2
- 研究类别：Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2510.23101v2](http://arxiv.org/abs/2510.23101v2)
- PDF：[https://arxiv.org/pdf/2510.23101v2](https://arxiv.org/pdf/2510.23101v2)
- 分析模式：仅元数据分析

## 摘要

Directed greybox fuzzing (DGF) aims to efficiently trigger bugs at specific target locations by prioritizing seeds whose execution paths are more likely to reach the targets. However, existing DGF approaches suffer from imprecise potential estimation due to their reliance on static-analysis-based distance metrics. The over-approximation inherent in static analysis causes many seeds with execution paths irrelevant to vulnerability triggering to be mistakenly prioritized, significantly reducing fuzzing efficiency. To address this issue, we propose trace-guided directed greybox fuzzing (TDGF). TDGF replaces static-analysis-based distance metrics with vulnerability-oriented execution information (referred to as guidance traces) to steer directed fuzzing: seeds whose execution paths overlap more with the guidance traces are scheduled earlier for mutation. We empirically study two representative types of guidance traces: the control-flow trace and the call-stack trace of vulnerability-triggering executions. We find that the fine-grained control-flow traces offer nearly the same guidance capability as the coarse-grained call-stack traces, while call-stack traces are also easier for large language models (LLMs) to predict. Based on this insight, we further propose a framework that leverages LLMs to predict the call stack at vulnerability-triggering time and uses it to guide DGF. We implement our approach and evaluate it against several state-of-the-art fuzzers with experiments totaling 58.4 CPU-years. On a suite of real-world programs, our approach triggers vulnerabilities 2.13$\times$ to 3.14$\times$ faster than the baselines. Moreover, through directed patch testing on the latest program versions used in our controlled experiments, our approach discovers 10 new vulnerabilities and 2 incomplete fixes, with 10 assigned CVE IDs.

## 研究问题

Directed greybox fuzzing (DGF) aims to efficiently trigger bugs at specific target locations by prioritizing seeds whose execution paths are more likely to reach the targets. However, existing DGF approaches suffer from imprecise potential estimation due to their reliance on static-analysis-based distance metrics. The over-approximation inherent in static analysis causes many seeds with execution paths irrelevant to vulnerability triggering to be mistakenly prioritized, significantly reducing fuzzing efficiency. To address this issue, we propose trace-guided directed greybox fuzzing (TDGF). TDGF replaces static-analysis-based distance metrics with vulnerability-oriented execution information (referred to as guidance traces) to steer directed fuzzing: seeds whose execution paths overlap more with the guidance traces are scheduled earlier for mutation. We empirically study two representative types of guidance traces: the control-flow trace and the call-stack trace of vulnerability-triggering executions. We find that the fine-grained control-flow traces offer nearly the same guidance capability as the coarse-grained call-stack traces, while call-stack traces are also easier for large language models (LLMs) to predict. Based on this insight, we further propose a framework that leverages LLMs to predict the call stack at vulnerability-triggering time and uses it to guide DGF. We implement our approach and evaluate it against several state-of-the-art fuzzers with experiments totaling 58.4 CPU-years. On a suite of real-world programs, our approach triggers vulnerabilities 2.13$\times$ to 3.14$\times$ faster than the baselines. Moreover, through directed patch testing on the latest program versions used in our controlled experiments, our approach discovers 10 new vulnerabilities and 2 incomplete fixes, with 10 assigned CVE IDs.

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
