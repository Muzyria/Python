import pyautogui
import time


# # Нажимаем клавишу Win (кнопка с логотипом Windows на клавиатуре)
# pyautogui.press('win')
# # Вводим название приложения в строку поиска
# pyautogui.write('scrcpy')
# # Ждем, пока поисковая строка обновится
# pyautogui.sleep(1)
# # Выбираем приложение в списке
# pyautogui.press('enter')
# # Ждем, пока браузер запустится
# pyautogui.sleep(5)


### import win32api
##
#     # Получаем текущий язык ввода
# lang = win32api.GetKeyboardLayout()
# if lang != 67699721:
#     pyautogui.hotkey('alt', 'shift')
#
# time.sleep(2)


# открываем командную строку
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
pyautogui.press('enter')
time.sleep(1)


# печатаем команду
pyautogui.typewrite(r'cd C:\scrcpy-win64-v2.0\scrcpy-win64-v2.0')
pyautogui.press('enter')

# pyautogui.typewrite(r'scrcpy --tcpip=192.168.3.128:40375')  # MY POCO in office
# pyautogui.typewrite(r'scrcpy --tcpip=192.168.0.103:42285')  # MY POCO at home
pyautogui.typewrite(r'scrcpy --tcpip=192.168.0.101:5555')
# pyautogui.typewrite(r'scrcpy -s 61c74e97')
pyautogui.press('enter')


