# Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation

## 基本信息

- 作者：Mengdi Lu、Steven Ding、Furkan Alaca、Philippe Charland
- 发表日期：2025-09-23
- 更新日期：2025-09-23
- 来源：arXiv
- 来源编号：2509.19533v1
- 研究类别：Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2509.19533v1](http://arxiv.org/abs/2509.19533v1)
- PDF：[https://arxiv.org/pdf/2509.19533v1](https://arxiv.org/pdf/2509.19533v1)
- 分析模式：仅元数据分析

## 摘要

Security vulnerabilities in Internet-of-Things devices, mobile platforms, and autonomous systems remain critical. Traditional mutation-based fuzzers -- while effectively explore code paths -- primarily perform byte- or bit-level edits without semantic reasoning. Coverage-guided tools such as AFL++ use dictionaries, grammars, and splicing heuristics to impose shallow structural constraints, leaving deeper protocol logic, inter-field dependencies, and domain-specific semantics unaddressed. Conversely, reasoning-capable large language models (LLMs) can leverage pretraining knowledge to understand input formats, respect complex constraints, and propose targeted mutations, much like an experienced reverse engineer or testing expert. However, lacking ground truth for "correct" mutation reasoning makes supervised fine-tuning impractical, motivating explorations of off-the-shelf LLMs via prompt-based few-shot learning. To bridge this gap, we present an open-source microservices framework that integrates reasoning LLMs with AFL++ on Google's FuzzBench, tackling asynchronous execution and divergent hardware demands (GPU- vs. CPU-intensive) of LLMs and fuzzers. We evaluate four research questions: (R1) How can reasoning LLMs be integrated into the fuzzing mutation loop? (R2) Do few-shot prompts yield higher-quality mutations than zero-shot? (R3) Can prompt engineering with off-the-shelf models improve fuzzing directly? and (R4) Which open-source reasoning LLMs perform best under prompt-only conditions? Experiments with Llama3.3, Deepseek-r1-Distill-Llama-70B, QwQ-32B, and Gemma3 highlight Deepseek as the most promising. Mutation effectiveness depends more on prompt complexity and model choice than shot count. Response latency and throughput bottlenecks remain key obstacles, offering directions for future work.

## 研究问题

Security vulnerabilities in Internet-of-Things devices, mobile platforms, and autonomous systems remain critical. Traditional mutation-based fuzzers -- while effectively explore code paths -- primarily perform byte- or bit-level edits without semantic reasoning. Coverage-guided tools such as AFL++ use dictionaries, grammars, and splicing heuristics to impose shallow structural constraints, leaving deeper protocol logic, inter-field dependencies, and domain-specific semantics unaddressed. Conversely, reasoning-capable large language models (LLMs) can leverage pretraining knowledge to understand input formats, respect complex constraints, and propose targeted mutations, much like an experienced reverse engineer or testing expert. However, lacking ground truth for "correct" mutation reasoning makes supervised fine-tuning impractical, motivating explorations of off-the-shelf LLMs via prompt-based few-shot learning. To bridge this gap, we present an open-source microservices framework that integrates reasoning LLMs with AFL++ on Google's FuzzBench, tackling asynchronous execution and divergent hardware demands (GPU- vs. CPU-intensive) of LLMs and fuzzers. We evaluate four research questions: (R1) How can reasoning LLMs be integrated into the fuzzing mutation loop? (R2) Do few-shot prompts yield higher-quality mutations than zero-shot? (R3) Can prompt engineering with off-the-shelf models improve fuzzing directly? and (R4) Which open-source reasoning LLMs perform best under prompt-only conditions? Experiments with Llama3.3, Deepseek-r1-Distill-Llama-70B, QwQ-32B, and Gemma3 highlight Deepseek as the most promising. Mutation effectiveness depends more on prompt complexity and model choice than shot count. Response latency and throughput bottlenecks remain key obstacles, offering directions for future work.

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
