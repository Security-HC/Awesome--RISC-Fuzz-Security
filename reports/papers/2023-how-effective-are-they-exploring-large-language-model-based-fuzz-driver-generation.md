# How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation

## 基本信息

- 作者：Cen Zhang、Yaowen Zheng、Mingqiang Bai、Yeting Li、Wei Ma、Xiaofei Xie、Yuekang Li、Limin Sun、Yang Liu
- 发表日期：2023-07-24
- 更新日期：2024-07-29
- 来源：arXiv
- 来源编号：2307.12469v5
- 研究类别：Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2307.12469v5](http://arxiv.org/abs/2307.12469v5)
- PDF：[https://arxiv.org/pdf/2307.12469v5](https://arxiv.org/pdf/2307.12469v5)
- 分析模式：仅元数据分析

## 摘要

LLM-based (Large Language Model) fuzz driver generation is a promising research area. Unlike traditional program analysis-based method, this text-based approach is more general and capable of harnessing a variety of API usage information, resulting in code that is friendly for human readers. However, there is still a lack of understanding regarding the fundamental issues on this direction, such as its effectiveness and potential challenges. To bridge this gap, we conducted the first in-depth study targeting the important issues of using LLMs to generate effective fuzz drivers. Our study features a curated dataset with 86 fuzz driver generation questions from 30 widely-used C projects. Six prompting strategies are designed and tested across five state-of-the-art LLMs with five different temperature settings. In total, our study evaluated 736,430 generated fuzz drivers, with 0.85 billion token costs ($8,000+ charged tokens). Additionally, we compared the LLM-generated drivers against those utilized in industry, conducting extensive fuzzing experiments (3.75 CPU-year). Our study uncovered that: - While LLM-based fuzz driver generation is a promising direction, it still encounters several obstacles towards practical applications; - LLMs face difficulties in generating effective fuzz drivers for APIs with intricate specifics. Three featured design choices of prompt strategies can be beneficial: issuing repeat queries, querying with examples, and employing an iterative querying process; - While LLM-generated drivers can yield fuzzing outcomes that are on par with those used in the industry, there are substantial opportunities for enhancement, such as extending contained API usage, or integrating semantic oracles to facilitate logical bug detection. Our insights have been implemented to improve the OSS-Fuzz-Gen project, facilitating practical fuzz driver generation in industry.

## 研究问题

LLM-based (Large Language Model) fuzz driver generation is a promising research area. Unlike traditional program analysis-based method, this text-based approach is more general and capable of harnessing a variety of API usage information, resulting in code that is friendly for human readers. However, there is still a lack of understanding regarding the fundamental issues on this direction, such as its effectiveness and potential challenges. To bridge this gap, we conducted the first in-depth study targeting the important issues of using LLMs to generate effective fuzz drivers. Our study features a curated dataset with 86 fuzz driver generation questions from 30 widely-used C projects. Six prompting strategies are designed and tested across five state-of-the-art LLMs with five different temperature settings. In total, our study evaluated 736,430 generated fuzz drivers, with 0.85 billion token costs ($8,000+ charged tokens). Additionally, we compared the LLM-generated drivers against those utilized in industry, conducting extensive fuzzing experiments (3.75 CPU-year). Our study uncovered that: - While LLM-based fuzz driver generation is a promising direction, it still encounters several obstacles towards practical applications; - LLMs face difficulties in generating effective fuzz drivers for APIs with intricate specifics. Three featured design choices of prompt strategies can be beneficial: issuing repeat queries, querying with examples, and employing an iterative querying process; - While LLM-generated drivers can yield fuzzing outcomes that are on par with those used in the industry, there are substantial opportunities for enhancement, such as extending contained API usage, or integrating semantic oracles to facilitate logical bug detection. Our insights have been implemented to improve the OSS-Fuzz-Gen project, facilitating practical fuzz driver generation in industry.

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
