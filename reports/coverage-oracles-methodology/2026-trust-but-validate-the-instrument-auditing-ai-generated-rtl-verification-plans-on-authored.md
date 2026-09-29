# Trust, but Validate the Instrument: Auditing AI-Generated RTL Verification Plans on Authored Security-Regression Proxies

## 基本信息

- 作者：Hang Xiao、Chuhong Xu、Kainan Zhou、Gangzhen Qian、Lu Yi
- 发表日期：2026-09-17
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：B·强邻近（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: rtl；verification/fuzzing method: verification, validation；security relevance: security
- 论文页面：[http://arxiv.org/abs/2609.19844v1](http://arxiv.org/abs/2609.19844v1)
- PDF：[https://arxiv.org/pdf/2609.19844v1](https://arxiv.org/pdf/2609.19844v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 7 页，提取 33174 字符

## 摘要

AI-generated RTL verification plans can satisfy a provider schema yet fail at the boundary to trusted execution. We present SecTB-RTL, an auditable framework covering 31 tasks and 124 authored hardware-security regressions. A deterministic non-AI baseline killed 36, 75, and 78 mutants at increasing resource limits. The first confirmatory run (C1-R2) failed before model execution because the provider rejected its response schema. After a schema-only repair made without viewing outcomes, a separately frozen follow-up run (C1-R3) completed 1,860 calls. The provider accepted 1,857 responses, but only nine passed the production semantic validator. The generation and execution rules did not match. We therefore preserve the run as an instrument-validation incident and report no prompt-effect estimate. This incident shows that provider or schema acceptance does not establish execution validity. Compilation and coverage are only diagnostics; the exact saved artifact must pass the full production path. A subsequent follow-up is excluded because it did not satisfy the preregistered evidence-completeness gate and is treated only as future work. We release the benchmark, failure-preserving contract, incident provenance, and governance controls needed to prevent infrastructure behavior from being misreported as model behavior.

## 研究问题

本文研究的核心问题是：AI/LLM 生成的 RTL 验证计划（verification plan）即便满足提供方 schema、能通过解析与编译，是否真的能在可信执行链中构成有效的安全测量工具（measurement instrument），以及当生成规则与执行规则不一致时，测量过程本身会在哪一语义边界失败。论文将问题从“LLM 能否生成 HDL/测试平台”转为“生成的验证器能否在预注册、计入全部已调度尝试的协议下提供可测量的安全证据”。

## Introduction 梳理

既有 LLM 硬件验证研究（如 AutoBench、VerifLLMBench、AssertionBench、AssertLLM）主要评估功能正确性、可执行行为或断言生成质量；硬件安全基准（HardSecBench）表明功能可接受的生成 RTL 仍可能携带 CWE 类弱点，但这些工作没有回答三个部署问题：模型响应到 golden 设计上有效验证器之间损耗多少、安全上下文相对等注意力功能提示是否提升检测、生成验证器达到高结构覆盖率时合格安全回归仍有多少未被生成 oracle 检出。本文的缺口在于：缺少一个把任务级处理分配、预筛选隐藏回归、以及失败即关闭（fail-closed）的部署证据链结合起来的可审计评测框架。作者声称贡献包括：SecTB-RTL 安全证据基准（31 个 RTL 任务、16 个 CWE/根机制分组、每任务 4 个隐藏预合格回归，共 124 个变体）；一次完整 1,860 调用运行的端到端事故证据，量化提供方接受（1,857 次）与生产语义有效（9 次）之间的差距；失败即关闭的保证契约；以及在全部 124 个变体上三个预算下的确定性非 AI 基线校准证据。作者明确不声称首次 LLM 生成硬件安全验证计划、不声称安全提示普遍提升、不声称防止漏洞利用或通过综合/物理实现/部署保持安全。

## 方法

{'dut_platform': 'DUT 是来自 HardSecBench revision e2084be7 的小型公开或派生 RTL 模块，经过 alpha-renaming 和去注释；任务按（CWE、根机制）分层，历史 C1 帧有 32 个任务，因 T21 无法实例化目标构造且无盲备选，C1-R2 保留 31 个任务和 124 个变体。执行平台使用 Icarus Verilog 和 Verilator 做交叉仿真，Yosys 做综合和形式准备；执行环境隔离，限制仅顶层 HDL、有界执行、无生成文件或网络访问。威胁模型中的攻击者不是模型服务或评分主机，而是削弱安全属性的 RTL 变更（意外或恶意）。', 'feedback_or_coverage': '本文的生成流程没有使用反馈驱动或 coverage-guided 迭代：DSL 本身禁止随机、循环和分支，生成计划是确定性刺激加断言。覆盖率仅作为诊断阈值（line≥90%、toggle≥80%），论文定义“coverage blind spot”为验证器通过 golden 设计并达到覆盖率阈值但变体仍存活的变体。作者在讨论中引用 coverage-guided stimulus generation 的迭代反馈工作，但未将其纳入本研究的执行方法。确定性基线使用固定手工模板和 32/64/128 步预算，没有反馈闭环。', 'golden_model_required': '需要 golden model。每个任务的生成产物必须在已知正确的 golden RTL 上以相同形式通过验证，再在四个隐藏变体上测试；golden 有效性、双仿真器一致性和变体检测是独立门。作者明确：编译、通过 golden 运行和高行覆盖率本身不足以证明 oracle 充分。', 'input_generation': '输入由 LLM 生成受限 JSON DSL 计划，格式为 sectb-stimulus-v1，必须包含 dsl_version、test_name 和 4–128 个有序步骤；DSL 允许 reset 赋值、顶层驱动、有界 ticks（1–16）和输出断言；禁止随机源、循环/分支、层次化访问、force、DPI、文件 I/O 和模型自写 verdict。提示臂包括 F0（功能目标）、FC（等注意力功能对照）、SA（抽象安全上下文，不含 CWE 或变体细节）、SE（显式安全需求）。R3 矩阵为 31 任务 × 3 模型别名 × 4 提示臂 × 5 重复，形成 465 个完整 task-model-repetition 块、1,860 次生成、7,440 个变体行；每个块内随机分配臂，全局调用顺序独立随机；每格仅允许一次提供方尝试，不重试、不重抽，所有已调度失败保留在分母中。', 'oracle': 'oracle 由生成计划中的输出断言以及可信 harness 降级生成的 self-checking SystemVerilog testbench 共同承担；杀死变体要求同一未修改的保存产物在 golden 设计上通过验证、在两个仿真器中一致，并杀死隐藏变体。变体作者化流程有 7 道门：解析并编译、与 golden 的顶层接口完全一致、golden 与变体均可综合、存在合法 witness 激活并通过顶层 harness 端口暴露差异、相对 golden 形式非等价、在可信 harness 下 replay witness、同一任务四个变体两两形式可区分。等价、不可达、不可观测、改变接口或重复的变体在任何生成验证器结果存在之前被排除。'}

## 实验与评估

{'artifact': '作者声称公开仓库包含基准、冻结协议、生成与执行代码、合格证据、事故清单和出处检查；历史基线冻结标签为 c1-confirmatory-author-freeze-v1（commit 2db72f31），后续修订冻结在 commit 675c214 下标签 82cecde5；C1-R2 作为不可变八次尝试 schema 事故保留，C1-R3 作为完成 1,860 调用的事故保留，均有 manifest、作者冻结、精确 schema 探针证据和替代恢复记录，且不把事故重新包装为处理结果。但正文也说明预注册是作者密封而非独立评审；artifact 的独立可复现性未在正文中进一步验证。', 'baseline': '确定性非 AI 基线使用固定手工模板，在 124 个变体上杀死 36/124（32 步）、75/124（64 步）和 78/124（128 步）；对应任务宏平均产出为 0.290、0.605 和 0.629。作者将其定位为基准校准，而非注册处理设计中的可交换 AI 臂，因为其 oracle 手工编写且资源预算固定。', 'bug_cve': '未确认发现真实 CVE 或生产漏洞。研究使用作者化安全回归变体作为受控代理，覆盖授权/门控、安全复位或失效默认、粘滞与优先级状态、边界/比较检查、调试或扫描泄漏等根机制，并用 CWE 分类词表；作者明确不声称杀死变体对应实际漏洞利用，也不声称存活测试意味着可被利用的芯片。', 'experimental_budget': 'R3 调度 1,860 次生成、7,440 个变体行、465 个完整块、5 次重复、3 个模型别名、4 个提示臂、31 个任务；每格一次提供方尝试，无重试。基线预算为 32/64/128 步。注册统计分析以任务为统计单位（n=31），使用配对对比、整任务重采样 bootstrap、块内随机化，主对比 SE-FC 在 α=0.05，次要对比 Holm 校正；但因 R3 未通过生产语义校准，这些程序未用于确认性提示效应声明。', 'overhead': '正文提到诊断记录包括延迟、token 和成本，但没有给出具体开销数值；因此开销未确认。可确认的运行开销相关数字是：R2 八次提供方尝试全部在提供方 schema 预验证阶段被拒，无模型响应、无 token/成本/覆盖/安全结果；R3 完成 1,860 次调用，提供方接受 1,857/1,860（99.84%），生产语义有效 9/1,860（0.48%），3 次提供方失败；1,848 次差距归因于执行层强制但生成面契约和精确 schema 探针缺失的 reset 状态机规则。', 'statistics': '作者明确区分：R3 支持聚合事故 funnel，不支持提示效应估计；没有完整病例救援、没有事后修复处理对比、没有按臂/模型/杀死/效应分层的结果挖掘。失败计入分母的失败归零评分仅在生成与执行规则对齐时有效，本研究因规则不匹配不能使用该修复。'}

## 核心贡献

关键贡献是方法论和证据治理层面的：1）一个安全证据基准 SecTB-RTL，包含 31 个 RTL 任务、16 个（CWE、根机制）分组和 124 个通过七道门的隐藏安全回归变体；2）一次完整的端到端事故证据，量化提供方接受（1,857/1,860）与生产语义有效（9/1,860）之间的巨大差距，并将该运行保留为工具验证事故而非处理结果；3）失败即关闭保证契约，覆盖提供方接受、schema、生产语义、渲染、双仿真器一致、golden 有效性和变体检测等独立门；4）在三个资源预算下对全部 124 个变体的确定性非 AI 基线校准参考。核心实践含义是：AI 生成的验证资产只有在精确持久化产物通过生产验证、干净 golden 执行、隐藏回归测试和可复现恢复检查后，才应进入安全决策。

## 与本仓库研究主线的关系

与仓库主题的关系应界定为“强邻近/方法借鉴”，而不是直接相关。它直接相关于 RTL/SoC 硬件 Fuzzing 中的 Oracle 有效性、覆盖盲点、故障注入/变异测试和评测治理，但其 DUT 是小型公开或派生 RTL 模块，DSL 禁止随机源、循环、分支和层次化访问，因此不涉及多 hart 调度、内存一致性、缓存一致性协议、原子性、乱序或并发交错。对多 hart/一致性路径研究，它不提供直接实验证据或可复用激励生成器；可借鉴的是其“每个边界单独检测”的分层保证链、失败即关闭校准、隐藏回归代理的预筛选门、coverage blind spot 诊断，以及把生成规则与执行规则绑定到同一生产验证器的要求。若将多 hart 一致性回归建模为隐藏变体，本文的变异合格门和事故保留实践可作为评测协议模板，但需要扩展 DSL 以支持并发、随机性和多 hart 仲裁。

## 结论

作者得出结论：在 31 个任务和 124 个作者化回归上，确定性基线建立了有界检测参考；两个 AI 研究暴露两层不同失败——R2 的提供方 schema 拒绝和 R3 的生成/执行语义不匹配。R3 完成了 1,860 次调用，但在冻结设计和事故处置下不支持任何提示效应声明。作者称负责任的结果是负面但具体的：提供方接受、流畅结构化输出和 schema 级探针并未验证一个可恢复的安全评测工具；编译和覆盖率仍是下游诊断，不能替代对齐的语义契约。可信 AI 辅助硬件验证必须在观察结果之前绑定并测试每个边界，包括持久化和恢复。

## 局限性

作者列出的威胁包括：构念效度——作者化变体是受控回归代理，不是生产漏洞利用，R3 契约不匹配使处理解释无效，尽管其聚合 funnel 是可靠事故证据；内部效度——事故分类是在不看臂、模型、杀死或效应分层的情况下做出的，没有报告完整病例子集或事后修复的处理对比；统计效度——R3 支持聚合事故 funnel，不支持提示效应估计，任务级分析不能修复测量工具中的构念无效；外部效度——证据限于公开 RTL、作者化回归、一个提供方表面、三个别名、固定日期和受限 DSL，是工作流保证发现而非模型普遍排名；可复现性——代码、协议、标签和 R1–R3 谱系有版本，事故 manifest 保留而非覆盖，但预注册为作者密封，非独立评审。另有未在正文中展开的限制：无多 hart、无内存一致性、无并发交错、无物理攻击、无模拟泄漏、无布局布线行为、无门级时序、无 foundry 威胁、无后硅验证；后续 follow-up 因未满足预注册证据完整性门被排除，仅作为未来工作。

## 详细阅读分析

深读要点：1）本文的失败不是模型能力失败，而是测量工具校准失败。R3 的 1,848 次差距被追溯到执行层强制的 reset 状态机规则未出现在生成面契约和精确 schema 探针中，探针自己的规范响应也在后续生产规则下失败；这说明“提供方接受”和“schema 探针通过”不能验证生产语义。2）作者提出多层次语义边界链：provider → schema → semantic contract → renderer → persistence → resume replay → golden validation → mutant oracle；每个箭头都是潜在语义边界，终止于下一层之前的探针不能验证该层，因此需要规范编码、负例 fixture 和 create-only 归档。3）变体预筛选的七道门（编译、接口一致、综合、合法 witness、形式非等价、replay、两两可区分）是值得借鉴的硬件安全回归构造流程，它把“目标必须可执行、可达、可观测且彼此不同”与“AI 是否检测到”分开。4）覆盖率被严格定位为诊断而非 oracle：coverage blind spot 定义为通过 golden 且达到 line≥90%/toggle≥80% 但仍存活的变体，直接挑战高覆盖率等于安全验证充分的假设。5）治理上采用预注册、任务级随机化、无重试、失败保留分母、作者密封冻结和事故与确认证据分离；即使发生 schema 事故和语义事故，也不从事后数据中挖掘有利臂。6）确定性基线显示 64 步到 128 步收益较小，提示更长通用刺激不能替代安全专用激活和 oracle，这一观察对硬件 fuzzing 的预算分配有参考意义。

## 后续核验问题

- 如何设计一个生成面与执行面共享的语义契约（例如 reset 状态机、时序语义、断言求值时机），使 schema 探针能够提前检测生产语义不匹配？
- 在多 hart/内存一致性 RTL 中，能否把本文的隐藏回归代理和七道合格门扩展到并发交错、缓存一致性协议状态和原子性属性？
- 如何为硬件安全验证定义可操作的 oracle 充分性指标，使其与 line/toggle 覆盖率解耦，并识别 coverage blind spot？
- 在 LLM 生成 RTL 验证计划的流程中，失败即关闭校准和 create-only 证据归档应如何工程化，才能防止基础设施行为被误报为模型行为？
- 确定性手工模板基线在 32/64/128 步下的收益递减是否可推广到其他 RTL 安全回归集合，以及安全专用激活策略相对通用刺激的增益如何量化？
- 本文的预注册为作者密封而非独立评审；独立第三方如何验证事故清单、冻结标签和精确持久化产物的可复现性？
- 若将 RISC-V 处理器核的安全回归作为任务，受限 JSON DSL 需要哪些扩展（并发、随机、内存访问、异常/中断）才能保持可审计性和可恢复执行？
