import os
import random
import time
from datetime import datetime


devices = {'QWERTY': '192.168.3.219'}

def send_order_food_device():
    for id_device, ip_device in devices.items():
        os.system(rf'adb shell input tap 1100 700')  # PRESS BUTTON FOOD and DRINK
        print(f'PRESS BUTTON FOOD and DRINK ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        os.system(rf'adb shell input tap 50 {random.randint(1, 5)}50')  # SELECT RANDOM FOOD
        print(f'SELECT RANDOM FOOD ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        os.system(rf'adb shell input tap 50 100')  # PRESS BUTTON FIRST ITEM IN LIST FOOD
        print(f'PRESS BUTTON FIRST ITEM IN LIST FOOD ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        os.system(rf'adb shell input tap 1100 750')  # PRESS BUTTON ADD TO ORDER
        print(f'PRESS BUTTON ADD TO ORDER ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        print('WAIT FOR FEW SECONDS')
        time.sleep(2)

        os.system(rf'adb shell input tap 1100 750')  # PRESS BUTTON SUBMIT ORDER
        print(f'PRESS BUTTON SUBMIT ORDER ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        os.system(rf'adb shell input tap 1100 750')  # PRESS BUTTON SUBMIT ORDER
        print(f'PRESS BUTTON SUBMIT ORDER ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        os.system(rf'adb shell input text "player_1"')  # INPUT NAME FOR ORDER
        print(f'INPUT NAME FOR ORDER ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        os.system(rf'adb shell input keyevent 66')  # INPUT ENTER BUTTON
        print(f'INPUT ENTER BUTTON ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        os.system(rf'adb shell input tap 50 100')  # PRESS BUTTON FIRST ITEM IN LIST PRINTERS
        print(f'PRESS BUTTON FIRST ITEM IN LIST PRINTERS ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

        os.system(rf'adb shell input tap 600 650')  # PRESS BUTTON CLOSE
        print(f'PRESS BUTTON CLOSE ON {id_device} in {datetime.now().time().strftime("%H:%M")}')







send_order_food_device()
