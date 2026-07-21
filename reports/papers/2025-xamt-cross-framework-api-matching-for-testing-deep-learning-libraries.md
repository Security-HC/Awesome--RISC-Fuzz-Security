# XAMT: Cross-Framework API Matching for Testing Deep Learning Libraries

## 基本信息

- 作者：Bin Duan、Ruican Dong、Naipeng Dong、Dan Dongseong Kim、Guowei Yang
- 发表日期：2025-08-18
- 更新日期：2025-08-18
- 来源：arXiv
- 来源编号：2508.12546v1
- 研究类别：Fuzzing Methodology、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2508.12546v1](http://arxiv.org/abs/2508.12546v1)
- PDF：[https://arxiv.org/pdf/2508.12546v1](https://arxiv.org/pdf/2508.12546v1)
- 分析模式：仅元数据分析

## 摘要

Deep learning powers critical applications such as autonomous driving, healthcare, and finance, where the correctness of underlying libraries is essential. Bugs in widely used deep learning APIs can propagate to downstream systems, causing serious consequences. While existing fuzzing techniques detect bugs through intra-framework testing across hardware backends (CPU vs. GPU), they may miss bugs that manifest identically across backends and thus escape detection under these strategies. To address this problem, we propose XAMT, a cross-framework fuzzing method that tests deep learning libraries by matching and comparing functionally equivalent APIs across different frameworks. XAMT matches APIs using similarity-based rules based on names, descriptions, and parameter structures. It then aligns inputs and applies variance-guided differential testing to detect bugs. We evaluated XAMT on five popular frameworks, including PyTorch, TensorFlow, Keras, Chainer, and JAX. XAMT matched 839 APIs and identified 238 matched API groups, and detected 17 bugs, 12 of which have been confirmed. Our results show that XAMT uncovers bugs undetectable by intra-framework testing, especially those that manifest consistently across backends. XAMT offers a complementary approach to existing methods and offers a new perspective on the testing of deep learning libraries.

## 研究问题

Deep learning powers critical applications such as autonomous driving, healthcare, and finance, where the correctness of underlying libraries is essential. Bugs in widely used deep learning APIs can propagate to downstream systems, causing serious consequences. While existing fuzzing techniques detect bugs through intra-framework testing across hardware backends (CPU vs. GPU), they may miss bugs that manifest identically across backends and thus escape detection under these strategies. To address this problem, we propose XAMT, a cross-framework fuzzing method that tests deep learning libraries by matching and comparing functionally equivalent APIs across different frameworks. XAMT matches APIs using similarity-based rules based on names, descriptions, and parameter structures. It then aligns inputs and applies variance-guided differential testing to detect bugs. We evaluated XAMT on five popular frameworks, including PyTorch, TensorFlow, Keras, Chainer, and JAX. XAMT matched 839 APIs and identified 238 matched API groups, and detected 17 bugs, 12 of which have been confirmed. Our results show that XAMT uncovers bugs undetectable by intra-framework testing, especially those that manifest consistently across backends. XAMT offers a complementary approach to existing methods and offers a new perspective on the testing of deep learning libraries.

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
