import time

import pyautogui


while True:
    x, y = pyautogui.position()
    print(f"Текущие координаты курсора: x={x}, y={y}")
    time.sleep(0.5)

