# put your python code here
x, y = map(int, input().split())
day = 1
while x <= y:
    x = x + (x *0.15)
    day += 1
print(day)
