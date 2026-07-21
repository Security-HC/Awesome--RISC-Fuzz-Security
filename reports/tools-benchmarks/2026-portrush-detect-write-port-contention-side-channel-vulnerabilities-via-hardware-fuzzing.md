# PortRush: Detect Write Port Contention Side-Channel Vulnerabilities via Hardware Fuzzing

## 基本信息

- 作者：Peihong Lin、Pengfei Wang、Lei Zhou、Gen Zhang、Xu Zhou、Wei Xie、Zhiyuan Jiang、Kai Lu
- 发表日期：2026
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：67f5ab50d038a60bdd9d39ccc03e1088bec32478
- 研究类别：RISC-V Fuzzing 研究、微架构安全、RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.14722/ndss.2026.240587](https://doi.org/10.14722/ndss.2026.240587)
- PDF：[https://doi.org/10.14722/ndss.2026.240587](https://doi.org/10.14722/ndss.2026.240587)
- 分析模式：仅元数据分析

## 摘要

—CPU vulnerabilities pose ongoing security challenges in modern CPU architectures. Among the CPU vulnerabilities, write port contention—caused by multiple functional modules simultaneously competing for a limited number of shared write ports—remains insufficiently studied. In this paper, we study write port contention side-channel vulnerabilities in CPUs and propose P ORT R USH , a novel fuzzing framework designed to detect and validate such vulnerabilities at the register-transfer level (RTL). First, P ORT R USH constructs a Write Request Graph (WRG) to statically identify potential write port contention instances by modeling write paths and priority relationships among functional modules that target shared storage elements. Second, within the WRG, P ORT R USH implements a Hierarchical Aggregation and Decoding method to efficiently detect write port contention by monitoring relevant hardware signals across design hierarchies. Third, P ORT R USH employs a Contention-guided Hardware Fuzzing approach to trigger write port contention and automatically combine contention-triggered instruction sequences with transient execution attack patterns, enabling validation of write port contention side-channel vulnerabilities. We evaluate P ORT R USH on three RISC-V CPUs (BOOM, NutShell, and Rocket Core) and demonstrate its effectiveness in identifying and triggering write port contention. Furthermore, we validate that the discovered vulnerabilities can be exploited in realistic write port contention attack scenarios. Based on these vulnerabilities, we present two novel attack vectors: Birgus-variant , which exploits contention at the physical register file in the Reorder Buffer, and MSHRush , which leverages contention be-tween the Load / Store Unit ( LSU ) and Miss Status Handling Register ( MSHR ) at the L1 data cache to induce secret-dependent execution delays. We also propose mitigation strategies for CPU developers to prevent such vulnerabilities.

## 研究问题

—CPU vulnerabilities pose ongoing security challenges in modern CPU architectures. Among the CPU vulnerabilities, write port contention—caused by multiple functional modules simultaneously competing for a limited number of shared write ports—remains insufficiently studied. In this paper, we study write port contention side-channel vulnerabilities in CPUs and propose P ORT R USH , a novel fuzzing framework designed to detect and validate such vulnerabilities at the register-transfer level (RTL). First, P ORT R USH constructs a Write Request Graph (WRG) to statically identify potential write port contention instances by modeling write paths and priority relationships among functional modules that target shared storage elements. Second, within the WRG, P ORT R USH implements a Hierarchical Aggregation and Decoding method to efficiently detect write port contention by monitoring relevant hardware signals across design hierarchies. Third, P ORT R USH employs a Contention-guided Hardware Fuzzing approach to trigger write port contention and automatically combine contention-triggered instruction sequences with transient execution attack patterns, enabling validation of write port contention side-channel vulnerabilities. We evaluate P ORT R USH on three RISC-V CPUs (BOOM, NutShell, and Rocket Core) and demonstrate its effectiveness in identifying and triggering write port contention. Furthermore, we validate that the discovered vulnerabilities can be exploited in realistic write port contention attack scenarios. Based on these vulnerabilities, we present two novel attack vectors: Birgus-variant , which exploits contention at the physical register file in the Reorder Buffer, and MSHRush , which leverages contention be-tween the Load / Store Unit ( LSU ) and Miss Status Handling Register ( MSHR ) at the L1 data cache to induce secret-dependent execution delays. We also propose mitigation strategies for CPU developers to prevent such vulnerabilities.

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
