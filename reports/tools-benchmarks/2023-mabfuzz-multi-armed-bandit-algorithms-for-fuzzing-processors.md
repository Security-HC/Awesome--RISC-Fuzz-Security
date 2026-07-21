# MABFuzz: Multi-Armed Bandit Algorithms for Fuzzing Processors

## 基本信息

- 作者：Vasudev Gohil、Rahul Kande、Chen Chen、Ahmad-Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2023-11-24
- 更新日期：2023-11-24
- 来源：arXiv
- 来源编号：2311.14594v1
- 研究类别：RISC-V Fuzzing 研究、微架构安全、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2311.14594v1](http://arxiv.org/abs/2311.14594v1)
- PDF：[https://arxiv.org/pdf/2311.14594v1](https://arxiv.org/pdf/2311.14594v1)
- 分析模式：仅元数据分析

## 摘要

As the complexities of processors keep increasing, the task of effectively verifying their integrity and security becomes ever more daunting. The intricate web of instructions, microarchitectural features, and interdependencies woven into modern processors pose a formidable challenge for even the most diligent verification and security engineers. To tackle this growing concern, recently, researchers have developed fuzzing techniques explicitly tailored for hardware processors. However, a prevailing issue with these hardware fuzzers is their heavy reliance on static strategies to make decisions in their algorithms. To address this problem, we develop a novel dynamic and adaptive decision-making framework, MABFuzz, that uses multi-armed bandit (MAB) algorithms to fuzz processors. MABFuzz is agnostic to, and hence, applicable to, any existing hardware fuzzer. In the process of designing MABFuzz, we encounter challenges related to the compatibility of MAB algorithms with fuzzers and maximizing their efficacy for fuzzing. We overcome these challenges by modifying the fuzzing process and tailoring MAB algorithms to accommodate special requirements for hardware fuzzing. We integrate three widely used MAB algorithms in a state-of-the-art hardware fuzzer and evaluate them on three popular RISC-V-based processors. Experimental results demonstrate the ability of MABFuzz to cover a broader spectrum of processors' intricate landscapes and doing so with remarkable efficiency. In particular, MABFuzz achieves up to 308x speedup in detecting vulnerabilities and up to 5x speedup in achieving coverage compared to a state-of-the-art technique.

## 研究问题

As the complexities of processors keep increasing, the task of effectively verifying their integrity and security becomes ever more daunting. The intricate web of instructions, microarchitectural features, and interdependencies woven into modern processors pose a formidable challenge for even the most diligent verification and security engineers. To tackle this growing concern, recently, researchers have developed fuzzing techniques explicitly tailored for hardware processors. However, a prevailing issue with these hardware fuzzers is their heavy reliance on static strategies to make decisions in their algorithms. To address this problem, we develop a novel dynamic and adaptive decision-making framework, MABFuzz, that uses multi-armed bandit (MAB) algorithms to fuzz processors. MABFuzz is agnostic to, and hence, applicable to, any existing hardware fuzzer. In the process of designing MABFuzz, we encounter challenges related to the compatibility of MAB algorithms with fuzzers and maximizing their efficacy for fuzzing. We overcome these challenges by modifying the fuzzing process and tailoring MAB algorithms to accommodate special requirements for hardware fuzzing. We integrate three widely used MAB algorithms in a state-of-the-art hardware fuzzer and evaluate them on three popular RISC-V-based processors. Experimental results demonstrate the ability of MABFuzz to cover a broader spectrum of processors' intricate landscapes and doing so with remarkable efficiency. In particular, MABFuzz achieves up to 308x speedup in detecting vulnerabilities and up to 5x speedup in achieving coverage compared to a state-of-the-art technique.

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
