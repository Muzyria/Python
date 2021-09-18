# put your python code here
x = input()
y = input()

if x != 'синий' and x != 'желтый' and x != 'красный' or y != 'красный' and y != 'синий' and y != 'желтый':
   print('ошибка цвета')
elif (x == 'красный' or y == 'красный') and (x == 'синий' or y == 'синий'):
   print('фиолетовый')
elif (x == 'красный' or y == 'красный') and (x == 'желтый' or y == 'желтый'):
   print('оранжевый')
elif (x == 'синий' or y == 'синий') and (x == 'желтый' or y == 'желтый'):
   print('зеленый')
elif x == y and (x == 'синий' or x == 'желтый' or x == 'красный') and (y == 'красный' or y == 'синий' or y == 'желтый'):
   print(x)
