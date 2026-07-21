# The Role of Road Features and Vehicle Dynamics in Cost-Effective Autonomous Vehicles Safety Testing: Insights from Instance Space Analysis

## 基本信息

- 作者：Victor Crespo-Rodriguez、Christian Birchler、Neelofar、Aldeida Aleti、Sebastiano Panichella
- 发表日期：2026-03-22
- 更新日期：2026-03-22
- 来源：arXiv
- 来源编号：2603.21066v1
- 研究类别：RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2603.21066v1](http://arxiv.org/abs/2603.21066v1)
- PDF：[https://arxiv.org/pdf/2603.21066v1](https://arxiv.org/pdf/2603.21066v1)
- 分析模式：仅元数据分析

## 摘要

Context: Simulation-based testing is a cost-efficient alternative to field testing for Autonomous Vehicles (AVs), but generating safety-critical test cases is challenging due to the vast search space. Prior work has studied static (road features) and dynamic (AV behavior) features of test scenarios separately, but their inter-dependencies are underexplored. Objective: In this paper, we describe an empirical to analyze how static and dynamic featuresof test scenarios, and their inter-dependencies, influence AV test scenario outcomes. Method: This study proposes an integrated approach using Instance Space Analysis (ISA) toevaluate both types of features, identify key influences on AV safety, and predict test outcomeswithout execution. Results: Our study identifies critical features affecting test outcomes (effective/ineffective, depending on whether it leads to a safety-critical condition). Results show that combining static and dynamic features improves prediction accuracy, confirmed by models trained on both feature types outperforming models trained with only one type of feature. Conclusion: The interplay of static and dynamic features enhances fault detection in AV testing. This research underscores the importance of integrating both types of features to create more effective testing frameworks for autonomous systems. Key contributions include: (1) a unified framework for AV safety assessment, (2) identification of influential features using ISA, and (3) efficient test outcome prediction for optimized regression testing.

## 研究问题

Context: Simulation-based testing is a cost-efficient alternative to field testing for Autonomous Vehicles (AVs), but generating safety-critical test cases is challenging due to the vast search space. Prior work has studied static (road features) and dynamic (AV behavior) features of test scenarios separately, but their inter-dependencies are underexplored. Objective: In this paper, we describe an empirical to analyze how static and dynamic featuresof test scenarios, and their inter-dependencies, influence AV test scenario outcomes. Method: This study proposes an integrated approach using Instance Space Analysis (ISA) toevaluate both types of features, identify key influences on AV safety, and predict test outcomeswithout execution. Results: Our study identifies critical features affecting test outcomes (effective/ineffective, depending on whether it leads to a safety-critical condition). Results show that combining static and dynamic features improves prediction accuracy, confirmed by models trained on both feature types outperforming models trained with only one type of feature. Conclusion: The interplay of static and dynamic features enhances fault detection in AV testing. This research underscores the importance of integrating both types of features to create more effective testing frameworks for autonomous systems. Key contributions include: (1) a unified framework for AV safety assessment, (2) identification of influential features using ISA, and (3) efficient test outcome prediction for optimized regression testing.

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
