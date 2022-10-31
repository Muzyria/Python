def nonempty_lines(file):
    pass


lines = nonempty_lines('file1.txt')
print(next(lines))
print(next(lines))
print(next(lines))

print(*nonempty_lines('file2.txt'))
