lst = []
lst_lower = []
for i in input().split():
    if i.lower() not in lst_lower:
        lst.append(i)
        lst_lower.append(i.lower())
print(*lst)
