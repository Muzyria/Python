import re
import sys

pattern = r'\b(\w)(\w)(\w*)\b'

for line in sys.stdin:
    print(re.sub(pattern, r'\2\1\3', line.rstrip()))
