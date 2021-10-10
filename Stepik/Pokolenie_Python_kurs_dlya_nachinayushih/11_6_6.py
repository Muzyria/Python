# put your python code here
n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])
nmin = n.index(min(n))
nmax = n.index(max(n))
n[nmin], n[nmax] = n[nmax], n[nmin] 
print(*n)