# put your python code here
n, m = map(int, input().split())
count = 0
a, b = [], []
for i in range(n):  
    b = []
    for j in range(m):
        b.append(count)
        count += 1
    a.append(b) 
    
for i in range(n):  
    if i % 2 == 0:
        print(*a[i])
    else: 
        print(*a[i][::-1])