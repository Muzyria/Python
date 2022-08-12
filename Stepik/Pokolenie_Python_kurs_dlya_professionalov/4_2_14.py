import csv

n = int(input())
with open('salary_data.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=',', quotechar='"')

