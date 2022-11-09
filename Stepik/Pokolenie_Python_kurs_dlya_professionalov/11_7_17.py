import sys
import re

res = {}
for tag, params in re.findall(r'<(\w+)(.*?)>', sys.stdin.read()):
    res.setdefault(tag, set()).update(re.findall(r'([\w-]+)=', params))
for k, v in sorted(res.items()):
    print(k+':', ', '.join(sorted(v)))
