def create_dict():
    my_dict = {}
    count = 0

    def counter(value):
        nonlocal count
        count += 1
        my_dict[count] = value
        return my_dict

    return counter


f_1 = create_dict()
print(f_1('hello'))  # f_1 возвращает {1: 'hello'}
print(f_1(100))  # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3]))  # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict()  # создаем новое замыкание в f_2
print(f_2('PoweR'))  # f_2 возвращает {1: 'PoweR'}
