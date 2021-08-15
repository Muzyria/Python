f = str(input())
if f=='треугольник':
    a=float(input())
    b=float(input())
    c=float(input())
    p = (a + b + c) / 2
    s = (p * ((p - a) * (p - b) * (p - c))) ** 0.5
    print (s)
elif f=='прямоугольник':
    a=float(input())
    b=float(input())
    print(a*b)
elif f=='круг':
    r=float(input())
    print((r**2)*3.14)