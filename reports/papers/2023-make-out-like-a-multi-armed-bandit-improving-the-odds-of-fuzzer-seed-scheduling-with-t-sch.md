# Make out like a (Multi-Armed) Bandit: Improving the Odds of Fuzzer Seed Scheduling with T-Scheduler

## 基本信息

- 作者：Simon Luo、Adrian Herrera、Paul Quirk、Michael Chase、Damith C. Ranasinghe、Salil S. Kanhere
- 发表日期：2023-12-07
- 更新日期：2023-12-07
- 来源：arXiv
- 来源编号：2312.04749v1
- 研究类别：Fuzzing Methodology
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2312.04749v1](http://arxiv.org/abs/2312.04749v1)
- PDF：[https://arxiv.org/pdf/2312.04749v1](https://arxiv.org/pdf/2312.04749v1)
- 分析模式：仅元数据分析

## 摘要

Fuzzing is a highly-scalable software testing technique that uncovers bugs in a target program by executing it with mutated inputs. Over the life of a fuzzing campaign, the fuzzer accumulates inputs inducing new and interesting target behaviors, drawing from these inputs for further mutation. This rapidly results in a large number of inputs to select from, making it challenging to quickly and accurately select the "most promising" input for mutation. Reinforcement learning (RL) provides a natural solution to this "seed scheduling" problem: the fuzzer dynamically adapts its selection strategy by learning from past results. However, existing RL approaches are (a) computationally expensive (reducing fuzzer throughput) and/or (b) require hyperparameter tuning (reducing generality across targets and input types). To this end, we propose T-Scheduler, a seed scheduler built on multi-armed bandit theory that automatically adapts to the target without any hyperparameter tuning. We evaluate T-Scheduler over 35 CPU-yr of fuzzing, comparing it to 11 state-of-the-art schedulers. Our results show that T-Scheduler improves on these 11 schedulers on both bug-finding and coverage-expansion abilities.

## 研究问题

Fuzzing is a highly-scalable software testing technique that uncovers bugs in a target program by executing it with mutated inputs. Over the life of a fuzzing campaign, the fuzzer accumulates inputs inducing new and interesting target behaviors, drawing from these inputs for further mutation. This rapidly results in a large number of inputs to select from, making it challenging to quickly and accurately select the "most promising" input for mutation. Reinforcement learning (RL) provides a natural solution to this "seed scheduling" problem: the fuzzer dynamically adapts its selection strategy by learning from past results. However, existing RL approaches are (a) computationally expensive (reducing fuzzer throughput) and/or (b) require hyperparameter tuning (reducing generality across targets and input types). To this end, we propose T-Scheduler, a seed scheduler built on multi-armed bandit theory that automatically adapts to the target without any hyperparameter tuning. We evaluate T-Scheduler over 35 CPU-yr of fuzzing, comparing it to 11 state-of-the-art schedulers. Our results show that T-Scheduler improves on these 11 schedulers on both bug-finding and coverage-expansion abilities.

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
