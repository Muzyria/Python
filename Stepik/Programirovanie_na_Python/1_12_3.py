a = float(input())
b = float(input())
z = str(input())
if b==0 and (z=='/' or z=='mod'or z=='div'):
    print("Деление на 0!")
elif z=='+':
    print(a+b)
elif z=='-':
    print(a-b)
elif z=='*':
    print(a*b)
elif z=='/':
    print(a/b)
elif z=='mod':
    print(a%b)
elif z=='div':
    print(a//b)
elif z=='pow':
    print(a**b)