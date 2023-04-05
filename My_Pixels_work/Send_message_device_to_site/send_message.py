import os
import random
import time
from datetime import datetime, timedelta

def press_button_menu():
    os.system(f'adb shell input tap 50 50')    # touch button "MENU"
    print('PRESS BUTTON MENU')


def press_button_send_mail():
    os.system(f'adb shell input tap 1000 200')  # touch button "SEND MAIL"
    print('PRESS BUTTON SEND MAIL')


def press_button_settings():
    os.system(f'adb shell input tap 800 600')   # touch button "SETTING"
    print('PRESS BUTTON SETTINGS')


def enter_password_settings():
    os.system(f'adb shell input tap 600 300')   # touch button "5"
    os.system(f'adb shell input tap 600 300')   # touch button "5"
    os.system(f'adb shell input tap 600 300')   # touch button "5"
    os.system(f'adb shell input tap 600 300')   # touch button "5"
    os.system(f'adb shell input tap 600 300')   # touch button "5"
    os.system(f'adb shell input tap 600 300')   # touch button "5"


def press_select_message():
    os.system(f'adb shell input tap 50 {random.randint(1, 8)}50')
    print('SELECT MAIL')


def press_yes_button():
    os.system(f'adb shell input tap 500 650')  # touch button "SEND MAIL"
    print('PRESS YES BUTTON')


press_button_menu()

start = datetime.now()  # получаем текущее время
finish = start + timedelta(hours=5)  # добавляем 2 hours

while datetime.now() < finish:
    press_button_send_mail()
    press_select_message()
    press_yes_button()
    time.sleep(30)

    print(f'{start} -> {datetime.now()} -> {finish}')
