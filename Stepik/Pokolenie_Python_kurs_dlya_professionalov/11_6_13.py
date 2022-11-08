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
