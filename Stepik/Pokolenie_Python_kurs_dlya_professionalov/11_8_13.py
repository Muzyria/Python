import re

def fun(a):
    a1 = int(a.group(1))
    a2 = a.group(2)
    return a1*a2

a = re.sub(r'(\d+)\((\w+)\)', fun, input())

while '(' in a:
    a = re.sub(r'(\d+)\((\w+)\)', fun, a)
print(a)
