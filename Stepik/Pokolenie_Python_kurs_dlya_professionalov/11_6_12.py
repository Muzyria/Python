import re, sys

p1, p2 = r'(bee).*(bee)', r'(\bgeek\b)'
bee = geek = 0
for s in sys.stdin:
    m1 = re.search(p1, s)
    m2 = re.search(p2, s)
    if m1:
        bee += 1
    if m2:
        geek += 1
print(bee, geek, sep='\n')
