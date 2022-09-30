from collections import Counter


def scrabble(symbol: str, word: str):
    print(Counter(symbol))


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
