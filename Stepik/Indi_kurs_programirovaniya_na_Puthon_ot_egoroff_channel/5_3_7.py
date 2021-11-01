# put your python code here
n = input()
digit = 0
count = 0
for i in n:
    if i in '0123456789':
        digit += 1
        count += int(i)
print(digit, count)