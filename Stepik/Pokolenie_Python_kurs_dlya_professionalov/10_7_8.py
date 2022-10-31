import csv


with open('data2.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_headers = next(line_values)
    line_dicts = (dict(zip(file_headers, data)) for data in line_values)

    result = (line['raisedAmt'] for line in line_dicts if line['round'] == 'a')
    print(sum(map(int, result)))

# import csv
#
# with open('data.csv', encoding='utf8') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     print(sum(int(line[1]) for line in reader if line[3]=='a'))
