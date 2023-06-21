from collections.abc import Sequence


class DNA(Sequence):
    def __init__(self, chain):
        self.chain = chain

    def __repr__(self):
        return self.chain

    def __len__(self):
        return len(self.chain)

    def __reversed__(self):
        return DNA(self.chain[::-1])

    def __iter__(self):
        return iter(self.get_base_pairs())

    def __getitem__(self, index):
        if isinstance(index, slice):
            return DNA(self.chain[index])
        elif isinstance(index, int):
            if index < 0:
                index = len(self.chain) + index
            if 0 <= index < len(self.chain):
                return self.get_base_pair(index)
            else:
                raise IndexError("Index out of range")

    def __contains__(self, base):
        return base in self.chain

    def __eq__(self, other):
        if isinstance(other, DNA):
            return self.chain == other.chain
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, DNA):
            return self.chain != other.chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, DNA):
            new_chain = self.chain + other.chain
            return DNA(new_chain)
        return NotImplemented

    def get_base_pair(self, index):
        base1 = self.chain[index]
        base2 = self.get_complementary_base(base1)
        return base1, base2

    def get_base_pairs(self):
        return (self.get_base_pair(i) for i in range(len(self.chain)))

    def get_complementary_base(self, base):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return complement.get(base)
