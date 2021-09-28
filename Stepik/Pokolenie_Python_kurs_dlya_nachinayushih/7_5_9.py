num = int(input())
x1 = 9
x2 = 0
while num != 0:
    last_digit = num % 10
    if last_digit > x2:
        x2 = last_digit
    if last_digit < x1:
        x1 = last_digit 
    num = num // 10
if x1 == x2:
    print('YES')
else:
    print('NO')