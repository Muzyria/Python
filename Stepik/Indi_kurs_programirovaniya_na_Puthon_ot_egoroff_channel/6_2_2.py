a = input().lower()
b = {}
for item in a:
    if item.isalpha():
        if item in b:
            b[item[0]] += 1
        else:
            b[item[0]] = 1
print(b)