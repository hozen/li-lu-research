#!/usr/bin/env python3
# -*- coding: utf-8 -*-
filepath = r"C:\Users\hozen\.openclaw\workspace\li-lu-research\wingtech-analysis.html"

with open(filepath, "rb") as f:
    raw = f.read()

has_crlf = b"\r\n" in raw
text = raw.replace(b"\r\n", b"\n").decode("utf-8")

# Find exact content around 偿付
idx = text.find("偿付资金来源测算")
if idx >= 0:
    segment = text[idx:idx+250]
    print("偿付 around index", idx)
    print(repr(segment[:200]))
    print()
    # Check for literal newline vs \n
    for i, c in enumerate(segment[:80]):
        if c == '\n':
            print(f"  pos {i}: ACTUAL NEWLINE")
        elif c == '\\':
            print(f"  pos {i}: BACKSLASH")
