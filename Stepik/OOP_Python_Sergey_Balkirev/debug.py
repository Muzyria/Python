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

print(CardCheck.check_card_number("1244-5678-9012-0000-5643"))