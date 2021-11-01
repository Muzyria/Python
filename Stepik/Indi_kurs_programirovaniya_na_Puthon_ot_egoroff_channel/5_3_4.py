# put your python code here
n = list(map(int, input().split()))
s = max(n)
for i in n:
    if s > i and i > 0:
        s = i
if s > 0: print(s)
else: print('Empty')