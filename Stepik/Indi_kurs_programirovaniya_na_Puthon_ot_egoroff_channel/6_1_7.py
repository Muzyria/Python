dic = {}

while True:
    line = input()
    if line == 'конец':
        break

    value, key = line.split(': ')
    dic.setdefault(int(key), value)

for el in sorted(dic, reverse= True):
    print(dic[el])