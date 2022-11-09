import re, sys


pat = r'(beegeek)'

count = 0
for line in sys.stdin:
    if re.search(pat, line.strip(), re.I):
        count += 1
print(count)
