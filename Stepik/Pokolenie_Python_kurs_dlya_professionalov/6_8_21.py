import csv
import json


for n in range(1, 5):
    with open(f'quarter{n}.csv', 'r', encoding='utf-8') as file:
        q = csv.DictReader(file)
        for row in q:
            print(row)
