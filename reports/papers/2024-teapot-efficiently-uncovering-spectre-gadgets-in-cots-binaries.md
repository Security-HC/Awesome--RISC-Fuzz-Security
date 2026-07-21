# Teapot: Efficiently Uncovering Spectre Gadgets in COTS Binaries

## 基本信息

- 作者：Fangzheng Lin、Zhongfa Wang、Hiroshi Sasaki
- 发表日期：2024-11-18
- 更新日期：2024-12-26
- 来源：arXiv
- 来源编号：2411.11624v2
- 研究类别：Microarchitecture Security、RTL and Hardware Verification
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2411.11624v2](http://arxiv.org/abs/2411.11624v2)
- PDF：[https://arxiv.org/pdf/2411.11624v2](https://arxiv.org/pdf/2411.11624v2)
- 分析模式：仅元数据分析

## 摘要

Speculative execution is crucial in enhancing modern processor performance but can introduce Spectre-type vulnerabilities that may leak sensitive information. Detecting Spectre gadgets from programs has been a research focus to enhance the analysis and understanding of Spectre attacks. However, one of the problems of existing approaches is that they rely on the presence of source code (or are impractical in terms of run-time performance and gadget detection ability). This paper presents Teapot, the first Spectre gadget scanner that works on COTS binaries with comparable performance to compiler-based alternatives. As its core principle, we introduce Speculation Shadows, a novel approach that separates the binary code for normal execution and speculation simulation in order to improve run-time efficiency. Teapot is based on static binary rewriting. It instruments the program to simulate the effects of speculative execution and also adds integrity checks to detect Spectre gadgets at run time. By leveraging fuzzing, Teapot succeeds in efficiently detecting Spectre gadgets. Evaluations show that Teapot outperforms both performance (more than 20x performant) and gadget detection ability than a previously proposed binary-based approach.

## 研究问题

Speculative execution is crucial in enhancing modern processor performance but can introduce Spectre-type vulnerabilities that may leak sensitive information. Detecting Spectre gadgets from programs has been a research focus to enhance the analysis and understanding of Spectre attacks. However, one of the problems of existing approaches is that they rely on the presence of source code (or are impractical in terms of run-time performance and gadget detection ability). This paper presents Teapot, the first Spectre gadget scanner that works on COTS binaries with comparable performance to compiler-based alternatives. As its core principle, we introduce Speculation Shadows, a novel approach that separates the binary code for normal execution and speculation simulation in order to improve run-time efficiency. Teapot is based on static binary rewriting. It instruments the program to simulate the effects of speculative execution and also adds integrity checks to detect Spectre gadgets at run time. By leveraging fuzzing, Teapot succeeds in efficiently detecting Spectre gadgets. Evaluations show that Teapot outperforms both performance (more than 20x performant) and gadget detection ability than a previously proposed binary-based approach.

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
