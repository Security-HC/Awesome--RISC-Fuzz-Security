# TaintFuzzer: SoC Security Verification using Taint Inference-enabled Fuzzing

## 基本信息

- 作者：Muhammad Monir Hossain、Nusrat Farzana Dipu、K. Z. Azar、Fahim Rahman、Farimah Farahmandi、M. Tehranipoor
- 发表日期：2023-10-28
- 会议/期刊：2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD)
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：RISC-V Processor Fuzzing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, system-on-chip, soc；verification/fuzzing method: fuzz, verification, information flow tracking；security relevance: security, vulnerability
- 论文页面：[https://doi.org/10.1109/ICCAD57390.2023.10323726](https://doi.org/10.1109/ICCAD57390.2023.10323726)
- PDF：未记录
- 分析模式：摘要级占位（未全文核验）

## 摘要

Modern System-on-Chip (SoC) designs containing sensitive information have become targets of malicious attacks. Unfortunately, current verification practices still undermine the importance of SoCs security verification due to extreme time-to-market constraints, lack of autonomous methodologies, and low coverage. This results in SoC designs moving forward to production with security holes, making them insecure and exploitable by adversaries. Traditional taint analysis and formal approaches are losing applicability to industrial applications due to labor-intensive, slow, and scalability issues. Some approaches apply fuzz testing for hardware vulnerability detection using state-of-the-art software fuzzers, also utilizing information flow tracking for better coverage. However, these approaches prove to be inefficient and cannot be applied to SoCs integrated with third-party IPs (3PIP) for several reasons: laborious white-box-based taint analysis, inconsiderate cross-layer co-verification, and lacking hardware-centric input mutations. This paper proposes Taintuzzer, a fuzzing-driven automated SoC security verification framework leveraging taint inference (feasible in gray-box verification) for detecting SoC security vulnerabilities. Unlike previous studies relying on traditional (code) coverage-related metrics, in TaintFuzzer, we develop (i) schemes for generating smart seeds, (ii) a security-oriented cost function, and (iii) run-time feedback for the mutation engine to choose the appropriate strategies to mutate stimuli targeting SoC modules. TaintFuzzer is powered by FPGA emulation of SoC, making it extremely fast and scalable, especially for cross-layer co-verification. TaintFuzzer's cost function and feedback enable dynamic tuning of mutation strategies to generate hardware-centric inputs. Our experiments with RISC-V-based SoC demonstrate the TaintFuzzer's effectiveness in detecting both known and unknown vulnerabilities in significantlv less time.

## 研究问题

摘要级初步判断（未核验正文）：Modern System-on-Chip (SoC) designs containing sensitive information have become targets of malicious attacks. Unfortunately, current verification practices still undermine the importance of SoCs security verification due to extreme time-to-market constraints, lack of autonomous methodologies, and low coverage. This results in SoC designs moving forward to production with security holes, making them insecure and exploitable by adversaries. Traditional taint analysis and formal approaches are losing applicability to industrial applications due to labor-intensive, slow, and scalability issues. Some approaches apply fuzz testing for hardware vulnerability detection using state-of-the-art software fuzzers, also utilizing information flow tracking for better coverage. However, these approaches prove to be inefficient and cannot be applied to SoCs integrated with third-party IPs (3PIP) for several reasons: laborious white-box-based taint analysis, inconsiderate cross-layer co-verification, and lacking hardware-centric input mutations. This paper proposes Taintuzzer, a fuzzing-driven automated SoC security verification framework leveraging taint inference (feasible in gray-box verification) for detecting SoC security vulnerabilities. Unlike previous studies relying on traditional (code) coverage-related metrics, in TaintFuzzer, we develop (i) schemes for generating smart seeds, (ii) a security-oriented cost function, and (iii) run-time feedback for the mutation engine to choose the appropriate strategies to mutate stimuli targeting SoC modules. TaintFuzzer is powered by FPGA emulation of SoC, making it extremely fast and scalable, especially for cross-layer co-verification. TaintFuzzer's cost function and feedback enable dynamic tuning of mutation strategies to generate hardware-centric inputs. Our experiments with RISC-V-based SoC demonstrate the TaintFuzzer's effectiveness in detecting both known and unknown vulnerabilities in significantlv less time.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《TaintFuzzer: SoC Security Verification using Taint Inference-enabled Fuzzing》，初步归入“RISC-V Processor Fuzzing”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
