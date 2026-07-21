# ArchXBench: A Complex Digital Systems Benchmark Suite for LLM Driven RTL Synthesis

## 基本信息

- 作者：Suresh Purini、Siddhant Garg、Mudit Gaur、Sankalp Bhat、Sohan Mupparapu、Arun Ravindran
- 发表日期：2025-08-08
- 更新日期：2025-08-08
- 来源：arXiv
- 来源编号：2508.06047v1
- 研究类别：RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2508.06047v1](http://arxiv.org/abs/2508.06047v1)
- PDF：[https://arxiv.org/pdf/2508.06047v1](https://arxiv.org/pdf/2508.06047v1)
- 分析模式：仅元数据分析

## 摘要

Modern SoC datapaths include deeply pipelined, domain-specific accelerators, but their RTL implementation and verification are still mostly done by hand. While large language models (LLMs) exhibit advanced code-generation abilities for programming languages like Python, their application to Verilog-like RTL remains in its nascent stage. This is reflected in the simple arithmetic and control circuits currently used to evaluate generative capabilities in existing benchmarks. In this paper, we introduce ArchXBench, a six-level benchmark suite that encompasses complex arithmetic circuits and other advanced digital subsystems drawn from domains such as cryptography, image processing, machine learning, and signal processing. Architecturally, some of these designs are purely combinational, others are multi-cycle or pipelined, and many require hierarchical composition of modules. For each benchmark, we provide a problem description, design specification, and testbench, enabling rapid research in the area of LLM-driven agentic approaches for complex digital systems design. Using zero-shot prompting with Claude Sonnet 4, GPT 4.1, o4-mini-high, and DeepSeek R1 under a pass@5 criterion, we observed that o4-mini-high successfully solves the largest number of benchmarks, 16 out of 30, spanning Levels 1, 2, and 3. From Level 4 onward, however, all models consistently fail, highlighting a clear gap in the capabilities of current state-of-the-art LLMs and prompting/agentic approaches.

## 研究问题

Modern SoC datapaths include deeply pipelined, domain-specific accelerators, but their RTL implementation and verification are still mostly done by hand. While large language models (LLMs) exhibit advanced code-generation abilities for programming languages like Python, their application to Verilog-like RTL remains in its nascent stage. This is reflected in the simple arithmetic and control circuits currently used to evaluate generative capabilities in existing benchmarks. In this paper, we introduce ArchXBench, a six-level benchmark suite that encompasses complex arithmetic circuits and other advanced digital subsystems drawn from domains such as cryptography, image processing, machine learning, and signal processing. Architecturally, some of these designs are purely combinational, others are multi-cycle or pipelined, and many require hierarchical composition of modules. For each benchmark, we provide a problem description, design specification, and testbench, enabling rapid research in the area of LLM-driven agentic approaches for complex digital systems design. Using zero-shot prompting with Claude Sonnet 4, GPT 4.1, o4-mini-high, and DeepSeek R1 under a pass@5 criterion, we observed that o4-mini-high successfully solves the largest number of benchmarks, 16 out of 30, spanning Levels 1, 2, and 3. From Level 4 onward, however, all models consistently fail, highlighting a clear gap in the capabilities of current state-of-the-art LLMs and prompting/agentic approaches.

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
