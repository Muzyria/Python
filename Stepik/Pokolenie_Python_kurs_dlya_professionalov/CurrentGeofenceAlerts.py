
import csv


with open('CurrentGeofenceAlerts.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';', quotechar='"')
    result = {}
    for row in data:
        print(row)
