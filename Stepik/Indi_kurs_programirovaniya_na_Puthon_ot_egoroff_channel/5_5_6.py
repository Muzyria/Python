N = int(input())
n = list(map(int, input().split()))
c = 0
for i in range(N - 1):
    for j in range(N - i - 1):
        if n[j] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]
            c += 1
print(*n)
print(c)