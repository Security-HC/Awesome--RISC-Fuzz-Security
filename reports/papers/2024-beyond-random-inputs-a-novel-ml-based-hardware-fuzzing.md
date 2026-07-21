# Beyond Random Inputs: A Novel ML-Based Hardware Fuzzing

## 基本信息

- 作者：Mohamadreza Rostami、Marco Chilese、Shaza Zeitouni、Rahul Kande、Jeyavijayan Rajendran、Ahmad-Reza Sadeghi
- 发表日期：2024-04-10
- 更新日期：2024-04-10
- 来源：arXiv
- 来源编号：2404.06856v1
- 研究类别：RISC-V Fuzzing、RTL and Hardware Verification
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：3
- 论文页面：[http://arxiv.org/abs/2404.06856v1](http://arxiv.org/abs/2404.06856v1)
- PDF：[https://arxiv.org/pdf/2404.06856v1](https://arxiv.org/pdf/2404.06856v1)
- 分析模式：仅元数据分析

## 摘要

Modern computing systems heavily rely on hardware as the root of trust. However, their increasing complexity has given rise to security-critical vulnerabilities that cross-layer at-tacks can exploit. Traditional hardware vulnerability detection methods, such as random regression and formal verification, have limitations. Random regression, while scalable, is slow in exploring hardware, and formal verification techniques are often concerned with manual effort and state explosions. Hardware fuzzing has emerged as an effective approach to exploring and detecting security vulnerabilities in large-scale designs like modern processors. They outperform traditional methods regarding coverage, scalability, and efficiency. However, state-of-the-art fuzzers struggle to achieve comprehensive coverage of intricate hardware designs within a practical timeframe, often falling short of a 70% coverage threshold. We propose a novel ML-based hardware fuzzer, ChatFuzz, to address this challenge. Ourapproach leverages LLMs like ChatGPT to understand processor language, focusing on machine codes and generating assembly code sequences. RL is integrated to guide the input generation process by rewarding the inputs using code coverage metrics. We use the open-source RISCV-based RocketCore processor as our testbed. ChatFuzz achieves condition coverage rate of 75% in just 52 minutes compared to a state-of-the-art fuzzer, which requires a lengthy 30-hour window to reach a similar condition coverage. Furthermore, our fuzzer can attain 80% coverage when provided with a limited pool of 10 simulation instances/licenses within a 130-hour window. During this time, it conducted a total of 199K test cases, of which 6K produced discrepancies with the processor's golden model. Our analysis identified more than 10 unique mismatches, including two new bugs in the RocketCore and discrepancies from the RISC-V ISA Simulator.

## 研究问题

Modern computing systems heavily rely on hardware as the root of trust. However, their increasing complexity has given rise to security-critical vulnerabilities that cross-layer at-tacks can exploit. Traditional hardware vulnerability detection methods, such as random regression and formal verification, have limitations. Random regression, while scalable, is slow in exploring hardware, and formal verification techniques are often concerned with manual effort and state explosions. Hardware fuzzing has emerged as an effective approach to exploring and detecting security vulnerabilities in large-scale designs like modern processors. They outperform traditional methods regarding coverage, scalability, and efficiency. However, state-of-the-art fuzzers struggle to achieve comprehensive coverage of intricate hardware designs within a practical timeframe, often falling short of a 70% coverage threshold. We propose a novel ML-based hardware fuzzer, ChatFuzz, to address this challenge. Ourapproach leverages LLMs like ChatGPT to understand processor language, focusing on machine codes and generating assembly code sequences. RL is integrated to guide the input generation process by rewarding the inputs using code coverage metrics. We use the open-source RISCV-based RocketCore processor as our testbed. ChatFuzz achieves condition coverage rate of 75% in just 52 minutes compared to a state-of-the-art fuzzer, which requires a lengthy 30-hour window to reach a similar condition coverage. Furthermore, our fuzzer can attain 80% coverage when provided with a limited pool of 10 simulation instances/licenses within a 130-hour window. During this time, it conducted a total of 199K test cases, of which 6K produced discrepancies with the processor's golden model. Our analysis identified more than 10 unique mismatches, including two new bugs in the RocketCore and discrepancies from the RISC-V ISA Simulator.

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
