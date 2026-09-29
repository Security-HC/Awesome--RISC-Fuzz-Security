# Self-Verifying Anomaly Detection using Explainable AI for Cybersecurity of DER Networks

## 基本信息

- 作者：Damilola Popoola、Souradeep Bhattacharya、Manimaran Govindarasu
- 发表日期：2026-09-11
- 会议/期刊：arXiv
- 主分类：形式化与定向处理器验证
- 相关性：B·强邻近（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: soc；verification/fuzzing method: verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2609.12305v1](http://arxiv.org/abs/2609.12305v1)
- PDF：[https://arxiv.org/pdf/2609.12305v1](https://arxiv.org/pdf/2609.12305v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 5 页，提取 24444 字符

## 摘要

The rapid growth of Distributed Energy Resources (DERs) has significantly expanded the cyber attack surface of modern power grids. Furthermore, increasing sophistication in attack techniques demands anomaly detection systems (ADS) that are accurate, interpretable, and reliable to support DER cybersecurity. While ML-based ADS provide strong detection capabilities, their black-box nature reduces operator trust and limits Security Operation Center's (SOC) ability to effectively interpret alerts and respond, highlighting the need for explainable Artificial Intelligence (XAI) to ensure transparency and operational confidence. This paper presents an XAI-based anomaly detection framework tailored for DER networks (ExCYDER). The proposed framework uses a self-verifying mechanism that validates ADS alerts to ensure trustworthy decision-making. ExCYDER combines LightGBM with SHAP to check whether each model decision aligns with its feature-attribution evidence, allowing the system to confirm that its internal reasoning is consistent and reliable. Experiments on a realistic DNP3 dataset achieved over 98% detection accuracy, an average rule--SHAP consistency of 44.6%, a SHAP latency of 14.5 ms per alert, and a confidence deviation within 5%, demonstrating stable verification behavior with minimal computational overhead. The framework distinguished between coherent and inconsistent alerts without compromising detection accuracy, demonstrating that integrated verification within XAI-based ADS enhances interpretability, auditability, and operational robustness for DER-focused SOCs.

## 研究问题

DER 网络快速接入扩大攻击面；基于 ML/DL 的异常检测系统（ADS）虽检测能力强但黑箱特性降低 SOC 操作员信任，限制告警解释与响应；现有 XAI 多为 post hoc 解释，可能不一致或与模型行为错位，缺少对解释/决策一致性的验证。论文要解决的是：为 DER 网络构建可解释、可自验证、适合 SOC 的异常检测框架，使每个告警在展示前经过规则—特征归因一致性校验。

## Introduction 梳理

研究缺口：传统边界防御对自适应威胁失效；ML/DL ADS 高精度但不可解释；XAI 可提升透明度，但作者主张“仅有解释不够”，还需验证解释是否忠实。既有方法不足：LIME/SHAP 等仅提供事后解释，不验证模型内部推理一致性；SOC 需要快速可靠地分诊告警。论文贡献（作者明确声称）：(1) 面向 DER SOC 的集成学习 ADS 与可解释机制；(2) 解释驱动的验证流程，通过规则—特征一致性分析校验模型决策，提升透明、置信与可审计性；(3) 使用真实 DER 数据集进行实时 testbed 评估，展示检测准确率、验证稳定性和可解释性。注意：检测模型与部分性能来自前期工作 [7]，本文主要新增验证机制与集成评估。

## 方法

输入生成：不是 fuzzing；使用 Iowa State University DER DNP3 数据集 [18] 的带标签 DNP3 通信记录，三个虚拟 DER 设备在 Python 3.13/Apple M4 上实时回放流量。反馈/coverage：无硬件 fuzzing coverage；以 rule–SHAP consistency 作为验证信号，无代码覆盖率反馈。Oracle：云层验证器，将 LightGBM 提取的决策规则（claim）与 SHAP top-K 特征归因（evidence）交叉校验，计算 Overlap O、Direction D、Coverage C，Cons=w_ov O+w_dir D+w_cov C；并与基础置信度混合 p_hat=αp+(1-α)·100·Cons；Cons≥θ（θ=50%）为 verified，否则 unverified。DUT/平台：边缘智能层执行 ML 推理并每 60 秒聚合 JSON 告警批次；云智能层进行验证、关联与可视化（SOC dashboard，Streamlit/RSS 等指标）。三层 DER 架构沿用 CySIDER [7]。是否需要 golden model：无传统 golden model；规则路径与 SHAP 互为一致性参照，属于启发式自校验而非形式化证明。模型：LightGBM（选用依据前期工作 [7]；对比 XGBoost、Random Forest）。预处理：标签编码、特征选择、Min–Max 归一化、SMOTE，70% 训练/30% 测试。

## 实验与评估

Baseline：检测侧对比 LightGBM、XGBoost、Random Forest，但该结果被表述为前期工作 [7] 已建立；验证侧未提供与其他 XAI 一致性/验证方法的 baseline。预算：250 个 DER 通信样本，7 分钟；121 个恶意事件（DNP3 Stealthy、DoS、Replay）；按 60 秒聚合为 7 个 JSON 批次；θ=50%。统计：报告均值/百分比，未确认置信区间、显著性检验或多轮重复。结果：摘要称检测准确率 >98%；前期工作报告 LightGBM Precision/Recall/F1 >99%，FNR 0.51%，XGBoost FNR 0.88%，Random Forest FNR 5.10%。本文验证：平均 rule–SHAP consistency 44.6%，验证成功率 54.5%，失败率 45.5%，置信度偏差在 ±5% 内，SHAP 平均 14.5 ms/告警，ingest latency <10 s，rerun 间隔 60 s，CPU <70%，RSS <900 MB。Bug/CVE：未发现新 bug 或 CVE；仅引用 [19] 关于逆变器层漏洞（DNP3 Stealthy、DoS、Replay）作为威胁场景。开销：SHAP 14.5 ms/告警，CPU、内存和 ingest 指标表明轻量。Artifact：未确认代码或 artifact 发布；数据集来自公开 GitHub [18]。注意：摘要的 >98% detection accuracy 与正文“前期工作 [7]”的高性能表述需要区分；平均一致性 44.6% 低于阈值 50% 但成功率 54.5%，正文未解释该分布矛盾。

## 核心贡献

提出 ExCYDER：面向 DER SOC 的 XAI 自验证异常检测框架。具体：a) 边缘—云分层工作流，边缘用 LightGBM 做实时异常检测并生成告警，云端进行验证与可视化；b) 将 LightGBM 决策规则与 SHAP 特征归因结合，定义 Overlap、Direction、Coverage 三项规则—SHAP 一致性指标；c) 用一致性分数混合置信度，并按阈值 θ 将告警标记为 verified/unverified，以支持 SOC 分诊与审计；d) 在 DNP3 数据集和 testbed 上报告检测、验证与运行时开销。作者声称该机制不牺牲检测准确率即可区分一致与不一致告警。

## 与本仓库研究主线的关系

仅方法借鉴/邻近度很低，甚至可视为主题不相关。该文不涉及 RISC-V、处理器 Fuzzing、多 hart、内存一致性、微架构安全自动测试或 RTL/SoC 硬件 Fuzzing；DUT 是 DER 网络流量与 ML 异常检测器，不是处理器或 RTL。对 repo 的可能借鉴点仅在“Oracle/自验证”层面：用规则路径与特征归因的一致性作为告警可信度信号，类似为硬件 fuzzing 设计交叉检查 oracle 的思路。但它没有硬件覆盖率、没有 RTL 故障注入、没有多 hart/一致性路径实验。与多 hart/一致性路径研究的关系：无直接关系；不能作为多 hart 验证或一致性 oracle 的证据。主分类“Formal & Directed Processor Verification”应视为误分类。

## 结论

作者结论：ExCYDER 将高精度 ML 检测与可解释、可验证推理结合，把 post hoc 解释转变为可操作、可审计的 SOC 情报；内部验证可减少冗余或低置信告警，支持透明分诊并增强分析员信任。未来工作：在真实 DER 网络中部署以评估性能、时延和扩展性；开发交互界面融合操作员经验与 AI 洞察，改善人机协作与威胁情报。注：真实部署、扩展性、人机界面均为未来工作，不是本文已验证结论。

## 局限性

1) 实验规模小：250 样本、7 分钟、3 个虚拟设备、7 个批次，未做生产网络部署。2) 检测性能主要依据前期工作 [7]，本文不是独立重新训练/全面复现。3) 验证侧缺少 baseline 与消融：未与 LIME、Anchors、其他 faithfulness 指标或人工审查比较。4) 一致性指标 O/D/C 的权重、top-K、α、θ=50% 的选取依据未充分说明；θ 接近平均一致性 44.6%，且成功率 54.5% 未解释。5) 无统计显著性、置信区间、多次重复实验。6) 无新 bug/CVE 发现，未证明能发现未知攻击或对抗性规避。7) 无 artifact/代码发布确认。8) 分类问题：论文属于电力 DER 网络安全与 XAI，不是处理器/RISC-V/多 hart/一致性验证；主分类“Formal & Directed Processor Verification”与内容不符。

## 详细阅读分析

细读要点：1) 该文核心不是形式验证，而是把 SHAP 事后解释与 LightGBM 决策规则做一致性打分；所谓 self-verifying 是启发式检查，不提供形式化 soundness 或完备性保证。2) 方法链条：DNP3 标注流量→预处理/特征选择/SMOTE/70-30 划分→LightGBM 检测→边缘每 60 s 聚合 JSON→云端提取规则与 SHAP top-K→O/D/C 一致性→置信度混合→θ=50% 验证→SOC dashboard。3) 验证指标含义：success rate 是 Cons≥θ 的比例；failure 是低于阈值的比例；confidence deviation 衡量验证前后置信度变化；SHAP time 是解释开销。4) 结果异常：平均 consistency 44.6% 低于阈值 50%，但 success rate 54.5%，说明一致性分布可能偏斜或统计口径不同；正文未解释。5) 检测指标主要来自 [7]：LightGBM >99% P/R/F1，FNR 0.51%；本文摘要写 >98% accuracy，需区分来源。6) 威胁场景引用 [19] 的逆变器层漏洞，未做新漏洞发现。7) 复现信息：数据集 [18] 公开；代码/artifact 未确认；环境为 Apple M4/macOS/Python 3.13，非生产 DER 硬件。

## 后续核验问题

- 1) ExCYDER 的 O/D/C 权重、top-K、α 和 θ=50% 如何选取？是否做过敏感性分析？2) 平均一致性 44.6% 低于阈值，为何验证成功率 54.5%？3) 校验失败（unverified）的告警中真是假阳性/假阴性比例如何？是否提升安全决策而非仅减少告警？4) 与 LIME、Anchors、SHAP-based faithfulness、人工审查的 baseline 对比如何？5) 对抗条件下，攻击者能否操纵 SHAP 或规则路径使不一致告警通过验证？6) 该“自验证”模式能否借鉴到 RTL/处理器 fuzzing 的 oracle 设计中，例如让覆盖反馈与规格断言交叉验证？7) 多 hart/内存一致性验证中，是否可用类似的 claim-evidence 一致性度量？8) 真实 DER 生产网络与时延/扩展性测试是否已完成？9) 是否发布代码/artifact 以支持复现？10) 论文为何被归入 Formal & Directed Processor Verification，是否存在分类错误？
