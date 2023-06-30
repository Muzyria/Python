from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.suit}{self.value}'


class Deck:
    def __init__(self):
        suits = ['♣', '♢', '♡', '♠']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __str__(self):
        return f'Карт в колоде: {len(self.cards)}'

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self.cards)
        return self

    def deal(self):
        if not self.cards:
            raise ValueError('Все карты разыграны')
        return self.cards.pop()