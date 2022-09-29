import csv
from collections import Counter

with open('name_log.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')
    result = Counter(row['email'] for row in sorted(rows, key=lambda x: x['email']))
    [print(f'{k}: {v}') for k, v in result.items()]
