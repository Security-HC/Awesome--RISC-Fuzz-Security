# BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking

## 基本信息

- 作者：Hossam ElAtali、Lachlan J. Gunn、Hans Liljestrand、N. Asokan
- 发表日期：2022-04-20
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, rtl；verification/fuzzing method: taint tracking；security relevance: security
- 论文页面：[http://arxiv.org/abs/2204.09649v8](http://arxiv.org/abs/2204.09649v8)
- PDF：[https://arxiv.org/pdf/2204.09649v8](https://arxiv.org/pdf/2204.09649v8)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 16 页，提取 91740 字符

## 摘要

Outsourced computing is widely used today. However, current approaches for protecting client data in outsourced computing fall short: use of cryptographic techniques like fully-homomorphic encryption incurs substantial costs, whereas use of hardware-assisted trusted execution environments has been shown to be vulnerable to run-time and side-channel attacks. We present Blinded Memory (BliMe), an architecture to realize efficient and secure outsourced computation. BliMe consists of a novel and minimal set of instruction set architecture (ISA) extensions implementing a taint-tracking policy to ensure the confidentiality of client data even in the presence of server vulnerabilities. To secure outsourced computation, the BliMe extensions can be used together with an attestable, fixed-function hardware security module (HSM) and an encryption engine that provides atomic decrypt-and-taint and encrypt-and-untaint operations. Clients rely on remote attestation and key agreement with the HSM to ensure that their data can be transferred securely to and from the encryption engine and will always be protected by BliMe's taint-tracking policy while at the server. We provide an RTL implementation BliMe-BOOM based on the BOOM RISC-V core. BliMe-BOOM requires no reduction in clock frequency relative to unmodified BOOM, and has minimal power ($<\!1.5\%$) and FPGA resource ($\leq\!9.0\%$) overheads. Various implementations of BliMe incur only moderate performance overhead ($8--25\%$). We also provide a machine-checked security proof of a simplified model ISA with BliMe extensions.

## 研究问题

外包计算中保护客户端数据机密性，现有方法（FHE开销巨大、TEE易受运行时和侧信道攻击）均存在不足。

## Introduction 梳理

现有TEE面临软件漏洞和侧信道泄漏，FHE性能开销过大。BliMe通过最小硬件扩展（ISA污点跟踪）结合独立HSM和加密引擎，实现高效安全的外包计算，无需信任服务器软件。贡献包括：BliMe架构、BliMe-BOOM RTL实现、形式化安全证明和性能评估。

## 方法

输入由客户端使用会话密钥加密后发送；服务器通过加密引擎原子解密并标记为盲化（taint）。无显式反馈/coverage机制，违反策略时触发故障。Oracle基于HSM远程认证和加密引擎原子操作。DUT包括基于BOOM RISC-V核的RTL设计（BliMe-BOOM-1/8）和gem5模拟器。无需golden model，但形式化证明针对简化模型ISA。

## 实验与评估

Baseline为未修改BOOM和gem5默认配置。实验使用SPEC2017整数ref workload，FireSim FPGA综合测量资源/功率，gem5模拟1B指令。平均性能开销：BliMe-BOOM-1/8为23%，BliMe-gem5为25%，优化后8%。未发现bug/CVE。功率开销<1.5%，FPGA资源≤9.0%。Artifact开源：https://github.com/ssg-research/BliMe。

## 核心贡献

1) BliMe架构及ISA污点跟踪扩展；2) 基于BOOM的RTL实现BliMe-BOOM；3) 简化模型ISA的形式化安全证明；4) 全面的性能评估显示低开销。

## 与本仓库研究主线的关系

强邻近：直接涉及RISC-V硬件安全增强和污点跟踪设计，但主题为安全外包而非处理器验证/fuzzing。方法论可借鉴于多hart一致性验证中的信息流控制和侧信道防御，但本文未涉及一致性模型验证。

## 结论

BliMe通过硬件强制污点跟踪实现安全外包计算，性能开销适度（8-25%），兼容现有侧信道抵抗代码，并提供形式化安全证明。

## 局限性

硬件攻击（如Rowhammer、DVFS故障注入、物理侧信道）超出范围；依赖HSM和加密引擎正确实现；仅支持2^n-1个客户端；未实现HSM本身；部分性能开销源于Chipyard限制。

## 详细阅读分析

需深入理解污点传播规则（表I）、形式化证明技术（F*模型）以及BliMe-BOOM与BOOM的集成细节（尤其是缓存标签管理、推测执行策略）。

## 后续核验问题

- 1) BliMe的污点跟踪如何扩展至多hart场景以支持一致性验证？2) BliMe能否防御瞬态执行攻击（如Spectre）？3) 如何自动编译BliMe兼容代码？
