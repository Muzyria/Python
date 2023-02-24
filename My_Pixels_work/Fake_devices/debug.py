class ShoppingCart:

    def __init__(self):
        self.items = {}

    def __getitem__(self, item_name):
        return self.items.get(item_name, 0)

    def __setitem__(self, item_name, item_quantity):
        self.items[item_name] = item_quantity

    def __delitem__(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def add_item(self, item_name, item_quantity=1):
        if item_name in self.items:
            self.items[item_name] += item_quantity
        else:
            self.items[item_name] = item_quantity

    def remove_item(self, item_name, item_quantity=1):
        if item_name not in self.items:
            return

        if item_quantity >= self.items[item_name]:
            del self.items[item_name]
        else:
            self.items[item_name] -= item_quantity
