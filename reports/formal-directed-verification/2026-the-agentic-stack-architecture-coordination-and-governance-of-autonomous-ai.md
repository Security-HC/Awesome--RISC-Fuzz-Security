# The Agentic Stack Architecture, Coordination, and Governance of Autonomous AI

## 基本信息

- 作者：Kameshwar Singh
- 发表日期：2026-09-19
- 会议/期刊：未记录
- 主分类：形式化与定向处理器验证
- 相关性：B·强邻近（score=5）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: rtl；verification/fuzzing method: verification；security relevance: security
- 论文页面：[https://doi.org/10.70593/978-81-6632-064-4](https://doi.org/10.70593/978-81-6632-064-4)
- PDF：[https://deepscienceresearch.com/dsr/catalog/download/854/3719/6372](https://deepscienceresearch.com/dsr/catalog/download/854/3719/6372)
- 分析模式：摘要级占位（未全文核验）

## 摘要

An AI demonstration can make a difficult task look effortless. A system receives a request, finds information, chooses a tool, and returns a convincing result. The harder questions appear when that same system is allowed to work inside an organisation. What may it change? Which information should it trust? Who can interrupt it? And what happens when a plausible decision turns out to be wrong? This book begins with those questions. The move from chatbots to agents changes what we need to understand about artificial intelligence. A response can be read and questioned before anyone acts on it. An agent may act while the work is still unfolding, using tools, credentials, and information gathered along the way. Its usefulness therefore depends on the conditions under which it operates, as well as on the capability of the model at its centre. The purpose of this book is to help readers examine those conditions carefully. It follows the agentic stack from reasoning and context through action, protocols, and orchestration, then considers reliability, evaluation, security, human oversight, and governance. The closing discussion looks at what agent-mediated work could mean for enterprise software and commercial strategy. Throughout, the concern is practical: how to turn an appealing capability into a system whose authority, behaviour, and consequences can be understood. A recurring idea is that responsibility must take a form people can test. An approval step needs to give a reviewer enough information and time to intervene. A permission boundary needs to hold when instructions conflict. A recovery plan needs to work after an action has already changed something. These details connect engineering decisions with the everyday responsibilities of the people who build, purchase, manage, and supervise such systems. The book is intended for engineers, architects, security professionals, technology leaders, and readers working in risk or governance. Researchers and students may also find its distinctions useful when examining claims about autonomy. Readers can follow the chapters in sequence to build a connected understanding, or use the role-based reading guidance in Chapter 1 to begin with the questions closest to their work. The examples, tables, and review checklists are meant to support discussion and careful judgement. This is a field in which particular models, tools, and standards will continue to change. The frameworks presented here should be read as aids to analysis and implementation, with attention to the evidence and limitations discussed in each chapter. They invite readers to ask what a system can demonstrate under realistic conditions and what still requires verification. My hope is that this book helps readers make more considered decisions about where agents belong, how much authority they should receive, and what evidence is needed before that authority grows. Dependable agentic systems require patient work on boundaries, failures, and accountability. That work deserves as much attention as the demonstration that first captures our interest.

## 研究问题

摘要级初步判断（未核验正文）：An AI demonstration can make a difficult task look effortless. A system receives a request, finds information, chooses a tool, and returns a convincing result. The harder questions appear when that same system is allowed to work inside an organisation. What may it change? Which information should it trust? Who can interrupt it? And what happens when a plausible decision turns out to be wrong? This book begins with those questions. The move from chatbots to agents changes what we need to understand about artificial intelligence. A response can be read and questioned before anyone acts on it. An agent may act while the work is still unfolding, using tools, credentials, and information gathered along the way. Its usefulness therefore depends on the conditions under which it operates, as well as on the capability of the model at its centre. The purpose of this book is to help readers examine those conditions carefully. It follows the agentic stack from reasoning and context through action, protocols, and orchestration, then considers reliability, evaluation, security, human oversight, and governance. The closing discussion looks at what agent-mediated work could mean for enterprise software and commercial strategy. Throughout, the concern is practical: how to turn an appealing capability into a system whose authority, behaviour, and consequences can be understood. A recurring idea is that responsibility must take a form people can test. An approval step needs to give a reviewer enough information and time to intervene. A permission boundary needs to hold when instructions conflict. A recovery plan needs to work after an action has already changed something. These details connect engineering decisions with the everyday responsibilities of the people who build, purchase, manage, and supervise such systems. The book is intended for engineers, architects, security professionals, technology leaders, and readers working in risk or governance. Researchers and students may also find its distinctions useful when examining claims about autonomy. Readers can follow the chapters in sequence to build a connected understanding, or use the role-based reading guidance in Chapter 1 to begin with the questions closest to their work. The examples, tables, and review checklists are meant to support discussion and careful judgement. This is a field in which particular models, tools, and standards will continue to change. The frameworks presented here should be read as aids to analysis and implementation, with attention to the evidence and limitations discussed in each chapter. They invite readers to ask what a system can demonstrate under realistic conditions and what still requires verification. My hope is that this book helps readers make more considered decisions about where agents belong, how much authority they should receive, and what evidence is needed before that authority grows. Dependable agentic systems require patient work on boundaries, failures, and accountability. That work deserves as much attention as the demonstration that first captures our interest.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《The Agentic Stack Architecture, Coordination, and Governance of Autonomous AI》，初步归入“Formal & Directed Processor Verification”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
