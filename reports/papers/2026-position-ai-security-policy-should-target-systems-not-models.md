# Position: AI Security Policy Should Target Systems, Not Models

## 基本信息

- 作者：Michael A. Riegler、Inga Strümke
- 发表日期：2026-05-10
- 更新日期：2026-05-10
- 来源：arXiv
- 来源编号：2605.09504v1
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2605.09504v1](http://arxiv.org/abs/2605.09504v1)
- PDF：[https://arxiv.org/pdf/2605.09504v1](https://arxiv.org/pdf/2605.09504v1)
- 分析模式：仅元数据分析

## 摘要

We present swarm-attack, an open-source adversarial testing framework in which multiple lightweight LLM agents coordinate through shared memory, parallel exploration, and evolutionary optimization. Together, our results demonstrate that both safety bypass of frontier models and software vulnerability discovery, i.e., the capability class that motivated restricted release of Anthropic's Mythos Preview, are achievable at effectively zero cost using commodity hardware and openly available models. We report two experiments. In the first, five instances of a 1.2 billion parameter model conducted 225 jailbreak attacks each against GPT-4o and Claude Sonnet~4. Against GPT-4o, the swarm achieved an Effective Harm Rate of 45.8%, producing 49 critical-severity breaches; against Claude Sonnet-4, the Effective Harm Rate was 0% despite a 40% technical success rate. In the second experiment, the same models performed combined source code analysis and binary fuzzing against a vulnerable C application with 9 planted CWEs. With a hand-crafted exploit seed corpus, regex pattern detection, and AddressSanitizer-based crash classification, the pipeline recovers 9 of 9 vulnerabilities (100% recall) in approximately four minutes on a consumer MacBook. With those scaffold components disabled, the same model recovers 0 of 9 by crash verification and 2 of 9 by citation. The capability class that motivated restricted release of Anthropic's Mythos Preview is therefore reproducible at effectively zero cost; the important enabler is the system scaffold itself, which compensates for the limited reasoning capacity of small individual models.

## 研究问题

We present swarm-attack, an open-source adversarial testing framework in which multiple lightweight LLM agents coordinate through shared memory, parallel exploration, and evolutionary optimization. Together, our results demonstrate that both safety bypass of frontier models and software vulnerability discovery, i.e., the capability class that motivated restricted release of Anthropic's Mythos Preview, are achievable at effectively zero cost using commodity hardware and openly available models. We report two experiments. In the first, five instances of a 1.2 billion parameter model conducted 225 jailbreak attacks each against GPT-4o and Claude Sonnet~4. Against GPT-4o, the swarm achieved an Effective Harm Rate of 45.8%, producing 49 critical-severity breaches; against Claude Sonnet-4, the Effective Harm Rate was 0% despite a 40% technical success rate. In the second experiment, the same models performed combined source code analysis and binary fuzzing against a vulnerable C application with 9 planted CWEs. With a hand-crafted exploit seed corpus, regex pattern detection, and AddressSanitizer-based crash classification, the pipeline recovers 9 of 9 vulnerabilities (100% recall) in approximately four minutes on a consumer MacBook. With those scaffold components disabled, the same model recovers 0 of 9 by crash verification and 2 of 9 by citation. The capability class that motivated restricted release of Anthropic's Mythos Preview is therefore reproducible at effectively zero cost; the important enabler is the system scaffold itself, which compensates for the limited reasoning capacity of small individual models.

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
