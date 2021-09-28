num = int(input())
x1 = True
x2 = 0
while num > 9:
    last_digit = num % 10
    if num % 10 > (num // 10) % 10:
        x1 = False
    num = num // 10 
if x1 == False:
    print('NO')
else:
    print('YES')