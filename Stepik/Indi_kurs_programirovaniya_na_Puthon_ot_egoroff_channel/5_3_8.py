a = input()

while len(a) > 0:
    if '()' in a:
        a = a.replace('()', '')
    elif '[]' in a:
        a = a.replace('[]', '')
    elif '{}' in a:
        a = a.replace('{}', '')
    else:
        break

if len(a) == 0:
    print('YES')
else:
    print('NO')