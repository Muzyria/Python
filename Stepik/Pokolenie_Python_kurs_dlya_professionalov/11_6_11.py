import re
import sys

pat = r'\b(\w+)\1\b'
for line in sys.stdin:
    if re.search(pat, line):
        print(line.strip())
