# Evaluating the Effectiveness of Hardware Trojan Detection Approaches at RTL

## 基本信息

- 作者：Ruochen Dai、Zhaoxiang Liu、Orlando Arias、Xiaolong Guo、Tuba Yavuz
- 发表日期：2025-05-05
- 会议/期刊：IEEE International Symposium on Hardware Oriented Security and Trust
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：B·强邻近（score=7）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：RTL & SoC Hardware Fuzzing、Formal & Directed Processor Verification
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: rtl；verification/fuzzing method: fuzz, model checking
- 论文页面：[https://doi.org/10.1109/HOST64725.2025.11050040](https://doi.org/10.1109/HOST64725.2025.11050040)
- PDF：未记录
- 分析模式：摘要级占位（未全文核验）

## 摘要

The rapid advancements in semiconductor technol-ogy have fostered unprecedented innovation while simultane-ously increasing the risk of hardware Trojans (HTs)-malicious alterations introduced into integrated circuits (ICs) during de-sign or production. Despite extensive research on HT detection techniques, their practical implementation remains criti-cal for developing robust defenses. This paper quantitatively evaluates the effectiveness of three hardware design analysis techniques-bounded model checking, symbolic execution, and fuzzing - for detecting four types of HTs: combinational, sequential, input-based, and timing-based. We generate a HT benchmark set using a dynamic Trojan insertion framework, DTjRTL, which facilitates a systematic and comprehensive benchmarking process. This paper uses a variety of structural and semantic Trojan complexity metrics to evaluate the strengths and weaknesses of each of the hardware analyses techniques. Our findings show that there is no single technique that is effective for all HTs. Although, bounded model checking based techniques outperform other approaches for most HT types, they may be limited due to RTL features or the supported property specification syntax. We also find that among all the techniques, hardware fuzzing seems to be more sensitive to HT trigger complexity. Symbolic execution based techniques handle deep Timing-based Trojans in a scalable way when guided by fuzzing as an oracle towards suspicious parts of the design. Additionally, signal-dependent metrics have more impact on Trojan detection difficulty compared to the structural metrics.

## 研究问题

摘要级初步判断（未核验正文）：The rapid advancements in semiconductor technol-ogy have fostered unprecedented innovation while simultane-ously increasing the risk of hardware Trojans (HTs)-malicious alterations introduced into integrated circuits (ICs) during de-sign or production. Despite extensive research on HT detection techniques, their practical implementation remains criti-cal for developing robust defenses. This paper quantitatively evaluates the effectiveness of three hardware design analysis techniques-bounded model checking, symbolic execution, and fuzzing - for detecting four types of HTs: combinational, sequential, input-based, and timing-based. We generate a HT benchmark set using a dynamic Trojan insertion framework, DTjRTL, which facilitates a systematic and comprehensive benchmarking process. This paper uses a variety of structural and semantic Trojan complexity metrics to evaluate the strengths and weaknesses of each of the hardware analyses techniques. Our findings show that there is no single technique that is effective for all HTs. Although, bounded model checking based techniques outperform other approaches for most HT types, they may be limited due to RTL features or the supported property specification syntax. We also find that among all the techniques, hardware fuzzing seems to be more sensitive to HT trigger complexity. Symbolic execution based techniques handle deep Timing-based Trojans in a scalable way when guided by fuzzing as an oracle towards suspicious parts of the design. Additionally, signal-dependent metrics have more impact on Trojan detection difficulty compared to the structural metrics.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Evaluating the Effectiveness of Hardware Trojan Detection Approaches at RTL》，初步归入“RTL & SoC Hardware Fuzzing”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

## 与本仓库研究主线的关系

该条目已通过自动相关性筛选，但尚未完成人工或全文级核验。

## 结论

尚未核验正文，因此不对论文最终结论作确定性概括。

## 局限性

尚未核验正文。至少需要检查方法是否只适用于特定 ISA、处理器、协议、仿真器或人工模板，以及实验是否存在目标泄漏和基线不公平。

## 详细阅读分析

优先阅读 Introduction、Background/Threat Model、Method、Evaluation、Limitations/Discussion，并核对官方论文页、DOI、Artifact 和代码仓库。

## 后续核验问题

- 论文的在线反馈信号和最终 Oracle 分别是什么？
- 实验是否包含公平的 random、通用 RTL coverage 和领域专用 coverage 基线？
- 论文是否提供开源 Artifact、真实漏洞、CVE 或可复现 PoC？
