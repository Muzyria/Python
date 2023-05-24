class ProtectedObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattribute__(self, item: str):
        # if item.startswith('_'):
        #     raise AttributeError('')
        object.__getattribute__(self, item)


    # def __setattr__(self, key, value):
    #     pass

    # def __delattr__(self, item):
    #     raise AttributeError('Доступ к защищенному атрибуту невозможен')


user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    # print(user._password)
except AttributeError as e:
    print(e)

