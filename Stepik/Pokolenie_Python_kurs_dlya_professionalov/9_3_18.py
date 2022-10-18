from string import ascii_lowercase, ascii_uppercase


# def verification(login, password, success, failure):
#     if not any(i in ascii_lowercase + ascii_uppercase for i in password):
#         failure(login, 'в пароле нет ни одной буквы')
#     elif not any(i in ascii_uppercase for i in password):
#         failure(login, 'в пароле нет ни одной заглавной буквы')
#     elif not any(i in ascii_lowercase for i in password):
#         failure(login, 'в пароле нет ни одной строчной буквы')
#     elif not any(i.isdigit() for i in password):
#         failure(login, 'в пароле нет ни одной цифры')
#     else:
#         success(login)

# def verification(login, password, success, failure):
#     vd = {str.isalpha: 'в пароле нет ни одной буквы',
#           str.islower: 'в пароле нет ни одной строчной буквы',
#           str.isupper: 'в пароле нет ни одной заглавной буквы',
#           str.isdigit: 'в пароле нет ни одной цифры'}
#     for f in vd:
#         if not any(f(i) for i in password):
#             return failure(login, vd[f])
#     success(login)

def verification(login, password, success, failure):
    vd = {(str.isalpha, str.isascii): 'в пароле нет ни одной буквы',
          (str.isascii, str.islower): 'в пароле нет ни одной строчной буквы',
          (str.isascii, str.isupper): 'в пароле нет ни одной заглавной буквы',
          (bool,        str.isdigit): 'в пароле нет ни одной цифры'}
    for f in vd:
        if not any(f[0](i) and f[1](i) for i in password):
            return failure(login, vd[f])
    success(login)

# def success(login):
#     print(f'Привет, {login}!')
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Ошибка: {text}')
#
# verification('timyrik20', 'Beegeek314', success, failure)


# def success(login):
#     print(f'Здравствуйте, {login}!')
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
# verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)

def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпароль123', success, failure)
