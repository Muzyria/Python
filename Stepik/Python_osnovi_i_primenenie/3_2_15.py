import re
import sys

pattern = r'(\w)\1+'

for line in sys.stdin:
    print(re.sub(pattern, r'\1', line.rstrip()))
