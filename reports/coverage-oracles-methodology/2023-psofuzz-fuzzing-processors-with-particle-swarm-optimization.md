# PSOFuzz: Fuzzing Processors with Particle Swarm Optimization

## 基本信息

- 作者：Chen Chen、Vasudev Gohil、Rahul Kande、Ahmad-Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2023-07-26
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=8）
- 证据等级：摘要级
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: processor；verification/fuzzing method: fuzz；security relevance: security, vulnerability
- 论文页面：[http://arxiv.org/abs/2307.14480v2](http://arxiv.org/abs/2307.14480v2)
- PDF：[https://arxiv.org/pdf/2307.14480v2](https://arxiv.org/pdf/2307.14480v2)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Hardware security vulnerabilities in computing systems compromise the security defenses of not only the hardware but also the software running on it. Recent research has shown that hardware fuzzing is a promising technique to efficiently detect such vulnerabilities in large-scale designs such as modern processors. However, the current fuzzing techniques do not adjust their strategies dynamically toward faster and higher design space exploration, resulting in slow vulnerability detection, evident through their low design coverage. To address this problem, we propose PSOFuzz, which uses particle swarm optimization (PSO) to schedule the mutation operators and to generate initial input programs dynamically with the objective of detecting vulnerabilities quickly. Unlike traditional PSO, which finds a single optimal solution, we use a modified PSO that dynamically computes the optimal solution for selecting mutation operators required to explore new design regions in hardware. We also address the challenge of inefficient initial seed generation by employing PSO-based seed generation. Including these optimizations, our final formulation outperforms fuzzers without PSO. Experiments show that PSOFuzz achieves up to 15.25$\times$ speedup for vulnerability detection and up to 2.22$\times$ speedup for coverage compared to the state-of-the-art simulation-based hardware fuzzer.

## 研究问题

摘要级初步判断（未核验正文）：Hardware security vulnerabilities in computing systems compromise the security defenses of not only the hardware but also the software running on it. Recent research has shown that hardware fuzzing is a promising technique to efficiently detect such vulnerabilities in large-scale designs such as modern processors. However, the current fuzzing techniques do not adjust their strategies dynamically toward faster and higher design space exploration, resulting in slow vulnerability detection, evident through their low design coverage. To address this problem, we propose PSOFuzz, which uses particle swarm optimization (PSO) to schedule the mutation operators and to generate initial input programs dynamically with the objective of detecting vulnerabilities quickly. Unlike traditional PSO, which finds a single optimal solution, we use a modified PSO that dynamically computes the optimal solution for selecting mutation operators required to explore new design regions in hardware. We also address the challenge of inefficient initial seed generation by employing PSO-based seed generation. Including these optimizations, our final formulation outperforms fuzzers without PSO. Experiments show that PSOFuzz achieves up to 15.25$\times$ speedup for vulnerability detection and up to 2.22$\times$ speedup for coverage compared to the state-of-the-art simulation-based hardware fuzzer.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《PSOFuzz: Fuzzing Processors with Particle Swarm Optimization》，初步归入“Coverage, Oracles & Fuzzing Methodology”。

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
