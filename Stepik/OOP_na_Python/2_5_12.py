# Напишите определение класса BankDeposit
class BankDeposit:
    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance * self.rate / 100

    def get_balance_with_profit(self):
        return self.balance + self.__calculate_profit()


# Ниже код для проверки методов класса BankDeposit
account = BankDeposit("John Connor", 1000, 5)
assert account.name == "John Connor"
assert account.balance == 1000
assert account.rate == 5
assert account._BankDeposit__calculate_profit() == 50.0
assert account.get_balance_with_profit() == 1050.0

account_2 = BankDeposit("Sarah Connor", 200, 27)
assert account_2.name == "Sarah Connor"
assert account_2.balance == 200
assert account_2.rate == 27
assert account_2._BankDeposit__calculate_profit() == 54.0
assert account_2.get_balance_with_profit() == 254.0
print('Good')
