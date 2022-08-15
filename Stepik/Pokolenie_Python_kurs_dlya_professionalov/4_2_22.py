
import csv


with open('prices.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';', quotechar='"')
    colum = next(data)

    result = []
    for row in data:
        shop = row[0]
        min_price = min([int(i) for i in row[1:]])
        food = colum[row.index(str(min([int(i) for i in row[1:]])))]
        result.append((min_price, food, shop))
        result = sorted(result, key=lambda x: (x[0], x[1]))
    print(f'{result[0][1]}: {result[0][2]}')

# import csv
#
# with open('prices.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     data = []
#     for row in reader:
#         shop = row.pop('Магазин')
#         goods, price = min(row.items(), key=lambda x: int(x[1]))
#         data.append((int(price), goods, shop))
#
# min_price = min(data)
# print(f'{min_price[1]}: {min_price[2]}')