from math import *


n, a = float(input()), float(input())
s = (n * a ** 2) / (4 * tan(pi / n))
print(s)

'''
towns = [input() for _ in range(3)]
print(min(towns, key=len), max(towns, key=len), sep='\n')
'''