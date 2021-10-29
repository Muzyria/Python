# put your python code here
n = int(input())
d100 = n // 100
n %= 100
d20 = n // 20
n %= 20
d10 = n // 10
n %= 10
d5 = n // 5
n %= 5
d1 = n // 1
n %= 1
print(d100 + d20 + d10 + d5 + d1)