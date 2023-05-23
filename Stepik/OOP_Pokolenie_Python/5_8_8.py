class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, item):
        if item == 'name':
            return object.__getattribute__(self, item).title()
        elif item == 'total':
            return self.price * self.quantity
        return object.__getattribute__(self, item)


fruit = Item('banana', 15, 5)

print(fruit.name)
print(fruit.total)
