# put your python code here
n, m = map(int, input().split())
a = []
z = '#Color'
for i in range(n):
    a.append(input())

for i in range(n):
    for j in range(m):
        if a[i][j] == 'W' or a[i][j] == 'B':
            z ='#Black&White'
            
        
print(z)    