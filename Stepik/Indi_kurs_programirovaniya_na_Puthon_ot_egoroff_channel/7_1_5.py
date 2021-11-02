def count_letters(s):
    up, low = 0, 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    print(f'Количество заглавных символов: {up}')
    print(f'Количество строчных символов: {low}')