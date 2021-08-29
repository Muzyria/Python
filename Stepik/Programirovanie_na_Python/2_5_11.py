s = [int(i) for i in input().split()]
s.sort()
s1 = []
for i in s:
    if s.count(i) > 1 and i not in s1:
        s1.append(i)
print(*s1)