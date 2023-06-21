from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.bits = [int(bit) for bit in iterable]

    def __repr__(self):
        return f"[{', '.join(str(bit) for bit in self.bits)}]"

    def __getitem__(self, index):
        return self.bits[index]

    def __len__(self):
        return len(self.bits)

    def __contains__(self, item):
        return item in self.bits

    def __reversed__(self):
        return reversed(self.bits)

    def __invert__(self):
        inverted_bits = [int(not bit) for bit in self.bits]
        return BitArray(inverted_bits)

    def __and__(self, other):
        if not isinstance(other, BitArray) or len(self) != len(other):
            return NotImplemented
        result_bits = [bit1 & bit2 for bit1, bit2 in zip(self.bits, other.bits)]
        return BitArray(result_bits)

    def __or__(self, other):
        if not isinstance(other, BitArray) or len(self) != len(other):
            return NotImplemented
        result_bits = [bit1 | bit2 for bit1, bit2 in zip(self.bits, other.bits)]
        return BitArray(result_bits)
