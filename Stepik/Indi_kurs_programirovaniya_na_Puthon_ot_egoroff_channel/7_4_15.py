import itertools

def shift_letter(letter, shift):
    """Функция сдвигает символ letter на shift позиций"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = alphabet.index(letter)
    shifted_index = (index + shift) % len(alphabet)
    shifted_letter = itertools.islice(itertools.cycle(alphabet), shifted_index, None).__next__()
    return shifted_letter
