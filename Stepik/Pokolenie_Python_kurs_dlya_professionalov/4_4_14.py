import json
import csv
from datetime import datetime

with open('exam_results.csv', encoding='utf-8') as file:
<<<<<<< HEAD
    data = csv.DictReader(file, delimiter=';', quotechar='"')
    for row in data:
        print(row)
=======
    data = csv.DictReader(file, delimiter=',', quotechar='"')
>>>>>>> origin/main
