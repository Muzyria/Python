
s = input()
while '()' in s:
    s = s.replace('()', '')
print(False if s else True)
