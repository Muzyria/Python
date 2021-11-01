# put your python code here
n, m = map(int, input().split())
count = 0
a = []
a.append('.' *(m +2))
for i in range(n):
    a.append('.' + input() + '.')
a.append('.' *(m +2))    


for i in range(1, n +1):
    for j in range(1, m +1):
        if a[i][j] == '.' and a[i][j +1] == '.' and a[i +1][j] == '.' and a[i][j -1] == '.' and a[i -1][j] == '.':
            count += 1
print(count)

