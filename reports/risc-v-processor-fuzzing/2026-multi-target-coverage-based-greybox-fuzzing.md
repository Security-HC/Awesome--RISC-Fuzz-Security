# Multi-target Coverage-based Greybox Fuzzing

## 基本信息

- 作者：Masami Ichikawa
- 发表日期：2026-03-26
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing
- 纳入依据：hardware/processor object: risc-v；verification/fuzzing method: fuzz；security relevance: vulnerability
- 论文页面：[http://arxiv.org/abs/2603.25354v1](http://arxiv.org/abs/2603.25354v1)
- PDF：[https://arxiv.org/pdf/2603.25354v1](https://arxiv.org/pdf/2603.25354v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 71 页，提取 100000 字符

## 摘要

In recent years, fuzzing has been widely applied not only to application software but also to system software, including the Linux kernel and firmware, and has become a powerful technique for vulnerability discovery. Among these approaches, Coverage-based grey-box fuzzing, which utilizes runtime code coverage information, has become the dominant methodology. Conventional fuzzing techniques primarily target a single software component and have paid little attention to cooperative execution with other software. However, modern system software architectures commonly consist of firmware and an operating system that operate cooperatively through well-defined interfaces, such as OpenSBI in the RISC-V architecture and OP-TEE in the ARM architecture. In this study, we investigate fuzzing techniques for architectures in which an operating system and firmware operate cooperatively. In particular, we propose a fuzzing method that enables deeper exploration of the system by leveraging the code coverage of each cooperating software component as feedback, compared to conventional Single-target fuzzing. To observe the execution of the operating system and firmware in a unified manner, our method adopts QEMU as a virtualization environment and executes fuzzing by booting the system within a virtual machine. This enables the measurement of code coverage across software boundaries. Furthermore, we implemented the proposed method as a Multi-target Coverage-based Greybox Fuzzer called MTCFuzz and evaluated its effectiveness.

## 研究问题

现有基于覆盖率的灰盒模糊测试主要针对单一软件组件，在多组件协作（如操作系统与固件）的现代系统软件架构中，无法利用跨组件边界的覆盖率信息，导致探索效率低下。

## Introduction 梳理

现代系统软件如RISC-V架构中的Linux内核与OpenSBI、ARM架构中的TrustZone，通过明确定义的接口协同执行。现有覆盖率引导的灰盒模糊测试仅测量单个组件的代码覆盖率，忽略了对协作组件的覆盖，无法检测因跨组件状态不一致导致的漏洞。本文提出多目标覆盖率反馈方法，通过QEMU统一测量多个组件的执行覆盖率，并实现原型MTCFuzz，在ARM和RISC-V平台上验证有效性。

## 方法

输入生成：基于AFL的种子变异策略，初始种子由用户提供（如系统调用参数）。反馈/覆盖率：通过修改QEMU的TCG翻译过程，在基本块粒度收集所有执行的PC地址；使用地址过滤器（JSON配置）仅保留指定内核和固件地址范围内的覆盖率，并计算哈希作为唯一标识用于反馈。Oracle：检测虚拟机崩溃（crash/hang信号）。DUT/平台：QEMU虚拟化环境，运行Linux内核+OpenSBI（RISC-V）或Linux+OP-TEE（ARM），测试用例通过ssh在guest中执行。Golden model：不需要。

## 实验与评估

Baseline：单目标模式（仅使用Linux内核覆盖率反馈）。实验预算：OpenSBI Base Extension实验：100次5分钟运行（两组各50次）；OP-TEE长运行：5次2小时、4次8小时、1次24小时；性能测试：hackbench基准测试。统计：多目标模式下55%的campaign达到完全覆盖（单目标34%），平均覆盖率提升约5.9%；长运行中多目标始终维持更高覆盖率。Bug/CVE：发现CVE-2025-40031（optee驱动中共享内存大小验证不足导致空指针解引用）。开销：QEMU测量引入45-65%性能开销（hackbench）；地址滤波器性能随滤波器数增加无明显下降（测试至2^15个滤波器）；快照加载引入约12.68%开销（从448次执行降至504.8次，提升12.68%）。Artifact：MTCFuzz原型，Docker容器，配置文件和复现脚本（未明确公开，但论文描述实现细节）。

## 核心贡献

1) 提出了多目标覆盖率灰盒模糊测试方法，统一利用多个协作软件组件的覆盖率反馈；2) 实现了原型系统MTCFuzz，基于QEMU无需修改源码或二进制；3) 在ARM和RISC-V两个架构上验证了方法的有效性和通用性；4) 发现并报告了一个新的CVE（CVE-2025-40031）。

## 与本仓库研究主线的关系

直接相关：本文针对RISC-V处理器（及ARM）中的操作系统与固件（OpenSBI/OP-TEE）协作系统进行模糊测试，属于RISC-V/处理器Fuzzing和微架构安全自动测试范畴。但与多hart/内存一致性验证无直接关联，其方法可借鉴于跨组件交互的漏洞发现，而非多处理器一致性保证。

## 结论

所提出的多目标覆盖率反馈方法在协作执行环境中比传统单目标模糊测试能获得更高代码覆盖率，且在QEMU下的性能开销和滤波器开销均在可接受范围内，证明该方法实用有效。

## 局限性

当前仅支持在单个QEMU实例内执行单个目标环境；测试驱动程序（test harness）需要手动创建，增加了应用难度；QEMU内覆盖率测量（fprintf写文件）导致显著性能开销。

## 详细阅读分析

建议重点阅读第三章（方法：QEMU instrument、地址滤波器、快照机制）和第四章（实验：覆盖率对比、性能开销、CVE发现），以理解具体实现和实验设计。

## 后续核验问题

- MTCFuzz能否扩展到多hart场景（如RISC-V多核系统）？是否会影响覆盖率反馈效率？
- 地址滤波器如何自动生成？能否结合符号分析以简化配置？
- 与硬件辅助模糊测试（如kAFL使用Intel PT）相比，QEMU方法在性能和发现能力上有何优劣？
