import re

for i in range(int(input())):
    res = re.findall(r'<a href="(.*)">(.*)</a>', input())
    if res:
        print(res[0][0], res[0][1], sep=', ')
