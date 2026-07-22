# Logic Solver Guided Directed Fuzzing for Hardware Designs

## 基本信息

- 作者：Raghul Saravanan、Sai Manoj P D
- 发表日期：2025-09-30
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=7）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: processor, rtl；verification/fuzzing method: fuzz, coverage-guided, verification
- 论文页面：[http://arxiv.org/abs/2509.26509v1](http://arxiv.org/abs/2509.26509v1)
- PDF：[https://arxiv.org/pdf/2509.26509v1](https://arxiv.org/pdf/2509.26509v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 7 页，提取 38304 字符

## 摘要

The ever-increasing complexity of design specifications for processors and intellectual property (IP) presents a formidable challenge for early bug detection in the modern IC design cycle. The recent advancements in hardware fuzzing have proven effective in detecting bugs in RTL designs of cutting-edge processors. The modern IC design flow involves incremental updates and modifications to the hardware designs necessitating rigorous verification and extending the overall verification period. To accelerate this process, directed fuzzing has emerged focusing on generating targeted stimuli for specific regions of the design, avoiding the need for exhaustive, full-scale verification. However, a significant limitation of these hardware fuzzers lies in their reliance on an equivalent SW model of the hardware which fails to capture intrinsic hardware characteristics. To circumvent the aforementioned challenges, this work introduces TargetFuzz, an innovative and scalable targeted hardware fuzzing mechanism. It leverages SAT-based techniques to focus on specific regions of the hardware design while operating at its native hardware abstraction level, ensuring a more precise and comprehensive verification process. We evaluated this approach across a diverse range of RTL designs for various IP cores. Our experimental results demonstrate its capability to effectively target and fuzz a broad spectrum of sites within these designs, showcasing its extensive coverage and precision in addressing targeted regions. TargetFuzz demonstrates its capability to effectively scale 30x greater in terms of handling target sites, achieving 100% state coverage and 1.5x faster in terms of site coverage, and shows 90x improvement in target state coverage compared to Coverage-Guided Fuzzing, demonstrating its potential to advance the state-of-the-art in directed hardware fuzzing.

## 研究问题

现有硬件定向模糊测试（如DirectFuzz）依赖软件模型，无法捕获硬件固有特性，且难以到达目标状态。

## Introduction 梳理

硬件验证面临复杂性和可扩展性挑战。动态和形式化方法效率低。硬件模糊测试虽有效，但现有CGF和DGF（如DirectFuzz）将RTL翻译为软件模型，丢失硬件特性，无法有效到达目标状态。本文提出TargetFuzz，利用SAT求解器在原生硬件抽象级生成定向输入，加速验证。

## 方法

输入生成：基于SAT求解器，对门级网表编码的布尔方程求解，生成满足目标状态的输入模式（可控制汉明距离防冗余）。反馈/覆盖度：提取目标状态覆盖度和目标站点覆盖度（通过EDA工具如Cadence IMC）。Oracle：不需要Golden Model（仅仿真后提取覆盖，无输出比较）。DUT/平台：RTL设计（包括PicoRV32、or1200等），使用Cadence Genus综合，PySAT求解器，Cadence Xcelium仿真。

## 实验与评估

Baseline：Coverage-Guided Fuzzing (CGF) 类似RFUZZ。实验预算：每个CGF运行15次取均值，TargetFuzz运行1次。统计：TargetFuzz实现100%目标状态覆盖（除个别设计外），平均目标站点覆盖98.9%，生成时间平均0.5秒。与CGF相比，目标站点覆盖快1.5倍，目标状态覆盖提升90倍。Bug/CVE：未确认（仅覆盖评估）。开销：生成输入时间，最大2.73秒（AES）。Artifact：未确认（未提供代码或开源）。

## 核心贡献

首次将SAT求解器应用于定向硬件模糊测试；提出目标状态覆盖度和目标站点覆盖度指标；在原生硬件抽象级实现高效定向测试；实验证明覆盖和速度优势。

## 与本仓库研究主线的关系

直接相关：属于RTL/SoC硬件Fuzzing主题。但与多hart/内存一致性路径无直接关联（本文仅单核设计）。方法可借鉴用于生成特定一致性场景的输入。

## 结论

TargetFuzz是首个在原生硬件抽象级利用SAT求解器的定向模糊测试方法，能高效生成输入到达目标状态，实现100%目标状态覆盖，显著优于CGF，且可扩展至复杂设计。

## 局限性

需要综合为门级网表，引入前期开销；目标站点选择可能需人工干预；对时序电路假设全扫描访问；未评估实际漏洞检测能力；可扩展性仅通过门数衡量，未涉及大规模SoC。

## 详细阅读分析

建议阅读RFUZZ [19]、DirectFuzz [20]、HyPFuzz [14]、DifuzzRTL [15] 等相关定向与覆盖率引导模糊测试工作。

## 后续核验问题

- 如何将TargetFuzz扩展到多核或SoC？如何自动选取目标状态？能否与形式化方法结合检测复杂漏洞？能否处理时序敏感的状态？
