from copy import deepcopy

class SequenceZip:
    def __init__(self, *args):
        self.sequences = [deepcopy(seq) for seq in args]

    def __len__(self):
        return min(len(seq) for seq in self.sequences)

    def __getitem__(self, item):
        return tuple(deepcopy(seq[item]) for seq in self.sequences)


sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

