n = int(input())
a = list(map(int,input().split()))
s = []
for i in range(n):
    s.append(a[a.index(min(a))])
    a.pop(a.index(min(a)))
print(*s)
