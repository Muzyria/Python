class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        """метод, возвращающий актуальный баланс счета"""
        return self._balance

    def deposit(self, amount) -> None:
        """метод, увеличивающий баланс счета"""
        if isinstance(amount, (int, float)):
            self._balance += amount
        else:
            raise ValueError("Неверный формат данных.")

    def withdraw(self, amount):
        """метод, уменьшающий баланс счета"""
        if isinstance(amount, (int, float)):
            if self._balance - amount < 0:
                raise ValueError("Неверный формат данных.")
            else:
                self._balance -= amount
        else:
            raise ValueError("Неверный формат данных.")


account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())
