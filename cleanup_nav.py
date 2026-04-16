"""Remove old .navbar system from index.html, keep #uni-navbar."""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Identify old navbar CSS rule prefixes
old_rules = [
    '.navbar{', '.navbar ', '.nav-brand{', '.nav-brand ',
    '.nav-links{', '.nav-links ', '.nav-link{', '.nav-link ',
    '.hamburger{', '.hamburger ', '.hamburger:',  # colon for :hover etc
    '.mobile-overlay{', '.mobile-overlay ', '.mobile-overlay:',
    '.mobile-drawer{', '.mobile-drawer ', '.mobile-drawer:',
    '.drawer-header{', '.drawer-header ',
    '.drawer-brand{', '.drawer-brand ',
    '.drawer-close{', '.drawer-close ',
    '.drawer-nav{', '.drawer-nav ',
    '.drawer-theme{', '.drawer-theme ',
    '.search-box{', '.search-box ',
]

# Also remove @media lines that ONLY contain old navbar rules
# and blank lines that are between CSS blocks (cleanup)

new_lines = []
skip_until_blank = False
skip_blank_after_old_css = False
i = 0

while i < len(lines):
    line = lines[i]
    
    # Skip lines that are exclusively old navbar CSS rules
    stripped = line.strip()
    
    is_old_css = False
    for prefix in old_rules:
        if stripped.startswith(prefix):
            is_old_css = True
            break
    
    # Also skip if this line is entirely an old navbar CSS block (multi-rule single line)
    # Check for patterns like ".navbar{...}" or ".nav-link{...}" as the whole line
    if re.match(r'^\.navbar\{', stripped): is_old_css = True
    elif re.match(r'^\.nav-brand\{', stripped): is_old_css = True
    elif re.match(r'^\.nav-links\{', stripped): is_old_css = True
    elif re.match(r'^\.nav-link', stripped): is_old_css = True
    elif re.match(r'^\.hamburger', stripped): is_old_css = True
    elif re.match(r'^\.mobile-overlay', stripped): is_old_css = True
    elif re.match(r'^\.mobile-drawer', stripped): is_old_css = True
    elif re.match(r'^\.drawer-header', stripped): is_old_css = True
    elif re.match(r'^\.drawer-brand', stripped): is_old_css = True
    elif re.match(r'^\.drawer-close', stripped): is_old_css = True
    elif re.match(r'^\.drawer-nav', stripped): is_old_css = True
    elif re.match(r'^\.drawer-theme', stripped): is_old_css = True
    elif re.match(r'^\.search-box', stripped): is_old_css = True
    
    if is_old_css:
        skip_until_blank = True
        i += 1
        continue
    
    # Skip the universal reset line that precedes old navbar blocks (only in style blocks)
    # Pattern: line before old navbar is *{box-sizing}, line after is .navbar{
    if (stripped.startswith('*{box-sizing:border-box') and 
        i + 1 < len(lines) and
        lines[i+1].strip().startswith('.navbar{')):
        # This *{box-sizing} is part of the old navbar CSS block — skip it
        i += 1
        continue
    
    # Skip blank lines that immediately follow old navbar CSS (cleanup)
    if skip_until_blank:
        if stripped == '':
            skip_until_blank = False
            i += 1
            continue
        else:
            # Non-blank after old CSS but not old CSS itself — stop skipping
            skip_until_blank = False
    
    new_lines.append(line)
    i += 1

print(f"Original: {len(lines)} lines")
print(f"Cleaned:  {len(new_lines)} lines")
print(f"Removed:  {len(lines) - len(new_lines)} lines")

with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(new_lines))

print("Done!")
