# put your python code here
n,m = map(int, input().split())
a = []
s = []
for i in range(n):
    a.append(list(map(int, input().split()))) # читаем матрицу
for i in range(n):
    s.append(sum(a[i]))
print(max(s), s.index(max(s)), sep='\n')