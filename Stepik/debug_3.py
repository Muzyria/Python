
def filter_names(names, ignor_char, max_names):
    without_digit = (i for i in names if i.isalpha())
    without_ignor_char = (i for i in without_digit if not i.lower().startswith(ignor_char.lower()))
    return (v for k, v in enumerate(without_ignor_char) if k < max_names)


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))