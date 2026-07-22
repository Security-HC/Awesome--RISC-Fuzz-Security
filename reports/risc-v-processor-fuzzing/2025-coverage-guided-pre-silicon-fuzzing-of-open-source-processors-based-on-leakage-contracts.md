# Coverage-Guided Pre-Silicon Fuzzing of Open-Source Processors based on Leakage Contracts

## 基本信息

- 作者：Gideon Geier、Pariya Hajipour、Jan Reineke
- 发表日期：2025-11-11
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=8）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Microarchitectural Security Testing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: risc-v, processor, microarchitectural；verification/fuzzing method: fuzz, coverage-guided, verification；security relevance: security, leakage
- 论文页面：[http://arxiv.org/abs/2511.08443v2](http://arxiv.org/abs/2511.08443v2)
- PDF：[https://arxiv.org/pdf/2511.08443v2](https://arxiv.org/pdf/2511.08443v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 12 页，提取 67674 字符

## 摘要

Hardware-software leakage contracts have emerged as a formalism for specifying side-channel security guarantees of modern processors, yet verifying that a complex hardware design complies with its contract remains a major challenge. While verification provides strong guarantees, current verification approaches struggle to scale to industrial-sized designs. Conversely, prevalent hardware fuzzing approaches are designed to find functional correctness bugs, but are blind to information leaks like Spectre. To bridge this gap, we introduce a novel and scalable approach: coverage-guided hardware-software contract fuzzing. Our methodology leverages a self-compositional framework to make information leakage directly observable as microarchitectural state divergence. The core of our contribution is a new, security-oriented coverage metric, Self-Composition Deviation (SCD), which guides the fuzzer to explore execution paths that violate the leakage contract. We implemented this approach and performed an extensive evaluation on two open-source RISC-V cores: the in-order Rocket Core and the complex out-of-order BOOM core. Our results demonstrate that coverage-guided strategies outperform unguided fuzzing and that increased microarchitectural coverage leads to a faster discovery of security vulnerabilities in the BOOM core.

## 研究问题

验证开源RISC-V处理器在流片前是否满足硬件-软件泄漏契约，现有形式化验证难以扩展，传统硬件模糊测试忽略侧信道泄漏，后硅片契约感知模糊测试缺乏覆盖引导。

## Introduction 梳理

硬件-软件泄漏契约形式化了侧信道安全保证，但验证复杂设计遵守契约面临可扩展性挑战；当前验证方法（如形式化验证）无法扩展到工业级设计，而硬件模糊测试针对功能正确性，对Spectre等信息泄漏盲视。本文填补这一空白，提出覆盖引导的硬件-软件契约模糊测试，利用自组合框架使信息泄漏直接可观察为微架构状态偏差，并引入安全导向的覆盖度量SCD来引导探索。

## 方法

输入生成：基于DifuzzRTL，随机生成指令序列（最多4条指令一个word）和两个数据段（共3072字节），支持三种数据生成策略（全随机、seq-arch专用、50-50混合），并通过变异（Mutate/Merge）和LRU缓存数据段。反馈/覆盖：定义Self-Composition Deviation (SCD)覆盖，度量两个处理器实例微架构寄存器偏差，使用滚动哈希（SHAKE128）压缩为2^24位覆盖向量。Oracle：基于Sail实现的leakage contracts（seq-ct, seq-ct-b, seq-arch），通过自组合框架检查两个实例是否contract-indistinguishable但attacker-distinguishable（attacker模型为程序总体执行周期数）。DUT/平台：两个开源RISC-V核心Rocket（顺序，5级）和BOOM（乱序，10级），使用Verilator仿真，cocotb桥接，TileLink TL-C总线协议，在Chipyard框架中集成。是否需要golden model：不需要经典golden model，使用Sail契约模拟器作为参考。

## 实验与评估

Baseline：无覆盖引导的Pass Feedback策略（语料库大小1000）。实验预算：每策略5次运行（10000次迭代/运行），后续针对BOOM核心进行100次运行。统计：使用曼-惠特尼U检验（p<0.05）。Bug/CVE：在Rocket核心上未发现违反seq-ct-b和seq-ct的泄漏；在BOOM核心上发现违反seq-arch的泄漏（未列出具体CVE编号）。开销：每个测试用例在Rocket上约1.5秒（包括仿真和I/O），BOOM更长；通过并行化（32任务一组）缓解。Artifact：未明确提及开源工件。

## 核心贡献

1) 首个将覆盖引导引入硬件-软件契约模糊测试的工作；2) 定义安全导向覆盖度量Self-Composition Deviation (SCD)；3) 设计并实现多种优先级策略，实验证明Weighted Feedback策略在累积覆盖和泄漏发现速度上均优于无引导方法。

## 与本仓库研究主线的关系

直接相关：主题完全匹配RISC-V处理器模糊测试和微架构安全自动测试。与多hart/一致性路径无直接关联，但自组合框架可扩展至多核场景。

## 结论

覆盖引导优先策略（Weighted Feedback）显著提高累积覆盖，且更高覆盖导致更快发现BOOM核心的契约违反。加权的 Self-Composition Deviation 覆盖度量为安全导向的模糊测试提供有效反馈。

## 局限性

1) 仅测试RV64I基础指令集，排除M扩展以简化，可能遗漏相关泄漏；2) 未考虑异常和中断；3) Rocket核心未发现泄漏，可能因设计安全或测试未充分探索；4) 仿真速度慢（每个测试用例1.5秒以上）；5) 基于DifuzzRTL，继承其程序生成局限性；6) SCD覆盖基于寄存器级偏差，可能不捕获所有微架构泄漏（如缓存状态）。

## 详细阅读分析

第III-C节SCD覆盖度的形式化定义与滚动哈希实现；第IV-D节加权反馈优先级公式；第V节实验设置和结果分析（表I-VIII）。

## 后续核验问题

- SCD覆盖能否有效引导发现其他类型侧信道（如功耗、电磁）？
- 如何将自组合方法扩展到多hart或内存一致性验证？
- 能否通过更高效的仿真（如FPGA加速）降低开销？
- 对于Rocket核心未发现泄漏，是否由于seq-ct-b契约本身在顺序处理器上满足，还是测试不充分？
