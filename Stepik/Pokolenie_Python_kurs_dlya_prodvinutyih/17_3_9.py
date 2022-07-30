# with open(r'C:\Users\Sasha\Downloads\lines.txt', 'r', encoding='utf-8') as file:
#     li = list(map(lambda x: x.strip(), file.readlines()))
#
#     li = list(filter(lambda x: len(x) == len(max(li, key=len)), li) )
#     print(*li, sep='\n')
#

with open("lines_2.txt", "r", encoding='utf-8') as file:
    lines = [line.rstrip() for line in file.readlines()]
    max_len = max([len(line.rstrip()) for line in lines])
    print(*[line for line in lines if len(line) == max_len], sep="\n")
