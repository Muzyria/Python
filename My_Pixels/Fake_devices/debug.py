
# import subprocess
# subprocess.call("test.sh")

import os
import time

# os.system('adb shell am broadcast -a com.yama.fake.ADBCom --es id "S10150000211018049" --es lat "50.08593724592065" --es lng "36.21560508169411"')

# id_car_start = 'S101500002110180'  #  without two simbol
# for i in range(70, 91):
#     new_id = f'{id_car_start}{i}'


lst_car = ['S101500002110180' + str(i) for i in range(70, 76)]
print(lst_car)
for _ in range(100):
    for i in lst_car:
        os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "{i}" --es lat "32.67062362844674" --es lng "-116.95901629375595"')
        time.sleep(5)
    time.sleep(5)
    os.system(f'adb shell am broadcast -a com.yama.fake.ADBCom --es id "S10150000211018076" --es lat "32.66993723927314" --es lng "-116.9582867329039"')
    time.sleep(5)