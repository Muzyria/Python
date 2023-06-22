import asyncio
import os
from datetime import datetime

from sincwise_clients_method import SyncwiseClient
from connect_device import ConnectDevice
from time import perf_counter
import asyncio
from may_day_may_day import push
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
    DICT_IP_DEVICES = {'S10115002211180009': '192.168.2.30'}
    START_COORDINATES = {1: ["50.07807852323376", "36.23065154766116"]}


    # @execution_time_decorator
    # def send_adb_command(self, ip_device, location):
    #     os.system(
    #         rf'adb -s {ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')

    def get_start_coordinates(self):
        coordinates = [self.START_COORDINATES[1] for _ in range(3)]
        push('192.168.3.219', coordinates)



    @execution_time_decorator
    def touch_screen(self):
        for id_device, ip_device in self.DICT_IP_DEVICES.items():
            os.system(rf'adb -s {ip_device}:5555 shell input tap 700 500')
            print(f'TOUCH SCREEN {id_device} in {datetime.now().time().strftime("%H:%M")}')

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


generator = IntermediateCoordinatesGenerator()

generator.get_start_coordinates()

generator.get_start_coordinates()




