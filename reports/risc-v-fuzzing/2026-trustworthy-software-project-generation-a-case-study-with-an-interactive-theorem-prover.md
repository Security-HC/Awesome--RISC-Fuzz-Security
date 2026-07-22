# Trustworthy Software Project Generation : a Case Study with an Interactive Theorem Prover

## 基本信息

- 作者：Jian Fang、Yingfei Xiong
- 发表日期：2026-05-25
- 更新日期：2026-05-25
- 来源：arXiv
- 来源编号：2605.26017v1
- 研究类别：RISC-V Fuzzing 研究、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2605.26017v1](http://arxiv.org/abs/2605.26017v1)
- PDF：[https://arxiv.org/pdf/2605.26017v1](https://arxiv.org/pdf/2605.26017v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

Generating code from natural-language requirements has become a primary route for LLM-assisted software development. Although LLMs can successfully complete small programming tasks, generating an entire complex project remains unreliable because subtle errors may survive compilation and testing. Verified programming can reduce this risk by requiring generated implementations to satisfy machine-checked specifications. Existing explorations mostly target verification-oriented languages and toolchains such as Dafny and Frama-C, but directly generating project-scale verified code with these systems remains difficult. This paper studies whether interactive theorem provers (ITPs) can support large-scale software generation. Because ITPs handle pure total functions but not effects such as I/O, our agent separates effectful code from pure logic: it implements the effects in the target language, proves the pure logic in an ITP, and extracts it for integration into the final project. We study this route through the fully automatic development of a CPU interpreter for all 47 instructions of the unprivileged RISC-V RV32I base: after the requirements are supplied, no human intervenes in synthesis, proof repair, extraction, or integration. With Rocq as the backend, the agent completes the project within 30 minutes, producing 1,859 lines of verified Rocq and extracting 2,848 lines of C++. The resulting interpreter passes all 265 LLM-generated tests covering the 47 instructions and exhibits zero crashes and zero hangs during 12 hours of AFL++ fuzzing. Under the same configuration, a Dafny-based backend fails to complete verification. Our observation is that Rocq exposes a concrete proof state when a proof attempt fails, giving the agent actionable feedback for repair. These results provide empirical evidence that ITP-based verified programming is a feasible route for LLM-generated software projects.

## 研究问题

研究如何利用交互式定理证明器（ITP）支持LLM代理自动生成具有机器验证核心的完整软件项目，克服直接使用Dafny等验证语言时由于失败反馈不充分导致的困难。

## Introduction 梳理

LLM辅助软件开发中，生成完整复杂项目常因代码编译测试通过但仍违背语义而不可信。验证编程要求实现满足形式化规范，但现有探索如Dafny在代理驱动下难以完成项目级验证，因为自动化验证失败仅提供有限调试信息。本文研究ITP作为后端是否可行，因为ITP（如Rocq）在证明失败时暴露具体证明状态，提供可操作修复反馈。通过一个完全自动开发RISC-V RV32I CPU解释器的案例，代理在30分钟内完成，生成1859行Rocq验证代码并提取2848行C++，所有265个LLM生成测试通过，12小时AFL++模糊测试零崩溃零挂起。这是已知最大的完全自动开发的可运行验证核心软件项目。贡献包括：最大自动验证项目、分离纯核心与副作用的工作流、Rocq与Dafny的对比实验。

## 方法

提出SPDDWL工作流，参数化ITP后端，实例化为Rocq。分为三阶段：1) 需求分析：LLM代理将自然语言需求转化为编程计划，明确类型定义、纯功能函数、逻辑规范（函数级和全局级）以及副作用分离；2) 合成与验证：编码代理生成Rocq纯函数定义，证明代理生成规范和战术证明，Rocq检查失败时返回证明状态和诊断信息供代理修复；3) 组合与提取：将验证过的处理程序组合成step函数，证明全局性质，然后通过提取工具（如Crane）导出C++代码，与实现副作用的宿主层链接。提取正确性假设成立。

## 实验与评估

以RISC-V RV32I全部47条指令的CPU解释器为测试任务，使用Claude Opus 4.7和Rocq 9.0.1后端。在30分钟自动运行中，代理合成1859行验证Rocq代码，提取2848行C++代码。265个LLM生成的指令测试全部通过；12小时AFL++模糊测试执行9820万输入，零崩溃零挂起。对比实验：相同配置下Dafny后端在30分钟内未能完成验证，观察认为Rocq的显式证明状态提供了更有效的修复信号。

## 结论

ITP为基础的验证编程是LLM生成软件项目的可行路线，案例提供了经验证据。Rocq的证明状态反馈是代理驱动开发中的优势属性。

## 局限性

1) 验证保证仅覆盖纯核心部分，宿主代码（I/O、运行时集成）通过动态测试而非形式化验证；2) 假设提取工具正确保留语义，未验证提取后代码与Rocq定义的等价性；3) 需求分析需要用户交互澄清表示选择，可能限制全自动化程度；4) 实验仅针对RISC-V RV32I子集，规模有限；5) 仅与Dafny进行一次30分钟对比，未控制变量如超时策略；6) 仅使用LLM生成测试和AFL++，未评估形式化规范本身的完整性。

## 详细阅读分析

论文创新在于利用ITP的显式证明状态作为LLM代理的修复反馈，相较于Dafny等黑盒验证器，这种细粒度反馈显著提升了自动修复效率。分离纯核心与副作用的设计使ITP能处理实际软件中的效果问题，通过提取将验证价值扩展到宿主语言。与主流验证语言Dafny的对比突出了反馈粒度的重要性，但Dafny的失败可能受限于其基于SMT的自动化策略对不完整程序缺乏指导。此外，工作流依赖于预先设计好的分离策略，对于更复杂的项目（如包含I/O、并发）可能需要更精细的模型。未来的研究方向包括自动化更细粒度的分离、扩展到其他ITP（如Lean）、以及评估提取可信度。

## 后续跟进问题

- 如何自动化地将复杂项目中的副作用与纯逻辑分离？是否可能通过类型系统或静态分析辅助？
- 该工作流能否扩展到其他领域，例如生成操作系统内核或网络协议栈？
- Rocq的证明状态反馈在代理修复中具体起到多大作用？能否量化为修复轮次减少或成功率提升？
- 与其他ITP（如Lean、Isabelle）相比，Rocq的反馈机制是否同样有效？
- 提取工具的可靠性如何？能否对提取结果进行二次验证以增强可信度？
- Dafny失败的根本原因是代理能力不足还是工具本身限制？是否可通过调整提示或增加时间改善？
- fuzzing测试的覆盖率如何？是否针对所有指令路径进行了充分测试？
- 该工作流能否与增量验证或持续集成结合，实现自动维护验证代码？
