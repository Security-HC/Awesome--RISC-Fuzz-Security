# PortRush: Detect Write Port Contention Side-Channel Vulnerabilities via Hardware Fuzzing

## 基本信息

- 作者：Peihong Lin、Pengfei Wang、Lei Zhou、Gen Zhang、Xu Zhou、Wei Xie、Zhiyuan Jiang、Kai Lu、Peihong Lin
- 发表日期：2026-01-01
- 会议/期刊：未记录
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Microarchitectural Security Testing、RTL & SoC Hardware Fuzzing
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: risc-v, cpu, rtl, mshr；verification/fuzzing method: fuzz, validation；security relevance: security, transient execution
- 论文页面：[https://doi.org/10.14722/ndss.2026.240587](https://doi.org/10.14722/ndss.2026.240587)
- PDF：[https://doi.org/10.14722/ndss.2026.240587](https://doi.org/10.14722/ndss.2026.240587)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 18 页，提取 100000 字符

## 摘要

CPU vulnerabilities pose ongoing security challenges in modern CPU architectures.Among the CPU vulnerabilities, write port contention-caused by multiple functional modules simultaneously competing for a limited number of shared write ports-remains insufficiently studied.In this paper, we study write port contention side-channel vulnerabilities in CPUs and propose PORTRUSH, a novel fuzzing framework designed to detect and validate such vulnerabilities at the register-transfer level (RTL).First, PORTRUSH constructs a Write Request Graph (WRG) to statically identify potential write port contention instances by modeling write paths and priority relationships among functional modules that target shared storage elements.Second, within the WRG, PORTRUSH implements a Hierarchical Aggregation and Decoding method to efficiently detect write port contention by monitoring relevant hardware signals across design hierarchies.Third, PORTRUSH employs a Contention-guided Hardware Fuzzing approach to trigger write port contention and automatically combine contention-triggered instruction sequences with transient execution attack patterns, enabling validation of write port contention side-channel vulnerabilities.We evaluate PORTRUSH on three RISC-V CPUs (BOOM, NutShell, and Rocket Core) and demonstrate its effectiveness in identifying and triggering write port contention.Furthermore, we validate that the discovered vulnerabilities can be exploited in realistic write port contention attack scenarios.Based on these vulnerabilities, we present two novel attack vectors: Birgus-variant, which exploits contention at the physical register file in the Reorder Buffer, and MSHRush, which leverages contention between the Load/Store Unit (LSU) and Miss Status Handling Register (MSHR) at the L1 data cache to induce secret-dependent execution delays.We also propose mitigation strategies for CPU developers to prevent such vulnerabilities.

## 研究问题

针对CPU微架构中写端口竞争侧信道漏洞的检测与验证问题，现有工作未专门研究此类漏洞，缺乏静态识别、动态监测和自动利用验证的方法。

## Introduction 梳理

现有CPU漏洞检测方法（如静态形式验证和硬件Fuzzing）未针对写端口竞争侧信道漏洞，该漏洞由多个功能模块同时竞争有限共享写端口引起，可通过时序差异泄露秘密信息。本文提出PORTRUSH框架，通过静态构建写请求图、层次化聚合解码实时监测、竞争引导硬件Fuzzing以及结合瞬态执行攻击模式自动验证，填补了这一空白。

## 方法

{'dut_platform': '三个开源RISC-V CPU：BOOM、NutShell、Rocket Core，在Verilator软件仿真环境中运行。', 'feedback_coverage': '寄存器覆盖率和写请求行为覆盖率（WPC coverage），以及Gini惩罚项促进写实体均衡覆盖。', 'golden_model': '未使用golden model；漏洞验证通过时序差异测量和瞬态执行监测自包含完成。', 'input_generation': '基于PSO优化器的种子生成，参数包括指令序列长度、操作码权重向量、中断时序参数；分探索和利用两个阶段，探索阶段使用RISC-V ISA字典，利用阶段基于现有种子变异。', 'oracle': '通过结合瞬态执行攻击模式验证：三个标准——瞬态执行成功触发（使用SpecDoctor监测）、写端口竞争发生、受害函数执行时间差异与秘密值相关。'}

## 实验与评估

{'artifact': '论文未明确提及artifact发布，但代码实现细节在实现章节描述（Scala和Python代码约1600行）。', 'baseline': '与DiFuzzRTL对比寄存器覆盖率和WPC覆盖率。', 'bugs_cve': '发现3个可利用漏洞（包括两个新变体Birgus-variant和MSHRush，以及已知Spectre-STC），已分配CVE编号。', 'experiment_budget': '每个DUT进行5次独立fuzzing运行，每次24小时；粒子群参数：种群大小30-50，迭代100-200。', 'overhead': '未确认具体的性能开销数据。', 'statistical_metrics': '寄存器覆盖率：PORTRUSH平均比DiFuzzRTL低6.90%（Rocket Core 6.27%，BOOM 7.03%），p值<0.001；WPC覆盖率：PORTRUSH 32.1% vs DiFuzzRTL 5.5%。'}

## 核心贡献

首次系统化研究写端口竞争侧信道漏洞，提出包含静态识别、实时监测、竞争引导Fuzzing和自动利用验证的完整框架PORTRUSH；发现两个新攻击变体MSHRush和Birgus-variant，并复现已知Spectre-STC攻击。

## 与本仓库研究主线的关系

直接相关。主题为RISC-V处理器硬件Fuzzing检测写端口竞争侧信道漏洞，与多hart/一致性路径研究属同一大类（微架构安全自动测试），但本文聚焦单核写端口竞争而非多核一致性。方法（WRG构建、竞争引导Fuzzing）可推广至多hart场景中的共享资源竞争分析。

## 结论

PORTRUSH能有效检测、触发和验证写端口竞争侧信道漏洞，在三个RISC-V CPU上发现177个潜在竞争实例，触发35个，其中3个可实际利用。写端口竞争侧信道攻击不同于传统缓存攻击，即使处理器有安全缓存也能泄露信息。

## 局限性

部分潜在竞争实例需要三个以上写实体同时请求，在24小时测试窗口内难触发；Rocket Core因单发射顺序架构无法实际触发；公平仲裁或增加写端口可能引入性能开销和设计复杂度，需权衡。

## 详细阅读分析

建议重点阅读方法部分IV-B至IV-E（WRG构建、信号聚合、竞争引导Fuzzing、利用验证），以及评估部分VI-D中MSHRush案例（展示攻击构建和时序分布图）。

## 后续核验问题

- PORTRUSH能否扩展到多核/多hart场景中的写端口竞争（如共享L2缓存写端口）？
- 层次化信号聚合方法在更复杂SoC（如有多个存储元素和深层次嵌套）中的可扩展性如何？
- PSO优化器的参数设置（种群大小、迭代次数）对覆盖率和竞争触发效率的敏感度如何？
- 除了RISC-V，该方法是否适用于x86或ARM处理器RTL？
- 提出的缓解策略（公平仲裁、增加写端口、优先长延迟指令）在实际设计中的性能开销如何量化？
