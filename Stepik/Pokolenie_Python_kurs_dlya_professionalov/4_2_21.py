
import csv


with open('student_counts.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=',', quotechar='"')
    lst = []
    for row in data:
        lst.append(row)

    rotated = tuple(zip(*lst[::-1]))
    l = []
    for i in rotated:
        l.append(i[::-1])

    l2 = []
    for i in rotated[1:]:
        l2.append(i[::-1])

    l2 = sorted(l2, key=lambda x: (int(x[0].split('-')[0]), x[0].split('-')[1]) )
    l2.insert(0, l[0])

    l2= tuple(zip(*l2[::-1]))

    l3 = []
    for i in l2:
        l3.append(i[::-1])

    with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_w:
        writer = csv.writer(file_w, delimiter=',')
        writer.writerows(l3)


# import csv
#
# def key_func(grade):
#     number, letter = grade.split('-')
#     return int(number), letter
#
# with open('student_counts.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
#     rows = list(reader)
#
# with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(rows)