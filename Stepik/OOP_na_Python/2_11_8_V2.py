
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


class Cart:
    @classmethod
    def __init__(self, User):
        self.user = User
        self.goods = dict()
        self.__total = 0
        self.price_pro = dict()

    @property
    def total(self):
        return self.__total

    def add(self, Product, ad_amount=1):
        if Product.name not in self.goods:
            Cart.price_pro.update({Product.name: Product.price})
            Cart.goods.update({Product.name: ad_amount})
            self.__total += ad_amount * Product.price
        else:
            Cart.goods[Product.name] = Cart.goods[Product.name] + ad_amount
            self.__total += ad_amount * Product.price

    def remove(self, Product, re_amount=1):
        if Product.name in self.goods and Cart.goods[Product.name] >= re_amount:
            Cart.goods[Product.name] = Cart.goods[Product.name] - re_amount
            self.__total -= re_amount * Product.price
        if Product.name in self.goods and Cart.goods[Product.name] < re_amount:
            re_amount = Cart.goods[Product.name]
            Cart.goods[Product.name] = Cart.goods[Product.name] - re_amount
            self.__total -= re_amount * Product.price
        if Cart.goods[Product.name] == 0:
            del Cart.goods[Product.name]
        
    def order(self):
        if User.payment(self.user, self.__total):
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")    

    def print_check(self):
        print("---Yor check---")
        for k, v in sorted(Cart.goods.items()):
            print(f"{k} {Cart.price_pro[k]} {v} {v * Cart.price_pro[k]}")
        print(f"---Total: {self.total}---")


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20
