# Machine-Speed Cyber and Poisoned Cognition: A Layer- Dependent Game-Theoretic Framework, with Empirical Probes

## 基本信息

- 作者：Sergey Gordeychik
- 发表日期：2026-07-03
- 更新日期：2026-07-14
- 来源：OpenAlex
- 来源编号：https://openalex.org/W7167341608
- 研究类别：RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.24108/preprints-3115766](https://doi.org/10.24108/preprints-3115766)
- PDF：[https://preprints.ru/files/4843](https://preprints.ru/files/4843)
- 分析模式：中文元数据分析

## 摘要

Strategic analysis of AI-enabled conflict often treats "cyber" as one offense–defense game and AI ca- pability as a scalar speedup. We argue instead that AI-mediated conflict is a layered strategic envi- ronment: a wire layer of machine-speed discovery and exploitation, a model/weights layer of captured decision-support, an audit layer of verification exhaustion, and an attribution layer where punishment is slower than defection. The central claim is an inversion across layers: the observable wire layer is relatively self-correcting, while the unobservable model and audit layers can become self- reinforcing. We formalize the stack with five compact model results and seven falsifiable predictions. Two results are empirically grounded here: the wire-layer queueing claim that correlated vulnerability arrivals in- flate remediation backlogs, and the model-layer capture-bound claim that deep, quiet, sustained ma- nipulation should be hard. The audit and attribution results remain simulation-only here; their in- cident-data grounding is future work. Throughout, we separate mathematical status from operational status: simulation-checked means the closed form is reproduced under the model assumptions, not that the mechanism has been observed in the wild. We then run two proof-of-concept probes, not a benchmark or a security evaluation. On the wire, open vulnerability corpora show clustered and over-dispersed discovery streams that inflate remedia- tion queues; the 2026 LLM-credited discovery wave is real but still mostly upstream of weaponiza- tion, with only a small fast-migrating subset reaching active-exploitation catalogs. On the model lay- er, adaptive red-teaming across six model checkpoints shows that the clean capture bound fails on a weak 0.5B model and becomes model- and domain-dependent on frontier systems. For factual ques- tions, an existence-scale test (N = 2 injections × 6 checkpoints) yields a transfer-confirmed 3:3 split: some checkpoints resist, while others flip through true-but-irrelevant context that evades a con- tent/plausibility auditor. This supports a content-versus-relevance diagnostic — not yet a gen- eral keyed-payload capability. For opinions, fact-robustness and opinion-robustness separate into distinct axes. The contribution is therefore a layered synthesis, a measurable content/relevance audit gap, and a disciplined path for testing where AI-enabled conflict shifts from exploitation of systems to manipulation of institutional judgment.

## 研究问题

Strategic analysis of AI-enabled conflict often treats "cyber" as one offense–defense game and AI ca- pability as a scalar speedup. We argue instead that AI-mediated conflict is a layered strategic envi- ronment: a wire layer of machine-speed discovery and exploitation, a model/weights layer of captured decision-support, an audit layer of verification exhaustion, and an attribution layer where punishment is slower than defection. The central claim is an inversion across layers: the observable wire layer is relatively self-correcting, while the unobservable model and audit layers can become self- reinforcing. We formalize the stack with five compact model results and seven falsifiable predictions. Two results are empirically grounded here: the wire-layer queueing claim that correlated vulnerability arrivals in- flate remediation backlogs, and the model-layer capture-bound claim that deep, quiet, sustained ma- nipulation should be hard. The audit and attribution results remain simulation-only here; their in- cident-data grounding is future work. Throughout, we separate mathematical status from operational status: simulation-checked means the closed form is reproduced under the model assumptions, not that the mechanism has been observed in the wild. We then run two proof-of-concept probes, not a benchmark or a security evaluation. On the wire, open vulnerability corpora show clustered and over-dispersed discovery streams that inflate remedia- tion queues; the 2026 LLM-credited discovery wave is real but still mostly upstream of weaponiza- tion, with only a small fast-migrating subset reaching active-exploitation catalogs. On the model lay- er, adaptive red-teaming across six model checkpoints shows that the clean capture bound fails on a weak 0.5B model and becomes model- and domain-dependent on frontier systems. For factual ques- tions, an existence-scale test (N = 2 injections × 6 checkpoints) yields a transfer-confirmed 3:3 split: some checkpoints resist, while others flip through true-but-irrelevant context that evades a con- tent/plausibility auditor. This supports a content-versus-relevance diagnostic — not yet a gen- eral keyed-payload capability. For opinions, fact-robustness and opinion-robustness separate into distinct axes. The contribution is therefore a layered synthesis, a measurable content/relevance audit gap, and a disciplined path for testing where AI-enabled conflict shifts from exploitation of systems to manipulation of institutional judgment.

## Introduction 梳理

该记录基于题名、摘要和元数据生成。论文来源为 未记录，当前分类为 RTL and Hardware Verification、Tools and Benchmarks。从命中查询看，论文与 OpenAlex: SoC verification fuzzing 相关。Introduction 部分应重点关注作者如何定义处理器/微架构/硬件 fuzzing 的验证缺口、现有方法的不足，以及本文声称的核心贡献。

## 方法

当前未进行 PDF 正文解析。可从摘要初步判断其方法线索；正式阅读时应提取 fuzz 输入生成策略、变异方式、覆盖率或反馈信号、oracle/差分对象、测试平台以及是否依赖仿真器、RTL 或真实硬件。

## 实验与评估

当前未进行 PDF 正文解析。后续应补充实验对象、baseline、发现 bug 数量、覆盖率提升、运行开销、复现条件和 artifact 可用性。

## 结论

当前结论基于摘要和元数据生成：该论文可能围绕处理器安全验证、fuzzing 效率、微架构漏洞发现或硬件测试自动化展开。需要结合正文确认作者最终证明的效果和适用边界。

## 局限性

当前未进行 PDF 正文解析。初步阅读时应重点检查：是否只覆盖特定 ISA/处理器/仿真器，是否依赖人工规则或特定 oracle，是否难以迁移到 RISC-V，是否缺少真实硬件验证，以及实验是否只在有限 benchmark 上成立。

## 详细阅读分析

元数据主题：Unobservable、Computer science、Attribution、Computer security、Audit trail、Audit、Observable、Layer (electronics)、Comparability、Vulnerability (computing)、Queueing theory、Empirical research、Econometrics、Operations research、Queue、Empirical evidence、Game theory、Inversion (geology)、Upstream (networking)、Benchmark (surveying)、Falsifiability、One shot、Intrusion detection system、Adversary、Asynchronous communication、Network packet、Minimax、Data mining、Causal model。建议优先阅读 Introduction、Threat Model/Background、Method、Evaluation 和 Discussion。如果该论文与 RISC-V 或处理器 fuzzing 强相关，应进一步记录其可复用的测试生成思路、覆盖率指标、oracle 设计和开源实现。

## 后续跟进问题

- 论文是否提供开源实现或实验 artifact？
- 方法是否可以迁移到 RISC-V core、RTL 仿真器或真实处理器？
- 论文依赖什么 oracle、覆盖率指标或差分测试对象？
