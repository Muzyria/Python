import os
from datetime import datetime, timedelta
import random
from sincwise_clients_method import SyncwiseClient
from connect_device import ConnectDevice
from time import perf_counter
import time


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f"Execution time for {func.__name__}: {elapsed_time:.2f} seconds")
        return result
    return wrapper

class IntermediateCoordinatesGenerator:
    # DICT_IP_DEVICES = {'S10115002211180009': '192.168.2.30', 'L101140017180605A5': '192.168.3.174'}
    DICT_IP_DEVICES = {'O_OLIH': '192.168.3.130'}
    START_COORDINATES = "50.07807852323376, 36.23065154766116"

    def __init__(self):
        ConnectDevice.connect_devices(self.DICT_IP_DEVICES)
        time.sleep(5)

        # for ip_device in self.DICT_IP_DEVICES.values():
        #     ConnectDevice.connect_device(ip_device)
        #     time.sleep(10)

        self.client_data = SyncwiseClient("https://dev-api.syncwise360.com")
        self.client_data.user_account_login()
        self.client_data.course_vector_details()
        # print(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH)

    @execution_time_decorator
    def send_adb_command(self, ip_device, location):
        os.system(
            rf'adb -s {ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')

    def get_start_coordinates(self, minutes):
        steps = int(minutes * 30)
        for _ in range(steps):  # start coordinate for begin
            time_minute = datetime.now().time().minute

            for ip_device in self.DICT_IP_DEVICES.values():
                self.send_adb_command(ip_device, self.START_COORDINATES)
                if (now := datetime.now().time().minute) != time_minute:
                    time_minute = now
                    self.touch_screen()

    @execution_time_decorator
    def touch_screen(self):
        for id_device, ip_device in self.DICT_IP_DEVICES.items():
            os.system(rf'adb -s {ip_device}:5555 shell input tap 700 500')
            print(f'TOUCH SCREEN {id_device} in {datetime.now().time().strftime("%H:%M")}')

    @execution_time_decorator
    def send_message_from_device(self):
        for id_device, ip_device in self.DICT_IP_DEVICES.items():
            os.system(rf'adb -s {ip_device}:5555 shell input tap 50 50')  # PRESS BUTTON MENU
            print(f'PRESS BUTTON MENU ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 1000 200')  # PRESS BUTTON SEND MAIL
            print(f'PRESS BUTTON SEND MAIL ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 50 {random.randint(1, 8)}50')  # SELECT RANDOM MAIL
            print(f'SELECT MAIL ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 500 650')  # PRESS YES BUTTON
            print(f'PRESS YES BUTTON ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

    @execution_time_decorator
    def send_order_food_device(self):
        for id_device, ip_device in self.DICT_IP_DEVICES.items():
            os.system(rf'adb -s {ip_device}:5555 shell input tap 1100 700')  # PRESS BUTTON FOOD and DRINK
            print(f'PRESS BUTTON FOOD and DRINK ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 50 {random.randint(1, 5)}50')  # SELECT RANDOM FOOD
            print(f'SELECT RANDOM FOOD ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 50 100')  # PRESS BUTTON FIRST ITEM IN LIST FOOD
            print(f'PRESS BUTTON FIRST ITEM IN LIST FOOD ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 1100 750')  # PRESS BUTTON ADD TO ORDER
            print(f'PRESS BUTTON ADD TO ORDER ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            print('WAIT FOR FEW SECONDS')
            time.sleep(2)
            os.system(rf'adb -s {ip_device}:5555 shell input tap 1100 750')  # PRESS BUTTON SUBMIT ORDER
            print(f'PRESS BUTTON SUBMIT ORDER ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 1100 750')  # PRESS BUTTON SUBMIT ORDER
            print(f'PRESS BUTTON SUBMIT ORDER ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input text "player_1"')  # INPUT NAME FOR ORDER
            print(f'INPUT NAME FOR ORDER ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input keyevent 66')  # INPUT ENTER BUTTON
            print(f'INPUT ENTER BUTTON ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 50 100')  # PRESS BUTTON FIRST ITEM IN LIST PRINTERS
            print(f'PRESS BUTTON FIRST ITEM IN LIST PRINTERS ON {id_device} in {datetime.now().time().strftime("%H:%M")}')
            os.system(rf'adb -s {ip_device}:5555 shell input tap 600 650')  # PRESS BUTTON CLOSE
            print(f'PRESS BUTTON CLOSE ON {id_device} in {datetime.now().time().strftime("%H:%M")}')

    def get_intermediate_coordinates(self, path, steps):  #  переделланный под работу с кусочками маршрута
        if steps <= 1 or len(path) <= 1:
            return path

        intermediate_coordinates = []
        num_segments = len(path) - 1
        segment_length = int(steps / num_segments)
        print(f'COUNT SEGMENT --- {segment_length}')

        for i in range(num_segments):
            start_coord = path[i]
            end_coord = path[i + 1]

            for j in range(segment_length):
                ratio = j / segment_length
                lat = start_coord['lat'] + (end_coord['lat'] - start_coord['lat']) * ratio
                lng = start_coord['lng'] + (end_coord['lng'] - start_coord['lng']) * ratio
                intermediate_coordinates.append({'lat': lat, 'lng': lng})

        intermediate_coordinates.append(path[-1])  # Добавляем последнюю координату
        print(f'COUNT STEPS FOR HOLE --- {len(intermediate_coordinates)}')
        return intermediate_coordinates

    def run_device_by_time(self, minutes, count_holes):  #  генераци нахождения на лунке по времени
        """генераци нахождения на лунке по времени"""
        steps = int(minutes * 30)

        for i in range(1, count_holes + 1):
            time_start_on_hole = datetime.now()
            time_finish_on_hole = time_start_on_hole + timedelta(minutes=minutes, seconds=-4)
            time_minute = datetime.now().time().minute
            print(f'STARTING TRIP ON HOLE ---> {i} in {time_start_on_hole.strftime("%H:%M:%S")} to {time_finish_on_hole.strftime("%H:%M:%S")}')

            for step_patch in (current_patch := self.get_intermediate_coordinates(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i], steps)):
                lat, lng = step_patch['lat'], step_patch['lng']
                print(f'step -> {lat}, {lng}')

                if datetime.now() <= time_finish_on_hole:  #  контролируем время нахождения на лунке
                    for ip_device in self.DICT_IP_DEVICES.values():
                        self.send_adb_command(ip_device, f"{lat}, {lng}")
                        if (now := datetime.now().time().minute) != time_minute:
                            time_minute = now
                            # self.touch_screen()
                            self.send_order_food_device() if random.randint(0, 1) else self.send_message_from_device()

                else:
                    for ip_device in self.DICT_IP_DEVICES.values():
                        print(f'FINISHING TRIP ON HOLE ---> {i} IN {datetime.now().strftime("%H:%M:%S")}')
                        lat, lng = current_patch[-1]
                        self.send_adb_command(ip_device, f"{lat}, {lng}")
                    break


generator = IntermediateCoordinatesGenerator()

while True:
    generator.get_start_coordinates(2)
    generator.run_device_by_time(3, 5)  # minuts on hole, count holes
    generator.get_start_coordinates(2)



