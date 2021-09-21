from math import *


n = int(input())
count = 1
for i in range(2, n + 1):
    count += 1 / i
count -= log(n)
print(count)
        