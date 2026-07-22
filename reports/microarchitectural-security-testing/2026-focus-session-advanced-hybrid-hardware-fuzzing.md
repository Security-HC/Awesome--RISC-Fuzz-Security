# Focus Session: Advanced Hybrid Hardware Fuzzing

## 基本信息

- 作者：Chen Chen、Stephen Muttathil、Mohamadreza Rostami、Nikhilesh Singh、Lichao Wu、Ahmad‐Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2026-04-20
- 会议/期刊：未记录
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=10）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：Microarchitectural Security Testing、RTL & SoC Hardware Fuzzing、Formal & Directed Processor Verification
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: processor, microarchitectural, rtl；verification/fuzzing method: fuzz, verification, formal verification；security relevance: security
- 论文页面：[https://doi.org/10.23919/date69613.2026.11539167](https://doi.org/10.23919/date69613.2026.11539167)
- PDF：未记录
- 分析模式：摘要级占位（未全文核验）

## 摘要

Modern processors are increasingly complex, with rich microarchitectural features and heterogeneous components. This complexity expands the attack surface and makes security vulnerabilities harder to detect using traditional security techniques. Hardware fuzzing has emerged as a scalable approach for uncovering insecure behaviors in modern processors. However, it often struggles to (i) explore hard-to-reach design spaces due to its randomness and (ii) locate the root causes of vulnerabilities due to design complexity.This work presents advanced hybrid hardware fuzzing techniques that combine the complementary strengths of fuzzing, formal verification, and static analysis to systematically detect and localize vulnerabilities in processors. Specifically, we investigate (i) the use of formal verification to guide fuzzing toward hard-to-reach design spaces, thereby enabling the discovery of subtle vulnerabilities, and (ii) the use of static analysis to extract and monitor timing behaviors at the register-transfer level (RTL), enabling localization of timing vulnerabilities that can arise even in functionally correct designs.Finally, we outline future research directions, including using large language models to generate expert-informed tests, leveraging prior design knowledge to enhance fuzzing effectiveness on new processors, and transferring effective strategies from white-box fuzzing to black-box fuzzing environments.

## 研究问题

摘要级初步判断（未核验正文）：Modern processors are increasingly complex, with rich microarchitectural features and heterogeneous components. This complexity expands the attack surface and makes security vulnerabilities harder to detect using traditional security techniques. Hardware fuzzing has emerged as a scalable approach for uncovering insecure behaviors in modern processors. However, it often struggles to (i) explore hard-to-reach design spaces due to its randomness and (ii) locate the root causes of vulnerabilities due to design complexity.This work presents advanced hybrid hardware fuzzing techniques that combine the complementary strengths of fuzzing, formal verification, and static analysis to systematically detect and localize vulnerabilities in processors. Specifically, we investigate (i) the use of formal verification to guide fuzzing toward hard-to-reach design spaces, thereby enabling the discovery of subtle vulnerabilities, and (ii) the use of static analysis to extract and monitor timing behaviors at the register-transfer level (RTL), enabling localization of timing vulnerabilities that can arise even in functionally correct designs.Finally, we outline future research directions, including using large language models to generate expert-informed tests, leveraging prior design knowledge to enhance fuzzing effectiveness on new processors, and transferring effective strategies from white-box fuzzing to black-box fuzzing environments.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Focus Session: Advanced Hybrid Hardware Fuzzing》，初步归入“Microarchitectural Security Testing”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
