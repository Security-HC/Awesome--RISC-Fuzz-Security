# Position: AI Security Policy Should Target Systems, Not Models

## 基本信息

- 作者：Michael A. Riegler、Inga Strümke
- 发表日期：2026-05-10
- 更新日期：2026-05-10
- 来源：arXiv
- 来源编号：2605.09504v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2605.09504v1](http://arxiv.org/abs/2605.09504v1)
- PDF：[https://arxiv.org/pdf/2605.09504v1](https://arxiv.org/pdf/2605.09504v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

We present swarm-attack, an open-source adversarial testing framework in which multiple lightweight LLM agents coordinate through shared memory, parallel exploration, and evolutionary optimization. Together, our results demonstrate that both safety bypass of frontier models and software vulnerability discovery, i.e., the capability class that motivated restricted release of Anthropic's Mythos Preview, are achievable at effectively zero cost using commodity hardware and openly available models. We report two experiments. In the first, five instances of a 1.2 billion parameter model conducted 225 jailbreak attacks each against GPT-4o and Claude Sonnet~4. Against GPT-4o, the swarm achieved an Effective Harm Rate of 45.8%, producing 49 critical-severity breaches; against Claude Sonnet-4, the Effective Harm Rate was 0% despite a 40% technical success rate. In the second experiment, the same models performed combined source code analysis and binary fuzzing against a vulnerable C application with 9 planted CWEs. With a hand-crafted exploit seed corpus, regex pattern detection, and AddressSanitizer-based crash classification, the pipeline recovers 9 of 9 vulnerabilities (100% recall) in approximately four minutes on a consumer MacBook. With those scaffold components disabled, the same model recovers 0 of 9 by crash verification and 2 of 9 by citation. The capability class that motivated restricted release of Anthropic's Mythos Preview is therefore reproducible at effectively zero cost; the important enabler is the system scaffold itself, which compensates for the limited reasoning capacity of small individual models.

## 研究问题

AI安全政策是否应聚焦于模型级访问限制，还是系统级能力评估？具体而言，通过开源小模型和系统框架能否复现前沿模型的攻击能力，从而质疑模型限制的有效性。

## Introduction 梳理

Anthropic的Claude Mythos Preview因具备自主发现和利用零日漏洞的能力而限制发布，但作者提出质疑：限制单个模型是否真能降低攻击者的可用能力。通过两个实验证明，使用5个1.2B参数的开源模型组成的协调群体（swarm-attack），在消费级硬件上，即可实现前沿模型的安全绕过和软件漏洞发现，且成本极低。关键能力来自系统框架（scaffold）而非模型本身。

## 方法

实验1：采用5个LFM2.5-1.2B-Thinking模型实例，分配不同攻击策略（指令覆盖、角色扮演、多轮升级、混淆、进化变异），通过共享记忆和进化优化（交叉率0.5，突变率0.3）生成225次攻击，针对GPT-4o和Claude Sonnet 4。采用跨提供商LLM-as-judge评估，并引入有效危害率（EHR）消除假阳性。实验2：针对包含9个CWE（如栈/堆溢出、UAF、命令注入等）的C程序（SwarmApp），分两阶段：阶段1源码分析使用角色分化模型（内存安全、注入、认证逻辑、算术），结合正则检测和LLM引用；阶段2二进制模糊测试使用AddressSanitizer，种子语料库8个，LLM生成突变输入。辅助配置包含所有组件；自主配置禁用人工组件，仅靠LLM生成输入和引用。

## 实验与评估

实验1：GPT-4o技术成功率60.9%，有效危害率45.8%（49个关键严重攻击）；Claude Sonnet 4技术成功率40.0%，有效危害率0%。群体进化使GPT-4o攻击成功率从31.4%提升至66.3%（峰值73%）。实验2：辅助配置下，5×3规模（5个agent×3代）召回8/9，7×3规模召回9/9，运行时间约240秒。自主配置下，crash验证召回0/9，引用验证召回2/9（其中一个CWE分类错误）。9个CWE的差距完全归因于系统框架。

## 结论

AI安全政策应转向系统级能力评估，因为攻击能力主要源于协调框架、共享内存、进化优化等系统级设计，而非模型本身。小模型+精心设计的框架可复现前沿模型的危险能力，且成本极低，模型级访问限制提供的防御窗口比预期窄。

## 局限性

实验只使用了1.2B参数模型，更大模型可能表现不同；漏洞发现目标是人为植入9个CWE的合成应用，真实软件代码可能更复杂；安全评估中LLM-as-judge存在假阳性，虽引入EHR但手动验证有限；系统框架组件（种子语料库、正则模式）需人工设计，自动化程度不足；实验仅覆盖两种场景（jailbreak和漏洞发现），其他攻击向量未涉及。

## 详细阅读分析

技术核心在于量化了系统框架与模型能力的分离：在相同模型和相同目标下，辅助配置召回100%，自主配置crash验证召回0%，说明1.2B模型本身几乎无法独立完成漏洞利用，但框架通过角色分化、正则检测、ASan崩溃分类和后处理CWE归一化弥补了模型推理能力的不足。有效危害率（EHR）的提出解决了LLM-as-judge对格式合规性误判为有害内容的问题，对安全评估指标设计有重要参考价值。两实验共同表明：攻击成本已趋近于零，防御者应投资于系统级防御而非仅依赖模型安全。

## 后续跟进问题

- 如何自动生成或优化系统框架（scaffold）以适配不同攻击目标？
- 安全政策如何具体定义和测量系统级能力？是否需要类似有效危害率的行业标准？
- 在更大规模模型（如7B、70B）上，系统框架与模型能力的贡献比例是否变化？
- 防御方如何构建等效的协调攻击检测系统以提前预警？
- 实验中的漏洞发现框架能否迁移到真实大型代码库（如Linux内核）？
