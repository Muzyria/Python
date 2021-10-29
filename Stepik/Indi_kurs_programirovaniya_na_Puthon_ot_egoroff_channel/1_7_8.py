# put your python code here
n = int(input())
h = n // 60
m = n % 60
if h > 24:
    h %= 24
print(h, m)