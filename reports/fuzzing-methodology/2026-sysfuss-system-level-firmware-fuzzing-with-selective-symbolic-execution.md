# SysFuSS: System-Level Firmware Fuzzing with Selective Symbolic Execution

## 基本信息

- 作者：Dakshina Tharindu、Aruna Jayasena、Prabhat Mishra
- 发表日期：2026-02-02
- 更新日期：2026-02-02
- 来源：arXiv
- 来源编号：2602.02243v1
- 研究类别：Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2602.02243v1](http://arxiv.org/abs/2602.02243v1)
- PDF：[https://arxiv.org/pdf/2602.02243v1](https://arxiv.org/pdf/2602.02243v1)
- 分析模式：仅元数据分析

## 摘要

Firmware serves as the critical interface between hardware and software in computing systems, making any bugs or vulnerabilities particularly dangerous as they can cause catastrophic system failures. While fuzzing is a promising approach for identifying design flaws and security vulnerabilities, traditional fuzzers are ineffective at detecting firmware vulnerabilities. For example, existing fuzzers focus on user-level fuzzing, which is not suitable for detecting kernel-level vulnerabilities. Existing fuzzers also face a coverage plateau problem when dealing with complex interactions between firmware and hardware. In this paper, we present an efficient firmware verification framework, SysFuSS, that integrates system-level fuzzing with selective symbolic execution. Our approach leverages system-level emulation for initial fuzzing, and automatically transitions to symbolic execution when coverage reaches a plateau. This strategy enables us to generate targeted test cases that can trigger previously unexplored regions in firmware designs. We have evaluated SysFuSS on real-world embedded firmware, including OpenSSL, WolfBoot, WolfMQTT, HTSlib, MXML, and libIEC. Experimental evaluation demonstrates that SysFuSS significantly outperforms state-of-the-art fuzzers in terms of both branch coverage and detection of firmware vulnerabilities. Specifically, SysFuSS can detect 118 known vulnerabilities while state-of-the-art can cover only 13 of them. Moreover, SysFuSS takes significantly less time (up to 3.3X, 1.7X on average) to activate these vulnerabilities.

## 研究问题

Firmware serves as the critical interface between hardware and software in computing systems, making any bugs or vulnerabilities particularly dangerous as they can cause catastrophic system failures. While fuzzing is a promising approach for identifying design flaws and security vulnerabilities, traditional fuzzers are ineffective at detecting firmware vulnerabilities. For example, existing fuzzers focus on user-level fuzzing, which is not suitable for detecting kernel-level vulnerabilities. Existing fuzzers also face a coverage plateau problem when dealing with complex interactions between firmware and hardware. In this paper, we present an efficient firmware verification framework, SysFuSS, that integrates system-level fuzzing with selective symbolic execution. Our approach leverages system-level emulation for initial fuzzing, and automatically transitions to symbolic execution when coverage reaches a plateau. This strategy enables us to generate targeted test cases that can trigger previously unexplored regions in firmware designs. We have evaluated SysFuSS on real-world embedded firmware, including OpenSSL, WolfBoot, WolfMQTT, HTSlib, MXML, and libIEC. Experimental evaluation demonstrates that SysFuSS significantly outperforms state-of-the-art fuzzers in terms of both branch coverage and detection of firmware vulnerabilities. Specifically, SysFuSS can detect 118 known vulnerabilities while state-of-the-art can cover only 13 of them. Moreover, SysFuSS takes significantly less time (up to 3.3X, 1.7X on average) to activate these vulnerabilities.

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
