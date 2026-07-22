# Fuzzilicon: A Post-Silicon Microcode-Guided x86 CPU Fuzzer

## 基本信息

- 作者：Johannes Lenzen、Mohamadreza Rostami、Lichao Wu、Ahmad-Reza Sadeghi
- 发表日期：2026-01-01
- 会议/期刊：未记录
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=8）
- 证据等级：摘要级
- 标签：Microarchitectural Security Testing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: processor, cpu, microarchitecture, microarchitectural；verification/fuzzing method: fuzz, coverage-guided, verification, formal verification；security relevance: security, vulnerability
- 论文页面：[https://doi.org/10.14722/ndss.2026.231486](https://doi.org/10.14722/ndss.2026.231486)
- PDF：[https://doi.org/10.14722/ndss.2026.231486](https://doi.org/10.14722/ndss.2026.231486)
- 分析模式：摘要级占位（未全文核验）

## 摘要

to faithfully implement their Instruction Set Architectures (ISAs) and enforce strict isolation between processes.However, this assumption has been increasingly challenged by the discovery of critical architectural and microarchitectural-level vulnerabilities [1]- [4].These attacks demonstrate that flaws in CPU microarchitectural can be exploited to leak data, bypass protections, or undermine system integrity, even for secure and well-written software [5].Indeed, modern processors, particularly in the x86 family, are highly complex, with layers of undocumented behavior implemented in proprietary code [6].As designs become increasingly complex and opaque, the risk of hardware-level security flaws continues to grow [7].To detect hardware-level vulnerabilities, researchers have traditionally relied on techniques such as formal verification [8]-[12], runtime detection [13], [14], information flow tracking [15]-[17], and hardware fuzzing [18], [19].Among them, hardware fuzzing has emerged as a promising approach due to its scalability and adaptability to various designs [20]-[41].Hardware fuzzing has evolved into two distinct approaches: pre-silicon fuzzing, which targets Register-Transfer Level (RTL) models during hardware development, and post-silicon fuzzing, which evaluates manufactured processors under real execution conditions [20]-[41].While presilicon fuzzing is widely studied in literature thanks to the deep observability and fine-grained instrumentation within the RTL model [20], [21], [25]-[30], [33], [39]-[41], postsilicon fuzzing is rarely touched.The reason is straightforward: post-silicon fuzzers commonly target black-box or proprietary CPUs (e.g., from Intel and AMD) with visibility limited to architectural registers or crash symptoms [24].Even worse, the internal microarchitectural state and code-level behavior, where many subtle bugs manifest [1], [2], [42], are largely inaccessible and undocumented.Existing hardware feedback mechanisms, such as performance counters or architectural registers, offer only coarse-grained or indirect insight.The lack of transparency and informative feedback prevents the evaluator from finding unexpected behaviors and tracing corresponding root causes.Our Contribution.In this work, we present Fuzzilicon, the first post-silicon fuzzer for proprietary x86 CPUs with gray-Abstract-Modern Central Processing Units (CPUs) are black boxes, proprietary, and increasingly characterized by sophisticated microarchitectural flaws that evade traditional analysis.While some of these critical vulnerabilities have been uncovered through cumbersome manual effort, building an automated and systematic vulnerability detection framework for real-world postsilicon processors remains a challenge.In this paper, we present Fuzzilicon, the first post-silicon fuzzing framework for real-world x86 CPUs that brings deep introspection into the microcode and microarchitectural layers.Fuzzilicon automates the discovery of vulnerabilities that were previously only detectable through extensive manual reverse engineering, and bridges the visibility gap by introducing microcode-level instrumentation.At the core of Fuzzilicon is a novel technique for extracting feedback directly from the processor's microarchitecture, enabled by reverse-engineering Intel's proprietary microcode update interface.We develop a minimally intrusive instrumentation method and integrate it with a hypervisor-based fuzzing harness to enable precise, feedbackguided input generation, without access to Register Transfer Level (RTL) or vendor support.Applied to Intel's Goldmont microarchitecture, Fuzzilicon introduces 5 significant findings, including two previously unknown microcode-level speculative-execution vulnerabilities.Besides, the Fuzzilicon framework automatically rediscover the Spectre class of vulnerabilities, which were detected manually in the previous work.Fuzzilicon reduces coverage collection overhead by up to 31 compared to baseline techniques and achieves 16.27% unique microcode coverage of hookable locations, the first empirical baseline of its kind.As a practical, coverage-guided, and scalable approach to post-silicon fuzzing, Fuzzilicon establishes a new foundation to automate the discovery of complex CPU vulnerabilities.

## 研究问题

摘要级初步判断（未核验正文）：to faithfully implement their Instruction Set Architectures (ISAs) and enforce strict isolation between processes.However, this assumption has been increasingly challenged by the discovery of critical architectural and microarchitectural-level vulnerabilities [1]- [4].These attacks demonstrate that flaws in CPU microarchitectural can be exploited to leak data, bypass protections, or undermine system integrity, even for secure and well-written software [5].Indeed, modern processors, particularly in the x86 family, are highly complex, with layers of undocumented behavior implemented in proprietary code [6].As designs become increasingly complex and opaque, the risk of hardware-level security flaws continues to grow [7].To detect hardware-level vulnerabilities, researchers have traditionally relied on techniques such as formal verification [8]-[12], runtime detection [13], [14], information flow tracking [15]-[17], and hardware fuzzing [18], [19].Among them, hardware fuzzing has emerged as a promising approach due to its scalability and adaptability to various designs [20]-[41].Hardware fuzzing has evolved into two distinct approaches: pre-silicon fuzzing, which targets Register-Transfer Level (RTL) models during hardware development, and post-silicon fuzzing, which evaluates manufactured processors under real execution conditions [20]-[41].While presilicon fuzzing is widely studied in literature thanks to the deep observability and fine-grained instrumentation within the RTL model [20], [21], [25]-[30], [33], [39]-[41], postsilicon fuzzing is rarely touched.The reason is straightforward: post-silicon fuzzers commonly target black-box or proprietary CPUs (e.g., from Intel and AMD) with visibility limited to architectural registers or crash symptoms [24].Even worse, the internal microarchitectural state and code-level behavior, where many subtle bugs manifest [1], [2], [42], are largely inaccessible and undocumented.Existing hardware feedback mechanisms, such as performance counters or architectural registers, offer only coarse-grained or indirect insight.The lack of transparency and informative feedback prevents the evaluator from finding unexpected behaviors and tracing corresponding root causes.Our Contribution.In this work, we present Fuzzilicon, the first post-silicon fuzzer for proprietary x86 CPUs with gray-Abstract-Modern Central Processing Units (CPUs) are black boxes, proprietary, and increasingly characterized by sophisticated microarchitectural flaws that evade traditional analysis.While some of these critical vulnerabilities have been uncovered through cumbersome manual effort, building an automated and systematic vulnerability detection framework for real-world postsilicon processors remains a challenge.In this paper, we present Fuzzilicon, the first post-silicon fuzzing framework for real-world x86 CPUs that brings deep introspection into the microcode and microarchitectural layers.Fuzzilicon automates the discovery of vulnerabilities that were previously only detectable through extensive manual reverse engineering, and bridges the visibility gap by introducing microcode-level instrumentation.At the core of Fuzzilicon is a novel technique for extracting feedback directly from the processor's microarchitecture, enabled by reverse-engineering Intel's proprietary microcode update interface.We develop a minimally intrusive instrumentation method and integrate it with a hypervisor-based fuzzing harness to enable precise, feedbackguided input generation, without access to Register Transfer Level (RTL) or vendor support.Applied to Intel's Goldmont microarchitecture, Fuzzilicon introduces 5 significant findings, including two previously unknown microcode-level speculative-execution vulnerabilities.Besides, the Fuzzilicon framework automatically rediscover the Spectre class of vulnerabilities, which were detected manually in the previous work.Fuzzilicon reduces coverage collection overhead by up to 31 compared to baseline techniques and achieves 16.27% unique microcode coverage of hookable locations, the first empirical baseline of its kind.As a practical, coverage-guided, and scalable approach to post-silicon fuzzing, Fuzzilicon establishes a new foundation to automate the discovery of complex CPU vulnerabilities.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Fuzzilicon: A Post-Silicon Microcode-Guided x86 CPU Fuzzer》，初步归入“Microarchitectural Security Testing”。

## 与本仓库研究主线的关系

该条目已通过自动相关性筛选，但尚未完成人工或全文级核验。

## 结论

尚未核验正文，因此不对论文最终结论作确定性概括。

## 局限性

尚未核验正文。至少需要检查方法是否只适用于特定 ISA、处理器、协议、仿真器或人工模板，以及实验是否存在目标泄漏和基线不公平。

## 详细阅读分析

优先阅读 Introduction、Background/Threat Model、Method、Evaluation、Limitations/Discussion，并核对官方论文页、DOI、Artifact 和代码仓库。

## 后续核验问题

- 论文的在线反馈信号和最终 Oracle 分别是什么？
- 实验是否包含公平的 random、通用 RTL coverage 和领域专用 coverage 基线？
- 论文是否提供开源 Artifact、真实漏洞、CVE 或可复现 PoC？
