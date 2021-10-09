# put your python code here
n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
del s[1::2]
print(s)
