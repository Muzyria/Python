
import csv


with open('wifi.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';', quotechar='"')
    result = {}
    for row in data:
        result.setdefault(row['district'],  0)
        result[row['district']] += int(row['number_of_access_points'])
    result = sorted(result.items(), key=lambda x: (x[1], [-o for o in map(ord, x[0])]), reverse=True)
    [print(*i, sep=': ') for i in result]
