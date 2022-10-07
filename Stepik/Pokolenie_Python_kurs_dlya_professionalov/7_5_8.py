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
        raise LengthError
    if not any(i.islower() for i in string) or not any(i.isupper() for i in string):
        raise LetterError
    if not any(i.isdigit() for i in string):
        raise DigitError
    return True



