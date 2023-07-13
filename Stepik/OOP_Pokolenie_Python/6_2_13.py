import copy

class SequenceZip:
    def __init__(self, *args):
        self.sequences = [copy.copy(seq) for seq in args]

    def __len__(self):
        return min(len(seq) for seq in self.sequences) if self.sequences else 0

    def __getitem__(self, index):
        if isinstance(index, slice):
            return tuple(tuple(elem for elem in seq[index]) for seq in self.sequences)
        else:
            if isinstance(self.sequences[0], dict):
                return tuple(seq.get(index, None) for seq in self.sequences)
            else:
                return tuple((seq[index],) for seq in self.sequences)

    def __iter__(self):
        return zip(*self.sequences)

# TEST
data = {'bee': 'bee', 'geek': 'geek'}
sequencezip = SequenceZip(data)
print(sequencezip[0])
print(list(sequencezip))