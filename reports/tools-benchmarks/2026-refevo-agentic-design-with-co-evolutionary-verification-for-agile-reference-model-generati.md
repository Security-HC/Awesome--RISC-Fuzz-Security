# RefEvo: Agentic Design with Co-Evolutionary Verification for Agile Reference Model Generation

## 基本信息

- 作者：Yifan Zhang、Jianmin Ye、Jiahao Yang、Xi Wang
- 发表日期：2026-04-27
- 更新日期：2026-04-27
- 来源：arXiv
- 来源编号：2604.24218v1
- 研究类别：Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2604.24218v1](http://arxiv.org/abs/2604.24218v1)
- PDF：[https://arxiv.org/pdf/2604.24218v1](https://arxiv.org/pdf/2604.24218v1)
- 分析模式：仅元数据分析

## 摘要

As the complexity of System-on-Chip (SoC) designs grows, the shift-left paradigm necessitates the rapid development of high-fidelity reference models (typically written in SystemC) for early architecture exploration and verification. While Large Language Models (LLMs) show promise in code generation, their application to hardware modeling faces unique challenges: (1) Rigid, static workflows fail to adapt to varying design complexity, causing inefficiency; (2) Context window overflow in multi-turn interactions leads to catastrophic forgetting of critical specifications; and (3) the Coupled Validation Failure problem--where generated Testbenches (TBs) incorrectly validate flawed models due to correlated hallucinations--severely undermines reliability. To address these limitations, we introduce RefEvo, a dynamic multi-agent framework designed for agile and reliable reference modeling. RefEvo features three key innovations: (1) A Dynamic Design Planner that autonomously decomposes design specifications and constructs tailored execution workflows based on semantic complexity; (2) A Co-Evolutionary Verification Mechanism, which employs a Dialectical Arbiter to simultaneously rectify the model and verification logic against the specification (Spec) oracle, effectively mitigating false positives; and (3) A Spec Anchoring Strategy for lossless context compression. Evaluated on a diverse benchmark of 20 hardware modules, RefEvo achieves a 95% pass rate, outperforming static baselines by a large margin. Furthermore, our context optimization reduces token consumption by an average of 71.04%, achieving absolute savings of over 70,000 tokens per session for complex designs while maintaining 100% specification recall.

## 研究问题

As the complexity of System-on-Chip (SoC) designs grows, the shift-left paradigm necessitates the rapid development of high-fidelity reference models (typically written in SystemC) for early architecture exploration and verification. While Large Language Models (LLMs) show promise in code generation, their application to hardware modeling faces unique challenges: (1) Rigid, static workflows fail to adapt to varying design complexity, causing inefficiency; (2) Context window overflow in multi-turn interactions leads to catastrophic forgetting of critical specifications; and (3) the Coupled Validation Failure problem--where generated Testbenches (TBs) incorrectly validate flawed models due to correlated hallucinations--severely undermines reliability. To address these limitations, we introduce RefEvo, a dynamic multi-agent framework designed for agile and reliable reference modeling. RefEvo features three key innovations: (1) A Dynamic Design Planner that autonomously decomposes design specifications and constructs tailored execution workflows based on semantic complexity; (2) A Co-Evolutionary Verification Mechanism, which employs a Dialectical Arbiter to simultaneously rectify the model and verification logic against the specification (Spec) oracle, effectively mitigating false positives; and (3) A Spec Anchoring Strategy for lossless context compression. Evaluated on a diverse benchmark of 20 hardware modules, RefEvo achieves a 95% pass rate, outperforming static baselines by a large margin. Furthermore, our context optimization reduces token consumption by an average of 71.04%, achieving absolute savings of over 70,000 tokens per session for complex designs while maintaining 100% specification recall.

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
