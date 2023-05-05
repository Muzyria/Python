# import pyautogui
# import time
#
# # # Открываем окно блокнота
# # pyautogui.press('win')
# # pyautogui.typewrite('notepad')
# # pyautogui.press('enter')
# # time.sleep(2)  # Ждем 2 секунды
# #
# # # Вводим текст
# # pyautogui.typewrite('Hello, World!')
# #
# # # Сохраняем файл
# # pyautogui.hotkey('ctrl', 's')
# # time.sleep(2)  # Ждем 2 секунды
# # pyautogui.typewrite('example.txt')
# # pyautogui.press('enter')
#
#
# # # Получаем текущие координаты курсора
# # x, y = pyautogui.position()
# # print(f"Текущие координаты курсора: x={x}, y={y}")
# #
# # # Перемещаем курсор в новые координаты
# # pyautogui.moveTo(100, 100)
# # pyautogui.moveTo(200, 200)
# # pyautogui.moveTo(300, 300)
# #
# # # Нажимаем и отпускаем левую кнопку мыши
# # pyautogui.click(button='left')
# #
# # # Отпускаем клавиши
# # pyautogui.keyUp('shift')
# # pyautogui.keyUp('ctrl')
#
# import pyautogui
# from PIL import Image
#
# # Получаем скриншот экрана
# screenshot = pyautogui.screenshot()
#
# # Сохраняем скриншот в файл
# screenshot.save('screenshot.png')
#
# # Открываем сохраненный файл и обрабатываем его с помощью библиотеки Pillow
# im = Image.open('screenshot.png')
#
# # Выводим размер изображения
# print("Размер изображения: ", im.size)
#
# # Показываем изображение
# im.show()
# import math
# import pyautogui
#
# # Устанавливаем центр окружности
# center_x, center_y = 500, 500
#
# # Устанавливаем радиус окружности
# radius = 100
#
# # Вычисляем количество шагов для обхода окружности
# num_steps = int(360 / 10)
#
# # Вычисляем шаг угла для каждого шага
# step_angle = 10 * math.pi / 180
#
# # Устанавливаем задержку между шагами
# pyautogui.PAUSE = 0.01
#
# # Движение курсора по окружности
# for i in range(num_steps):
#     # Вычисляем координаты точки на окружности
#     x = center_x + radius * math.cos(i * step_angle)
#     y = center_y + radius * math.sin(i * step_angle)
#
#     # Перемещаем курсор на новые координаты
#     pyautogui.moveTo(x, y)

# import math
# import pyautogui
#
# # Устанавливаем радиус окружности
# radius = 100
#
# # Вычисляем количество шагов для обхода окружности
# num_steps = int(360 / 10)
#
# # Вычисляем шаг угла для каждого шага
# step_angle = 10 * math.pi / 180
#
# # Устанавливаем задержку между шагами
# pyautogui.PAUSE = 0.01
#
# # Рисуем пять окружностей
# for i in range(5):
#     # Устанавливаем центр окружности
#     center_x = 500 + i * 2 * radius
#     center_y = 500
#
#     # Движение курсора по окружности
#     for j in range(num_steps):
#         # Вычисляем координаты точки на окружности
#         x = center_x + radius * math.cos(j * step_angle)
#         y = center_y + radius * math.sin(j * step_angle)
#
#         # Перемещаем курсор на новые координаты
#         pyautogui.moveTo(x, y)

# import subprocess
#
# # Запускаем Telegram Desktop
# subprocess.Popen(r"C:\Users\Fila\AppData\Roaming\Telegram Desktop\Telegram.exe")

