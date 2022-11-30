import os
from random import choice, randrange
import time

test_49 = 'S10150000211018049'

# Высадка дисанта
for i in ['S101500002110180' + str(i) for i in range(70, 91)]:
    x = '32.6' + str(randrange(6739266744535, 7320189906043))
    y = '-116.9' + str(randrange(5185681343078, 6095486640930))
    print(i, x, y, 'На поле')
    os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "{i}" --es lat "{x}" --es lng "{y}"')
    time.sleep(0)

count_iter = 3600
for j in range(count_iter):
    car_id = choice(['S101500002110180' + str(i) for i in range(70, 91)])
    x = '32.6' + str(randrange(6739266744535, 7320189906043))
    y = '-116.9' + str(randrange(5185681343078, 6095486640930))
    print(car_id, x, y, ' -------------------------> ' + str(count_iter - j))
    os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "{car_id}" --es lat "{x}" --es lng "{y}"')
    time.sleep(5)

# lst_car = ['S101500002110180' + str(i) for i in range(70, 91)]

# os.system('adb shell am broadcast -a com.yama.fake.ADBCom --es id "S10150000211018049" --es lat "50.08593724592065" --es lng "36.21560508169411"')

