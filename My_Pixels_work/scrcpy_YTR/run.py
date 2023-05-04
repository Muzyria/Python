import pyautogui
import time

# # Открываем окно блокнота
# pyautogui.press('win')
# pyautogui.typewrite('notepad')
# pyautogui.press('enter')
# time.sleep(2)  # Ждем 2 секунды
#
# # Вводим текст
# pyautogui.typewrite('Hello, World!')
#
# # Сохраняем файл
# pyautogui.hotkey('ctrl', 's')
# time.sleep(2)  # Ждем 2 секунды
# pyautogui.typewrite('example.txt')
# pyautogui.press('enter')


# Получаем текущие координаты курсора
# while True:
#     x, y = pyautogui.position()
#     time.sleep(0.5)
#     print(f"Текущие координаты курсора: x={x}, y={y}")

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


#
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

pyautogui.typewrite(r'scrcpy --tcpip=192.168.2.30:5555')
pyautogui.press('enter')


