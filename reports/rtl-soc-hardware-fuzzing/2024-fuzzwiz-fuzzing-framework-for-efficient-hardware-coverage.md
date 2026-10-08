# FuzzWiz -- Fuzzing Framework for Efficient Hardware Coverage

## 基本信息

- 作者：Deepak Narayan Gadde、Aman Kumar、Djones Lettnin、Sebastian Simon
- 发表日期：2024-10-23
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：B·强邻近（score=7）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: rtl, system-on-chip, soc；verification/fuzzing method: fuzz, verification
- 论文页面：[http://arxiv.org/abs/2410.17732v1](http://arxiv.org/abs/2410.17732v1)
- PDF：[https://arxiv.org/pdf/2410.17732v1](https://arxiv.org/pdf/2410.17732v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 5 页，提取 30001 字符

## 摘要

Ever-increasing design complexity of System-on-Chips (SoCs) led to significant verification challenges. Unlike software, bugs in hardware design are vigorous and eternal i.e., once the hardware is fabricated, it cannot be repaired with any patch. Despite being one of the powerful techniques used in verification, the dynamic random approach cannot give confidence to complex Register Transfer Leve (RTL) designs during the pre-silicon design phase. In particular, achieving coverage targets and exposing bugs is a complicated task with random simulations. In this paper, we leverage an existing testing solution available in the software world known as fuzzing and apply it to hardware verification in order to achieve coverage targets in quick time. We created an automated hardware fuzzing framework FuzzWiz using metamodeling and Python to achieve coverage goals faster. It includes parsing the RTL design module, converting it into C/C++ models, creating generic testbench with assertions, fuzzer-specific compilation, linking, and fuzzing. Furthermore, it is configurable and provides the debug flow if any crash is detected during the fuzzing process. The proposed framework is applied on four IP blocks from Google's OpenTitan chip with various fuzzing engines to show its scalability and compatibility. Our benchmarking results show that we could achieve around 90% of the coverage 10 times faster than traditional simulation regression based approach.

## 研究问题

传统随机仿真在复杂RTL设计中达到覆盖率目标和暴露bug方面效率低下，需要自动化硬件fuzzing框架加速验证。

## Introduction 梳理

论文指出设计验证占项目时间60%以上，CRV和CDG方法存在状态空间爆炸、测试生成效果依赖DUV结构等问题。现有硬件fuzzing研究在HDL支持、覆盖反馈和fuzzing引擎方面有局限性。本文贡献是提出自动化硬件fuzzing框架FuzzWiz，支持多种fuzzing引擎，设计无关，并对比了不同引擎在OpenTitan IP上的表现。

## 方法

输入生成：RTL parser提取端口规格，Verilator将RTL转换为C++模型。反馈：硬件行覆盖率（vlt）和软件线/块覆盖率。Oracle：手动添加的SystemVerilog断言（如key_store_debug示例）。DUT：OpenTitan的AES、KMAC、HMAC、RV-Timer IP。平台：软件模型（Verilator转换）fuzzing，使用AFL、AFL++、Fairfuzz、Perffuzz、Tortoisefuzz引擎。无需golden model。

## 实验与评估

Baseline：传统仿真回归（10小时）。实验预算：每个DUV fuzzing 10小时，多次运行。统计：报告了不同引擎的硬件行覆盖率随时间变化的折线图，未报告具体bug数量或CVE。开销：未确认。Artifact：框架代码未公开，使用了开源工具（Verilator, kcov, LLVM）。发现bug示例：key_store_debug的debug_mode=1时断言失败，但未报告在OpenTitan IP上发现的真实bug。

## 核心贡献

1) 提出自动化硬件fuzzing框架FuzzWiz，支持多HDL和多fuzzing引擎；2) 提出MetaFuzz metamodeling代码生成框架；3) 对五种fuzzing引擎在OpenTitan IP上进行基准测试。

## 与本仓库研究主线的关系

直接相关：RTL & SoC Hardware Fuzzing。FuzzWiz关注通用IP block的覆盖率，未涉及多hart/一致性验证，但方法可借鉴用于处理器验证。属于强邻近关系。

## 结论

FuzzWiz框架能更快达到覆盖率目标，Fairfuzz在HMAC和RV-Timer上达到最高硬件行覆盖率约90%，AFL++在AES和KMAC上表现更好且速度更快。RTL仿真比fuzzing慢10倍（基于引用[28][10]）。

## 局限性

1) 依赖软件覆盖率，可能不直接对应硬件覆盖率；2) 未评估实际bug发现能力（仅示例）；3) 断言需手动添加；4) 仅对四个IP实验；5) 未与真实bug检测结果比较。

## 详细阅读分析

重点阅读Section IV（框架细节）和Section V（结果对比），特别是图5的覆盖率增长曲线及Section IV-G的RTL debug流程。

## 后续核验问题

- FuzzWiz如何支持多周期或复杂状态机？是否可扩展至多核或一致性协议？
- 除了硬件行覆盖率，是否支持其他覆盖率（如状态转移）？如何集成？
- 断言是否自动生成？如何保证断言完备性？
- 在OpenTitan IP上实际发现了多少真实bug？
- 框架对大型SoC的扩展性如何？
