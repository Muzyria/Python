from functools import total_ordering


@total_ordering
class RomanNumeral:
    _roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
              'CM': 900, 'M': 1000}
    _arabic = {1000: 'M',  900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}

    def __init__(self, number):
        self.number = self.convert_to_arabic(number)
