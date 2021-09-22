# put your python code here
i = int(input())
x = 0
while i >= 0 and i < 6:
    x += i == 5
    i = int(input())
print(x)