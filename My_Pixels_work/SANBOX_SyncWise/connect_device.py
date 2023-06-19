import multiprocessing
import time

import pyautogui


class ConnectDevice:
    @staticmethod
    def connect_devise(ip_device):
        pyautogui.hotkey('win', 'r')
        pyautogui.typewrite('cmd')
        pyautogui.press('enter')
        time.sleep(1)

        # печатаем команду
        pyautogui.typewrite(r'cd C:\scrcpy-win64-v2.0\scrcpy-win64-v2.0')
        pyautogui.press('enter')

        pyautogui.typewrite(fr'scrcpy --tcpip={ip_device}:5555')
        pyautogui.press('enter')
        print(f'CONNECTED TCP/IP {ip_device}')

    @staticmethod
    def connect_devices(DICT_IP_DEVICES):
        pool = multiprocessing.Pool()
        for ip_device in DICT_IP_DEVICES.values():
            pool.apply_async(ConnectDevice.connect_device, args=(ip_device,))
        pool.close()
        pool.join()
