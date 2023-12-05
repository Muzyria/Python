import json

# Ваш JSON-строк
json_str = '''
[
    {
        "id": 2891,
        "serNum": "57467",
        "manf": "Ukrgaztech",
        "type": "corrector_pc_2",
        "mfDev": 5,
        "typeDev": 12,
        "chNum": 0,
        "meteringStation": "0097359301",
        "cardNo": "+380679241941",
        "org": "ДП Укргазтех",
        "adr": "ЖУРНАЛIСТIВ 15",
        "gasName": "dnipro",
        "clientEic": "",
        "note": null,
        "dataComplete": false,
        "dvst_alwrk": null,
        "dvwrk_alwrk": null
    },
    # Дополнительные блоки...
]
'''

# Преобразование строки JSON в объект Python
data = json.loads(json_str)

# Создание словаря
result_dict = {}

# Обработка каждого блока данных
for block in data:
    manf = block["manf"]
    type_ = block["type"]
    serNum = block["serNum"]
    mfDev = block["mfDev"]
    typeDev = block["typeDev"]
    chNum = block["chNum"]

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

# Вывод результата
for manf, values in result_dict.items():
    print(f"Manufacturer: {manf}")
    for item in values:
        print(f"  Type: {item['type']}, SerNum: {item['serNum']}, mfDev: {item['mfDev']}, typeDev: {item['typeDev']}, chNum: {item['chNum']}")
