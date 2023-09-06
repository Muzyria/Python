import os
import subprocess
import time
from datetime import datetime, timedelta


class Scheduler:
    def get_value_new_time(self, minutes=1, seconds=10):
        now = datetime.now()  # получаем текущее время
        one_minute_later = now + timedelta(minutes=minutes, seconds=seconds)  # добавляем 1 минуту к текущему времени
        hour = one_minute_later.time().hour  # получаем часы через 1 минуту
        minute = one_minute_later.time().minute  # получаем минуты через 1 минуту
        print(f'Расчетное время power_off_time={hour:02}:{minute:02}')
        print()
        return f'{hour:02}{minute:02}'

    def check_devices_active(self, ip_address=None):
        output = subprocess.check_output(['adb', 'devices'])
        # Проверяем, есть ли подключенные устройства в выводе
        if ip_address in str(output) and "offline" not in str(output):
            print('Устройство Android подключено и активно.')

        else:
            print(f'Устройство Android {ip_address} будет подключено. -----> ')
            self.device_disconnect()
            self.device_connect(ip_address)

    def adb_get_state(self):
        output = os.system('adb get-state')
        print(f'{output}-------------')

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

    def open_date_settings(self):
        os.system('adb shell am start -a android.settings.DATE_SETTINGS')



