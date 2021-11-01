a = []
n, m = map(int, input().split())
smax, sum_throw, player = 0, 0, 0

for i in range(n):
    a.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        if a[i][j] > smax:
            smax = a[i][j]
            sum_throw = sum(a[i])
            player = i
        elif a[i][j] == smax:
            if sum_throw < sum(a[i]):
                sum_throw = sum(a[i])
                player = i
            
            
print(player)
