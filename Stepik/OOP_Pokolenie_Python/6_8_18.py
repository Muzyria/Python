class TypeChecked:
    def __init__(self, *types):
        self.types = types

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if not any(isinstance(value, t) for t in self.types):
            raise TypeError('Некорректное значение')
        instance.__dict__[self.name] = value
