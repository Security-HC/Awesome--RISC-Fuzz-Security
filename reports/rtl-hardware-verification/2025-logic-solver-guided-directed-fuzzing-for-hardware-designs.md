# Logic Solver Guided Directed Fuzzing for Hardware Designs

## 基本信息

- 作者：Raghul Saravanan、Sai Manoj P D
- 发表日期：2025-09-30
- 更新日期：2025-09-30
- 来源：arXiv
- 来源编号：2509.26509v1
- 研究类别：RTL 与硬件验证
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：3
- 论文页面：[http://arxiv.org/abs/2509.26509v1](http://arxiv.org/abs/2509.26509v1)
- PDF：[https://arxiv.org/pdf/2509.26509v1](https://arxiv.org/pdf/2509.26509v1)
- 分析模式：仅元数据分析

## 摘要

The ever-increasing complexity of design specifications for processors and intellectual property (IP) presents a formidable challenge for early bug detection in the modern IC design cycle. The recent advancements in hardware fuzzing have proven effective in detecting bugs in RTL designs of cutting-edge processors. The modern IC design flow involves incremental updates and modifications to the hardware designs necessitating rigorous verification and extending the overall verification period. To accelerate this process, directed fuzzing has emerged focusing on generating targeted stimuli for specific regions of the design, avoiding the need for exhaustive, full-scale verification. However, a significant limitation of these hardware fuzzers lies in their reliance on an equivalent SW model of the hardware which fails to capture intrinsic hardware characteristics. To circumvent the aforementioned challenges, this work introduces TargetFuzz, an innovative and scalable targeted hardware fuzzing mechanism. It leverages SAT-based techniques to focus on specific regions of the hardware design while operating at its native hardware abstraction level, ensuring a more precise and comprehensive verification process. We evaluated this approach across a diverse range of RTL designs for various IP cores. Our experimental results demonstrate its capability to effectively target and fuzz a broad spectrum of sites within these designs, showcasing its extensive coverage and precision in addressing targeted regions. TargetFuzz demonstrates its capability to effectively scale 30x greater in terms of handling target sites, achieving 100% state coverage and 1.5x faster in terms of site coverage, and shows 90x improvement in target state coverage compared to Coverage-Guided Fuzzing, demonstrating its potential to advance the state-of-the-art in directed hardware fuzzing.

## 研究问题

The ever-increasing complexity of design specifications for processors and intellectual property (IP) presents a formidable challenge for early bug detection in the modern IC design cycle. The recent advancements in hardware fuzzing have proven effective in detecting bugs in RTL designs of cutting-edge processors. The modern IC design flow involves incremental updates and modifications to the hardware designs necessitating rigorous verification and extending the overall verification period. To accelerate this process, directed fuzzing has emerged focusing on generating targeted stimuli for specific regions of the design, avoiding the need for exhaustive, full-scale verification. However, a significant limitation of these hardware fuzzers lies in their reliance on an equivalent SW model of the hardware which fails to capture intrinsic hardware characteristics. To circumvent the aforementioned challenges, this work introduces TargetFuzz, an innovative and scalable targeted hardware fuzzing mechanism. It leverages SAT-based techniques to focus on specific regions of the hardware design while operating at its native hardware abstraction level, ensuring a more precise and comprehensive verification process. We evaluated this approach across a diverse range of RTL designs for various IP cores. Our experimental results demonstrate its capability to effectively target and fuzz a broad spectrum of sites within these designs, showcasing its extensive coverage and precision in addressing targeted regions. TargetFuzz demonstrates its capability to effectively scale 30x greater in terms of handling target sites, achieving 100% state coverage and 1.5x faster in terms of site coverage, and shows 90x improvement in target state coverage compared to Coverage-Guided Fuzzing, demonstrating its potential to advance the state-of-the-art in directed hardware fuzzing.

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
