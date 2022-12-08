while True:
    product = None
    print('Приветствую тебя в нашем интеренет магазине')
    print('Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light,'
        ' 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie,'
        ' 6 - Test.allTheThings() T-Shirt (Red)')
    try:
        product = input()
        print(len(product))
        if len(product) != 1 or int(product) not in range(1, 7):
            continue
        else:

            break
    except ValueError:
        continue
print(product)
