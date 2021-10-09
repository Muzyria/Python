s, result = input(), ''
for i in range(len(s)):
    if i % 3 == 0:
        continue
    result += s[i]
print(result)

'''
s = input()
for i in range(0, len(s)):
    if i % 3 != 0:
        print(s[i], end='')
    else:
        continue
'''