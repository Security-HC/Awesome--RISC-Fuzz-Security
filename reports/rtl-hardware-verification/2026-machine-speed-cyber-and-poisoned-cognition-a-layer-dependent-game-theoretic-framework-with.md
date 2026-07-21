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
- 分析模式：仅元数据分析

## 摘要

Strategic analysis of AI-enabled conflict often treats "cyber" as one offense–defense game and AI ca- pability as a scalar speedup. We argue instead that AI-mediated conflict is a layered strategic envi- ronment: a wire layer of machine-speed discovery and exploitation, a model/weights layer of captured decision-support, an audit layer of verification exhaustion, and an attribution layer where punishment is slower than defection. The central claim is an inversion across layers: the observable wire layer is relatively self-correcting, while the unobservable model and audit layers can become self- reinforcing. We formalize the stack with five compact model results and seven falsifiable predictions. Two results are empirically grounded here: the wire-layer queueing claim that correlated vulnerability arrivals in- flate remediation backlogs, and the model-layer capture-bound claim that deep, quiet, sustained ma- nipulation should be hard. The audit and attribution results remain simulation-only here; their in- cident-data grounding is future work. Throughout, we separate mathematical status from operational status: simulation-checked means the closed form is reproduced under the model assumptions, not that the mechanism has been observed in the wild. We then run two proof-of-concept probes, not a benchmark or a security evaluation. On the wire, open vulnerability corpora show clustered and over-dispersed discovery streams that inflate remedia- tion queues; the 2026 LLM-credited discovery wave is real but still mostly upstream of weaponiza- tion, with only a small fast-migrating subset reaching active-exploitation catalogs. On the model lay- er, adaptive red-teaming across six model checkpoints shows that the clean capture bound fails on a weak 0.5B model and becomes model- and domain-dependent on frontier systems. For factual ques- tions, an existence-scale test (N = 2 injections × 6 checkpoints) yields a transfer-confirmed 3:3 split: some checkpoints resist, while others flip through true-but-irrelevant context that evades a con- tent/plausibility auditor. This supports a content-versus-relevance diagnostic — not yet a gen- eral keyed-payload capability. For opinions, fact-robustness and opinion-robustness separate into distinct axes. The contribution is therefore a layered synthesis, a measurable content/relevance audit gap, and a disciplined path for testing where AI-enabled conflict shifts from exploitation of systems to manipulation of institutional judgment.

## 研究问题

Strategic analysis of AI-enabled conflict often treats "cyber" as one offense–defense game and AI ca- pability as a scalar speedup. We argue instead that AI-mediated conflict is a layered strategic envi- ronment: a wire layer of machine-speed discovery and exploitation, a model/weights layer of captured decision-support, an audit layer of verification exhaustion, and an attribution layer where punishment is slower than defection. The central claim is an inversion across layers: the observable wire layer is relatively self-correcting, while the unobservable model and audit layers can become self- reinforcing. We formalize the stack with five compact model results and seven falsifiable predictions. Two results are empirically grounded here: the wire-layer queueing claim that correlated vulnerability arrivals in- flate remediation backlogs, and the model-layer capture-bound claim that deep, quiet, sustained ma- nipulation should be hard. The audit and attribution results remain simulation-only here; their in- cident-data grounding is future work. Throughout, we separate mathematical status from operational status: simulation-checked means the closed form is reproduced under the model assumptions, not that the mechanism has been observed in the wild. We then run two proof-of-concept probes, not a benchmark or a security evaluation. On the wire, open vulnerability corpora show clustered and over-dispersed discovery streams that inflate remedia- tion queues; the 2026 LLM-credited discovery wave is real but still mostly upstream of weaponiza- tion, with only a small fast-migrating subset reaching active-exploitation catalogs. On the model lay- er, adaptive red-teaming across six model checkpoints shows that the clean capture bound fails on a weak 0.5B model and becomes model- and domain-dependent on frontier systems. For factual ques- tions, an existence-scale test (N = 2 injections × 6 checkpoints) yields a transfer-confirmed 3:3 split: some checkpoints resist, while others flip through true-but-irrelevant context that evades a con- tent/plausibility auditor. This supports a content-versus-relevance diagnostic — not yet a gen- eral keyed-payload capability. For opinions, fact-robustness and opinion-robustness separate into distinct axes. The contribution is therefore a layered synthesis, a measurable content/relevance audit gap, and a disciplined path for testing where AI-enabled conflict shifts from exploitation of systems to manipulation of institutional judgment.

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
