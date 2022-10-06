import json


try:
    file_name = input()
    file = open(file_name)
    try:
        data = json.load(file)
        print(data)
    except json.decoder.JSONDecodeError:
        print('Ошибка при десериализации')
    finally:
        file.close()
except FileNotFoundError:
    print('Файл не найден')

