tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: {'name': 'Misha', 'is_vip': False},
}


def is_table_free(number):
    return tables[number] is None


def get_free_tables():
    return list(filter(is_table_free, tables.keys()))


def reserve_table(number, name, status=False):
    if is_table_free(number):
        tables[number] = {"name": name, "is_vip": status}


def delete_reservation(number):
    tables[number] = None

print(tables)
reserve_table(2, 'Niko', True)
reserve_table(6, 'Chubaka') # не передается вип-статус
print(tables)