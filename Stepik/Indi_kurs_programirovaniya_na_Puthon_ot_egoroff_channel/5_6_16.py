n, x = map(int, input().split())
matrix = []
count = 0

for i in range(n):
    matrix.append([0] * n)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        matrix[i-1][j-1] = i * j
    if x in matrix[i-1]:
        count += 1

print(count)