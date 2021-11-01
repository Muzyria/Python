a=int(input())
c = 0
i = 0
while c != a:
    c += 1
    if a % c == 0:
        i += c
print(i)
