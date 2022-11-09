import re, sys

for i in sys.stdin:
    res = re.findall(r'<a href="(.*)">(.*)</a>', i)
    if res:
        print(res[0][0], res[0][1], sep=', ')
