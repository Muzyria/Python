# put your python code here
a = int(input())
count = 0
while a >= 1 and a % 2 == 0:
    a //= 2
    count += 1
print(count if a == 1 else 'НЕТ')