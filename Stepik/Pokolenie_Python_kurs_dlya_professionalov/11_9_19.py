import re


a, b = map(int, input().split())
regex_obj = re.compile(r'\d+')
result = regex_obj.findall(input(), pos=a, endpos=b)

print(sum([int(i) for i in result]))
