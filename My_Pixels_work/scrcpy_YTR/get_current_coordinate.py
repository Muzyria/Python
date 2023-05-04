import pyautogui
import time

# Получаем текущие координаты курсора
while True:
    x, y = pyautogui.position()
    time.sleep(0.5)
    print(f"Текущие координаты курсора: x={x}, y={y}")
