
import csv


path_consumer_client = 'csv_files/sql_requests_consumer_client'
path_customer_devices = 'csv_files/sql_requests_customer_devices'
path_customer_devices_direct = 'csv_files/sql_requests_customer_devices_direct'


def change_consumer_client():
    # Открываем consumer_client.csv
    with open('csv_files/consumer_client.csv', mode='r', encoding='utf-8') as file:
         with open(f'{path_consumer_client}/sql_without_eic.txt', mode='w', encoding='utf-8') as file_sql_without_eic:
            with open(f'{path_consumer_client}/sql_with_eic.txt', mode='w', encoding='utf-8') as file_sql_with_eic:
                # Создаем объект CSV reader
                csv_reader = csv.reader(file)

                # Пропускаем заголовок
                next(csv_reader, None)
                number_row = 1

                # Читаем и выводим каждую строку
                for row in csv_reader:
                    id_, customerID, client_name, client_eic, activation, test_activation = row
                    print(f'{id_}, {customerID}, {client_name}, {client_eic}, {activation}, {test_activation} ----- row number {number_row}')

                    # Записываем два файла с SQL запросами для изменения на пустые значения и второй для возврата в прежнее состоянмие
                    file_sql_without_eic.write(f"UPDATE `gmp`.`consumer_client` SET `client_eic` = '' WHERE (`id` = '{id_}');\n")
                    file_sql_with_eic.write(f"UPDATE `gmp`.`consumer_client` SET `client_eic` = '{client_eic}' WHERE (`id` = '{id_}');\n")
                    number_row += 1


def change_customer_devices():
    # Открываем customer_devices.csv
    with open('csv_files/customer_devices.csv', mode='r', encoding='utf-8') as file:
         with open(f'{path_customer_devices}/sql_without_eic.txt', mode='w', encoding='utf-8') as file_sql_without_eic:
            with open(f'{path_customer_devices}/sql_with_eic.txt', mode='w', encoding='utf-8') as file_sql_with_eic:
                # Создаем объект CSV reader
                csv_reader = csv.reader(file)

                # Пропускаем заголовок
                next(csv_reader, None)
                number_row = 1

                # Читаем и выводим каждую строку
                for row in csv_reader:
                    id_, customerID, mod_time, client_name, client_eic, gas_node, gas_operator, serNUM, mfDEV, typeDEV, chNUM, address, scenario, consumer_client_id = row
                    print(f'{id_}, {customerID}, {mod_time}, {client_name}, {client_eic}, {gas_node}, {gas_operator}, {serNUM}, {mfDEV}, {typeDEV}, {chNUM}, {address}, {scenario}, {consumer_client_id} ----- row number {number_row}')

                    # Записываем два файла с SQL запросами для изменения на пустые значения и второй для возврата в прежнее состоянмие
                    file_sql_without_eic.write(f"UPDATE `gmp`.`customer_devices` SET `client_eic` = '' WHERE (`id` = '{id_}');\n")
                    file_sql_with_eic.write(f"UPDATE `gmp`.`customer_devices` SET `client_eic` = '{client_eic}' WHERE (`id` = '{id_}');\n")
                    number_row += 1


def change_customer_devices_direct():
    # Открываем customer_devices_direct.csv
    with open('csv_files/customer_devices.csv', mode='r', encoding='utf-8') as file:
         with open(f'{path_customer_devices_direct}/sql_without_eic.txt', mode='w', encoding='utf-8') as file_sql_without_eic:
            with open(f'{path_customer_devices_direct}/sql_with_eic.txt', mode='w', encoding='utf-8') as file_sql_with_eic:
                # Создаем объект CSV reader
                csv_reader = csv.reader(file)

                # Пропускаем заголовок
                next(csv_reader, None)
                number_row = 1

                # Читаем и выводим каждую строку
                for row in csv_reader:
                    id_, customerID, client_name, client_eic, gas_node, gas_operator, serNUM, mfDEV, typeDEV, chNUM, address, scenario, note = row
                    print(f'{id_}, {customerID}, {client_name}, {client_eic}, {gas_node}, {gas_operator}, {serNUM}, {mfDEV}, {typeDEV}, {chNUM}, {address}, {scenario}, {note} ----- row number {number_row}')

                    # Записываем два файла с SQL запросами для изменения на пустые значения и второй для возврата в прежнее состоянмие
                    file_sql_without_eic.write(f"UPDATE `gmp`.`customer_devices_direct` SET `client_eic` = '' WHERE (`id` = '{id_}');\n")
                    file_sql_with_eic.write(f"UPDATE `gmp`.`customer_devices_direct` SET `client_eic` = '{client_eic}' WHERE (`id` = '{id_}');\n")
                    number_row += 1


# change_consumer_client()
# change_customer_devices()
change_customer_devices_direct()