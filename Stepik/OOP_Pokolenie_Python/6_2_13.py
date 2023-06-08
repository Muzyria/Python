class SequenceZip:
<<<<<<< HEAD
    def __init__(self, *sequences):
        self.sequences = list(map(tuple, sequences))
        self.length = min(len(seq) for seq in self.sequences) if self.sequences else 0

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= self.length:
            raise StopIteration
        result = tuple(seq[self.current_index] for seq in self.sequences)
        self.current_index += 1
        return result
=======
    def __init__(self, *args):
        self.sequences = args
        self.length = min(len(seq) for seq in self.sequences)

    def __iter__(self):
        return zip(*self.sequences)
>>>>>>> origin/main

    def __len__(self):
        return self.length

    def __getitem__(self, index):
<<<<<<< HEAD
        if index >= self.length:
            raise IndexError("list index out of range")
        return tuple(seq[index] for seq in self.sequences)



# Тесты...
# Тест 1
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
print(list(sequencezip))
print(tuple(sequencezip))

# Тест 2
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])

# Тест 3
print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], 'data')))

# Тест 4
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)
=======
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

>>>>>>> origin/main
print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])

<<<<<<< HEAD
# Тест 5
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])

# Тест 6
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

# Тест 7
data = {'bee': 'bee', 'geek': 'geek'}
sequencezip = SequenceZip(data)
data['python'] = 'python'
print(data)
print(len(sequencezip))
print(list(sequencezip))

# Тест 8
data = {'bee': 'bee', 'geek': 'geek'}
sequencezip = SequenceZip(data)
print(sequencezip[0])
print(list(sequencezip))
=======



>>>>>>> origin/main
