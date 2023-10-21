from sincwise_clients_method import SyncwiseClient
import time
from convert_to_DDMMmmmm import get_new_DDDDmmmm_formate
from generate_csv_utilitygauge import write_utilitygauge_2_csv

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f"Execution time for {func.__name__}: {elapsed_time:.2f} seconds")
        return result
    return wrapper


class IntermediateCoordinatesGenerator:
    DICT_IP_DEVICES = None
    START_COORDINATES = [{'lat': 50.07807852323376, 'lng': 36.23065154766116}]
    OUT_OFF_COURSE_COORDINATES = [{'lat': 50.07810572861073, 'lng': 36.22751781974624}]
    PATH_LIST_HOLES_COORDINATES = []
    # LAST_COORDINATE = None

    def __init__(self):
        self.client_data = SyncwiseClient("https://api2.syncwise360.com")
        self.client_data.user_account_login()
        self.client_data.course_vector_details()
        self.last_coordinate = None

    def get_start_coordinates(self, minutes):
        steps = int(minutes * 60)
        print('RETURN AREA COORDINATE')
        for _ in range(steps):  # start coordinate for begin
            lat, lng = self.START_COORDINATES[0]['lat'], self.START_COORDINATES[0]['lng']
            self.PATH_LIST_HOLES_COORDINATES.append(get_new_DDDDmmmm_formate(f'{lat},{lng}'))
            print(f'step By get_start_coordinates -> {lat}, {lng}')

        self.last_coordinate = self.START_COORDINATES

    def get_intermediate_coordinates(self, path, steps):  #  переделланный под работу с кусочками маршрута
        if steps <= 1 or len(path) <= 1:
            return path

        intermediate_coordinates = []
        num_segments = len(path) - 1
        segment_length = int(steps / num_segments)
        print(f'COUNT SEGMENT --- {num_segments}')

        for i in range(num_segments):
            start_coord = path[i]
            end_coord = path[i + 1]

            for j in range(segment_length):
                ratio = j / segment_length
                lat = start_coord['lat'] + (end_coord['lat'] - start_coord['lat']) * ratio
                lng = start_coord['lng'] + (end_coord['lng'] - start_coord['lng']) * ratio
                intermediate_coordinates.append({'lat': lat, 'lng': lng})

        intermediate_coordinates.append(path[-1])  # Добавляем последнюю координату
        print(f'get_intermediate_coordinates {intermediate_coordinates}')
        print(f'COUNT STEPS FOR HOLE --- {len(intermediate_coordinates)}')
        return intermediate_coordinates

    def run_device_last_step_to_next_point(self, path, minutes):
        steps = int(minutes * 60)
        print(f'MOVED LAST COORDINATE TO NEXT POINT')
        for step_patch in (current_patch := self.get_intermediate_coordinates(path, steps)):
            lat, lng = step_patch['lat'], step_patch['lng']
            print(f'step By run_device_last_step_to_next_point -> {lat}, {lng}')
            self.PATH_LIST_HOLES_COORDINATES.append(get_new_DDDDmmmm_formate(f'{lat},{lng}'))
        self.last_coordinate = [current_patch[-1]]

    def run_device_by_time(self, minutes):  #  генераци нахождения на лунке по времени
        steps = int(minutes * 60)
        for i in range(1, self.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT + 1):
            self.run_device_last_step_to_next_point([self.last_coordinate[0], self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i][0]], 0.1)
            for step_patch in (current_patch := self.get_intermediate_coordinates(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i], steps)):
                lat, lng = step_patch['lat'], step_patch['lng']
                print(f'step By run_device_by_time -> ON HOLE ({i}) -> {lat}, {lng}')
                self.PATH_LIST_HOLES_COORDINATES.append(get_new_DDDDmmmm_formate(f'{lat},{lng}'))
            self.last_coordinate = [current_patch[-1]]


    def run_device_from_start_coordinate_to_first_hole(self, minutes):
        """ Расчет маршрута от стартовых координат к координатам HOLE 1"""
        steps = int(minutes * 60)
        self.run_device_last_step_to_next_point([self.last_coordinate[0], self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[1][0]], steps)

    def run_device_from_last_hole_to_start_coordinate(self, minutes):
        """ Расчет маршрута от финишных координат к координатам RETURN AREA"""
        print(f'MOVED TO RETURN AREA COORDINATE')
        self.run_device_last_step_to_next_point([self.last_coordinate[0], self.START_COORDINATES[0]], minutes)




generator = IntermediateCoordinatesGenerator()

generator.get_start_coordinates(0.1)
generator.run_device_by_time(0.1)
generator.run_device_from_last_hole_to_start_coordinate(0.1)
generator.get_start_coordinates(0.1)


print("Everything has gone well.".upper())
print(f'TOTAL STEPS - {len(generator.PATH_LIST_HOLES_COORDINATES)}')
write_utilitygauge_2_csv(generator.PATH_LIST_HOLES_COORDINATES)
