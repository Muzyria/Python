
with open('files.txt', encoding='utf-8') as file:

    sort_pattern = {'B': 1, 'KB': 2, 'MB': 3, 'GB': 4}  # опред. порядок сортировки
    sort_pattern_lst = list(sort_pattern.keys())  # список ключей единиц измерения
    convert_units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3} # перевод в байты

    res_name = {}  # расширение: список названий файлов
    size_res = {}  # 'jpeg': {'B': 1700, 'KB': 10000, 'MB': 3}

    for line in file:
        name, size, units = line.split()
        res_name.setdefault(name.split('.')[1], []).append(name)
        size_res.setdefault(name.split('.')[1], {}).setdefault(units, []).append(int(size))

    total_size_dct = {}  # по старшим единицам 'mp4': 'Summary: 4 GB'

    for k, v in size_res.items():
        total_size_B = 0
        for k1, v2 in v.items():
            total_size_B += sum(v2) * convert_units[k1]  # переводим объем файлов в байты

        max_units = max(v, key=lambda x: sort_pattern[x]) # определяем макс. един. измерения
        total_value = round(total_size_B / convert_units[max_units])

        # если макс. един. измерения > 1024, то меняем един. измерения
        while total_value > 1024:
            max_units = sort_pattern_lst[sort_pattern_lst.index(max_units) + 1]
            total_value = round(total_value / 1024)

        total_size_dct[k] = f'Summary: {total_value} {max_units}'

    for k, v in sorted(res_name.items()):
        print(*sorted(v), sep='\n')
        print('----------')
        print(total_size_dct[k])
        print()
