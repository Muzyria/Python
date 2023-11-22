import json

# Укажите путь к вашему файлу JSON
file_path = 'data.json'

# Открытие файла и чтение данных
with open(file_path, 'r', encoding='utf-8') as file:
    # Загрузка данных из файла
    data = json.load(file)

names = [name for name in data[0]]
# print(names)

manf = {}  # Создаем пустой словарь

for item in data:
    # Проверяем, есть ли производитель в словаре
    if item['manf'] not in manf:
        manf[item['manf']] = set()  # Если нет, создаем пустой список для этого производителя

    manf[item['manf']].add(item['type'])  # Добавляем тип в список для данного производителя

# Выводим результат
for k, v in manf.items():
    print(k, v, len(v))


