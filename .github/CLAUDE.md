# CLAUDE.md — 李录研究站点开发规范

## 核心原则

**不看当前状态就动手 = 制造返工。每一个任务都要先验证，再动手。**

**质量 gate 必须强制执行。检查不通过 = 不推送。坏代码不允许到达 master。**

---

## 一、Agent 行为准则

### 准则 1：永远先验证，再行动
每次任务前，必须先读取目标文件的**当前实际内容**，确认：
- 任务描述的问题是否真实存在？
- 任务描述的功能是否真的缺失？

如果问题不存在或功能已实现，**标记为"已确认完成，无需操作"**，不要改动任何文件。

### 准则 2：只相信实际文件内容，不相信 REVIEW_NOTES
REVIEW_NOTES 可能过时、可能错误。不要基于 REVIEW_NOTES 的描述做任何假设。
**一切以 `git checkout origin/master -- <文件>` 拉取的最新内容为准。**

### 准则 3：同一次任务内不要推送多次
如果一次任务需要修改多个文件，先全部改完，再一次性推送。
不要改一个文件就推送一次。

### 准则 4：完成标准 — 三重验证
任务完成的定义是：
1. 编码检查通过（规则 2）
2. HTML 标签完整性通过（规则 3）
3. Playwright 回归测试通过（0 console errors）

**三个全部通过才能推送。任何一个失败 = 报告失败，停止，不推送。**

### 准则 5：更新 REVIEW_NOTES 是完成任务的硬性步骤
每次完成任务后，必须立即更新 `REVIEW_NOTES.md`：
- 将该任务标记为 ✅已完成（日期）
- 补充本次修复的具体内容

**未更新 REVIEW_NOTES = 任务未完成。** 即使代码已推送，如果 REVIEW_NOTES 未更新，视为任务失败。

---

## 二、文件写入规范（强制）

### 规则 1：必须用 `write` 工具写入中文内容
- 所有 `.html` / `.json` / `.md` / `.txt` 文件**必须用 `write` 工具**
- **禁止** `exec echo` / `>` 重定向 / `python f.write()` 等方式写入中文内容
- 违反此规则 = 任务失败

### 规则 2：写入后立即编码检查
```bash
python scripts/check_encoding.py <文件路径>
```
检查项：
- `e9 8f 89` 乱码序列（错误「李录」的特征）
- `U+FFFD?` 乱码字符（Unicode替换符 + 问号）
- BOM 头 `\xef\xbb\xbf`

发现乱码 → **立即用 `write` 工具重写**，不要 sed 修复。

### 规则 3：HTML 文件标签完整性校验
```bash
python3 -c "
from html.parser import HTMLParser
class V(HTMLParser):
    def __init__(self):
        super().__init__(); self.s=[]; self.e=[]
    def handle_starttag(self,t,a):
        if t not in ['br','hr','img','input','meta','link','area','base','col','embed','param','source','track','wbr']: self.s.append(t)
    def handle_endtag(self,t):
        if self.s and self.s[-1]==t: self.s.pop()
        elif t not in ['br','hr','img','input','meta','link','area','base','col','embed','param','source','track','wbr']: self.e.append(t)
with open('index.html') as f:
    p=V(); p.feed(f.read())
print('ERRORS:'+str(p.e+p.s) if p.e or p.s else 'OK')
"
```
输出 `OK` 才算通过。

---

## 三、Git 操作规范

### 规则 4：禁止 git pull
**绝对禁止**在这个 workspace 执行 `git pull`，会损坏文件编码。

### 规则 5：每次推送前先同步远程状态
```python
# 用 GitHub API 获取 master 分支最新 SHA
import urllib.request, json
TOKEN = "ghp_YOUR_TOKEN_HERE"  # Replace with your GitHub PAT
REPO = "hozen/li-lu-research"

def api(path):
    url = f"https://api.github.com/repos/{REPO}{path}"
    req = urllib.request.Request(url, headers={"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

master = api("/branches/master")
print("Remote master SHA:", master["commit"]["sha"])
print("Remote master date:", master["commit"]["commit"]["message"])
```
**先确认远程 SHA，再决定基于哪个 commit 创建新 tree。**

### 规则 6：推送格式
所有 commit message 必须包含：
1. 简短功能描述
2. 编码检查状态：`(encoding: clean)`
3. Playwright 测试状态：`(tested: N pages / 0 errors)`

格式：`feat: add civilization section (encoding: clean, tested: 7 pages / 0 errors)`

---

## 四、工作流程

### 标准开发流程

```
第一步：获取远程 master 最新状态
  → 用 GitHub API 获取 origin/master 最新 SHA
  → 确认你要基于哪个 commit 工作

第二步：读取目标文件的实际内容
  → git checkout origin/master -- <文件>（或 GitHub API 获取 blob）
  → 验证任务描述的问题是否真实存在

第三步：实施修改
  → 使用 write 工具
  → 每次写完立即执行编码检查

第四步：三重验证
  → 编码检查（规则 2）
  → HTML 标签校验（规则 3）
  → Playwright 回归测试（7 pages / 0 errors）

第五步：GitHub API 推送
  → 基于最新远程 SHA 创建 tree
  → 创建 commit，message 包含测试状态
  → 更新 master ref

第六步：更新 REVIEW_NOTES（硬要求，参见准则 5）
  → 记录：任务 + commit SHA + 验证状态 + 完成时间
```

### Playwright 回归测试（必须执行）
```javascript
// 使用 Playwright MCP
mcporter call playwright.chromium.open { "headless": false }
mcporter call playwright.chromium.navigate { "url": "http://localhost:8080/index.html" }
// 检查 console errors
```
至少测试：index, video_study, bookshelf, timeline, quotes, glossary, downloads。
**0 console errors 才算通过。**

---

## 五、质量标准

| 检查项 | 标准 |
|--------|------|
| 编码 | 无 `e9 8f 89`，无 `U+FFFD?`，无 BOM |
| HTML 标签 | 全部闭合，层级正确 |
| Console errors | 0 errors |
| Git message | 包含 `(encoding: clean)` 和 `(tested: N pages)` |
| 推送前 | 确认远程 SHA，避免分叉提交 |

---

## 六、任务优先级

每次选择任务时：
1. **优先选 P0**（功能性错误）— 影响页面渲染、链接错误
2. **其次 P1**（UX 问题）— 样式不一致、缺失按钮
3. **最后 P2**（内容补充）— 文案优化、新增内容

**禁止**跳过 P0 先做 P2。

---

## 七、目录结构
```
li-lu-research/
├── .github/
│   └── CLAUDE.md          # 本文件
├── index.html             # 首页
├── video_study.html       # 视频学习
├── bookshelf.html         # 书架
├── timeline.html          # 时间线
├── quotes.html            # 语录
├── glossary.html          # 术语表
├── downloads.html         # 下载资源
├── data/                  # JSON 数据
│   ├── videos.json
│   └── segments.json
├── videos/                # 视频子页
│   └── <youtube-id>.html
├── scripts/               # 通用工具（位于 workspace/scripts/）
│   ├── check_encoding.py
│   └── push_*.py
└── REVIEW_NOTES.md        # 任务状态追踪
```

---

## 八、Changelog 维护规范（强制）

### 规则 7：每次发布必须追加 changelog
**位置**：`index.html` 中 `<section id="changelog">`，位于 `</main>` 和 `<footer>` 之间。

**格式**：
```html
<section id="changelog" style="background:#f7fafc;padding:40px 60px;">
  <h3 style="color:#c9a227;margin-bottom:20px;">更新日志</h3>
  <div style="margin-bottom:20px;">
    <span style="color:#c9a227;font-weight:600;">2026-04-12</span>
    <ul style="margin-top:8px;padding-left:20px;color:#4a5568;">
      <li>新增 xxx 页面/功能</li>
      <li>修复 xxx 问题</li>
    </ul>
  </div>
</section>
```

**要求**：
- 日期金色 `color:#c9a227`
- 列表克制风格，无 emoji
- 每次 `git push` 到 dev 或 master 后立即追加
- **不写 changelog = 任务未完成**

---

## 九、本地开发服务器

```bash
# 启动 HTTP 服务器（端口 8080）
python -m http.server 8080 --directory C:\Users\hozen\.openclaw\workspace\li-lu-research

# 访问地址
http://localhost:8080/index.html
```
