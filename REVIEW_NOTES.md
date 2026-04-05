# Li Lu Site Review Notes (2026-04-05)

## Review Prompt Framework
Reference: https://claude.ai/public/artifacts/f424f11e-d889-4b7d-9a51-30376a35300d

**Note:** Comments split into:
- **产品类 (Product)**: UI/UX/功能/内容
- **流程类 (Process)**: 工作流程规范

---

## 产品类 P0 Issues (Must Fix)
1. **video_study.html** — Only CCBC video. Add Master Class, 北大演讲, We Study Billionaires etc.
2. **downloads.html** — YouTube link `example` placeholder + 2 "待补充" blanks.
3. **li-lu-qa.md** — Portfolio outdated. Must match 13F: Alphabet 43.86%, BAC 16.08%, PDD 14.64%, BRK.B 12.64%, EWBC 8.74%, OXY 1.69%, CROX 1.50%, AAPL 0.84%.

## 产品类 P1 Issues (Should Fix)
1. **video_study.html** — No navigation. Add nav bar.
2. **bookshelf.html** — Step 5 no link to index.html.
3. **downloads.html** — Add SEC EDGAR direct link.
4. **index.html** — Principle cards 04/05/06 inconsistent.
5. **index.html** — "所有者心态" quote duplicated.

## 产品类 P2 Issues (Nice to Have)
1. **bookshelf.html** — Add purchase links.
2. **downloads.html** — ZIP bundle option.
3. **index.html** — "Last updated" date near 13F section.
4. **index.html** — Glossary terms clickable → scroll.

---

## 流程类 Process Rules (MUST FOLLOW)
1. **Git worktree for parallel dev**: Each sub-agent in its own worktree directory
2. **NEVER run `git pull`** in any session
3. **Use GitHub API** for all reads/writes
4. **After every push**: Playwright regression test (7 pages, 0 errors)
5. **Review → Plan → Do** — don't modify immediately on feedback
6. **Encoding check**: corrupt `e9 8f 89 e5 ba a1 e7 b6 8d` → fix with `e6 9d 8e e5 bd 95`
7. **Design**: Follow M3 (Material Design 3) principles
8. **Mobile**: hamburger + back-to-top + overflow-x hidden

---

## Sub-Agent Protocol (CRITICAL)
Sub-agents MUST:
- Read files via GitHub API (not local git)
- Write back via GitHub API (not git commit)
- Never touch local git repository
- Check for corruptions after any file modification
- Run regression test before reporting done
