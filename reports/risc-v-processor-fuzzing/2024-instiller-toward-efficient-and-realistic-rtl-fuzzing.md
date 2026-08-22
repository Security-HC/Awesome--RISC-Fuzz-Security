# Instiller: Toward Efficient and Realistic RTL Fuzzing

## 基本信息

- 作者：Gen Zhang、Pengfei Wang、Tai Yue、Danjun Liu、Yubei Guo、Kai Lu
- 发表日期：2024-01-29
- 会议/期刊：IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=9）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: rtl fuzzing；hardware/processor object: cpu, rtl；verification/fuzzing method: fuzz
- 论文页面：[https://doi.org/10.1109/TCAD.2024.3360318](https://doi.org/10.1109/TCAD.2024.3360318)
- PDF：[https://arxiv.org/pdf/2401.15967](https://arxiv.org/pdf/2401.15967)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 15 页，提取 77730 字符

## 摘要

Bugs exist in hardware, such as CPU. Unlike software bugs, these hardware bugs need to be detected before deployment. Previous fuzzing work in CPU bug detection has several disadvantages, e.g., the length of register transition level (RTL) input instructions keeps growing, and longer inputs are ineffective for fuzzing. In this article, we propose Instiller (Instruction Distiller), an RTL fuzzer based on ant colony optimization (ACO). First, to keep the input instruction length short and efficient in fuzzing, it distills input instructions with a variant of ACO (VACO). Next, related work cannot simulate realistic interruptions well in fuzzing, and Instiller solves the problem of inserting interruptions and exceptions in generating the inputs. Third, to further improve the fuzzing performance of Instiller, we propose hardware-based seed selection and mutation strategies. We implement a prototype and conduct extensive experiments against state-of-the-art fuzzing work in real-world target CPU cores. In experiments, Instiller has 29.4% more coverage than DiFuzzRTL. In addition, 17.0% more mismatches are detected by Instiller. With the VACO algorithm, Instiller generates 79.3% shorter input instructions than DiFuzzRTL, demonstrating its effectiveness in distilling the input instructions. In addition, the distillation leads to a 6.7% increase in execution speed on average.

## 研究问题

RTL级CPU fuzzing面临三个挑战：输入指令长度不断增长导致执行效率下降且覆盖率不随长度线性提升；既有方法无法真实模拟多中断、异常及其优先级；种子选择与变异未充分利用硬件特征。

## Introduction 梳理

硬件bug（如Meltdown、Spectre）部署后难以修补，RTL验证至关重要。现有RTL fuzzing工具（如DiFuzzRTL）输入指令不断变长，降低效率；中断异常模拟过于简单，未包含多中断、异常及优先级；种子选择与变异未结合硬件特性。本文提出Instiller，基于蚁群优化变体（VACO）蒸馏输入指令，实现多中断/异常模拟，并设计硬件相关种子选择与变异策略，从而提升覆盖率和bug检测能力。

## 方法

输入生成：基于VACO的指令蒸馏，通过关系提取（软件数据/控制流关系、硬件时钟/中断/特权/特殊寄存器关系）形成指令组，用VACO迭代选择最优指令长度和组合；额外插入多中断和异常（支持优先级）。反馈/coverage：使用控制寄存器覆盖（DiFuzzRTL定义），并计算覆盖率/长度作为启发性信息。Oracle：差分测试，比较ISA模拟（Spike）与RTL模拟（cocotb）结果，不一致即mismatch，不需要golden model（Spike本身作为参考模型）。DUT/平台：目标CPU为mor1kx、or1200、Boom、Rocket（RISC-V/OpenRISC）。实现基于DiFuzzRTL，使用FIRRTL仪器化、Verilator仿真。

## 实验与评估

Baseline：DiFuzzRTL（主要），额外对比HFP、RFuzz（无差分测试），以及多个消融配置（I_NSTILLER−R、−V、−RV等）和简单上限长度策略。实验预算：每个CPU 24小时fuzzing，重复10次，报告p值和A12统计。结果：覆盖率平均提升29.4%（各CPU +11.9%~+36.5%），输入长度平均缩短79.3%，mismatch平均增加17.0%（除mor1kx外所有CPU提升），执行速度平均提升6.7%。额外实验：VACO vs 简单上限策略，VACO显著更好；中断/异常相关覆盖占10%以上，相关bug约占10%；12个真实世界bug中复现8个。开销：关系提取和VACO引入开销（禁用关系提取速度+6.3%，禁用VACO速度-9.4%），种子选择和变异开销可忽略。Artifact：未确认（未提供源码/链接）。

## 核心贡献

1) 提出基于VACO的输入指令蒸馏技术，缩短输入长度并保持/提升覆盖率；2) 首次在RTL fuzzing中支持多中断、异常及优先级处理，更真实模拟CPU执行；3) 提出硬件相关种子选择（使用归一化启发式）和变异策略（字典、插入、删除等）；4) 实现并评估原型，证明有效性。

## 与本仓库研究主线的关系

直接相关：这是针对RISC-V处理器RTL的fuzzing工作，属于处理器验证和硬件fuzzing范畴。与多hart/一致性路径研究关系较弱：本文聚焦单核上的中断/异常和指令序列优化，未涉及多hart并发或内存一致性模型。但其中断/异常和优先级处理与多核中断控制器（PLIC）相关，可能为多核验证提供基础。

## 结论

作者总结解决了三个挑战：提出基于VACO指令蒸馏、多中断异常模拟和硬件相关种子选择/变异，实现原型Instiller，实验证明在覆盖率、输入长度和漏洞发现方面优于现有工作。

## 局限性

作者在讨论中指出：RTL仿真速度仍远慢于二进制fuzzing（每秒一次 vs 数千次）；FIRRTL仪器化耗时；目前仅支持RISC-V/OpenRISC，未来计划扩展到ARM和x86；未涉及power schedule，留作未来工作；覆盖机制可针对侧信道等特定bug改进。另：mismatch数量作为漏洞指标，但未确认所有mismatch均为真实硬件bug。

## 详细阅读分析

仔细阅读VACO算法（Algorithm 3）与关系提取（Algorithm 2）的实现在代码中的具体逻辑，特别是如何将覆盖率作为启发式信息融入概率计算。第二，研究中断/异常插入如何修改mcause/scause等寄存器以及如何选择优先级组合，其实现细节在signature_checker.py中。第三，检查种子选择公式（Equation 4）中硬件指标的权重敏感性，以及变异策略（Equation 5）中长度阈值l的设定。第四，分析实验统计数据的稳健性，注意mor1kx上mismatch下降的归因。

## 后续核验问题

- 1) VACO参数（ρ、w、l）在不同CPU核上的敏感性如何？是否可能有自动调参机制？2) 多中断/异常插入是否会误触发非法状态或导致噪声？如何过滤误报？3) 该技术能否扩展到多核RTL平台，以覆盖内存一致性或缓存一致性相关路径？4) 与生成式RTL fuzzing（如Cascade）相比，蒸馏方法的优势在何种规模下体现？5) 是否考虑使用更细粒度的覆盖指标（如FSM、mux）与现有控制寄存器覆盖结合？
