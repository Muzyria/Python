n = int(input())
matrix = [[1]*n for _ in range(n)]

[print(*row) for row in matrix]