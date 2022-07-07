
s = "abab"
a = "ab"
b = "ba"

# s, a, b = [input() for _ in range(3)]

count = 0
flag = True

while a in s:
    if count < 1000:
        s = s.replace(a, b)
        count += 1
    else:
        flag = False
        break

print(count if flag else "Impossible")
