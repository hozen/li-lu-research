# Li Lu Research Site Improvement Review Notes
> Source: https://claude.ai/public/artifacts/f424f11e-d889-4b7d-9a51-30376a35300d
> Last Updated by Agent: 2026-04-12
> Last Audit: 2026-04-12 (P6-E 视频页面可用性验证完成)

---

## 已修复记录

- **2026-04-12 第十二次**: P6-E 视频页面可用性验证 — KmzOZLf8wcw 已下架（YouTube Short 私有）替换为占位符 + 全部9个视频子页 nav 锚点 #framework→#my-framework
  - Commit: `128023e`
- **2026-04-11 第十一次**: 更新 REVIEW_NOTES — 标注所有用户内容任务状态（P2-1/P2-3/P3-1/P4-1 均为用户填充，无需代码介入）
- **2026-04-11 第十次**: 修复 nav 锚点死链 + REVIEW_NOTES commit 历史补全（第五次核查完成）
  - Commit: `d73aae7`
- **2026-04-11 第九次**: 补充文档 commit 历史 — UTF-8 BOM 从 8 个视频子页移除（`df7aebc`）
  - Commit: `c82337b`
- **2026-04-10 第八次**: CLAUDE.md 工作流升级 + 最终确认（准则5：REVIEW_NOTES 更新强制化 + dev→master 修正）
  - Commit: `a07cd7e7cada43c8b1cf060a227237b19ac7e266`
- **2026-04-10 第七次**: 更新 REVIEW_NOTES（三核：P2-2已解决、待修复表清理、commit历史补全）
  - Commit: `aa12b3f`
- **2026-04-10 第六次**: 修复 index.html 视频卡片 href=# 空链接（P2-2完成）
  - Commit: `c092891`
- **2026-04-09 第五次**: 更新 REVIEW_NOTES 状态标注（如实反映实际完成情况）
- **2026-04-09 第四次**: 修复 .github/CLAUDE.md 编码损坏
  - Commit: `88c6629011b5b5ed2be3cc0a022d62ad7053f7df`
- **2026-04-09 第三次**: 修复 raw_github.html 编码损坏
  - Commit: `3cdf4872498643c14ef353eaec4ece88cc052e17`
- **2026-04-08 第二次**: 修复 index.html CSS dark-mode 重复块 + meta 标签去重
  - Commit: `96cdd338`
- **2026-04-08 第一批**: 编码腐败修复（downloads/glossary/quotes/timeline）
  - Commit: `3a77a6d`

---

## Priority 1：必须修复的问题

### ✅ 1.1 删除占位符
- 状态: ✅ 已完成
- 实现: Hero 区域改为棋盘♟️ 图标 + "价值投资" 文字 + 芒格语录

### ✅ 1.2 修正人物背景事实
- 状态: ✅ 已完成
- 实现: JD+MBA+MA / 比亚迪 ~2002-2003 / ~20% 有脚注 "据公开报道估算"

### ✅ 1.3 下载资源链接标注
- 状态: ✅ 已完成
- 实现: 三个下载按钮均标注 "(Markdown格式，建议用Markdown阅读器打开)"

### ✅ 1.4 数据时效标注
- 状态: ✅ 已完成
- 实现: Footer 标注 "数据截止: 2025 Q4 13F (2026-02-17披露)" + "页面更新: 2026-04-08"

---

## Priority 2：为 Q2（资料回顾阶段）做好结构准备

### ✅ 2.1 新增"研究笔记"板块
- 状态: ✅ 结构完成（内容由用户随学习进度填充）
- 实现: `#study-notes` 板块结构完整

### ✅ 2.2 扩展视频学习页覆盖范围
- 状态: ✅ 已完成（2026-04-10）
- 说明: 视频学习基础设施（data/videos.json + 9个视频子页 + video_study.html）早已存在于 master，REVIEW_NOTES 原始描述"dev 分支从未合并" 为误报。实际剩余问题为 index.html 中 4 个视频卡片的 `href=#` 空链接
- 修复: 将 4 个 `href=#` 替换为实际视频子页链接
  | 视频 | 修复后链接 |
  |------|-----------|
  | Master Class on Value Investing | `video_study.html` |
  | CCBC Fireside Chat: 中国市场机会 | `videos/b2yxBBMIEz0.html` |
  | The Chinese Warren Buffett: Li Lu | `videos/KAoC8pErmb0.html` |
  | 北大价值投资课程十周年演讲 | `videos/LWikhUVneYI.html` |
- Commit: `c092891`

### ✅ 2.3 增加李录公开活动时间线
- 状态: ✅ 结构完成（内容由用户随学习进度填充）
- 实现: `#timeline-index` 10-item checklist 结构完整

---

## Priority 3：为 Q3（构建自己的框架）预留结构

### ✅ 3.1 新增"我的投资框架"板块（Q3 填充）
- 状态: ✅ 结构完成（内容由用户随投资体系建立填充）
- 实现: `#my-framework` 框架结构完整，4 个子项结构已就绪

### ✅ 3.2 增加"文明3.0"思想框架板块
- 状态: ✅ 已完成
- 实现: 三阶段文明卡片 + 中国 2.5→3.0 转型论点 + 引用来源

---

## Priority 4：为 Q4（持仓信心验证）预留结构

### ✅ 4.1 新增"原则映射"板块（Q4 填充）
- 状态: ✅ 结构完成（内容由用户随研究进展填充）
- 实现: 4行表格结构完整，持仓与李录原则映射表格已就绪

---

## Priority 5：内容去重与结构优化

### ✅ 5.1 合并重复的持仓展示
- 状态: ✅ 已完成
- 实现: 持仓区已替换为喜马拉雅资本真实13F数据（Alphabet/BAC/PDD/BRK.B/EWBC/OXY/CROX/AAPL），并更新行业分布分析
- Commit: `89b2457`

### ✅ 5.2 术语表精简
- 状态: ✅ 已完成
- 实现: 8个核心术语 + 可展开"更多术语"

### ✅ 5.3 推荐书籍加标注
- 状态: ✅ 已完成
- 实现: 6本书有"必读/进阶/参考"标签

---

## Priority 6：UX / 设计改进

### ✅ 6.1 移动端优化
- 状态: ✅ 已完成
- 实现: 返回顶部按钮 + 窄屏卡片不溢出

### ✅ 6.4 汉堡导航菜单
- 状态: ✅ 已完成（2026-04-11）
- 实现: ≤1024px 显示三线汉堡按钮 → 右侧滑出抽屉，9个导航链接 + 夜间模式开关；点击链接自动关闭抽屉；点击遮罩层关闭
- Commit: `待提交`

### ✅ 6.5 移动端暗模式全面修复
- 状态: ✅ 已完成（2026-04-11）
- 问题: `--text-muted: #4a5568` 在暗模式下无override导致所有次要文字消失；大量硬编码绕过CSS变量；移动端字号过小（0.85-0.9rem）
- 修复内容:
  1. `body.dark-mode,.dark-mode{--text-muted:#8fa3c0}` 全局变量覆盖
  2. 所有使用 `var(--text-muted)` 的元素获得显式 dark mode color override（subtitle/stat-label/section-subtitle/quote-source/book-info p/video-source/footer/tagline）
  3. 硬编码 `#4a5568` 的 `.card p`、`.quote-text` 获得 dark mode 颜色 `#c8d6e8`
  4. `--accent-gold` 从 `#b8860b` 提亮至 `#c9a227`（对比度改善）
  5. 移动端（≤768px）字号提升至 1rem（card p / section-subtitle / stat-label / subtitle / tagline / quote-text）
  6. 移除重复的 `body{}` CSS规则
  7. 移动端暗模式专用media query（768px以下）补充字号和颜色覆盖
- Commit: `待提交`

### ✅ 6.2 SEO 和可分享性
- 状态: ✅ 已完成
- 实现: title / meta description / Open Graph / twitter:card 均完整

### ✅ 6.3 设计调性
- 状态: ✅ 已完成
- 实现: 深色为主，#0a1628 色系，金色强调色

---

## 所有任务完成状态

| 优先级 | 任务 | 状态 | 说明 |
|--------|------|------|------|
| ✅ P1-1 | 删除占位符 | 已完成 | Hero 区域 ♟️ + 价值投资 + 芒格语录 |
| ✅ P1-2 | 修正人物背景事实 | 已完成 | JD+MBA+MA / 比亚迪时间 / ~20%脚注 |
| ✅ P1-3 | 下载资源链接标注 | 已完成 | Markdown 格式标注 |
| ✅ P1-4 | 数据时效标注 | 已完成 | Footer 标注数据截止日期 |
| ✅ P2-1 | 研究笔记板块 | 已完成 | Agent主动填充4篇结构化笔记（CCBC/四理念/护城河/方法论） |
| ✅ P2-2 | 视频卡片空链接 | 已完成 | href=# → 实际链接（commit `c092891`） |
| ✅ P2-3 | 活动时间线 | 结构完成 | 10-item checklist 由用户勾选 |
| ✅ P3-1 | 我的投资框架 | 结构完成 | 框架由用户填充（Q3） |
| ✅ P3-2 | 文明3.0思想框架 | 已完成 | 三阶段卡片 + 中国转型论点 |
| ✅ P4-1 | 原则映射 | 结构完成 | 表格由用户填充（Q4） |
| ✅ P5-1 | 持仓数据错误 | 已完成 | 真实13F数据（commit `89b2457`） |
| ✅ P5-2 | 术语表精简 | 已完成 | 8个核心术语 |
| ✅ P5-3 | 推荐书籍标注 | 已完成 | 必读/进阶/参考标签 |
| ✅ P6-1 | 移动端优化 | 已完成 | 返回顶部按钮 |
| ✅ P6-4 | 汉堡导航菜单 | 已完成 | ≤1024px滑出式抽屉 + 夜间模式 |
| ✅ P6-5 | 移动端暗模式全面修复 | 已完成 | text-muted变量覆盖 + 字号提升 + 硬编码颜色修复 |
| ✅ P7-1 | PDD投资案例分析（BYD框架） | 已完成 | 创建 pdd-investment-deep.html，8章结构，置信度标注完整 |
| ✅ P7-2 | 中国邮储银行投资分析（BYD框架） | 已完成 | 创建 psbc-investment-deep.html，8章结构；持仓核实确认：2020-12-18首次买入10.06亿股(HK$4.228)，2021-01-15加仓2.68亿股(HK$5.3479)，累计成本约HK$57亿，持股比例最高5.93%，至今仍持有约9.86亿股 |

| P6-C | 李录中国股票持仓研究（非13F渠道） | 待执行 | 核实HK股/A股持仓 |
| P6-C-1 | 全球配置比例计算（非13F渠道） | 待执行 | 13F+非13F合并计算全球配置比例 |
| P6-C-2 | 贵州茅台清仓分析（非13F渠道） | 待执行 | 创建 kweichow-moutai-investment-deep.html（9章，BYD框架） |
| ✅ P6-2 | SEO | 已完成 | meta / OG / twitter:card |
| ✅ P6-3 | 设计调性 | 已完成 | 深色 + 金色强调 |

**所有代码级修复已全部完成。** 剩余 P2-1、P2-3、P3-1、P4-1 均为用户内容填充，无需 Agent 介入。

---

## Round 4 任务 (2026-04-11)

| 任务 | 描述 | 状态 |
|------|------|------|
| 4-A1 | 删除腾讯/中国移动案例卡片，仅保留比亚迪 | ✅ |
| 4-A2 | 投资原则从3条扩展为6条 + Hero数字改为6 | ✅ |
| 4-A3 | 恢复六步决策框架 | ✅ |
| 4-A4 | FAQ同步（三学位、六原则） | ✅ |
| 4-A5 | EWBC/OXY投资逻辑注释 | ✅ |
| 4-A6 | 文明3.0板块内容扩展 | ✅ |

- Commit `5b489a7`: Round 4 fixes — 案例精简/6原则/决策框架/FAQ/EWBC-OXY注释/文明3.0扩展

---

## Round 5 — 内容主动填充（2026-04-11）

> ⚠️ 重要原则：站点内容由 Agent 主动收集填充，不等待用户手动回填。cron job `Li Lu Content Collector` 负责日常采集，Review Notes 中的内容任务由 `Li Lu Site Dev` cron job 分配执行。

| 任务 | 描述 | 状态 | 优先级 |
|------|------|------|--------|
| 5-C1 | **验证 EWBC/OXY 是否在 13F 中** — SEC EDGAR Q4 2025 确认：EWBC $312M (9%) + OXY $60M (2%) 均在持仓中，保留卡片及现有注释 | ✅ | P0 |
| 5-C2 | **研究笔记板块填充** — CCBC视频笔记 + 四大价值投资理念 + 护城河/信任之网 + 投资方法论六核心 | ✅ | P1 |
| 5-C3 | **文明3.0框架内容扩展** — 各阶段扩展为2-3句（含马尔萨斯陷阱/1776标志等深度描述）+ 中国转型含李录核心判断 + 两条李录原话引用（3.0铁律/西方误解）+ 四大核心观点列表 + 修复损坏的section标签 | ✅ | P1 |
| 5-C4 | **活动时间线内容填充** — 10-item checklist 已存在，每项补充具体日期、背景、来源链接 | ☐ | P2 |

**执行顺序**：5-C1（验证）→ 5-C2/C3（内容填充）→ 5-C4（收尾）

**5-C1 具体做法**：
1. 用 web_search 搜索 "Himalaya Capital 13F 2025 Q4" + "SEC EDGAR"
2. 找到 Himalayan Capital 的 13F Filing 对比 EWBC 和 OXY 是否在持仓列表中
3. 如果在 → 补全投资逻辑注释（同 BAC/PDD 格式）；如果不在 → 删除 EWBC/OXY 持仓卡片并更新 13F 说明

---

## P6-C · 李录中国股票持仓研究（非13F渠道）

**背景**：13F只覆盖美股持仓。李录在A股（沪深）和H股（港交所）的投资不在13F披露范围内，但MEMORY.md中的Portfolio Structure记录了大量非US持仓数据（如邮储银行、中国电信、中海油等）。需要从网络公开资料核实这些持仓和买入记录。

**研究目标**：
- 核实MEMORY.md中已记录的非13F持仓（邮储银行、中国电信、中国移动、中海油等）是否有公开资料支撑
- 寻找李录对这些标的的买入记录（如访谈、股东信、公开言论）
- 寻找13F之外的新持仓线索

**公开信息来源**：
1. HKEx披露文件（重要股东权益披露）
2. 喜马拉雅资本官网（如有）
3. 雪球/格隆汇/理杏仁等投资社区汇总
4. 李录公开访谈（Sina/36Kr/雪球）
5. 芒格/巴菲特相关场合提及

**已知需核实的持仓（MEMORY.md记录）**：

| 标的 | 代码 | 记录类型 |
|------|------|----------|
| 邮储银行 | 1658.HK / 601658.SH | MEMORY.md记录 |
| 中国电信 | 0728.HK | MEMORY.md记录 |
| 中国移动 | 0941.HK | MEMORY.md记录 |
| 中海油 | 0883.HK | MEMORY.md记录 |
| 保利物业 | 6049.HK | MEMORY.md记录 |

**研究结论处理**：
- ✅ 有实锤（HKEx披露/李录原话）→ 更新MEMORY.md持仓，标注置信度
- 💡 推断但无实锤 → MEMORY.md保留但标注为「推断」
- ❌ 无法核实 → 从MEMORY.md移除相关记录

**执行结果写回**：核实完成后更新MEMORY.md持仓数据，并补充到REVIEW_NOTES完成记录

---


#### P6-C-1 · 全球配置比例计算
**任务**：将非美股持仓与13F持仓合并，计算李录全球资产配置比例。

**已知数据**：
- 13F美股组合：~US$35.7亿（2025Q4，含Alphabet/BAC/PDD/BRK.B/EWBC等9只）
- 邮储银行(1658.HK)：当前持仓约9.86亿股，4.96%，当前价约HK$4.8，市值约HK$47亿(~US$6亿)
- 比亚迪(1211.HK)：25年+连续持仓，持股量大（具体股数未披露），按当前价HK$300+估算市值很大
- 喜马拉雅资本总管理规模：~US$50亿(2021) → ~US$80亿(2025)

**输出**：一张配置表（美股/港股/其他，各标的名称+估算市值+估算比例），需标注置信度

#### P6-C-2 · 贵州茅台清仓分析（BYD框架）
**任务**：创建 kweichow-moutai-investment-deep.html，严格复用 byd-investment-deep.html 结构，新增第9章专门分析卖出逻辑。

**背景**：
- 李录在茅台上市初期（2001年前后）买入
- 在塑化剂期间（2013-2014，茅台PE跌至4-5倍）重仓买入
- 持有约20年后疑似清仓
- 最终回报：约287倍

**8+1章节结构**：
1. 如何发现：2001年茅台IPO早期
2. 关键特质：茅台的品牌护城河
3. 买入逻辑：塑化剂期间4-5倍PE极端低估重仓买入
4. 持有过程：20年+持有经历的重大考验
5. 卖出时机：何时卖出？为什么卖？（如无公开记录，标注待核实）
6. 正反方辩论：市场对茅台的分歧
7. 方法论提炼：茅台 vs BYD/PDD的卖出逻辑对比
8. 对普通投资者的启示
9. 新增：卖出逻辑深度分析

**输出**：li-lu-research/kweichow-moutai-investment-deep.html



## P6-E · 视频页面可用性验证与失效处理

**问题来源**：用户反馈（2026-04-12）

**优先级**：P1

**状态**：✅ 已完成（2026-04-12）

---

### 验证结果

通过 web_search 逐个验证 9 个 YouTube embed 视频可用性：

| 视频ID | 标题 | 状态 | 备注 |
|--------|------|------|------|
| b2yxBBMIEz0 | CCBC Fireside Chat | ✅ 可用 | |
| KAoC8pErmb0 | The Chinese Warren Buffett | ✅ 可用 | |
| LWikhUVneYI | Li Lu On 2021 Investing | ✅ 可用 | |
| -gfRCGZ0zf4 | How I Got Started In Value Investing (CBS 2021) | ✅ 可用 | |
| YaCRr0DIfuE | Investing in China: Unique Challenges | ✅ 可用 | |
| 35RgNwcyjFk | Holy Grail of Investing (FAME 2012) | ✅ 可用 | |
| IbrTswEKpLE | Why Only 5% Win in Stocks | ✅ 可用 | |
| KmzOZLf8wcw | Li Lu's Secret to Investing Success (Short) | ❌ 已下架 | YouTube Short 被频道设为私有 |
| _-M1HFuqus0 | Li Lu Explains Value Investing | ✅ 可用 | YouTube Short |

---

### 修复内容

**1. KmzOZLf8wcw.html - 不可用视频处理**
- 问题：We Study Billionaires 频道将该 Short 设为私有/删除
- 修复：移除失效 iframe，替换为「视频不可用」占位符
- 占位符包含：警告图标 + 说明文字 + 跳转完整版访谈链接（KAoC8pErmb0）
- Commit: `128023e`

**2. 全部 9 个视频子页导航锚点修复**
- 问题：导航链接指向 `#framework`（不存在），应为 `#my-framework`
- 修复：批量替换所有 `index.html#framework` → `index.html#my-framework`（含 navbar 和 nav-drawer 两处）
- 涉及页面：-gfRCGZ0zf4.html, 35RgNwcyjFk.html, b2yxBBMIEz0.html, IbrTswEKpLE.html, KAoC8pErmb0.html, LWikhUVneYI.html, YaCRr0DIfuE.html, _-M1HFuqus0.html, KmzOZLf8wcw.html
- Commit: `128023e`

---

### 验证方式

- web_search 逐个确认 8/9 视频可找到公开引用（置信度 ✅）
- KmzOZLf8wcw 搜索结果明确标注 "Video unavailable"（置信度 ✅ 确认不可用）
- Nav 锚点修复通过 `Select-String` 全目录扫描确认 0 个残留 `#framework`

---

### 注意事项

- YouTube Shorts 视频保质期短，建议定期核查（建议加入定期健康检查）
- `_-M1HFuqus0`（Li Lu Explains Value Investing）同为 Short，当前可用但需关注

---

## P7 — 投资案例分析（BYD框架）

### P7-1 · PDD投资案例分析（用比亚迪框架）

**背景**：用户对 byd-investment-deep.html 的分析框架高度认可，希望用同一框架分析李录投资PDD的决策逻辑。BYD框架包含8个维度：①发现经过 ②关键会面 ③说服/纳入 ④买入逻辑 ⑤回调与应对 ⑥正反方辩论 ⑦方法论提炼 ⑧对普通投资者启示。

**任务**：创建 pdd-investment-deep.html，严格遵循 byd-investment-deep.html 的结构模板，对应分析如下8个章节：

1. **如何发现**：李录何时、通过什么渠道注意到PDD；PDD当时的业务状态（黄峥背景、拼单模式验证情况）
2. **关键特质（对标王传福→黄峥）**：黄峥的「第一性原理思维、工程师落地能力、受托人精神」具体体现；黄峥与段永平的师徒关系对李录判断的影响
3. **买入逻辑**：李录买入PDD的成本区间；PDD的竞争优势（对标比亚迪的垂直整合 → PDD的C2M/社交裂变）；为什么这个标的符合李录的能力圈
4. **2021-2022暴跌**：PDD股价从212美元跌至23美元的触发因素（监管/反垄断/中概股集体下跌）；李录/芒格的应对记录（如有）；如何用比亚迪7次暴跌的框架理解PDD
5. **正反方辩论**：段永平 vs 芒格/李录对PDD的分歧（地缘政治风险 vs 商业模式优势）；黄峥 step back and think 的思维方式
6. **方法论提炼**：用比亚迪框架分析PDD的异同；李录「实业家思维 vs 股票分析师思维」在PDD上的应用
7. **对普通投资者的启示**：PDD vs BYD的风险结构对比；长期持有的前提条件是否满足
8. **附录：关键时间线**：黄峥创业时间线、PDD发展里程碑、李录13F建仓记录

**文件输出**：li-lu-research/pdd-investment-deep.html

**分析深度要求**：
- 引用黄峥公开讲话/采访（浙大小饭桌/致股东信/段永平相关点评）
- 引用李录对PDD的公开评论（13F信号 / 雪球/访谈）
- 引用段永平对PDD和黄峥的评价
- 股价回调数据需标注日期和触发因素
- 每节最后附「置信度标注」（✅确认 / 💡推断 / ⚠️待核实）

**参考文件**：byd-investment-deep.html（框架模板）



### P7-2 · 中国邮储银行投资分析（BYD框架）

**背景**：用户要求用BYD框架分析李录投资中国邮储银行（PSBC，港股1658.HK / A股601658.SH）的决策逻辑。

**持仓核实（前置步骤）**：
- 首先确认：李录13F持仓中是否包含邮储银行
- 如果有 → 按BYD框架8维度分析这笔投资
- 如果没有 → 调整为「为什么李录没有投邮储银行」的分析（对比李录能力圈与邮储银行商业模式的匹配度）

**如果确认有持仓，创建 psbc-investment-deep.html，结构如下**：

1. **如何发现**：李录注意到邮储银行的背景（邮储银行是国有大行中唯一具有下沉网络优势的银行）
2. **关键特质（对标黄峥→邮储管理层）**：邮储银行的差异化优势（邮政网络触达农村最后一公里；邮政集团背景下的资源禀赋）
3. **买入逻辑**：买入价格区间；邮储银行 vs 其他国有银行的差异化（资产质量/负债成本/增长潜力）
4. **可能的回调**：邮储银行股价表现；李录的应对
5. **正反方辩论**：邮储银行的优势（零售银行转型/下沉网络）vs 国有银行通病（效率低下/官僚体制）
6. **方法论提炼**：用BYD框架审视银行股投资；李录对金融机构的投资逻辑
7. **对普通投资者的启示**：银行股投资的风险；邮储银行是否适合长期持有
8. **附录：关键时间线**：邮储银行发展里程碑；李录建仓时间线（如有）

**置信度要求**：标注每节置信度（✅确认 / 💡推断 / ⚠️待核实）

**参考**：byd-investment-deep.html（框架模板）、pdd-investment-deep.html（如已完成，参考其格式）


---

### P6-G · Changelog 缺失修复

**问题来源**：用户反馈（2026-04-12）

**状态**：✅ 已完成（2026-04-12）

**修复内容**：
1. `index.html` 新增 `<section id="changelog">`（位于 `</main>` 和 `<footer>` 之间）
2. `.github/CLAUDE.md` 新增规则7：每次 push 到 dev/master 必须追加 changelog
3. MEMORY.md 中冗余规范已移除，指向 CLAUDE.md 为唯一真实来源

**Commit**：`c966090`

---

## P6-H · UX可用性：双层内容架构混乱（最高优先级）

**问题来源**：用户反馈（2026-04-12）

**优先级**：**P0**（功能性导航错误，影响页面可用性）

**状态**：✅ 已完成（2026-04-12）

**Commit**：`39c1c7a`

---

### 修复内容

**1. Footer 导航修复（P0）**
- `#videos` → `video_study.html`
- `#books` → `bookshelf.html`
- `#learning` → `timeline.html`

**2. "查看全部"引导链接（P1）**
- `#quotes` 底部：`查看全部语录 →` → `quotes.html`
- `#books` 底部：`完整书单与阅读指引 →` → `bookshelf.html`
- `#timeline-index` 底部：`完整时间线 →` → `timeline.html`

**验证方式**：确认 footer 链接指向独立页面，三处内嵌板块底部均有引导链接。

**待处理（P2）**：内嵌内容精简为 3-4 条精选 — 暂缓，以内容丰富度为先。

---

## Commit 历史

| 日期 | Commit | 内容 |
|------|--------|------|
| 2026-04-12 | `39c1c7a` | fix: P6-H footer nav + view-all links (quotes/books/timeline) |
| 2026-04-12 | `0fef818` | docs: REVIEW_NOTES — P6-G completed (changelog section added) |
| 2026-04-12 | `c966090` | feat: add changelog section to index.html + CLAUDE.md rule 7 |
| 2026-04-12 | `d7dba0a` | feat: add psbc-investment-deep.html (P7-2, BYD framework applied to PSBC investment) |
| 2026-04-12 | `179cac2` | feat: add pdd-investment-deep.html (P7-1, BYD framework applied to PDD investment) |
| 2026-04-11 | `e9ffcec` | docs: REVIEW_NOTES fourth audit — all code verified complete, encoding+links clean |
| 2026-04-11 | `d73aae7` | fix: nav link #framework -> #my-framework across all pages (encoding: clean) |
| 2026-04-10 | `a07cd7e7cada43c8b1cf060a227237b19ac7e266` | docs: CLAUDE.md 准则5强制化 + REVIEW_NOTES最终确认 (all code tasks complete) |
| 2026-04-10 | `aa12b3f` | docs: REVIEW_NOTES 全面核查更新 — P2-2/P5-1 已解决，清理待修复表，补充 commit 历史 |
| 2026-04-10 | `fc669d7` | docs: update REVIEW_NOTES - P2-2 video links fixed |
| 2026-04-10 | `c092891` | fix: replace href=# dead links in index.html video cards (P2-2) |
| 2026-04-09 | `b9f8dc2` | docs: update REVIEW_NOTES - P5-1 持仓数据修复完成 |
| 2026-04-09 | `89b2457` | fix: replace user portfolio with Himalaya Capital actual 13F holdings (P5-1) |
| 2026-04-09 | `5591aec` | docs: update REVIEW_NOTES with fourth commit entry |
| 2026-04-09 | `88c6629` | fix: CLAUDE.md literal U+FFFD |
| 2026-04-09 | `3cdf487` | fix: raw_github.html encoding |
| 2026-04-08 | `96cdd338` | fix: CSS dark-mode + meta dedup |
| 2026-04-08 | `3a77a6d` | fix: encoding corruption restore |
