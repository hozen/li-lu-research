with open(r"C:\Users\hozen\.openclaw\workspace\li-lu-research\index.html", "rb") as f:
    raw = f.read()
if raw[:3] == b'\xef\xbb\xbf':
    raw = raw[3:]
html = raw.decode("utf-8", errors="replace")

# Fix BYD timeline - add note about early discovery
# Find and replace the BYD timeline item content
old = "2008\u5e74</div><div class=timeline-title>\u6295\u8d44\u65f6\u95f4\u7684\u8f6c\u6298</div><div class=timeline-content>\u6bd5\u4e1a\u4e8e\u535a\u58eb\u987f\u3001\u738b\u4f20\u798f\u7684\u4f01\u4e1a\u5bb6\u7cbe\u795e\uff0c\u4e8b\u5148\u6295\u8d44\u8005\u3002"
new = "2008\u5e74</div><div class=timeline-title>\u6295\u8d44\u65f6\u95f4\u7684\u8f6c\u6298</div><div class=timeline-content>\u674e\u5f55\u7ec6\u7814\u6bd5\uff0c\u738b\u4f20\u798f\u4e3b\u5bfc\uff0c\u4e8b\u5148\u6295\u8d44\uff0c2008\u5e74\u5df2\u5168\u90e8\u6301\u80a1\uff08\u5b9e\u9645\u4e0a\u4ed6\u57282002-2003\u5e74\u5c31\u5df2\u5173\u6ce8\u6bd4\u4e9a\u8f66\uff09\u3002"
if old in html:
    html = html.replace(old, new)
    print("Fixed BYD timeline - added early discovery note")
else:
    print("BYD old text not found")

# Fix paper title
old_paper = "cilivilized and Modern"
new_paper = "Civilizations, Modernization, Value Investing and China"
if old_paper in html:
    html = html.replace(old_paper, new_paper)
    print("Fixed paper title typo")
else:
    print("Paper title not found")

# Save
with open(r"C:\Users\hozen\.openclaw\workspace\li-lu-research\index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved successfully")
