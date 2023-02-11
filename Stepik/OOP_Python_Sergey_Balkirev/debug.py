s = input()
while '()' in s:
    s = s.replace('()', '')
print('NO' if s else 'YES')
