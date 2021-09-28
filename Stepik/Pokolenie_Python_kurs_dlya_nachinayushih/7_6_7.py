# put your python code here
n = int(input())
num = n
for i in range(2, n, 1):
    if n % i == 0 and num > i:
        num = i 
        break
print(num)