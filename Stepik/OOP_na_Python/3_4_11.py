class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.price == other.price
        elif isinstance(other, (int, float)):
            return self.price == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fruit):
            return self.price < other.price
        elif isinstance(other, (int, float)):
            return self.price < other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fruit):
            return self.price > other.price
        elif isinstance(other, (int, float)):
            return self.price > other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fruit):
            return self.price <= other.price
        elif isinstance(other, (int, float)):
            return self.price <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fruit):
            return self.price >= other.price
        elif isinstance(other, (int, float)):
            return self.price >= other
        else:
            return NotImplemented




# Ниже код для проверки методов класса Fruit

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert banana > 1.2
assert banana >= 1.2
assert not banana == 1.2
assert banana != 1.2
assert not banana < 1.2
assert not banana <= 1.2

assert not apple > orange
assert not apple >= orange
assert not apple == orange
assert apple != orange
assert apple < orange
assert apple <= orange

assert orange == lime
assert not orange != lime
assert not orange > lime
assert not orange < lime
assert orange <= lime
assert orange >= lime
print('Good')
