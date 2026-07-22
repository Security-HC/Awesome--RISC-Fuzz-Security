# Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledge

## 基本信息

- 作者：Wyatt Benno、Alberto Centelles、Antoine Douchet、Khalil Gibran
- 发表日期：2026-02-19
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=7）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：strong phrase in abstract: memory consistency verification；hardware/processor object: cpu, memory consistency；verification/fuzzing method: verification
- 论文页面：[http://arxiv.org/abs/2602.17452v1](http://arxiv.org/abs/2602.17452v1)
- PDF：[https://arxiv.org/pdf/2602.17452v1](https://arxiv.org/pdf/2602.17452v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 21 页，提取 48376 字符

## 摘要

We present Jolt Atlas, a zero-knowledge machine learning (zkML) framework that extends the Jolt proving system to model inference. Unlike zkVMs (zero-knowledge virtual machines), which emulate CPU instruction execution, Jolt Atlas adapts Jolt's lookup-centric approach and applies it directly to ONNX tensor operations. The ONNX computational model eliminates the need for CPU registers and simplifies memory consistency verification. In addition, ONNX is an open-source, portable format, which makes it easy to share and deploy models across different frameworks, hardware platforms, and runtime environments without requiring framework-specific conversions. Our lookup arguments, which use sumcheck protocol, are well-suited for non-linear functions -- key building blocks in modern ML. We apply optimisations such as neural teleportation to reduce the size of lookup tables while preserving model accuracy, as well as several tensor-level verification optimisations detailed in this paper. We demonstrate that Jolt Atlas can prove model inference in memory-constrained environments -- a prover property commonly referred to as \textit{streaming}. Furthermore, we discuss how Jolt Atlas achieves zero-knowledge through the BlindFold technique, as introduced in Vega. In contrast to existing zkML frameworks, we show practical proving times for classification, embedding, automated reasoning, and small language models. Jolt Atlas enables cryptographic verification that can be run on-device, without specialised hardware. The resulting proofs are succinctly verifiable. This makes Jolt Atlas well-suited for privacy-centric and adversarial environments. In a companion work, we outline various use cases of Jolt Atlas, including how it serves as guardrails in agentic commerce and for trustless AI context (often referred to as \textit{AI memory}).

## 研究问题

如何将零知识证明技术应用于机器学习推理，以实现在资源受限设备上可验证且保护隐私的推理，同时克服传统zkVM在非线性和大张量运算上的高开销。

## Introduction 梳理

现有zkML框架（如EZKL、Bionetta、DeepProve）在处理非线性和大张量运算时效率低下（EZKL的非线性运算开销高，Bionetta依赖可信设置且不支持通用ONNX，DeepProve的GKR协议对矩阵乘法存在常数因子开销）。Jolt Atlas通过将Jolt的查找表证明范式适配到ONNX张量计算，规避了CPU寄存器和任意内存访问，简化了内存一致性验证，并利用sumcheck协议实现了流式prover。贡献包括：用ONNX图替代RISC-V指令集、张量级直接验证、使用HyperKZG替换Dory以减少承诺开销。

## 方法

{'DUT_platform': 'Jolt Atlas证明系统，在Apple M3 MacBook Pro上运行', 'feedback_coverage': '不适用（zkML框架无反馈驱动测试）', 'golden_model': '不需要golden model，证明过程验证了模型计算正确性', 'input_generation': 'ONNX模型和输入数据生成执行轨迹，记录每一步操作、源/目标张量地址和值，轨迹填充到2的幂次', 'oracle': '正确性通过零知识证明的sumcheck和查找表参数的一致性保证'}

## 实验与评估

{'artifact': '未确认（仅提及companion work，未说明是否开源）', 'baseline': 'ezkl（同一nanoGPT模型，报告数据来自ezkl博客）', 'bug_CVE': '未报告', 'experiment_budget': 'MacBook Pro (Apple M3) 16GB RAM', 'overhead': '证明时间相对ezkl提速17倍，但未提供内存开销对比', 'statistics': 'nanoGPT: 证明时间14s (ezkl 237s)，验证时间0.517s，密钥生成0.246s；GPT-2 (125M): 端到端证明~38s'}

## 核心贡献

1) 将Jolt的查找表证明范式扩展到ONNX张量计算，消除CPU寄存器和内存一致性开销；2) 通过前缀-后缀分解实现流式证明；3) 应用neural teleportation压缩查找表；4) 采用BlindFold实现零知识；5) 实验显示相比ezkl显著提速。

## 与本仓库研究主线的关系

不直接相关。论文主题是zkML，与多hart/内存一致性验证无关；仅方法上借鉴了Jolt的查找表证明和内存一致性技术（Twist and Shout），但本体不涉及RISC-V处理器或硬件fuzzing。

## 结论

Jolt Atlas实现了可验证的机器学习推理，在nanoGPT上比ezkl快17倍，支持流式证明，适合资源受限设备，但当前限于部分ONNX算子，且依赖HyperKZG（需配对，阻碍上链验证）。

## 局限性

算子支持有限（仅覆盖推理常用子集）；全局单侧neural teleportation引入近似误差；HyperKZG的配对操作不利于链上验证；未评估更大模型或不同证明系统的跨框架比较。

## 详细阅读分析

建议深入阅读Section 4（查找表证明的流式实现）和Section 6（基准测试）以借鉴其证明系统设计思路，但对处理器验证无直接指导。

## 后续核验问题

- Jolt Atlas的流式证明能否适配到RISC-V处理器的指令级验证？
- 该框架的查找表分解技术如何与Twist and Shout结合用于多核一致性协议测试？
- ONNX图中张量操作的验证方法能否泛化到SoC总线的数据流验证？
