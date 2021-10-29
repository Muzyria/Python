# put your python code here
x, y, z = int(input()), int(input()), int(input())
f1 = x + y * z
f2 = x * (y + z)
f3 = x * y * z
f4 = (x + y) * z
f5 = x + y + z
print(max(f1, f2, f3, f4, f5))