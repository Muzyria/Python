
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

shop_items = {}
for i in lst_in:
    temp_list = i.split()
    temp_item = ShopItem(temp_list[0], temp_list[1], temp_list[2])
    if temp_item in shop_items:
        shop_items[temp_item][1] += 1
    else:
        shop_items[temp_item] = [temp_item, 1]

    