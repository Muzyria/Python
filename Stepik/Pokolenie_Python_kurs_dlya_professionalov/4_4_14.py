import json
import csv
from datetime import datetime

with open('exam_results.csv', encoding='utf-8') as file:
    # data = csv.DictReader(file, delimiter=',', quotechar='"')
    data = csv.reader(file)
    next(data)
    result = {}
    for row in data:
        name_full = (row[0], row[1])
        if (row[0], row[1]) not in result:
            result.setdefault((row[0], row[1]), (int(row[2]), datetime.fromisoformat(row[3]), row[4]))
        else:
            if result[(row[0], row[1])][0] < int(row[2]):
                result[(row[0], row[1])] = (int(row[2]), datetime.fromisoformat(row[3]), row[4])
            elif result[(row[0], row[1])][0] == int(row[2]):
                result[(row[0], row[1])] = (int(row[2]), datetime.fromisoformat(row[3]), row[4])
    print(result)
