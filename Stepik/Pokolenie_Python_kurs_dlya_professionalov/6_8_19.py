from collections import Counter


def scrabble(symbols: str, word: str):
    return Counter(symbols.lower()) >= Counter(word.lower())


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))

print(scrabble('beegeek', 'beegeek'))
