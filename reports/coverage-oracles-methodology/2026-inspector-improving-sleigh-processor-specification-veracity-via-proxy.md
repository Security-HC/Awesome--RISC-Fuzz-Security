# InSPECtor: Improving SLEIGH Processor Specification Veracity via Proxy

## 基本信息

- 作者：Michael Chesser、Paul Quirk、Douglas Cooke、Guy Farrelly、Surya Nepal、Damith C. Ranasinghe
- 发表日期：2026-08-13
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, processor；verification/fuzzing method: validation；security relevance: security
- 论文页面：[http://arxiv.org/abs/2608.13042v2](http://arxiv.org/abs/2608.13042v2)
- PDF：[https://arxiv.org/pdf/2608.13042v2](https://arxiv.org/pdf/2608.13042v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 30 页，提取 100000 字符

## 摘要

Processor specifications underpin critical security and program- analysis tools such as disassemblers, decompilers, and emulators, yet, their correctness is rarely examined. Errors in specifications distort program behaviour, obscure vulnerabilities, and enable analysis-evasion techniques. Validating processor specifications is a non-trivial task. Our study is a significant undertaking to enable, for the first time, the systematic validation of open-source SLEIGH language specifications, predominantly used by Ghidra. We design and implement a testing framework based on an automated oracle validation strategy by proxy. Our approach leverages the structure encoded in a specification itself to enumerate decodable instruction forms and generate targeted initial states. Then differentially test the successful decoding and emulation of those instructions by comparing emulators exercising the processor specification against hardware references. Applying InSPECtor across diverse, open-source specifications---x86-64, AArch64, ARM/Thumb, RISC-V, MSP430---embedding differences in specification styles, author preferences, and instruction set architecture designs, we uncovered over 38,920 discrepancies that led to 125 unique bugs with proposed fixes, identifying decoding and semantic defects as well as cross-vendor inconsistencies. We distill our findings into 8 concrete recommendations to drive future improvements. Our work underscores the importance of specification correctness and provides a practical tool to substantially improve the fidelity of SLEIGH processor specifications, strengthening the reliability of downstream security and analysis tools.

## 研究问题

SLEIGH 处理器规格验证缺失，存在解码和语义错误，影响 Ghidra 等安全工具。

## Introduction 梳理

现有研究关注 CPU 模拟器、虚拟化、处理器硬件或二进制 lifters，但 SLEIGH 规格的正确性未被系统性验证。SLEIGH 规格支撑 Ghidra 等关键安全工具，其错误会传播到下游分析。研究空白是缺少对 SLEIGH 规格的系统性测试方法。本文首次提出基于代理的自动化 oracle 验证框架，通过枚举规格中的指令结构和生成定向初始状态来揭示规格缺陷。贡献是设计并实现 InSPECtor，发现大量缺陷和 bug，提出改进建议。

## 方法

输入生成：使用 GenSYS 符号遍历 SLEIGH 解码规则，将构造器约束编码为 SMT 约束，求解具体指令编码；生成代表性操作数值（最小/最大、简单随机、强制别名）。反馈/coverage：构造器覆盖率，作为指标；通过求解约束生成指令。Oracle：代理策略——使用 SLEIGH 模拟器（Icicle）与硬件参考（KVM 或调试器）进行差分测试；硬件作为 oracle。DUT/平台：x86-64, AArch64, ARM/Thumb, RISC-V, MSP430 的 Ghidra SLEIGH 规格；硬件参考包括 KVM VM 和 MSP430FR5969, BeagleV-Ahead (RISC-V)。是否需要 golden model：不需要，使用硬件作为真实参考。

## 实验与评估

baseline：简单随机生成（naive approach）在 x86-64 上进行对比。实验预算：生成时间各架构不同，如 x86-64 总计约 1937 秒；测试执行速度差异大；未报告总执行时间。统计：报告通过分组后的 38,920 组差异，125 个 unique bugs；手动分析约每 bug 4 小时。bug/CVE：125 个 unique bugs，分解码、语义排序、错误语义、别名等，无 CVE 报告。开销：生成时间、测试时间、分析时间。Artifact：开源 GitHub https://github.com/Sleigh-InSPECtor/。其他结果：构造器覆盖率 90%-99%；ablation 显示禁用约束翻译导致准确性大幅下降。

## 核心贡献

设计符号遍历 SLEIGH 解码规则生成指令和初始状态的框架；实现原型 InSPECtor（GenSYS + JuxtaPlayer）；在五个不同 ISA 上发现 125 个 unique bugs 并提出修复；基于根因分析给出 8 条 SLEIGH DSL 改进建议。

## 与本仓库研究主线的关系

直接相关：该工作针对处理器规格验证，使用差分测试和硬件 oracle，与 RISC-V 处理器 fuzzing 和微架构安全测试强相关。与多 hart/一致性路径关系不直接：本文只测试单指令单 hart 行为，未涉及多 hart 或内存一致性；但其生成指令和状态的方法可用于后续多 hart 测试。属于强邻近方法借鉴。

## 结论

InSPECtor 首个系统性验证 SLEIGH 规格的框架，在五个 ISA 上发现大量规格错误，证明规格驱动方法有效，并提出 8 条语言改进建议。作者强调规格正确性对安全工具的重要性，提供实用工具。

## 局限性

无法测试规格缺失的指令（完整性）；单指令测试不覆盖跨指令状态影响（如 ITE 条件执行）；未解决不可预测行为、浮点语义、SIMD 等规格限制；需要人工分析差异；硬件与规格版本差异可能导致部分差异。

## 详细阅读分析

核心创新在于用 SLEIGH 规格本身作为指令生成的结构输入，用 SMT 求解约束，并设计状态生成从 Pcode 操作提取边界条件。差分测试的 oracle 是硬件，避免 golden model。对 RISC-V 测试覆盖了基整数指令，但向量扩展未实现。作者明确区分已实现、占位符和不可修复问题。推荐的语言改进如 SIMD 向量化、浮点舍入模式、对齐信息等，反映当前 SLEIGH 表达局限。

## 后续核验问题

- GenSYS 符号遍历在遇到自引用或高度重叠构造器时如何保证终止和效率？
- 差分测试对异常路径的比较时如何处理硬件实现的差异（例如不同厂商 CPU 的容忍度）？
- 状态生成中边界用例的表驱动方法覆盖了多少 Pcode 操作？是否存在遗漏？
- 这些方法和发现能否扩展到多 hart 并发测试或内存一致性测试？
- 如何自动化 bug 分类以减少人工分析工作量？
