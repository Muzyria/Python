
# import subprocess
# subprocess.call("test.sh")

# import os
# os.system('adb shell am broadcast -a com.yama.fake.ADBCom --es id "S10150000211018049" --es lat "50.08593724592065" --es lng "36.21560508169411"')
# os.system('adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings')
# os.system('adb shell input tap 800 100')
# os.system('adb shell input keyevent 4')
# os.system('')
# os.system('')


#
# id_car_start = 'S101500002110180'  #  without two simbol
# for i in range(70, 91):
#     new_id = f'{id_car_start}{i}'


lst_car = ['S101500002110180' + str(i) for i in range(70, 91)]
print(lst_car)
for i in lst_car:
    print(i[-2::])