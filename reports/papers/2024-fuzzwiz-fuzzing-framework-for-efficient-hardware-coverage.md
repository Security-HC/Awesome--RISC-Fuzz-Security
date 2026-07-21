# FuzzWiz -- Fuzzing Framework for Efficient Hardware Coverage

## 基本信息

- 作者：Deepak Narayan Gadde、Aman Kumar、Djones Lettnin、Sebastian Simon
- 发表日期：2024-10-23
- 更新日期：2024-10-23
- 来源：arXiv
- 来源编号：2410.17732v1
- 研究类别：RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2410.17732v1](http://arxiv.org/abs/2410.17732v1)
- PDF：[https://arxiv.org/pdf/2410.17732v1](https://arxiv.org/pdf/2410.17732v1)
- 分析模式：仅元数据分析

## 摘要

Ever-increasing design complexity of System-on-Chips (SoCs) led to significant verification challenges. Unlike software, bugs in hardware design are vigorous and eternal i.e., once the hardware is fabricated, it cannot be repaired with any patch. Despite being one of the powerful techniques used in verification, the dynamic random approach cannot give confidence to complex Register Transfer Leve (RTL) designs during the pre-silicon design phase. In particular, achieving coverage targets and exposing bugs is a complicated task with random simulations. In this paper, we leverage an existing testing solution available in the software world known as fuzzing and apply it to hardware verification in order to achieve coverage targets in quick time. We created an automated hardware fuzzing framework FuzzWiz using metamodeling and Python to achieve coverage goals faster. It includes parsing the RTL design module, converting it into C/C++ models, creating generic testbench with assertions, fuzzer-specific compilation, linking, and fuzzing. Furthermore, it is configurable and provides the debug flow if any crash is detected during the fuzzing process. The proposed framework is applied on four IP blocks from Google's OpenTitan chip with various fuzzing engines to show its scalability and compatibility. Our benchmarking results show that we could achieve around 90% of the coverage 10 times faster than traditional simulation regression based approach.

## 研究问题

Ever-increasing design complexity of System-on-Chips (SoCs) led to significant verification challenges. Unlike software, bugs in hardware design are vigorous and eternal i.e., once the hardware is fabricated, it cannot be repaired with any patch. Despite being one of the powerful techniques used in verification, the dynamic random approach cannot give confidence to complex Register Transfer Leve (RTL) designs during the pre-silicon design phase. In particular, achieving coverage targets and exposing bugs is a complicated task with random simulations. In this paper, we leverage an existing testing solution available in the software world known as fuzzing and apply it to hardware verification in order to achieve coverage targets in quick time. We created an automated hardware fuzzing framework FuzzWiz using metamodeling and Python to achieve coverage goals faster. It includes parsing the RTL design module, converting it into C/C++ models, creating generic testbench with assertions, fuzzer-specific compilation, linking, and fuzzing. Furthermore, it is configurable and provides the debug flow if any crash is detected during the fuzzing process. The proposed framework is applied on four IP blocks from Google's OpenTitan chip with various fuzzing engines to show its scalability and compatibility. Our benchmarking results show that we could achieve around 90% of the coverage 10 times faster than traditional simulation regression based approach.

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
