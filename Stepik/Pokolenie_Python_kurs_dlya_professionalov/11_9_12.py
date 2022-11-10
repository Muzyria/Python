import re


def multiple_split(string, delimiters):
    pat = '|'.join(map(re.escape, delimiters))
    return re.split(fr'{pat}', string)


print(multiple_split('beegeek-python.stepik', ['.', '-']))
# ['beegeek', 'python', 'stepik']
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
# ['Timur', 'Arthur', 'Dima', 'Anri']
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))
# ['timur', 'arthur', 'dima', 'anri', 'roma', 'ruslan']
print(multiple_split('stepik_python-dima*roma*jenya-timur__arthur', ['_', '*', '#', '@']))
# ['stepik', 'python-dima', 'roma', 'jenya-timur', '', 'arthur']
