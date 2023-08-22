import os
import subprocess
import time
from datetime import datetime, timedelta


class Scheduler:
    def set_power_of_time(self, minutes=1, seconds=10):
        now = datetime.now()  # получаем текущее время
        one_minute_later = now + timedelta(minutes=minutes, seconds=seconds)  # добавляем 1 минуту к текущему времени
        hour = one_minute_later.time().hour  # получаем часы через 1 минуту
        minute = one_minute_later.time().minute  # получаем минуты через 1 минуту
        print(f'Будет установалено power_off_time={hour:02}:{minute:02}')
        print()
        return f'{hour:02}{minute:02}'

    def check_devices_active(self, ip_address=None):
        output = subprocess.check_output(['adb', 'devices'])
        # Проверяем, есть ли подключенные устройства в выводе
        if ip_address in str(output):
            print('Устройство Android подключено и активно.')

        else:
            print('Устройство Android будет подключено. -----> ')
            self.device_disconnect()
            self.device_connect(ip_address)

    def device_disconnect(self):
        os.system(f'adb disconnect')

    def device_connect(self, ip_address):
        os.system(f'adb connect {ip_address}')

    def get_time_off(self):
        os.system(f'adb shell settings get system power_off_time')

    def get_random_power_off_time(self):
        os.system(f'adb shell settings get system random_power_off_time')


    def put_time_off(self, time):
        os.system(f'adb shell settings put system power_off_time {time}')

    def put_random_power_off_time(self, time):
        os.system(f'shell settings put system random_power_off_time {time}')



