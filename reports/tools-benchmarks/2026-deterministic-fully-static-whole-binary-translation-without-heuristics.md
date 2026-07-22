# Deterministic Fully-Static Whole-Binary Translation without Heuristics

## 基本信息

- 作者：Hongyu Chen、James McGowan、Michael Franz
- 发表日期：2026-05-08
- 更新日期：2026-05-13
- 来源：arXiv
- 来源编号：2605.08419v2
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2605.08419v2](http://arxiv.org/abs/2605.08419v2)
- PDF：[https://arxiv.org/pdf/2605.08419v2](https://arxiv.org/pdf/2605.08419v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

We present Elevator, the first binary translator that statically translates entire x86-64 executables to AArch64 without debug information, source code, or assumptions about code layout. Unlike existing systems, which rely on heuristics or runtime fallbacks to handle code-versus-data decoding errors, Elevator considers all possible interpretations of every byte and produces a separate translation for each feasible one ahead of time. Any byte may be interpreted as data, an opcode, or an opcode argument; we generate separate control flow paths for all interpretations, pruning only those leading to abnormal termination. Translations are built by composing code "tiles" automatically derived from a high-level description of the source ISA, yielding a nimble translation framework. The approach is deterministic and produces complete, self-contained binaries with no runtime component in the trusted code base. The principal cost is substantial code size expansion. The key benefit is that the output is the actual code that will run, enabling testing, validation, certification, and cryptographic signing prior to deployment, reducing risk compared to emulators or JIT compilers. We evaluate Elevator on a diverse corpus of real-world binaries, including the entire SPECint 2006 suite, demonstrating that static full-program binary translation can be both reliable and practical. Elevator achieves performance on par with or better than QEMU's user-mode JIT emulation.

## 研究问题

静态二进制翻译中代码与数据区分的不可判定性导致现有方法依赖启发式或运行时回退机制，无法实现完全静态、确定性的跨ISA翻译，且输出依赖运行时组件，难以在部署前进行测试、验证和认证。

## Introduction 梳理

硬件ISA过渡需迁移遗留软件，但源码可能不可得或无法复现原始二进制；现有静态二进制翻译因代码/数据区分等价于停机问题而依赖启发式，动态翻译则覆盖不完整且输出非确定性。Elevator通过超集反汇编，为每个字节的所有可行解释生成独立控制流路径，前置构建所有翻译，输出自包含二进制，无需运行时组件，从而支持部署前全面验证。

## 方法

离线阶段：将每条x64指令语义表达为C函数，针对每种寄存器/操作数组合特化，通过LLVM编译成AArch64代码瓷砖，构建可复用的瓷砖库。在线阶段：对输入二进制执行超集反汇编，从每个可执行字节偏移开始，考虑所有可能的指令起始点，构建超集控制流图；为每个候选指令在瓷砖库中查找对应瓷砖并拼接，同时嵌入地址查找表（从原始指令地址到翻译代码地址）。最后打包阶段：将翻译代码、原始二进制、查找表及运行时驱动程序链接为自包含的AArch64可执行文件。关键设计：全状态保存（一对一寄存器映射）、指令级隔离、无需启发式决策。

## 实验与评估

在包含整个SPECint 2006套件及手工构造的病理样例（如重叠指令、计算间接分支）的语料上评估。结果表明Elevator能正确翻译所有程序，性能与QEMU用户态JIT仿真相当或更优（SPECint 2006平均运行时间比QEMU快约5%）。代码膨胀为主要代价：翻译后二进制大小平均为原始x86-64二进制的10.3倍。

## 结论

Elevator是首个完全静态、确定性、无启发式的跨ISA（x86-64到AArch64）二进制翻译器。它消除了运行时组件，使输出二进制可直接部署前测试、验证、认证和签名。方法可靠且实用，性能可接受，主要代价是代码膨胀，但在高可靠性场景中可接受。

## 局限性

1. 显著的代码膨胀（约10倍），可能限制在存储敏感场景的应用。2. 仅支持x86-64输入到AArch64输出，扩展至其他ISA需重建瓷砖库。3. 未处理自修改代码、多线程、异常处理等复杂运行时行为。4. 地址查找表对间接分支的转发引入微小性能开销。5. 评估仅限SPECint 2006，未测试大型服务器或图形应用。

## 详细阅读分析

论文核心创新是将超集反汇编（先前仅用于二进制重写）首次应用于静态二进制翻译，通过不区分代码/数据而生成所有可能路径的翻译，从根本上避免了启发式错误。瓷砖库的离线构建利用LLVM简化工程，但瓷砖的C函数表达依赖于对x64指令语义的精确建模（包括对部分寄存器写、标志位修改的模拟）。预处理阶段通过一次离线编译生成所有瓷砖，使得在线阶段仅需查表和拼接，从而高效。性能收益来自于全静态翻译消除了动态检查和缓存，但代价是代码膨胀。论文未讨论多线程同步、信号处理等，可能在这些场景中需要额外机制。

## 后续跟进问题

- 如何通过代码压缩或二进制差分技术减少Elevator的代码膨胀？
- 能否将Elevator方法扩展至自修改代码或动态代码生成场景？
- 与Apple Rosetta 2等混合翻译方法相比，Elevator在安全性和性能上具体优劣如何？
- 瓷砖库能否由高层ISA规范自动生成，以支持更多源和目标ISA？
- 是否需要添加运行时支持以处理多线程程序中的原子指令和内存模型差异？
