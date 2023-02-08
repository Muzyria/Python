class Shop:
    def __init__(self, name_shop):
        self.name_shop = name_shop
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        del self.goods[self.goods.index(product)]


class Product:
    _id_instance = 1
    attrs = {'id': int, 'name': str, 'weight': (int, float), 'price': (int, float)}

    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        self.id = Product._id_instance
        Product._id_instance += 1
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.attrs and not set(str(type(value))).issubset(set(str(self.attrs[key]))):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif  type(value) in (int, float) and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")