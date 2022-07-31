# def read_csv():
#     result = []
#     with open('data.csv') as file:
#         keys = file.readline().strip('\n').split(',')
#         for line in file:
#             values = line.strip('\n').split(',')
#             result.append(dict(zip(keys, values)))
#     return result

def read_csv():
    with open("data.csv",  "r", encoding='utf-8') as file:
        lst = []
        keys = file.readline().rstrip().split(",")
        for line in file:
            values = line.rstrip().split(",")
            lst.append(dict(zip(keys, values)))
        return lst


print(*read_csv(), sep="\n")
