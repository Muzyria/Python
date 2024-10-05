
from functools import singledispatchmethod
from datetime import date

class BirthInfo:

    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register
    def _init_(self, birth_date: date):
        self.birth_date = birth_date

    @property
    def age(self):
        return self.birth_date

birthinfo = BirthInfo(date(2023, 2, 26))

print(birthinfo.age)