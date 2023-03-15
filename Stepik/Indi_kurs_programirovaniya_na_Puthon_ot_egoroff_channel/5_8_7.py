x, y = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(x)]

for i in range(1, x):
    for j in range(1, y):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

for i in matrix:
    print(*i)
