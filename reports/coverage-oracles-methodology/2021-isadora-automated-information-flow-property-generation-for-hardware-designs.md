# Isadora: Automated Information Flow Property Generation for Hardware Designs

## 基本信息

- 作者：Calvin Deutschbein、Andres Meza、Francesco Restuccia、Ryan Kastner、Cynthia Sturton
- 发表日期：2021-06-14
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, processor, soc；verification/fuzzing method: validation, information flow tracking；security relevance: security
- 论文页面：[http://arxiv.org/abs/2106.07449v2](http://arxiv.org/abs/2106.07449v2)
- PDF：[https://arxiv.org/pdf/2106.07449v2](https://arxiv.org/pdf/2106.07449v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 11 页，提取 60847 字符

## 摘要

Isadora is a methodology for creating information flow specifications of hardware designs. The methodology combines information flow tracking and specification mining to produce a set of information flow properties that are suitable for use during the security validation process, and which support a better understanding of the security posture of the design. Isadora is fully automated; the user provides only the design under consideration and a testbench and need not supply a threat model nor security specifications. We evaluate Isadora on a RISC-V processor plus two designs related to SoC access control. Isadora generates security properties that align with those suggested by the Common Weakness Enumerations (CWEs), and in the case of the SoC designs, align with the properties written manually by security experts.

## 研究问题

自动生成硬件设计的信息流安全属性，减少对手动属性定义的依赖。

## Introduction 梳理

现有安全验证工具（如JasperGold）需要用户手动指定安全属性，而手动定义复杂且易出错。Isadora结合信息流追踪（IFT）和规范挖掘，自动从设计+测试台中生成信息流属性，无需威胁模型或安全规范。IFT将信息流超属性转换为可挖掘的轨迹属性，首次实现硬件信息流安全属性的自动挖掘。

## 方法

输入：RTL设计（Verilog）和测试台。使用Tortuga Radix-S进行IFT检测，每个源信号单独追踪，模拟生成轨迹。第2阶段分析轨迹中跟踪信号从0→1的跳变，识别所有流对和时序，产生无流属性列表。第3阶段对每个流对截取2周期轨迹切片，用Daikon挖掘流量条件谓词（等式/不等式）。第4阶段后处理去除冗余和全部轨迹不变量，输出有条件流属性。无需Golden Model，依赖测试台覆盖。

## 实验与评估

设计：PicoRV32 RISC-V CPU, Single ACW, Multi ACW（AKER框架）。基线：与AKER设计者手动编写的安全断言比较，以及CWE映射。实验预算：Single ACW轨迹生成9h33m，可并行化至<5分钟；PicoRV32轨迹8h35m。统计：采样10个属性评估CWE相关性，Single ACW全部10个为安全相关，PicoRV32有8个安全相关（2个功能）。Bug/CVE：发现违背手动断言的流动条件，但设计者确认安全；对Multi ACW发现非法流（CWE 411）。开销：轨迹生成主导，可并行化。Artifact：Isadora实现（Python + Daikon + Radix-S + QuestaSim），未公开代码库。

## 核心贡献

首次结合信息流追踪与规范挖掘，全自动生成硬件信息流安全属性，无需用户提供安全目标或威胁模型。

## 与本仓库研究主线的关系

直接相关：提供硬件安全验证中的Oracle自动生成方法，可作为硬件Fuzzing的测试预言。与多hart/一致性路径无直接关系，但方法可扩展到多核心，需处理多源IFT复杂度。

## 结论

Isadora能自动生成硬件信息流安全属性，其特征与设计者手动属性和CWE对齐，可应用于SoC和CPU，减少安全验证的手动开销。

## 局限性

依赖测试台覆盖，测试台不完整可能导致漏报；假阳性率约10%（功能属性误标为安全）；仅支持单时钟延迟的时序（2周期窗口）；初始化期间流量条件不精确。

## 详细阅读分析

建议精读第3节方法论（IFT与Daikon结合）、第5节评估（CWE映射和采样分析）、第6节局限（轨迹依赖和假阳性）。

## 后续核验问题

- Isadora能否应用于多核心RISC-V处理器，处理跨核信息流？
- 如何量化测试台覆盖对Isadora生成属性质量的影响？
- Isadora能否与硬件Fuzzing工具（如RTL-ConTest）结合，迭代提升覆盖？
- 如何减少Isadora生成的假阳性属性（如功能属性误标为安全）？
