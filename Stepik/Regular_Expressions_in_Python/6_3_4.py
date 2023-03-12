import re, sys

text = ''.join(sys.stdin.readlines())
print(re.findall(r'(?m)^([$^]+)$', text))
