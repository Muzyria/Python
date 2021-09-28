# put your python code here
num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit, end='')
    num = num // 10