
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

    @property
    def total(self):
        return self.__total

    def add(self, Product, ad_amount=1):
        self.ad_amount = ad_amount
        if Product.name not in self.goods:
            Cart.goods.update({Product.name: ad_amount})
            self.__total += ad_amount
        else:
            Cart.goods[Product.name] = Cart.goods[Product.name] + ad_amount
            self.__total += ad_amount
        print(self.goods, self.__total) #===========================================

    def remove(self, Product, re_amount=1):
        self.re_amount = re_amount
        if Product.name in self.goods and Cart.goods[Product.name] >= re_amount:
            Cart.goods[Product.name] = Cart.goods[Product.name] - re_amount
            self.__total -= re_amount
        print(self.goods, self.__total) #===========================================

    def order(self):
        pass


billy = User('billy@rambler.ru')
lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.add(lemon, 2)
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.add(lemon, 2)
cart_billy.remove(lemon, 8)
cart_billy.remove(carrot, 2)



