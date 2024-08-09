import string
alfa = string.ascii_lowercase


def rotate_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    index = (shift + alfa.index(letter)) % len(alfa)
    return alfa[index]


def caesar_cipher(phrase: str, key: int) -> str:
    """caesar_cipher"""
    return "".join([rotate_letter(i, key) if i in alfa else i for i in phrase])



