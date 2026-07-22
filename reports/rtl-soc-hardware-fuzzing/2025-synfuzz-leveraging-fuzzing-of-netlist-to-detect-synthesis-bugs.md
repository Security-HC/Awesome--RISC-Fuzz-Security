# SynFuzz: Leveraging Fuzzing of Netlist to Detect Synthesis Bugs

## 基本信息

- 作者：Raghul Saravanan、Sudipta Paria、Aritra Dasgupta、Venkat Nitin Patnala、Swarup Bhunia、Sai Manoj P D
- 发表日期：2025-04-26
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=8）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: processor, rtl, soc；verification/fuzzing method: fuzz, verification, formal verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2504.18812v3](http://arxiv.org/abs/2504.18812v3)
- PDF：[https://arxiv.org/pdf/2504.18812v3](https://arxiv.org/pdf/2504.18812v3)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 15 页，提取 92238 字符

## 摘要

In the evolving landscape of integrated circuit (IC) design, the increasing complexity of modern processors and intellectual property (IP) cores has introduced new challenges in ensuring design correctness and security. The recent advancements in hardware fuzzing techniques have shown their efficacy in detecting hardware bugs and vulnerabilities at the RTL abstraction level of hardware. However, they suffer from several limitations, including an inability to address vulnerabilities introduced during synthesis and gate-level transformations. These methods often fail to detect issues arising from library adversaries, where compromised or malicious library components can introduce backdoors or unintended behaviors into the design. In this paper, we present a novel hardware fuzzer, SynFuzz, designed to overcome the limitations of existing hardware fuzzing frameworks. SynFuzz focuses on fuzzing hardware at the gate-level netlist to identify synthesis bugs and vulnerabilities that arise during the transition from RTL to the gate-level. We analyze the intrinsic hardware behaviors using coverage metrics specifically tailored for the gate-level. Furthermore, SynFuzz implements differential fuzzing to uncover bugs associated with EDA libraries. We evaluated SynFuzz on popular open-source processors and IP designs, successfully identifying 7 new synthesis bugs. Additionally, by exploiting the optimization settings of EDA tools, we performed a compromised library mapping attack (CLiMA), creating a malicious version of hardware designs that remains undetectable by traditional verification methods. We also demonstrate how SynFuzz overcomes the limitations of the industry-standard formal verification tool, Cadence Conformal, providing a more robust and comprehensive approach to hardware verification.

## 研究问题

Existing hardware fuzzing techniques focus on RTL abstraction and fail to detect bugs introduced during synthesis and gate-level transformations, including those from compromised EDA libraries. There is a need for fuzzing at the gate-level netlist to identify synthesis errors and library-related vulnerabilities.

## Introduction 梳理

The complexity of modern IC designs introduces vulnerabilities at multiple abstraction levels. Current hardware fuzzers only operate at RTL, missing issues from synthesis and EDA library manipulation. Formal verification (e.g., LEC) is not scalable and requires expert knowledge. SynFuzz is proposed as the first hardware fuzzer targeting gate-level netlists, using differential fuzzing and coverage tailored to library cells, to detect synthesis bugs and demonstrate a library mapping attack (CLiMA).

## 方法

**Input generation:** NetInput format concatenates input ports with their widths; AFL-style mutation with separate engines for control and data bits. **Feedback/coverage:** Library Toggle Coverage (monitors toggling of library cell instances) and Expression Coverage (checks constant assignments). **Oracle:** For standard synthesis bugs, compare RTL and gate-level simulation final traces; for library bugs, use differential fuzzing (DiffLib) with three configurations: intra-tool inter-lib, inter-tool intra-lib, inter-tool inter-lib. **DUT/platform:** RTL and netlist simulated with Synopsys VCS or Cadence Xcelium; synthesis with Synopsys Design Compiler, Cadence Genus, or Yosys. **Golden model:** RTL serves as golden for ordinary synthesis bugs; library bugs lack a golden model and rely on differential analysis.

## 实验与评估

**Baseline:** Compared qualitatively with Cadence Conformal LEC (SynFuzz overcomes its limitations). **Budget:** 48-core Intel Xeon, 512GB RAM; small designs 8 hours, large 12 hours. **Statistical results:** Found 7 new synthesis bugs (in RSA, PicoRV32, MIPS, or1200) and 10 existing Yosys bugs. Coverage: small designs ~99%, large designs ~67–70%. **Overhead:** Not reported. **Artifact:** CVEs assigned for bugs; code/tool artifacts not explicitly released.

## 核心贡献

1) First hardware fuzzer operating on gate-level netlist for synthesis bug detection. 2) Novel CLiMA attack exploiting optimization settings to insert undetectable bugs. 3) Discovery of 7 new synthesis bugs and 10 existing Yosys bugs. 4) Demonstration that SynFuzz overcomes limitations of formal equivalence checking.

## 与本仓库研究主线的关系

Directly relevant as it addresses hardware fuzzing at RTL/SoC level. Focuses on single-core designs; method (differential fuzzing, coverage guidance) could be extended to multi-hart and memory consistency verification.

## 结论

SynFuzz effectively detects synthesis and library bugs by fuzzing gate-level netlists with tailored coverage and differential comparison. It introduces CLiMA, a library mapping attack that bypasses LEC. Compared to Conformal, SynFuzz requires no specialized design or tool knowledge.

## 局限性

Requires access to RTL and synthesis tool licenses; limited to zero-delay simulation (no timing bugs); not yet extended to FPGA synthesis or multi-hart designs.

## 详细阅读分析

Sections 4 (SynFuzz design), 5.2 (bug details), 5.5 (comparison with LEC), and 6 (CLiMA attack). Figures 4 and 6 illustrate the workflow and differential configurations.

## 后续核验问题

- How can SynFuzz be adapted to fuzz multi-core or multi-hart designs with shared memory?
- What is the runtime overhead of SynFuzz compared to RTL-only fuzzers?
- Can CLiMA attacks be detected by other verification methods like simulation-based information flow tracking?
- How sensitive is the Library Toggle Coverage to different mutation strategies?
