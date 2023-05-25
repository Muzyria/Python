class ProtectedObject:
    def __init__(self, **kwargs):
        [object.__setattr__(self, k, v) for k, v in kwargs.items()]

    def __setattr__(self, key, value):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, key, value)

    def __getattribute__(self, key):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, key)

    def __delattr__(self, key):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, key)

