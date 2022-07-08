import re
import sys

pattern = r'\b[Aa]+\b'

for line in sys.stdin:
    print(re.sub(pattern, 'argh', line.rstrip(), 1))
