class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 0:
            raise ValueError("На счете недостаточно средств")
        self._balance -= amount

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


account1 = BankAccount(100)
account2 = BankAccount(200)

account1.transfer(account2, 50)
print(account1.get_balance())
print(account2.get_balance())



