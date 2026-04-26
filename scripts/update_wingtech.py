#!/usr/bin/env python3
# -*- coding: utf-8 -*-
filepath = r"C:\Users\hozen\.openclaw\workspace\li-lu-research\wingtech-analysis.html"

with open(filepath, "rb") as f:
    raw = f.read()

# Normalize to LF for matching, remember original crlf status
has_crlf = b"\r\n" in raw
content = raw.replace(b"\r\n", b"\n")

# Decode to string for easy text replacement
text = content.decode("utf-8")

# --- Simple numeric replacements ---
replacements = [
    ("43.60元/股（2024年11月向下修正）", "32.66元/股（2026年4月10日下修生效）"),
    ("约31元（2026年3月）", "29.29元（-6.66%，4月21日）"),
    ("~105-114元（2026年3-4月）", "98.845元（跌破面值，4月20日）"),
    ("43.60元，转股溢价率收窄", "32.66元，转股溢价率收窄"),
    ("正股涨超43.60元", "正股涨超32.66元"),
    ("数据截止2026年3月。<br>", "数据截止<strong>2026年4月21日</strong>。<br>"),
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        print(f"OK: {old[:40]}")
    else:
        print(f"MISS: {old[:40]}")

# Insert new rows after "到期赎回价" row in the bond table
insert_after = '<tr><td>到期赎回价</td><td>108元/张（含最后一年利息2%）</td></tr>'
new_rows = ('<tr><td>到期收益率</td><td><strong style="color:#c53030">8.74%（市场定价高风险）</strong></td></tr>'
            '<tr><td>转股溢价率</td><td><strong style="color:#c53030">-2.58%（已转负，市场罕见）</strong></td></tr>'
            '<tr><td>下修进度</td><td>✅ 已完成！4月10日生效，转股价32.66元</td></tr>'
            '<tr><td>年报风险</td><td><strong style="color:#991b1b">⚠️ 4月30日披露，*ST风险</strong></td></tr>')

if insert_after in text:
    text = text.replace(insert_after, insert_after + new_rows, 1)
    print("Inserted new rows after 到期赎回价")
else:
    print("MISS: 到期赎回价 row")

# Remove 下修触发 row
old_trigger = '<tr><td>下修触发</td><td>已触发，董事会2026年3月提议下修转股价</td></tr>'
if old_trigger in text:
    text = text.replace(old_trigger, "")
    print("Removed 下修触发 row")
else:
    print("MISS: 下修触发 row")

# Add crash narrative before 转债定价分析 heading
crash_narrative = ('<h3>转债暴跌始末（2026年4月）</h3>\n'
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

target = '<h3>转债定价分析</h3>\n<div class="lesson-card"><h4>当前市场定价逻辑</h4>'
if target in text:
    text = text.replace(target, crash_narrative + target, 1)
    print("Inserted crash narrative")
else:
    print("MISS: 转债定价分析 heading")

# Update 转债定价逻辑 content
old_logic = ('<div class="lesson-card"><h4>当前市场定价逻辑</h4>\n'
             '<ul><li>转债价格105-114元（接近面值）反映市场对"最终能还钱"的信任，而非对正股的乐观</li>\n'
             '<li>YTM约3-4%，非极端高水平——市场并未定价违约概率很高</li>\n'
             '<li>信用评级A（展望负面）：已price in部分风险，但非垃圾债水平</li>\n'
             '<li>转股溢价率40%+：正股表现平平，转股概率低，更多是纯债属性</li></ul></div>')

new_logic = ('<div class="lesson-card"><h4>当前市场定价逻辑（已发生根本性变化）</h4>\n'
             '<ul><li>转债价格98.845元（<strong>跌破面值</strong>）：市场对"最终能还钱"的信任<strong>正在动摇</strong></li>\n'
             '<li>YTM 8.74%：较此前的3-4%大幅飙升，市场正在<strong>定价较高违约风险</strong></li>\n'
             '<li>信用评级A（展望负面）：已接近垃圾债边缘，机构被迫出库</li>\n'
             '<li><strong>转股溢价率-2.58%</strong>：已转负——转债市场极罕见，正股前景极度不乐观</li></ul></div>')

if old_logic in text:
    text = text.replace(old_logic, new_logic, 1)
    print("Updated 转债定价逻辑")
else:
    print("MISS: 转债定价逻辑 card")

# Update 3paths
old3 = ('<div class="lesson-card"><h4>转债三条路</h4>\n'
        '<ul><li><strong>转股（最优）</strong>：正股涨超43.60元，转股溢价率收窄，投资者转股，公司零偿付</li>\n'
        '<li><strong>下修转股价（大概率）</strong>：董事会已提议下修，降低转股门槛，促转股减轻到期压力</li>\n'
        '<li><strong>到期赎回（底线）</strong>：若无法转股，需备85.97亿现金，按108元/张赎回（含最后一年利息）</li></ul></div>')
new3 = ('<div class="lesson-card"><h4>转债三条路（已更新）</h4>\n'
        '<ul><li><strong>转股（最优）</strong>：正股需涨超32.66×1.3=42.46元（目前仅29.29元，差距44.8%）</li>\n'
        '<li><strong>下修转股价（已完成）</strong>：32.66元4月10日已生效，但正股持续下跌，转股价值仍低</li>\n'
        '<li><strong>到期赎回（底线风险上升）</strong>：若无法转股，需备85.97亿现金，按108元/张赎回</li></ul></div>')
if old3 in text:
    text = text.replace(old3, new3, 1)
    print("Updated 3paths")
else:
    print("MISS: 3paths")

# Update 偿付资金来源
old4 = ('<div class="lesson-card"><h4>偿付资金来源测算</h4>\n'
        '<ul><li><strong>ODM出售回款</strong>：43.89亿元已到账（大部分已完成交割）</li>\n'
        '<li><strong>半导体经营现金流</strong>：年化约20-25亿（按H1 2025 annualized），足以覆盖利息</li>\n'
        '<li><strong>合肥国资背书</strong>：合肥东方投资是重要股东，具有政策性保障含义</li>\n'
        '<li><strong>下修+拉正股</strong>：公司有意愿也有能力通过拉正股化解到期压力</li></ul></div>')
new4 = ('<div class="lesson-card" style="border-left-color:#991b1b"><h4>偿付资金来源（压力测试）</h4>\n'
        '<ul><li><strong>ODM出售回款</strong>：43.89亿元已到账（大部分完成交割）</li>\n'
        '<li><strong>半导体现金流</strong>：年化20-25亿，但安世控制权受限导致不确定性上升</li>\n'
        '<li><strong>合肥国资背书</strong>：重要股东，面对86亿规模能分担多少不确定</li>\n'
        '<li><strong>核心压力</strong>：86亿转债到期（2027年7月），若触发*ST+机构出库，局面将极其被动</li></ul></div>')
if old4 in text:
    text = text.replace(old4, new4, 1)
    print("Updated funding section")
else:
    print("MISS: funding section")

# Update conclusion title
old5 = '<div class="highlight"><h4>第三层结论：信息不足（偏正面）</h4>'
new5 = '<div class="highlight"><h4>第三层结论更新：风险显著上升，逻辑仍在但需等待</h4>'
if old5 in text:
    text = text.replace(old5, new5, 1)
    print("Updated conclusion title")
else:
    print("MISS: conclusion title")

# Encode back
result = text.encode("utf-8")

# Restore CRLF if original had it
if has_crlf:
    result = result.replace(b"\n", b"\r\n")

with open(filepath, "wb") as f:
    f.write(result)

print("\nAll done!")
