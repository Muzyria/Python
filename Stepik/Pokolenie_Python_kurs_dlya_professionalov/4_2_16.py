
import csv


with open('data.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=',', quotechar='"')
    result = {}
    for row in data:
        result.setdefault(row['email'].split('@')[1],  0)
        result[row['email'].split('@')[1]] += 1
    result = sorted(result.items(), key=lambda x: (x[1], x[0]))
    # print(*result)

    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_w:
        writer = csv.writer(file_w)
        writer.writerow(['domain', 'count'])
        writer.writerows(result)





