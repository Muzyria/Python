dct = {}
for _ in range(int(input())):
    val, key = input().split()
    if key in dct:
        dct [key].append(val)
    else:
        dct [key] = [val] 
for _ in range(int(input())):
    key = input()
    if key in dct:
        print(*dct [key])
    else:
        print('Неизвестный номер')

