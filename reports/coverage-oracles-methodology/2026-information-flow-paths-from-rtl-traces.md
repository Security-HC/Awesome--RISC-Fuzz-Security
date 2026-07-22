# Information Flow Paths from RTL Traces

## 基本信息

- 作者：Calvin Deutschbein、Owyn Wyatt
- 发表日期：2026-06-11
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：B·强邻近（score=5）
- 证据等级：摘要级
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: rtl；verification/fuzzing method: validation, information flow tracking；security relevance: security
- 论文页面：[http://arxiv.org/abs/2606.13860v1](http://arxiv.org/abs/2606.13860v1)
- PDF：[https://arxiv.org/pdf/2606.13860v1](https://arxiv.org/pdf/2606.13860v1)
- 分析模式：DeepSeek PDF 首 8 页与末 2 页文本：deepseek-v4-flash

## 摘要

Security validation is an important yet challenging part of the hardware design process, yet, by convention, validation engineers are tasked with defining the threat model, specifying the relevant security properties, detecting any violations of those properties, and assessing the consequences to system security, each of which is manually intensive and may introduce errors. The combined technologies of information flow tracking and specification mining represent an automated approach to property generation and validation, but prior work on information flow tracking on RTL trace data was limited to find cases under which information flowed between registers, without reproducing full paths to capture how sensitive information propagates through a design. With the introduction of new technologies accelerating hardware analysis, we develop a novel approach for constructing information flow paths from register transfer level (RTL) trace data.

## 研究问题

从RTL跟踪数据中重建信息流路径，确定敏感信息从源信号到汇信号的确切传播路径，解决先前工作仅能检测寄存器间是否存在信息流而无法再现完整路径的问题。

## Introduction 梳理

硬件安全验证面临手动定义威胁模型、指定安全属性和检测违规的挑战，过程繁琐且易出错。结合信息流跟踪（IFT）和规范挖掘可实现自动化属性生成和验证，但先前IFT在RTL跟踪数据上的工作仅限于发现寄存器间是否存在信息流，无法再现敏感信息如何通过设计传播的完整路径。本文针对这一缺口，提出了一种从RTL跟踪数据构建信息流路径的新方法。

## 方法

方法包括：1) 使用Cycuity Radix IFT工具对设计进行插桩，为每个信号添加跟踪信号；2) 对每个信号作为根源信号进行仿真（使用提供的测试台），生成VCD跟踪文件；3) 提取时间流（time-of-flow）元组（根源信号、汇信号、时间增量）；4) 通过稀疏表示（字典格式）或Parquet格式存储数据；5) 构建信息流图：从时间流元组中识别已知非边、已知边，并通过候选提升和路径查找循环推导候选边；6) 输出路径树。输入为RTL设计和测试台，无需金模型，但需要测试台驱动仿真；覆盖反馈未显式提及；Oracle为IFT跟踪信号的置位事件；DUT包括PicoRV32和AKER等开源设计；平台依赖仿真器（如Radix）和并行化工具Myrtha。

## 实验与评估

在PicoRV32 RISC-V CPU（232个寄存器，3049行Verilog，2201周期测试台）上评估。Baseline为先前Isadora工具，本文能发现更精确的路径。实验预算：序列仿真所有182个非平凡寄存器耗时8小时45分钟，预计并行化可降至约3.5秒。结果找到路径长度2至5，数量分别为151、130、71、59。发现CWE-1244（内部资产暴露于不安全调试访问）和CWE-411（非预期代理/中介）的实例。存储开销：VCD文件64MB，数据框525MB，稀疏表示419KB，图36KB，路径32KB。Artifact：代码开源在GitHub。未确认：与其他工具的详细性能对比、对多核设计的扩展性。

## 核心贡献

1. 提出从RTL跟踪数据构建信息流路径的新算法，解决先前无法重建完整路径的问题。2. 实现并验证了在PicoRV32上自动发现CWE的流程。3. 使用稀疏表示和并行化提高效率，并开源代码。

## 与本仓库研究主线的关系

直接相关，属于RTL硬件Fuzzing中的Oracle和覆盖分析领域。该方法可作为信息流路径的Oracle，帮助验证处理器安全性。虽未涉及多hart或内存一致性，但其路径构建技术可借鉴用于多核场景下的信息流分析。

## 结论

本文展示了一种从RTL跟踪数据提取信息流路径的技术，可有效识别硬件设计中的安全漏洞（如CWE）。在PicoRV32上的案例验证了方法的可行性，并展示了自动发现路径和归类漏洞的能力。

## 局限性

1) 依赖测试台覆盖，覆盖率不足可能遗漏路径。2) 存在候选边（因逻辑OR导致模糊），无法通过跟踪数据唯一确定。3) 对于大规模设计，仿真所有信号仍可能开销较高。4) 当前方法基于单次仿真，未结合形式化方法处理所有可行路径。

## 详细阅读分析

建议深入阅读，其图构建算法、稀疏表示方法和并行化策略对硬件Fuzzing工具开发有参考价值。

## 后续核验问题

- 如何将候选边消除与静态分析或符号执行结合？
- 该方法能否扩展至多核/多hart设计？
- 如何处理测试台覆盖不足的问题？
- 在大规模设计（如SERV）上的性能表现如何？
