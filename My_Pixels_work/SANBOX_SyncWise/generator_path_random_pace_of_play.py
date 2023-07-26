import os
from datetime import datetime, timedelta

from sincwise_clients_method import SyncwiseClient
from connect_device import ConnectDevice
from time import perf_counter
import time
import random


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
    DICT_IP_DEVICES = {'W_W_W_->>>': '192.168.3.219'}
    START_COORDINATES = "50.07807852323376, 36.23065154766116"
    PATH_LIST_HOLES = None


    def __init__(self):
        ConnectDevice.connect_devices(self.DICT_IP_DEVICES)
        time.sleep(5)

        self.client_data = SyncwiseClient("https://dev-api.syncwise360.com")
        self.client_data.user_account_login()
        self.client_data.course_vector_details()
        # print(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH)


    def generate_random_path(self, number_holes, range_time: tuple):
        """Generator random path with range of time"""
        path = [(i, random.randint(range_time[0], range_time[1])) for i in range(1, number_holes + 1)]
        random.shuffle(path)
        print(path)  # [(1, 3), (11, 3), (4, 3), (17, 3), (13, 3), (8, 3), (6, 3), (2, 3), (10, 3), (18, 3), (15, 4), (5, 4), (16, 3), (12, 3), (14, 4), (3, 3), (7, 4), (9, 3)]
        print(f"TIME FOR ALL PATH MORE THEN {sum(map(lambda x: x[1], path))}")
        self.PATH_LIST_HOLES = path

    @execution_time_decorator
    def send_adb_command(self, ip_device, location):
        os.system(
            rf'adb -s {ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')

    def get_start_coordinates(self):
        for _ in range(60):  # start coordinate for begin
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

    # def get_intermediate_coordinates(self, path, steps):
    #     if steps <= 1 or len(path) <= 1:
    #         return path
    #
    #     intermediate_coordinates = []
    #     num_segments = len(path) - 1
    #     segment_length = steps / num_segments
    #
    #     for i in range(num_segments):
    #         start_coord = path[i]
    #         end_coord = path[i + 1]
    #
    #         for j in range(steps):
    #             ratio = j / steps
    #             lat = start_coord['lat'] + (end_coord['lat'] - start_coord['lat']) * ratio
    #             lng = start_coord['lng'] + (end_coord['lng'] - start_coord['lng']) * ratio
    #             intermediate_coordinates.append({'lat': lat, 'lng': lng})
    #
    #     intermediate_coordinates.append(path[-1])  # Добавляем последнюю координату
    #     return intermediate_coordinates

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

    def run_device(self, steps):
        for i in range(1, self.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT + 1):
            for step_patch in self.get_intermediate_coordinates(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i], steps):
                lat, lng = step_patch['lat'], step_patch['lng']
                print(f'step -> {lat}, {lng}')
                time_minute = datetime.now().time().minute

                for ip_device in self.DICT_IP_DEVICES.values():
                    self.send_adb_command(ip_device, f"{lat}, {lng}")
                    if (now := datetime.now().time().minute) != time_minute:
                        time_minute = now
                        self.touch_screen()

    def run_device_by_time(self, minutes):  #  генераци нахождения на лунке по времени
        steps = int(minutes * 30)
        time_on_hole = None  # Declare the variable outside the loop

        for i in range(1, self.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT + 1):
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
                            self.touch_screen()

                else:
                    for ip_device in self.DICT_IP_DEVICES.values():
                        print(f'FINISHING TRIP ON HOLE ---> {i} IN {datetime.now().strftime("%H:%M:%S")}')
                        lat, lng = current_patch[-1]
                        self.send_adb_command(ip_device, f"{lat}, {lng}")
                    break

    def run_device_by_random_path(self):  #  генераци нахождения на лунке по времени

        for item in self.PATH_LIST_HOLES:  #
            steps = int(item[1] * 30)  # count steps
            time_start_on_hole = datetime.now()  # start time
            time_finish_on_hole = time_start_on_hole + timedelta(minutes=item[1], seconds=-4)  # finish time
            time_minute = datetime.now().time().minute
            print(f'STARTING TRIP ON HOLE ---> {item[0]} in {time_start_on_hole.strftime("%H:%M:%S")} to {time_finish_on_hole.strftime("%H:%M:%S")}')

            for step_patch in (current_patch := self.get_intermediate_coordinates(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[item[0]], steps)):
                lat, lng = step_patch['lat'], step_patch['lng']
                print(f'step -> {lat}, {lng}')

                if datetime.now() <= time_finish_on_hole:  #  контролируем время нахождения на лунке
                    for ip_device in self.DICT_IP_DEVICES.values():
                        self.send_adb_command(ip_device, f"{lat}, {lng}")
                        if (now := datetime.now().time().minute) != time_minute:
                            time_minute = now
                            self.touch_screen()

                else:
                    for ip_device in self.DICT_IP_DEVICES.values():
                        print(f'FINISHING TRIP ON HOLE ---> {item} IN {datetime.now().strftime("%H:%M:%S")}')
                        lat, lng = current_patch[-1]
                        self.send_adb_command(ip_device, f"{lat}, {lng}")
                    break


generator = IntermediateCoordinatesGenerator()

generator.generate_random_path(18, (4, 6))



