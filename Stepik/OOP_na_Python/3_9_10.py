class FileReader:
    def __init__(self, filename):
        self.file = open(filename, encoding='utf-8')

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.file).strip()


for line in FileReader('lorem.txt'):
    print(line)
