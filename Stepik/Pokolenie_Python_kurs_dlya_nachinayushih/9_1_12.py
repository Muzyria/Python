n = input()
q = 0
w = 0

for i in range(0, len(n)):
    if '*' == n[i]:
        q += 1
    if '+' == n[i]:
        w += 1
print('Символ + встречается', w, 'раз')
print('Символ * встречается', q, 'раз')