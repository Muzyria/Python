
word = input()
n = int(input())
list_index_word = [i for i, j in enumerate(word, 0) if j in 'ауоыиэяюёе']

for _ in range(n):
    check_word = input()
    list_index_check_word = [i for i, j in enumerate(check_word, 0) if j in 'ауоыиэяюёе']
    if list_index_word == list_index_check_word:
        print(check_word)
