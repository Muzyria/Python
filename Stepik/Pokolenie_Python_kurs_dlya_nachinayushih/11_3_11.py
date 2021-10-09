# put your python code here
n = int(input())
x = 0
s = []
for i in range(n):
    digit = int(input())
    x += digit
    s.append(x)
    x = digit
print(s[1:])