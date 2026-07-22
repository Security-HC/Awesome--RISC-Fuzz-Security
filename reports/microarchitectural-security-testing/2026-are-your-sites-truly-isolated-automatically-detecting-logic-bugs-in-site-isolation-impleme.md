# Are your Sites Truly Isolated? Automatically Detecting Logic Bugs in Site Isolation Implementations

## 基本信息

- 作者：Jan Drescher、David Klein、Martin Johns
- 发表日期：2026-01-01
- 会议/期刊：未记录
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: microarchitectural；verification/fuzzing method: fuzz, sanitizer；security relevance: security
- 论文页面：[https://doi.org/10.14722/ndss.2026.240902](https://doi.org/10.14722/ndss.2026.240902)
- PDF：[https://doi.org/10.14722/ndss.2026.240902](https://doi.org/10.14722/ndss.2026.240902)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 18 页，提取 97603 字符

## 摘要

Site Isolation (SI) is a recent browser security architecture that isolates web applications by site in separate, sandboxed renderer processes to mitigate Spectre and renderer compromises [2].A site is defined as the tuple of scheme (e.g., https) and extended Top-Level Domain plus one subdomain (short eTLD+1, e.g., example.com).The security of Site Isolation relies on process isolation provided by the operating system.It also relies on the security of the privileged browser process.The browser process communicates with all renderer processes via inter-process communication (IPC) to provide them with cross-site networking and communication capabilities.These capabilities are restricted by the sameorigin policy and Cross-Origin Resource Sharing (CORS).The browser process must correctly track the site context of every renderer process and enforce these security policies.Bugs in the site mapping or the policy enforcement lead to Site Isolation bypass vulnerabilities that allow an attacker to execute malicious JavaScript in the context of another site or steal cookies.Site Isolation was rolled out in 2018 in Chrome [2] and in 2021 in Firefox [3].At the moment of writing, Safari developers started implementing Site Isolation.Most Site Isolation bypass bugs discovered since then required the attacker to have compromised the sandboxed renderer process to be exploitable.This produced a relatively high barrier.But assuming that the sandbox is secure and sandbox escapes are impossible, Site Isolation bypasses are the most lucrative attack vector to utilize a renderer compromise.The vendors of Chrome and Firefox rank Site Isolation bypass vulnerabilities in the secondhighest tier of their security bug bounty programs.In contrast to memory corruptions that the Address Sanitizer [4] can detect, detecting semantic bugs such as Site Isolation bypass bugs is hard because they do not produce easily visible crashes [5].To detect these vulnerabilities, we need to infer which process is under the control of the attacker (i.e., processes attacker-provided inputs) and if this process is able to access cross-site data, leading to our first research question:RQ1 How can SI bypass vulnerabilities (i.e., cross-process data leaks) be reliably detected?Abstract-Site Isolation is one of the core security mechanisms of a modern browser.By confining a spects s uch a s t he JavaScript Just-in-Time compiler or the HTML rendering to a sandboxed process, web browsers significantly r educe t he i mpact o f memory corruption errors.In addition, the mechanism protects against microarchitectural attacks such as Spectre.When using Site Isolation, the browser confines all processing related to a site to its own sandboxed process.All communication with the privileged browser process is done via exchanging IPC messages.This, however, requires the browser process to keep track of which renderer processbelongs to which site, as otherwise, an attacker can abuse a memory corruption issue in the renderer to attack other sites by sending malicious IPC messages.This, in turn, would allow attackers to leak sensitive data, such as cookies, or even achieve Universal Cross-Site Scripting.This work presents the first automatic approach to detect such vulnerabilities, called Site Isolation bypasses, in Firefox and Chrome.For this, we propose a novel oracle to detect the semantic bugs that cause Site Isolation bypass vulnerabilities by flagging cross-site data leaks on the process level.In addition, we design a fuzzer that simulates a compromised renderer process, trying to use the browser process as a confused deputy by hooking into the IPC communication.Our work uncovered four security vulnerabilities in Chrome and Firefox: three less severe bugs leak data cross-site while the fourth bug facilitates complete control over the victim site.

## 研究问题

自动检测浏览器Site Isolation实现中的逻辑漏洞（绕过漏洞），这些漏洞允许跨站点数据泄露。

## Introduction 梳理

现有方法如Address Sanitizer无法检测语义漏洞（非崩溃），且Site Isolation绕过漏洞需要触发复杂条件。本文提出第一个自动化方案，包括基于Web IDL的生成器、IPC消息突变模拟渲染器被攻破、两种检测器（leak sanitizer和process sanitizer），并在Chrome和Firefox中发现新漏洞。

## 方法

输入生成：基于Web IDL的JavaScript生成器，生成跨站点交互的HTML文档。反馈/coverage：使用LLVM trace-pc-guards测量边覆盖率，但不作为引导（未声称覆盖引导）。Oracle：leak sanitizer（检测跨进程数据泄露）和process sanitizer（检测进程重用）。DUT/平台：Chrome和Firefox（修补版本）。是否需要golden model：不需要，因为生成器已知每个文档的正确站点，用于对比。

## 实验与评估

baseline：对比Fuzzorigin（UXSS fuzzer）在覆盖率和bug发现上的表现。实验预算：24小时覆盖率实验，一个月（两周各）fuzzing campaign，50个并行实例。统计：覆盖率百分比（图7），语义有效性（Chrome 89.5%，Firefox 85.3%），已知漏洞复现时间（CVE-2019-5856 <1分钟，CVE-2018-18345 ~14分钟，CVE-2022-1637 ~11.4小时）。bug/CVE：共4个，包括CVE-2024-9392以及三个其他漏洞。开销：渲染器杀死导致重新启动影响性能；修复渲染器杀死导致假阳性。Artifact：代码在GitHub（https://github.com/si-bypass-fuzzing）。

## 核心贡献

1. 首次对已知Site Isolation绕过漏洞进行系统分析和分类。2. 实现了Web IDL驱动的fuzzer，模拟渲染器被攻破。3. 提出两种新检测器（leak sanitizer, process sanitizer）。4. 月级fuzzing发现4个漏洞，包括CVE-2024-9392。

## 与本仓库研究主线的关系

方法借鉴：该论文关于浏览器安全测试，但其方法论（模糊测试、Oracle设计、IPC突变）与微架构安全自动测试相关。与多hart/一致性路径研究无直接关系。

## 结论

作者总结了基于对已知漏洞分类的分析，设计了模拟被攻破渲染器的fuzzer，并成功发现了新漏洞，证明了有效性。

## 局限性

渲染器杀死影响性能；不能创建随机IPC消息（需要IPC突变引擎）；WebKit/Safari无法测试（Webdriver不支持）；调试断言不利于检测。

## 详细阅读分析

推荐重点阅读：Section III（漏洞分析和分类），Section IV（Fuzzer设计），Section VI（评估）。尤其是IPC突变策略和两种Oracle的设计。

## 后续核验问题

- 1. 该fuzzer能否扩展到检测其他类似逻辑漏洞（如跨源策略）？2. 渲染器杀死导致的性能开销能否通过更精细的突变策略降低？3. 如何将类似方法应用到RISC-V处理器一致性验证中的消息突变？
