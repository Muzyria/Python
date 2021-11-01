# put your python code here
n, m=map(int, input().split())
s=[]
maxi=0
kolvo=0
for i in range(n):
    s.append(list(map(int, input().split())))
    for j in range(m):
        if s[i][j] > maxi:
            maxi = s[i][j]
for i in s:
    if maxi in i:
        kolvo+=1
print(kolvo)