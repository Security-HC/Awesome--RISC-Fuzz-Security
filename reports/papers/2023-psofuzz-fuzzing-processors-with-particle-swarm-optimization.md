# PSOFuzz: Fuzzing Processors with Particle Swarm Optimization

## 基本信息

- 作者：Chen Chen、Vasudev Gohil、Rahul Kande、Ahmad-Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2023-07-26
- 更新日期：2023-08-18
- 来源：arXiv
- 来源编号：2307.14480v2
- 研究类别：RTL and Hardware Verification、Fuzzing Methodology
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2307.14480v2](http://arxiv.org/abs/2307.14480v2)
- PDF：[https://arxiv.org/pdf/2307.14480v2](https://arxiv.org/pdf/2307.14480v2)
- 分析模式：仅元数据分析

## 摘要

Hardware security vulnerabilities in computing systems compromise the security defenses of not only the hardware but also the software running on it. Recent research has shown that hardware fuzzing is a promising technique to efficiently detect such vulnerabilities in large-scale designs such as modern processors. However, the current fuzzing techniques do not adjust their strategies dynamically toward faster and higher design space exploration, resulting in slow vulnerability detection, evident through their low design coverage. To address this problem, we propose PSOFuzz, which uses particle swarm optimization (PSO) to schedule the mutation operators and to generate initial input programs dynamically with the objective of detecting vulnerabilities quickly. Unlike traditional PSO, which finds a single optimal solution, we use a modified PSO that dynamically computes the optimal solution for selecting mutation operators required to explore new design regions in hardware. We also address the challenge of inefficient initial seed generation by employing PSO-based seed generation. Including these optimizations, our final formulation outperforms fuzzers without PSO. Experiments show that PSOFuzz achieves up to 15.25$\times$ speedup for vulnerability detection and up to 2.22$\times$ speedup for coverage compared to the state-of-the-art simulation-based hardware fuzzer.

## 研究问题

Hardware security vulnerabilities in computing systems compromise the security defenses of not only the hardware but also the software running on it. Recent research has shown that hardware fuzzing is a promising technique to efficiently detect such vulnerabilities in large-scale designs such as modern processors. However, the current fuzzing techniques do not adjust their strategies dynamically toward faster and higher design space exploration, resulting in slow vulnerability detection, evident through their low design coverage. To address this problem, we propose PSOFuzz, which uses particle swarm optimization (PSO) to schedule the mutation operators and to generate initial input programs dynamically with the objective of detecting vulnerabilities quickly. Unlike traditional PSO, which finds a single optimal solution, we use a modified PSO that dynamically computes the optimal solution for selecting mutation operators required to explore new design regions in hardware. We also address the challenge of inefficient initial seed generation by employing PSO-based seed generation. Including these optimizations, our final formulation outperforms fuzzers without PSO. Experiments show that PSOFuzz achieves up to 15.25$\times$ speedup for vulnerability detection and up to 2.22$\times$ speedup for coverage compared to the state-of-the-art simulation-based hardware fuzzer.

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
