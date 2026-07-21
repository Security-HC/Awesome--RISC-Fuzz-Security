# Evaluating the Effectiveness of Hardware Trojan Detection Approaches at RTL

## 基本信息

- 作者：Ruochen Dai、Zhaoxiang Liu、Orlando Arias、Xiaolong Guo、Tuba Yavuz
- 发表日期：2025-05-05
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：226d2a435ea8a7152e6ed9192ebb3354221ace24
- 研究类别：RTL 与硬件验证、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.1109/HOST64725.2025.11050040](https://doi.org/10.1109/HOST64725.2025.11050040)
- PDF：[]()
- 分析模式：仅元数据分析

## 摘要

The rapid advancements in semiconductor technol-ogy have fostered unprecedented innovation while simultane-ously increasing the risk of hardware Trojans (HTs)-malicious alterations introduced into integrated circuits (ICs) during de-sign or production. Despite extensive research on HT detection techniques, their practical implementation remains criti-cal for developing robust defenses. This paper quantitatively evaluates the effectiveness of three hardware design analysis techniques-bounded model checking, symbolic execution, and fuzzing - for detecting four types of HTs: combinational, sequential, input-based, and timing-based. We generate a HT benchmark set using a dynamic Trojan insertion framework, DTjRTL, which facilitates a systematic and comprehensive benchmarking process. This paper uses a variety of structural and semantic Trojan complexity metrics to evaluate the strengths and weaknesses of each of the hardware analyses techniques. Our findings show that there is no single technique that is effective for all HTs. Although, bounded model checking based techniques outperform other approaches for most HT types, they may be limited due to RTL features or the supported property specification syntax. We also find that among all the techniques, hardware fuzzing seems to be more sensitive to HT trigger complexity. Symbolic execution based techniques handle deep Timing-based Trojans in a scalable way when guided by fuzzing as an oracle towards suspicious parts of the design. Additionally, signal-dependent metrics have more impact on Trojan detection difficulty compared to the structural metrics.

## 研究问题

The rapid advancements in semiconductor technol-ogy have fostered unprecedented innovation while simultane-ously increasing the risk of hardware Trojans (HTs)-malicious alterations introduced into integrated circuits (ICs) during de-sign or production. Despite extensive research on HT detection techniques, their practical implementation remains criti-cal for developing robust defenses. This paper quantitatively evaluates the effectiveness of three hardware design analysis techniques-bounded model checking, symbolic execution, and fuzzing - for detecting four types of HTs: combinational, sequential, input-based, and timing-based. We generate a HT benchmark set using a dynamic Trojan insertion framework, DTjRTL, which facilitates a systematic and comprehensive benchmarking process. This paper uses a variety of structural and semantic Trojan complexity metrics to evaluate the strengths and weaknesses of each of the hardware analyses techniques. Our findings show that there is no single technique that is effective for all HTs. Although, bounded model checking based techniques outperform other approaches for most HT types, they may be limited due to RTL features or the supported property specification syntax. We also find that among all the techniques, hardware fuzzing seems to be more sensitive to HT trigger complexity. Symbolic execution based techniques handle deep Timing-based Trojans in a scalable way when guided by fuzzing as an oracle towards suspicious parts of the design. Additionally, signal-dependent metrics have more impact on Trojan detection difficulty compared to the structural metrics.

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
