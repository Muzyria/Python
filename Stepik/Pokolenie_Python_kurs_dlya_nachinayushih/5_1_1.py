# put your python code here
num = int(input())

a = (num % 100) // 10
b = num % 10

if a == 0 and b == 0:
    print('YES')
else:
    print('NO')