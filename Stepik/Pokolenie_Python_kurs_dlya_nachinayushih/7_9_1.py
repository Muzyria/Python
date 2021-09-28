n = int(input())
t = 1
for j in range(1, n + 1):
    for i in range(1, j + 1):
        print(t, end=' ')
        t += 1
    print()