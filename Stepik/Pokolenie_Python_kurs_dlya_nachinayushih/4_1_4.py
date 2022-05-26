'''
word_1, word_2 = str(input()), str(input())
if word_1 == word_2:
    print("Пароль принят")
else:
    print("Пароль не принят")
'''
print("Пароль принят" if str(input()) == str(input()) else "Пароль не принят")