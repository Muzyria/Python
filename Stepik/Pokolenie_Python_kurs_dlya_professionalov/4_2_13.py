import csv

n = int(input())
with open('deniro.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=',', quotechar='"')

    for row in sorted(rows, key=lambda x: int(x[n - 1]) if str(x[n - 1]).isdigit() else str(x[n - 1])):
        print(*row, sep=",")

