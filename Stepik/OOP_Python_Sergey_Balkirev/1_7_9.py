from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if len(number) != 19:
            return False
        for i in range(4, 19, 5):
            if number[i] != "-":
                return False
        if not number.replace("-", "").isdigit():
            return False
        return True

    @staticmethod
    def check_name(name):
        if name.count(" ") != 1:
            return False
        for char in name.replace(" ", ""):
            if char not in CardCheck.CHARS_FOR_NAME:
                return False
        return True


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(CardCheck.CHARS_FOR_NAME)

"""
from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    PATTERN_NUMBER = r'\d{4}-\d{4}-\d{4}-\d{4}'
    PATTERN_NAME = r'^[A-Z]+ [A-Z]+$'

    @classmethod
    def check_card_number(cls, number):
        return bool(re.fullmatch(cls.PATTERN_NUMBER, number))

    @classmethod
    def check_name(cls, name):
        return bool(re.fullmatch(cls.PATTERN_NAME, name))
"""