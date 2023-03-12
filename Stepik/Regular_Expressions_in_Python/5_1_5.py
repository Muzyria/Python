import re

regex = re.compile(r'\b[a-z]+\b')
s, a, b = input(), int(input()), int(input())
if (t := regex.search(s, pos=a, endpos=b)):
    print(t[0])
