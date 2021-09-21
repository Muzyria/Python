m, n = int(input()), int(input())

if m > n:
    for i in range(m, n - 1, -1):
        if i % 2 == 1:
            print(i)