# Accelerating Hardware Verification with Graph Models

## 基本信息

- 作者：Raghul Saravanan、Sreenitha Kasarapu、Sai Manoj Pudukotai Dinakarrao
- 发表日期：2024-12-17
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=7）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Benchmarks, Bug Injection & Artifacts
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: processor, rtl；verification/fuzzing method: fuzz, verification
- 论文页面：[http://arxiv.org/abs/2412.13374v2](http://arxiv.org/abs/2412.13374v2)
- PDF：[https://arxiv.org/pdf/2412.13374v2](https://arxiv.org/pdf/2412.13374v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 15 页，提取 92464 字符

## 摘要

The increasing complexity of modern processor and IP designs presents significant challenges in identifying and mitigating hardware flaws early in the IC design cycle. Traditional hardware fuzzing techniques, inspired by software testing, have shown promise but face scalability issues, especially at the gate-level netlist where bugs introduced during synthesis are often missed by RTL-level verification due to longer simulation times. To address this, we introduce GraphFuzz, a graph-based hardware fuzzer designed for gate-level netlist verification. In this approach, hardware designs are modeled as graph nodes, with gate behaviors encoded as features. By leveraging graph learning algorithms, GraphFuzz efficiently detects hardware vulnerabilities by analyzing node patterns. Our evaluation across benchmark circuits and open-source processors demonstrates an average prediction accuracy of 80% and bug detection accuracy of 70%, highlighting the potential of graph-based methods for enhancing hardware verification.

## 研究问题

门级网表硬件验证面临可扩展性问题：传统硬件模糊测试和形式化方法在门级效率低，无法有效检测综合引入的漏洞。

## Introduction 梳理

现有硬件模糊测试主要针对RTL级，无法捕获综合引入的bug；门级仿真速度慢，缺乏高效的自动化验证方法。本文提出GraphFuzz，首个基于图学习的门级网表模糊测试框架，通过图表示和循环神经网络加速验证，无需深入硬件设计知识。

## 方法

{'dut_platform': 'ISCAS基准电路（C5315、C7552、S13207、S5378）、IP外设（AES、DSP）、开源处理器ALU（Ariane、IBEX、Rocket、or1200、mor1kx）。平台：Cadence Genus综合，Cadence Xcelium仿真。', 'feedback_coverage': '使用图节点覆盖（度中心性、介数中心性、紧密中心性、特征向量中心性）以及EDA工具（Cadence Xcelium）的切换覆盖作为反馈。', 'golden_model_description': 'RTL设计作为黄金参考模型。', 'golden_model_required': True, 'input_generation': '将输入引脚位向量作为输入种子，通过AFL风格的变异引擎生成变异输入。', 'oracle': '以RTL设计作为黄金参考模型，并辅助使用商业EDA工具比较门级网表输出。'}

## 实验与评估

{'artifact': '未确认（论文未提供开源链接）。', 'baseline': '未与现有硬件模糊测试框架直接对比。', 'bugs_cves': '检测到：(1) mor1kx ALU进位标志错误，平均准确率70% (2) or1200 ALU溢出标志错误，平均准确率82.7% (3) 门延迟导致的错误（AES、DSP、or1200、mor1kx、Rocket、IBEX ALU），未量化具体准确率。未报告CVE编号。', 'experiment_budget': '48核Intel Xeon处理器，512GB RAM；NVIDIA T4 GPU用于训练。', 'overhead': '推理延迟：AES 1.64s, or1200 ALU 1.44s, mor1kx ALU 1.34s, 其他低于1s。内存消耗：AES 17MB, or1200 ALU 15MB, mor1kx ALU 12MB, 其他低于10MB。', 'statistics': {'accuracy': '表III显示各设计准确率：AES 92.42%, C5315 79.82%, DSP 70.25%, C7552 72.78%, S13207 76.85%, S5378 96.04%, IBEX ALU 79.69%, Rocket ALU 73.87%, or1200 ALU 83.14%, mor1kx ALU 69.37%, Ariane ALU 95.38%', 'precision_recall_f1': '见表III，各指标与准确率相近。'}}

## 核心贡献

['提出将门级网表建模为图（NetGraph）并编码门行为作为特征。', '设计图循环神经网络（GRNN）用于预测节点逻辑值，实现加速模糊测试。', '利用EDA工具生成训练数据集（逻辑值、切换覆盖）。', '实现NetGraph模糊测试器，基于图节点覆盖引导输入变异。']

## 与本仓库研究主线的关系

直接相关（RTL/SoC硬件Fuzzing），侧重门级网表验证。方法借鉴图学习，但未涉及多hart或内存一致性验证。

## 结论

GraphFuzz是首个基于图学习的门级网表硬件模糊测试框架，能够加速验证并检测实际bug（如进位/溢出标志错误和门延迟问题）。

## 局限性

['依赖RTL或门级网表的访问。', '当前图模型未编码时序特性，无法检测时序漏洞。', '无法完全检测某些合成优化引入的漏洞（如合并顺序实例、取消层次分组），需结合EDA工具。']

## 详细阅读分析

True

## 后续核验问题

- 如何将时序特性（如门延迟）融入图模型？
- 与RTL级模糊测试（如TheHuzz）相比，GraphFuzz在bug检测准确率或性能上的优势如何？
- 能否扩展到检测多hart竞争条件或内存一致性错误？
