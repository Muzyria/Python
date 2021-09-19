m, p, n = int(input()), int(input()), int(input())

for i in range(n): 
    print(i + 1, m)
    m = m + (m / 100) * p