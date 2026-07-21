# $ρ$Hammer: Reviving RowHammer Attacks on New Architectures via Prefetching

## 基本信息

- 作者：Weijie Chen、Shan Tang、Yulin Tang、Xiapu Luo、Yinqian Zhang、Weizhong Qiang
- 发表日期：2025-10-18
- 更新日期：2025-10-18
- 来源：arXiv
- 来源编号：2510.16544v1
- 研究类别：Microarchitecture Security、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2510.16544v1](http://arxiv.org/abs/2510.16544v1)
- PDF：[https://arxiv.org/pdf/2510.16544v1](https://arxiv.org/pdf/2510.16544v1)
- 分析模式：仅元数据分析

## 摘要

Rowhammer is a critical vulnerability in dynamic random access memory (DRAM) that continues to pose a significant threat to various systems. However, we find that conventional load-based attacks are becoming highly ineffective on the most recent architectures such as Intel Alder and Raptor Lake. In this paper, we present $ρ$Hammer, a new Rowhammer framework that systematically overcomes three core challenges impeding attacks on these new architectures. First, we design an efficient and generic DRAM address mapping reverse-engineering method that uses selective pairwise measurements and structured deduction, enabling recovery of complex mappings within seconds on the latest memory controllers. Second, to break through the activation rate bottleneck of load-based hammering, we introduce a novel prefetch-based hammering paradigm that leverages the asynchronous nature of x86 prefetch instructions and is further enhanced by multi-bank parallelism to maximize throughput. Third, recognizing that speculative execution causes more severe disorder issues for prefetching, which cannot be simply mitigated by memory barriers, we develop a counter-speculation hammering technique using control-flow obfuscation and optimized NOP-based pseudo-barriers to maintain prefetch order with minimal overhead. Evaluations across four latest Intel architectures demonstrate $ρ$Hammer's breakthrough effectiveness: it induces up to 200K+ additional bit flips within 2-hour attack pattern fuzzing processes and has a 112x higher flip rate than the load-based hammering baselines on Comet and Rocket Lake. Also, we are the first to revive Rowhammer attacks on the latest Raptor Lake architecture, where baselines completely fail, achieving stable flip rates of 2,291/min and fast end-to-end exploitation.

## 研究问题

Rowhammer is a critical vulnerability in dynamic random access memory (DRAM) that continues to pose a significant threat to various systems. However, we find that conventional load-based attacks are becoming highly ineffective on the most recent architectures such as Intel Alder and Raptor Lake. In this paper, we present $ρ$Hammer, a new Rowhammer framework that systematically overcomes three core challenges impeding attacks on these new architectures. First, we design an efficient and generic DRAM address mapping reverse-engineering method that uses selective pairwise measurements and structured deduction, enabling recovery of complex mappings within seconds on the latest memory controllers. Second, to break through the activation rate bottleneck of load-based hammering, we introduce a novel prefetch-based hammering paradigm that leverages the asynchronous nature of x86 prefetch instructions and is further enhanced by multi-bank parallelism to maximize throughput. Third, recognizing that speculative execution causes more severe disorder issues for prefetching, which cannot be simply mitigated by memory barriers, we develop a counter-speculation hammering technique using control-flow obfuscation and optimized NOP-based pseudo-barriers to maintain prefetch order with minimal overhead. Evaluations across four latest Intel architectures demonstrate $ρ$Hammer's breakthrough effectiveness: it induces up to 200K+ additional bit flips within 2-hour attack pattern fuzzing processes and has a 112x higher flip rate than the load-based hammering baselines on Comet and Rocket Lake. Also, we are the first to revive Rowhammer attacks on the latest Raptor Lake architecture, where baselines completely fail, achieving stable flip rates of 2,291/min and fast end-to-end exploitation.

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
