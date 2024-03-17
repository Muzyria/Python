
# def res_1():
#     with open('res_1.txt', 'r', encoding='utf-8') as file_1:
#         yield from (i for i in file_1)
#
# def res_2():
#     with open('res_2.txt', 'r', encoding='utf-8') as file_2:
#         return (i for i in file_2)
#
#
# for i in res_1():
#
def find_differences(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
            if line1 != line2:
                yield i

# Пример использования
file1 = 'res_1.txt'
file2 = 'res_2.txt'

differences = list(find_differences(file1, file2))
print("Различия в строках:", differences)