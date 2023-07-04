
import os
from datetime import datetime
import time
from connect_device import ConnectDevice
from sincwise_clients_method import SyncwiseClient


class IntermediateCoordinatesGenerator:
    DICT_IP_DEVICES = {'S10115002211180009': '192.168.2.30'}
    START_COORDINATES = {1: ["50.07807852323376", "36.23065154766116"]}

    def __init__(self):
        print('MAY_DAY')
        ConnectDevice.connect_devices(self.DICT_IP_DEVICES)
        time.sleep(2)

        self.client_data = SyncwiseClient("https://dev-api.syncwise360.com")
        self.client_data.user_account_login()
        self.client_data.course_vector_details()

    @staticmethod
    def touch_screen():
        for id_device, ip_device in IntermediateCoordinatesGenerator.DICT_IP_DEVICES.items():
            os.system(rf'adb -s {ip_device}:5555 shell input tap 700 500')
            print(f'TOUCH SCREEN {id_device} in {datetime.now().time().strftime("%H:%M")}')

    @staticmethod
    def get_start_coordinates():
        print(f'PATH TO START COORDINATE')
        return [IntermediateCoordinatesGenerator.START_COORDINATES[1] for _ in range(10)]

    @staticmethod
    def get_intermediate_coordinates(path, steps):
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

    # @staticmethod
    def run_device(self, steps):
        print(self.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT)
        for i in range(1, self.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT + 1):
            path = [[step_patch['lat'], step_patch['lng']]for step_patch in self.get_intermediate_coordinates(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i], steps)]
            print(f'PATH TO HOLE - > {i}')

            yield path


# generator = IntermediateCoordinatesGenerator()
# # print(generator.get_start_coordinates())
# iterator = generator.run_device(4)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#



