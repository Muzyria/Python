class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if len(kwargs) == 0:
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'
        else:
            key = list(kwargs)[0]
            self.message = f'Значение первичного ключа {key} = {kwargs[key]} недопустимо'

    def __str__(self):
        return self.message


if __name__ == '__main__':
    try:
        raise PrimaryKeyError(id=-10.5)
    except PrimaryKeyError as e:
        print(e)
