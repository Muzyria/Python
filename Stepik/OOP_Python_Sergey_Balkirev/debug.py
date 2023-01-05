import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self, a, b):
        if b >= len(DataBase.lst_data):
            b = len(DataBase.lst_data) - 1
        return [DataBase.lst_data[1] for i in range(a, b)]

    def insert(self, data):
        DataBase.lst_data.append(zip(DataBase.FIELDS, data))


db = DataBase()
db.insert(lst_in)
