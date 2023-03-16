x, y = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(x)]

for i in range(x-2, -1, -1):
    for j in range(y-2, -1, -1):
        matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]

for i in matrix:
    print(*i)

