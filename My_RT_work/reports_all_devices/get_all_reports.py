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

    # Проверка наличия manf в словаре
    if manf not in result_dict:
        result_dict[manf] = {}

    # Проверка наличия type в словаре manf
    if type_ not in result_dict[manf]:
        result_dict[manf][type_] = {
            "serNum": serNum,
            "chNum": chNum,
            "mfDev": mfDev,
            "typeDev": typeDev
        }

translation_dict = {
    "Slot_oe_vpt": "Слот_OE-VPT",
    "Slot_oe_22la": "Слот_OE-22ЛА",
    "Slot_oe_vt": "Слот_OR-VT",

    "Ukrgaztech_corrector_pc_2": "УкрГазтех_Корректор ПК-2",
    "Ukrgaztech_floutek_tm_vr_1": "УкрГазтех_ФЛОУТЭК-ТМ-ВР-1",
    "Ukrgaztech_pk_v": "УкрГазтех_ПК-В",
    "Ukrgaztech_floutek_tm_board2": "УкрГазтех_ФЛОУТЭК-ТМ (плата 2)",

    "Radmirtech_vega_1_01": "Радмиртех_ВЕГА-1.01",
    "Radmirtech_kvr_1_01": "Радмиртех_КВР-1.01",
    "Radmirtech_tkb": "Радмиртех_ТКБ",
    "Radmirtech_vega_1_01n": "Радмиртех_ВЕГА-1.01Н",
    "Radmirtech_kplg_1_02r": "Радмиртех_КПЛГ-1.02Р",
    "Radmirtech_vega_2_01n": "Радмиртех_ВЕГА-2.01Н",
    "Radmirtech_kvr_1_02": "Радмиртех_КВР-1.02",
    "Radmirtech_kplg_2_01r": "Радмиртех_КПЛГ-2.01Р",
    "Radmirtech_vega_2_01": "Радмиртех_ВЕГА-2.01",
    "Radmirtech_vega_1_01vch": "Радмиртех_ВЕГА-1.01ВЧ",
    "Radmirtech_kvr_1_01n": "Радмиртех_КВР-1.01Н",
    "Radmirtech_tkb_1": "Радмиртех_ТКБ-1",
    "Radmirtech_kplg_1_02rv": "Радмиртех_КПЛГ-1.02РВ",
    "Radmirtech_kplg_1_01": "Радмиртех_КПЛГ-1.01",
    "Radmirtech_radio_modul": "Радмиртех_РАДИО-МОДУЛЬ",
    "Radmirtech_vega_1_01_nvch": "Радмиртех_ВЕГА-1.01 НВЧ",

    "Vymiruvalnitechnologii_v25": "Вычислительные технологии_V25",

    "rgk_smart104": "RGK_smart104",

    "Grempis_universal_01": "Гремпис_Универсал-01",
    "Grempis_universal_02": "Гремпис_Универсал-02",
    "Grempis_universal_m": "Гремпис_Универсал-М",
    "Grempis_universal_mt": "Гремпис_Универсал-МT",

    "Tandem_tandem_tr": "Тандем_Тандем-ТР",
    "Tandem_tandem_t": "Тандем_Тандем-Т",

    "Ukrgaztech_Imod_corrector_pc_2": "УкрГазтех_Imod_Корректор ПК-2",
}


# Выводим результат
for key, value in result_dict.items():
    for k, v in value.items():

        print(f'"{key}_{k}": "",')
        # print(key, k)

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