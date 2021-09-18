# put your python code here
x, y, z = int(input()), int(input()), int(input())
if x == y == z:
    print('Равносторонний')  
elif x != y and x != z and y != z:
    print('Разносторонний')
else:
    print('Равнобедренный')