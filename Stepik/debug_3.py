

class CardDeck:
    KEY = ("пик", "треф", "бубен", "червей")
    VALUE = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")

    def __init__(self):
        self.coloda = iter([(k, v) for v in self.KEY for k in self.VALUE])

    def __iter__(self):
        return self

    def __next__(self):
        return "{} {}".format(*next(self.coloda))


cards = CardDeck()

print(next(cards))
print(next(cards))

print()

cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
