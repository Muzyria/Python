import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str):
    if not len(string) >= 9:
        raise LengthError('LengthError')
    if not any(i.islower() for i in string) or not any(i.isupper() for i in string):
        raise LetterError('LetterError')
    if not any(i.isdigit() for i in string):
        raise DigitError('DigitError')
    return True


for line in sys.stdin:
    s = line.strip('\n')
    try:
        is_good_password(s)
    except Exception as err:
        print(err.args[0])
    else:
        print('Success!')
        break


