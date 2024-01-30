

from functools import total_ordering


@total_ordering
class RomanNumeral:
    _roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
              'CM': 900, 'M': 1000}
    _arabic = {1000: 'M',  900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}

    def __init__(self, number):
        self.number = self.convert_to_arabic(number)

    @classmethod
    def convert_to_roman(cls, arabic):
        roman = ''
        for value, symbol in cls._arabic.items():
            while arabic >= value:
                roman += symbol
                arabic -= value
        return roman

    @classmethod
    def convert_to_arabic(cls, roman):
        arabic = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i + 2] in cls._roman:
                arabic += cls._roman[roman[i:i + 2]]
                i += 2
            else:
                arabic += cls._roman[roman[i]]
                i += 1
        return arabic

    def __str__(self):
        return self.convert_to_roman(self.number)

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number < other.number
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.convert_to_roman(self.number + other.number))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.convert_to_roman(self.number - other.number))
        return NotImplemented

    def __int__(self):
        return int(self.number)
