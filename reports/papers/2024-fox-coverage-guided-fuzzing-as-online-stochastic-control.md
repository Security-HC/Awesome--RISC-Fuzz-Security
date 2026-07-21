# FOX: Coverage-guided Fuzzing as Online Stochastic Control

## 基本信息

- 作者：Dongdong She、Adam Storek、Yuchong Xie、Seoyoung Kweon、Prashast Srivastava、Suman Jana
- 发表日期：2024-06-06
- 更新日期：2024-06-06
- 来源：arXiv
- 来源编号：2406.04517v1
- 研究类别：Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2406.04517v1](http://arxiv.org/abs/2406.04517v1)
- PDF：[https://arxiv.org/pdf/2406.04517v1](https://arxiv.org/pdf/2406.04517v1)
- 分析模式：仅元数据分析

## 摘要

Fuzzing is an effective technique for discovering software vulnerabilities by generating random test inputs and executing them against the target program. However, fuzzing large and complex programs remains challenging due to difficulties in uncovering deeply hidden vulnerabilities. This paper addresses the limitations of existing coverage-guided fuzzers, focusing on the scheduler and mutator components. Existing schedulers suffer from information sparsity and the inability to handle fine-grained feedback metrics. The mutators are agnostic of target program branches, leading to wasted computation and slower coverage exploration. To overcome these issues, we propose an end-to-end online stochastic control formulation for coverage-guided fuzzing. Our approach incorporates a novel scheduler and custom mutator that can adapt to branch logic, maximizing aggregate edge coverage achieved over multiple stages. The scheduler utilizes fine-grained branch distance measures to identify frontier branches, where new coverage is likely to be achieved. The mutator leverages branch distance information to perform efficient and targeted seed mutations, leading to robust progress with minimal overhead. We present FOX, a proof-of-concept implementation of our control-theoretic approach, and compare it to industry-standard coverage-guided fuzzers. 6 CPU-years of extensive evaluations on the FuzzBench dataset and complex real-world programs (a total of 38 test programs) demonstrate that FOX outperforms existing state-of-the-art fuzzers, achieving average coverage improvements up to 26.45% in real-world standalone programs and 6.59% in FuzzBench programs over the state-of-the-art AFL++. In addition, it uncovers 20 unique bugs in popular real-world applications including eight that are previously unknown, showcasing real-world security impact.

## 研究问题

Fuzzing is an effective technique for discovering software vulnerabilities by generating random test inputs and executing them against the target program. However, fuzzing large and complex programs remains challenging due to difficulties in uncovering deeply hidden vulnerabilities. This paper addresses the limitations of existing coverage-guided fuzzers, focusing on the scheduler and mutator components. Existing schedulers suffer from information sparsity and the inability to handle fine-grained feedback metrics. The mutators are agnostic of target program branches, leading to wasted computation and slower coverage exploration. To overcome these issues, we propose an end-to-end online stochastic control formulation for coverage-guided fuzzing. Our approach incorporates a novel scheduler and custom mutator that can adapt to branch logic, maximizing aggregate edge coverage achieved over multiple stages. The scheduler utilizes fine-grained branch distance measures to identify frontier branches, where new coverage is likely to be achieved. The mutator leverages branch distance information to perform efficient and targeted seed mutations, leading to robust progress with minimal overhead. We present FOX, a proof-of-concept implementation of our control-theoretic approach, and compare it to industry-standard coverage-guided fuzzers. 6 CPU-years of extensive evaluations on the FuzzBench dataset and complex real-world programs (a total of 38 test programs) demonstrate that FOX outperforms existing state-of-the-art fuzzers, achieving average coverage improvements up to 26.45% in real-world standalone programs and 6.59% in FuzzBench programs over the state-of-the-art AFL++. In addition, it uncovers 20 unique bugs in popular real-world applications including eight that are previously unknown, showcasing real-world security impact.

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
