a = []
b = input()
while b != 'end' :
    a.append([int(i) for i in b.split()])
    b = input()
c = []
for i in range(len(a)):
    c.append([])
    for j in range(len(a[0])):
        c[i].append(a[i-1][j]+a[(i+1)%(len(a))][j]+a[i][j-1]+a[i][(j+1)%(len(a[0]))])
for a in c:
    print(*a)