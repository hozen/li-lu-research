# CLAUDE.md — 李录研究站点开发规范

## 核心原则

**每个文件都有归属。不是项目的文件，就该在 workspace 根目录。**

---

## 一、文件写入规范（强制）

### 规则 1：必须用 `write` 工具写入中文内容
- 所有 `.html` / `.json` / `.md` / `.txt` 文件**必须用 `write` 工具**
- **禁止**用 `exec echo` / `>` 重定向 / `python f.write()` 等方式写入中文内容
- 违反此规则 = 任务失败

### 规则 2：写入后立即编码检查
```bash
python scripts/check_encoding.py <文件路径>
```
检查项：
- `e9 8f 89` 乱码序列（错误「李录」的特征）
- `�?` 乱码字符
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

## 二、Git 操作规范

### 规则 4：禁止 git pull
**绝对禁止**在这个 workspace 执行 `git pull`，会损坏文件编码。

**正确方式：**
- 推送 → 使用 GitHub API（参考 `scripts/push_*.py`）
- 获取更新 → 创建新的 worktree + 手动合并

### 规则 5：提交前检查
所有 HTML/MD 文件 commit 前必须确认：
1. 编码检查通过（规则 2）
2. HTML 标签完整性通过（规则 3）

---

## 三、工作流程

### 标准开发流程
1. 读取 `REVIEW_NOTES.md` — 找到标记为"待处理"的任务
2. 读取相关页面了解现状
3. 实施修改（使用 `write` 工具）
4. 编码检查 + HTML 校验
5. Playwright 回归测试（7 pages / 0 errors）
6. GitHub API 推送（dev 分支）
7. 更新 `REVIEW_NOTES.md` 状态

### Playwright 回归测试（必须执行）
每次修改后，至少测试改动的页面，**0 console errors** 才算完成。

---

## 四、质量标准

| 检查项 | 标准 |
|--------|------|
| 编码 | 无 `e9 8f 89`，无 `�?` |
| HTML 标签 | 全部闭合，层级正确 |
| Console errors | 0 errors |
| Git 推送 | 仅使用 GitHub API，禁止 git pull |

---

## 五、目录结构
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
