
import csv


# Открываем CSV файл для чтения
with open('csv_files/consumer-client.csv', mode='r', encoding='utf-8') as file:
    # Создаем объект CSV reader
    csv_reader = csv.reader(file)

    # Пропускаем заголовок (если есть)
    next(csv_reader, None)
    number_row = 1

    # Читаем и выводим каждую строку
    for row in csv_reader:
        id_, customerID, client_name, client_eic, activation, test_activation = row
        print(f'{id_}, {customerID}, {client_name}, {client_eic}, {activation}, {test_activation}, ----- row number {number_row}')
        number_row += 1


