# Fuzzing Hardware Like Software

## 基本信息

- 作者：Timothy Trippel、Kang G. Shin、Alex Chernyakhovsky、Garret Kelly、Dominic Rizzo、Matthew Hicks
- 发表日期：2021-02-03
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：B·强邻近（score=90）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：manual adjacent seed title
- 论文页面：[http://arxiv.org/abs/2102.02308v1](http://arxiv.org/abs/2102.02308v1)
- PDF：[https://arxiv.org/pdf/2102.02308v1](https://arxiv.org/pdf/2102.02308v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 15 页，提取 85944 字符

## 摘要

Hardware flaws are permanent and potent: hardware cannot be patched once fabricated, and any flaws may undermine any software executing on top. Consequently, verification time dominates implementation time. The gold standard in hardware Design Verification (DV) is concentrated at two extremes: random dynamic verification and formal verification. Both struggle to root out the subtle flaws in complex hardware that often manifest as security vulnerabilities. The root problem with random verification is its undirected nature, making it inefficient, while formal verification is constrained by the state-space explosion problem, making it infeasible against complex designs. What is needed is a solution that is directed, yet under-constrained. Instead of making incremental improvements to existing DV approaches, we leverage the observation that existing software fuzzers already provide such a solution, and adapt them for hardware DV. Specifically, we translate RTL hardware to a software model and fuzz that model. The central challenge we address is how best to mitigate the differences between the hardware execution model and software execution model. This includes: 1) how to represent test cases, 2) what is the hardware equivalent of a crash, 3) what is an appropriate coverage metric, and 4) how to create a general-purpose fuzzing harness for hardware. To evaluate our approach, we fuzz four IP blocks from Google's OpenTitan SoC. Our experiments reveal a two orders-of-magnitude reduction in run time to achieve Finite State Machine (FSM) coverage over traditional dynamic verification schemes. Moreover, with our design-agnostic harness, we achieve over 88% HDL line coverage in three out of four of our designs -- even without any initial seeds.

## 研究问题

硬件验证中随机动态验证效率低，形式化验证受状态空间爆炸限制，现有覆盖导向测试生成（CDG）方法存在覆盖率追踪慢和设计兼容性差的问题。

## Introduction 梳理

硬件缺陷永久且严重，验证时间超过实现时间。现有动态验证（CRV）和形式化验证各有局限。CDG方法虽有前景，但存在覆盖率追踪瓶颈和设计专用性。作者主张将硬件RTL转换为软件模型，直接利用现有软件模糊测试器进行硬件验证，克服上述挑战。

## 方法

输入生成：使用覆盖引导的灰盒模糊测试器（AFL），通过变异种子文件生成测试用例。反馈/coverage：通过编译时插桩追踪软件模型的基本块边覆盖率。Oracle：使用SystemVerilog断言（SVA）或黄金模型比较，违反时触发崩溃。DUT/平台：将RTL硬件通过Verilator转换为C++软件模型，与通用测试台和仿真引擎链接形成硬件仿真二进制（HSB）。需要golden model：支持两种方法：不变性检查（SVA）和黄金模型检查。对于数字锁实验，使用SVA作为crash条件；对于OpenTitan IP，使用SVA。

## 实验与评估

baseline：与约束随机验证（CRV）比较。实验预算：数字锁实验：480种不同状态数和代码宽度组合，每种20次试验；OpenTitan IP：4个IP块（AES, HMAC, KMAC, RV-Timer），每种语法组合10次重复，24小时。统计：使用Mann-Whitney U检验（显著性水平0.05）。bug/CVE：未明确报告发现的bug或CVE。开销：硬件模糊测试比CRV快两个数量级达到FSM覆盖率。Artifact：开源硬件模糊测试管道（HWFP）[33]。

## 核心贡献

1) 提出将硬件RTL转换为软件模型并用软件模糊测试器进行硬件验证；2) 提供经验指导：仅插桩DUT部分，硬件复位开销可忽略；3) 设计通用模糊测试台和总线语法（TL-UL），实现设计无关的模糊测试；4) 开源HWFP管道；5) 实验证明相比CRV快两个数量级。

## 与本仓库研究主线的关系

直接相关。论文主题是RTL硬件模糊测试，属于仓库核心方向。但与多hart/一致性路径研究不直接相关，主要针对单个IP核的验证，未涉及多核一致性。方法可借鉴到多hart场景（如通过总线语法驱动多个核）。

## 结论

硬件模糊测试是有效的CDG解决方案，通过将硬件翻译为软件模型并利用软件模糊测试工具，实现了设计无关的测试，相比CRV快两个数量级，在无种子情况下1小时内对3/4的商业IP达到88%以上HDL行覆盖率。

## 局限性

1) 没有硬件sanitizer，需要手动创建不变性或黄金模型；2) 不适用于检测模拟域侧信道漏洞。

## 详细阅读分析

论文详细讨论了如何将硬件仿真二进制（HSB）与软件模糊测试器接口，包括仅插桩DUT部分、如何处理硬件复位、如何将一维输入映射到时空二维序列。提出总线语法和指令格式优化。实验部分对比了不同语法格式（定长/变长指令帧，常量/映射操作码）对覆盖率收敛的影响。

## 后续核验问题

- 如何在多核或多hart系统中应用硬件模糊测试？
- 如何扩展总线语法以支持一致性协议？
- 硬件模糊测试能否检测到如Spectre之类的微架构安全漏洞？
- 是否需要专门的硬件sanitizer来检测更多漏洞类型？
- 对于非总线接口的硬件，如何设计通用语法？
