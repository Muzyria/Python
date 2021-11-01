s = input()
if (sum(map(int, s[::2])) - sum(map(int, s[1::2]))) % 11 == 0:
    print('YES')
else:
    print('NO')