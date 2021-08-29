n = int(input())
res = []
for i in range(n + 1):
    for j in range(i):
        if len(res) == n:
            break
        res.append(i)
print(*res)