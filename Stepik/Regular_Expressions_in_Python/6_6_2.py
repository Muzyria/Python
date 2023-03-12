import re, sys

text = ''.join(sys.stdin.readlines())
print(re.findall(r'(?s)start(.+)end', text))
