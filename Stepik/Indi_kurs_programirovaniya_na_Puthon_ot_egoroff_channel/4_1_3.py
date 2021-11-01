# put your python code here
a, b = map(int, input().split())
count = 0
while a <= b:
    count += 1
    a *= 3
    b *= 2
print(count)
