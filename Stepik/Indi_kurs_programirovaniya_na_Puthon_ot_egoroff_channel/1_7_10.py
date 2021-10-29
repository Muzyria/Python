# put your python code here
s = int(input())
h = s // 3600
m = (s - h * 3600) // 60
m1 = m // 10
sek = s % 60
sek1 = sek // 10
if m1 > 0:
    m1 = str('')
if sek1 > 0:
    sek1 = str('')    

print(h, ':', m1, m, ':', sek1, sek, sep='')