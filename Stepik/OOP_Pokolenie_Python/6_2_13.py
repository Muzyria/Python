# import copy
#
# class SequenceZip:
#     def __init__(self, *args):
#         self.sequences = [copy.deepcopy(seq) for seq in args]
#
#     def __len__(self):
#         return min(len(seq) for seq in self.sequences) if self.sequences else 0
#
#     def __getitem__(self, index):
#         if isinstance(index, slice):
#             return tuple(tuple(elem for elem in seq[index]) for seq in self.sequences)
#         else:
#             if isinstance(self.sequences[0], dict):
#                 return tuple(((seq[index],) for seq in self.sequences))
#             else:
#                 return tuple(seq[index] for seq in self.sequences)
#
#     def __iter__(self):
#         return zip(*self.sequences)


# x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
# sequencezip = SequenceZip(x, y, z)
#
# print(sequencezip[2])
# x[-1], z[-1] = z[-1], x[-1]
# print(sequencezip[2])
#
#
# many_large_sequences = [range(100000) for _ in range(100)]
# sequencezip = SequenceZip(*many_large_sequences)
# print(sequencezip[99999])
#
#
# sequencezip = SequenceZip()
# print(len(sequencezip))
# print(list(sequencezip))

import copy

class SequenceZip:
    def __init__(self, *args):
        self.sequences = [copy.deepcopy(seq) for seq in args]

    def __len__(self):
        return min(len(seq) for seq in self.sequences) if self.sequences else 0

    def __getitem__(self, index):
        if isinstance(index, slice):
            return tuple(tuple(elem for elem in seq[index]) for seq in self.sequences)
        else:
            if isinstance(self.sequences[0], dict):
                try:
                    return tuple(((seq[index],) for seq in self.sequences))
                except KeyError:
                    return tuple(((seq.get(index),) for seq in self.sequences))
            else:
                return tuple(seq[index] if index < len(seq) else None for seq in self.sequences)

    def __iter__(self):
        return zip(*self.sequences)


data = {'bee': 'bee', 'geek': 'geek'}
sequencezip = SequenceZip(data)
print(sequencezip[0])
print(list(sequencezip))


