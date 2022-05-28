'''
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if  b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
elif a2 <= a1 and b2 >= b1:
    print(a1, b1)
elif a1 < a2 and b1 > b2:
    print(a2, b2)
elif a1 <= a2 < b1 and b1 <= b2:
    print(a2, b1)
elif a2 <= a1 < b2 and b2 <= b1:
    print(a1, b2)
else:
    print('пустое множество')
'''
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
a = max(a1, a2) 
b = min(b1, b2)
if a < b: print(a,b)
elif a == b: print(a)
else: print("пустое множество")    