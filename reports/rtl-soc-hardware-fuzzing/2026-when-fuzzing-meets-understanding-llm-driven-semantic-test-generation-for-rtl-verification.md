# When Fuzzing Meets Understanding: LLM-Driven Semantic Test Generation for RTL Verification

## 基本信息

- 作者：Kun Wang、Cangyuan Li、Kaiyan Chang、Siyang Cai、Yinhe Han、Ying Wang
- 发表日期：2026-07-11
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：摘要级
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2607.10340v1](http://arxiv.org/abs/2607.10340v1)
- PDF：[https://arxiv.org/pdf/2607.10340v1](https://arxiv.org/pdf/2607.10340v1)
- 分析模式：DeepSeek PDF 首 8 页与末 2 页文本：deepseek-v4-flash

## 摘要

The growing complexity of modern chips poses significant challenges to hardware verification. In recent years, coverage-guided fuzzing has emerged as a promising approach for improving verification efficiency. However, existing hardware fuzzers still struggle to achieve high coverage and expose corner-case bugs, as they predominantly rely on heuristic strategies with limited ability to reason about the internal logic and semantic behavior of the design under test (DUT). In this work, we propose ChipFuzzer, a hardware fuzzing framework that leverages the semantic reasoning capabilities of large language models (LLMs) to improve fuzzing effectiveness. ChipFuzzer adopts a dual-stage workflow comprising a Coverage-Guided stage and a Bug-Guided stage. In the Coverage-Guided stage, ChipFuzzer employs control-flow similarity and discrepancy analysis to guide LLM-driven testcase generation, thereby improving coverage. In the Bug-Guided stage, ChipFuzzer leverages historical bug data to identify bug-prone code regions and prioritize testcase generation for those regions, thus enhancing bug discovery efficiency. Experimental results on three open-source CPU designs show that ChipFuzzer improves average condition coverage by 5.8 percentage points and bug detection rate by 21.1 percentage points over the strongest baseline.

## 研究问题

现有硬件fuzzer主要依赖启发式策略，缺乏对DUT内部逻辑和语义行为的推理能力，导致覆盖率有限且难以发现角落bug。

## Introduction 梳理

芯片复杂性增加，验证消耗超70%项目资源。形式验证面临状态空间爆炸，仿真验证中覆盖引导fuzzing虽常用但存在根本局限：现有方法采用输入中心思路，忽略HDL信号的结构语义，无法深入理解DUT功能，导致覆盖率仅约80%且增长平缓。LLM在硬件代码生成和验证中展现出语义推理潜力。本文提出ChipFuzzer，利用LLM的语义推理进行双阶段fuzzing：覆盖引导阶段通过控制流相似性索引和差异分析指导生成覆盖目标区域的测试；bug引导阶段利用历史bug数据优先测试易错区域。贡献包括框架设计、两种引导策略及实验验证。

## 方法

输入生成：LLM根据目标代码段、从种子库中检索的控制流最相似测试模板、差异分析结果，生成候选RISC-V测试程序。反馈/coverage：使用条件覆盖率、寄存器toggle覆盖率、多路选择器toggle覆盖率作为反馈；覆盖引导阶段优先选择未覆盖代码段，bug引导阶段选择历史bug易发区域。Oracle：差分分析——RTL模拟（Verilator）结果与ISA黄金模型（Spike）对比。DUT/平台：RocketCore（Chisel）、BOOM（Chisel）、CV A6（SystemVerilog），使用PyVerilog解析，RISC-V工具链编译。是否需要golden model：是，Spike作为指令集精确参考。

## 实验与评估

Baseline：TheHuzz、Cascade、BMCFuzz。实验预算：24小时fuzzing。统计：平均条件覆盖率提升5.8个百分点（绝对），bug检测率提升21.1个百分点；在RocketCore上条件覆盖率从80.06%（BMCFuzz）提升至89.2%；Bug检测：Encarsia平台90个bug中ChipFuzzer检出61.1%（55个），Baseline最高40%。开销：LLM推理导致早期测试生成吞吐量低，但后期持续提升。Artifact：代码已匿名公开（https://anonymous.4open.science/r/ChipFuzzer-212B）。

## 核心贡献

1. 提出ChipFuzzer，首个利用LLM语义推理进行双阶段硬件fuzzing的框架。2. 覆盖引导阶段引入控制流相似性索引与差异分析，指导LLM生成覆盖未达代码的测试。3. bug引导阶段利用历史bug数据识别三类易错区域，并设计语义感知种子融合策略。4. 在三个RISC-V CPU上实验证明覆盖率和bug检测率显著优于现有fuzzer。

## 与本仓库研究主线的关系

直接相关：属于RTL硬件fuzzing，使用RISC-V处理器DUT。与多hart/一致性路径研究：论文未涉及多hart或内存一致性，方法目前针对单核，但控制流分析和语义推理思路可潜在扩展到多核共享资源验证，属于强邻近领域，方法有借鉴价值。

## 结论

ChipFuzzer通过语义引导的生成显著提升覆盖率和bug检测。实验表明其优势，但存在依赖LLM推理质量、高开销、评估范围限于开源RISC-V CPU等局限。

## 局限性

依赖LLM推理质量，可能产生硬件语义幻觉；LLM推理导致早期测试吞吐量低；当前评估仅覆盖开源RISC-V CPU设计，对其他RTL设计有效性未知。

## 详细阅读分析

需要进一步阅读论文以下细节：差异分析的五条规则如何自动化执行？历史bug语料库的构建标准和128个PR的具体筛选过程？种子融合策略中LLM重写的具体prompt设计？语义纠正器的执行反馈循环如何实现？LLM不同版本对结果的影响有多大？

## 后续核验问题

- 1. 如何确保LLM生成的测试用例语法正确？失败后的纠正机制效果如何？2. 差异分析的五条规则是否完全自动执行，还是需要人工干预？3. 历史bug语料库的组成和覆盖范围，是否包含多核相关bug？4. 种子融合相比简单拼接的优势是否有定量分析？5. 本方法在多核处理器（如多hart RISC-V设计）上是否有效？6. 如何评估和缓解LLM对硬件语义的幻觉问题？
