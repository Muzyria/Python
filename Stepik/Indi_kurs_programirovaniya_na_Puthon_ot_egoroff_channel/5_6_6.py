# put your python code here
n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n-1, -1, -1):
    for j in range(m ):
        print(a[i][j], end=' ')
    print()