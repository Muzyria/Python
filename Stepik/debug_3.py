

class ProtectedObject:
    def __init__(self, **kwargs):
        [object.__setattr__(self, k, v) for k, v in kwargs.items()]

    def __getattribute__(self, item: str):
        if item.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        return object.__getattribute__(self, item)

    def __setattr__(self, key: str, value):
        if key.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__setattr__(self, key, value)

    def __delattr__(self, item: str):
        if item.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__delattr__(self, item)

user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)
