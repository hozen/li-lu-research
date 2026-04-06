# Li Lu Site Review Notes

**Last Updated:** 2026-04-06
**Reference:** `li-lu-site-improvement-prompt.md` (最新完整改进需求)

---

## 当前状态总览

| 优先级 | 状态 | 说明 |
|--------|------|------|
| P0 | 🔶 大部分完成 | Hero/YouTube/事实核查已完成；PR #3 已合并 |
| P1 | 🔄 进行中 | video_study/原则卡片/书架跳转 |
| P2 | 🔄 部分完成 | .md标注/footer日期/持仓标注 |

---

## P0 Issues — 状态

| # | 问题 | 文件 | 状态 | 备注 |
|---|------|------|------|------|
| P0-1 | Hero占位符"李录照片" | index.html | ✅ 已完成 | 替换为"价值投资·长期复利" + 抽象SVG |
| P0-2 | downloads.html YouTube占位符 | downloads.html | ✅ 已完成 | CCBC✅ / WSB✅ / MasterClass✅ |
| P0-3 | 事实核查 | index, li-lu-qa.md | ✅ 已完成 | 哥大三学位/JD+MBA+MA / BYD ~2002 / ~20%脚注 / 论文标题 |
| P0-4 | 数据时效标注 | index.html | ✅ 已完成 | "数据截止：2025 Q4 13F (2026-02-17披露)" |
| P0-5 | .md链接标注 | downloads.html | ✅ 已完成 | "(Markdown 格式)" 标注 |
| P0-6 | footer日期规范 | 全页面 | ✅ 已完成 | "页面更新：YYYY-MM-DD" |

---

## Round 2 — 待处理任务

### A组：遗留修正

| # | 问题 | 文件 | 状态 | 说明 |
|---|------|------|------|------|
| A1 | 比亚迪时间线措辞 | index.html | ✅ 已完成 | 两条独立条目：~2002-2003发现 + 2008芒格/巴菲特入场 |
| A2 | FAQ Q4措辞 | index.html | ✅ 已完成 | FAQ Q4 引用~2002-2003发现 + 2008巴菲特入股上下文 |
| A3 | 持仓区与案例区去重 | index.html | ✅ 已完成 | 案例区仅保留比亚迪历史案例；Alphabet/BAC/PDD卡片移除；副标题注明"当前持仓请见上方持仓区" |

### B组：新增板块（Q2结构搭建）

| # | 板块 | 位置 | 状态 | 说明 |
|---|------|------|------|------|
| B1 | 研究笔记 Study Notes | "投资案例"后/"关于李录"前 | ✅ 已完成 | CBS访谈+北大演讲+文明3.0三条笔记卡 | 将现有CBS访谈要点迁移为第一条笔记 |
| B2 | 李录公开活动索引 | 视频资源区顶部 | ✅ 已完成 | 10-item checklist，3/10已完成 | 10-item checklist，已回顾的打勾 |
| B3 | 文明3.0框架 | 核心原则后/决策框架前 | 🔴 待新增 | 三阶段文明+中国2.5→3.0转型 |

---

## P1 Issues — 状态

| # | 问题 | 文件 | 状态 | 说明 |
|---|------|------|------|------|
| P1-1 | video_study → 视频列表入口页 | video_study.html | 🔴 待处理 | 每视频独立子页面，JSON数据分离 |
| P1-2 | principle cards 04/05/06 样式一致 | index.html | 🔴 待处理 | 样式统一 |
| P1-3 | bookshelf Step 5 跳转链接 | bookshelf.html | 🔴 待处理 | 添加 → index.html |
| P1-4 | "所有者心态"语录重复 | index.html | 🔴 待确认 | 确认是否已修复 |
| P1-5 | video_study 移动端汉堡菜单 | video_study.html | ✅ 已完成 | |

---

## P2 Issues — 状态

| # | 问题 | 文件 | 状态 | 说明 |
|---|------|------|------|------|
| P2-1 | .md链接标注 | downloads.html | ✅ 已完成 | |
| P2-2 | 持仓数据时间戳 | index.html | ✅ 已完成 | |
| P2-3 | footer日期规范化 | 全页面 | ✅ 已完成 | |
| P2-4 | 新增可折叠时间线 | timeline.html | 🔴 待处理 | 公开活动索引 |
| P2-5 | 术语表精简 | glossary.html | ✅ 已完成 | 11→8术语：移除经济护城河(重复)、内在记分卡(偏巴菲特)、无缝信任网(子概念) |
| P2-4 | 新增可折叠时间线 | timeline.html | 🔴 待处理 | |
| P2-6 | 书架加购买链接 | bookshelf.html | 🔴 待处理 | |

## 2026-04-07 更新

### 新增 (B1 + B2)
- **B1 研究笔记 (Study Notes)**：新增独立 section，放置在 cases 区之后，包含三条研究笔记（CBS访谈/北大演讲/文明3.0）
- **B2 公开活动索引**：10-item checklist，放置在视频资源区前，3/10已完成标记
- 导航栏新增「笔记」「索引」快速入口

### 技术
- 编码检查：无乱码
- Playwright 回归测试：7 pages / 0 errors ✅


---

## 技术约束（始终遵守）

1. **M3设计规范** — CSS变量/圆角/间距/字体全合规，参考 `web_development_standards.md`
2. **编码检查** — 每次修改后 `python scripts/check_encoding.py`，无 `e9 8f 89` 乱码
3. **Playwright回归测试** — headed模式，7 pages / 0 errors
4. **Git工作流** — worktree开发 / GitHub API推送 / **禁止git pull / 禁止推master**
5. **外部链接** — `target="_blank" rel="noopener"`
6. **肖像权** — 不用未授权照片

---

## 流程规范

1. **Review → Plan → Do** — 不在review后立即修改，先做规划
2. **每次推送前** — 编码检查 + 回归测试全部通过
3. **PR合并** — dev分支通过PR合并到master，不直接推送
4. **下个sprint建议** — 每次报告包含下个任务建议
