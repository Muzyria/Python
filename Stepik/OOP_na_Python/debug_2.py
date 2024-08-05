def print_goods(*args):
    goods = list(filter(lambda x: type(x) is str and x, args))
    if goods:
        [print(f"{n}. {name}") for n, name in enumerate(goods, 1)]
    else:
        print("Нет товаров")


print_goods('apple', 'banana', 'orange')
print()
print_goods(1, True, 'Грушечка', '', 'Pineapple')
print()
print_goods(*list('qwerty'))
print()
print_goods([], {}, 1, 2)
print()
print_goods(*list('abc'), 1, 'hello')