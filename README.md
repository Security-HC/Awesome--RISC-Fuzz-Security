# Awesome--RISC-Fuzz-Security

面向 RISC-V、处理器、微架构、硬件 Fuzzing 与安全验证方向的定期论文自动收集和中文阅读整理仓库。

## 表格入口

自动生成的中文论文分类表格在 [reports/README.md](reports/README.md)。

机器可读原始数据在 [data/papers.json](data/papers.json)，它是 JSON 数据库，不会显示成表格。

`reports/` 下会按研究类型建立子目录，例如：

- `reports/risc-v-fuzzing/`
- `reports/processor-cpu-fuzzing/`
- `reports/microarchitecture-security/`
- `reports/rtl-hardware-verification/`
- `reports/fuzzing-methodology/`
- `reports/tools-benchmarks/`

## 输出内容

GitHub Action 每 3 天自动运行并更新：

- [reports/README.md](reports/README.md)：按研究类别划分的中文论文总表
- `reports/<研究类别>/README.md`：单个类别下的中文论文表格
- `reports/<研究类别>/*.md`：每篇论文的中文详细阅读记录
- [data/papers.json](data/papers.json)：累计论文元数据、分类和分析状态

每篇论文详情页包含：

- 基本信息和可点击论文链接
- 研究问题
- Introduction 梳理
- 方法
- 实验与评估
- 结论
- 局限性
- 详细阅读分析
- 后续跟进问题

## 定期运行时间

工作流默认每 3 天在北京时间 09:00 左右运行一次：

```yaml
cron: "0 1 */3 * *"
```

GitHub Actions 的 cron 使用 UTC，因此 `01:00 UTC` 对应北京时间 `09:00`。这里的 `*/3` 表示每月日期为 1、4、7、10、13、16、19、22、25、28、31 日时运行；跨月时不是严格每 72 小时，但可以有效降低检索频率。

也可以在 GitHub Actions 页面通过 `workflow_dispatch` 手动运行。

## API Key 设置

如果使用 OpenAI，在仓库 Secret 中添加：

```text
OPENAI_API_KEY
```

如果使用 DeepSeek，在仓库 Secret 中添加：

```text
DEEPSEEK_API_KEY
```

如果没有配置 API Key，工作流仍会抓取论文，并基于题名和摘要生成中文记录；配置 API Key 后会尝试读取 PDF 正文并生成更完整的中文全文分析。

默认每次运行最多对 3 篇论文做 LLM 分析，避免一次任务运行过久。默认关闭 PDF 全文下载，使用标题、摘要和元数据生成中文阅读记录；如需开启全文 PDF 分析，可以在 workflow 中把 `ENABLE_FULL_TEXT_ANALYSIS` 改为 `"true"`。

## 检索范围

默认检索范围包括：

- RISC-V fuzzing
- processor fuzzing
- CPU fuzzing
- microarchitecture fuzzing
- hardware fuzzing
- ISA testing
- instruction set fuzzing
- RTL fuzzing
- SoC verification
- transient execution fuzzing
- cache side channel fuzzing

可以编辑 [config/search_queries.json](config/search_queries.json) 和 [config/categories.json](config/categories.json) 来调整关键词和研究类别。

## 查重机制

脚本在生成报告前会自动查重。只要下面任一字段命中已有记录，就认为是同一篇论文：

- arXiv 或其他来源编号
- 归一化后的标题
- 论文页面 URL
- PDF URL

如果同一篇论文每天被重复检索到，但元数据没有变化，脚本不会重写记录，也不会制造无意义的每日提交。元数据中会保留 `first_seen`、`last_seen`、`seen_count` 和 `content_hash` 便于追踪。
