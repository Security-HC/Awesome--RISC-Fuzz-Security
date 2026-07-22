# MABFuzz: Multi-Armed Bandit Algorithms for Fuzzing Processors

## 基本信息

- 作者：Vasudev Gohil、Rahul Kande、Chen Chen、Ahmad-Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2023-11-24
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：摘要级
- 标签：RISC-V Processor Fuzzing、Microarchitectural Security Testing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2311.14594v1](http://arxiv.org/abs/2311.14594v1)
- PDF：[https://arxiv.org/pdf/2311.14594v1](https://arxiv.org/pdf/2311.14594v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

As the complexities of processors keep increasing, the task of effectively verifying their integrity and security becomes ever more daunting. The intricate web of instructions, microarchitectural features, and interdependencies woven into modern processors pose a formidable challenge for even the most diligent verification and security engineers. To tackle this growing concern, recently, researchers have developed fuzzing techniques explicitly tailored for hardware processors. However, a prevailing issue with these hardware fuzzers is their heavy reliance on static strategies to make decisions in their algorithms. To address this problem, we develop a novel dynamic and adaptive decision-making framework, MABFuzz, that uses multi-armed bandit (MAB) algorithms to fuzz processors. MABFuzz is agnostic to, and hence, applicable to, any existing hardware fuzzer. In the process of designing MABFuzz, we encounter challenges related to the compatibility of MAB algorithms with fuzzers and maximizing their efficacy for fuzzing. We overcome these challenges by modifying the fuzzing process and tailoring MAB algorithms to accommodate special requirements for hardware fuzzing. We integrate three widely used MAB algorithms in a state-of-the-art hardware fuzzer and evaluate them on three popular RISC-V-based processors. Experimental results demonstrate the ability of MABFuzz to cover a broader spectrum of processors' intricate landscapes and doing so with remarkable efficiency. In particular, MABFuzz achieves up to 308x speedup in detecting vulnerabilities and up to 5x speedup in achieving coverage compared to a state-of-the-art technique.

## 研究问题

摘要级初步判断（未核验正文）：As the complexities of processors keep increasing, the task of effectively verifying their integrity and security becomes ever more daunting. The intricate web of instructions, microarchitectural features, and interdependencies woven into modern processors pose a formidable challenge for even the most diligent verification and security engineers. To tackle this growing concern, recently, researchers have developed fuzzing techniques explicitly tailored for hardware processors. However, a prevailing issue with these hardware fuzzers is their heavy reliance on static strategies to make decisions in their algorithms. To address this problem, we develop a novel dynamic and adaptive decision-making framework, MABFuzz, that uses multi-armed bandit (MAB) algorithms to fuzz processors. MABFuzz is agnostic to, and hence, applicable to, any existing hardware fuzzer. In the process of designing MABFuzz, we encounter challenges related to the compatibility of MAB algorithms with fuzzers and maximizing their efficacy for fuzzing. We overcome these challenges by modifying the fuzzing process and tailoring MAB algorithms to accommodate special requirements for hardware fuzzing. We integrate three widely used MAB algorithms in a state-of-the-art hardware fuzzer and evaluate them on three popular RISC-V-based processors. Experimental results demonstrate the ability of MABFuzz to cover a broader spectrum of processors' intricate landscapes and doing so with remarkable efficiency. In particular, MABFuzz achieves up to 308x speedup in detecting vulnerabilities and up to 5x speedup in achieving coverage compared to a state-of-the-art technique.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《MABFuzz: Multi-Armed Bandit Algorithms for Fuzzing Processors》，初步归入“RISC-V Processor Fuzzing”。

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
