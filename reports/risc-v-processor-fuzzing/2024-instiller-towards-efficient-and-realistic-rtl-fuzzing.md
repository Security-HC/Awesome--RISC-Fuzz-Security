# INSTILLER: Towards Efficient and Realistic RTL Fuzzing

## 基本信息

- 作者：Gen Zhang、Pengfei Wang、Tai Yue、Danjun Liu、Yubei Guo、Kai Lu
- 发表日期：2024-01-29
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=9）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: rtl fuzzing；hardware/processor object: cpu, rtl；verification/fuzzing method: fuzz
- 论文页面：[http://arxiv.org/abs/2401.15967v1](http://arxiv.org/abs/2401.15967v1)
- PDF：[https://arxiv.org/pdf/2401.15967v1](https://arxiv.org/pdf/2401.15967v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 15 页，提取 77824 字符

## 摘要

Bugs exist in hardware, such as CPU. Unlike software bugs, these hardware bugs need to be detected before deployment. Previous fuzzing work in CPU bug detection has several disadvantages, e.g., the length of RTL input instructions keeps growing, and longer inputs are ineffective for fuzzing. In this paper, we propose INSTILLER (Instruction Distiller), an RTL fuzzer based on ant colony optimization (ACO). First, to keep the input instruction length short and efficient in fuzzing, it distills input instructions with a variant of ACO (VACO). Next, related work cannot simulate realistic interruptions well in fuzzing, and INSTILLER solves the problem of inserting interruptions and exceptions in generating the inputs. Third, to further improve the fuzzing performance of INSTILLER, we propose hardware-based seed selection and mutation strategies. We implement a prototype and conduct extensive experiments against state-of-the-art fuzzing work in real-world target CPU cores. In experiments, INSTILLER has 29.4% more coverage than DiFuzzRTL. In addition, 17.0% more mismatches are detected by INSTILLER. With the VACO algorithm, INSTILLER generates 79.3% shorter input instructions than DiFuzzRTL, demonstrating its effectiveness in distilling the input instructions. In addition, the distillation leads to a 6.7% increase in execution speed on average.

## 研究问题

解决RTL fuzzing中指令长度不断增长导致效率低下、缺乏真实中断异常模拟以及缺少硬件感知的种子选择和变异策略的问题。

## Introduction 梳理

现有RTL fuzzing工作（如DiFuzzRTL）存在三个主要不足：1) 输入指令长度随fuzzing持续增长，长指令不利于fuzzing效率且覆盖率不随长度比例增长；2) 无法模拟真实世界中的多中断和异常处理，缺失嵌套中断和优先级；3) 未充分利用硬件特征进行种子选择和变异。本文提出INSTILLER，通过基于蚁群优化变体的指令蒸馏、多中断异常模拟以及硬件相关的种子选择和变异来提升RTL fuzzing的效率和真实性。

## 方法

{'dut_platform': '目标RTL设计：mor1kx、or1200、Boom、Rocket（RISC-V和OpenRISC核）。', 'feedback_coverage': '采用控制寄存器覆盖率（DiFuzzRTL定义），并利用覆盖率反馈指导VACO的终止条件（平均覆盖率下降时启动）。', 'golden_model': '需要Spike作为黄金参考模型。', 'input_generation': '基于蚁群优化变体（VACO）进行指令蒸馏，通过关系提取构建指令组，用VACO算法输出当前最优指令长度和组合；种子选择使用归一化启发式（覆盖率、执行速度、特殊指令数量）；变异包括字典替换、插入、删除、基本变异，根据长度条件选择。', 'oracle': '差分测试：比较Spike（ISA模拟器）和Verilator（RTL模拟器）的输出结果，不一致即潜在bug。'}

## 实验与评估

{'artifact': '未明确提供开源仓库链接，但提及实现基于DiFuzzRTL，代码约1750行。', 'baseline': 'DiFuzzRTL（主要）、RFuzz、HFP；还比较了INSTILLER去除组件的变体。', 'bug_cve': '检测到17.0%更多不匹配（平均1573.9 vs 1344.4），在8个真实世界bug中可复现6个（原文说8/12，但表XII显示8个可复现，实为8/12）。', 'experiment_budget': '每个目标CPU进行24小时fuzzing，重复10次。', 'overhead': '关系提取和VACO带来性能开销，但整体执行速度提升6.7%；去除此模块后速度与DiFuzzRTL相当。', 'statistics': '计算p值和A12值，p<0.05且A12>0.5表示统计显著。'}

## 核心贡献

1) 提出基于蚁群优化变体的指令蒸馏技术，缩短输入长度并维持覆盖率；2) 实现多中断和异常模拟，涵盖优先级和嵌套场景；3) 设计硬件感知的种子选择和变异策略；4) 开源原型INSTILLER，实验表明在覆盖率、输入长度和漏洞检测上优于现有工具。

## 与本仓库研究主线的关系

直接相关：论文主题为RISC-V处理器RTL fuzzing，使用差分测试和覆盖率反馈，与仓库中处理器验证、硬件fuzzing直接对应。但未涉及多hart（多核）或内存一致性验证，其关注单核CPU的指令级fuzzing。可借鉴其VACO优化和中断异常插入方法用于多hart场景。

## 结论

INSTILLER通过VACO指令蒸馏、多中断异常模拟和硬件相关种子选择/变异，显著提升了RTL fuzzing的覆盖率和漏洞发现能力，同时缩短了输入指令长度并提高了执行速度。

## 局限性

RTL仿真速度仍远慢于二进制fuzzing（每秒一次vs数千次）；RTL工具链复杂（需FIRRTL）；仅支持RISC-V和OpenRISC，未扩展到ARM/x86；未探索功率调度（power schedule）；黄金模型(Spike)也可能存在bug。

## 详细阅读分析

推荐精读，尤其VACO算法（III-B节）、中断异常模拟（III-C节）和实验设置（V节）。需注意实验中的覆盖率定义为控制寄存器覆盖率，与仓库中其他工作的覆盖率可能不同。

## 后续核验问题

- VACO算法中的蒸发率ρ和启发式权重如何影响不同CPU核的fuzzing效果？
- 中断异常插入是否考虑了不同hart之间的交互（如跨核中断）？
- 种子选择公式中的RTL启发式（ld_st, fp, jp）是否适用于多hart场景？
- 论文未提及多hart或cache一致性，是否可以扩展其方法验证多核系统的内存一致性？
- 黄金模型Spike是否完全正确？其自身bug如何影响差分测试的可靠性？
