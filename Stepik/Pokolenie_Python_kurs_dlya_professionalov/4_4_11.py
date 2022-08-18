import json
import csv

with open('playgrounds.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';', quotechar='"')
    result = {}

    for row in data:
        result.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])

    with open('addresses.json', 'w', encoding='utf-8') as file_w:
        json.dump(result, file_w, indent=3, ensure_ascii=False)


# with open('playgrounds.csv', 'r', encoding='utf-8') as csv_file, \
#         open('addresses.json', 'w', encoding='utf-8') as json_file:
#     rows = list(csv.reader(csv_file, delimiter=';'))
#     dictionary = {}
#
#     for row in rows[1:]:
#         if row[1] not in dictionary:
#             dictionary[row[1]] = dict.fromkeys([row[2]], [row[-1]])
#         else:
#             if row[2] not in dictionary[row[1]]:
#                 dictionary[row[1]][row[2]] = [row[-1]]
#             else:
#                 dictionary[row[1]][row[2]].append(row[-1])
#     json.dump(dictionary, json_file, indent=3, ensure_ascii=False)
