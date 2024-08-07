
menu = ('soup', 'desert', 'drink', 'main_dish', 'salad')

def is_table_free(number):
    return tables[number] is None


def get_free_tables():
    return list(filter(is_table_free, tables.keys()))


def reserve_table(number, name, status=False):
    if is_table_free(number):
        tables[number] = {"name": name, "is_vip": status, 'order': {}}


def delete_reservation(number):
    tables[number] = None


def make_order(number, **kwargs):
    for key, value in kwargs.items():
        if key in menu:
            tables[number]["order"][key] = value


def delete_order(*, number_table=None, delete_all=False, **kwargs):
    if delete_all:
        tables[number_table]["order"].clear()
    else:
        for key, value in kwargs.items():
            if key in menu and value and key in tables[number_table]["order"]:
                del tables[number_table]["order"][key]


tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh'}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)

delete_order(number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True)
delete_order(number_table=1, soup=True, desert=True, call=True)
print(tables)