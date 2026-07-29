# Sonar: A Hardware Fuzzing Framework to Uncover Contention Side Channels in Processors

## 基本信息

- 作者：Kanqi Zhang、Peinan Li、Miao Li、Xin Tian、Zelong Du、Quanchen Liu、Yongqiang Lyu、Yu Jiang、Dan Meng、Rui Hou
- 发表日期：2025-10-17
- 会议/期刊：Micro
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：RISC-V Processor Fuzzing、Microarchitectural Security Testing
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: risc-v, processor, microarchitectural；verification/fuzzing method: fuzz；security relevance: security, side channel
- 论文页面：[https://doi.org/10.1145/3725843.3756136](https://doi.org/10.1145/3725843.3756136)
- PDF：[https://doi.org/10.1145/3725843.3756136](https://doi.org/10.1145/3725843.3756136)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Contention-based side channels, rooted in resource sharing, have emerged as a significant security threat in modern processors. These side channels allow attackers to leverage timing differences caused by conflicts in execution ports, caches, or interconnects to infer secret information such as cryptographic keys or enclave-resident data. Despite increasing awareness, detecting such channels remains challenging because triggering contentions requires precisely orchestrating specific microarchitectural states, which is often difficult in practice, especially for timing-sensitive contentions. This paper introduces Sonar, the first systematic and automated fuzzing framework designed to uncover contention side channels in processors. Our core idea is to leverage microarchitectural states to guide testcase generation, enabling the precise triggering of microarchitectural events with stringent conditions. Sonar is built on the key observation that multiplexers (MUXes) are hotspots for contention, as resource contention frequently involves data routing and signal selection, which are fundamentally implemented by MUXes in circuits. We first identify contention-critical states with side channel risks based on MUXes, and then utilize these runtime states to directly guide testcase generation via fuzzing, progressively approaching and ultimately triggering contentions. Finally, we employ a dual-differential comparison method to efficiently detect contention-induced side channels and simulate attack scenarios to assess their exploitability. Evaluated on two out-of-order RISC-V processors, Sonar uncovers 14 contention side channels, including 11 previously unknown. These results demonstrate the effectiveness of Sonar in uncovering potentially exploitable microarchitectural contentions.

## 研究问题

摘要级初步判断（未核验正文）：Contention-based side channels, rooted in resource sharing, have emerged as a significant security threat in modern processors. These side channels allow attackers to leverage timing differences caused by conflicts in execution ports, caches, or interconnects to infer secret information such as cryptographic keys or enclave-resident data. Despite increasing awareness, detecting such channels remains challenging because triggering contentions requires precisely orchestrating specific microarchitectural states, which is often difficult in practice, especially for timing-sensitive contentions. This paper introduces Sonar, the first systematic and automated fuzzing framework designed to uncover contention side channels in processors. Our core idea is to leverage microarchitectural states to guide testcase generation, enabling the precise triggering of microarchitectural events with stringent conditions. Sonar is built on the key observation that multiplexers (MUXes) are hotspots for contention, as resource contention frequently involves data routing and signal selection, which are fundamentally implemented by MUXes in circuits. We first identify contention-critical states with side channel risks based on MUXes, and then utilize these runtime states to directly guide testcase generation via fuzzing, progressively approaching and ultimately triggering contentions. Finally, we employ a dual-differential comparison method to efficiently detect contention-induced side channels and simulate attack scenarios to assess their exploitability. Evaluated on two out-of-order RISC-V processors, Sonar uncovers 14 contention side channels, including 11 previously unknown. These results demonstrate the effectiveness of Sonar in uncovering potentially exploitable microarchitectural contentions.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Sonar: A Hardware Fuzzing Framework to Uncover Contention Side Channels in Processors》，初步归入“RISC-V Processor Fuzzing”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
