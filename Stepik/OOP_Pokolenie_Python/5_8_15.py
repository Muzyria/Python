class ProtectedObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, item):
        raise AttributeError('Доступ к защищенному атрибуту невозможен')

