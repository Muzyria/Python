import csv
import statistics


with open('data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',', quotechar='"')

    data = [int(row['зарплата']) for row in rows]
    print(f'Средняя заработная плата = {int(statistics.mean(data))}')
    print(f'Медианная заработная плата = {int(statistics.median(data))}')
    print(f'Размах выборки = {max(data) - min(data)}')
