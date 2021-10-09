s = []
char = ''
for i in range(26):
    char = chr(i + 97) * (i +1)
    s.append(char)
print(s)