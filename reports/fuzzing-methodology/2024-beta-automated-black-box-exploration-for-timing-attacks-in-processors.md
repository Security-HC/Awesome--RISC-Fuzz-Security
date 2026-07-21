# BETA: Automated Black-box Exploration for Timing Attacks in Processors

## 基本信息

- 作者：Congcong Chen、Jinhua Cui、Jiliang Zhang
- 发表日期：2024-10-22
- 更新日期：2024-10-22
- 来源：arXiv
- 来源编号：2410.16648v1
- 研究类别：微架构安全、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2410.16648v1](http://arxiv.org/abs/2410.16648v1)
- PDF：[https://arxiv.org/pdf/2410.16648v1](https://arxiv.org/pdf/2410.16648v1)
- 分析模式：仅元数据分析

## 摘要

Modern processor advancements have introduced security risks, particularly in the form of microarchitectural timing attacks. High-profile attacks such as Meltdown and Spectre have revealed critical flaws, compromising the entire system's security. Recent black-box automated methods have demonstrated their advantages in identifying these vulnerabilities on various commercial processors. However, they often focus on specific attack types or incorporate numerous ineffective test cases, which severely limits the detection scope and efficiency. In this paper, we present BETA, a novel black-box framework that harnesses fuzzing to efficiently uncover multifaceted timing vulnerabilities in processors. Our framework employs a two-pronged approach, enhancing both mutation space and exploration efficiency: 1) we introduce an innovative fuzzer that precisely constrains mutation direction for diverse instruction combinations, including opcode, data, address, and execution level; 2) we develop a coverage feedback mechanism based on our instruction classification to discard potentially trivial or redundant test cases. This mechanism significantly expands coverage across a broader spectrum of instruction types. We evaluate the performance and effectiveness of BETA on four processors from Intel and AMD, each featuring distinct microarchitectures. BETA has successfully detected all x86 processor vulnerabilities previously identified by recent black-box methods, as well as 8 previously undiscovered timing vulnerabilities. BETA outperforms the existing state-of-the-art black-box methods, achieving at least 3x faster detection speed.

## 研究问题

Modern processor advancements have introduced security risks, particularly in the form of microarchitectural timing attacks. High-profile attacks such as Meltdown and Spectre have revealed critical flaws, compromising the entire system's security. Recent black-box automated methods have demonstrated their advantages in identifying these vulnerabilities on various commercial processors. However, they often focus on specific attack types or incorporate numerous ineffective test cases, which severely limits the detection scope and efficiency. In this paper, we present BETA, a novel black-box framework that harnesses fuzzing to efficiently uncover multifaceted timing vulnerabilities in processors. Our framework employs a two-pronged approach, enhancing both mutation space and exploration efficiency: 1) we introduce an innovative fuzzer that precisely constrains mutation direction for diverse instruction combinations, including opcode, data, address, and execution level; 2) we develop a coverage feedback mechanism based on our instruction classification to discard potentially trivial or redundant test cases. This mechanism significantly expands coverage across a broader spectrum of instruction types. We evaluate the performance and effectiveness of BETA on four processors from Intel and AMD, each featuring distinct microarchitectures. BETA has successfully detected all x86 processor vulnerabilities previously identified by recent black-box methods, as well as 8 previously undiscovered timing vulnerabilities. BETA outperforms the existing state-of-the-art black-box methods, achieving at least 3x faster detection speed.

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
