import csv

with open('sales.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';', quotechar='"')
    for row in rows:
        try:
            if int(row[1]) > int(row[2]):
                print(*row[:1])
        except ValueError:
            continue

# with open('sales.csv', encoding='utf-8') as file:
#     data = csv.DictReader(file, delimiter=';', quotechar='"')
#     for row in data:
#         if int(row['old_price']) > int(row['new_price']):
#             print(row['name'])