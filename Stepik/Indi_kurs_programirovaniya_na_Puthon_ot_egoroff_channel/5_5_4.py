n = int(input())
count = 0
for i in range(n + 1, 2*n):
    d = 0
    for j in range(2, round(i**0.5) + 1):
        if i % j == 0:
            d += 1
        if d > 0:
            break
    if d == 0:
        count += 1
print(count)