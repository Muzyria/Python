class StringValidation:
    def __init__(self, min_length=None, max_length=None, exclude_chars=None, is_same_register=False):
        self.min_length = min_length
        self.max_length = max_length
        self.exclude_chars = exclude_chars
        self.is_same_register = is_same_register

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки')
        if self.min_length and  len(value) < self.min_length:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна быть не меньше {self.min_length} символов')
        if self.max_length and len(value) > self.max_length:
            raise ValueError(f"Длина атрибута {self.attribute_name} должна быть не больше {self.max_length} символов")
        if self.exclude_chars and any(map(lambda x: x in self.exclude_chars, value)):
            raise ValueError(f"Имеются недопустимые символы в атрибуте {self.attribute_name}")
        if self.is_same_register and not (value.isupper() or value.islower()):
            raise ValueError(f"Все буквы должны быть в одном регистре в атрибуте {self.attribute_name}")
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'calling __get__ for {self.attribute_name}')
            return instance.__dict__.get(self.attribute_name, None)



class Person:
    name = StringValidation(is_same_register=True, exclude_chars='tyur', max_length=15, min_length=5)
    last_name = StringValidation(max_length=15, min_length=5, is_same_register=True, exclude_chars='!^&%^@%')



p = Person()
try:
    p.name = 'MICHAIL SECOND'
except ValueError as ex:
    print(ex)
try:
    p.last_name = 'lermontov'
except ValueError as ex:
    print(ex)
print(p.name, p.last_name)
# print(p.last_name)