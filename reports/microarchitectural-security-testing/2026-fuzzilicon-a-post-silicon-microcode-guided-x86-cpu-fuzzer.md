# Fuzzilicon: A Post-Silicon Microcode-Guided x86 CPU Fuzzer

## 基本信息

- 作者：Johannes Lenzen、Mohamadreza Rostami、Lichao Wu、Ahmad-Reza Sadeghi
- 发表日期：2026-01-01
- 会议/期刊：未记录
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=8）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: processor, cpu, microarchitecture, microarchitectural；verification/fuzzing method: fuzz, coverage-guided, verification, formal verification；security relevance: security, vulnerability
- 论文页面：[https://doi.org/10.14722/ndss.2026.231486](https://doi.org/10.14722/ndss.2026.231486)
- PDF：[https://doi.org/10.14722/ndss.2026.231486](https://doi.org/10.14722/ndss.2026.231486)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 20 页，提取 100000 字符

## 摘要

to faithfully implement their Instruction Set Architectures (ISAs) and enforce strict isolation between processes.However, this assumption has been increasingly challenged by the discovery of critical architectural and microarchitectural-level vulnerabilities [1]- [4].These attacks demonstrate that flaws in CPU microarchitectural can be exploited to leak data, bypass protections, or undermine system integrity, even for secure and well-written software [5].Indeed, modern processors, particularly in the x86 family, are highly complex, with layers of undocumented behavior implemented in proprietary code [6].As designs become increasingly complex and opaque, the risk of hardware-level security flaws continues to grow [7].To detect hardware-level vulnerabilities, researchers have traditionally relied on techniques such as formal verification [8]-[12], runtime detection [13], [14], information flow tracking [15]-[17], and hardware fuzzing [18], [19].Among them, hardware fuzzing has emerged as a promising approach due to its scalability and adaptability to various designs [20]-[41].Hardware fuzzing has evolved into two distinct approaches: pre-silicon fuzzing, which targets Register-Transfer Level (RTL) models during hardware development, and post-silicon fuzzing, which evaluates manufactured processors under real execution conditions [20]-[41].While presilicon fuzzing is widely studied in literature thanks to the deep observability and fine-grained instrumentation within the RTL model [20], [21], [25]-[30], [33], [39]-[41], postsilicon fuzzing is rarely touched.The reason is straightforward: post-silicon fuzzers commonly target black-box or proprietary CPUs (e.g., from Intel and AMD) with visibility limited to architectural registers or crash symptoms [24].Even worse, the internal microarchitectural state and code-level behavior, where many subtle bugs manifest [1], [2], [42], are largely inaccessible and undocumented.Existing hardware feedback mechanisms, such as performance counters or architectural registers, offer only coarse-grained or indirect insight.The lack of transparency and informative feedback prevents the evaluator from finding unexpected behaviors and tracing corresponding root causes.Our Contribution.In this work, we present Fuzzilicon, the first post-silicon fuzzer for proprietary x86 CPUs with gray-Abstract-Modern Central Processing Units (CPUs) are black boxes, proprietary, and increasingly characterized by sophisticated microarchitectural flaws that evade traditional analysis.While some of these critical vulnerabilities have been uncovered through cumbersome manual effort, building an automated and systematic vulnerability detection framework for real-world postsilicon processors remains a challenge.In this paper, we present Fuzzilicon, the first post-silicon fuzzing framework for real-world x86 CPUs that brings deep introspection into the microcode and microarchitectural layers.Fuzzilicon automates the discovery of vulnerabilities that were previously only detectable through extensive manual reverse engineering, and bridges the visibility gap by introducing microcode-level instrumentation.At the core of Fuzzilicon is a novel technique for extracting feedback directly from the processor's microarchitecture, enabled by reverse-engineering Intel's proprietary microcode update interface.We develop a minimally intrusive instrumentation method and integrate it with a hypervisor-based fuzzing harness to enable precise, feedbackguided input generation, without access to Register Transfer Level (RTL) or vendor support.Applied to Intel's Goldmont microarchitecture, Fuzzilicon introduces 5 significant findings, including two previously unknown microcode-level speculative-execution vulnerabilities.Besides, the Fuzzilicon framework automatically rediscover the Spectre class of vulnerabilities, which were detected manually in the previous work.Fuzzilicon reduces coverage collection overhead by up to 31 compared to baseline techniques and achieves 16.27% unique microcode coverage of hookable locations, the first empirical baseline of its kind.As a practical, coverage-guided, and scalable approach to post-silicon fuzzing, Fuzzilicon establishes a new foundation to automate the discovery of complex CPU vulnerabilities.

## 研究问题

后硅阶段的商业x86 CPU由于微架构不透明、缺乏有效反馈和oracle，难以自动化检测微架构级安全漏洞。

## Introduction 梳理

现有硬件漏洞检测方法如形式化验证、运行时检测和预硅fuzzing在后硅场景中受限：后硅CPU为黑盒，可见性仅限于架构寄存器和崩溃症状，内部微码状态不可访问。已有后硅fuzzer如Osiris和SiliFuzz依赖粗粒度反馈或ISA模拟器，无法深入微架构。本文提出Fuzzilicon，首个利用微码级内部反馈的后硅x86 fuzzer，通过逆向Intel微码更新接口实现运行时插桩，无需RTL或厂商支持。

## 方法

输入生成：初始语料为随机字节序列或从软件库提取的有效指令，通过自定义遗传算法和Havoc变异器进行变异。反馈/覆盖率：微码级覆盖率，通过注入微码钩子记录每个可挂钩微码地址的执行次数。Oracle：序列化Oracle，对每个测试用例生成语义等价的序列化变体（插入fence指令抑制推测），比较两者架构状态差异以检测漏洞。DUT/平台：Intel Goldmont N3350 CPU，运行在Fuzzilicon自研的裸机型Type-1 hypervisor中，提供隔离和确定性执行。是否需要golden model：不需要，采用差分测试。

## 实验与评估

Baseline：无覆盖率引导的随机fuzzer（随机语料无反馈）。实验预算：48小时，至少3次重复。统计：最终覆盖2,867个唯一微码地址（占可挂钩地址的16.27%）；相比baseline，达到相同覆盖速度平均快8倍，覆盖率收集开销降低31倍。Bug/CVE：发现5个重要发现，包括2个此前未知的微码级推测执行漏洞（F2,F3），自动重现µSpectre漏洞（F1），以及3个其他发现。开销：单次执行总开销18.274ms（vs baseline 566.490ms）。Artifact：开源于https://github.com/0xCCF4/ufuzz和Zenodo（DOI:10.5281/zenodo.17012971）。

## 核心贡献

1. 首个后硅x86 CPU fuzzer利用微码内部反馈。2. 提出微码覆盖率作为细粒度fuzzing引导信号。3. 优化微码插桩策略，将开销降低31倍。4. 设计序列化Oracle实现无需参考模型的漏洞检测。5. 发现5个重要微码级安全发现（含2个新漏洞）。6. 提供完整的开源框架。

## 与本仓库研究主线的关系

直接相关于“微架构安全自动测试”类别。方法（微码级覆盖率、序列化Oracle、hypervisor隔离）对处理器fuzzing有重要借鉴意义。虽不涉及多hart/内存一致性，但微码级推测执行漏洞可能与一致性路径相关（如跨hart推测影响）。属于强邻近，技术可迁移至RISC-V的微架构fuzzing。

## 结论

Fuzzilicon是首个后硅x86 CPU fuzzer，通过微码级反馈实现了对商业处理器内部微架构的深度探索，有效发现了微码级推测执行漏洞，建立了后硅fuzzing的新基础。

## 局限性

仅适用于Intel Goldmont微架构，且需处理器处于Red-unlocked模式（需逆向工程）；当前不支持AMD或其他厂商CPU；微码插桩依赖对特定微架构逆向知识的完整性和正确性；序列化Oracle对自修改代码和动态跳转处理存在限制。

## 详细阅读分析

建议重点阅读第四节（设计）中的微码覆盖率度量（IV-B）、超视距隔离执行（IV-D）和序列化Oracle（IV-E）；第五节（实现）中的微码插桩（V-B）和覆盖收集优化（V-C）；以及第六节（评估）中的漏洞发现（VI-A、VI-B）和覆盖分析（VI-C）。

## 后续核验问题

- 1. Fuzzilicon的微码插桩技术能否适配开源RISC-V处理器（如使用可编程微码或自定义指令）？2. 序列化Oracle在其他架构（如ARM）上是否有效？3. 所发现的微码推测漏洞是否可能引起跨hart或内存一致性违规？4. 如何将微码覆盖率与多hart场景结合？
