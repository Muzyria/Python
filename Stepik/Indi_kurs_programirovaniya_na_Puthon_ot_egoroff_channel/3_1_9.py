# put your python code her
s = input()
if len(s) < 6:
    s = s.rjust(6, '0')
l = int(s[0]) + int(s[1]) + int(s[2])
r = int(s[3]) + int(s[4]) + int(s[5])

print('YES' if l == r else 'NO')