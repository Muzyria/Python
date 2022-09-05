import json
import csv
from datetime import datetime

students = []
students_dict = {}
pattern = "%Y-%m-%d %H:%M:%S"
with open('exam_results.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';', quotechar='"')
    for row in data:
        key = row['email']
