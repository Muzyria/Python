import json
import csv

with open('students.json', encoding='utf-8') as file:
    data = json.load(file)
    for row in data:
        print(row)
