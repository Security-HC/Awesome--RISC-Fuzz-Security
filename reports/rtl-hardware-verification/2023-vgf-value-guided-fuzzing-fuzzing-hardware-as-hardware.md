# VGF: Value-Guided Fuzzing -- Fuzzing Hardware as Hardware

## 基本信息

- 作者：Ruochen Dai、Michael Lee、Patrick Hoey、Weimin Fu、Tuba Yavuz、Xiaolong Guo、Shuo Wang、Dean Sullivan、Orlando Arias
- 发表日期：2023-12-11
- 更新日期：2023-12-11
- 来源：arXiv
- 来源编号：2312.06580v1
- 研究类别：微架构安全、RTL 与硬件验证、Fuzzing 方法论
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2312.06580v1](http://arxiv.org/abs/2312.06580v1)
- PDF：[https://arxiv.org/pdf/2312.06580v1](https://arxiv.org/pdf/2312.06580v1)
- 分析模式：仅元数据分析

## 摘要

As the complexity of logic designs increase, new avenues for testing digital hardware becomes necessary. Fuzz Testing (fuzzing) has recently received attention as a potential candidate for input vector generation on hardware designs. Using this technique, a fuzzer is used to generate an input to a logic design. Using a simulation engine, the logic design is given the generated stimulus and some metric of feedback is given to the fuzzer to aid in the input mutation. However, much like software fuzzing, hardware fuzzing uses code coverage as a metric to find new possible fuzzing paths. Unfortunately, as we show in this work, this coverage metric falls short of generic on some hardware designs where designers have taken a more direct approach at expressing a particular microarchitecture, or implementation, of the desired hardware. With this work, we introduce a new coverage metric which employs not code coverage, but state coverage internal to a design. By observing changes in signals within the logic circuit under testing, we are able to explore the state space of the design and provide feedback to a fuzzer engine for input generation. Our approach, Value-Guided Fuzzing (VGF), provides a generic metric of coverage which can be applied to any design regardless of its implementation. In this paper, we introduce our state-based VGF metric as well as a sample implementation which can be used with any VPI, DPI, VHPI, or FLI compliant simulator, making it completely HDL agnostic. We demonstrate the generality of VGF and show how our sample implementation is capable of finding bugs considerably faster than previous approaches.

## 研究问题

As the complexity of logic designs increase, new avenues for testing digital hardware becomes necessary. Fuzz Testing (fuzzing) has recently received attention as a potential candidate for input vector generation on hardware designs. Using this technique, a fuzzer is used to generate an input to a logic design. Using a simulation engine, the logic design is given the generated stimulus and some metric of feedback is given to the fuzzer to aid in the input mutation. However, much like software fuzzing, hardware fuzzing uses code coverage as a metric to find new possible fuzzing paths. Unfortunately, as we show in this work, this coverage metric falls short of generic on some hardware designs where designers have taken a more direct approach at expressing a particular microarchitecture, or implementation, of the desired hardware. With this work, we introduce a new coverage metric which employs not code coverage, but state coverage internal to a design. By observing changes in signals within the logic circuit under testing, we are able to explore the state space of the design and provide feedback to a fuzzer engine for input generation. Our approach, Value-Guided Fuzzing (VGF), provides a generic metric of coverage which can be applied to any design regardless of its implementation. In this paper, we introduce our state-based VGF metric as well as a sample implementation which can be used with any VPI, DPI, VHPI, or FLI compliant simulator, making it completely HDL agnostic. We demonstrate the generality of VGF and show how our sample implementation is capable of finding bugs considerably faster than previous approaches.

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
