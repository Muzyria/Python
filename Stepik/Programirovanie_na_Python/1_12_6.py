a = int(input())
x='программист'
y='программиста'
z='программистов'
if a==0:
    print(a,z)
elif a%100>=10 and a%100<=20:
    print(a,z)
elif a%10==1: 
    print(a,x)
elif a%10>=2 and a%10<=4:
    print(a,y)
else:
    print(a,z)