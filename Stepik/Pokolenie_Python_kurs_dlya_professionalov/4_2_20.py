
import csv


def condense_csv(filename, id_name='ID'):
    with open(filename, encoding='utf-8') as file:
        data = csv.reader(file, delimiter=',')
        result = {}
        keys = [id_name]

        for row in data:
            keys.append(row[1])
            result.setdefault(row[0], []).append(row[2])
        n = len(keys) // len(result)

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file_w:
        writer = csv.writer(file_w, delimiter=',')
        writer.writerow(keys[:n+1])
        for k, v in result.items():
            writer.writerow([k, *v])


condense_csv('4_2_20.txt', 'ID')


# ID,color,size,notes
# ball,purple,4,it's round
# cup,blue,1,none
