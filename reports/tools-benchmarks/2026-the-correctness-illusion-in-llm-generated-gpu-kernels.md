# The Correctness Illusion in LLM-Generated GPU Kernels

## 基本信息

- 作者：Dipankar Sarkar
- 发表日期：2026-06-18
- 更新日期：2026-07-21
- 来源：arXiv
- 来源编号：2606.20128v1
- 研究类别：Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-22
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2606.20128v2](http://arxiv.org/abs/2606.20128v2)
- PDF：[https://arxiv.org/pdf/2606.20128v2](https://arxiv.org/pdf/2606.20128v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

Benchmarks for LLM-generated GPU kernels (KernelBench, TritonBench, GEAK) score correctness through fixed-shape, small-sample allclose-style checks. The number of inputs varies between benchmarks. The shape, dtype, and tolerance are fixed for each kernel. We test that oracle empirically. We construct a controlled corpus of 24 Triton and CPU stand-in kernels (15 correct controls and 9 LLM-style buggy variants seeded with documented transcription errors) and re-evaluate it under op-schema-aware seeded fuzzing with a high-precision (fp64) CPU reference and per-(op, dtype) absolute tolerances. The seeded oracle flags 9 of 9 buggy kernels and passes 15 of 15 correct controls, at zero precision cost on controls. We extend the corpus to 26 ops (adding a flash-attention pair) and re-run the same protocol on five GPU classes (RTX 3060, A10, L40S, A100 SXM4, H100 NVL). The verdicts are identical across all five GPUs: 10 of 10 illusions caught and 16 of 16 controls clean. The corpus result is about LLM-style transcription bugs that the allclose-on-one-shape oracle certifies as correct, not about the bug rate of any specific deployed LLM. Every flagged failure replays byte-for-byte from a stored seed.

## 研究问题

现有LLM生成GPU内核的基准测试（KernelBench、TritonBench、GEAK）通过固定形状、小样本的allclose-style检查来评判正确性，但该检查存在系统性乐观偏差，无法检测LLM式的转录错误，导致产生“正确性幻觉”。

## Introduction 梳理

现有基准测试在评判LLM生成GPU内核正确性时，采用固定形状、固定数据类型和手动设定的容忍度，这种单一测试方式会漏掉许多真实错误。本文构造了一个包含24个内核的语料库（15个正确控制组和9个LLM式错误变体），通过op-schema-aware种子模糊测试和高精度fp64参考预言机重新评估，以揭示这种幻觉。

## 方法

方法包括三个核心部分：（1）op-schema-aware模糊测试：每个内核声明一个模式，包含共享符号维度及其候选值（包括边界值），模糊器根据主种子推导出每个测试用例的确定性形状，从而覆盖操作的真实输入域。（2）参考预言机：使用fp64 CPU参考计算，然后向下取整到目标数据类型，采用基于(op, dtype)的绝对容忍度进行比较，并检测NaN和Inf，记录完整的逐元素误差分布（最大绝对值、最大相对值、ULP百分位数等）。（3）语料库构建：最初24个操作，15个正确控制组和9个LLM式错误变体（如GELU缺少0.5、softmax尾部掩码错误、RMSNorm缺少sqrt等），随后扩展到26个操作（添加flash-attention对）用于跨GPU验证。所有测试通过可重复流水线运行，每个失败案例存储完整输入快照。

## 实验与评估

在RTX 3060上的单GPU评估中，种子预言机正确捕获了9个LLM式错误变体（其中4个为真实Triton GPU内核），15个正确控制组全部通过，零误报。扩展至26个操作并在5种GPU（RTX 3060、A10、L40S、A100 SXM4、H100 NVL）上进行跨GPU验证，结果完全一致：16个控制组通过，10个LLM式错误变体被捕获。错误分为两类：幅度均匀错误（如缺失缩放因子）几乎在所有形状下触发；形状敏感错误（如尾部掩码）仅在特定边界形状下触发，而边界形状不在常规测试中。

## 结论

LLM式的转录错误能够通过现有的固定形状、小样本allclose-style检查被错误地认证为“正确”。本文提出的op-schema-aware种子预言机成功揭示了这一差距，并提供了边界感知形状生成、基于(op, dtype)的绝对容忍度校准以及原则性输入生成等对策。这些对策易于集成到任何现有项目，可有效消除正确性幻觉。

## 局限性

1. 10个错误变体是作者人工植入的、文献中记载的LLM转录错误模式，并非直接从真实LLM输出中获取，因此本研究衡量的是哪些错误模式会被allclose-style检查遗漏，而非任何特定LLM的错误率。2. 预言机当前仅进行同数据类型比较（内核fp16与从fp64向下取整的参考fp16），跨数据类型比较（如内核fp16与参考fp64）是未来工作。3. Python客户端将接收张量解码为连续布局，因此非连续布局的模糊测试在客户端边界上是名义上的。4. bfloat16在Python客户端中受限于NumPy缺乏原生bf16类型，测试中代理为fp16。5. 高精度fp64参考经向下取整后作为正确性标准，不保证与特定库的字节一致。6. Triton内核每次运行重新编译，未控制ptxas随机性，但跨GPU验证表明不影响正确性判决。

## 详细阅读分析

本文的核心贡献在于系统性地揭示了LLM生成GPU内核验证中的正确性幻觉问题，并通过构造的语料库和模糊测试方法证实了该问题的存在。op-schema-aware形状生成是方法上的关键创新，它通过共享符号维度和边界候选集，使测试能够覆盖操作的完整输入域，从而暴露形状相关错误。采用绝对容忍度并基于(op, dtype)校准，避免了PyTorch allclose组合容忍度可能掩盖错误的风险。跨GPU一致性验证表明方法对硬件平台不敏感，增强了结果的可靠性。可重复性设计（每失败存储快照）确保了实验的可审计性。论文坦诚地讨论了局限性，尤其是错误变体的人工性质，并给出了合理理由：确保ground truth准确且针对已知威胁模型。这为进一步将方法应用于真实LLM输出提供了基准。

## 后续跟进问题

- 1. 如何将本文的模糊测试方法扩展到对真实LLM生成的大规模内核集（如KernelBench或GEAK的输出）进行自动评估，以测量实际错误率？2. 如何自动化校准每个(op, dtype)的绝对容忍度，使其既能捕获错误又避免假阳性？3. 本文的op-schema-aware模糊测试能否作为集成模块加入现有LLM内核基准测试中，取代原有的allclose检查？4. 对于形状敏感错误，边界候选集的设计是否可以自动化生成或优化，而非手动选择？5. 预言机如何扩展到跨数据类型比较（例如内核fp16与fp64参考），以更好地检测混合精度问题？6. 该模糊测试框架是否可迁移到其他硬件平台（如AMD GPU或CPU）？
