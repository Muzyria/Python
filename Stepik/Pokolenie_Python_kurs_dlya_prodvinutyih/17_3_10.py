# with open(r'C:\Users\Sasha\Downloads\numbers.txt', 'r', encoding='utf-8') as file:
#     li = list(map(lambda x: x.strip().split(), file.readlines()))
#
#     for i in li:
#         print(sum([int(j) for j in i]))
#
#

with open("numbers_2.txt", "r", encoding='utf-8') as file:
    for line in file:
        print(sum(map(int, line.split())))
