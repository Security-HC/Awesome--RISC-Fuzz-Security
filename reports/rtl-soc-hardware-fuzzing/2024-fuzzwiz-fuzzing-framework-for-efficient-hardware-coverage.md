# FuzzWiz -- Fuzzing Framework for Efficient Hardware Coverage

## 基本信息

- 作者：Deepak Narayan Gadde、Aman Kumar、Djones Lettnin、Sebastian Simon
- 发表日期：2024-10-23
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：B·强邻近（score=7）
- 证据等级：摘要级
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: rtl, system-on-chip, soc；verification/fuzzing method: fuzz, verification
- 论文页面：[http://arxiv.org/abs/2410.17732v1](http://arxiv.org/abs/2410.17732v1)
- PDF：[https://arxiv.org/pdf/2410.17732v1](https://arxiv.org/pdf/2410.17732v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Ever-increasing design complexity of System-on-Chips (SoCs) led to significant verification challenges. Unlike software, bugs in hardware design are vigorous and eternal i.e., once the hardware is fabricated, it cannot be repaired with any patch. Despite being one of the powerful techniques used in verification, the dynamic random approach cannot give confidence to complex Register Transfer Leve (RTL) designs during the pre-silicon design phase. In particular, achieving coverage targets and exposing bugs is a complicated task with random simulations. In this paper, we leverage an existing testing solution available in the software world known as fuzzing and apply it to hardware verification in order to achieve coverage targets in quick time. We created an automated hardware fuzzing framework FuzzWiz using metamodeling and Python to achieve coverage goals faster. It includes parsing the RTL design module, converting it into C/C++ models, creating generic testbench with assertions, fuzzer-specific compilation, linking, and fuzzing. Furthermore, it is configurable and provides the debug flow if any crash is detected during the fuzzing process. The proposed framework is applied on four IP blocks from Google's OpenTitan chip with various fuzzing engines to show its scalability and compatibility. Our benchmarking results show that we could achieve around 90% of the coverage 10 times faster than traditional simulation regression based approach.

## 研究问题

摘要级初步判断（未核验正文）：Ever-increasing design complexity of System-on-Chips (SoCs) led to significant verification challenges. Unlike software, bugs in hardware design are vigorous and eternal i.e., once the hardware is fabricated, it cannot be repaired with any patch. Despite being one of the powerful techniques used in verification, the dynamic random approach cannot give confidence to complex Register Transfer Leve (RTL) designs during the pre-silicon design phase. In particular, achieving coverage targets and exposing bugs is a complicated task with random simulations. In this paper, we leverage an existing testing solution available in the software world known as fuzzing and apply it to hardware verification in order to achieve coverage targets in quick time. We created an automated hardware fuzzing framework FuzzWiz using metamodeling and Python to achieve coverage goals faster. It includes parsing the RTL design module, converting it into C/C++ models, creating generic testbench with assertions, fuzzer-specific compilation, linking, and fuzzing. Furthermore, it is configurable and provides the debug flow if any crash is detected during the fuzzing process. The proposed framework is applied on four IP blocks from Google's OpenTitan chip with various fuzzing engines to show its scalability and compatibility. Our benchmarking results show that we could achieve around 90% of the coverage 10 times faster than traditional simulation regression based approach.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《FuzzWiz -- Fuzzing Framework for Efficient Hardware Coverage》，初步归入“RTL & SoC Hardware Fuzzing”。

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
