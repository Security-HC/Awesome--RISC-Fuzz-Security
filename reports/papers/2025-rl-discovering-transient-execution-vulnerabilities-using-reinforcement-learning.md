# μRL: Discovering Transient Execution Vulnerabilities Using Reinforcement Learning

## 基本信息

- 作者：M. Caner Tol、Kemal Derya、Berk Sunar
- 发表日期：2025-02-20
- 更新日期：2025-02-20
- 来源：arXiv
- 来源编号：2502.14307v1
- 研究类别：Microarchitecture Security、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：4
- 论文页面：[http://arxiv.org/abs/2502.14307v1](http://arxiv.org/abs/2502.14307v1)
- PDF：[https://arxiv.org/pdf/2502.14307v1](https://arxiv.org/pdf/2502.14307v1)
- 分析模式：仅元数据分析

## 摘要

We propose using reinforcement learning to address the challenges of discovering microarchitectural vulnerabilities, such as Spectre and Meltdown, which exploit subtle interactions in modern processors. Traditional methods like random fuzzing fail to efficiently explore the vast instruction space and often miss vulnerabilities that manifest under specific conditions. To overcome this, we introduce an intelligent, feedback-driven approach using RL. Our RL agents interact with the processor, learning from real-time feedback to prioritize instruction sequences more likely to reveal vulnerabilities, significantly improving the efficiency of the discovery process. We also demonstrate that RL systems adapt effectively to various microarchitectures, providing a scalable solution across processor generations. By automating the exploration process, we reduce the need for human intervention, enabling continuous learning that uncovers hidden vulnerabilities. Additionally, our approach detects subtle signals, such as timing anomalies or unusual cache behavior, that may indicate microarchitectural weaknesses. This proposal advances hardware security testing by introducing a more efficient, adaptive, and systematic framework for protecting modern processors. When unleashed on Intel Skylake-X and Raptor Lake microarchitectures, our RL agent was indeed able to generate instruction sequences that cause significant observable byte leakages through transient execution without generating any $μ$code assists, faults or interrupts. The newly identified leaky sequences stem from a variety of Intel instructions, e.g. including SERIALIZE, VERR/VERW, CLMUL, MMX-x87 transitions, LSL+RDSCP and LAR. These initial results give credence to the proposed approach.

## 研究问题

We propose using reinforcement learning to address the challenges of discovering microarchitectural vulnerabilities, such as Spectre and Meltdown, which exploit subtle interactions in modern processors. Traditional methods like random fuzzing fail to efficiently explore the vast instruction space and often miss vulnerabilities that manifest under specific conditions. To overcome this, we introduce an intelligent, feedback-driven approach using RL. Our RL agents interact with the processor, learning from real-time feedback to prioritize instruction sequences more likely to reveal vulnerabilities, significantly improving the efficiency of the discovery process. We also demonstrate that RL systems adapt effectively to various microarchitectures, providing a scalable solution across processor generations. By automating the exploration process, we reduce the need for human intervention, enabling continuous learning that uncovers hidden vulnerabilities. Additionally, our approach detects subtle signals, such as timing anomalies or unusual cache behavior, that may indicate microarchitectural weaknesses. This proposal advances hardware security testing by introducing a more efficient, adaptive, and systematic framework for protecting modern processors. When unleashed on Intel Skylake-X and Raptor Lake microarchitectures, our RL agent was indeed able to generate instruction sequences that cause significant observable byte leakages through transient execution without generating any $μ$code assists, faults or interrupts. The newly identified leaky sequences stem from a variety of Intel instructions, e.g. including SERIALIZE, VERR/VERW, CLMUL, MMX-x87 transitions, LSL+RDSCP and LAR. These initial results give credence to the proposed approach.

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
