# When Fuzzing Meets Understanding: LLM-Driven Semantic Test Generation for RTL Verification

## 基本信息

- 作者：Kun Wang、Cangyuan Li、Kaiyan Chang、Siyang Cai、Yinhe Han、Ying Wang
- 发表日期：2026-07-11
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2607.10340v1](http://arxiv.org/abs/2607.10340v1)
- PDF：[https://arxiv.org/pdf/2607.10340v1](https://arxiv.org/pdf/2607.10340v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 10 页，提取 53573 字符

## 摘要

The growing complexity of modern chips poses significant challenges to hardware verification. In recent years, coverage-guided fuzzing has emerged as a promising approach for improving verification efficiency. However, existing hardware fuzzers still struggle to achieve high coverage and expose corner-case bugs, as they predominantly rely on heuristic strategies with limited ability to reason about the internal logic and semantic behavior of the design under test (DUT). In this work, we propose ChipFuzzer, a hardware fuzzing framework that leverages the semantic reasoning capabilities of large language models (LLMs) to improve fuzzing effectiveness. ChipFuzzer adopts a dual-stage workflow comprising a Coverage-Guided stage and a Bug-Guided stage. In the Coverage-Guided stage, ChipFuzzer employs control-flow similarity and discrepancy analysis to guide LLM-driven testcase generation, thereby improving coverage. In the Bug-Guided stage, ChipFuzzer leverages historical bug data to identify bug-prone code regions and prioritize testcase generation for those regions, thus enhancing bug discovery efficiency. Experimental results on three open-source CPU designs show that ChipFuzzer improves average condition coverage by 5.8 percentage points and bug detection rate by 21.1 percentage points over the strongest baseline.

## 研究问题

现有硬件fuzzers依赖启发式策略，缺乏对DUT内部逻辑和语义的推理能力，导致覆盖率低且难以发现角落bug。

## Introduction 梳理

形式化方法存在状态爆炸问题，模拟验证中覆盖引导fuzzing仅能达到约80%覆盖率且增长缓慢。本文提出ChipFuzzer，利用LLM的语义推理能力进行双阶段fuzzing：覆盖引导阶段通过控制流相似性索引和差异分析生成针对未覆盖代码的测试用例；bug引导阶段利用历史bug数据聚焦bug易发区域。

## 方法

输入生成：LLM基于目标代码段、检索的相似测试用例模板及差异分析结果生成测试用例。反馈/coverage：使用条件覆盖率、寄存器翻转覆盖率、多路选择器翻转覆盖率作为反馈。Oracle：差分检测，比较RTL模拟器（Verilator）和ISA模拟器（Spike）的输出。DUT/平台：RocketCore、BOOM（Chisel）、CVA6（SystemVerilog）。是否需要golden model：是，Spike作为ISA参考模型。

## 实验与评估

baseline：TheHuzz、Cascade、BMCFuzz。实验预算：24小时fuzzing。统计：覆盖率曲线、平均条件覆盖率提升5.8个百分点，bug检测率提升21.1个百分点。bug：使用Encarsia平台90个bug，ChipFuzzer检测率61.1%。开销：LLM推理导致初期测试用例吞吐量较低。Artifact：代码公开链接（https://anonymous.4open.science/r/ChipFuzzer-212B）。

## 核心贡献

提出LLM驱动的双阶段硬件fuzzing框架，引入控制流相似性索引、差异分析、历史bug引导和语义种子融合策略。

## 与本仓库研究主线的关系

直接相关：属于RTL/SoC硬件Fuzzing类别，但未专门涉及多hart或内存一致性验证。

## 结论

ChipFuzzer在三个开源CPU设计和Encarsia基准上提升了覆盖率和bug检测能力，展示了LLM在硬件验证中的潜力。

## 局限性

依赖LLM的推理质量，可能产生硬件语义幻觉；LLM生成测试用例的吞吐量低于传统变异方法；评估仅针对开源RISC-V CPU设计，对更广泛RTL设计的有效性需进一步研究。

## 详细阅读分析

True

## 后续核验问题

- 如何量化LLM对硬件语义的幻觉并设计修复机制？
- 历史bug先验在不同CPU设计间的可迁移性如何？
- 能否将双阶段框架扩展到多hart/一致性场景？
