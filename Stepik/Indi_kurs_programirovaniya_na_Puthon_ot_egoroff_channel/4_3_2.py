# put your python code here
a, b = map(int, input().split())
x = 2
delitel = 1
while x < a or x < b:
    if a % x == 0 and b % x == 0:
        delitel = x
        x += 1
    else:
        x += 1
print(delitel)

'''
a, b = map(int, input().split())
while a != b:
    if a < b:
        a, b = b, a
    a -= b
print(a)
'''