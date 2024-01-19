class BankAccount:
    def __init__(self, balance: int | float = 0):
        self._balance = balance

    def get_balance(self) -> int | float:
        """метод, возвращающий актуальный баланс счета"""
        return self._balance

    def deposit(self, amount: int | float) -> None:
        """метод, увеличивающий баланс счета"""
        if isinstance(amount, (int, float)):
            self._balance += amount
        else:
            raise ValueError("Неверный формат данных.")

    def withdraw(self, amount: int | float) -> None:
        """метод, уменьшающий баланс счета"""
        if isinstance(amount, (int, float)):
            if self._balance - amount < 0:
                raise ValueError("На счете недостаточно средств")
            else:
                self._balance -= amount
        else:
            raise ValueError("Неверный формат данных.")

    def transfer(self, account: object, amount: int | float) -> None:
        """Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount"""
        if isinstance(amount, (int, float)):
            if self._balance - amount < 0:
                raise ValueError("На счете недостаточно средств")
            else:
                self._balance -= amount
                account.deposit(amount)
        else:
            raise ValueError("Неверный формат данных.")


account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())

account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)

account1 = BankAccount(100)
account2 = BankAccount(200)

account1.transfer(account2, 50)
print(account1.get_balance())
print(account2.get_balance())

account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)
