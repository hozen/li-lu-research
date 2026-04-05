with open(r"C:\Users\hozen\.openclaw\workspace\li-lu-research\index.html", "rb") as f:
    raw = f.read()
if raw[:3] == b'\xef\xbb\xbf':
    raw = raw[3:]
html = raw.decode("utf-8", errors="replace")

# Find "2008年" in raw bytes
idx = raw.find(b'2008')
print(f"2008 at byte: {idx}")

# Show the full timeline item
# Find "timeline-item" before 2008
tidx = raw.rfind(b'timeline-item', 0, idx+10)
print(f"timeline-item before 2008 at: {tidx}")
print("Timeline item hex:")
item = raw[tidx:idx+500]
# Print hex of Chinese part
for i, b in enumerate(item):
    if b > 127:
        print(f"  pos {i}: byte {b:02x}")
print("Text around 2008:")
# Find >2008<
start = raw.find(b'>', idx-5)
end = raw.find(b'<', idx+20)
print(raw[start:end+1])

# Find education
eidx = raw.find(b'MBA')
print(f"\nMBA at byte: {eidx}")
if eidx >= 0:
    print("Around MBA:", raw[eidx-30:eidx+100])
