
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
        if key in menu and key not in tables[number]["order"]:
            tables[number]["order"][key] = value.split(",")
        elif key in menu and key in tables[number]["order"]:
            tables[number]["order"][key] += value.split(",")
            # for item in value.split(","):
            #     if item not in tables[number]["order"][key]:
            #         tables[number]["order"][key].append(item)


def delete_order(*, number_table=None, delete_all=False, **kwargs):
    if delete_all:
        tables[number_table]["order"].clear()
    else:
        for key, value in kwargs.items():
            if key in menu and value and key in tables[number_table]["order"]:
                del tables[number_table]["order"][key]



tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь,Мимоза', breakfast='Яичница,Бекон')
make_order(2, drink='Raf,Coffee,Juice', main_dish='Утка по-пекински,Отбивная')
make_order(2, desert='Трюфель', call='такси')

make_order(1, desert='Наполеон', drink='Чай', meal='Манка,Овсянка')
make_order(1, desert='Вишня', drink='Кофе')
print(tables)
delete_order(number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True)
delete_order(number_table=1, soup=True, desert=True, call=True)
print(tables)