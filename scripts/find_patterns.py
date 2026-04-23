#!/usr/bin/env python3
# -*- coding: utf-8 -*-
filepath = r"C:\Users\hozen\.openclaw\workspace\li-lu-research\wingtech-analysis.html"

with open(filepath, "rb") as f:
    raw = f.read()

has_crlf = b"\r\n" in raw
text = raw.replace(b"\r\n", b"\n").decode("utf-8")

changes = 0

# 1. 转债三条路 - update 43.60 to 32.66 in the text (there are two occurrences now)
text = text.replace("正股涨超43.60元，转股溢价率收窄", "正股涨超32.66元，转股溢价率收窄")
print("1. Updated 转股 trigger price in 转债三条路")

# 2. Fix 转债定价分析 section - add crash narrative BEFORE the heading
# The section is: </table></div><h3>转债定价分析</h3><div class="lesson-card"><h4>当前市场定价逻辑</h4>
crash = ('<h3>转债暴跌始末（2026年4月）</h3>\n'
    '<div class="lesson-card"><h4>8连阴：下修利好反成利空</h4>\n'
    '<ul><li><strong>4月8日</strong>：董事会确定下修转股价至32.66元（幅度25.1%，下修到底）</li>\n'
    '<li><strong>4月9日</strong>：转债开盘冲高至116.2元，回落收113.746元（-1.26%）</li>\n'
    '<li><strong>4月10日起</strong>：转股价生效，开启8连阴</li>\n'
    '<li><strong>4月20日</strong>：收98.845元（-1.11%），<strong>跌破面值100元</strong></li>\n'
    '<li><strong>4月21日</strong>：正股跌6.66%至29.29元，转债同步承压</li></ul></div>\n'
    '<div class="lesson-card" style="border-left-color:#991b1b"><h4>转债vs正股：为何背离？</h4>\n'
    '<ul><li>转股溢价率-2.58%：转债价格已低于转股价值，<strong>纯债属性超过股性</strong></li>\n'
    '<li>核心焦虑：4月30日年报，若审计出具"无法表示意见"将触发<strong>*ST退市警示</strong></li>\n'
    '<li>兴业证券：机构资金已在抛售，基金对弱资质品种持续出库</li></ul></div>\n')

old_pricing = '<h3>转债定价分析</h3>\n<div class="lesson-card"><h4>当前市场定价逻辑</h4>\n<ul><li>转债价格105-114元（接近面值）反映市场对"最终能还钱"的信任，而非对正股的乐观</li>\n<li>YTM约3-4%，非极端高水平——市场并未定价违约概率很高</li>\n<li>信用评级A（展望负面）：已price in部分风险，但非垃圾债水平</li>\n<li>转股溢价率40%+：正股表现平平，转股概率低，更多是纯债属性</li></ul></div>'

new_pricing = ('<h3>转债定价分析</h3>\n'
    '<div class="lesson-card"><h4>当前市场定价逻辑（已发生根本性变化）</h4>\n'
    '<ul><li>转债价格98.845元（<strong>跌破面值</strong>）：市场对"最终能还钱"的信任<strong>正在动摇</strong></li>\n'
    '<li>YTM 8.74%：较此前的3-4%大幅飙升，市场正在<strong>定价较高违约风险</strong></li>\n'
    '<li>信用评级A（展望负面）：已接近垃圾债边缘，机构被迫出库</li>\n'
    '<li><strong>转股溢价率-2.58%</strong>：已转负——转债市场极罕见，正股前景极度不乐观</li></ul></div>')

if old_pricing in text:
    text = text.replace(old_pricing, crash + new_pricing, 1)
    changes += 1
    print("2. Inserted crash narrative AND updated 转债定价逻辑")
else:
    # Try with just the heading match
    if '<h3>转债定价分析</h3>' in text:
        # The content might be slightly different - try to find and insert just the crash narrative
        text = text.replace('<h3>转债定价分析</h3>', crash + '<h3>转债定价分析</h3>', 1)
        print("2b. Inserted crash narrative only (pricing card unchanged)")
    else:
        print("2. MISS: 转债定价分析 section")

# 3. Update 转债三条路 - the full card (in second occurrence too)
old_3paths = ('<div class="lesson-card"><h4>转债三条路</h4>\n'
    '<ul><li><strong>转股（最优）</strong>：正股涨超43.60元，转股溢价率收窄，投资者转股，公司零偿付</li>\n'
    '<li><strong>下修转股价（大概率）</strong>：董事会已提议下修，降低转股门槛，促转股减轻到期压力</li>\n'
    '<li><strong>到期赎回（底线）</strong>：若无法转股，需备85.97亿现金，按108元/张赎回（含最后一年利息）</li></ul></div>')

new_3paths = ('<div class="lesson-card"><h4>转债三条路（已更新）</h4>\n'
    '<ul><li><strong>转股（最优）</strong>：正股需涨超32.66×1.3=42.46元（目前仅29.29元，差距44.8%）</li>\n'
    '<li><strong>下修转股价（已完成）</strong>：32.66元4月10日已生效，但正股持续下跌，转股价值仍低</li>\n'
    '<li><strong>到期赎回（底线风险上升）</strong>：若无法转股，需备85.97亿现金，按108元/张赎回</li></ul></div>')

if old_3paths in text:
    text = text.replace(old_3paths, new_3paths, 1)
    changes += 1
    print("3. Updated 转债三条路")
else:
    print("3. MISS: 转债三条路 full card")
    # Try to at least replace the 43.60 occurrence in 转债三条路
    text = text.replace('正股涨超43.60元，转股溢价率收窄', '正股涨超32.66元，转股溢价率收窄')
    print("3b. Replaced 43.60->32.66 in 转债三条路")

# 4. Update 偿付资金来源
old_fund = ('<div class="lesson-card"><h4>偿付资金来源测算</h4>\n'
    '<ul><li><strong>ODM出售回款</strong>：43.89亿元已到账（大部分已完成交割）</li>\n'
    '<li><strong>半导体经营现金流</strong>：年化约20-25亿（按H1 2025 annualized），足以覆盖利息</li>\n'
    '<li><strong>合肥国资背书</strong>：合肥东方投资是重要股东，具有政策性保障含义</li>\n'
    '<li><strong>下修+拉正股</strong>：公司有意愿也有能力通过拉正股化解到期压力</li></ul></div>')

new_fund = ('<div class="lesson-card" style="border-left-color:#991b1b"><h4>偿付资金来源（压力测试）</h4>\n'
    '<ul><li><strong>ODM出售回款</strong>：43.89亿元已到账（大部分完成交割）</li>\n'
    '<li><strong>半导体现金流</strong>：年化20-25亿，但安世控制权受限导致不确定性上升</li>\n'
    '<li><strong>合肥国资背书</strong>：重要股东，面对86亿规模能分担多少不确定</li>\n'
    '<li><strong>核心压力</strong>：86亿转债到期（2027年7月），若触发*ST+机构出库，局面将极其被动</li></ul></div>')

if old_fund in text:
    text = text.replace(old_fund, new_fund, 1)
    changes += 1
    print("4. Updated 偿付资金来源")
else:
    print("4. MISS: 偿付资金来源 full card")

# 5. Update conclusion
old_conc = '<div class="highlight"><h4>第三层结论：信息不足（偏正面）</h4>'
new_conc = '<div class="highlight"><h4>第三层结论更新：风险显著上升，逻辑仍在但需等待</h4>'
if old_conc in text:
    text = text.replace(old_conc, new_conc, 1)
    changes += 1
    print("5. Updated conclusion title")
else:
    print("5. Already updated or MISS")

print(f"\nTotal changes: {changes} sections updated")

# Encode and save
result = text.encode("utf-8")
if has_crlf:
    result = result.replace(b"\n", b"\r\n")

with open(filepath, "wb") as f:
    f.write(result)

print("File saved!")
