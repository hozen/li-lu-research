import re

with open(r"C:\Users\hozen\.openclaw\workspace\li-lu-research\index.html", encoding="utf-8") as f:
    html = f.read()

# 1. Remove photo placeholder text
old_placeholder = '<p style=color:var(--text-muted);font-size:0.8rem;margin-top:10px>(请放置照片于此)</p>'
new_placeholder = '<p style=color:rgba(255,255,255,0.4);font-size:0.8rem;margin-top:10px>(照片待替换)</p>'
html = html.replace(old_placeholder, new_placeholder)

# 2. Add disclaimer to ~20% returns stat
html = html.replace('>年化复合收益</div>', '>年化复合收益*</div>')

# 3. Add data timestamp to holdings section
old_holding_footnote = '* 数据来源: Himalaya Capital 2025年Q4 13F申报 (2026年2月17日披露) | 仅供研究参考，不构成投资建议'
new_holding_footnote = '* 数据截止：2025年Q4 13F (2026年2月17日披露) | 页面更新：2026-04-05 | 仅供研究参考，不构成投资建议'
html = html.replace(old_holding_footnote, new_holding_footnote)

# 4. Fix BYD timing - remove the 2008 specific text and make it clearer
old_byd = '<p style="color: #666; font-size: 0.9rem; margin-top: 10px;"><strong>投资时间:</strong> 2008年</p>'
new_byd = '<p style="color: #666; font-size: 0.9rem; margin-top: 10px;"><strong>发现时间:</strong> 约2002-2003年（李录首次研究比亚迪）</p>'
html = html.replace(old_byd, new_byd)

# 5. Fix 2014 paper title typo - "cilivilized" -> "Civilizations"
html = html.replace('cilivilized and Modern', 'Civilizations, Modernization, Value Investing and China')

# 6. Fix education background - add 3 degrees from Columbia
old_edu = '在哥伦比亚大学师从Bruce Greenwald教授，获MBA学位'
new_edu = '在哥伦比亚大学师从Bruce Greenwald教授，获JD法律博士 + MBA工商管理硕士 + MA经济学硕士三学位'
html = html.replace(old_edu, new_edu)

print("Applied: education fix, paper title fix")

# 7. Fix FAQ education entry - add 3 degrees
old_faq_edu = '李录在哥伦比亚大学师从Bruce Greenwald教授学习价值投资，深受格雷厄姆与巴菲特思想影响，后创立喜马拉雅资本。'
new_faq_edu = '李录在哥伦比亚大学获JD+MBA+MA三学位，师从Bruce Greenwald教授学习价值投资，深受格雷厄姆与巴菲特思想影响，后创立喜马拉雅资本。'
html = html.replace(old_faq_edu, new_faq_edu)

print("All Priority 1 fixes applied!")

with open(r"C:\Users\hozen\.openclaw\workspace\li-lu-research\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done - Priority 1 fixes applied")
