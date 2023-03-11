import re

print(re.sub(r'(\w+) \1', r'\1', input()))
