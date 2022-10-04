try:
    file_name = input()
    file = open(file_name, 'r', encoding='utf-8')
    try:
        print(file.read())
    finally:
        file.close()
except FileNotFoundError:
    print('Файл не найден')
