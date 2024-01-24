from functools import singledispatchmethod
from datetime import date

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(list)
    @__init__.register(tuple)
    def from_list_tuple(self, birth_date):
        self.birth_date = date(*birth_date)

    @__init__.register(date)
    def from_object(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def from_str(self, birth_date):
        self.birth_date = date.fromisoformat(birth_date)

    @property
    def age(self):
        age = date.today().year - self.birth_date.year - 1
        age += (date.today().month, date.today().day) >= (self.birth_date.month, self.birth_date.day)
        return age


birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)