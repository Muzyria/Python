import re
import sys

pat = r'_\d+\w*_?'
for line in sys.stdin:
    print(True if re.search(pat, line) else False)
