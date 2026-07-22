# μRL: Discovering Transient Execution Vulnerabilities Using Reinforcement Learning

## 基本信息

- 作者：M. Caner Tol、Kemal Derya、Berk Sunar
- 发表日期：2025-02-20
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, microarchitecture, microarchitectural；verification/fuzzing method: fuzz；security relevance: security, transient execution, leakage
- 论文页面：[http://arxiv.org/abs/2502.14307v1](http://arxiv.org/abs/2502.14307v1)
- PDF：[https://arxiv.org/pdf/2502.14307v1](https://arxiv.org/pdf/2502.14307v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

We propose using reinforcement learning to address the challenges of discovering microarchitectural vulnerabilities, such as Spectre and Meltdown, which exploit subtle interactions in modern processors. Traditional methods like random fuzzing fail to efficiently explore the vast instruction space and often miss vulnerabilities that manifest under specific conditions. To overcome this, we introduce an intelligent, feedback-driven approach using RL. Our RL agents interact with the processor, learning from real-time feedback to prioritize instruction sequences more likely to reveal vulnerabilities, significantly improving the efficiency of the discovery process. We also demonstrate that RL systems adapt effectively to various microarchitectures, providing a scalable solution across processor generations. By automating the exploration process, we reduce the need for human intervention, enabling continuous learning that uncovers hidden vulnerabilities. Additionally, our approach detects subtle signals, such as timing anomalies or unusual cache behavior, that may indicate microarchitectural weaknesses. This proposal advances hardware security testing by introducing a more efficient, adaptive, and systematic framework for protecting modern processors. When unleashed on Intel Skylake-X and Raptor Lake microarchitectures, our RL agent was indeed able to generate instruction sequences that cause significant observable byte leakages through transient execution without generating any $μ$code assists, faults or interrupts. The newly identified leaky sequences stem from a variety of Intel instructions, e.g. including SERIALIZE, VERR/VERW, CLMUL, MMX-x87 transitions, LSL+RDSCP and LAR. These initial results give credence to the proposed approach.

## 研究问题

摘要级初步判断（未核验正文）：We propose using reinforcement learning to address the challenges of discovering microarchitectural vulnerabilities, such as Spectre and Meltdown, which exploit subtle interactions in modern processors. Traditional methods like random fuzzing fail to efficiently explore the vast instruction space and often miss vulnerabilities that manifest under specific conditions. To overcome this, we introduce an intelligent, feedback-driven approach using RL. Our RL agents interact with the processor, learning from real-time feedback to prioritize instruction sequences more likely to reveal vulnerabilities, significantly improving the efficiency of the discovery process. We also demonstrate that RL systems adapt effectively to various microarchitectures, providing a scalable solution across processor generations. By automating the exploration process, we reduce the need for human intervention, enabling continuous learning that uncovers hidden vulnerabilities. Additionally, our approach detects subtle signals, such as timing anomalies or unusual cache behavior, that may indicate microarchitectural weaknesses. This proposal advances hardware security testing by introducing a more efficient, adaptive, and systematic framework for protecting modern processors. When unleashed on Intel Skylake-X and Raptor Lake microarchitectures, our RL agent was indeed able to generate instruction sequences that cause significant observable byte leakages through transient execution without generating any $μ$code assists, faults or interrupts. The newly identified leaky sequences stem from a variety of Intel instructions, e.g. including SERIALIZE, VERR/VERW, CLMUL, MMX-x87 transitions, LSL+RDSCP and LAR. These initial results give credence to the proposed approach.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《μRL: Discovering Transient Execution Vulnerabilities Using Reinforcement Learning》，初步归入“Microarchitectural Security Testing”。

## 与本仓库研究主线的关系

该条目已通过自动相关性筛选，但尚未完成人工或全文级核验。

## 结论

尚未核验正文，因此不对论文最终结论作确定性概括。

## 局限性

尚未核验正文。至少需要检查方法是否只适用于特定 ISA、处理器、协议、仿真器或人工模板，以及实验是否存在目标泄漏和基线不公平。

## 详细阅读分析

优先阅读 Introduction、Background/Threat Model、Method、Evaluation、Limitations/Discussion，并核对官方论文页、DOI、Artifact 和代码仓库。

## 后续核验问题

- 论文的在线反馈信号和最终 Oracle 分别是什么？
- 实验是否包含公平的 random、通用 RTL coverage 和领域专用 coverage 基线？
- 论文是否提供开源 Artifact、真实漏洞、CVE 或可复现 PoC？
