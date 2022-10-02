def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char.lewer() in vowels:
            swapped_string += char.upper()
        else:
            swapped_string += char

    return swapped_string
