# Scalable Test Generation to Trigger Rare Targets in High-Level Synthesizable IPs for Cloud FPGAs

## 基本信息

- 作者：Mukta Debnath、Animesh Basak Chowdhury、Debasri Saha、Susmita Sur-Kolay
- 发表日期：2024-05-30
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Benchmarks, Bug Injection & Artifacts
- 纳入依据：hardware/processor object: processor, rtl；verification/fuzzing method: fuzz, test generation；security relevance: security, leakage
- 论文页面：[http://arxiv.org/abs/2405.19948v1](http://arxiv.org/abs/2405.19948v1)
- PDF：[https://arxiv.org/pdf/2405.19948v1](https://arxiv.org/pdf/2405.19948v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

High-Level Synthesis (HLS) has transformed the development of complex Hardware IPs (HWIP) by offering abstraction and configurability through languages like SystemC/C++, particularly for Field Programmable Gate Array (FPGA) accelerators in high-performance and cloud computing contexts. These IPs can be synthesized for different FPGA boards in cloud, offering compact area requirements and enhanced flexibility. HLS enables designs to execute directly on ARM processors within modern FPGAs without the need for Register Transfer Level (RTL) synthesis, thereby conserving FPGA resources. While HLS offers flexibility and efficiency, it also introduces potential vulnerabilities such as the presence of hidden circuitry, including the possibility of hosting hardware trojans within designs. In cloud environments, these vulnerabilities pose significant security concerns such as leakage of sensitive data, IP functionality disruption and hardware damage, necessitating the development of robust testing frameworks. This research presents an advanced testing approach for HLS-developed cloud IPs, specifically targeting hidden malicious functionalities that may exist in rare conditions within the design. The proposed method leverages selective instrumentation, combining greybox fuzzing and concolic execution techniques to enhance test generation capabilities. Evaluation conducted on various HLS benchmarks, possessing characteristics of FPGA-based cloud IPs with embedded cloud related threats, demonstrates the effectiveness of our framework in detecting trojans and rare scenarios, showcasing improvements in coverage, time efficiency, memory usage, and testing costs compared to existing methods.

## 研究问题

摘要级初步判断（未核验正文）：High-Level Synthesis (HLS) has transformed the development of complex Hardware IPs (HWIP) by offering abstraction and configurability through languages like SystemC/C++, particularly for Field Programmable Gate Array (FPGA) accelerators in high-performance and cloud computing contexts. These IPs can be synthesized for different FPGA boards in cloud, offering compact area requirements and enhanced flexibility. HLS enables designs to execute directly on ARM processors within modern FPGAs without the need for Register Transfer Level (RTL) synthesis, thereby conserving FPGA resources. While HLS offers flexibility and efficiency, it also introduces potential vulnerabilities such as the presence of hidden circuitry, including the possibility of hosting hardware trojans within designs. In cloud environments, these vulnerabilities pose significant security concerns such as leakage of sensitive data, IP functionality disruption and hardware damage, necessitating the development of robust testing frameworks. This research presents an advanced testing approach for HLS-developed cloud IPs, specifically targeting hidden malicious functionalities that may exist in rare conditions within the design. The proposed method leverages selective instrumentation, combining greybox fuzzing and concolic execution techniques to enhance test generation capabilities. Evaluation conducted on various HLS benchmarks, possessing characteristics of FPGA-based cloud IPs with embedded cloud related threats, demonstrates the effectiveness of our framework in detecting trojans and rare scenarios, showcasing improvements in coverage, time efficiency, memory usage, and testing costs compared to existing methods.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Scalable Test Generation to Trigger Rare Targets in High-Level Synthesizable IPs for Cloud FPGAs》，初步归入“RTL & SoC Hardware Fuzzing”。

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
