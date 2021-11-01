# put your python code here
a, b = [], []
n, m = map(int, input().split())
count = 0

for i in range(n):
    a.append(input())
input()
for i in range(n):
    b.append(input())
    
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            count += 1
    
    
print(count)