# put your python code here
n = int(input())
s = 0
count = 0
while n > 0:
    s = n % 10
    if s == 7: count += 1
    n = n // 10
print(count)