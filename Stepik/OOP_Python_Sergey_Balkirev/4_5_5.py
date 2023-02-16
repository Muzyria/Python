class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem(ShopInterface):
    __id = 0

    def __init__(self, name, weight, price):
        self.__id = ShopItem.__id
        ShopItem.__id += 1
        self._name = name
        self._weight = weight
        self._price = price


    def get_id(self):
        return self.__id

item = ShopItem("Товар 1", 10, 100)
print(item.get_id())  # выводится уникальный идентификатор товара