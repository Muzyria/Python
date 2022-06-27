class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

carrot = Product('carrot', 30)
print(carrot.name, carrot.price)

