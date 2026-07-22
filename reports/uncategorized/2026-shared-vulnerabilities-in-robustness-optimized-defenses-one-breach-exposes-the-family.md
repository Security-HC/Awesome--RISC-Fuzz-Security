# Shared Vulnerabilities in Robustness-Optimized Defenses: One Breach Exposes the Family

## 基本信息

- 作者：Hanrui Wang、Ruihao Zheng、Shuo Wang、Isao Echizen、Xingbo Dong、Zhe Jin
- 发表日期：2026-07-20
- 更新日期：2026-07-20
- 来源：arXiv
- 来源编号：2607.18339v1
- 研究类别：未分类
- 首次发现：2026-07-22
- 最近更新：2026-07-22
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2607.18339v1](http://arxiv.org/abs/2607.18339v1)
- PDF：[https://arxiv.org/pdf/2607.18339v1](https://arxiv.org/pdf/2607.18339v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

Adversarial robustness optimization aims to preserve correct prediction under adversarial perturbations, and has produced substantial robustness gains through methods such as adversarial training and adversarial purification. However, we identify a new security risk: these gains can create shared vulnerabilities across defenses. Once one representative robustness-optimized defense is effectively breached, the broader family may become exposed. Studying this risk requires separating genuine transferability from distortion-induced degradation and from the algorithmic gains of sophisticated attacks. We therefore introduce stricter transfer-only protocols and a deliberately simple adaptive attack, PGDTransfer, to test whether robustness-optimized defenses share transfer-only vulnerability under controlled conditions. We further introduce Adversarial Sensitivity Maps (AdvSMs) to visualize and quantify shared alignment beyond differentiable classifiers, including stochastic and non-differentiable defenses. Across adversarially trained classifiers, purification-based defenses, and LVLMs with robust visual encoders, we identify natural transferability within each robustness family, i.e., transfer that arises even with simple PGD-style optimization rather than specialized transferable-attack design. The risk is already severe for purification: PGDTransfer reaches an average transfer attack success rate of $80.4\%$ across filtering-, compression-, and diffusion-based purifiers under $ε=4/255$, suggesting that purifier defenses may no longer provide reliable protection. As attacks improve, currently stronger robustness families may face the same risk. Future defenses should therefore treat vulnerability diversity and transfer-only isolation as security objectives, rather than optimizing only individual robustness.

## 研究问题

鲁棒性优化防御（如对抗训练和净化）虽然提升了单个模型的鲁棒性，但可能引入共享漏洞：一旦一个代表性防御被有效攻破，整个同族防御（同一任务和鲁棒性优化目标）可能被暴露。这种共享漏洞导致防御隔离风险，即攻击者可通过一个公开的代理防御生成对抗样本，无需目标梯度、查询或自适应就能攻击私有防御。

## Introduction 梳理

对抗攻击对模型鲁棒性构成严重威胁，已发展出多种防御方法，如对抗检测、对抗训练和对抗净化。本文关注鲁棒性优化（旨在对抗扰动下保持正确预测）的防御，认为这些防御可能产生共享的对抗敏感性，导致三个部署风险：①公共代表防御可能暴露私有系统；②防御随机化可能失效；③当前鲁棒防御可能被未来更强攻击突破。现有研究存在三个空白：①常用协议使用大扰动预算（如16/255）导致失真驱动的过估计；②复杂攻击难以分离算法增益与自然迁移性；③缺乏超越攻击成功率的共享漏洞证据。本文贡献：①提出更严格的传输协议（小预算非目标传输、目标传输、鲁棒性不匹配传输、干净正确子集）；②提出简单自适应攻击PGDTransfer，仅用PGD+EOT+适当代理，验证同族防御间的自然迁移性；③提出对抗敏感性图（AdvSMs），用于可视化和量化不可微或随机防御的共享对齐。

## 方法

本文方法包括三个部分：第一，严格的传输协议，包括小预算非目标传输（ℓ∞=4/255）、目标传输、鲁棒性不匹配传输（同架构鲁棒与非鲁棒模型之间）、干净正确子集评估，以排除失真驱动和架构驱动的过估计。第二，PGDTransfer攻击，一种故意简单的自适应攻击，使用PGD优化、EOT平均和适当代理（如DDIM用于净化防御），在无目标自适应的情况下测试迁移性。第三，对抗敏感性图（AdvSMs），通过输入空间上的局部扰动敏感性度量，可视化并量化不同防御（包括随机和非可微）的共享对齐程度。

## 实验与评估

实验在三个鲁棒性家族上进行：对抗训练分类器（ResNet-50、ConvNeXt-B、ViT-B、Swin-B等）、净化防御（基于滤波、压缩、扩散的八种方法）和具有鲁棒视觉编码器的LVLM（VQA任务）。使用PGDTransfer攻击，在严格协议下（ϵ=4/255非目标传输）观察到显著迁移性：净化防御的平均传输成功率（TASR）达80.4%，表明净化防御可能不再可靠。对抗训练分类器间也有强迁移，但LVLM中鲁棒编码器间迁移较弱。AdvSMs显示同族防御具有对齐的敏感性，而跨族非鲁棒防御则不明显。

## 结论

鲁棒性优化虽然提升了单独鲁棒性，但削弱了防御隔离：同族防御共享漏洞，一个代表防御被攻破则整个家族暴露。未来防御应将漏洞多样性和传输隔离作为安全目标，而非仅优化个体鲁棒性。

## 局限性

①仅研究同一防御家族内的迁移，未探索跨家族（如对抗训练到净化）的共享漏洞。②攻击方法PGDTransfer虽简单，但可能无法代表未来更强攻击；更复杂的攻击可能进一步放大风险。③评估局限于特定任务（分类、VQA）和模型架构，泛化到其他模态或任务需验证。④AdvSMs的量化指标未与传输成功率建立严格因果关系，仅提供可视相关性。⑤实验仅在有限预算（ϵ=4/255）下进行，更大预算下结果可能不同。

## 详细阅读分析

本文的核心洞察是鲁棒性优化可能创造‘家族级’漏洞：当多个防御系统向相似的鲁棒特征对齐时，它们的对抗敏感性会趋同，从而使单个代理攻击能高效迁移。这挑战了传统认知——鲁棒性提升通常被认为个体有益，但本文揭示其可能以牺牲系统多样性和隔离性为代价。PGDTransfer的简单性设计是关键：它排除了复杂攻击技巧的混淆，证明迁移性本身源于防御的内在特性而非攻击算法。AdvSMs通过局部梯度/不可微近似提供可视化证据，弥补了仅攻击成功率的不足。需要注意的是，实验中的‘净化防御’（如DiffPure）在代理（DDIM）和攻击设置下失效严重，提示当前主流的扩散净化可能面临根本性安全风险。

## 后续跟进问题

- 如何设计同时保持个体鲁棒性和家族内多样性的防御策略？
- 不同鲁棒性家族（如对抗训练与净化）之间是否存在潜在的共享漏洞？
- 本文提出的严格传输协议能否推广到其他攻击类型（如物理世界攻击）？
- 对抗敏感性图（AdvSMs）能否进一步量化漏洞严重程度并与攻击成功率建立解析关系？
- 对于LVLM，如何避免视觉编码器的鲁棒性优化导致下游推理一致被攻破？
