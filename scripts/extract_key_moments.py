import re, sys

srt_file = sys.argv[1] if len(sys.argv) > 1 else "li-lu-byd-2026-full.srt"

with open(srt_file, "r", encoding="utf-8") as f:
    content = f.read()

# Extract all entries
entries = re.findall(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\n\d+\n|\n*$)', content, re.DOTALL)

keywords = [
    "巴菲特", "比亚迪", "投资", "买入", "卖出", "护城河", "第一次", "2002", "2003", "2008",
    "时机", "机会", "逻辑", "理解", "判断", "决策", " mistake", "错误", "教训",
    "王传福", "李录", "李黔", "喜马拉雅", "仓位", "持仓", "下跌", "上涨", "估值"
]

results = []
for idx, start, end, text in entries:
    text_clean = re.sub(r'<[^>]+>', '', text).strip()
    if not text_clean:
        continue
    for kw in keywords:
        if kw.lower() in text_clean.lower() or kw in text_clean:
            results.append(f"{start} --> {text_clean[:80]}")
            break

for r in results[:60]:
    print(r)
