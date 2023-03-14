import csv
import statistics


with open('students.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',', quotechar='"')
    print(statistics.mode([row['first_name'].title() for row in rows]))
