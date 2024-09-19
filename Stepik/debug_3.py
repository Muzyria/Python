
class CardDeck:
    def __init__(self):
        self.cards = iter(f"{name} {card}" for card in ("пик", "треф", "бубен", "червей") for name in list(range(2, 11)) + ["валет", "дама", "король", "туз"])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cards)


cards = CardDeck()

print()
print(*cards)
