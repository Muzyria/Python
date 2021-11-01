# put your python code here
q = input()
w = input()
a = 'abcdefgh'
x1 = a.index(q[0]) + 1
x2 = int(q[1])
y1 = a.index(w[0]) + 1
y2 = int(w[1])
if (x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')