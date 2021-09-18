# put your python code here
x = int(input())
if not 0 <= x <= 36:
    print('ошибка ввода')
elif x == 0:
    print('зеленый')    
    
elif 1 <= x <= 10 and x % 2 == 1 or 11 <= x <= 18 and x % 2 == 0 or 19 <= x <= 28 and x % 2 == 1 or 29 <= x <= 36 and x % 2 == 0:
    print('красный')
else:
    print('черный')    