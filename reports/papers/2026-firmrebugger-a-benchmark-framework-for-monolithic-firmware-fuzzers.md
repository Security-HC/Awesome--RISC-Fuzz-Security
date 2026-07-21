# FirmReBugger: A Benchmark Framework for Monolithic Firmware Fuzzers

## 基本信息

- 作者：Mathew Duong、Michael Chesser、Guy Farrelly、Surya Nepal、Damith C. Ranasinghe
- 发表日期：2026-01-22
- 更新日期：2026-01-22
- 来源：arXiv
- 来源编号：2601.15774v1
- 研究类别：Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2601.15774v1](http://arxiv.org/abs/2601.15774v1)
- PDF：[https://arxiv.org/pdf/2601.15774v1](https://arxiv.org/pdf/2601.15774v1)
- 分析模式：仅元数据分析

## 摘要

Monolithic Firmware is widespread. Unsurprisingly, fuzz testing firmware is an active research field with new advances addressing the unique challenges in the domain. However, understanding and evaluating improvements by deriving metrics such as code coverage and unique crashes are problematic, leading to a desire for a reliable bug-based benchmark. To address the need, we design and build FirmReBugger, a holistic framework for fairly assessing monolithic firmware fuzzers with a realistic, diverse, bug-based benchmark. FirmReBugger proposes using bug oracles--C syntax expressions of bug descriptors--with an interpreter to automate analysis and accurately report on bugs discovered, discriminating between states of detected, triggered, reached and not reached. Importantly, our idea of benchmarking does not modify the target binary and simply replays fuzzing seeds to isolate the benchmark implementation from the fuzzer while providing a simple means to extend with new bug oracles. Further, analyzing fuzzing roadblocks, we created FirmBench, a set of diverse, real-world binary targets with 313 software bug oracles. Incorporating our analysis of roadblocks challenging monolithic firmware fuzzing, the bench provides for rapid evaluation of future advances. We implement FirmReBugger in a FuzzBench-for-Firmware type service and use FirmBench to evaluate 9 state-of-the art monolithic firmware fuzzers in the style of a reproducibility study, using a 10 CPU-year effort, to report our findings.

## 研究问题

Monolithic Firmware is widespread. Unsurprisingly, fuzz testing firmware is an active research field with new advances addressing the unique challenges in the domain. However, understanding and evaluating improvements by deriving metrics such as code coverage and unique crashes are problematic, leading to a desire for a reliable bug-based benchmark. To address the need, we design and build FirmReBugger, a holistic framework for fairly assessing monolithic firmware fuzzers with a realistic, diverse, bug-based benchmark. FirmReBugger proposes using bug oracles--C syntax expressions of bug descriptors--with an interpreter to automate analysis and accurately report on bugs discovered, discriminating between states of detected, triggered, reached and not reached. Importantly, our idea of benchmarking does not modify the target binary and simply replays fuzzing seeds to isolate the benchmark implementation from the fuzzer while providing a simple means to extend with new bug oracles. Further, analyzing fuzzing roadblocks, we created FirmBench, a set of diverse, real-world binary targets with 313 software bug oracles. Incorporating our analysis of roadblocks challenging monolithic firmware fuzzing, the bench provides for rapid evaluation of future advances. We implement FirmReBugger in a FuzzBench-for-Firmware type service and use FirmBench to evaluate 9 state-of-the art monolithic firmware fuzzers in the style of a reproducibility study, using a 10 CPU-year effort, to report our findings.

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
