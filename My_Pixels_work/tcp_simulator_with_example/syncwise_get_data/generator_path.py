import os
from datetime import datetime, timedelta

from sincwise_clients_method import SyncwiseClient

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
    DICT_IP_DEVICES = {'W_W_W_->>>': '192.168.3.221'}
    START_COORDINATES = [{'lat': 50.07807852323376, 'lng': 36.23065154766116}]
    OUT_OFF_COURSE_COORDINATES = [{'lat': 50.07810572861073, 'lng': 36.22751781974624}]
    PATH_LIST_HOLES = None

    def __init__(self):
        self.client_data = SyncwiseClient("https://api2.syncwise360.com")
        self.client_data.user_account_login()
        self.client_data.course_vector_details()
        self.last_coordinate = None




    def get_start_coordinates(self, steps):
        print('RETURN AREA COORDINATE')
        for _ in range(steps):  # start coordinate for begin192.168
            time_minute = datetime.now().time().minute

            lat, lng = self.START_COORDINATES[0]['lat'], self.START_COORDINATES[0]['lng']
            print(f'step -> {lat}, {lng}')

        self.last_coordinate = self.START_COORDINATES



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
        print(intermediate_coordinates)
        print(f'COUNT STEPS FOR HOLE --- {len(intermediate_coordinates)}')
        return intermediate_coordinates



    def run_device_last_step_to_next_point(self, path, steps):
        print(f'MOVED LAST COORDINATE TO NEXT POINT')
        # temp_coord = [{'lat': 50.07807852323376, 'lng': 36.23065154766116}, {'lat': 50.079678437647, 'lng': 36.231405436993}]
        for step_patch in self.get_intermediate_coordinates(path, steps):
            lat, lng = step_patch['lat'], step_patch['lng']
            print(f'step -> {lat}, {lng}')



    def run_device_by_time(self, minutes):  #  генераци нахождения на лунке по времени
        steps = int(minutes * 60)


        for i in range(1, self.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT + 1):

            for step_patch in (current_patch := self.get_intermediate_coordinates(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i], steps)):
                lat, lng = step_patch['lat'], step_patch['lng']
                print(f'step -> {lat}, {lng}')






generator = IntermediateCoordinatesGenerator()

generator.get_start_coordinates(10)

generator.run_device_by_time(0.5)

generator.run_device_last_step_to_next_point([generator.last_coordinate[0], generator.START_COORDINATES[0]], 40)
generator.get_start_coordinates(10)


print("Everything went well.".upper())
