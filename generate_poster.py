#!/usr/bin/env python3
"""Li Lu Research poster v4 — light background, editorial style."""

from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1080, 1440
BG = (247, 248, 250)        # 浅灰白
NAVY = (10, 22, 40)         # 深蓝
GOLD = (201, 162, 39)        # 金色
GOLD_DIM = (160, 130, 60)
TEXT = (28, 28, 32)
MUTED = (110, 118, 130)
DIVIDER = (220, 222, 226)

FONT = "C:/Windows/Fonts/NotoSerifSC-VF.ttf"

def fnt(size): return ImageFont.truetype(FONT, size)

def main():
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    # ── TOP GOLD BANNER ─────────────────────────────
    draw.rectangle([0, 0, W, 8], fill=GOLD)

    # ── HEADER ──────────────────────────────────────
    fnt_tag = fnt(15)
    draw.text((80, 50), "喜马拉雅资本 · Himalaya Capital", font=fnt_tag, fill=MUTED)

    draw.line([(80, 80), (W-80, 80)], fill=DIVIDER, width=1)

    # Main title
    fnt_title = fnt(90)
    draw.text((80, 95), "李录研究", font=fnt_title, fill=NAVY)

    fnt_sub = fnt(26)
    draw.text((80, 205), "北大光华 · 哥大商学院 · 价值投资", font=fnt_sub, fill=MUTED)

    fnt_url = fnt(20)
    draw.text((80, 252), "oldmacdonald.xyz", font=fnt_url, fill=GOLD)

    draw.line([(80, 295), (W-80, 295)], fill=DIVIDER, width=1)

    # ── QUOTE CARD ───────────────────────────────────
    # Light card with left gold accent
    draw.rectangle([80, 320, W-80, 440], fill=(255, 255, 255))
    draw.rectangle([80, 320, 88, 440], fill=GOLD)  # Left gold bar
    draw.rectangle([80, 320, W-80, 440], outline=DIVIDER, width=1)

    fnt_quote = fnt(22)
    quote_lines = [
        "只投资于真正理解的行业和公司，",
        "在公司被市场误解时买入，",
        "在市场贪婪时保持理性。",
    ]
    for i, line in enumerate(quote_lines):
        draw.text((110, 340 + i*36), line, font=fnt_quote, fill=TEXT)

    fnt_src = fnt(15)
    draw.text((110, 462), "— 李录", font=fnt_src, fill=MUTED)

    # ── GOLD DIVIDER ─────────────────────────────────
    draw.line([(80, 480), (W-80, 480)], fill=GOLD, width=2)

    # ── CONTENT GRID — 3 COLUMNS ────────────────────
    cols = [
        ("投资框架", [
            "Morris SDI 文明测量体系",
            "Morris「For Now」操作化",
            "China 2.5 三层晴雨表",
            "Buffett/Munger 原典研究",
            "Bruce Greenwald 护城河",
        ]),
        ("深度案例", [
            "腾讯控股 · 护城河分析",
            "阿里巴巴 · 悖论转型",
            "拼多多 · 结构性竞争",
            "比亚迪 · 经典投资案例",
            "美国银行 · 危机买入",
        ]),
        ("演讲/采访", [
            "北大光华系列（2015-2024）",
            "哥大商学院 Fireside Chat",
            "2021 CBS 采访全集",
            "Morris 2011 预测复盘",
            "价值投资实践知行合一",
        ]),
    ]

    col_w = (W - 160) // 3
    start_x = [80, 80 + col_w, 80 + col_w * 2]
    y = 510

    for ci, (sec_title, items) in enumerate(cols):
        cx = start_x[ci]

        # Section header with gold underline
        fnt_sh = fnt(18)
        draw.text((cx, y), sec_title, font=fnt_sh, fill=NAVY)
        bbox = draw.textbbox((cx, y), sec_title, font=fnt_sh)
        tw = bbox[2] - bbox[0]
        draw.line([(cx, y+28), (cx+tw, y+28)], fill=GOLD, width=2)

        y_items = y + 48
        fnt_it = fnt(16)
        for item in items:
            draw.ellipse([cx, y_items+6, cx+6, y_items+12], fill=GOLD)
            draw.text((cx+16, y_items), item, font=fnt_it, fill=TEXT)
            y_items += 32

    # ── BOTTOM ───────────────────────────────────────
    draw.line([(80, H-120), (W-80, H-120)], fill=DIVIDER, width=1)

    fnt_dis = fnt(15)
    draw.text((80, H-100), "仅供研究参考，不构成投资建议", font=fnt_dis, fill=MUTED)

    # Right side: URL + year
    fnt_bot_url = fnt(16)
    bbox = draw.textbbox((0, 0), "oldmacdonald.xyz", font=fnt_bot_url)
    tw = bbox[2] - bbox[0]
    draw.text((W-80-tw, H-100), "oldmacdonald.xyz", font=fnt_bot_url, fill=GOLD)

    fnt_year = fnt(14)
    bbox = draw.textbbox((0, 0), "2026 · Li Lu Research Project", font=fnt_year)
    tw = bbox[2] - bbox[0]
    draw.text(((W-tw)//2, H-65), "2026 · Li Lu Research Project", font=fnt_year, fill=MUTED)

    # Decorative bottom bar
    draw.rectangle([0, H-6, W, H], fill=GOLD)

    # ── CORNER ACCENTS ────────────────────────────────
    # Top left L-shape
    draw.line([(40, 30), (40, 50)], fill=GOLD, width=3)
    draw.line([(40, 30), (60, 30)], fill=GOLD, width=3)
    # Top right L-shape
    draw.line([(W-40, 30), (W-40, 50)], fill=GOLD, width=3)
    draw.line([(W-40, 30), (W-60, 30)], fill=GOLD, width=3)
    # Bottom left
    draw.line([(40, H-30), (40, H-50)], fill=GOLD, width=3)
    draw.line([(40, H-30), (60, H-30)], fill=GOLD, width=3)
    # Bottom right
    draw.line([(W-40, H-30), (W-40, H-50)], fill=GOLD, width=3)
    draw.line([(W-40, H-30), (W-60, H-30)], fill=GOLD, width=3)

    output = "C:/Users/hozen/.openclaw/wtdev/poster.png"
    img.save(output, 'PNG', quality=95)
    print(f"OK: {output}")

if __name__ == "__main__":
    main()
