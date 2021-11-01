# put your python code here
'''
# put your python code here
a, b = map(int, input().split())
x = []
if a <= b:
    for i in range(a, b +1):
        x.append(i ** 2)
elif a > b:
    for i in range(b, a +1)[::-1]:
        x.append(i ** 3)
print(x)        

'''
a, b = map(int, input().split())
print([i**2 for i in range(a, b + 1)] or [i**3 for i in range(a, b - 1, -1)])