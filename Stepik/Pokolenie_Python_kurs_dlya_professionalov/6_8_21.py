import csv
import json
from collections import Counter

result = Counter()
total = 0
for n in range(1, 5):
    temp_dict = Counter()
    with open(f'quarter{n}.csv', 'r', encoding='utf-8') as file:
        products = csv.DictReader(file)
        for row in products:
            elm = list(row.values())
            temp_dict[elm[0]] = sum([int(i) for i in elm[1::]])
        result += temp_dict
with open('prices.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for k, v in result.items():
        total += data[k] * v
print(total)
