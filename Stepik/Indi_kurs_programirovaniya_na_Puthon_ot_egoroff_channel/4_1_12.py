# put your python code here
n, m = map(int, input().split())
a = 0
b = 0
while (a ** 2 <= n):
    if (a + (n - a ** 2) **2 ) == m:
        b += 1
    a += 1
print(b)