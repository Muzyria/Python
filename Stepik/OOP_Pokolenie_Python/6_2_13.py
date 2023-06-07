class SequenceZip:
    def __init__(self, *args):
        self.sequences = args
        self.length = min(len(seq) for seq in self.sequences)

    def __iter__(self):
        return zip(*self.sequences)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if isinstance(index, int):
            return tuple(seq[index] for seq in self.sequences)
        elif isinstance(index, slice):
            start, stop, step = index.indices(self.length)
            return tuple(tuple(seq[i] for seq in self.sequences) for i in range(start, stop, step))
        else:
            raise TypeError("Invalid index type.")

    def __setitem__(self, index, value):
        raise TypeError("SequenceZip object does not support item assignment.")


x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])




