def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as file:
        file_lines = (line for line in file)




lines = nonempty_lines('file1.txt')
print(next(lines))
print(next(lines))
print(next(lines))

print(*nonempty_lines('file2.txt'))
