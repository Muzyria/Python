
import csv


with open('titanic.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';', quotechar='"')
    result_male = []
    result_female = []
    for row in data:
        if float(row['age']) < 18 and row['survived'] == '1':
            if row['sex'] == 'male':
                result_male.append(row['name'])
            else:
                result_female.append(row['name'])
    [print(i) for i in result_male]
    [print(i) for i in result_female]
