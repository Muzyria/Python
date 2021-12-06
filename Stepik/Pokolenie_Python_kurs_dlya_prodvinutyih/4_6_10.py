n, m = map(int, input().split())
l = [[0] * m for _ in range(n)]
num = 1
k = 0                                 # уровень квадрата: 0 - внешний, 1 - вложенный и т.д.
product = n * m + 1                   # вынесено в переменную, т.к. n и m меняются в цикле

while num < product:
    for j in range(k, m):             # верхняя сторона
        l[k][j] = num
        num += 1
    for i in range(k + 1, n):         # правая сторона
        l[i][j] = num
        num += 1
    if num == product:                # костыль для случаев с маленькими n, m
        break
    for j in range(m - 2, k - 1, -1): # нижняя сторона
        l[i][j] = num
        num += 1
    for i in range(n - 2, k, -1):     # левая сторона
        l[i][j] = num
        num += 1
    m -= 1                            # изменяю размер сторон для будущего квадрата
    n -= 1
    k += 1

for row in l:
    for el in row:
        print(str(el).ljust(3), end='')
    print()