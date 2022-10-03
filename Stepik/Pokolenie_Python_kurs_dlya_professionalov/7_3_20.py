from calendar import month_name


try:
    print(dict(enumerate(month_name[1:], 1))[int(input())])
except KeyError:
    print('Введено число из недопустимого диапазона')
except:
    print('Введено некорректное значение')
