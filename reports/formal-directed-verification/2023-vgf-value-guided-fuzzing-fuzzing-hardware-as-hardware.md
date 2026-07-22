# VGF: Value-Guided Fuzzing -- Fuzzing Hardware as Hardware

## 基本信息

- 作者：Ruochen Dai、Michael Lee、Patrick Hoey、Weimin Fu、Tuba Yavuz、Xiaolong Guo、Shuo Wang、Dean Sullivan、Orlando Arias
- 发表日期：2023-12-11
- 会议/期刊：arXiv
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=7）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Formal & Directed Processor Verification
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: microarchitecture；verification/fuzzing method: fuzz
- 论文页面：[http://arxiv.org/abs/2312.06580v1](http://arxiv.org/abs/2312.06580v1)
- PDF：[https://arxiv.org/pdf/2312.06580v1](https://arxiv.org/pdf/2312.06580v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 20 页，提取 77060 字符

## 摘要

As the complexity of logic designs increase, new avenues for testing digital hardware becomes necessary. Fuzz Testing (fuzzing) has recently received attention as a potential candidate for input vector generation on hardware designs. Using this technique, a fuzzer is used to generate an input to a logic design. Using a simulation engine, the logic design is given the generated stimulus and some metric of feedback is given to the fuzzer to aid in the input mutation. However, much like software fuzzing, hardware fuzzing uses code coverage as a metric to find new possible fuzzing paths. Unfortunately, as we show in this work, this coverage metric falls short of generic on some hardware designs where designers have taken a more direct approach at expressing a particular microarchitecture, or implementation, of the desired hardware. With this work, we introduce a new coverage metric which employs not code coverage, but state coverage internal to a design. By observing changes in signals within the logic circuit under testing, we are able to explore the state space of the design and provide feedback to a fuzzer engine for input generation. Our approach, Value-Guided Fuzzing (VGF), provides a generic metric of coverage which can be applied to any design regardless of its implementation. In this paper, we introduce our state-based VGF metric as well as a sample implementation which can be used with any VPI, DPI, VHPI, or FLI compliant simulator, making it completely HDL agnostic. We demonstrate the generality of VGF and show how our sample implementation is capable of finding bugs considerably faster than previous approaches.

## 研究问题

现有硬件fuzzing方法基于代码覆盖率（如控制流覆盖）在微架构实现（如微码ROM、flattened netlist）中失效，无法捕捉隐式控制流，导致fuzzer退化为随机搜索，需要一种不依赖HDL实现风格的覆盖率度量。

## Introduction 梳理

硬件设计日益复杂，现有硬件fuzzing方法（如HW-Fuzz）依赖控制流引导的代码覆盖率，但在微码ROM、技术库特定HDL风格等实现中，控制流信息无法从HDL到C++的转换中获得，导致覆盖率引导失效。作者提出Value-Guided Fuzzing (VGF)，通过追踪设计内部信号的状态变化来重建控制流等价信息，提供通用且与HDL无关的覆盖率度量。贡献包括：重新审视现有假设、提出状态覆盖率度量、实现VGF框架、通过静态分析自动选择信号、实验证明VGF在多个设计上优于HW-Fuzz。

## 方法

输入生成：使用AFL进行输入变异。反馈/覆盖：追踪用户指定信号的变化，通过压缩函数（如BLAKE2b）将{信号ID, 新值}映射到AFL哈希桶，实现状态覆盖。Oracle：用户提供的断言（类似SystemVerilog断言），触发时报告给AFL作为crash。DUT/平台：HDL设计（Verilog/VHDL），通过cocotb抽象层连接兼容VPI/DPI/VHPI/FLI的模拟器（如Icarus Verilog、VCS），支持同步/异步设计及多时钟域。是否需要golden model：否，基于断言。

## 实验与评估

baseline: HW-Fuzz（基于代码覆盖率的硬件fuzzer）。实验预算：96核服务器，每个设计/配置重复5次取平均，超时24小时。统计：平均执行次数（触发断言所需的输入变异次数）和平均时间（秒）。bug/CVE: 在8个设计（AES128-T100, lock case, lock micro, DAIO, Dekker, Unidec, AES128-T2500, RS232-T600, AE18 core, async fifo）上测试，Unidec超时；VGF在大多数设计上执行次数少于HW-Fuzz，尤其async fifo（多时钟域）VGF可触发而HW-Fuzz不能。开销：VGF时间开销较大（因解释性模拟器Icarus Verilog），VGF fast时间接近或优于HW-Fuzz但无法处理多时钟域；具体开销数值未明确给出。Artifact: 未确认公开代码链接，但描述了实现架构和配置。

## 核心贡献

1) 重新审视硬件fuzzing假设，揭示代码覆盖率在微架构实现中的不足；2) 提出基于信号状态变化的覆盖率度量VGF；3) 实现与HDL和模拟器无关的VGF框架（VGF和VGF fast）；4) 通过静态分析自动选择相关信号和权重；5) 实验证明VGF在多个设计上执行次数少于HW-Fuzz，并能处理多时钟域设计（HW-Fuzz不能）。

## 与本仓库研究主线的关系

直接相关（RTL/SoC硬件Fuzzing）。该方法针对硬件设计的状态空间探索，可应用于处理器核和SoC的fuzzing验证。与多hart/一致性路径研究的关系：可处理多时钟域设计（如async fifo），但未专门针对多hart或内存一致性；其状态覆盖思想可推广到多hart共享状态的一致性验证，但需扩展Oracle和信号选择策略。

## 结论

VGF通过状态覆盖引导fuzzing，比代码覆盖率更通用，能更快找到bug。静态分析可显著提升性能。VGF fast牺牲仿真精度换取速度，但无法处理多时钟域。未来工作包括改进仿真接口。

## 局限性

1) VGF因通过VPI回调追踪信号，模拟速度较慢；2) VGF fast基于Verilator，无法处理多时钟域设计；3) 信号选择依赖静态分析，不相关信号会降低性能；4) Oracle限于用户提供的断言，可能遗漏非断言bug；5) 未对大型设计（如BOOM）进行扩展性测试。

## 详细阅读分析

1) 作者呼吁改进仿真接口以提升VGF速度；2) 信号选择阈值τ的影响：过大引入无关信号，过小丢失相关信号，建议τ∈[min, max/4]；3) 尝试修改AFL适应性函数（如几何均值、桶数），但默认适应性函数在大多数设计中表现更差；4) 压缩函数（压缩值 vs 向量化）对结果无显著影响；5) 裁剪步骤和确定性突变对性能的影响：裁剪有害，确定性突变在输入大时严重降速。

## 后续核验问题

- 1) VGF如何扩展到多hart处理器验证？需要哪些额外信号和Oracle？2) 能否结合硬件形式化方法自动生成断言或选择信号？3) 对于大型设计（如RISC-V BOOM），静态分析的可扩展性如何？4) VGF的覆盖率度量能否与其他硬件fuzzer（如DIFUZZRTL）结合？5) 是否支持时序攻击类fuzzing（如侧信道）？
