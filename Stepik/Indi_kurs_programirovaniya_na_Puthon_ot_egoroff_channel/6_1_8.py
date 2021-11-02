dict = {}
dict_2 = {}
while True:
    a = list(input().split(', '))
    if a[0] == 'конец':
        break
    if a[0] in dict:
        dict[a[0]] += [int(a[1])]
    else:
        dict[a[0]] = [int(a[1])]
for items in dict:
    result = sum(dict[items]) / len(dict[items])
    dict_2[items] = result
for i in sorted(dict_2.items(), key=lambda para: (-para[1], para[0])):
    print(*i)