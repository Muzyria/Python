
import csv


with open('name_log.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=',', quotechar='"')
    result = {}
    for row in data:
        result.setdefault(row['email'], []).append((row['username'], row['dtime']))
    for k, v in result.items():
        if len(v) > 1:
            result[k] = sorted(v, key=lambda x: x[1])
    result = [[v[-1][0], k, v[-1][1]] for k, v in sorted(result.items())]
    # print(result)

    with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file_w:
        writer = csv.writer(file_w, delimiter=',')
        writer.writerow(['username', 'email', 'dtime'])
        writer.writerows(result)
