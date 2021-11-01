x=float(input())
y=float(input())
z=input()
if z[0]=='+':
    print(x+y)
elif z[0]=='-':
    print(x-y)
elif z[0]=='*':
    print(x*y)
elif z[0]=='/':
    if y==0:
        print('Неизвестно')
    else:
        print(x/y)
else:
    print('Неизвестно')