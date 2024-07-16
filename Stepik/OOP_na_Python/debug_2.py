
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other

    def __radd__(self, other):
        return self.balance + other


class Numbers:
    def __init__(self, values: list):
        self._values = values

    @property
    def balance(self):
        return sum(self._values)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other

    def __radd__(self, other):
        return self.balance + other


lst = [
    BankAccount('Jack', 1000),
    Numbers([1, 2, 3, 4, 5]),
    BankAccount('Ivan', 30),
    7.5,
    Numbers([10, 20, 30, 40, 50]),
    BankAccount('Frank', 2000),
    10
]
print(sum(lst))