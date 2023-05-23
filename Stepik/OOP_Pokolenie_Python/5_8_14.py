class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self, key, value)


videogame = Const(name='Dicso Elysium')

try:
    videogame.name = 'Half-Life: Alyx'
except AttributeError as e:
    print(e)
