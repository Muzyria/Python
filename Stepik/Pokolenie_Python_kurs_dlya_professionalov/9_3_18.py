from string import ascii_lowercase, ascii_uppercase


def verification(login, password, success, failure):
    print(password)



def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


verification('timyrik20', 'Beegeek314', success, failure)
