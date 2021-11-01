# put your python code here
a , b = map(int, input().split())
h = a
while a > 0:
    a //= b
    h += a
print(h)