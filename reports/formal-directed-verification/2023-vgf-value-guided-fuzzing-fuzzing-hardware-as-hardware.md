# VGF: Value-Guided Fuzzing -- Fuzzing Hardware as Hardware

## 基本信息

- 作者：Ruochen Dai、Michael Lee、Patrick Hoey、Weimin Fu、Tuba Yavuz、Xiaolong Guo、Shuo Wang、Dean Sullivan、Orlando Arias
- 发表日期：2023-12-11
- 会议/期刊：arXiv
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=7）
- 证据等级：摘要级
- 标签：Formal & Directed Processor Verification
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: microarchitecture；verification/fuzzing method: fuzz
- 论文页面：[http://arxiv.org/abs/2312.06580v1](http://arxiv.org/abs/2312.06580v1)
- PDF：[https://arxiv.org/pdf/2312.06580v1](https://arxiv.org/pdf/2312.06580v1)
- 分析模式：摘要级占位（未全文核验）

## 摘要

As the complexity of logic designs increase, new avenues for testing digital hardware becomes necessary. Fuzz Testing (fuzzing) has recently received attention as a potential candidate for input vector generation on hardware designs. Using this technique, a fuzzer is used to generate an input to a logic design. Using a simulation engine, the logic design is given the generated stimulus and some metric of feedback is given to the fuzzer to aid in the input mutation. However, much like software fuzzing, hardware fuzzing uses code coverage as a metric to find new possible fuzzing paths. Unfortunately, as we show in this work, this coverage metric falls short of generic on some hardware designs where designers have taken a more direct approach at expressing a particular microarchitecture, or implementation, of the desired hardware. With this work, we introduce a new coverage metric which employs not code coverage, but state coverage internal to a design. By observing changes in signals within the logic circuit under testing, we are able to explore the state space of the design and provide feedback to a fuzzer engine for input generation. Our approach, Value-Guided Fuzzing (VGF), provides a generic metric of coverage which can be applied to any design regardless of its implementation. In this paper, we introduce our state-based VGF metric as well as a sample implementation which can be used with any VPI, DPI, VHPI, or FLI compliant simulator, making it completely HDL agnostic. We demonstrate the generality of VGF and show how our sample implementation is capable of finding bugs considerably faster than previous approaches.

## 研究问题

摘要级初步判断（未核验正文）：As the complexity of logic designs increase, new avenues for testing digital hardware becomes necessary. Fuzz Testing (fuzzing) has recently received attention as a potential candidate for input vector generation on hardware designs. Using this technique, a fuzzer is used to generate an input to a logic design. Using a simulation engine, the logic design is given the generated stimulus and some metric of feedback is given to the fuzzer to aid in the input mutation. However, much like software fuzzing, hardware fuzzing uses code coverage as a metric to find new possible fuzzing paths. Unfortunately, as we show in this work, this coverage metric falls short of generic on some hardware designs where designers have taken a more direct approach at expressing a particular microarchitecture, or implementation, of the desired hardware. With this work, we introduce a new coverage metric which employs not code coverage, but state coverage internal to a design. By observing changes in signals within the logic circuit under testing, we are able to explore the state space of the design and provide feedback to a fuzzer engine for input generation. Our approach, Value-Guided Fuzzing (VGF), provides a generic metric of coverage which can be applied to any design regardless of its implementation. In this paper, we introduce our state-based VGF metric as well as a sample implementation which can be used with any VPI, DPI, VHPI, or FLI compliant simulator, making it completely HDL agnostic. We demonstrate the generality of VGF and show how our sample implementation is capable of finding bugs considerably faster than previous approaches.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《VGF: Value-Guided Fuzzing -- Fuzzing Hardware as Hardware》，初步归入“Formal & Directed Processor Verification”。

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
