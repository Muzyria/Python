class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self._default = default

    def __get__(self, obj, cls):
        if self._name in obj.__dict__:
            return obj.__dict__[self._name]
        elif self._default is not None:
            return self._default
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._name] = value


class Student:
    score = NonNegativeInteger('score')


student = Student()
student.score = 90

print(student.score)


class Student:
    score = NonNegativeInteger('score', 0)


student = Student()

print(student.score)
