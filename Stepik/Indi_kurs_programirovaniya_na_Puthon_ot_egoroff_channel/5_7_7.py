r, c = map(int, input().split())
t = []
am = 0
for i in range(r):
    t.append(list(input()))
for i in range(r):
    if 'S' not in t[i] and t[i] != ['#'] * c:
        for k in range(c):
            if t[i][k] == '.':
                am += 1
                t[i][k] = '#'
for i in range(c):
    j = []
    for k in range(r):
        j.append(t[k][i])
    if 'S' not in j and j != ['#'] * r:
        for k in range(r):
            if j[k] == '.':
                am += 1
                t[k][i] = '#'
print(am)