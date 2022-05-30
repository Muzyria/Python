n, m = int(input()), int(input())

if n < m:
    for i in range(n, m + 1):
        print(i)
else:
    for i in range(n, m - 1, -1):
        print(i)

'''
m, n, s = int(input()), int(input()), 1
if m > n:
    s = -1
for i in range(m,n+s,s):
    print(i)
'''        