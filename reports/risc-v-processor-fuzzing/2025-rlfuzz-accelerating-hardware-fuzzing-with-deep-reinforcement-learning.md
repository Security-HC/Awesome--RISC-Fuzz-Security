# RLFuzz: Accelerating Hardware Fuzzing with Deep Reinforcement Learning

## 基本信息

- 作者：Raphael Götz、Christoph Sendner、Nico Ruck、Mohamadreza Rostami、Alexandra Dmitrienko、Ahmad Sadeghi
- 发表日期：2025-05-05
- 会议/期刊：IEEE International Symposium on Hardware Oriented Security and Trust
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=9）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: risc-v, processor；verification/fuzzing method: fuzz, verification, formal verification
- 论文页面：[https://doi.org/10.1109/HOST64725.2025.11050051](https://doi.org/10.1109/HOST64725.2025.11050051)
- PDF：未记录
- 分析模式：摘要级占位（未全文核验）

## 摘要

Once hardware is manufactured, it becomes immutable, and any design flaws or vulnerabilities are permanent. Therefore, comprehensive testing of hardware designs is essential before production. However, the increasing complexity of modern processors makes static analysis and formal verification increasingly challenging. Fuzzing is a highly effective technique for detecting software vulnerabilities but adapting it to hardware presents unique challenges due to the fundamental differences between software and hardware. However, the current state-of-the-art in hardware fuzzing still has significant limitations, particularly in terms of performance, practicality, and the need for human intervention. To address these issues, we introduce RLFuzz, a novel hardware fuzzer that employs reinforcement learning to explore processors autonomously, achieving faster and more comprehensive coverage. Reinforcement learning enables the fuzzer to learn from its interactions with the processor without requiring labeled data, allowing it to more effectively select modifications for test cases and target previously unexplored areas. RLFuzz uses an asynchronous training mechanism that permits concurrent fuzzing and neural network training. To optimize RLFuzz, we performed an extensive evaluation of various deep Q-learning optimization techniques and hyperparameters. We then tested the optimized fuzzer on three complex RISC-V cores-the Rocket core, CVA6, and BOOM-and compared its performance to a current hardware fuzzer, TheHuzz [20]. Our results show that RLFuzz achieved up to 1.77 % higher coverage, and on average 2.35 times faster, and demonstrated a maximum speedup of up to 6.93 times. For branch coverage, the average speedup was 7.85 times, with a peak speedup of 92.98 times. Additionally, RLFuzz needed less time to complete 100,000 test cases and did not require any human intervention.

## 研究问题

摘要级初步判断（未核验正文）：Once hardware is manufactured, it becomes immutable, and any design flaws or vulnerabilities are permanent. Therefore, comprehensive testing of hardware designs is essential before production. However, the increasing complexity of modern processors makes static analysis and formal verification increasingly challenging. Fuzzing is a highly effective technique for detecting software vulnerabilities but adapting it to hardware presents unique challenges due to the fundamental differences between software and hardware. However, the current state-of-the-art in hardware fuzzing still has significant limitations, particularly in terms of performance, practicality, and the need for human intervention. To address these issues, we introduce RLFuzz, a novel hardware fuzzer that employs reinforcement learning to explore processors autonomously, achieving faster and more comprehensive coverage. Reinforcement learning enables the fuzzer to learn from its interactions with the processor without requiring labeled data, allowing it to more effectively select modifications for test cases and target previously unexplored areas. RLFuzz uses an asynchronous training mechanism that permits concurrent fuzzing and neural network training. To optimize RLFuzz, we performed an extensive evaluation of various deep Q-learning optimization techniques and hyperparameters. We then tested the optimized fuzzer on three complex RISC-V cores-the Rocket core, CVA6, and BOOM-and compared its performance to a current hardware fuzzer, TheHuzz [20]. Our results show that RLFuzz achieved up to 1.77 % higher coverage, and on average 2.35 times faster, and demonstrated a maximum speedup of up to 6.93 times. For branch coverage, the average speedup was 7.85 times, with a peak speedup of 92.98 times. Additionally, RLFuzz needed less time to complete 100,000 test cases and did not require any human intervention.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《RLFuzz: Accelerating Hardware Fuzzing with Deep Reinforcement Learning》，初步归入“RISC-V Processor Fuzzing”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
