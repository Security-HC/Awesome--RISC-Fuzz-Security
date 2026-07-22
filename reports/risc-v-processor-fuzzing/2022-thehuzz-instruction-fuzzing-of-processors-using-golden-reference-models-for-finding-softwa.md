# TheHuzz: Instruction Fuzzing of Processors Using Golden-Reference Models for Finding Software-Exploitable Vulnerabilities

## 基本信息

- 作者：Aakash Tyagi、Addison Crump、Ahmad-Reza Sadeghi、Garrett Persyn、Jeyavijayan Rajendran、Patrick Jauernig、Rahul Kande
- 发表日期：2022-01-24
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2201.09941v1](http://arxiv.org/abs/2201.09941v1)
- PDF：[https://arxiv.org/pdf/2201.09941v1](https://arxiv.org/pdf/2201.09941v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 23 页，提取 100000 字符

## 摘要

The increasing complexity of modern processors poses many challenges to existing hardware verification tools and methodologies for detecting security-critical bugs. Recent attacks on processors have shown the fatal consequences of uncovering and exploiting hardware vulnerabilities. Fuzzing has emerged as a promising technique for detecting software vulnerabilities. Recently, a few hardware fuzzing techniques have been proposed. However, they suffer from several limitations, including non-applicability to commonly used Hardware Description Languages (HDLs) like Verilog and VHDL, the need for significant human intervention, and inability to capture many intrinsic hardware behaviors, such as signal transitions and floating wires. In this paper, we present the design and implementation of a novel hardware fuzzer, TheHuzz, that overcomes the aforementioned limitations and significantly improves the state of the art. We analyze the intrinsic behaviors of hardware designs in HDLs and then measure the coverage metrics that model such behaviors. TheHuzz generates assembly-level instructions to increase the desired coverage values, thereby finding many hardware bugs that are exploitable from software. We evaluate TheHuzz on four popular open-source processors and achieve 1.98x and 3.33x the speed compared to the industry-standard random regression approach and the state-of-the-art hardware fuzzer, DiffuzRTL, respectively. Using TheHuzz, we detected 11 bugs in these processors, including 8 new vulnerabilities, and we demonstrate exploits using the detected bugs. We also show that TheHuzz overcomes the limitations of formal verification tools from the semiconductor industry by comparing its findings to those discovered by the Cadence JasperGold tool.

## 研究问题

现有硬件模糊测试方法无法有效检测处理器中软件可利用的漏洞，存在不支持常见HDL（Verilog/VHDL）、需大量人工干预、不能捕获信号跳变和浮空线等硬件固有行为、规模受限等问题。

## Introduction 梳理

论文指出现有硬件验证技术（形式验证、运行时检测、信息流追踪）的局限性：形式验证面临状态爆炸、难以扩展到大设计；运行时检测仅在制造后可用；信息流追踪需要手动标记且易产生误报。模糊测试在软件领域成功，但直接应用于硬件存在挑战：硬件不崩溃、仿真速度慢、无法直接使用软件覆盖反馈。TheHuzz通过直接对RTL仿真并使用黄金参考模型（GRM）比较，同时采用多种硬件覆盖指标（语句、分支、表达式、跳变、FSM、条件）指导输入生成，克服了上述限制。

## 方法

输入生成：在ISA层级生成汇编指令序列，包括配置指令（CI，初始化裸机环境）和测试指令（TI，用于模糊测试）。种子生成器产生初始序列，刺激生成器通过AFL风格的变异（位翻转、算术、随机覆盖、删除、克隆、操作码覆盖等）生成新序列，并保留能提高覆盖的序列。反馈/覆盖：使用工业标准仿真工具ModelSim提取六种覆盖指标（语句、分支、表达式、跳变、FSM、条件），覆盖日志反馈给变异引擎。Oracle：将每个指令执行后的寄存器/内存跟踪与黄金参考模型（GRM）比较，对于RISC-V处理器使用spike，对于OpenRISC使用or1ksim。DUT/平台：RTL仿真，支持Verilog和VHDL，无需修改目标处理器。黄金模型：需要GRM作为比较基准。

## 实验与评估

baseline: 随机回归测试（random regression）和DifuzzRTL（最先进硬件模糊测试器），以及形式验证工具Cadence JasperGold。实验预算：每种实验重复10次，在32核Intel Xeon 2.6GHz、512GB RAM、CentOS 7.3上运行。统计：Mann-Whitney U检验p<0.05，Vargha-Delaney A12度量显示TheHuzz最优。bug/CVE: 在Ariane、mor1kx、or1200和Rocket Core四个处理器中发现11个bug，其中8个新漏洞，每个bug映射到CWE（如CWE-440、CWE-1202等），并给出两个利用演示（Ariane FENCE.I漏洞导致缓存一致性问题，mor1kx EPCR寄存器漏洞导致权限提升）。开销：运行时开销71%（高于DifuzzRTL的6.9%），但作者解释是因为需要收集多种覆盖指标。Artifact：计划开源。

## 核心贡献

1. 提出TheHuzz，首个结合语句、跳变、分支、表达式、条件、FSM六种覆盖指标的硬件模糊器，直接对RTL进行指令级模糊测试。2. 通过优化选择最佳指令和变异技术，提升模糊效率。3. 在四个开源处理器上发现11个bug（8个新），并提供两个可利用的漏洞演示。4. 对比形式验证工具JasperGold，显示TheHuzz无需人工编写断言、可扩展至大设计。

## 与本仓库研究主线的关系

直接相关：论文专注于RISC-V处理器模糊测试，使用黄金参考模型作为Oracle，覆盖指标包含FSM和表达式等，可用于单核处理器的软件可利用漏洞检测。对于多hart/内存一致性验证，论文仅涉及单核内的缓存一致性（B4），未扩展至多核。但方法（指令生成、覆盖引导、GRM比较）可借鉴于多核一致性测试，例如在多核仿真中比较各核的存储行为。

## 结论

TheHuzz是第一个直接使用多种硬件覆盖指标引导RTL模糊测试的处理器模糊器，相比随机回归测试速度提升1.98×，相比DifuzzRTL速度提升3.33×，无需人工设计安全规则，发现11个bug（其中8个新漏洞），并展示了两个可利用的软件攻击。

## 局限性

依赖黄金参考模型（但工业中普遍存在）；需要RTL源代码（可通过逆向工程获取）；目前仅支持处理器设计，不支持非处理器模块（如SoC外设）；不能用于FPGA仿真（因为覆盖指标不易获取）；不测试参数化行为（如缓存时序，无法检测侧信道漏洞）。

## 详细阅读分析

推荐深入阅读Section 4.1（硬件行为与覆盖指标的关系）、Section 4.4（优化选择指令和变异）、Section 6.3（漏洞利用案例）以及附录中的变异技术列表。

## 后续核验问题

- 1. 如何将TheHuzz扩展至多核/多hart情境？是否需调整覆盖指标（如增加互连覆盖）或Oracle（如使用一致性模型）？2. 当没有现成黄金参考模型时（如新型处理器），如何自动构建？3. 优化选择（指令-变异权重）是否在不同处理器上表现一致？是否有理论保证？
