# put your python code here
l = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
n = []
for i in range(len(l)):
    n.append(l[i] + m[i])
print(*n)
