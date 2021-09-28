n = int(input())
max_digit = -1 # берем максимальное число '-1' что б пройти проверку если среди введеных цифр будет '0'
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit: # проверка или цифра числа максимальная
            max_digit = digit
    n = n // 10 # уменьшаем число на один знак
if max_digit < 0: # если условие не истина, значит чисел чисел кратных "3" не было
    print('NO')
else:
    print(max_digit)