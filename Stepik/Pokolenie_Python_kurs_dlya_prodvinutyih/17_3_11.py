# import re
#
#
# with open(r'C:\Users\Sasha\Downloads\nums.txt', 'r', encoding='utf-8') as file:
#     #li = list(map(lambda x: x.strip(), file.readlines()))
#     li = [re.findall(r'\d+', line) for line in file.readlines()]
#
#     sw = []
#     for i in li:
#         #sw = sum([int(j) for j in i])
#         sw.append(sum([int(j) for j in i]))
#     print(sum(sw))

with open("nums_2.txt", "r", encoding='utf-8') as file:
    lines = 0
    for line in file:
        for j in line:
            if not j.isdigit():
                line = line.replace(j, " ")
        lines += sum(list(map(int, line.split())))
    print(lines)
