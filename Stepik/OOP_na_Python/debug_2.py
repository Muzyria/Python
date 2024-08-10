
def check_exist_attrs(obj: object, lst: list[str]) -> dict[str, bool]:
    return {i: hasattr(obj, i) for i in lst}


def create_attrs(obj: object, lst: list[tuple[str, int|bool|str]]) -> None:
    [setattr(obj, k, v) for k, v in lst]



def print_goods(lst):
    pass

create_attrs(print_goods, [('is_working', False), ('days', 10), ('status', 'Not ready')])

print(check_exist_attrs(print_goods, ['sort', 'is_working', 'days', 'status', 'upper']))