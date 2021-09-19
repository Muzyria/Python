from math import *


a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - (4 * a * c)
if D < 0:
    print('Нет корней')
elif D == 0:
    print(-b / (2 * a))
elif D > 0:
    print(min((-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a)     ))
    print(max((-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a)     ))
