#!/usr/bin/env python3
# -*- coding: utf-8 -*-
filepath = r"C:\Users\hozen\.openclaw\workspace\li-lu-research\wingtech-analysis.html"

with open(filepath, "rb") as f:
    raw = f.read()

has_crlf = b"\r\n" in raw
text = raw.replace(b"\r\n", b"\n").decode("utf-8")

# The file has NO newlines between HTML tags. All HTML is on single lines.
# We must use exact strings as they appear in the file.

# Pattern for 偿付资金来源 - NO newlines
old1 = "偿付资金来源测算</h4><ul><li><strong>ODM出售回款</strong>：43.89亿元已到账（大部分已完成交割）</li><li><strong>半导体经营现金流</strong>：年化约20-25亿（按H1 2025 annualized），足以覆盖利息"
new1 = "偿付资金来源（压力测试）</h4><ul><li><strong>ODM出售回款</strong>：43.89亿元已到账（大部分完成交割）</li><li><strong>半导体现金流</strong>：年化20-25亿，但安世控制权受限导致不确定性上升"
if old1 in text:
    text = text.replace(old1, new1, 1)
    print("1. OK: 偿付资金来源 part 1")
else:
    print("1. MISS: 偿付 part 1")

old2 = "合肥国资背书</strong>：合肥东方投资是重要股东，具有政策性保障含义</li><li><strong>下修+拉正股</strong>：公司有意愿也有能力通过拉正股化解到期压力"
new2 = "合肥国资背书</strong>：重要股东，面对86亿规模能分担多少不确定</li><li><strong>核心压力</strong>：86亿转债到期（2027年7月），若触发*ST+机构出库"
if old2 in text:
    text = text.replace(old2, new2, 1)
    print("2. OK: 偿付资金来源 part 2")
else:
    print("2. MISS: 偿付 part 2")

# Insert border style into 偿付 card (it's now a div, need to add style)
old_div = '<div class="lesson-card"><h4>偿付资金来源（压力测试）'
new_div = '<div class="lesson-card" style="border-left-color:#991b1b"><h4>偿付资金来源（压力测试）'
if old_div in text:
    text = text.replace(old_div, new_div, 1)
    print("3. OK: Added red border style to 偿付 card")
else:
    print("3. MISS: 偿付 border style (may already have it)")

# Insert crash narrative before 转债定价分析 h3
crash = ('<h3>转债暴跌始末（2026年4月）</h3>'
    '<div class="lesson-card"><h4>8连阴：下修利好反成利空</h4>'
    '<ul><li><strong>4月8日</strong>：董事会确定下修转股价至32.66元（幅度25.1%，下修到底）</li>'
    '<li><strong>4月9日</strong>：转债开盘冲高至116.2元，回落收113.746元（-1.26%）</li>'
    '<li><strong>4月10日起</strong>：转股价生效，开启8连阴</li>'
    '<li><strong>4月20日</strong>：收98.845元（-1.11%），<strong>跌破面值100元</strong></li>'
    '<li><strong>4月21日</strong>：正股跌6.66%至29.29元，转债同步承压</li></ul></div>'
    '<div class="lesson-card" style="border-left-color:#991b1b"><h4>转债vs正股：为何背离？</h4>'
    '<ul><li>转股溢价率-2.58%：转债价格已低于转股价值，<strong>纯债属性超过股性</strong></li>'
    '<li>核心焦虑：4月30日年报，若审计出具"无法表示意见"将触发<strong>*ST退市警示</strong></li>'
    '<li>兴业证券：机构资金已在抛售，基金对弱资质品种持续出库</li></ul></div>')

insert_pt = '<h3>转债定价分析</h3><div class="lesson-card"><h4>当前市场定价逻辑'
if insert_pt in text:
    text = text.replace(insert_pt, crash + insert_pt, 1)
    print("4. OK: Inserted crash narrative before 转债定价分析")
else:
    print("4. MISS: crash insert point")

# Fix 转债定价分析 card content
old_pricing = ('<li>转债价格105-114元（接近面值）反映市场对"最终能还钱"的信任，而非对正股的乐观</li>'
    '<li>YTM约3-4%，非极端高水平——市场并未定价违约概率很高</li>'
    '<li>信用评级A（展望负面）：已price in部分风险，但非垃圾债水平</li>'
    '<li>转股溢价率40%+：正股表现平平，转股概率低，更多是纯债属性</li>')
new_pricing = ('<li>转债价格98.845元（<strong>跌破面值</strong>）：市场对"最终能还钱"的信任<strong>正在动摇</strong></li>'
    '<li>YTM 8.74%：较此前的3-4%大幅飙升，市场正在<strong>定价较高违约风险</strong></li>'
    '<li>信用评级A（展望负面）：已接近垃圾债边缘，机构被迫出库</li>'
    '<li><strong>转股溢价率-2.58%</strong>：已转负——转债市场极罕见，正股前景极度不乐观</li>')
if old_pricing in text:
    text = text.replace(old_pricing, new_pricing, 1)
    print("5. OK: Updated 转债定价分析 card content")
else:
    print("5. MISS: pricing card content")

result = text.encode("utf-8")
if has_crlf:
    result = result.replace(b"\n", b"\r\n")

with open(filepath, "wb") as f:
    f.write(result)

print("\nSaved!")
