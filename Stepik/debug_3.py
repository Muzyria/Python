from functools import total_ordering


@total_ordering
class RomanNumeral:
    _roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
              'CM': 900, 'M': 1000}
    _arabic = {1000: 'M',  900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}

    def __init__(self, number):
        self.number = number

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: str) -> None:
        self._number = self._roman[value]

    def __str__(self):
        return self._arabic[self.number]

    def __int__(self):
        return self.number

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number > other.number
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.number + other.number)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.number + other.number)
        return NotImplemented


number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))
