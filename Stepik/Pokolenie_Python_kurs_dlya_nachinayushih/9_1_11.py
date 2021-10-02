# put your python code here
n = input()
q = 0
for i in range(0, 10):
    if str(i) in n:
        
        q += 1
if q == 0:
    print('Цифр нет')
else:
    print('Цифра')