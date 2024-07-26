class RangeValidator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __set_name__(self, owner, name):
        self.attribute_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Неправильный тип данных')
        if not self.x <= value <= self.y:
            raise ValueError(f"Значение должно быть между {self.x} и {self.y}")
        instance.__dict__[self.attribute_name] = value


class Temperature:
    celsius = RangeValidator(-273.15, 1000)


temp = Temperature()
try:
    temp.celsius = 500
except TypeError as ex:
    print(ex)
else:
    print(temp.celsius)
    print(temp.__dict__)


