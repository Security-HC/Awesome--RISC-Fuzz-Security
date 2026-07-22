# Formalising CXL Cache Coherence

## 基本信息

- 作者：Chengsong Tan、Alastair F. Donaldson、John Wickerson
- 发表日期：2024-10-21
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=7）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：strong phrase in abstract: cache coherence protocol；hardware/processor object: cache coherence；verification/fuzzing method: verification
- 论文页面：[http://arxiv.org/abs/2410.15908v2](http://arxiv.org/abs/2410.15908v2)
- PDF：[https://arxiv.org/pdf/2410.15908v2](https://arxiv.org/pdf/2410.15908v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 14 页，提取 72239 字符

## 摘要

We report our experience formally modelling and verifying CXL.cache, the inter-device cache coherence protocol of the Compute Express Link standard. We have used the Isabelle proof assistant to create a formal model for CXL.cache based on the prose English specification. This led to us identifying and proposing fixes to several problems we identified as unclear, ambiguous or inaccurate, some of which could lead to incoherence if left unfixed. Nearly all our issues and proposed fixes have been confirmed and tentatively accepted by the CXL consortium for adoption, save for one which is still under discussion. To validate the faithfulness of our model we performed scenario verification of essential restrictions such as "Snoop-pushes-GO", and produced a fully mechanised proof of a coherence property of the model. The considerable size of this proof, comprising tens of thousands of lemmas, prompted us to develop new proof automation tools, which we have made available for other Isabelle users working with similarly cumbersome proofs.

## 研究问题

CXL.cache协议作为CXL标准中提供设备间缓存一致性的部分，其规范存在模糊、歧义和不准确之处，可能导致实现不一致。论文旨在形式化建模并验证该协议是否真正提供声明的缓存一致性，同时识别并修复规范中的问题。

## Introduction 梳理

CXL是一个新兴的工业标准，通过PCIe总线实现多设备间缓存一致性，有望提升数据中心性能。然而，CXL.cache协议规范庞大复杂，可能存在不一致性和歧义。既有工作如Oswald等人的ProtoGen和Hemiola DSL等，但尚未有对CXL.cache的完整形式化验证。论文的贡献包括：(1) 使用Isabelle proof assistant对CXL.cache进行形式化建模；(2) 通过场景验证和机械证明确认协议满足单写者多读者(SWMR)属性；(3) 开发super_sketch工具以加速大型归纳不变量的迭代开发。

## 方法

论文使用Isabelle proof assistant构建了CXL.cache协议的形式化模型，表示为状态转换系统。模型包括主机、两个设备、缓存行状态（稳定态和瞬态）、各类通道（请求、响应、数据）以及设备缓冲区。输入生成未涉及（模型手动构建）；反馈机制通过状态检查和转换规则实现；Oracle为SWMR属性及归纳不变量；DUT为CXL.cache协议模型；不需要golden model，因为正确性通过形式化证明来保证。

## 实验与评估

Baseline：无明确baseline。实验预算：未确认。统计：归纳不变量包含796个合取项，共68条转换规则，需证明53,332个引理；证明耗时约12人月；每个规则文件检查约1-2分钟，整个session构建需3-5小时。Bug/CVE：发现5个规范问题，其中4个已被CXL联盟确认并将在后续版本采纳，1个仍在讨论中。开销：证明了SWMR属性，但未包含数据值不变性。Artifact：Isabelle理论文件在GitHub公开。

## 核心贡献

1) 第一个完整的CXL.cache协议形式化模型（Isabelle）；2) 机械证明该模型满足单写者多读者（SWMR）属性；3) 开发super_sketch工具，实现大数据自动推理，降低归纳不变量迭代成本。

## 与本仓库研究主线的关系

直接相关。论文主题涉及多设备缓存一致性协议的形式化验证，直接对应多hart与内存一致性验证研究范畴。其形式化方法和自动化工具可借鉴于处理器验证和RISC-V一致性测试，但非硬件fuzzing或RTL级测试，而是更高层次的协议验证。

## 结论

论文成功形式化了CXL.cache协议并证明了其满足SWMR属性，从而为CXL设备间缓存一致性提供了部分形式化保证。建模过程中发现了规范中的模糊、冗余和潜在错误，多数已被CXL联盟接受。此外，开发了super_sketch工具，有效加速了大型归纳证明的迭代过程，可供其他Isabelle用户使用。

## 局限性

1) 仅证明了SWMR属性，未证明数据值不变性；2) 模型限于两个设备和一个内存位置，未覆盖多设备多位置场景；3) 省略了部分CXL.cache消息类型（如RdCurr、WrInv等）；4) 假设主机能完美跟踪设备状态，实际实现中可能不可行；5) 未考虑死锁、活性等性质。

## 详细阅读分析

需进一步阅读：第3节模型详细定义（状态和转换规则）；第4节规范问题及修复；第6节SWMR证明结构和归纳不变量设计；第7节super_sketch工具的工作原理和脚本生成。

## 后续核验问题

- 1) 如何将模型扩展至更多设备（>2）和多位置以获得更全面的验证？2) 能否将形式化模型转化为硬件fuzzing的oracle或覆盖率指导？3) super_sketch工具能否直接用于其他协议（如RISC-V一致性协议）的形式化？4) 模型中的完美假设如何通过更实际的跟踪机制（如bit-vector）来消除？
