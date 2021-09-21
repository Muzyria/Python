m = int(input())
a, b, c = 0, 0, 1
for _ in range(m):
    a = b + c
    print(a, end=' ')
    c = b
    b = a