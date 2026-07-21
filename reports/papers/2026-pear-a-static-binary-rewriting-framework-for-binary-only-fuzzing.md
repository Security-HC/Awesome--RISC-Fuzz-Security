# PeAR: A Static Binary Rewriting Framework for Binary-Only Fuzzing

## 基本信息

- 作者：Alvin Charles、Adrian Herrera、Peter Oslington、Alwen Tiu
- 发表日期：2026-06-01
- 更新日期：2026-06-01
- 来源：arXiv
- 来源编号：2606.02126v1
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2606.02126v1](http://arxiv.org/abs/2606.02126v1)
- PDF：[https://arxiv.org/pdf/2606.02126v1](https://arxiv.org/pdf/2606.02126v1)
- 分析模式：仅元数据分析

## 摘要

Binary-only fuzzing is a key technique for finding bugs in close-source software. Without access to source code, the fuzzer must rely on static or dynamic binary instrumentation for coverage guidance. In practice, most fuzzers favor dynamic binary instrumentation (DBI), accepting runtime overhead to avoid the perceived accuracy and soundness challenges associated with static binary instrumentation (SBI). We show that these concerns are unwarranted, and that accurate, scalable~SBI is achievable using off-the-shelf frameworks. Building on these frameworks, we develop PeAR, an extensible binary-only fuzzing framework. We demonstrate PeAR's versatility by implementing several modern fuzzer features -- including, deferred initialization, persistent mode, and shared-memory fuzzing. We evaluate PeAR over 4.25 CPU-yrs of fuzzing on the FUZZBENCH benchmark and find that PeAR: (i) successfully instruments 88% of FUZZBENCH targets, comparable to the best SBI-based fuzzers; (ii) achieves a median throughput improvement of 4x when using persistent mode and shared memory fuzzing; and (iii) attains coverage comparable to compiler-based instrumentation. Our results show that SBI is a practical and effective technique for binary-only fuzzing, and that modern binary rewriting frameworks can apply complex instrumentation with high granularity and negligible performance compromise.

## 研究问题

Binary-only fuzzing is a key technique for finding bugs in close-source software. Without access to source code, the fuzzer must rely on static or dynamic binary instrumentation for coverage guidance. In practice, most fuzzers favor dynamic binary instrumentation (DBI), accepting runtime overhead to avoid the perceived accuracy and soundness challenges associated with static binary instrumentation (SBI). We show that these concerns are unwarranted, and that accurate, scalable~SBI is achievable using off-the-shelf frameworks. Building on these frameworks, we develop PeAR, an extensible binary-only fuzzing framework. We demonstrate PeAR's versatility by implementing several modern fuzzer features -- including, deferred initialization, persistent mode, and shared-memory fuzzing. We evaluate PeAR over 4.25 CPU-yrs of fuzzing on the FUZZBENCH benchmark and find that PeAR: (i) successfully instruments 88% of FUZZBENCH targets, comparable to the best SBI-based fuzzers; (ii) achieves a median throughput improvement of 4x when using persistent mode and shared memory fuzzing; and (iii) attains coverage comparable to compiler-based instrumentation. Our results show that SBI is a practical and effective technique for binary-only fuzzing, and that modern binary rewriting frameworks can apply complex instrumentation with high granularity and negligible performance compromise.

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
