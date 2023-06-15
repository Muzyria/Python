from keyword import kwlist


class NonKeyword:
    '''Checking that word not in keywords list'''

    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if value in kwlist:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value



class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

print(student.name)
