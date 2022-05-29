'''
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))
'''
s = [int(input()) for i in range(5)]
print('Наименьшее число =', min(s))
print('Наибольшее число =', max(s))