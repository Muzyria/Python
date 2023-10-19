import csv
import random


# Заголовок CSV файла
header = ["id", "deviceid", "date_recorded", "epochtime", "ugaugereporttype", "inputvolt", "battpackvolt", "alt",
          "calfixstatus", "hdop", "headingdirection", "gpsaccuracy", "gpsspeed", "gpsstatus", "lat", "lon",
          "lostfixtime", "numbersat", "rssi", "serialcode", "serialreportflag", "serialparam00", "serialparam01",
          "serialparam02", "serialparam03", "serialparam04", "serialparam05", "serialparam06", "serialparam07",
          "serialparam08", "serialparam09", "serialparam10", "serialparam11", "serialparam12", "serialparam13",
          "serialparam14", "serialparam15", "serialparam16", "serialparam17", "serialparam18", "serialparam19",
          "serialparam20", "serialparam21", "serialparam22", "serialparam23", "serialparam24", "serialparam25",
          "serialparam26", "serialparam27", "serialparam28", "serialparam29", "serialparam30", "serialparam31",
          "serialparam32", "serialparam33", "serialparam34", "serialparam35", "serialparam36", "serialparam37",
          "serialparam38", "serialparam39", "serialparam40", "serialparam41", "serialparam42", "serialparam43",
          "serialparam44", "serialparam45", "serialparam46", "serialparam47"
          ]

# Список данных для записи
data = {'id': '61328', 'deviceid': 'S10150000211018049', 'date_recorded': '1.71E+11', 'epochtime': '1511999433',
         'ugaugereporttype': '3', 'inputvolt': '11.8', 'battpackvolt': 'NULL', 'alt': 'NULL', 'calfixstatus': '0',
         'hdop': 'NULL', 'headingdirection': 'NULL', 'gpsaccuracy': 'NULL', 'gpsspeed': 'NULL', 'gpsstatus': 'NULL',
         'lat': '5004.670665', 'lon': '3613.827855', 'lostfixtime': 'NULL', 'numbersat': 'NULL', 'rssi': '-70',
         'serialcode': '53', 'serialreportflag': '1', 'serialparam00': '2', 'serialparam01': '100',
         'serialparam02': 'NULL', 'serialparam03': 'NULL', 'serialparam04': 'NULL', 'serialparam05': 'NULL',
         'serialparam06': 'NULL', 'serialparam07': 'NULL', 'serialparam08': 'NULL', 'serialparam09': '0',
         'serialparam10': 'NULL', 'serialparam11': 'NULL', 'serialparam12': 'NULL', 'serialparam13': 'NULL',
         'serialparam14': 'NULL', 'serialparam15': 'NULL', 'serialparam16': '25', 'serialparam17': 'NULL',
         'serialparam18': 'NULL', 'serialparam19': 'NULL', 'serialparam20': 'NULL', 'serialparam21': 'NULL',
         'serialparam22': 'NULL', 'serialparam23': 'NULL', 'serialparam24': 'NULL', 'serialparam25': 'NULL',
         'serialparam26': 'NULL', 'serialparam27': 'NULL', 'serialparam28': 'NULL', 'serialparam29': 'NULL',
         'serialparam30': 'NULL', 'serialparam31': 'NULL', 'serialparam32': '12', 'serialparam33': 'NULL',
         'serialparam34': 'NULL', 'serialparam35': 'NULL', 'serialparam36': 'NULL', 'serialparam37': 'NULL',
         'serialparam38': 'NULL', 'serialparam39': 'NULL', 'serialparam40': 'NULL', 'serialparam41': 'NULL',
         'serialparam42': 'NULL', 'serialparam43': 'NULL', 'serialparam44': 'NULL', 'serialparam45': 'NULL',
         'serialparam46': 'NULL', 'serialparam47': 'NULL'}



# Имя файла
filename = 'utilitygauge_2.csv'

# Запись заголовка и данных в CSV файл
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)

    # Запись заголовка
    writer.writeheader()

    # Запись данных
    for i in range(100):
        lat = data['lat'][:-5] + str(random.randint(0, 99999)).zfill(5)
        lon = data['lon'][:-5] + str(random.randint(0, 99999)).zfill(5)
        print(lat, lon)
        data['lat'], data['lon'] = lat, lon
        data['id'] = i

        writer.writerow(data)

print(f'CSV файл "{filename}" успешно создан.')
