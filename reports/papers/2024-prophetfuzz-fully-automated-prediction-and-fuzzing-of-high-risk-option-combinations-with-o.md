# ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via Large Language Model

## 基本信息

- 作者：Dawei Wang、Geng Zhou、Li Chen、Dan Li、Yukai Miao
- 发表日期：2024-09-02
- 更新日期：2024-09-02
- 来源：arXiv
- 来源编号：2409.00922v1
- 研究类别：Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2409.00922v1](http://arxiv.org/abs/2409.00922v1)
- PDF：[https://arxiv.org/pdf/2409.00922v1](https://arxiv.org/pdf/2409.00922v1)
- 分析模式：仅元数据分析

## 摘要

Vulnerabilities related to option combinations pose a significant challenge in software security testing due to their vast search space. Previous research primarily addressed this challenge through mutation or filtering techniques, which inefficiently treated all option combinations as having equal potential for vulnerabilities, thus wasting considerable time on non-vulnerable targets and resulting in low testing efficiency. In this paper, we utilize carefully designed prompt engineering to drive the large language model (LLM) to predict high-risk option combinations (i.e., more likely to contain vulnerabilities) and perform fuzz testing automatically without human intervention. We developed a tool called ProphetFuzz and evaluated it on a dataset comprising 52 programs collected from three related studies. The entire experiment consumed 10.44 CPU years. ProphetFuzz successfully predicted 1748 high-risk option combinations at an average cost of only \$8.69 per program. Results show that after 72 hours of fuzzing, ProphetFuzz discovered 364 unique vulnerabilities associated with 12.30\% of the predicted high-risk option combinations, which was 32.85\% higher than that found by state-of-the-art in the same timeframe. Additionally, using ProphetFuzz, we conducted persistent fuzzing on the latest versions of these programs, uncovering 140 vulnerabilities, with 93 confirmed by developers and 21 awarded CVE numbers.

## 研究问题

Vulnerabilities related to option combinations pose a significant challenge in software security testing due to their vast search space. Previous research primarily addressed this challenge through mutation or filtering techniques, which inefficiently treated all option combinations as having equal potential for vulnerabilities, thus wasting considerable time on non-vulnerable targets and resulting in low testing efficiency. In this paper, we utilize carefully designed prompt engineering to drive the large language model (LLM) to predict high-risk option combinations (i.e., more likely to contain vulnerabilities) and perform fuzz testing automatically without human intervention. We developed a tool called ProphetFuzz and evaluated it on a dataset comprising 52 programs collected from three related studies. The entire experiment consumed 10.44 CPU years. ProphetFuzz successfully predicted 1748 high-risk option combinations at an average cost of only \$8.69 per program. Results show that after 72 hours of fuzzing, ProphetFuzz discovered 364 unique vulnerabilities associated with 12.30\% of the predicted high-risk option combinations, which was 32.85\% higher than that found by state-of-the-art in the same timeframe. Additionally, using ProphetFuzz, we conducted persistent fuzzing on the latest versions of these programs, uncovering 140 vulnerabilities, with 93 confirmed by developers and 21 awarded CVE numbers.

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
