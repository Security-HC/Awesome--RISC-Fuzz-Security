# Are your Sites Truly Isolated? Automatically Detecting Logic Bugs in Site Isolation Implementations

## 基本信息

- 作者：Jan Drescher、David Klein、Martin Johns
- 发表日期：2026-01-01
- 会议/期刊：未记录
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: microarchitectural；verification/fuzzing method: fuzz, sanitizer；security relevance: security
- 论文页面：[https://doi.org/10.14722/ndss.2026.240902](https://doi.org/10.14722/ndss.2026.240902)
- PDF：[https://doi.org/10.14722/ndss.2026.240902](https://doi.org/10.14722/ndss.2026.240902)
- 分析模式：摘要级占位（未全文核验）

## 摘要

Site Isolation (SI) is a recent browser security architecture that isolates web applications by site in separate, sandboxed renderer processes to mitigate Spectre and renderer compromises [2].A site is defined as the tuple of scheme (e.g., https) and extended Top-Level Domain plus one subdomain (short eTLD+1, e.g., example.com).The security of Site Isolation relies on process isolation provided by the operating system.It also relies on the security of the privileged browser process.The browser process communicates with all renderer processes via inter-process communication (IPC) to provide them with cross-site networking and communication capabilities.These capabilities are restricted by the sameorigin policy and Cross-Origin Resource Sharing (CORS).The browser process must correctly track the site context of every renderer process and enforce these security policies.Bugs in the site mapping or the policy enforcement lead to Site Isolation bypass vulnerabilities that allow an attacker to execute malicious JavaScript in the context of another site or steal cookies.Site Isolation was rolled out in 2018 in Chrome [2] and in 2021 in Firefox [3].At the moment of writing, Safari developers started implementing Site Isolation.Most Site Isolation bypass bugs discovered since then required the attacker to have compromised the sandboxed renderer process to be exploitable.This produced a relatively high barrier.But assuming that the sandbox is secure and sandbox escapes are impossible, Site Isolation bypasses are the most lucrative attack vector to utilize a renderer compromise.The vendors of Chrome and Firefox rank Site Isolation bypass vulnerabilities in the secondhighest tier of their security bug bounty programs.In contrast to memory corruptions that the Address Sanitizer [4] can detect, detecting semantic bugs such as Site Isolation bypass bugs is hard because they do not produce easily visible crashes [5].To detect these vulnerabilities, we need to infer which process is under the control of the attacker (i.e., processes attacker-provided inputs) and if this process is able to access cross-site data, leading to our first research question:RQ1 How can SI bypass vulnerabilities (i.e., cross-process data leaks) be reliably detected?Abstract-Site Isolation is one of the core security mechanisms of a modern browser.By confining a spects s uch a s t he JavaScript Just-in-Time compiler or the HTML rendering to a sandboxed process, web browsers significantly r educe t he i mpact o f memory corruption errors.In addition, the mechanism protects against microarchitectural attacks such as Spectre.When using Site Isolation, the browser confines all processing related to a site to its own sandboxed process.All communication with the privileged browser process is done via exchanging IPC messages.This, however, requires the browser process to keep track of which renderer processbelongs to which site, as otherwise, an attacker can abuse a memory corruption issue in the renderer to attack other sites by sending malicious IPC messages.This, in turn, would allow attackers to leak sensitive data, such as cookies, or even achieve Universal Cross-Site Scripting.This work presents the first automatic approach to detect such vulnerabilities, called Site Isolation bypasses, in Firefox and Chrome.For this, we propose a novel oracle to detect the semantic bugs that cause Site Isolation bypass vulnerabilities by flagging cross-site data leaks on the process level.In addition, we design a fuzzer that simulates a compromised renderer process, trying to use the browser process as a confused deputy by hooking into the IPC communication.Our work uncovered four security vulnerabilities in Chrome and Firefox: three less severe bugs leak data cross-site while the fourth bug facilitates complete control over the victim site.

## 研究问题

摘要级初步判断（未核验正文）：Site Isolation (SI) is a recent browser security architecture that isolates web applications by site in separate, sandboxed renderer processes to mitigate Spectre and renderer compromises [2].A site is defined as the tuple of scheme (e.g., https) and extended Top-Level Domain plus one subdomain (short eTLD+1, e.g., example.com).The security of Site Isolation relies on process isolation provided by the operating system.It also relies on the security of the privileged browser process.The browser process communicates with all renderer processes via inter-process communication (IPC) to provide them with cross-site networking and communication capabilities.These capabilities are restricted by the sameorigin policy and Cross-Origin Resource Sharing (CORS).The browser process must correctly track the site context of every renderer process and enforce these security policies.Bugs in the site mapping or the policy enforcement lead to Site Isolation bypass vulnerabilities that allow an attacker to execute malicious JavaScript in the context of another site or steal cookies.Site Isolation was rolled out in 2018 in Chrome [2] and in 2021 in Firefox [3].At the moment of writing, Safari developers started implementing Site Isolation.Most Site Isolation bypass bugs discovered since then required the attacker to have compromised the sandboxed renderer process to be exploitable.This produced a relatively high barrier.But assuming that the sandbox is secure and sandbox escapes are impossible, Site Isolation bypasses are the most lucrative attack vector to utilize a renderer compromise.The vendors of Chrome and Firefox rank Site Isolation bypass vulnerabilities in the secondhighest tier of their security bug bounty programs.In contrast to memory corruptions that the Address Sanitizer [4] can detect, detecting semantic bugs such as Site Isolation bypass bugs is hard because they do not produce easily visible crashes [5].To detect these vulnerabilities, we need to infer which process is under the control of the attacker (i.e., processes attacker-provided inputs) and if this process is able to access cross-site data, leading to our first research question:RQ1 How can SI bypass vulnerabilities (i.e., cross-process data leaks) be reliably detected?Abstract-Site Isolation is one of the core security mechanisms of a modern browser.By confining a spects s uch a s t he JavaScript Just-in-Time compiler or the HTML rendering to a sandboxed process, web browsers significantly r educe t he i mpact o f memory corruption errors.In addition, the mechanism protects against microarchitectural attacks such as Spectre.When using Site Isolation, the browser confines all processing related to a site to its own sandboxed process.All communication with the privileged browser process is done via exchanging IPC messages.This, however, requires the browser process to keep track of which renderer processbelongs to which site, as otherwise, an attacker can abuse a memory corruption issue in the renderer to attack other sites by sending malicious IPC messages.This, in turn, would allow attackers to leak sensitive data, such as cookies, or even achieve Universal Cross-Site Scripting.This work presents the first automatic approach to detect such vulnerabilities, called Site Isolation bypasses, in Firefox and Chrome.For this, we propose a novel oracle to detect the semantic bugs that cause Site Isolation bypass vulnerabilities by flagging cross-site data leaks on the process level.In addition, we design a fuzzer that simulates a compromised renderer process, trying to use the browser process as a confused deputy by hooking into the IPC communication.Our work uncovered four security vulnerabilities in Chrome and Firefox: three less severe bugs leak data cross-site while the fourth bug facilitates complete control over the victim site.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Are your Sites Truly Isolated? Automatically Detecting Logic Bugs in Site Isolation Implementations》，初步归入“Microarchitectural Security Testing”。

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
