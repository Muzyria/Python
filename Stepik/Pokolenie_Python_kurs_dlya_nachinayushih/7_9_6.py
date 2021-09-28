# put your python code here
n = int(input())
a = 1
b = 0
for i in range(1, n + 1):
    a *= i
    b += a
print(b)
