# AutoFlows++: Hierarchical Message Flow Mining for System on Chip Designs

## 基本信息

- 作者：Bardia Nadimi、Hao Zheng
- 发表日期：2026-04-12
- 更新日期：2026-04-12
- 来源：arXiv
- 来源编号：2604.15359v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2604.15359v1](http://arxiv.org/abs/2604.15359v1)
- PDF：[https://arxiv.org/pdf/2604.15359v1](https://arxiv.org/pdf/2604.15359v1)
- 分析模式：仅元数据分析

## 摘要

Understanding communication behavior in modern system-on-chip (SoC) designs is critical for functional verification, performance analysis, and post-silicon debugging. Communication traces capture message exchanges among system components and provide valuable insights into system behavior. However, deriving concise communication specifications from such traces remains challenging due to interleaved instances of communication flows, and ambiguous causal relationships among messages. Existing mining approaches often struggle with scalability and ambiguity when traces contain complex interleaving of message patterns across multiple components. These conditions often lead to an explosion in the number of candidate flows and inaccurate extraction of communication behaviors. This paper presents AutoFlows++, a design-architecture-guided hierarchical framework for mining message flows from communication traces of complex SoC designs. AutoFlows++ operates in two stages: local mining followed by global mining. In the local mining stage, simple communication patterns are extracted from traces observed at individual communication interfaces between components. In the global mining stage, these local patterns are composed to identify higher-level message flows that characterize communication behavior across multiple components. Experimental results on both synthetic traces and traces generated from SoC models in GEM5 demonstrate that AutoFlows++ significantly improves flow extraction accuracy compared with prior approaches, highlighting its effectiveness for practical SoC validation tasks.

## 研究问题

Understanding communication behavior in modern system-on-chip (SoC) designs is critical for functional verification, performance analysis, and post-silicon debugging. Communication traces capture message exchanges among system components and provide valuable insights into system behavior. However, deriving concise communication specifications from such traces remains challenging due to interleaved instances of communication flows, and ambiguous causal relationships among messages. Existing mining approaches often struggle with scalability and ambiguity when traces contain complex interleaving of message patterns across multiple components. These conditions often lead to an explosion in the number of candidate flows and inaccurate extraction of communication behaviors. This paper presents AutoFlows++, a design-architecture-guided hierarchical framework for mining message flows from communication traces of complex SoC designs. AutoFlows++ operates in two stages: local mining followed by global mining. In the local mining stage, simple communication patterns are extracted from traces observed at individual communication interfaces between components. In the global mining stage, these local patterns are composed to identify higher-level message flows that characterize communication behavior across multiple components. Experimental results on both synthetic traces and traces generated from SoC models in GEM5 demonstrate that AutoFlows++ significantly improves flow extraction accuracy compared with prior approaches, highlighting its effectiveness for practical SoC validation tasks.

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
