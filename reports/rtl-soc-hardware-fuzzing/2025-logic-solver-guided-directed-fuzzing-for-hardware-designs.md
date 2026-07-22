# Logic Solver Guided Directed Fuzzing for Hardware Designs

## 基本信息

- 作者：Raghul Saravanan、Sai Manoj P D
- 发表日期：2025-09-30
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=7）
- 证据等级：摘要级
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: processor, rtl；verification/fuzzing method: fuzz, coverage-guided, verification
- 论文页面：[http://arxiv.org/abs/2509.26509v1](http://arxiv.org/abs/2509.26509v1)
- PDF：[https://arxiv.org/pdf/2509.26509v1](https://arxiv.org/pdf/2509.26509v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

The ever-increasing complexity of design specifications for processors and intellectual property (IP) presents a formidable challenge for early bug detection in the modern IC design cycle. The recent advancements in hardware fuzzing have proven effective in detecting bugs in RTL designs of cutting-edge processors. The modern IC design flow involves incremental updates and modifications to the hardware designs necessitating rigorous verification and extending the overall verification period. To accelerate this process, directed fuzzing has emerged focusing on generating targeted stimuli for specific regions of the design, avoiding the need for exhaustive, full-scale verification. However, a significant limitation of these hardware fuzzers lies in their reliance on an equivalent SW model of the hardware which fails to capture intrinsic hardware characteristics. To circumvent the aforementioned challenges, this work introduces TargetFuzz, an innovative and scalable targeted hardware fuzzing mechanism. It leverages SAT-based techniques to focus on specific regions of the hardware design while operating at its native hardware abstraction level, ensuring a more precise and comprehensive verification process. We evaluated this approach across a diverse range of RTL designs for various IP cores. Our experimental results demonstrate its capability to effectively target and fuzz a broad spectrum of sites within these designs, showcasing its extensive coverage and precision in addressing targeted regions. TargetFuzz demonstrates its capability to effectively scale 30x greater in terms of handling target sites, achieving 100% state coverage and 1.5x faster in terms of site coverage, and shows 90x improvement in target state coverage compared to Coverage-Guided Fuzzing, demonstrating its potential to advance the state-of-the-art in directed hardware fuzzing.

## 研究问题

摘要级初步判断（未核验正文）：The ever-increasing complexity of design specifications for processors and intellectual property (IP) presents a formidable challenge for early bug detection in the modern IC design cycle. The recent advancements in hardware fuzzing have proven effective in detecting bugs in RTL designs of cutting-edge processors. The modern IC design flow involves incremental updates and modifications to the hardware designs necessitating rigorous verification and extending the overall verification period. To accelerate this process, directed fuzzing has emerged focusing on generating targeted stimuli for specific regions of the design, avoiding the need for exhaustive, full-scale verification. However, a significant limitation of these hardware fuzzers lies in their reliance on an equivalent SW model of the hardware which fails to capture intrinsic hardware characteristics. To circumvent the aforementioned challenges, this work introduces TargetFuzz, an innovative and scalable targeted hardware fuzzing mechanism. It leverages SAT-based techniques to focus on specific regions of the hardware design while operating at its native hardware abstraction level, ensuring a more precise and comprehensive verification process. We evaluated this approach across a diverse range of RTL designs for various IP cores. Our experimental results demonstrate its capability to effectively target and fuzz a broad spectrum of sites within these designs, showcasing its extensive coverage and precision in addressing targeted regions. TargetFuzz demonstrates its capability to effectively scale 30x greater in terms of handling target sites, achieving 100% state coverage and 1.5x faster in terms of site coverage, and shows 90x improvement in target state coverage compared to Coverage-Guided Fuzzing, demonstrating its potential to advance the state-of-the-art in directed hardware fuzzing.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Logic Solver Guided Directed Fuzzing for Hardware Designs》，初步归入“RTL & SoC Hardware Fuzzing”。

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
