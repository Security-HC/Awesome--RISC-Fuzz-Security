# ProcessorFuzz: Guiding Processor Fuzzing using Control and Status Registers

## 基本信息

- 作者：Sadullah Canakci、Chathura Rajapaksha、Anoop Mysore Nataraja、Leila Delshadtehrani、Michael Taylor、Manuel Egele、Ajay Joshi
- 发表日期：2022-09-05
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in title: processor fuzzing；hardware/processor object: risc-v, processor, rtl；verification/fuzzing method: fuzz, verification；security relevance: security, side channel
- 论文页面：[http://arxiv.org/abs/2209.01789v1](http://arxiv.org/abs/2209.01789v1)
- PDF：[https://arxiv.org/pdf/2209.01789v1](https://arxiv.org/pdf/2209.01789v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 17 页，提取 98361 字符

## 摘要

As the complexity of modern processors has increased over the years, developing effective verification strategies to identify bugs prior to manufacturing has become critical. Undiscovered micro-architectural bugs in processors can manifest as severe security vulnerabilities in the form of side channels, functional bugs, etc. Inspired by software fuzzing, a technique commonly used for software testing, multiple recent works use hardware fuzzing for the verification of Register-Transfer Level (RTL) designs. However, these works suffer from several limitations such as lack of support for widely-used Hardware Description Languages (HDLs) and misleading coverage-signals that misidentify "interesting" inputs. Towards overcoming these shortcomings, we present ProcessorFuzz, a processor fuzzer that guides the fuzzer with a novel CSR-transition coverage metric. ProcessorFuzz monitors the transitions in Control and Status Registers (CSRs) as CSRs are in charge of controlling and holding the state of the processor. Therefore, transitions in CSRs indicate a new processor state, and guiding the fuzzer based on this feedback enables ProcessorFuzz to explore new processor states. ProcessorFuzz is agnostic to the HDL and does not require any instrumentation in the processor design. Thus, it supports a wide range of RTL designs written in different hardware languages. We evaluated ProcessorFuzz with three real-world open-source processors -- Rocket, BOOM, and BlackParrot. ProcessorFuzz triggered a set of ground-truth bugs 1.23$\times$ faster (on average) than DIFUZZRTL. Moreover, our experiments exposed 8 new bugs across the three RISC-V cores and one new bug in a reference model. All nine bugs were confirmed by the developers of the corresponding projects.

## 研究问题

现有处理器硬件fuzzer（如DIFUZZRTL）的寄存器覆盖率指标监控大量数据通路寄存器，这些寄存器的变化不代表处理器FSM状态变化，误导fuzzer花费时间在无意义的输入上，降低bug发现效率。

## Introduction 梳理

处理器验证面临状态空间爆炸问题，动态验证需高效方法。现有硬件fuzzer（如DIFUZZRTL）使用寄存器覆盖率，但该指标会监控数据通路寄存器（如余数寄存器），其变化不反映FSM状态变化，导致fuzzer被误导。本文提出ProcessorFuzz，利用控制状态寄存器（CSR）的转换作为覆盖率指标，通过ISA仿真快速判断输入是否有趣，避免缓慢的RTL仿真，从而加速bug发现。

## 方法

输入生成：从空种子集开始，生成随机汇编程序，通过变异引擎对种子进行删除、追加、替换指令等变异。反馈/覆盖率：使用CSR转换覆盖率，监控ISA仿真中每个指令执行后CSR值的变化，通过转换单元检查是否为新的转换（存储为(指令助记符, 转换前CSR值, 转换后CSR值)），新转换则标记输入为有趣。Oracle：差异测试，对有新转换的输入同时运行RTL仿真，比较ISA仿真和RTL仿真的扩展跟踪日志（包含寄存器最终状态），不一致则报bug。DUT/平台：Rocket、BOOM、BlackParrot三款开源RISC-V处理器。是否需要golden model：是，使用ISA模拟器（Spike用于Rocket和BOOM，Dromajo用于BlackParrot）作为参考模型。

## 实验与评估

baseline: DIFUZZRTL的两种设置（no-cov-difuzzrtl和reg-cov-difuzzrtl）。实验预算：每个处理器设计重复10次，每次48小时，总计4320 CPU小时。统计：使用Time-to-Exposure (TTE)度量。bug/CVE: 在BOOM上发现6个ground-truth bug（比DIFUZZRTL平均快1.23倍）；在BlackParrot发现6个新bug，Rocket/BOOM发现1个新bug，Dromajo发现1个新bug，BOOM发现1个性能退化bug（mstatus.FS不当设为dirty），合计9个新bug，均被开发者确认。开销：ISA模拟器Spike的代码行开销0.4%，运行时开销0.15%。Artifact: 源代码将开源（论文中声明）。

## 核心贡献

1) 提出CSR转换覆盖率指标，利用CSR转换反映处理器FSM状态变化；2) 使用ISA仿真快速确定有趣输入，避免慢速RTL仿真；3) 在三个开源RISC-V处理器上发现9个新bug（8个设计bug，1个参考模型bug）。

## 与本仓库研究主线的关系

直接相关：主题是RISC-V处理器fuzzing，提出的CSR转换覆盖率方法直接适用于处理器验证。但与多hart/内存一致性验证无直接关系，论文未涉及多hart或缓存一致性路径。

## 结论

ProcessorFuzz通过CSR转换覆盖率有效引导处理器fuzzing，比DIFUZZRTL平均快1.23倍，并发现9个新bug。

## 局限性

1) 仅评估了RISC-V ISA，对其他ISA的适用性未验证；2) 依赖ISA仿真反馈，可能错过只在RTL仿真中出现的CSR转换；3) 不从RTL仿真收集覆盖率反馈，可能漏掉某些bug。

## 详细阅读分析

建议深入阅读第3节（方法细节，包括CSR选择准则、转换单元工作流）、第4节（实验设置和结果，特别是表1-3的TTE数据）、第6节（讨论与局限性）。

## 后续核验问题

- 1) ProcessorFuzz能否扩展到多hart系统？如何利用CSR转换处理hart间交互？2) 论文中ISA仿真比RTL仿真快79倍，该比例是否具有普遍性？3) 对于非RISC-V ISA（如x86），CSR选择准则是否直接适用？
