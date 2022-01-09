
file = open('numbers.txt', 'r', encoding="utf-8")
line = list(map(lambda line: int(line.strip()), file.readlines()))
print(sum(line))

file.close()