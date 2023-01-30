class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if self.__balance < value:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        self.__balance -= value
        return True

class Cart:
    def __init__(self, user: User):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product: Product, count=1):
        if product.name not in self.goods:
            self.goods[product.name] = [product.price, count]
            self.__total += product.price * count
        else:
            self.goods[product.name][1] += count
            self.__total += product.price * count


    def remove(self, product: Product, count=1):
        if self.goods[product.name][1] - count <= 0:
            self.__total -= self.goods[product.name][1] * self.goods[product.name][0]
            del self.goods[product.name]
        else:
            self.goods[product.name][1] -= count
            self.__total -= self.goods[product.name][1] * self.goods[product.name][0]

    @property
    def total(self):
        return self.__total

    def order(self):
        if User.payment(self.user, self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        [print(f"{k} {v[0]} {v[1]} {v[0] * v[1]}") for k, v in sorted(self.goods.items())]
        print(f'---Total: {self.total}---')




billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
print()
print(1, '------------------------------------')
print()
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
print()
print(2, '------------------------------------')
print()
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print()
print(3, '------------------------------------')
print()
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
print()
print(4, '------------------------------------')
print()
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20