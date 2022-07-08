import csv


with open('Crimes.csv') as file:
    d = {}
    reader = csv.reader(file)
    for line in reader:
        if line[2][6:10] == '2015':
            key = line[5]
            d[key] = d.get(key, 0) + 1
    print(max(d, key=d.get))