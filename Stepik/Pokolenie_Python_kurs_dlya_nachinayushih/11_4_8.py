# put your python code here
n = int(input())
m1, m2, m3 = [], [], []
for _ in range(n):
    s = int(input())
    if s < 0:
        m1.append(s)
    elif s == 0:
        m2.append(s)
    else:
        m3.append(s)
print(*m1, *m2, *m3, sep='\n')