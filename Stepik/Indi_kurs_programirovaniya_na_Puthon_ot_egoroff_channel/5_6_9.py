# put your python code here
n = int(input())
a = []
result = True
for i in range(n):
    a.append(list(map(int, input().split()))) # читаем матрицу
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]: 
            result = False
if result:
    print('Yes')
else:
    print('No')