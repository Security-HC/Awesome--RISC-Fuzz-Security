# Data-Oblivious ML Accelerators using Hardware Security Extensions

## 基本信息

- 作者：Hossam ElAtali、John Z. Jekel、Lachlan J. Gunn、N. Asokan
- 发表日期：2024-01-29
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: processor, cpu；verification/fuzzing method: information flow tracking；security relevance: security, side channel
- 论文页面：[http://arxiv.org/abs/2401.16583v1](http://arxiv.org/abs/2401.16583v1)
- PDF：[https://arxiv.org/pdf/2401.16583v1](https://arxiv.org/pdf/2401.16583v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 8 页，提取 40236 字符

## 摘要

Outsourced computation can put client data confidentiality at risk. Existing solutions are either inefficient or insufficiently secure: cryptographic techniques like fully-homomorphic encryption incur significant overheads, even with hardware assistance, while the complexity of hardware-assisted trusted execution environments has been exploited to leak secret data. Recent proposals such as BliMe and OISA show how dynamic information flow tracking (DIFT) enforced in hardware can protect client data efficiently. They are designed to protect CPU-only workloads. However, many outsourced computing applications, like machine learning, make extensive use of accelerators. We address this gap with Dolma, which applies DIFT to the Gemmini matrix multiplication accelerator, efficiently guaranteeing client data confidentiality, even in the presence of malicious/vulnerable software and side channel attacks on the server. We show that accelerators can allow DIFT logic optimizations that significantly reduce area overhead compared with general-purpose processor architectures. Dolma is integrated with the BliMe framework to achieve end-to-end security guarantees. We evaluate Dolma on an FPGA using a ResNet-50 DNN model and show that it incurs low overheads for large configurations ($4.4\%$, $16.7\%$, $16.5\%$ for performance, resource usage and power, respectively, with a 32x32 configuration).

## 研究问题

将硬件动态信息流跟踪（DIFT）从 CPU 扩展到矩阵乘法加速器，以保护外包计算中客户端数据的机密性，同时最小化开销。

## Introduction 梳理

现有外包计算解决方案中，全同态加密（FHE）虽然安全但开销巨大，即使有硬件加速仍比本地计算慢数个数量级；可信执行环境（TEE）如 Intel SGX 易受侧信道攻击，且信任软件处理代码。BliMe 和 OISA 通过硬件 DIFT 保护 CPU 工作负载，但不支持加速器。然而许多外包计算（如 ML）广泛使用加速器。本文提出 Dolma，将 DIFT 应用于 Gemmini 矩阵乘法加速器，在存在恶意/易受攻击软件和侧信道攻击下高效保证客户端数据机密性。贡献包括：首次为加速器提供抗软件漏洞和侧信道的机密计算平台，无需软件纳入 TCB；利用加速器的固定行为在行粒度上实现 DIFT，显著降低面积开销；集成到 BliMe 框架实现端到端安全；通过 F* 形式化模型给出机器检查的安全证明。

## 方法

输入生成：客户端加密数据，服务器端 BliMe 指令原子解密并标记（盲化）数据。反馈/coverage：无。Oracle：DIFT 策略——如果任何输入行有非零标签且标签不匹配则故障，输出行获得非零标签；禁止使用盲化指令或地址。DUT/平台：Gemmini 矩阵乘法加速器集成到 Chipyard SoC（RISC-V BOOM 核），在 Xilinx VCU118 FPGA 上评估。是否需要 golden model：无需，安全性由形式化模型证明。

## 实验与评估

baseline：未修改的 Gemmini（无 BliMe）。实验预算：在 FPGA 上运行 ResNet-50 图像分类，100 张随机 ImageNet 图像。统计：平均性能开销 5.6%（8x8: +6.0%, 16x16: +6.5%, 32x32: +4.4%）；时钟频率无显著变化（WNS 类似）；FPGA 资源开销（LUT/寄存器）随尺寸增大相对降低（8x8 约 250%，32x32 约 60%）；功耗增加 12.2%-16.5%。bug/CVE：未提及。开销：见上述。Artifact：未确认。

## 核心贡献

1. 首次将 BliMe 的 DIFT 扩展到矩阵乘法加速器（Gemmini），实现端到端数据机密性保证；2. 提出行粒度 DIFT 优化，利用脉动阵列的固定行为减少面积开销（相对通用 CPU DIFT）；3. 集成到 Chipyard 并评估实际 ML 工作负载，显示低开销；4. 扩展 BliMe 的 F* 形式化模型，证明加速器操作的安全性。

## 与本仓库研究主线的关系

不直接相关。论文主题是安全硬件设计（DIFT 实现），而非处理器/RTL Fuzzing、多 hart 一致性验证或微架构安全自动测试。仅方法上可能借鉴其硬件安全扩展思想，但与本仓库核心方向无重叠。

## 结论

Dolma 通过识别固定功能组件并移除不必要的跟踪逻辑实现了高效的 DIFT，将行级跟踪逻辑用于脉动阵列，开销低且可扩展。适用于其他固定功能单元如密码加速器和 GPU。

## 局限性

仅针对没有数据相关控制流的固定功能加速器（如 Gemmini）；对于有数据相关优化或片上控制流的加速器（如稀疏矩阵加速器、GPU）需要额外处理；考虑物理攻击（如总线嗅探、差分功耗分析）超出范围。

## 详细阅读分析

建议阅读第 IV 节设计细节、第 V 节评估和附录中形式化证明。重点关注标签传播、读-检查-写流水线优化以及安全模型。

## 后续核验问题

- 1. Dolma 的 DIFT 策略是否能用于检测硬件设计错误（如信息泄露）？2. 能否将 Dolma 的标签逻辑注入到 RTL Fuzzing 中作为 Oracle 检查意外信息流？3. 如何将类似方法扩展到 GPU 等更复杂加速器？4. 论文未讨论一致性，但多 hart 场景下 DIFT 标签在核间一致性协议中如何维护？
