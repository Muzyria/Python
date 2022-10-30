def filter_names(names, ignore_char, max_names):
    gen1 = (i for i in names if i[0].upper() != ignore_char.upper() and all(map(lambda x: x.isalpha(), i)))
    return (name for inx, name in enumerate(gen1) if inx < max_names)


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))
# Timur Arthur Arina

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 't', 20))
# Dima Arthur Arina German Ruslan

