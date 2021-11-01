n = int(input())
sp = list(map(int, input().split()))
for i in range(n):
    while i != 0 and sp[i] < sp[i - 1]:
        sp[i], sp[i - 1] = sp[i - 1], sp[i]
        i -= 1
print(*sp)