import os
from datetime import datetime
from random import choice, randrange
import time

# test_49 = 'S10150000211018049'
time_value = 5  # Величина паузы между командами

geofens_for_4_car = {'S10150000211018201': ("32.67029213323701", "-116.95823751379653"),
                     'S10150000211018202': ("32.67030568038896", "-116.95804439474746"),
                     'S10150000211018203': ("32.66996700097419", "-116.95840917517349"),
                     'S10150000211018204': ("32.66999861110722", "-116.95814631869003")}

for i in ['S10150000211018' + str(i) for i in range(201, 250)]:

    # Return area
    x = '32.67211882231258'
    y = '-116.95939616862482'
    print(i, 'На RETURN AREA')
    os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "{i}" --es lat "{x}" --es lng "{y}"')
    time.sleep(time_value)

    # HOLE 1
    x = '32.67075509305431'
    y = '-116.95889191333002'
    print(i, 'На HOLE 1')
    os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "{i}" --es lat "{x}" --es lng "{y}"')
    time.sleep(time_value)


    # В геофенс !!!
    x = "32.66999861110722"
    y = "-116.95814631869003"
    print(i, 'В ГЕОФЕНС АЛЕРТ 18')
    os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "{i}" --es lat "{x}" --es lng "{y}"')
    time.sleep(time_value)

# while True:
#     for i in ['S10150000211018' + str(i) for i in range(201, 205)]:
#
#         # В геофенс !!!
#         x = geofens_for_4_car[i][0]
#         y = geofens_for_4_car[i][1]
#         print(i, 'В ГЕОФЕНС АЛЕРТ 18 в ЦИКЛЕ')
#         os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "{i}" --es lat "{x}" --es lng "{y}"')
#         time.sleep(time_value)

count_iter = 3600
start_time = datetime.now()  # включаем счетчик
for j in range(count_iter):
    count_time = str(datetime.now() - start_time).split('.')[0]
    car_id = choice(['S10150000211018' + str(i) for i in range(201, 250)])
    x = '32.6' + str(randrange(6739266744535, 7320189906043))
    y = '-116.9' + str(randrange(5185681343078, 6095486640930))
    print(car_id, x, y, ' -------------------------> ' + str(count_iter - j), ' прошло времени ' + count_time,
          datetime.now().strftime('%H:%M:%S'))
    os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "{car_id}" --es lat "{x}" --es lng "{y}"')
    time.sleep(time_value)

# lst_car = ['S101500002110180' + str(i) for i in range(70, 91)]
# os.system('adb shell am broadcast -a com.yama.fake.ADBCom --es id "S10150000211018049" --es lat "50.08593724592065" --es lng "36.21560508169411"')
