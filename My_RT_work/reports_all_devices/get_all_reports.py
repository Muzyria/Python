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


