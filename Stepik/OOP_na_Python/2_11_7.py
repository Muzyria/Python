
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance    

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if value > self.__balance:
            print("Не хватает средств на балансе. Пополните счет") 
            return False
        else:
            self.__balance -= value
            return True

billy = User('billy@rambler.ru')
print(billy) # Пользователь billy@rambler.ru, баланс - 0
billy.deposit(100)
billy.deposit(300)
print(billy) # Пользователь billy@rambler.ru, баланс - 400
billy.payment(500) # Не хватает средств на балансе. Пополните счет
billy.payment(150)
print(billy) # Пользователь billy@rambler.ru, баланс - 250
                             

        