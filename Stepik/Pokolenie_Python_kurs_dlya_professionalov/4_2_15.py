
import csv


def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        result = {}
        rows = csv.reader(file, delimiter=',', quotechar='"')
        for i in next(rows):
            result.setdefault(i, [])
        for row in rows:
            for i, k in zip(result, row):
                result.setdefault(i, []).append(k)
        return result


csv_columns("4_2_15.txt")

# import csv
# def csv_columns(filename):
#     res = {}
#     with open(filename, 'r', encoding='utf8') as file:
#         data = csv.DictReader(file)
#         for i in data:
#             for k, v in i.items():
#                 res.setdefault(k, []).append(v)
#     return res