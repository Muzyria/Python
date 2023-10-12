import os
import subprocess
import time
from datetime import datetime, timedelta


class Scheduler:
    def __init__(self, ip_device):
        self.ip_device = ip_device

    def get_value_new_time(self, minutes=1, seconds=10):
        """RETURN NEW TIME"""
        now = datetime.now()  # получаем текущее время
        one_minute_later = now + timedelta(minutes=minutes, seconds=seconds)  # добавляем 1 минуту к текущему времени
        hour = one_minute_later.time().hour  # получаем часы через 1 минуту
        minute = one_minute_later.time().minute  # получаем минуты через 1 минуту
        print(f'Расчетное время power_off_time={hour:02}:{minute:02}')
        print()
        return f'{hour:02}{minute:02}'

    def check_devices_active(self):
        output = subprocess.check_output(['adb', 'devices'])
        # Проверяем, есть ли подключенные устройства в выводе
        if self.ip_device in str(output) and "offline" not in str(output):
            print('Устройство Android подключено и активно.')

        else:
            print(f'Устройство Android {self.ip_device} будет подключено. -----> ')
            self.device_disconnect()
            time.sleep(2)
            self.device_connect()

    def adb_get_state(self):
        output = os.system('adb get-state')
        print(f'{output}-------------')

    def device_disconnect(self):
        os.system(f'adb disconnect')

    def device_connect(self):
        os.system(f'adb connect {self.ip_device}')

    def get_time_off(self):
        print('time_off ', end='')
        os.system(f'adb shell settings get system power_off_time')

    def get_random_power_off_time(self):
        print('random_power_off_time ', end='')
        os.system(f'adb shell settings get system random_power_off_time')

    def put_time_off(self, time):
        os.system(f'adb shell settings put system power_off_time {time}')

    def put_random_power_off_time(self, time):
        os.system(f'adb shell settings put system random_power_off_time {time}')

    def open_date_settings(self):
        os.system('adb shell am start -a android.settings.DATE_SETTINGS')



