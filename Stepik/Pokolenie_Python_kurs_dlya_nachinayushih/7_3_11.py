# put your python code here
n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += i
print(count)