import os
from datetime import datetime

from sincwise_clients_method import SyncwiseClient
import pyautogui
import time

class IntermediateCoordinatesGenerator:
    def __init__(self):
        # self.connect_devise()
        # time.sleep(10)
        self.client_data = SyncwiseClient("https://dev-api.syncwise360.com")
        self.client_data.user_account_login()
        self.client_data.course_vector_details()
        # print(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH)

    def connect_devise(self):
        pyautogui.hotkey('win', 'r')
        pyautogui.typewrite('cmd')
        pyautogui.press('enter')
        time.sleep(1)

        # печатаем команду
        pyautogui.typewrite(r'cd C:\scrcpy-win64-v2.0\scrcpy-win64-v2.0')
        pyautogui.press('enter')

        pyautogui.typewrite(r'scrcpy --tcpip=192.168.2.30:5555')
        pyautogui.press('enter')

    def get_intermediate_coordinates(self, path, steps):
        if steps <= 1 or len(path) <= 1:
            return path

        intermediate_coordinates = []
        num_segments = len(path) - 1
        segment_length = steps / num_segments

        for i in range(num_segments):
            start_coord = path[i]
            end_coord = path[i + 1]

            for j in range(steps):
                ratio = j / steps
                lat = start_coord['lat'] + (end_coord['lat'] - start_coord['lat']) * ratio
                lng = start_coord['lng'] + (end_coord['lng'] - start_coord['lng']) * ratio
                intermediate_coordinates.append({'lat': lat, 'lng': lng})

        intermediate_coordinates.append(path[-1])  # Добавляем последнюю координату

        return intermediate_coordinates


# path = [
#     {'lat': 50.079678437647, 'lng': 36.231405436993},
#     {'lat': 50.082184485494, 'lng': 36.231842637062}
# ]

steps = 1
generator = IntermediateCoordinatesGenerator()


# start_coordinates = "50.07807852323376, 36.23065154766116"
#
# for _ in range(50):  # start coordinate for begin
#     time_minute = datetime.now().time().minute
#     os.system(rf'adb shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{start_coordinates}\"')
#     if (now := datetime.now().time().minute) != time_minute:
#         time_minute = now
#         os.system(rf'adb shell input tap 700 500')
#         print(f'TOUCH SCREEN in {datetime.now().time().strftime("%H:%M")}')

# print(generator.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH)
for i in range(1, generator.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT + 1):
    print(f'{generator.get_intermediate_coordinates(generator.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i], steps)}  ------ new coord {i}')





