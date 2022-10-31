def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as file:
        file_lines = (line.strip() if len(line) <= 25 else '...' for line in file if line.strip() != '')
        yield from (line for line in file_lines)


lines = nonempty_lines('file1.txt')
print(next(lines))
print(next(lines))
print(next(lines))

# print(*nonempty_lines('file2.txt'))
