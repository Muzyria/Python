# put your python code here
a = []
n, m = map(int, input().split())
smax, x, y = 0, 0, 0

for i in range(n):
    a.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        if a[i][j] > smax:
            smax, x, y = a[i][j], i, j
print(smax)
print(x, y)