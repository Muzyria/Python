import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    # создаем reader объект и указываем в качестве разделителя символ ;
    rows = csv.reader(csv_file, delimiter=";")
    # выводим каждую строку
    for row in rows:
        print(row)
