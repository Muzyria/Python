import json

# Укажите путь к вашему файлу JSON
file_path = 'data.json'

# Открытие файла и чтение данных
with open(file_path, 'r', encoding='utf-8') as file:
    # Загрузка данных из файла
    data = json.load(file)

names = [name for name in data[0]]
# print(names)

result_dict = {}  # Создаем пустой словарь

for block in data:
    manf = block["manf"]
    type_ = block["type"]
    serNum = block["serNum"]
    mfDev = block["mfDev"]
    typeDev = block["typeDev"]
    chNum = block["chNum"]
    # Проверяем, есть ли производитель в словаре

    # Проверка наличия manf в словаре
    if manf not in result_dict:
        result_dict[manf] = []

    # Проверка наличия type в списке значений для manf
    if type_ not in result_dict[manf]:
        result_dict[manf].append({
            "type": type_,
            "serNum": serNum,
            "mfDev": mfDev,
            "typeDev": typeDev,
            "chNum": chNum
        })


# Выводим результат
for k, v in result_dict.items():
    print()
    print(k, v, len(v))


"""
Slot {'oe_22la', 'oe_vpt', 'oe_vt'} 3
Ukrgaztech {'floutek_tm_vr_1', 'floutek_tm_board2', 'pk_v', 'corrector_pc_2'} 4
Radmirtech {'kvr_1_02', 'kplg_1_01', 'vega_1_01', 'radio_modul', 'kplg_2_01r', 'tkb', 'vega_1_01_nvch', 'kvr_1_01n', 'kplg_1_02r', 'vega_2_01n', 'tkb_1', 'kplg_1_02rv', 'kvr_1_01', 'vega_1_01vch', 'vega_2_01', 'vega_1_01n'} 16
Vymiruvalnitechnologii {'v25'} 1
rgk {'smart104'} 1
Grempis {'universal_01', 'universal_m', 'universal_02', 'universal_mt'} 4
Tandem {'tandem_tr', 'tandem_t'} 2
Ukrgaztech_Imod {'corrector_pc_2'} 1
"""