class Wallet:
    def __init__(self, currency: str, balance: int):
        self.currency = currency
        self.balance = balance

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if not isinstance(value, str):
            raise TypeError("Неверный тип валюты")
        if len(value) != 3:
            raise NameError("Неверная длина названия валюты")
        if not all(map(lambda x: x.isupper(), value)):
            raise ValueError("Название должно состоять только из заглавных букв")
        else:
            self._currency = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        if self.currency != other.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        else:
            return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        else:
            return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency or self.balance < other.balance:
            raise ValueError("Данная операция запрещена")
        else:
            return Wallet(self.currency, self.balance - other.balance)


wallet1 = Wallet('USD', 250)
wallet2 = Wallet('RUB', 200)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 - wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
