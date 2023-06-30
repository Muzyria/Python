class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=()):
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum([i.price for i in self.items])

    def remove(self, name):
        [self.items.remove(i) for i in self.items if i.name == name]

    def __str__(self):
        return '\n'.join(str(item) for item in self.items)


shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])

shopping_cart.add(Item('Flannel Shirt', 22))
print(shopping_cart)
print(shopping_cart.total())

shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])

shopping_cart.remove('Yoga Mat')
print(shopping_cart)
print(shopping_cart.total())

shopping_cart = ShoppingCart([Item('Banana', 100), Item('Apple', 120), Item('Orange', 110), Item('Tomato', 180), Item('Cucumber', 150)])

shopping_cart.add(Item('Banana', 100))
print(shopping_cart)
print(shopping_cart.total())

shopping_cart.remove('Banana')
print(shopping_cart)
print(shopping_cart.total())

#  Banana, 100$
# Apple, 120$
# Orange, 110$
# Tomato, 180$
# Cucumber, 150$
# Banana, 100$
# 760
# Apple, 120$
# Orange, 110$
# Tomato, 180$
# Cucumber, 150$
# 560