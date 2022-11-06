def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_mast = ["пик", "треф", "бубен", "червей"]
    ind = 0
    while True:
        try:
            for i in card_values:
                if ind != card_mast.index(suit):
                    yield f'{i} {card_mast[ind]}'
                else:
                    continue
            ind += 1
        except IndexError:
            ind = 0

generator = card_deck('пик')
print(next(generator))
print(next(generator))
print(next(generator))
