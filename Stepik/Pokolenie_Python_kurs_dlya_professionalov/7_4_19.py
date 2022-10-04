def get_id(names: list, name: str):
    if not type(name) == str:
        raise TypeError('Имя не является строкой')
    if not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    return len(names) + 1


# names = ['Timur', 'Anri', 'Dima']
# name = 'Arthur'
# print(get_id(names, name))
#
# names = ['Timur', 'Anri', 'Dima', 'Arthur']
# name = 'Ruslan1337'
# try:
#     print(get_id(names, name))
# except ValueError as e:
#     print(e)
#
# names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
# name = ['E', 'd', 'u', 'a', 'r', 'd']
# try:
#     print(get_id(names, name))
# except TypeError as e:
#     print(e)
#
# names = ['Timur', 'Anri', 'Dima', 'Arthur']
# name = 'ruslan'
# try:
#     print(get_id(names, name))
# except ValueError as e:
#     print(e)
