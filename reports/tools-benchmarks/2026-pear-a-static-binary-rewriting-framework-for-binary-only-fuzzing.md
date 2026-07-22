# PeAR: A Static Binary Rewriting Framework for Binary-Only Fuzzing

## 基本信息

- 作者：Alvin Charles、Adrian Herrera、Peter Oslington、Alwen Tiu
- 发表日期：2026-06-01
- 更新日期：2026-06-01
- 来源：arXiv
- 来源编号：2606.02126v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2606.02126v1](http://arxiv.org/abs/2606.02126v1)
- PDF：[https://arxiv.org/pdf/2606.02126v1](https://arxiv.org/pdf/2606.02126v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

Binary-only fuzzing is a key technique for finding bugs in close-source software. Without access to source code, the fuzzer must rely on static or dynamic binary instrumentation for coverage guidance. In practice, most fuzzers favor dynamic binary instrumentation (DBI), accepting runtime overhead to avoid the perceived accuracy and soundness challenges associated with static binary instrumentation (SBI). We show that these concerns are unwarranted, and that accurate, scalable~SBI is achievable using off-the-shelf frameworks. Building on these frameworks, we develop PeAR, an extensible binary-only fuzzing framework. We demonstrate PeAR's versatility by implementing several modern fuzzer features -- including, deferred initialization, persistent mode, and shared-memory fuzzing. We evaluate PeAR over 4.25 CPU-yrs of fuzzing on the FUZZBENCH benchmark and find that PeAR: (i) successfully instruments 88% of FUZZBENCH targets, comparable to the best SBI-based fuzzers; (ii) achieves a median throughput improvement of 4x when using persistent mode and shared memory fuzzing; and (iii) attains coverage comparable to compiler-based instrumentation. Our results show that SBI is a practical and effective technique for binary-only fuzzing, and that modern binary rewriting frameworks can apply complex instrumentation with high granularity and negligible performance compromise.

## 研究问题

二进制模糊测试中，静态二进制插桩（SBI）被认为精度和可靠性不足，且现有SBI框架缺乏延迟初始化、持久模式和共享内存等现代模糊测试特性，导致性能受限。

## Introduction 梳理

论文提出PeAR，一个基于静态二进制重写的二进制-only模糊测试框架，利用Ddisasm和GTIRB工具，在二进制级别注入覆盖追踪、延迟初始化、持久模式和共享内存模糊测试等功能，并与AFL++集成。

## 方法

PeAR使用Ddisasm将二进制反汇编为GTIRB中间表示，然后通过gtirb-rewriting框架插入插桩。覆盖追踪采用基本块边覆盖，通过trampoline调用__afl_trace函数；初始化时设置共享内存覆盖图；支持延迟初始化（用户指定分支服务器位置）；持久模式将目标函数包裹在循环中，保存/恢复返回地址和寄存器；共享内存模糊测试通过钩子函数重定向输入读取。支持x64 Linux ELF和Windows PE。

## 实验与评估

在FuzzBench的25个目标上评估。PeAR成功插桩88%的目标（22个），与最佳SBI模糊测试器相当。使用持久模式和共享内存时，中位数吞吐量提升4倍，覆盖率与编译器插桩相当。与ZAFL、StochFuzz、afl-dyninst、E9AFL相比，PeAR是唯一支持所有现代特性的框架。

## 结论

静态二进制插桩可实现高效、准确的二进制模糊测试，现代重写框架能以高粒度应用复杂插桩且性能损失可忽略。PeAR开源。

## 局限性

1) 对包含数据表或非常量符号的二进制（如curl、libjpeg-turbo）需手动提示；2) Windows上不支持分支服务器（缺少fork）；3) gtirb-rewriting限制内联插桩（不能使用非活动寄存器）；4) 无法添加数据到.bss段，强制动态内存分配；5) 评估仅针对Linux ELF，未涵盖Windows PE。

## 详细阅读分析

论文核心贡献在于挑战SBI不如DBI的普遍认知，通过实现现代模糊特性展示SBI的实用性。利用Datalog的Ddisasm提供高精度反汇编，结合GTIRB实现可扩展插桩。4倍吞吐量提升凸显持久模式和共享内存的关键作用。对闭源软件漏洞挖掘有重要价值。

## 后续跟进问题

- PeAR如何处理更复杂的二进制保护（如混淆、控制流平坦化）？
- 如何进一步减少手动Ddisasm提示的需求？
- 是否可扩展到ARM或RISC-V架构？
- 与类似工具相比，覆盖率和吞吐量的详细权衡分析？
- 持久模式下的状态重置安全性如何保证？
