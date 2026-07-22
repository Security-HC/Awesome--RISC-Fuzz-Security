# Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation

## 基本信息

- 作者：Mengdi Lu、Steven Ding、Furkan Alaca、Philippe Charland
- 发表日期：2025-09-23
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: cpu；verification/fuzzing method: fuzz, coverage-guided；security relevance: security
- 论文页面：[http://arxiv.org/abs/2509.19533v1](http://arxiv.org/abs/2509.19533v1)
- PDF：[https://arxiv.org/pdf/2509.19533v1](https://arxiv.org/pdf/2509.19533v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 16 页，提取 100000 字符

## 摘要

Security vulnerabilities in Internet-of-Things devices, mobile platforms, and autonomous systems remain critical. Traditional mutation-based fuzzers -- while effectively explore code paths -- primarily perform byte- or bit-level edits without semantic reasoning. Coverage-guided tools such as AFL++ use dictionaries, grammars, and splicing heuristics to impose shallow structural constraints, leaving deeper protocol logic, inter-field dependencies, and domain-specific semantics unaddressed. Conversely, reasoning-capable large language models (LLMs) can leverage pretraining knowledge to understand input formats, respect complex constraints, and propose targeted mutations, much like an experienced reverse engineer or testing expert. However, lacking ground truth for "correct" mutation reasoning makes supervised fine-tuning impractical, motivating explorations of off-the-shelf LLMs via prompt-based few-shot learning. To bridge this gap, we present an open-source microservices framework that integrates reasoning LLMs with AFL++ on Google's FuzzBench, tackling asynchronous execution and divergent hardware demands (GPU- vs. CPU-intensive) of LLMs and fuzzers. We evaluate four research questions: (R1) How can reasoning LLMs be integrated into the fuzzing mutation loop? (R2) Do few-shot prompts yield higher-quality mutations than zero-shot? (R3) Can prompt engineering with off-the-shelf models improve fuzzing directly? and (R4) Which open-source reasoning LLMs perform best under prompt-only conditions? Experiments with Llama3.3, Deepseek-r1-Distill-Llama-70B, QwQ-32B, and Gemma3 highlight Deepseek as the most promising. Mutation effectiveness depends more on prompt complexity and model choice than shot count. Response latency and throughput bottlenecks remain key obstacles, offering directions for future work.

## 研究问题

传统基于突变的模糊测试器（如AFL++）仅进行字节/位级编辑，缺乏语义推理，无法深入协议逻辑和域语义。推理型LLM可理解输入格式并生成针对性突变，但缺乏监督微调的ground truth。本文旨在通过提示工程集成现成推理LLM到突变循环中。

## Introduction 梳理

现有覆盖引导模糊测试使用字典、语法等浅层结构约束，未解决深层协议逻辑和域语义；LLM-based模糊测试将LLM视为黑盒，忽略中间推理步骤。本文贡献：提出开源微服务框架，将推理LLM与AFL++集成于FuzzBench，无需微调；首次系统研究推理LLM用于突变式二进制模糊测试，对比0-shot、1-shot、3-shot，评估四个开源推理LLM。

## 方法

输入生成：初始种子来自FuzzBench seed pool；反馈/coverage：AFL++覆盖位图；Oracle：通过崩溃/超时和覆盖新路径判断；DUT/平台：25个FuzzBench基准（来自OSS-Fuzz），Ubuntu 20.04，Intel Xeon Gold 5218 CPU，NVIDIA Quadro RTX 6000 GPU；无需golden model。具体方法：custom_mutator hook扩展AFL++，Redis队列解耦，Ollama部署LLM，llm_fuzz服务生成提示。突变策略：先AFL++默认突变，后LLM突变（2000字节分片，十六进制转换，提示工程设计含角色扮演、任务澄清、指令分解、链式推理、few-shot示例）。提示shot：0-shot、1-shot、3-shot，温度0.0。

## 实验与评估

Baseline：AFL++、AFL、LibFuzzer（主baseline为AFL++）；实验预算：1小时和4小时运行，3次独立试验；统计：CIP、SCR、RDR；bug/CVE：未报告具体CVE，评估覆盖率和崩溃/挂起；开销：Ollama响应超时约35%，LLM延迟和吞吐量瓶颈；Artifact：开源框架发布。

## 核心贡献

开源微服务框架集成推理LLM与AFL++；首次系统比较不同shot策略和四个推理LLM；发现平衡语法正确性和多样性重要；提供经验性基线。

## 与本仓库研究主线的关系

方法借鉴：LLM引导的覆盖模糊测试可推广到硬件模糊测试，但本文不针对RISC-V/处理器或多hart一致性。属于强邻近领域，提供通用方法论。

## 结论

提出集成推理LLM与AFL++的框架，实验表明增加shots不线性改善覆盖；无单一LLM一致优于baseline；Llama3.3早期表现好，Deepseek-r1-Distill-Llama-70B长期表现好；平衡语法正确性和响应多样性关键；延迟和超时是障碍。

## 局限性

1）突变有时偏离格式；2）LLM缺乏原生二进制支持；3）大输入可能超token或超时；4）实验规模受时间和资源限制；5）Fuzzbench仅保留一次试验详细报告。

## 详细阅读分析

建议深入阅读Method 2.2数据流、2.4提示优化和Evaluation 4.2-4.4部分。

## 后续核验问题

- 如何将LLM推理应用于硬件模糊测试的输入生成？
- 在多hart一致性验证中，如何利用LLM生成覆盖复杂内存模型的输入？
