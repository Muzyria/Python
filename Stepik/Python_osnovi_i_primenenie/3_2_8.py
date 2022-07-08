import re
import sys
pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)