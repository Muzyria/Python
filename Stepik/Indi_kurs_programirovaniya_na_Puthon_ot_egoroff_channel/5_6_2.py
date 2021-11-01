# put your python code here
c = int(input())
s = 0
a = []
for i in range(c):
    a.append(list(map(int, input().split())))

for l in range(c):
    for k in range(c):
        if l == k:
            s += a[l][k]
print(s)