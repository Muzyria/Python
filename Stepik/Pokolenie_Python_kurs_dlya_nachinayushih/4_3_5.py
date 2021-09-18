# put your python code here
x, y, z = int(input()), int(input()), int(input())
if y < x < z or y > x > z:
    print(x)  
elif x < y < z or x > y > z:
    print(y)
elif x < z < y or x > z > y:
    print(z)