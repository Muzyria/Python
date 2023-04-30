n = int(input())
matrix = [[1]*n for _ in range(n)]
step = n // 2

marker = 1
start = 0
finish = n

while step != 0:
    marker += 1
    start += 1
    finish -= 1
    for i in range(start, finish):
        for j in range(start, finish):
            matrix[i][j] = marker
    step -= 1

[print(*row) for row in matrix]
