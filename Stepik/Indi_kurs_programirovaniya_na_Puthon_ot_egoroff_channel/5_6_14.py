# put your python code here
a = []
result = True
for i in range(4):
    a.append(input())

for i in range(4 -1):
    for j in range(4 -1):
        if a[i][j] == a[i][j +1] and a[i][j] == a[i +1][j +1] and a[i][j] == a[i +1][j]:
            result = False
if result:
    print('Yes')
else:
    print('No')