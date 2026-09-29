# SoK: You Find What You Seek: Rethinking Oracles, Guidance, and Input Generation in Hardware Fuzzing

## 基本信息

- 作者：G. Abarajithan、Zheng-Hua Ma、Cristian Tirelli、Andres Meza、F. Restuccia、C. Sturton、Ryan Kastner
- 发表日期：2026-09-23
- 会议/期刊：未记录
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: cpu, rtl, soc；verification/fuzzing method: fuzz, verification；security relevance: security
- 论文页面：[https://www.semanticscholar.org/paper/4ab1e2172f097a417e6385d209c20c870f74aad1](https://www.semanticscholar.org/paper/4ab1e2172f097a417e6385d209c20c870f74aad1)
- PDF：[https://arxiv.org/pdf/2609.27300v1](https://arxiv.org/pdf/2609.27300v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 18 页，提取 96114 字符

## 摘要

Hardware fuzzing is an active area in security verification research, yet its industrial adoption remains in its early stages. This SoK examines which lessons from software fuzzing carry over to hardware and where unique approaches are needed. By analyzing 52 fuzzers across RTL/IP, CPU, NoC, and SoC designs, we introduce an analytical framework that frames verification as a bounded search. This search is defined by its objective, oracle, guidance, input generation, target abstraction, and budget. Consequently, a campaign only uncovers failures it can effectively reach, recognize, and prioritize before exhausting its resources. We distinguish two roles for hardware fuzzing: (1) augmenting constrained-random verification (CRV) via feedback-guided coverage and (2) directed adversarial testing based on threat models and security specifications. Through our framework, we identify what each campaign can observe and generate, providing a basis for assessing the evidence behind reported results. Our analysis suggests that mainstream adoption of hardware fuzzing will require reusable interfaces, target-specific verification assets, reproducible evaluations, and transparent reporting of cost and user effort.

## 研究问题

硬件 Fuzzing 在学术安全验证中非常活跃，但工业采纳仍处早期。论文要回答的核心问题是：缺少一个统一的分析框架来判断某个 fuzzing campaign 究竟能“到达、识别、优先化”哪些失败，也缺少判断不同硬件 fuzzer 何时可比较、可复现、可部署的条件。具体分解为三问：(1) fuzzing 在何处补充既有验证（CRV、形式化、定向对抗测试）；(2) 每个 fuzzer 的 oracle 能识别什么、输入生成能到达什么、guidance 能优先化什么；(3) 公平比较与可复现评测需要哪些条件。

## Introduction 梳理

研究缺口：软件 fuzzing 三十年积累的执行反馈、失败检测、结构化输入生成、harness 与持续 fuzzing 基础设施并不能自动迁移到硬件——硬件并行执行、RTL 仿真中错误通常不 crash 模拟器、bug 可能横跨多个信号与时钟周期，且“有用输入”强依赖目标是 IP、CPU 还是完整 SoC。既有工作的不足在于：各硬件 fuzzer 使用互不相同的 oracle、反馈信号与输入表示；评测以自消融、重实现、引用前作数值或功能对照表为主，很少与现代 CRV 在同一环境同一预算下比较；DUT 常只写 Rocket/BOOM/OpenTitan 而不写版本与配置；artifact 与预算/人工投入报告不一致，导致“谁更好”难以判定。作者主张硬件 fuzzing 应承担两种角色：(1) 通过反馈引导覆盖来增强 CRV；(2) 基于威胁模型与安全规约做定向对抗测试。贡献（作者明确声称）：(a) 把硬件 fuzzing 形式化为预算受限的有界搜索，分解出 verification objective、oracle、guidance、input generation、target abstraction、budget 六要素及其子组件与权衡；(b) 对横跨 IP/CPU/NoC/SoC 的 52 个硬件 fuzzer 做结构化比较（oracle 族、结构/功能/定向 guidance、输入表示、变异与调度策略、solver 辅助的目标到输入生成）；(c) 指出常用反馈信号与 verification plan/threat model 所编码的功能与安全行为之间存在普遍错配；(d) 比较评测、可复现与部署要求，提出公平比较与主流采纳的条件（一致指标、版本化 DUT、公开 bug 语料、共享验证基础设施、组件消融、开放 artifact）。

## 方法

研究类型：Systematization of Knowledge（文献分析），不是新实验。分析对象为 52 个硬件 fuzzer，按 RTL/IP、CPU、NoC、SoC 抽象层次归类；同时以软件 fuzzing（AFL++、OSS-Fuzz、FuzzBench、Magma、Klees et al.、SAGE、Csmith/syzkaller）作为迁移经验的对照。分析工具是作者提出的框架：verification objective 驱动 oracle（决定哪些失败可被识别）、guidance（决定有限预算下哪些执行受重视）、input generation（决定哪些测试可被表达与到达），外加上层约束 target abstraction 与 budget（时间、算力、内存、人力）。Algorithm 1 给出统一伪代码：initialize(seed)→select_parent→assign_energy→generate_inputs→apply_harness→execute_observe→measure_feedback→check_oracle→is_interesting→adapt_search，并明确 feedback 与 oracle 相互独立。输入生成（Table 3，计数非互斥）：IP(10) 以 Mutation 9 / Solving 3，表示如 bytes→pins×cycles、ATPG 激活模式、SAT/Z3 补全；SoC/NoC(9) M7/C2/S3，表示如 firmware（FPGA emulation）、bytes 配置的 tamperer（firmware/NoC/memory flip）、bytes→UVM sequences、总线事务翻译为 SoC 程序种子；CPU(31) M23/C12/S1，表示如 ISA 指令或程序 IR 编辑、指令/中断/地址、模板与 transient seed、ISS 或执行模型下构造（操作数、页表）、LLM 生成 RISC-V 程序（ChatFuzz/GenHuzz/GoldenFuzz，用 ISA 有效性、RTL coverage 作为 reward）、model checker 求解未覆盖点；Misc(3) M3（bytes→TileLink、netlist 输入按控制/数据标注分别变异）。反馈/coverage（Table 2，非互斥）：implementation structure/state 32（Coverage 24，Score 8：GA fitness、PSO、多臂/上下文 bandit reward、deep-RL reward、LM RL 与调优）；selected region of design 6；user-defined behavior 3（UVM 功能 covergroup 等）；threat model / security property 12；program 1；other 6（不使用执行反馈，改用静态/形式化分析、执行模型、历史数据或构造规则）。oracle（Table 1 四族，53 个非互斥归类覆盖 52 个中的 44 个）：reference-model comparison 21；specialized semantic/cost model 8；differential/relational 11；property/runtime checker 13。BugsBunny 与 RFUZZ 将失败判定交给用户定义 target 或外部 checker；FMTC、TargetFuzz、DirectFuzz、FuSS、ProFuzz、RTLFuzzLab 只报告可达性/覆盖，不实现 pass/fail oracle。DUT/平台：RTL/IP（SiFive TileLink 外设、OpenTitan AES/HMAC/KMAC/RV-Timer、spinal.lib、OpenCores/Trust-Hub）、CPU（Rocket/BOOM、CV A6、mor1kx/or1200 等）、SoC/NoC（Ariane/CVA6、OpenPiton、OpenTitan、Caliptra、PicoSoC 等）；执行平台包括开源/商业仿真（Verilator、Synopsys VCS、Cadence Xcelium/JasperGold）、FPGA emulation 与物理硬件；可见性分布为 black-box 2 / grey-box 30 / white-box 20（Table 5）。是否需要 golden model：依 oracle 族而定——reference-model 族需要独立参考模型/ISS/scoreboard/golden 结果；differential/relational 族用成对执行、self-composition 或跨实现比较代替单一 golden；property/runtime checker 族依赖断言、契约、monitor、sanitizer 或超属性（hyperproperty）编码；specialized model 族用微架构/泄漏/信息流/漏洞成本模型。文中还给出 OpenTitan ac_range_check 的 CRV 伪代码（Algorithm 2）作为对照，其 oracle = Monitor + Golden Reference Model + Scoreboard + Assertions，并强调 oracle 必须与 target abstraction 和 threat model 匹配（局部断言不能证明 SoC 级安全不变量）。5.3 提出 guidance 链：objective→target behavior→observable→feedback（coverage 或 score）→search policy，每一步都可能丢弃信息，且“no optimizer can recover distinctions discarded earlier”。

## 实验与评估

baseline：NoCFuzzer 是论文点名的少见例子，在同一 UVM 环境、共享覆盖目标下比较 fuzzing 与 CRV [42]；CPU 侧出现过 riscv-dv（仅一个核）、riscv-torture、random regression；IP 侧出现过同 testbench 的 CRV、uniform random、只引用未实测的 regression speedup。大量工作只做 guidance-disabled 消融、自消融、同源重跑、重实现、引用前作数值、或仅给功能对照表，而非与可运行的现代 CRV 对比（论文据此认为多数比较无法归因于搜索机制本身）。实验预算：论文要求对齐 verification objective、target abstraction、oracle 与预算后再比较，并主张给 CRV 与 fuzzer 相同时间与算力、以覆盖与 bug 数（而非执行次数）衡量；但本文并未给出各被调查工作的统一预算数值，也未做统一重跑（未确认）。统计：本文没有做统计检验或定量元分析（未确认），只报告计数与分类表；它建议多次独立 seed 并报告分布与不确定性，理由是 fuzzing 对 seed 高度敏感。被引证据包括：Encarsia 用自动 bug 注入评测 CPU fuzzer，发现两个 fuzzer 在开启/关闭结构反馈时找到相同的注入 bug，而更换 seed 程序会改变被找到的 bug 集合 [3]；Klees et al. 指出 32 篇软件 fuzzing 评测每篇都有问题；FuzzBench 与 Magma（reach/trigger/detect 区分）被作为可借鉴范式。NoCFuzzer 的结论：CRV 更快关闭了容易的 router covergroup，而 fuzzing 在预算内关闭了 CRV 未达成的更难代码与功能目标。bug/CVE：SynFuzz 报告新的 synthesis bug 与 CVE（来自被引文献报告）；IP 类别中十个工作未报告任何 bug；可用的 bug 来源包括 Hack@DAC 竞赛注入 bug（PULPissimo/OpenPiton/OpenTitan）、EnCorpus 的 90 个经形式化检查的 CPU bug，以及可作共享 oracle 的 SystemVerilog 断言套件；本 SoK 自身未做新 bug 发现（Open Science 节声明无新实验）。开销：论文论证 fuzzing 因 guidance 与输入生成而可能每测试更贵，但若更少测试即可关闭关键覆盖或暴露失败则可能优于 CRV，并要求分别报告求解与执行成本、内存与人工投入；正文未汇总实测开销数据（未确认）。Artifact：Table 4 汇总各方向的 artifact 状况（公开代码 / 部分或占位 / 承诺无 URL / 按需 / 未找到），并指出复现常需精确 DUT 与配置、输入资产、工具版本或许可、辅助验证基础设施与专用硬件；本文自身不提供实验 artifact。

## 核心贡献

1) 提出把硬件 fuzzing 视为“预算受限的有界搜索”的分析框架，显式分离 verification objective、oracle、guidance、input generation、target abstraction 与 budget，并给出统一伪代码与组件级权衡。2) 首次（作者主张）对 52 个横跨 IP/CPU/NoC/SoC 的硬件 fuzzer 做统一词汇下的结构化比较，包括 oracle 四族分类、guidance 的观测来源与类型（coverage 或 score）、输入生成机制（变异/构造/求解）与可见性模型。3) 指出通用反馈信号与 verification plan/threat model 所编码行为之间的系统性错配，并提出 guidance 应从验证目标反向设计（objective→target behavior→observation→feedback→search policy）。4) 给出公平比较与可复现的评测处方：对齐目标、抽象、oracle 与预算后做单变量消融；用独立 covergroup/oracle replay fuzzer 生成的输入；按 IP/CPU/NoC/SoC 与目标组织版本化 benchmark 家族并区分 reach/trigger/detect。5) 汇总部署与复现所需的 DUT 表示、harness、seed、toolchain 许可、专用硬件与人力成本等要求，作为面向工业采纳的清单。

## 与本仓库研究主线的关系

对本库的“RTL & SoC 硬件 Fuzzing”主题属于直接相关（元研究/框架与评测层），对“多 hart 与内存一致性验证”属于强邻近而非直接覆盖——正文没有出现缓存一致性或内存一致性模型 fuzzing 的专门章节、也无 coherence bug 的归类或案例，映射需要推断。可直接借鉴的点：(a) 框架可用于为一一致性/多 hart campaign 明确六要素，特别是 oracle 选择——differential/relational 族（成对执行、self-composition、跨实现比较）与 property/runtime checker 族（断言、契约、超属性）在机制上与基于多执行比较的序化/原子性检查天然对应，但论文未点名该场景。(b) NoC/SoC 章节的论述与多 hart 交叉请求直接相关：SoC/NoC 级 harness 须保留 ordering、handshake、并发与响应，firmware 单独不足以表达恶意 NoC 事务或内存翻转；NoCFuzzer 的教训是当每个变异字节影响多个 NoC 队列时性能反而低于随机测试，这提示互连/一致性路径的 harness 粒度设计风险。(c) 5.3 的 guidance 链对齐原则可用来避免用 mux toggle 之类结构反馈去逼近一致性类 bug。(d) 7.3 的 benchmark 处方（版本化 DUT + covergroup + oracle + faulty/fixed 修订 + 注入 bug + replay 脚本）对一致性验证的公平评测有直接借鉴价值。(e) Table 5 的可见性模型（grey/white-box 占多数）对需要内部状态观测的一致性 oracle 设计有参考意义。总体：方法与评测层面的直接相关文献，技术细节需自行映射。

## 结论

中心结论是 “you find what you seek”：campaign 只在其 oracle、输入生成、guidance 三者与验证目标重叠且在预算内时才可能发现失败，改进任一组件都无法消除其余组件施加的限制。因此 guidance 必须与 objective 对齐（功能 coverpoint 优于纯结构距离，安全派生 score 优于盲目结构覆盖），coverage closure 与定向进展需要不同种类的反馈，结构反馈只有在保留目标相关区分时才有意义。作者给出的采纳条件：oracle/guidance/输入生成与验证目标强对齐；做子组件级消融；把 harness、grammar、seed、covergroup、oracle 作为版本化 campaign 资产；按 IP/CPU/NoC/SoC 与验证目标组织 benchmark 家族而非单一排行榜，包括版本化 DUT、faulty/fixed 修订、真实与注入 bug、replay 脚本、资源预算与测量流程；coverage 最大化类 fuzzer 应与既有 CRV 在同环境同预算对比并分别报告人工投入，定向对抗类需在同安全目标、同威胁模型与预算下与替代方案比较；此外还需要可复用工具、稳定接口、持续 fuzzing、失败 triage 与跨平台可靠 replay。

## 局限性

1) 论文类型限制：这是 SoK/文献综述，Open Science 节明确说明不报告新实验或需要源码/数据/二进制的经验测量，因此所有性能、覆盖、bug 与 CRV 对比结论均来自被引文献，本文未重复验证。2) 分类计数为作者判断且非互斥（Table 1 的 53 个归类覆盖 44/52，Table 2、3 计数亦非互斥），正文未给出编码准则、双人复核或一致性度量（未确认）。3) 论文批评他人未报告预算、统计与人工投入，但正文也未汇总这些数值：各 campaign 的具体时间/算力预算、覆盖数值、统计显著性、triage 与人工工时均未在提供的正文中给出（未确认）。4) 框架的解释力未作实验验证：oracle/guidance/input generation 的分解与“有界搜索”是有组织力的分析视角，但本文未证明它能预测某个 fuzzer 的相对效果。5) 提出的 benchmark 家族、共享 oracle、自动属性生成仍是建议；作者承认初始基准集无法满足所有目标，自动属性生成仍是开放问题。6) 适用范围：论文未专门分析多 hart 缓存一致性或内存一致性模型 fuzzing，也未列出此类工作的专项归类；相关适用性需要谨慎推断。7) 框架的边界被作者自己限定：oracle 未检查的失败对 campaign 不可见，feedback 是有损代理，coverage 不能证明无 bug。

## 详细阅读分析

建议精读并按顺序提取：§2 与 Fig.1（框架与“bounded search”定义、oracle/guidance/input generation 的职责边界）；§3.2 Algorithm 1（硬件 fuzzing 循环的统一词汇与每一函数的语义，可用于对照自律实现的 fuzzer）；§3.3 Algorithm 2（OpenTitan ac_range_check 的 CRV 具体形态：约束输入生成、功能 covergroup 的 cross 与 illegal bins、Monitor+GRM+Scoreboard+Assertions 构成的 oracle，以及“人工检查覆盖缺口”这一与 fuzzing 的分界线）；§4.1（oracle 四族与盲区：架构参考模型看不见微架构/信息流违规；局部断言不等价于 SoC 级不变量）；§5.1–5.3（反馈来源与类型表、coverage 与 score 的代价/收益、target selection 中“自动求解器不能判定目标是否符合用户验证意图”、guidance 链的信息丢失）；§6.1（grammar 有效性与灵活性的张力、NoCFuzzer harness 反例、威胁模型入口点必须进入 grammar）；§6.3（seed 与调度、DirectFuzz 的 energy 恢复、TaintFuzzer 的确定性算子→havoc 切换）；§7.1–7.3（可比性条件、组件消融、replay 至 CRV 环境并用独立 covergroup 度量、Klees/Magma/FuzzBench 的范式迁移）；§8.1–8.2（部署所需资产与可见性模型）；Table 1–5（分类计数与 artifact/CRV 对比现状）。同时值得顺链阅读的关键被引工作：NoCFuzzer [42]、Encarsia [3]、HyperFuzzing [50]、FUZZItizer [34]、SpecDoctor/DejaVuzz/MileSan（同一高层目标下不同 oracle 识别不同失败集的例证）、Magma [26] 与 FuzzBench [45]。

## 后续核验问题

- 1) 如何用该框架定义多 hart/缓存一致性 campaign 的 verification objective 与失败集合？oracle 应选 differential/relational（成对执行与 self-composition 比较 litmus 式结果）还是 property/runtime checker（互连协议断言 + 序化/原子性契约），还是二者组合并在 SoC 层把 ISA 级 GRM 与互连 monitor 拼接？2) 在一致性/争用路径探索中，哪种反馈既廉价又与目标对齐：NoC 事务与等待时间、CSR 转换、占用的 covergroup、还是结构 mux/CSR 覆盖？如何按论文要求做组件消融来证明 guidance 的增益而不是 seed 或 harness 的增益？3) 多 hart 仿真本身昂贵，如何按论文建议分别报告求解、执行、内存与人工成本，并给出可复现的预算定义？4) 能否以 OpenPiton/OpenTitan 等为基础，构造“按抽象层次与验证目标组织”的一致性 benchmark 家族（版本化 DUT + covergroup + oracle + faulty/fixed 修订 + replay 脚本）？EnCorpus 与 Hack@DAC 的 bug 集中是否包含一致性/序化类 bug（正文未说明）？5) 多 hart 并发交织与原子操作的 grammar/harness 如何设计，才能既保证协议合法序列又不排除对抗性输入（协议违规、竞争窗口、内存翻转）——这是否会与“transaction-aware harness 避免 protocol-invalid 测试”的取舍冲突（参见 eXpect/Xray 的对照）？6) 论文的框架在多大程度上能预测具体 fuzzer 相对效果？需要什么样的受控实验（同 objective、同 oracle、同抽象、同预算、多变 seed 分布）才能验证“you find what you seek”的可操作预测力？7) 对于需要内部状态观测的一致性 oracle，Table 5 的 grey/white-box 分类如何影响 instrumentation 成本与可复现性？
