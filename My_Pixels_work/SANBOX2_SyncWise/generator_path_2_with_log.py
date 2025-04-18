import os

from datetime import datetime, timedelta

from sincwise_clients_method import SyncwiseClient
from connect_device import ConnectDevice

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
    DICT_IP_DEVICES = {'W_W_W_->>>': '192.168.0.103'}
    # START_COORDINATES = "50.07807852323376, 36.23065154766116" # superior
    # START_COORDINATES = "49.86316203910068, 24.029529539745567" # lviv demo
    # START_COORDINATES = "41.399138246290164, -75.71986696282578"  # Eighteen Hole-Pine
    START_COORDINATES = "41.12502128041975, -73.85760706390852"  # Eighteen-Sleepy Hollow Country Club
    # START_COORDINATES = "43.48540681475642, -79.77989637028654"  # Angels View-Oakville Executive Golf Courses 9 holes

    def __init__(self):
        ConnectDevice.connect_devices(self.DICT_IP_DEVICES)
        time.sleep(5)

        # for ip_device in self.DICT_IP_DEVICES.values():
        #     ConnectDevice.connect_device(ip_device)
        #     time.sleep(10)

        self.client_data = SyncwiseClient("https://dev-api-gateway.syncwise360.com")
        self.client_data.user_account_login()

        # self.client_data.course_vector_details("Xy4NX6enHAhQ")  # Eighteen Hole-Pine
        # self.client_data.course_vector_details("vUBhsVKC7vLg")  # Par 3-Pine Hills
        self.client_data.course_vector_details("7rOQfXBAtJ2C")  # Eighteen-Sleepy Hollow Country Club
        # self.client_data.course_vector_details("GsVhpjLhrEIy")  # Eighteen-Sleepy Nine
        # self.client_data.course_vector_details("GfzkZL9LMMuc")  # Angels View-Oakville Executive Golf Courses 9 holes

        # print(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH)

    @execution_time_decorator
    def send_adb_command(self, ip_device, location):
        os.system(
            rf'adb -s {ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')

    @staticmethod
    def log_to_file(message):
        with open('logs_trip/log.txt', 'a') as log_file:
            log_file.write(message + '\n')

    def get_start_coordinates(self, minutes):
        steps = int(minutes * 40)
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

    def run_device_by_time(self, minutes=None):  #  генераци нахождения на лунке по времени
        # steps = int(minutes * 40) # ----------------------------

        # time_list = [0, 6, 6, 6, 6, 6, 6, 6, 6, 6]

                     #  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8
        time_list = [0, 6, 6,6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        # 18 hole = 3min (meaning minimum trigger for pace) , on hole 1 = 3 min , on hole 2 = 1 min, hole 3 = 1 min, hole 4 = 1 min, hole 5 = 5 min (6...17 = 3 min )
        # time_list = [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

        for i in range(1, self.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT + 1):  # MAIN
        # for i in [18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
        # for i in range(1, 4):
            # ------------- ---------------- -------------- -----------------
            # minutes = random.randint(4, 5)
            minutes = time_list[i]

            #--------------------

            time_start_on_hole = datetime.now()
            time_finish_on_hole = time_start_on_hole + timedelta(minutes=minutes, seconds=5)  # -1 по умочанию
            time_minute = datetime.now().time().minute
            message = f'STARTING TRIP ON HOLE -> {i} from {time_start_on_hole.strftime("%H:%M:%S")} to {time_finish_on_hole.strftime("%H:%M:%S")}'
            self.log_to_file(message)
            print(message)

            # ---------------------------------------------------------
            steps = int(minutes * 50) #  35 -------------------------------------------------------------------------------
            print(f"-------------------------- STEP TIME {steps} -----------------------------------------------")

            for step_patch in (current_patch := self.get_intermediate_coordinates(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i], steps))[5:-5]:  # добавил срез для смещения к центру лунки
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
                        message = f'FINISHING TRIP ON HOLE --> {i} at {datetime.now().strftime("%H:%M:%S")}'
                        self.log_to_file(message)
                        print(message)
                        lat, lng = current_patch[-1]
                        self.send_adb_command(ip_device, f"{lat}, {lng}")
                    break


generator = IntermediateCoordinatesGenerator()

print()
print(f"START GAME - -----------------------------------------------------------------------------------------")
generator.log_to_file(f'the game started at {datetime.now().strftime("%H:%M:%S")}')
# generator.get_start_coordinates(1)
# generator.run_device(6)
generator.run_device_by_time()
generator.get_start_coordinates(4)
print()
generator.log_to_file(f'the game finished at {datetime.now().strftime("%H:%M:%S")}')
print(f'FINISH GAME ------------------------------------------------------------------------------------------')
