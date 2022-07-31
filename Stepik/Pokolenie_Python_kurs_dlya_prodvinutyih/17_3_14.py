# with open(r'C:\Users\Sasha\Downloads\population.txt') as file:
#     for line in file.readlines():
#         n, p = line.split('\t')
#         if n.startswith('G') and int(p) > 500000:
#             print(n)

with open("population.txt",  "r", encoding='utf-8') as file:
    for line in file.readlines():
        n, p = line.split("\t")
        if n[0] == "G" and int(p) > 500000:
            print(n)
