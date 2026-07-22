# AKER: A Design and Verification Framework for Safe andSecure SoC Access Control

## 基本信息

- 作者：Francesco Restuccia、Andres Meza、Ryan Kastner
- 发表日期：2021-06-24
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：B·强邻近（score=5）
- 证据等级：摘要级
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：hardware/processor object: soc, multicore；verification/fuzzing method: verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2106.13263v1](http://arxiv.org/abs/2106.13263v1)
- PDF：[https://arxiv.org/pdf/2106.13263v1](https://arxiv.org/pdf/2106.13263v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Modern systems on a chip (SoCs) utilize heterogeneous architectures where multiple IP cores have concurrent access to on-chip shared resources. In security-critical applications, IP cores have different privilege levels for accessing shared resources, which must be regulated by an access control system. AKER is a design and verification framework for SoC access control. AKER builds upon the Access Control Wrapper (ACW) -- a high performance and easy-to-integrate hardware module that dynamically manages access to shared resources. To build an SoC access control system, AKER distributes the ACWs throughout the SoC, wrapping controller IP cores, and configuring the ACWs to perform local access control. To ensure the access control system is functioning correctly and securely, AKER provides a property-driven security verification using MITRE common weakness enumerations. AKER verifies the SoC access control at the IP level to ensure the absence of bugs in the functionalities of the ACW module, at the firmware level to confirm the secure operation of the ACW when integrated with a hardware root-of-trust (HRoT), and at the system level to evaluate security threats due to the interactions among shared resources. The performance, resource usage, and security of access control systems implemented through AKER is experimentally evaluated on a Xilinx UltraScale+ programmable SoC, it is integrated with the OpenTitan hardware root-of-trust, and it is used to design an access control system for the OpenPULP multicore architecture.

## 研究问题

摘要级初步判断（未核验正文）：Modern systems on a chip (SoCs) utilize heterogeneous architectures where multiple IP cores have concurrent access to on-chip shared resources. In security-critical applications, IP cores have different privilege levels for accessing shared resources, which must be regulated by an access control system. AKER is a design and verification framework for SoC access control. AKER builds upon the Access Control Wrapper (ACW) -- a high performance and easy-to-integrate hardware module that dynamically manages access to shared resources. To build an SoC access control system, AKER distributes the ACWs throughout the SoC, wrapping controller IP cores, and configuring the ACWs to perform local access control. To ensure the access control system is functioning correctly and securely, AKER provides a property-driven security verification using MITRE common weakness enumerations. AKER verifies the SoC access control at the IP level to ensure the absence of bugs in the functionalities of the ACW module, at the firmware level to confirm the secure operation of the ACW when integrated with a hardware root-of-trust (HRoT), and at the system level to evaluate security threats due to the interactions among shared resources. The performance, resource usage, and security of access control systems implemented through AKER is experimentally evaluated on a Xilinx UltraScale+ programmable SoC, it is integrated with the OpenTitan hardware root-of-trust, and it is used to design an access control system for the OpenPULP multicore architecture.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《AKER: A Design and Verification Framework for Safe andSecure SoC Access Control》，初步归入“Multi-Hart, Memory Consistency & Cache Coherence”。

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
