# put your python code here
'''
# put your python code here
n = int(input())
d ={}
for i in range(1, n +1):
    d.setdefault(i, i ** 2)
print(d)
'''
#n = int(input())
print({x: x ** 2 for x in range(1, int(input()) + 1)})