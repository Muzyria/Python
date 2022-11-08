import sys, re

pattern_3 = r'^beegeek.*beegeek$'
pattern_2 = r'^beegeek|beegeek$'
pattern_1 = r'beegeek'

points = 0
for i in sys.stdin.readlines():
    if re.search(pattern_3, i.strip()):
        points += 3
    elif re.search(pattern_2, i.strip()):
        points += 2
    elif re.search(pattern_1, i.strip()):
        points += 1
print(points)

# import sys
# import re
# text = map(str.rstrip, sys.stdin)
# total = 0
# for line in text:
#     res = re.search(r'(^beegeek.*beegeek$)|(^beegeek.+|.+beegeek$)|(.+beegeek.+)', line)
#     if res:
#         for i, val in enumerate(res.groups()):
#             if val is not None:
#                 total += 3 - i
# print(total)
