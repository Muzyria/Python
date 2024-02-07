from copy import deepcopy


class SequenceZip:
    def __init__(self, *args):
        self.sequences = [deepcopy(seq) for seq in args]


    def __len__(self):
        if self.sequences:
            return min(len(seq) for seq in self.sequences)
        else:
            return 0

    def __getitem__(self, item):

        return tuple(deepcopy(seq[item]) for seq in self.sequences)

    # def __iter__(self):
    #     return iter(zip(*self.sequences))


sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))
