word = input()
n = 0
while n < len(word):
    if word[n] not in ('a', 'e'):
        print(f'Текущая буква: {word[n]}')
        n += 1
    else:
        print('Ага! Нашлась')
        break
else:
    print("Распечатали все буквы")
