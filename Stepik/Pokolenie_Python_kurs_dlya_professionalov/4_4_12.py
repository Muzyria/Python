import json
import csv

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    result = []
    for row in data:
        if row['age'] >= 18 and row['progress'] >= 75:
            result.append([row['name'], row['phone']])

    with open('data_1.csv', 'w', encoding='utf-8', newline='') as file_w:
        writer = csv.writer(file_w)
        writer.writerow(['name', 'phone'])
        writer.writerows(sorted(result, key=lambda x: x[0]))
