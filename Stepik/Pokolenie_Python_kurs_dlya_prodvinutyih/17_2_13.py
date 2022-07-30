# from random import *
#
# file = open(r'C:\Users\Sasha\Downloads\lines.txt', 'r', encoding="utf-8")
# line = list(map(lambda line: line.strip(), file.readlines()))
# print(choice(line))
#
# file.close()


from random import choice

with open("lines.txt", "r", encoding='utf-8') as file:
    line = file.readlines()
    print(choice(line).rstrip())
