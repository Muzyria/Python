# put your python code here
a, b, c = int(input()), int(input()), input()

if b == 0 and c == '/': print('На ноль делить нельзя!')
elif c == '+': print(a + b)
elif c == '-': print(a - b)
elif c == '*': print(a * b)
elif c == '/': print(a / b)
else: print('Неверная операция')