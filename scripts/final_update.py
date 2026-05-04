#!/usr/bin/env python3
# -*- coding: utf-8 -*-
filepath = r"C:\Users\hozen\.openclaw\workspace\li-lu-research\wingtech-analysis.html"

with open(filepath, "rb") as f:
    raw = f.read()

has_crlf = b"\r\n" in raw
text = raw.replace(b"\r\n", b"\n").decode("utf-8")

changes = 0

# Simple string approach - do targeted replacements
# Use single-char replacements for key values

# Fix 转债三条路 - the 32.66 trigger text needs updating to show it needs 42.46 to trigger redemption
# The key phrase is: 正股涨超32.66元，转股溢价率收窄
# We want: 正股需涨超32.66×1.3=42.46元（目前仅29.29元，差距44.8%）
old_3p_trigger = "正股涨超32.66元，转股溢价率收窄，投资者转股，公司零偿付"
new_3p_trigger = "正股需涨超32.66x1.3=42.46元（目前仅29.29元，差距44.8%），无力转股"
if old_3p_trigger in text:
    text = text.replace(old_3p_trigger, new_3p_trigger, 1)
    changes += 1
    print("1. Updated 转债三条路 trigger text")
else:
    print("1. MISS: 3paths trigger text")

# Fix 下修转股价（大概率） -> (已完成)
if "下修转股价（大概率）</strong>：董事会已提议下修" in text:
    text = text.replace(
        "下修转股价（大概率）</strong>：董事会已提议下修，降低转股门槛，促转股减轻到期压力",
        "下修转股价（已完成）</strong>：32.66元4月10日已生效，但正股持续下跌"
    )
    changes += 1
    print("2. Updated 下修转股价 label")
else:
    print("2. MISS: 下修转股价 label")

# Fix 到期赎回底线
if "到期赎回（底线）</strong>：若无法转股，需备85.97亿现金，按108元/张赎回（含最后一年利息）" in text:
    text = text.replace(
        "到期赎回（底线）</strong>：若无法转股，需备85.97亿现金，按108元/张赎回（含最后一年利息）",
        "到期赎回（底线风险上升）</strong>：若无法转股，需备85.97亿现金，按108元/张赎回"
    )
    changes += 1
    print("3. Updated 到期赎回 label")
else:
    print("3. MISS: 到期赎回 label")

# Fix 转债三条路 h4 title
if "<h4>转债三条路</h4>" in text:
    text = text.replace("<h4>转债三条路</h4>", "<h4>转债三条路（已更新）</h4>", 1)
    changes += 1
    print("4. Updated 转债三条路 title")
else:
    print("4. MISS: 转债三条路 title")

# Fix 偿付资金来源
old_fund = "偿付资金来源测算</h4>\n<ul><li><strong>ODM出售回款</strong>：43.89亿元已到账（大部分已完成交割）</li>\n<li><strong>半导体经营现金流</strong>：年化约20-25亿（按H1 2025 annualized），足以覆盖利息"
new_fund = "偿付资金来源（压力测试）</h4>\n<ul><li><strong>ODM出售回款</strong>：43.89亿元已到账（大部分完成交割）</li>\n<li><strong>半导体现金流</strong>：年化20-25亿，但安世控制权受限导致不确定性上升"
if old_fund in text:
    text = text.replace(old_fund, new_fund, 1)
    changes += 1
    print("5. Updated 偿付资金来源 part 1")
else:
    print("5. MISS: 偿付资金来源 part 1")

old_fund2 = "合肥国资背书</strong>：合肥东方投资是重要股东，具有政策性保障含义</li>\n<li><strong>下修+拉正股</strong>：公司有意愿也有能力通过拉正股化解到期压力"
new_fund2 = "合肥国资背书</strong>：重要股东，面对86亿规模能分担多少不确定</li>\n<li><strong>核心压力</strong>：86亿转债到期（2027年7月），若触发*ST+机构出库"
if old_fund2 in text:
    text = text.replace(old_fund2, new_fund2, 1)
    changes += 1
    print("6. Updated 偿付资金来源 part 2")
else:
    print("6. MISS: 偿付资金来源 part 2")

# Add border style to 偿付资金来源 card
if 'border-left-color:#991b1b' not in text and '偿付资金来源（压力测试）' in text:
    # Already updated text above
    pass

# Fix 转债定价分析 - update the pricing card content
old_pricing_items = (
    "<li>转债价格105-114元（接近面值）反映市场对\"最终能还钱\"的信任，而非对正股的乐观</li>\n"
    "<li>YTM约3-4%，非极端高水平——市场并未定价违约概率很高</li>\n"
    "<li>信用评级A（展望负面）：已price in部分风险，但非垃圾债水平</li>\n"
    "<li>转股溢价率40%+：正股表现平平，转股概率低，更多是纯债属性</li>"
)
new_pricing_items = (
    "<li>转债价格98.845元（<strong>跌破面值</strong>）：市场对\"最终能还钱\"的信任<strong>正在动摇</strong></li>\n"
    "<li>YTM 8.74%：较此前的3-4%大幅飙升，市场正在<strong>定价较高违约风险</strong></li>\n"
    "<li>信用评级A（展望负面）：已接近垃圾债边缘，机构被迫出库</li>\n"
    "<li><strong>转股溢价率-2.58%</strong>：已转负——转债市场极罕见，正股前景极度不乐观</li>"
)
if old_pricing_items in text:
    text = text.replace(old_pricing_items, new_pricing_items, 1)
    changes += 1
    print("7. Updated 转债定价分析 card content")
else:
    print("7. MISS: 转债定价分析 card content")

# Fix 转债定价分析 title
if "<h4>当前市场定价逻辑</h4>" in text:
    text = text.replace(
        "<h4>当前市场定价逻辑</h4>",
        "<h4>当前市场定价逻辑（已发生根本性变化）</h4>",
        1
    )
    changes += 1
    print("8. Updated 转债定价分析 title")
else:
    print("8. MISS: 转债定价分析 title")

# Insert crash narrative before 转债定价分析 h3
crash_h3 = (
    '<h3>转债暴跌始末（2026年4月）</h3>\n'
    '<div class="lesson-card"><h4>8连阴：下修利好反成利空</h4>\n'
    '<ul><li><strong>4月8日</strong>：董事会确定下修转股价至32.66元（幅度25.1%，下修到底）</li>\n'
    '<li><strong>4月9日</strong>：转债开盘冲高至116.2元，回落收113.746元（-1.26%）</li>\n'
    '<li><strong>4月10日起</strong>：转股价生效，开启8连阴</li>\n'
    '<li><strong>4月20日</strong>：收98.845元（-1.11%），<strong>跌破面值100元</strong></li>\n'
    '<li><strong>4月21日</strong>：正股跌6.66%至29.29元，转债同步承压</li></ul></div>\n'
    '<div class="lesson-card" style="border-left-color:#991b1b"><h4>转债vs正股：为何背离？</h4>\n'
    '<ul><li>转股溢价率-2.58%：转债价格已低于转股价值，<strong>纯债属性超过股性</strong></li>\n'
    '<li>核心焦虑：4月30日年报，若审计出具"无法表示意见"将触发<strong>*ST退市警示</strong></li>\n'
    '<li>兴业证券：机构资金已在抛售，基金对弱资质品种持续出库</li></ul></div>\n'
)
insert_pt = '<h3>转债定价分析</h3>\n<div class="lesson-card"><h4>当前市场定价逻辑'
if insert_pt in text:
    text = text.replace(insert_pt, crash_h3 + insert_pt, 1)
    changes += 1
    print("9. Inserted crash narrative before 转债定价分析")
else:
    print("9. MISS: crash narrative insert point")

print(f"\nTotal: {changes} changes")

result = text.encode("utf-8")
if has_crlf:
    result = result.replace(b"\n", b"\r\n")

with open(filepath, "wb") as f:
    f.write(result)

print("Saved!")
