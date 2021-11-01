# put your python code here
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if a[i][0] == a[j][1]:
            count += 1
print(count)