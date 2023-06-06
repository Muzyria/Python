class ForgivingIndexer:
    def __init__(self, sequence):
        self.sequence = sequence

    def __getitem__(self, index):
        return self.sequence[int(index)]

    def __len__(self):
        return len(self.sequence)


words = ForgivingIndexer(['beegeek', 'pygen', 'stepik', 'python'])

print(len(words[1.9]))