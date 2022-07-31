# from random import *
#
# with open(r'C:\Users\Sasha\Downloads\first_names.txt', 'r', encoding='utf-8') as file, open(r'C:\Users\Sasha\Downloads\last_names.txt', 'r', encoding='utf-8') as file2:
#     li = list(map(lambda x: x.strip(), file.readlines()))
#     li2 = list(map(lambda x: x.strip(), file2.readlines()))
#
#     for _ in range(3):
#         print(choice(li), choice(li2))

from random import choice

with open("first_names.txt",  "r", encoding='utf-8') as file, open("last_names.txt",  "r", encoding='utf-8') as file2:
    name, surname = file.readlines(), file2.readlines()
    for _ in range(3):
        print(choice(name).rstrip(), choice(surname).rstrip())
    