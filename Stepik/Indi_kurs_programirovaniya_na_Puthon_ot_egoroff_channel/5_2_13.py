# put your python code here
n = int(input())

for i in range(n):
    s = input()
    if len(s) > 10:
        s2 = len(s[1:-1])
        print(s[0] + str(s2) + s[-1])
    else: print(s)