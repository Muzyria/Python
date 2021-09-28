# put your python code here
n = int(input())

for j in range(1, n // 2 + 2):
    for i in range(1, j + 1):
        print('*', end='')
    print()
for j in range(n // 2 + 1, 1, -1):
    for i in range(1, j):
        print('*', end='')
    print()