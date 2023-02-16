import os
import subprocess
import time
from datetime import datetime, timedelta

def set_time():
    now = datetime.now()  # получаем текущее время
    one_minute_later = now + timedelta(minutes=1)  # добавляем 1 минуту к текущему времени
    hour = one_minute_later.time().hour  # получаем часы через 1 минуту
    minute = one_minute_later.time().minute  # получаем минуты через 1 минуту
    print(f'Будет установалено power_off_time={hour:02}:{minute:02}')
    print()
    return f'{hour:02}{minute:02}'

def check_devices_active():
    # Запускаем команду adb devices для получения списка устройств
    output = subprocess.check_output(['adb', 'devices'])
    # Проверяем, есть ли подключенные устройства в выводе
    if b'device' in output:
        print('Устройство Android подключено и активно.')
        return True

    else:
        print('Устройство Android не найдено или неактивно. -----> ')
        return False

def get_time_off():
    os.system(f'adb shell settings get system power_off_time')


while True:
    if check_devices_active():
        os.system(f'adb shell settings put system power_off_time {set_time()}')
        time.sleep(5)
        print(f'time_off_timer = {get_time_off()}')
        time.sleep(140)
    else:
        time.sleep(60)
