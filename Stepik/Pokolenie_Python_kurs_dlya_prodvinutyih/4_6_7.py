
n, m = map(int, input().split())
s = []

for i in range(n):
    s.append([str(j +1) for j in range(m)])
       
for i in range(n):
    for j in range(m):
        s[i][j] = (i  + j) % m + 1
        
for i in range(n):
    for j in range(m):
        print(str(s[i][j]).ljust(3), end='')
    print()