#!/usr/bin/env python3
# -*- coding: utf-8 -*-
filepath = r"C:\Users\hozen\.openclaw\workspace\li-lu-research\wingtech-analysis.html"

with open(filepath, "rb") as f:
    raw = f.read()

text = raw.replace(b"\r\n", b"\n").decode("utf-8")

# Find all occurrences of key markers
for marker in ["转债三条路", "偿付资金来源", "转债定价分析", "当前市场定价逻辑"]:
    idx = text.find(marker)
    if idx >= 0:
        print(f"\n=== {marker} (first at {idx}) ===")
        print(repr(text[idx:idx+300]))
    else:
        print(f"\n=== {marker}: NOT FOUND ===")
