# put your python code here
s = list(input().lower())
w = []
for i in range(len(s)):
    if s[i] not in 'aoyeui':
        w.append(s[i])
print('.', end='')            
print(*w, sep='.')