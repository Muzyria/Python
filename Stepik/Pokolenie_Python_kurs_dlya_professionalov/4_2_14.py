import csv


with open('salary_data.csv', encoding='utf-8') as file:
    result = {}
    data = csv.DictReader(file, delimiter=';', quotechar='"')
    for row in data:
        result.setdefault(row['company_name'], []).append(int(row['salary']))
    result = {k: (sum(v) / len(v)) for k, v in result.items()}
    [print(i[0]) for i in (sorted(result.items(), key=lambda x: x[1]))]
